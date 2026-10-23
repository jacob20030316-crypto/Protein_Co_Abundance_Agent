# Conserved co-abundance modules: breast and rectum

## Module 0

**Tissue pair**: breast and rectum  
**Genes (7)**: ALDH1A2, FAM3C, MYO1E, NOP56, PARP4, RSL1D1, SLC25A13

### Function

The module does not have a statistically supported GO or KEGG functional theme: no GO or KEGG term passed global multiple-testing correction. Its structure is therefore more informative than enrichment. ALDH1A2 is the central co-abundance hub, connecting MYO1E, NOP56, PARP4, FAM3C, and SLC25A13. These genes span retinoic-acid biosynthesis, nucleolar RNA processing, actin-based cellular organization, poly-ADP-ribosylation and DNA-damage-related processes, secreted signaling, and mitochondrial solute transport. This is a heterogeneous module rather than a well-established canonical pathway. A cautious interpretation is a shared cellular-state or tissue-composition signal with a possible retinoic-acid-centered component, not a demonstrated unified biochemical complex.

**Cell composition.** All module proteins are detected in both breast and rectum, so the module is technically observable in both tissues. Most genes have low tissue specificity, while several show enhanced specificity in particular cell types. Neutrophils recur among the enriched cell annotations, and additional annotations include stromal cells, colonocytes, enterocytes, mast cells, podocytes, hepatocytes, and B-cell populations. One gene, FAM3C, is secreted in other tissues; the remaining genes are not classified as secreted. The combination of broad tissue detection, multiple cell-type-enhanced genes, and immune-cell annotations means that shared blood or stromal-cell representation could contribute substantially to the co-abundance pattern. The data do not support describing the module as a plasma-protein module or as a uniform housekeeping module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship is the NOP56–RSL1D1 pair. NOP56 is a nucleolar ribonucleoprotein involved in ribosomal RNA processing, whereas RSL1D1 is associated with the nucleolus and regulation of apoptosis and cellular senescence. No other module pair has a high-confidence STRING interaction, and no hu.MAP complex contains multiple module members. Thus, the NOP56–RSL1D1 edge is established interaction evidence, but the remaining co-abundance edges are not supported by known physical interaction evidence in these resources. The network is better interpreted as coordinated abundance or shared cellular composition than as a single experimentally established protein complex.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: NOP56–RSL1D1 (0.991)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact co-abundance grouping may be a potentially new observation because most of its edges are absent from the supplied STRING and hu.MAP evidence. However, database absence does not establish biological novelty. The lack of globally significant GO or KEGG enrichment, the mixed subcellular functions, and the presence of only one known high-confidence interaction make a claim of a new mechanistic pathway premature. The strongest defensible novelty claim is that this particular cross-tissue co-abundance pattern warrants validation. Independent cohorts, cell-composition adjustment, perturbation experiments, and comparison with existing transcriptomic or proteomic modules would be needed before calling it a novel conserved module.

**Hypothesis.** Hypothesis: the module reflects a shared stromal or immune-associated cellular state in breast and rectum in which ALDH1A2-mediated local retinoic-acid production is coordinated with mitochondrial substrate transport, cytoskeletal or membrane organization, secreted signaling, and stress or inflammatory responses. In parallel, NOP56 and RSL1D1 may mark a nucleolar RNA-processing and cellular-state component. The proposed mechanism is functional coordination or co-occurrence within particular cell populations, not direct physical assembly of all module proteins. This hypothesis predicts that the ALDH1A2-centered pattern will weaken after careful adjustment for neutrophil, stromal, and other shared cell populations, whereas a genuine cell-intrinsic mechanism should remain detectable in purified or single-cell-matched material.

Web sources: https://en.wikipedia.org/wiki/ALDH1A2

### Important genes

#### ALDH1A2

- **Related proteins** (co-abundance neighbors): MYO1E (0.85), NOP56 (0.83), PARP4 (0.83), FAM3C (0.82), SLC25A13 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in breast, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 1 family member A2. This protein belongs to the aldehyde dehydrogenase family of proteins. The product of this gene is an enzyme that catalyzes the synthesis of retinoic acid (RA) from retinaldehyde. Retinoic acid, the active derivative of vitamin A (retinol), is a hormonal signaling molecule that functions in developing and adult tissues. The studies of a similar mouse gene suggest that this enzyme and the cytochrom…
- **Diseases (Open Targets)**: diaphragmatic hernia 4, with cardiovascular defects (0.704); osteoarthritis, hand (0.464); osteoarthritis, knee (0.462); Knee pain (0.366); alcohol drinking (0.352)
- **Europe PMC papers**: 3482
- **Why important**: ALDH1A2 is the network hub, with the greatest connectivity and weighted strength in the module. It encodes an enzyme that synthesizes retinoic acid from retinaldehyde, linking the module to a biologically consequential signaling metabolite. Its tissue and cell annotations point toward reproductive or stromal contexts, mesothelial cells, hepatocytes, and neutrophils. It also has the largest literature volume among the selected genes and disease associations involving developmental abnormalities and osteoarthritis.
- **Conclusion**: Established evidence supports ALDH1A2 as the best functional anchor and the most influential network gene. The module data do not establish that retinoic-acid signaling drives the entire module. A retinoic-acid-centered interpretation remains a hypothesis requiring direct retinoid measurements, enzyme-activity assessment, and cell-type-resolved validation.

#### NOP56

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.83), ALDH1A2 (0.83); STRING partners: RSL1D1 (0.991)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in breast, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NOP56 ribonucleoprotein. Nop56p is a yeast nucleolar protein that is part of a complex with the nucleolar proteins Nop58p and fibrillarin. Nop56p is required for assembly of the 60S ribosomal subunit and is involved in pre-rRNA processing. The protein encoded by this gene is similar in sequence to Nop56p and is also found in the nucleolus. Expansion of a GGCCTG repeat from 3-8 copies to 1500-2500 copies in an intron of th…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 36 (0.586); neurodegenerative disease (0.495); ovarian neoplasm (0.272); hereditary disease (0.193); cerebellar ataxia (0.121)
- **Europe PMC papers**: 1517
- **Why important**: NOP56 is part of the only high-confidence STRING pair in the module, interacting with RSL1D1. It is a nucleolar protein involved in pre-ribosomal RNA processing and ribosome biogenesis, giving the module a plausible RNA-processing or proliferative-state component. It has substantial literature support and a disease association with spinocerebellar ataxia type thirty-six.
- **Conclusion**: Established evidence supports NOP56 as a nucleolar RNA-processing marker and as a known partner of RSL1D1. Its connection to ALDH1A2 in the co-abundance graph is not an established physical interaction, so any proposed link between retinoic-acid biology and nucleolar processing is hypothetical.

#### RSL1D1

- **Related proteins** (co-abundance neighbors): NOP56 (0.83); STRING partners: NOP56 (0.991)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in breast, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal L1 domain containing 1. Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in regulation of apoptotic process and regulation of cellular senescence. Acts upstream of or within regulation of protein localization. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.219); hepatocellular carcinoma (0.099); neoplasm (0.099); colorectal carcinoma (0.096); insomnia (0.078)
- **Europe PMC papers**: 381
- **Why important**: RSL1D1 is the direct STRING partner of NOP56 and is localized to the nucleolar rim and mitotic chromosome. Its annotations include regulation of apoptosis, cellular senescence, and protein localization, which could make it informative about cellular state even though it is not a hub. Its literature volume is more limited than that of the other selected genes, making it a useful but relatively understudied component.
- **Conclusion**: Established evidence supports a NOP56–RSL1D1 nucleolar relationship and a possible connection to senescence or apoptosis-related state. The module does not demonstrate that RSL1D1 mediates the broader ALDH1A2-centered pattern; that role is a hypothesis.

#### SLC25A13

- **Related proteins** (co-abundance neighbors): ALDH1A2 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in breast, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 13. This gene is a member of the mitochondrial carrier family. The encoded protein contains four EF-hand Ca(2+) binding motifs in the N-terminal domain, and localizes to mitochondria. The protein catalyzes the exchange of aspartate for glutamate and a proton across the inner mitochondrial membrane, and is stimulated by calcium on the external side of the inner mitochondrial membrane. Mutations in this…
- **Diseases (Open Targets)**: neonatal intrahepatic cholestasis due to citrin deficiency (0.804); citrullinemia type II (0.756); citrin deficiency (0.652); citrullinemia (0.649); citrullinemia type I (0.464)
- **Europe PMC papers**: 1421
- **Why important**: SLC25A13 is the module member with liver-enriched tissue annotation and mitochondrial localization. It transports aspartate, glutamate, and protons across the inner mitochondrial membrane and is associated with citrin deficiency and citrullinemia type two. Its connection to the ALDH1A2 hub may indicate that cellular metabolic state contributes to the shared abundance pattern.
- **Conclusion**: Established evidence supports SLC25A13 as a mitochondrial transport protein with a strong metabolic and disease-relevant function. The module does not show that its transport activity is coupled to ALDH1A2 or retinoic-acid synthesis. Such metabolic coupling is a testable hypothesis rather than a demonstrated mechanism.

#### FAM3C

- **Related proteins** (co-abundance neighbors): ALDH1A2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in breast, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FAM3 metabolism regulating signaling molecule C. This gene is a member of the family with sequence similarity 3 (FAM3) family and encodes a secreted protein with a GG domain. A change in expression of this protein has been noted in pancreatic cancer-derived cells. [provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: osteoporosis (0.469); Abnormality of the skeletal system (0.406); bone disorder (0.405); upper extremity fracture (0.353); bone fracture (0.338)
- **Europe PMC papers**: 816
- **Why important**: FAM3C is directly connected to the ALDH1A2 hub and is the only module gene classified as secreted in other tissues. It is a Golgi-associated protein described as a secreted signaling molecule, with cell annotations involving enterocytes, parietal cells, and memory and naive B-cell populations. Its disease associations include osteoporosis and skeletal-system abnormalities, and it has a moderate literature base.
- **Conclusion**: Established evidence supports FAM3C as a secreted or secretory-pathway signaling component that may report epithelial or B-cell-associated biology. The module does not establish that FAM3C communicates with ALDH1A2 or that its secretion creates the cross-tissue module. That paracrine interpretation remains hypothetical.

## Module 1

**Tissue pair**: breast and rectum  
**Genes (5)**: COL1A1, COL1A2, COL6A1, COL6A2, COL6A3

### Function

This is a highly coherent extracellular-matrix collagen module. The primary evidence is exceptionally consistent: every module gene contributes to the globally corrected tensile-strength extracellular-matrix term (GO:MF extracellular matrix structural constituent conferring tensile strength; q_global = 1.74e-07), the collagen-trimer term (GO:CC collagen trimer; q_global = 5.85e-07), protein digestion and absorption (KEGG Protein digestion and absorption - Homo sapiens (human); q_global = 9.63e-07), ECM-receptor interaction (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 8.01e-06), and related extracellular-matrix, focal-adhesion, integrin, collagen-fibril, growth-factor-binding, and collagen-metabolism terms (25 globally significant GO/KEGG terms, q_global 2.5e-05–0.0275; see the table). The most direct interpretation is coordinated production and organization of type I and type VI collagen in structural extracellular matrix. The pathway labels involving PI3K–Akt, focal adhesion, integrin signaling, and cytoskeletal responses are compatible with matrix-mediated cell adhesion and signaling, but they should not be read as evidence that the module contains intracellular pathway components. The human papillomavirus and protein-digestion labels are pathway-overlap annotations rather than specific evidence that this module mediates infection or digestion. STRING supplementary results independently support collagen triple helices, trimerization, fibril assembly, collagen degradation, and ECM organization (15 supplementary STRING terms; within-query FDR 1.03e-08–5.5e-07).

**Cell composition.** All module genes are secreted extracellular-matrix proteins according to HPA, so this is not a plasma-protein or conventional housekeeping module. HPA assigns the genes mainly to stromal and fibroblast-related cell types, including decidual stromal cells, endometrial stromal cells, fibroblasts, fibro-adipogenic progenitors, and hepatic stellate cells. The shared breast–rectum signal therefore most plausibly reflects conserved stromal or fibroblast-associated matrix biology, or variation in stromal content, rather than blood contamination. Most genes are not detected in immune cells; COL6A2 has group enrichment in several T-cell categories, but this isolated blood-cell annotation does not outweigh the coherent extracellular-matrix and stromal pattern. Protein detection is present for part of the module in both breast and rectum, while the lack of immunohistochemical detection for some genes does not negate transcript or secretome-based module membership.

**GO/KEGG enrichment**: 29 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF extracellular matrix structural constituent conferring tensile strength | 1.74e-07 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| GO:CC collagen trimer | 5.85e-07 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| KEGG Protein digestion and absorption - Homo sapiens (human) | 9.63e-07 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| KEGG ECM-receptor interaction - Homo sapiens (human) | 8.01e-06 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| GO:CC complex of collagen trimers | 2.5e-05 | COL1A1, COL1A2, COL6A1, COL6A3 |
| KEGG PI3K-Akt signaling pathway - Homo sapiens (human) | 3.56e-05 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| KEGG Focal adhesion - Homo sapiens (human) | 9.51e-05 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| KEGG Integrin signaling - Homo sapiens (human) | 9.51e-05 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| GO:MF extracellular matrix structural constituent | 0.000126 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| KEGG Human papillomavirus infection - Homo sapiens (human) | 0.000126 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| GO:CC external encapsulating structure | 0.000164 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| GO:CC extracellular matrix | 0.000164 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| KEGG Cytoskeleton in muscle cells - Homo sapiens (human) | 0.000572 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |
| GO:MF platelet-derived growth factor binding | 0.000654 | COL1A1, COL1A2, COL6A1 |
| GO:CC endoplasmic reticulum lumen | 0.000686 | COL1A1, COL1A2, COL6A1, COL6A2, COL6A3 |

### STRING and hu.MAP

STRING reports high-confidence relationships for every possible gene pair in the module. These links are biologically expected because COL1A1 and COL1A2 form type I collagen, while COL6A1, COL6A2, and COL6A3 form type VI collagen; the complete pairwise network is therefore consistent with shared collagen assembly, matrix organization, and functional co-occurrence rather than independent associations. STRING enrichment supports collagen triple-helix repeats, collagen trimerization, fibril assembly, collagen degradation, ECM proteoglycans, and ECM-receptor interaction (15 supplementary STRING terms; within-query FDR 1.03e-08–5.5e-07). hu.MAP provides multiple complexes containing COL1A1 and COL1A2 (hu.MAP huMAP3_02141.1) (hu.MAP huMAP3_06460.1) (hu.MAP huMAP3_07562.1) (hu.MAP huMAP3_02069.1) (hu.MAP huMAP3_10780.1) (hu.MAP huMAP3_09231.1) (hu.MAP huMAP3_09523.1) (hu.MAP huMAP3_09606.1) (hu.MAP huMAP3_10652.1) (hu.MAP huMAP3_14070.1), but each reported complex contains only these two module members and includes varying non-module proteins. Thus hu.MAP supports known physical or complex-associated biology for the type I collagen pair, but does not establish a single experimentally defined complex containing all five module genes. COL6A1, COL6A2, and COL6A3 have no listed hu.MAP complexes in the supplied evidence.

**STRING interactions (score >= 0.7)**: 10 of 10 gene pairs: COL1A1–COL1A2 (0.999); COL1A1–COL6A1 (0.969); COL1A1–COL6A2 (0.954); COL1A1–COL6A3 (0.974); COL1A2–COL6A1 (0.875); COL1A2–COL6A2 (0.908); COL1A2–COL6A3 (0.968); COL6A1–COL6A2 (0.998); COL6A1–COL6A3 (0.994); COL6A2–COL6A3 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Banded collagen fibril, and FACIT collagen trimer (FDR = 1.03e-08, 5 genes); Pfam Collagen triple helix repeat (20 copies) (FDR = 1.65e-08, 5 genes); Function Extracellular matrix structural constituent conferring tensile strength (FDR = 2.61e-08, 5 genes); Keyword Collagen (FDR = 2.97e-08, 5 genes); RCTM Collagen chain trimerization (FDR = 3.99e-08, 5 genes); KEGG Protein digestion and absorption (FDR = 4.22e-08, 5 genes); RCTM Collagen degradation (FDR = 4.74e-08, 5 genes); RCTM Assembly of collagen fibrils and other multimeric structures (FDR = 6.19e-08, 5 genes); InterPro Collagen triple helix repeat (FDR = 1e-07, 5 genes); Component Collagen trimer (FDR = 1.29e-07, 5 genes); KEGG ECM-receptor interaction (FDR = 1.87e-07, 5 genes); HPO Atrophic scars (FDR = 2.59e-07, 5 genes); RCTM ECM proteoglycans (FDR = 2.93e-07, 5 genes); Keyword Hydroxylation (FDR = 4.81e-07, 5 genes); HPO Dermal atrophy (FDR = 5.5e-07, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02141.1 (COL1A1, COL1A2; 2/3); huMAP3_06460.1 (COL1A1, COL1A2; 2/3); huMAP3_07562.1 (COL1A1, COL1A2; 2/3); huMAP3_02069.1 (COL1A1, COL1A2; 2/4); huMAP3_10780.1 (COL1A1, COL1A2; 2/5); huMAP3_09231.1 (COL1A1, COL1A2; 2/6); huMAP3_09523.1 (COL1A1, COL1A2; 2/6); huMAP3_09606.1 (COL1A1, COL1A2; 2/6); huMAP3_10652.1 (COL1A1, COL1A2; 2/6); huMAP3_14070.1 (COL1A1, COL1A2; 2/8)

### Novelty

The module is not a convincing discovery of a previously unknown collagen interaction or function. Its genes, pairwise STRING relationships, collagen annotations, and type I/type VI assembly roles are already well established, and the enrichment results largely recapitulate canonical collagen biology. What may still be novel is the observation that this particular coordinated collagen program is conserved as a co-abundance module across breast and rectum, especially if the cross-tissue comparison and dataset context were not previously reported. That claim requires comparison with prior tissue co-abundance studies and independent replication. Absence from hu.MAP for the type VI genes is not evidence of novelty, because database coverage and complex definitions are incomplete.

**Hypothesis.** Hypothesis: the shared module represents a conserved stromal fibroblast matrix-production program in breast and rectum. Coordinated synthesis of type I collagen through COL1A1 and COL1A2, together with type VI collagen through COL6A1, COL6A2, and COL6A3, could assemble fibrillar and beaded-filament matrix, influence basement-membrane/interstitial-matrix organization, and alter integrin or growth-factor-dependent signaling in neighboring epithelial, vascular, or stromal cells. The co-abundance pattern may therefore reflect shared stromal abundance or activation across the tissues rather than a novel signaling pathway. This hypothesis should be tested with spatial or single-cell localization, independent cohorts, and measurements of matrix deposition and cell–matrix signaling.

### Important genes

#### COL1A1

- **Related proteins** (co-abundance neighbors): COL1A2 (0.92), COL6A3 (0.85), COL6A1 (0.85); STRING partners: COL1A2 (0.999), COL6A1 (0.969), COL6A2 (0.954), COL6A3 (0.974)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in breast, rectum
- **hu.MAP 3.0**: huMAP3_02141.1, huMAP3_06460.1, huMAP3_07562.1, huMAP3_02069.1, huMAP3_10780.1, huMAP3_09231.1, huMAP3_09523.1, huMAP3_09606.1, huMAP3_10652.1, huMAP3_14070.1
- **Function (MyGene.info)**: collagen type I alpha 1 chain. This gene encodes the pro-alpha1 chains of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIA, Ehlers-Danlos syndrome Classical type,…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.847); osteogenesis imperfecta type 4 (0.837); osteogenesis imperfecta type 3 (0.835); osteogenesis imperfecta type 1 (0.834); osteogenesis imperfecta (0.808)
- **Europe PMC papers**: 45548
- **Why important**: COL1A1 is a central network member with strong links to every other module gene and is part of the type I collagen trimer with COL1A2. It contributes to essentially all major globally corrected collagen and extracellular-matrix terms (13 globally significant GO/KEGG terms, q_global 1.74e-07–0.000572; see the table), (5 globally significant GO/KEGG terms, q_global 0.000686–0.0106; see the table), and (5 globally significant GO/KEGG terms, q_global 0.0146–0.0275; see the table). HPA places it in extracellular matrix and fibroblast- or stromal-associated cell types, while the supplied disease evidence connects it to osteogenesis imperfecta and related connective-tissue disorders. Its large literature base and direct structural role make it a primary marker of the module.
- **Conclusion**: Established evidence supports COL1A1 as a core type I collagen structural gene and a major indicator of stromal extracellular-matrix production. The module data do not establish that COL1A1 initiates the cross-tissue program or that it is a therapeutic driver; those would remain hypotheses.

#### COL1A2

- **Related proteins** (co-abundance neighbors): COL6A3 (0.92), COL1A1 (0.92), COL6A1 (0.85); STRING partners: COL1A1 (0.999), COL6A1 (0.875), COL6A2 (0.908), COL6A3 (0.968)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in breast, rectum
- **hu.MAP 3.0**: huMAP3_02141.1, huMAP3_06460.1, huMAP3_07562.1, huMAP3_02069.1, huMAP3_10780.1, huMAP3_09231.1, huMAP3_09523.1, huMAP3_09606.1, huMAP3_10652.1, huMAP3_14070.1
- **Function (MyGene.info)**: collagen type I alpha 2 chain. This gene encodes the pro-alpha2 chain of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIB, recessive Ehlers-Danlos syndrome Classi…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.845); osteogenesis imperfecta type 3 (0.830); osteogenesis imperfecta type 4 (0.820); Ehlers-Danlos syndrome, cardiac valvular type (0.777); osteogenesis imperfecta type 1 (0.770)
- **Europe PMC papers**: 67901
- **Why important**: COL1A2 has strong links to COL1A1 and all type VI collagen members, is present in every listed hu.MAP complex for the module, and contributes to the type I collagen trimer. It appears across the globally corrected collagen, ECM, focal-adhesion, integrin, growth-factor-binding, and collagen-organization terms (29 globally significant GO/KEGG terms, q_global 1.74e-07–0.0275; see the table). HPA detects its protein in both breast and rectum and associates it with stromal cell types and several tissue-enhanced contexts. Its extensive disease and literature evidence includes osteogenesis imperfecta, Ehlers–Danlos syndromes, osteoporosis, and atypical Marfan syndrome.
- **Conclusion**: Established evidence supports COL1A2 as the most direct type I collagen partner of COL1A1 and as a strong cross-tissue stromal matrix marker. Its repeated hu.MAP appearance indicates known complex-associated biology, not a newly discovered complex or a demonstrated causal role in this module.

#### COL6A1

- **Related proteins** (co-abundance neighbors): COL6A2 (0.95), COL6A3 (0.88), COL1A1 (0.85), COL1A2 (0.85); STRING partners: COL1A1 (0.969), COL1A2 (0.875), COL6A2 (0.998), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is a highly connected type VI collagen member with strong STRING relationships to all other module genes and the greatest weighted connectivity among the type VI genes. It participates broadly in the globally corrected terms, including collagen trimer, ECM-receptor interaction, focal adhesion, integrin signaling, growth-factor binding, collagen metabolism, and collagen fibril organization (19 globally significant GO/KEGG terms, q_global 1.74e-07–0.0106; see the table) and (9 globally significant GO/KEGG terms, q_global 0.0109–0.0275; see the table). HPA links it to fibroblasts and stromal populations and identifies secretion to extracellular matrix. The supplied disease associations include Bethlem myopathy, Ullrich congenital muscular dystrophy, and collagen six-related myopathy.
- **Conclusion**: Established evidence supports COL6A1 as a central structural component of type VI collagen and a bridge between the type I and type VI collagen portions of the network. Its network centrality suggests importance for module coherence, but does not prove that it regulates the other genes.

#### COL6A3

- **Related proteins** (co-abundance neighbors): COL1A2 (0.92), COL6A2 (0.89), COL6A1 (0.88), COL1A1 (0.85); STRING partners: COL1A1 (0.974), COL1A2 (0.968), COL6A1 (0.994), COL6A2 (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 3 chain. This gene encodes the alpha-3 chain, one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The alpha-3 chain of type VI collagen is much larger than the alpha-1 and -2 chains. This difference in size is largely due to an increase in the number of subdomains, similar to von Willebrand Factor type A domains, that are found in the amino termin…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy (0.766); dystonia 27 (0.764); Bethlem myopathy (0.758); Bethlem myopathy 1C (0.747); Bethlem myopathy 1A (0.718)
- **Europe PMC papers**: 5386
- **Why important**: COL6A3 has the highest weighted connectivity in the module and strong STRING relationships with every other gene. It encodes the larger alpha three chain of type VI collagen, whose additional domains can bind extracellular-matrix components. It contributes to the globally corrected collagen-trimer and ECM terms (13 globally significant GO/KEGG terms, q_global 1.74e-07–0.000572; see the table), (GO:CC endoplasmic reticulum lumen; q_global = 0.000686), and (5 globally significant GO/KEGG terms, q_global 0.0109–0.0146; see the table). HPA associates it with smooth muscle, fibroblast-related and stromal cell types, and secretion to extracellular matrix. The supplied disease evidence includes Ullrich congenital muscular dystrophy, dystonia, and Bethlem myopathy, with substantial literature support.
- **Conclusion**: Established evidence supports COL6A3 as a structurally important and highly connected type VI collagen component, potentially helping organize matrix interfaces through its larger extracellular domains. The module alone does not demonstrate that its high network position reflects biochemical control rather than shared collagen biology.

#### COL6A2

- **Related proteins** (co-abundance neighbors): COL6A1 (0.95), COL6A3 (0.89); STRING partners: COL1A1 (0.954), COL1A2 (0.908), COL6A1 (0.998), COL6A3 (0.994)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Cytosol; IHC detected in breast, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 2 chain. This gene encodes one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The product of this gene contains several domains similar to von Willebrand Factor type A domains. These domains have been shown to bind extracellular matrix proteins, an interaction that explains the importance of this collagen in organizing matrix components. Mutation…
- **Diseases (Open Targets)**: Ullrich congenital muscular dystrophy 1B (0.770); Bethlem myopathy (0.755); Ullrich congenital muscular dystrophy (0.743); Bethlem myopathy 1B (0.723); Bethlem myopathy 1A (0.713)
- **Europe PMC papers**: 4115
- **Why important**: COL6A2 completes the type VI collagen chain set and is strongly connected to COL6A1 and COL6A3, with additional links to the type I collagen genes. It contributes to the principal collagen and ECM terms (13 globally significant GO/KEGG terms, q_global 1.74e-07–0.000572; see the table), (GO:CC endoplasmic reticulum lumen; q_global = 0.000686), and (GO:MF structural molecule activity; q_global = 0.0146). HPA identifies secretion to extracellular matrix and enrichment in fibroblast- and stromal-associated cell groups; it is also the only module gene with the supplied group-enriched blood-cell annotation. The disease evidence includes Bethlem myopathy and Ullrich muscular dystrophy, and its annotation describes domains that bind matrix proteins.
- **Conclusion**: Established evidence supports COL6A2 as an essential type VI collagen chain and matrix-organizing component. Its blood-cell annotation should be treated cautiously because the broader module is non-immune and stromal; the available evidence does not show that COL6A2 reflects a blood-derived signal in these tissues.

## Module 2

**Tissue pair**: breast and rectum  
**Genes (5)**: LAMB2, LAMC1, NID1, HSPG2, SORBS1

### Function

This module is a basement-membrane and extracellular-matrix program centered on laminin, nidogen, and perlecan biology. The primary evidence converges on basement-membrane organization, extracellular-matrix structure, cell-matrix adhesion, integrin-mediated signaling, and ECM-receptor interaction through (GO:BP regulation of basement membrane organization; q_global = 0.000184), (GO:BP positive regulation of integrin-mediated signaling pathway; q_global = 0.000654), (GO:CC basement membrane; q_global = 0.000809), (GO:CC protein complex involved in cell-matrix adhesion; q_global = 0.001), (GO:BP regulation of integrin-mediated signaling pathway; q_global = 0.001), (GO:BP basement membrane organization; q_global = 0.00532), (GO:BP regulation of extracellular matrix organization; q_global = 0.00773), (GO:MF extracellular matrix structural constituent; q_global = 0.00776), (GO:CC extracellular matrix; q_global = 0.0096), and (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0462). LAMB2, LAMC1, NID1, and HSPG2 form the principal structural matrix component, while SORBS1 provides a focal-adhesion and cytoskeletal connection. The muscle-cell differentiation terms (GO:BP positive regulation of muscle cell differentiation; q_global = 0.00145) and (GO:BP regulation of muscle cell differentiation; q_global = 0.00773) are compatible with vascular, stromal, or contractile-cell contexts but do not establish muscle specificity. Overall, the module indicates basement-membrane assembly and adhesion with potential effects on tissue architecture, cell attachment, and signaling.

**Cell composition.** The module is strongly extracellular and secretory rather than a housekeeping module. LAMB2, LAMC1, NID1, and HSPG2 are secreted to the extracellular matrix, whereas SORBS1 is associated with focal adhesion sites. HPA points toward vascular smooth muscle, adipose, fibro-adipogenic, hepatic stellate, and fibroblast-related stromal populations. This favors a vascular or stromal origin for the shared signal. The module is not predominantly blood-cell enriched because several genes are not detected in immune cells, although NID1 has group enrichment in monocyte and myeloid dendritic-cell populations and SORBS1 is immune-cell enriched in basophils. Blood or immune-cell carryover is therefore possible but is not the most coherent explanation. Protein detection in breast and rectum supports biological presence of much of the module, while the absence of NID1 immunohistochemical detection in those tissues cautions against assuming uniform local protein deposition.

**GO/KEGG enrichment**: 19 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP regulation of basement membrane organization | 0.000184 | LAMB2, LAMC1, NID1 |
| GO:BP positive regulation of integrin-mediated signaling pathway | 0.000654 | LAMB2, LAMC1, NID1 |
| GO:CC basement membrane | 0.000809 | HSPG2, LAMB2, LAMC1, NID1 |
| GO:CC protein complex involved in cell-matrix adhesion | 0.001 | LAMB2, LAMC1, NID1 |
| GO:BP regulation of integrin-mediated signaling pathway | 0.001 | LAMB2, LAMC1, NID1 |
| GO:BP positive regulation of muscle cell differentiation | 0.00145 | LAMB2, LAMC1, NID1 |
| GO:BP basement membrane organization | 0.00532 | LAMB2, LAMC1, NID1 |
| GO:BP regulation of muscle cell differentiation | 0.00773 | LAMB2, LAMC1, NID1 |
| GO:BP regulation of extracellular matrix organization | 0.00773 | LAMB2, LAMC1, NID1 |
| GO:MF extracellular matrix structural constituent | 0.00776 | HSPG2, LAMB2, LAMC1, NID1 |
| GO:CC external encapsulating structure | 0.0096 | HSPG2, LAMB2, LAMC1, NID1 |
| GO:CC extracellular matrix | 0.0096 | HSPG2, LAMB2, LAMC1, NID1 |
| GO:CC protein complex involved in cell adhesion | 0.0159 | LAMB2, LAMC1, NID1 |
| GO:BP glomerular basement membrane development | 0.026 | LAMB2, NID1 |
| GO:CC laminin-521 trimer | 0.026 | LAMB2, LAMC1 |

### STRING and hu.MAP

STRING supports a pre-existing basement-membrane interaction network. The supplied relationships include HSPG2 with NID1, LAMC1 with NID1, LAMB2 with LAMC1, HSPG2 with LAMC1, and LAMB2 with NID1. These relationships agree with the primary enrichment terms and with the basement-membrane and laminin annotations in (STRING NetworkNeighborAL Laminin IV, and G2 nidogen domain and fibulin; within-query FDR = 7.57e-06), (STRING Keyword Basement membrane; within-query FDR = 9.2e-06), (STRING RCTM Laminin interactions; within-query FDR = 5.73e-05), (STRING COMPARTMENTS Basement membrane; within-query FDR = 8.5e-05), (STRING NetworkNeighborAL laminin-1 complex, and G2 nidogen domain and fibulin; within-query FDR = 0.00023), (STRING Component Basement membrane; within-query FDR = 0.00026), (STRING Component Protein complex involved in cell-matrix adhesion; within-query FDR = 0.00039), (STRING COMPARTMENTS Laminin complex; within-query FDR = 0.00058), and (STRING Function Extracellular matrix structural constituent; within-query FDR = 0.0021). The domain and extracellular-matrix signals in (STRING Keyword Laminin EGF-like domain; within-query FDR = 0.00019), (STRING SMART Laminin-type epidermal growth factor-like domai; within-query FDR = 0.00023), (STRING InterPro EGF-like domain; within-query FDR = 0.00028), and (STRING InterPro Laminin-type EGF domain; within-query FDR = 0.00063) are supportive, but STRING enrichment is supplementary rather than globally corrected primary evidence. hu.MAP identifies LAMC1 and NID1 together in (hu.MAP huMAP3_14233.1), although that complex contains many proteins outside this module. SORBS1 has no supplied STRING partner and no hu.MAP assignment, so its connection may reflect co-abundance and focal-adhesion biology rather than a documented physical interaction.

**STRING interactions (score >= 0.7)**: 5 of 10 gene pairs: HSPG2–LAMC1 (0.82); HSPG2–NID1 (0.999); LAMB2–LAMC1 (0.962); LAMB2–NID1 (0.734); LAMC1–NID1 (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Laminin IV, and G2 nidogen domain and fibulin (FDR = 7.57e-06, 4 genes); Keyword Basement membrane (FDR = 9.2e-06, 4 genes); RCTM Laminin interactions (FDR = 5.73e-05, 4 genes); COMPARTMENTS Basement membrane (FDR = 8.5e-05, 4 genes); Keyword Laminin EGF-like domain (FDR = 0.00019, 3 genes); SMART Laminin-type epidermal growth factor-like domai (FDR = 0.00023, 3 genes); NetworkNeighborAL laminin-1 complex, and G2 nidogen domain and fibulin (FDR = 0.00023, 3 genes); Component Basement membrane (FDR = 0.00026, 4 genes); InterPro EGF-like domain (FDR = 0.00028, 4 genes); Component Protein complex involved in cell-matrix adhesion (FDR = 0.00039, 3 genes); COMPARTMENTS Laminin complex (FDR = 0.00058, 3 genes); InterPro Laminin-type EGF domain (FDR = 0.00063, 3 genes); COMPARTMENTS Protein complex involved in cell-matrix adhesion (FDR = 0.00084, 3 genes); COMPARTMENTS External encapsulating structure (FDR = 0.0013, 4 genes); Function Extracellular matrix structural constituent (FDR = 0.0021, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14233.1 (LAMC1, NID1; 2/14)

### Novelty

This should not be presented as a newly discovered molecular complex. The central relationships are already represented in STRING, LAMC1 and NID1 occur together in hu.MAP, and the functions of laminins, nidogen, and perlecan are well established. Absence of SORBS1 from STRING or hu.MAP does not prove novelty because database coverage is incomplete. The potentially novel observation is the conserved co-abundance of this basement-membrane program across breast and rectum, including its coupling to SORBS1. This is a hypothesis-generating systems-level finding, not proof of a new biochemical interaction or tissue-specific mechanism.

**Hypothesis.** Hypothesis: the shared module reflects coordinated production or remodeling of a vascular and stromal basement membrane in breast and rectum. LAMB2 and LAMC1 may assemble laminin structures, NID1 may organize or stabilize their linkage, and HSPG2 may provide a proteoglycan scaffold that cross-links matrix components and cell-surface signaling molecules. Integrin-associated adhesion could influence cell attachment, tissue architecture, and differentiation of vascular or smooth-muscle-related cells. SORBS1 may connect the matrix-associated adhesion state to intracellular cytoskeletal or insulin-responsive signaling. This is a mechanistic hypothesis; co-abundance and annotation evidence do not establish directionality, physical assembly, or causality.

### Important genes

#### LAMB2

- **Related proteins** (co-abundance neighbors): NID1 (0.86), SORBS1 (0.84), LAMC1 (0.83), HSPG2 (0.81); STRING partners: LAMC1 (0.962), NID1 (0.734)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit beta 2. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: LAMB2-related infantile-onset nephrotic syndrome (0.808); Pierson syndrome (0.797); nephrotic syndrome (0.496); eye disorder (0.434); synaptic congenital myasthenic syndrome (0.381)
- **Europe PMC papers**: 2504
- **Why important**: LAMB2 is the central hub of the module graph, connected to every other module gene, and appears in all primary GO and KEGG terms (GO:BP regulation of basement membrane organization; q_global = 0.000184) through (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0462). It is a laminin beta subunit and a core candidate for basement-membrane assembly, adhesion, integrin signaling, and muscle-cell differentiation. Its disease associations include Pierson syndrome and infantile-onset nephrotic syndrome. It also has substantial literature support and is detected in breast tissue.
- **Conclusion**: Established evidence identifies LAMB2 as the strongest network and annotation anchor. It is likely a principal structural contributor to the shared basement-membrane signal. A direct causal role in the co-abundance pattern remains a hypothesis.

#### LAMC1

- **Related proteins** (co-abundance neighbors): LAMB2 (0.83); STRING partners: HSPG2 (0.82), LAMB2 (0.962), NID1 (0.997)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in breast, rectum
- **hu.MAP 3.0**: huMAP3_14233.1
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is the laminin gamma subunit and is represented in the primary basement-membrane, adhesion, laminin-complex, and ECM-receptor terms. It has supplied STRING relationships with HSPG2, LAMB2, and NID1 and occurs with NID1 in hu.MAP complex (hu.MAP huMAP3_14233.1). It is detected in both breast and rectum, has the largest literature volume in the supplied evidence, and has disease associations including colorectal cancer and prostate carcinoma.
- **Conclusion**: Established evidence supports LAMC1 as a core laminin-network component linking the module to basement-membrane structure and cell-matrix signaling. Its detection in both tissues makes it a strong candidate for the conserved matrix program. Causality is not established.

#### NID1

- **Related proteins** (co-abundance neighbors): LAMB2 (0.86); STRING partners: HSPG2 (0.999), LAMB2 (0.734), LAMC1 (0.997)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14233.1
- **Function (MyGene.info)**: nidogen 1. This gene encodes a member of the nidogen family of basement membrane glycoproteins. The protein interacts with several other components of basement membranes, and may play a role in cell interactions with the extracellular matrix. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.425); focal epilepsy (0.259); Hemiparesis (0.259); Hydrocephalus (0.259); placental retention (0.233)
- **Europe PMC papers**: 1838
- **Why important**: NID1 is a basement-membrane glycoprotein that interacts with several matrix components. It participates in the primary organization, adhesion, integrin-signaling, and differentiation terms (GO:BP regulation of basement membrane organization; q_global = 0.000184) through (GO:BP glomerular basement membrane development; q_global = 0.026). It has strong supplied STRING relationships with HSPG2 and LAMC1 and shares hu.MAP complex (hu.MAP huMAP3_14233.1) with LAMC1. Its annotations point toward placental, fibroblastic, stromal, and some myeloid populations. It also has neurological and placental disease associations.
- **Conclusion**: Established evidence supports NID1 as an extracellular organizer of the laminin-rich basement-membrane network. Its lack of immunohistochemical detection in breast and rectum requires caution: it may mark matrix-producing cells at the transcript level without being uniformly deposited as protein.

#### HSPG2

- **Related proteins** (co-abundance neighbors): LAMB2 (0.81); STRING partners: LAMC1 (0.82), NID1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in breast, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 encodes perlecan, a multidomain extracellular proteoglycan that binds and cross-links matrix and cell-surface molecules. It contributes to the primary basement-membrane, extracellular-matrix, structural-constituent, and ECM-receptor terms (GO:CC basement membrane; q_global = 0.000809), (GO:MF extracellular matrix structural constituent; q_global = 0.00776), (GO:CC extracellular matrix; q_global = 0.0096), and (KEGG ECM-receptor interaction - Homo sapiens (human); q_global = 0.0462). STRING links it with NID1 and LAMC1, while HPA places it in blood-vessel and stromal or adipose-associated contexts. Its disease associations include Schwartz-Jampel syndrome and dyssegmental dysplasia, with substantial literature support.
- **Conclusion**: Established evidence supports HSPG2 as the proteoglycan scaffold component complementing the laminin and nidogen core. A role coupling matrix structure to growth-factor or receptor signaling in these tissues remains a mechanistic hypothesis.

#### SORBS1

- **Related proteins** (co-abundance neighbors): LAMB2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Focal adhesion sites; IHC detected in breast, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorbin and SH3 domain containing 1. This gene encodes a CBL-associated protein which functions in the signaling and stimulation of insulin. Mutations in this gene may be associated with human disorders of insulin resistance. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.454); atrial fibrillation (0.394); urinary system disorder (0.381); uterine corpus leiomyoma (0.351); hypertensive disorder (0.345)
- **Europe PMC papers**: 1367
- **Why important**: SORBS1 is connected to the central LAMB2 hub and is detected in both breast and rectum. HPA localizes it to focal adhesion sites and associates it with blood vessels, adipocytes, cardiomyocytes, and related cell types. MyGene.info links it to insulin signaling, cytoskeletal organization, cell-matrix adhesion, cell-substrate adhesion, and stress-fiber assembly. It has disease associations involving insulin resistance and cardiovascular or urinary-system disorders, despite lacking supplied STRING or hu.MAP support.
- **Conclusion**: Established evidence supports SORBS1 as a focal-adhesion and intracellular-signaling candidate that may connect the matrix program to cytoskeletal or metabolic responses. Its lack of documented STRING and hu.MAP relationships makes physical integration into the basement-membrane complex uncertain.
