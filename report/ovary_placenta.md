# Conserved co-abundance modules: ovary and placenta

## Module 0

**Tissue pair**: ovary and placenta  
**Genes (5)**: ANXA3, KRT18, KRT19, KRT7, KRT8

### Function

The module represents a simple epithelial intermediate-filament program. The primary global evidence is the enrichment of intermediate filament (GO:CC intermediate filament; q_global = 0.0405) and intermediate filament cytoskeleton (GO:CC intermediate filament cytoskeleton; q_global = 0.0405), both driven by KRT18, KRT19, KRT7, and KRT8. KRT8 and KRT18 are established heterotypic filament partners in simple epithelia, while KRT7 and KRT19 support the broader epithelial keratin network. The STRING supplementary results reinforce keratin, intermediate-filament, epithelial-cell, and carcinoma-related annotations (15 supplementary STRING terms; within-query FDR 0.0008–0.0133), but these are supplementary rather than globally corrected enrichment evidence.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. Its composition is strongly epithelial and cell-type restricted rather than broadly housekeeping-like. HPA links the genes especially to migrating cytotrophoblasts and extravillous trophoblasts, with additional associations to alveolar, intestinal, glandular, and other epithelial cell types. The module is detected at the protein level in placenta but is largely not detected in ovary, so the shared abundance pattern may reflect epithelial or trophoblast representation in the samples rather than equivalent protein expression in ovarian tissue. Blood-cell associations are mixed: some genes are immune-cell enriched or enhanced, while others are not detected in immune cells. This does not support a primarily blood-derived module, although cellular composition remains a possible contributor.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC intermediate filament | 0.0405 | KRT18, KRT19, KRT7, KRT8 |
| GO:CC intermediate filament cytoskeleton | 0.0405 | KRT18, KRT19, KRT7, KRT8 |

### STRING and hu.MAP

STRING supports a known keratin interaction core. KRT18–KRT8 is especially strongly supported, and KRT18–KRT19, KRT19–KRT8, KRT19–KRT7, and KRT7–KRT8 also meet the stated high-confidence interaction threshold. The STRING functional results repeatedly identify intermediate-filament and epithelial annotations (7 supplementary STRING terms; within-query FDR 0.0008–0.006) and (4 supplementary STRING terms; within-query FDR 0.0084–0.0091). ANXA3 is connected to KRT19 and KRT7 in the module graph but has no reported STRING partner in the fact sheet, making that part of the network less independently supported. No hu.MAP complex contains multiple module members. Thus, the network is best interpreted as a known keratin filament association pattern rather than evidence for a newly identified multiprotein complex.

**STRING interactions (score >= 0.7)**: 5 of 10 gene pairs: KRT18–KRT19 (0.928); KRT18–KRT8 (0.999); KRT19–KRT7 (0.701); KRT19–KRT8 (0.796); KRT7–KRT8 (0.746)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Mixed, incl. Signet ring cell adenocarcinoma, and Apical plasma membrane urothelial plaque (FDR = 0.0008, 4 genes); SMART Intermediate filament protein (FDR = 0.0015, 4 genes); Keyword Keratin (FDR = 0.003, 4 genes); Keyword Intermediate filament (FDR = 0.0032, 4 genes); DISEASES Carcinoma (FDR = 0.0035, 4 genes); InterPro Intermediate filament protein, conserved site (FDR = 0.006, 4 genes); InterPro Intermediate filament, rod domain (FDR = 0.006, 4 genes); TISSUES Colonic cancer cell (FDR = 0.0074, 5 genes); TISSUES Epithelial cell (FDR = 0.0084, 3 genes); TISSUES Squamous epithelium (FDR = 0.0084, 3 genes); COMPARTMENTS Intermediate filament (FDR = 0.0085, 4 genes); RCTM Formation of the cornified envelope (FDR = 0.0091, 4 genes); DISEASES Organ system cancer (FDR = 0.0107, 4 genes); DISEASES Reproductive system disease (FDR = 0.0133, 3 genes); DISEASES Reproductive organ cancer (FDR = 0.0133, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The biological program itself is unlikely to be a new discovery because the dominant genes are canonical epithelial keratins, their annotations describe established intermediate-filament functions, and several of their pairwise relationships are already supported by STRING. The absence of a hu.MAP complex or a STRING association for ANXA3 does not establish novelty. A potentially new aspect is the identification of this particular co-abundance pattern as conserved between ovary and placenta, but the fact sheet alone does not establish that this tissue-pair observation is novel relative to prior transcriptomic or proteomic studies. The conservative conclusion is that the module is a plausible tissue-shared epithelial or trophoblast signature, not a demonstrated novel molecular mechanism.

**Hypothesis.** Hypothesis: the shared module reflects coordinated representation of simple epithelial and trophoblast-like cells in ovary and placenta, with KRT8–KRT18 filaments forming the structural core and KRT7–KRT19 extending the epithelial cytoskeletal program. ANXA3 may mark a membrane-associated, migratory, vascular, or myeloid-related component linked to the keratin-positive cells, but its role in this module is not established by the reported STRING or hu.MAP evidence. This hypothesis should be tested using cell-composition estimates, spatial localization, and independent tissue-level protein or RNA measurements.

### Important genes

#### KRT19

- **Related proteins** (co-abundance neighbors): KRT8 (0.95), KRT7 (0.86), ANXA3 (0.85), KRT18 (0.85); STRING partners: KRT18 (0.928), KRT7 (0.701), KRT8 (0.796)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 19. The protein encoded by this gene is a member of the keratin family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. The type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains. Unlike its related family members, this smallest known ac…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.134); neoplasm (0.119); hereditary breast ovarian cancer syndrome (0.118); breast carcinoma (0.118); thyroid gland papillary carcinoma (0.117)
- **Europe PMC papers**: 6566
- **Why important**: KRT19 is the principal network hub, connecting to KRT8, KRT7, ANXA3, and KRT18. It participates in both globally significant intermediate-filament terms (GO:CC intermediate filament; q_global = 0.0405) and (GO:CC intermediate filament cytoskeleton; q_global = 0.0405), has extensive epithelial and trophoblast-related HPA annotations, and has the largest literature volume among the module genes in the fact sheet. Its disease associations include neoplastic and hereditary breast–ovarian cancer-related entries.
- **Conclusion**: Established evidence supports KRT19 as a central epithelial intermediate-filament component and the best network marker of the module. It is reasonable to use KRT19 as a representative marker of the shared epithelial program. Its hub position does not establish that KRT19 drives the cross-tissue conservation.

#### KRT8

- **Related proteins** (co-abundance neighbors): KRT19 (0.95), KRT18 (0.94); STRING partners: KRT18 (0.999), KRT19 (0.796), KRT7 (0.746)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Intermediate filaments; IHC detected in ovary, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 8. This gene is a member of the type II keratin family clustered on the long arm of chromosome 12. Type I and type II keratins heteropolymerize to form intermediate-sized filaments in the cytoplasm of epithelial cells. The product of this gene typically dimerizes with keratin 18 to form an intermediate filament in simple single-layered epithelial cells. This protein plays a role in maintaining cellul…
- **Diseases (Open Targets)**: cirrhosis of liver (0.596); cirrhosis, familial (0.401); neurodegenerative disease (0.371); prostate carcinoma (0.314); Abnormality of the liver (0.306)
- **Europe PMC papers**: 5942
- **Why important**: KRT8 is a core type two keratin with strong STRING support for its interaction with KRT18 and additional support for interactions with KRT19 and KRT7. It occurs in both primary global terms (GO:CC intermediate filament; q_global = 0.0405) and (GO:CC intermediate filament cytoskeleton; q_global = 0.0405), is detected in both ovary and placenta by HPA immunohistochemistry, and is associated with simple epithelial and extravillous trophoblast cell types. The fact sheet also links it to liver disease and carcinoma associations.
- **Conclusion**: Established evidence supports KRT8 as a structural core of simple epithelial intermediate filaments, especially through its partnership with KRT18. Its detection in both tissues makes it an important cross-tissue marker. A causal role in generating the co-abundance pattern remains hypothetical.

#### KRT18

- **Related proteins** (co-abundance neighbors): KRT8 (0.94), KRT19 (0.85); STRING partners: KRT19 (0.928), KRT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 18. KRT18 encodes the type I intermediate filament chain keratin 18. Keratin 18, together with its filament partner keratin 8, are perhaps the most commonly found members of the intermediate filament gene family. They are expressed in single layer epithelial tissues of the body. Mutations in this gene have been linked to cryptogenic cirrhosis. Two transcript variants encoding the same protein have bee…
- **Diseases (Open Targets)**: cirrhosis of liver (0.623); cirrhosis, familial (0.396); prostate carcinoma (0.140); neoplasm (0.117); breast carcinoma (0.113)
- **Europe PMC papers**: 6539
- **Why important**: KRT18 is the type one partner of KRT8 and has the strongest reported STRING support for that pair. It belongs to both primary global terms (GO:CC intermediate filament; q_global = 0.0405) and (GO:CC intermediate filament cytoskeleton; q_global = 0.0405), has broad simple-epithelial and trophoblast annotations, and is associated with intermediate-filament organization, cell–cell adhesion, apoptosis-related processes, and cirrhosis or neoplasm evidence. It also has a large literature base.
- **Conclusion**: Established evidence supports KRT18 as a central structural partner of KRT8 and a biologically meaningful component of the module. Its disease associations indicate clinical relevance but do not show that disease processes caused the tissue-shared module.

#### KRT7

- **Related proteins** (co-abundance neighbors): KRT19 (0.86), ANXA3 (0.84); STRING partners: KRT19 (0.701), KRT8 (0.746)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 7. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the simple epithelia lining the cavities of the internal organs and in th…
- **Diseases (Open Targets)**: neoplasm (0.118); lung carcinoma (0.105); cancer (0.102); lung cancer (0.099); colorectal carcinoma (0.099)
- **Europe PMC papers**: 3815
- **Why important**: KRT7 is included in both primary global intermediate-filament terms (GO:CC intermediate filament; q_global = 0.0405) and (GO:CC intermediate filament cytoskeleton; q_global = 0.0405), connects to KRT19 and ANXA3 in the module, and has STRING support for relationships with KRT19 and KRT8. HPA associates it with simple epithelia, glandular tissues, cytotrophoblasts, and extravillous trophoblasts. Its annotations and disease associations make it a useful marker of epithelial differentiation and carcinoma-related biology.
- **Conclusion**: Established evidence supports KRT7 as an epithelial intermediate-filament component that helps define the module beyond the KRT8–KRT18 pair. Its connection to ANXA3 is present in the module network, but the functional significance of that link is not established.

#### ANXA3

- **Related proteins** (co-abundance neighbors): KRT19 (0.85), KRT7 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A3. This gene encodes a member of the annexin family.  Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways.  This protein functions in the inhibition of phopholipase A2 and cleavage of inositol 1,2-cyclic phosphate to form inositol 1-phosphate. This protein may also play a role in anti-coagulation. […
- **Diseases (Open Targets)**: rheumatoid arthritis (0.318); Meniere disease (0.276); insomnia (0.255); hair color (0.209); refractive error (0.176)
- **Europe PMC papers**: 2243
- **Why important**: ANXA3 is the non-keratin member and provides a potentially distinct biological axis. It connects to KRT19 and KRT7 in the module, is associated with plasma-membrane localization, cytoskeletal or cell-migration-relevant functions, angiogenesis, neutrophil degranulation, and trophoblast or myeloid cell types. Unlike the keratins, it has no primary GO or KEGG term and no reported STRING partner in the fact sheet, while still having substantial literature volume.
- **Conclusion**: Established evidence supports ANXA3 as a membrane-associated annexin with roles in signaling, phospholipid biology, migration, angiogenesis, and immune-related processes. Its membership may indicate cellular heterogeneity or a membrane-associated extension of the epithelial program. A direct functional connection to the keratin core is a hypothesis rather than an established interaction.
