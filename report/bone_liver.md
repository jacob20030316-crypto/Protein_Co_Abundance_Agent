# Conserved co-abundance modules: bone and liver

## Module 0

**Tissue pair**: bone and liver  
**Genes (7)**: ABCF3, CTH, RAP1GDS1, GBE1, MVP, POR, PLS3

### Function

The module does not have a statistically supported unified GO or KEGG function: no term passed global correction, and there are no supplementary STRING-enrichment terms. Its genes nevertheless suggest a heterogeneous intracellular program involving hepatic metabolism, glycogen handling, redox and xenobiotic processing, actin organization, and intracellular signaling. RAP1GDS1 is the most connected node and links genes with otherwise different annotations, so the co-abundance pattern may reflect coordinated cellular state rather than a single canonical pathway. The evidence supports a liver-associated metabolic and structural module, but not a definitive pathway assignment.

**Cell composition.** The module is not composed of secreted or plasma proteins. Most genes have low immune-cell specificity, with only PLS3 showing a blood-cell-enriched pattern, so broad blood contamination is not the leading interpretation, although shared vascular or immune-related cellular contributions cannot be excluded. HPA tissue evidence is liver-centered: most module proteins are detected in liver, with CTH and POR showing liver tissue enrichment, while GBE1 is skeletal-muscle enhanced and PLS3 is blood-vessel enhanced. The single-cell annotations are heterogeneous and include hepatocytes, vascular or epithelial populations, muscle-related cells, neutrophils, and other specialized cell types. This supports a mixed intracellular module that may reflect shared cell states or common metabolic and structural demands in bone and liver rather than a bone-specific or liver-specific secretory program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes, no STRING functional-enrichment terms, and no hu.MAP complex containing multiple module members. Thus the co-abundance edges are not corroborated by the surveyed physical-interaction or curated-complex resources. The lack of support does not invalidate co-abundance, but it indicates that the module is primarily an expression-level association and should not be interpreted as a demonstrated protein complex or direct molecular interaction network.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a newly discovered biological mechanism. Its absence from STRING and hu.MAP indicates limited prior support for direct interactions or shared complexes, but database absence alone cannot establish novelty. The genes themselves have established functions and disease associations, especially CTH, POR, PLS3, GBE1, MVP, and RAP1GDS1. The potentially novel aspect is the coordinated co-abundance of this particular combination across bone and liver, but that claim requires independent replication, adjustment for cell composition, and comparison with existing co-expression and tissue-specific datasets.

**Hypothesis.** Hypothesis: the module may represent a shared intracellular adaptation linking hepatic metabolic capacity with cytoskeletal, vascular, and cellular stress programs. In this model, CTH, POR, and GBE1 contribute to sulfur, redox, xenobiotic, and glycogen-related metabolism; PLS3 contributes to actin organization and tissue architecture; MVP contributes to intracellular transport and signaling; and RAP1GDS1 may coordinate signaling or organelle-related responses across these processes. The cross-tissue co-abundance could arise from common metabolic demand, vascular or stromal contributions, or shared cell-state regulation rather than direct protein binding. This hypothesis is not established by the enrichment or interaction evidence.

### Important genes

#### RAP1GDS1

- **Related proteins** (co-abundance neighbors): CTH (0.90), PLS3 (0.84), POR (0.82), GBE1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rap1 GTPase-GDP dissociation stimulator 1. The smg GDP dissociation stimulator (smgGDS) protein is a stimulatory GDP/GTP exchange protein with GTPase activity (Riess et al., 1993 [PubMed 8262526]).[supplied by OMIM, Feb 2010].
- **Diseases (Open Targets)**: Alfadhel syndrome (0.430); carcinoma of liver and intrahepatic biliary tract (0.370); uterine carcinosarcoma (0.370); ovarian endometrioid adenocarcinoma with squamous differentiation (0.370); HER2 positive breast carcinoma (0.370)
- **Europe PMC papers**: 561
- **Why important**: RAP1GDS1 is the central network connector, linking CTH, PLS3, POR, and GBE1. Its annotated functions include regulation of mitochondrial organization, calcium-related processes, myosin filament assembly, vascular smooth-muscle contraction, and protein localization. It therefore provides a plausible regulatory bridge between the module's metabolic and structural components. Its disease links include Alfadhel syndrome and several cancers, while its literature volume is moderate relative to the extensively studied metabolic genes.
- **Conclusion**: Established evidence supports RAP1GDS1 as the network hub and as a regulator of signaling, organelle organization, and contractile or cytoskeletal processes. It is a candidate coordinator of the module, but a mechanistic role connecting all module genes remains a hypothesis because no STRING or hu.MAP relationship supports those direct connections.

#### CTH

- **Related proteins** (co-abundance neighbors): RAP1GDS1 (0.90), ABCF3 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cystathionine gamma-lyase. This gene encodes a cytoplasmic enzyme in the trans-sulfuration pathway that converts cystathione derived from methionine into cysteine. Glutathione synthesis in the liver is dependent upon the availability of cysteine. Mutations in this gene cause cystathioninuria. Alternative splicing of this gene results in three transcript variants encoding different isoforms. [provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: cystathioninuria (0.717); ankylosing spondylitis (0.303); hereditary disease (0.193); parasitic infectious disease (0.174); Cholecystitis (0.146)
- **Europe PMC papers**: 4159
- **Why important**: CTH is liver-enriched, detected in liver, and has a direct co-abundance connection to the network hub. It catalyzes a key step in transsulfuration and supports cysteine availability for hepatic glutathione synthesis. Its established associations include cystathioninuria and other disease links, and it has substantial literature support.
- **Conclusion**: Established evidence identifies CTH as a major hepatic sulfur-metabolism and redox-related enzyme. Its position adjacent to RAP1GDS1 supports its importance in the module's liver-associated metabolic interpretation, but the data do not show that CTH directly regulates the other module members.

#### POR

- **Related proteins** (co-abundance neighbors): RAP1GDS1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome p450 oxidoreductase. This gene encodes an endoplasmic reticulum membrane oxidoreductase that is essential for multiple metabolic processes, including reactions catalyzed by cytochrome P450 proteins for metabolism of steroid hormones, drugs and xenobiotics. The encoded protein has a flavin adenine dinucleotide (FAD)-binding domain and a flavodoxin-like domain which bind two cofactors, FAD and FMN, that allow it to dona…
- **Diseases (Open Targets)**: congenital adrenal hyperplasia due to cytochrome P450 oxidoreductase deficiency (0.834); Antley-Bixler syndrome with genital anomalies and disordered steroidogenesis (0.810); congenital adrenal hyperplasia (0.534); coffee consumption (0.446); Antley-Bixler syndrome without genital anomalies or disordered steroidogenesis (0.444)
- **Europe PMC papers**: 28661
- **Why important**: POR is liver tissue enhanced, detected in liver, and connected to RAP1GDS1. It supplies reducing equivalents to microsomal cytochrome P450 enzymes and is therefore relevant to steroid, drug, xenobiotic, fatty-acid, and related metabolic processes. It has extensive literature and well-established disease associations, including POR deficiency and Antley-Bixler syndrome.
- **Conclusion**: Established evidence supports POR as a strong marker of hepatic endoplasmic-reticulum redox and xenobiotic-metabolism capacity. Its inclusion strengthens the liver-metabolic interpretation, whereas its connection to RAP1GDS1 is a co-abundance relationship rather than evidence of direct biochemical interaction.

#### PLS3

- **Related proteins** (co-abundance neighbors): RAP1GDS1 (0.84), MVP (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plastin 3. Plastins are a family of actin-binding proteins that are conserved throughout eukaryote evolution and expressed in most tissues of higher eukaryotes. In humans, two ubiquitous plastin isoforms (L and T) have been identified. Plastin 1 (otherwise known as Fimbrin) is a third distinct plastin isoform which is specifically expressed at high levels in the small intestine. The L isoform is expressed on…
- **Diseases (Open Targets)**: X-linked osteoporosis with fractures (0.727); congenital diaphragmatic hernia (0.553); osteoporosis (0.477); hernia, anterior diaphragmatic (0.380); postmenopausal osteoporosis (0.341)
- **Europe PMC papers**: 1365
- **Why important**: PLS3 connects the network hub to MVP and is tissue enhanced in blood vessels. It encodes an actin-binding protein involved in actin-bundle and actin-network organization and has annotations related to bone development. Its blood-cell-enriched pattern and associations with osteoporosis and related skeletal disorders make it especially informative for a bone-and-liver module. It also has substantial literature support.
- **Conclusion**: Established evidence supports PLS3 as the module's principal cytoskeletal and bone-relevant component, with possible vascular or blood-cell contributions. Its role in linking structural biology to the metabolic genes is plausible but remains a hypothesis because interaction databases provide no corroboration.

#### GBE1

- **Related proteins** (co-abundance neighbors): RAP1GDS1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 1,4-alpha-glucan branching enzyme 1. The protein encoded by this gene is a glycogen branching enzyme that catalyzes the transfer of alpha-1,4-linked glucosyl units from the outer end of a glycogen chain to an alpha-1,6 position on the same or a neighboring glycogen chain. Branching of the chains is essential to increase the solubility of the glycogen molecule and, consequently, in reducing the osmotic pressure within cells. Highest l…
- **Diseases (Open Targets)**: glycogen storage disease due to glycogen branching enzyme deficiency (0.848); adult polyglucosan body disease (0.801); glycogen storage disease due to glycogen branching enzyme deficiency, adult neuromuscular form (0.711); glycogen storage disease due to glycogen branching enzyme deficiency, congenital neuromuscular form (0.591); disorder of glycogen metabolism (0.573)
- **Europe PMC papers**: 1361
- **Why important**: GBE1 is tissue enhanced in skeletal muscle, detected in liver, and connected to RAP1GDS1. It catalyzes glycogen branching, which is essential for glycogen solubility and cellular energy storage. Its highest expression in liver and muscle and its strong disease associations with glycogen storage and adult polyglucosan disorders make it a biologically informative metabolic member.
- **Conclusion**: Established evidence supports GBE1 as the module's glycogen and energy-storage component. Its presence is consistent with shared energy-management demands across tissues, but the module does not establish a direct regulatory relationship between GBE1 and RAP1GDS1 or the other genes.

## Module 1

**Tissue pair**: bone and liver  
**Genes (8)**: ADK, ALCAM, CLPB, GFM1, IDE, NRDC, NSF, OPA1

### Function

The module is best interpreted as a heterogeneous cellular maintenance and communication module, with emphasis on mitochondrial function, proteostasis, intracellular trafficking, peptide processing, and cell adhesion. The strongest network position belongs to GFM1, which connects mitochondrial translation with OPA1, NRDC, and NSF. The remaining links connect mitochondrial quality control and proteolysis to vesicle transport, adhesion, and purine metabolism. No GO or KEGG term passed global correction, so there is no globally significant pathway assignment. The individual gene annotations nevertheless support a biologically coherent theme of maintaining cellular energy production, protein quality, intracellular transport, and extracellular or intercellular signaling.

**Cell composition.** This is not predominantly a plasma or secreted-protein module and does not show a strong blood-cell signature. Most genes have low immune-cell specificity, although NRDC and CLPB show immune-cell-related enhancement involving myeloid dendritic cells. Two genes, IDE and ALCAM, have secreted annotations, with ALCAM reported in blood and IDE secreted in other tissues. The tissue and cell-type signals are diverse rather than concentrated: liver, skeletal muscle, brain, parathyroid gland, testis, epithelial populations, germ-cell populations, and neural populations are represented. Liver protein detection is broad across the module, whereas matching bone protein data are unavailable. Thus, the shared bone-liver signal may reflect broadly expressed cellular machinery, liver contribution, or shared cellular composition rather than a bone-liver-specific pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence pairwise interactions among the module genes. Its only supplementary functional signal is (STRING Pfam Middle or third domain of peptidase_M16; within-query FDR = 0.0484), linking IDE and NRDC through a peptidase-related domain annotation; this is not global enrichment and should not be treated as proof of pathway enrichment. No hu.MAP complex contains multiple module members. Therefore, the co-abundance relationships are not supported by a known high-confidence interaction network or a known shared complex. The module may reflect coordinated expression or protein abundance across tissues rather than direct physical binding. The internal topology still suggests possible bridges: GFM1 links several functional neighborhoods, while NRDC, NSF, and CLPB connect neighboring processes.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam Middle or third domain of peptidase_M16 (FDR = 0.0484, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module-level co-abundance pattern appears potentially novel because its specific relationships are absent from the supplied high-confidence STRING network and from hu.MAP multi-member complexes. However, database absence alone cannot establish novelty. The component genes and their individual functions are well established, particularly OPA1, NSF, IDE, ADK, CLPB, and GFM1, and several have substantial disease and literature support. A defensible conclusion is that the coordinated abundance pattern across bone and liver is a new or at least insufficiently characterized observation, requiring replication in independent cohorts and testing against tissue composition, cell-type abundance, and technical effects.

**Hypothesis.** Hypothesis: the module represents coordinated maintenance of metabolically active cells in which mitochondrial translation and dynamics, protein disaggregation, peptide turnover, vesicle recycling, adhesion, and purine salvage are jointly regulated. GFM1 and OPA1 may form the mitochondrial maintenance axis; CLPB and NRDC may contribute to protein quality control or proteolytic processing; NSF and ALCAM may reflect trafficking and cell-contact biology; and IDE and ADK may connect peptide signaling with nucleotide and energy metabolism. In bone and liver, the observed co-abundance could arise from shared metabolic stress responses or shared abundance of particular cell populations rather than direct physical assembly of all module proteins.

### Important genes

#### GFM1

- **Related proteins** (co-abundance neighbors): NRDC (0.85), OPA1 (0.84), NSF (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 has the strongest network position and connects three distinct neighbors, including OPA1, NRDC, and NSF. Its established role in mitochondrial translation makes it a plausible bridge between mitochondrial protein synthesis, organelle maintenance, and the broader cellular maintenance pattern. It is associated with combined oxidative-phosphorylation disorders and hepatoencephalopathy, and it has a substantial literature base.
- **Conclusion**: Established evidence supports GFM1 as a mitochondrial translation factor and as the central network connector in this module. It is a strong candidate for an organizing marker of the module. It remains a hypothesis that GFM1 causally coordinates the other module processes rather than merely covarying with them.

#### OPA1

- **Related proteins** (co-abundance neighbors): IDE (0.86), GFM1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 is directly connected to GFM1 and IDE and is a core regulator of mitochondrial inner-membrane organization, fusion, stability, and energy output. It also has the largest literature volume among the module genes and well-established associations with optic atrophy and mitochondrial disease.
- **Conclusion**: Established evidence supports OPA1 as a central mitochondrial dynamics and quality-control gene with strong disease relevance. Its position supports a mitochondrial component of the module, but the co-abundance data do not demonstrate that OPA1 physically interacts with every module component or drives the shared tissue signal.

#### NSF

- **Related proteins** (co-abundance neighbors): GFM1 (0.82), ALCAM (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-ethylmaleimide sensitive factor, vesicle fusing ATPase. Enables PDZ domain binding activity and ionotropic glutamate receptor binding activity. Involved in intracellular protein transport; positive regulation of protein catabolic process; and positive regulation of receptor recycling. Located in Golgi apparatus; cytosol; and plasma membrane. Implicated in developmental and epileptic encephalopathy. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy 96 (0.561); neurodegenerative disease (0.529); atrial fibrillation (0.310); Abnormality of the skeletal system (0.303); androgenetic alopecia (0.300)
- **Europe PMC papers**: 65784
- **Why important**: NSF connects GFM1 to ALCAM and is an established ATPase involved in vesicle-mediated transport, exocytosis, intra-Golgi transport, and receptor recycling. It has the largest literature volume in the module and is associated with developmental and epileptic encephalopathy and other neurological phenotypes.
- **Conclusion**: Established evidence supports NSF as a major intracellular trafficking and membrane-recycling factor. Its network position suggests that vesicle transport may connect mitochondrial or metabolic state to cell-surface signaling. That bridging interpretation is a hypothesis rather than a demonstrated molecular mechanism.

#### IDE

- **Related proteins** (co-abundance neighbors): OPA1 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin degrading enzyme. This gene encodes a zinc metallopeptidase that degrades intracellular insulin, and thereby terminates insulins activity, as well as participating in intercellular peptide signalling by degrading diverse peptides such as glucagon, amylin, bradykinin, and kallidin. The preferential affinity of this enzyme for insulin results in insulin-mediated inhibition of the degradation of other peptides such as…
- **Diseases (Open Targets)**: diabetes mellitus (0.307); type 2 diabetes mellitus (0.287); diabetic retinopathy (0.146); diabetic eye disease (0.144); brain cancer (0.142)
- **Europe PMC papers**: 19876
- **Why important**: IDE is connected to OPA1 and is a zinc metallopeptidase that degrades insulin and other signaling peptides. It provides a direct link between mitochondrial biology and peptide turnover, with relevance to insulin signaling, diabetes, protein catabolism, and neurodegenerative disease. It is also one of the genes contributing to the supplementary STRING signal (STRING Pfam Middle or third domain of peptidase_M16; within-query FDR = 0.0484).
- **Conclusion**: Established evidence supports IDE as an intracellular peptide-degrading enzyme with metabolic and signaling functions. Its association with OPA1 in the abundance network may indicate coordinated metabolic regulation, but it does not establish a direct IDE–OPA1 mechanism.

#### CLPB

- **Related proteins** (co-abundance neighbors): NRDC (0.81), ADK (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ClpB family mitochondrial disaggregase. This gene belongs to the ATP-ases associated with diverse cellular activities (AAA+) superfamily. Members of this superfamily form ring-shaped homo-hexamers and have highly conserved ATPase domains that are involved in various processes including DNA replication, protein degradation and reactivation of misfolded proteins. All members of this family hydrolyze ATP through their AAA+ domains and use …
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria with cataracts, neurologic involvement, and neutropenia (0.840); neutropenia, severe congenital, 9, autosomal dominant (0.788); 3-methylglutaconic aciduria, type VIIA (0.691); 3-methylglutaconic aciduria (0.665); hereditary disease (0.495)
- **Europe PMC papers**: 4069
- **Why important**: CLPB connects NRDC and ADK and encodes a mitochondrial disaggregase involved in handling misfolded proteins. Its annotations include granulocyte differentiation, heat response, antiviral innate immunity, and mitochondrial disease with neutropenia. Its tissue and single-cell signals are distinctive, including testis and late spermatids, while its liver protein detection supports its presence in the liver samples.
- **Conclusion**: Established evidence supports CLPB as a mitochondrial protein-quality-control factor with immune and inherited-disease relevance. Its position suggests a possible link between proteostasis and nucleotide or metabolic regulation through ADK. The interpretation that CLPB explains the shared bone-liver co-abundance pattern remains provisional because its cell-type-specific signals could also reflect sample composition.

## Module 2

**Tissue pair**: bone and liver  
**Genes (48)**: AFDN, AP1M1, CD2AP, CNOT1, CPNE1, CPSF6, DDX6, EPB41L2, ELOC, ELP1, GAR1, GMPPA, GCLM, HARS1, IRGQ, LBR, MAT2B, MDN1, MAP2K3, MTFP1, NDRG1, NDUFS2, NIBAN2, NIF3L1, NSUN2, ALDH18A1, PDXDC1, PDXP, PPM1F, PRRC1, RAI14, RAB3GAP2, UPF1, RPL6, POLR2B, SEC23IP, SHTN1, SNX6, SWAP70, FARSB, TTLL12, UBA5, UBTF, USP15, UCHL5, ATP6V1A, XPO1, TJP2

### Function

No GO or KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The gene-level evidence instead supports a heterogeneous cellular-maintenance module linking redox defense, RNA regulation, protein quality control, intracellular trafficking, epithelial junction organization, cytoskeletal signaling, and mitochondrial or translational functions. GCLM provides a glutathione-synthesis and oxidative-stress connection; DDX6 and UPF1 provide RNA decay, translation control, and surveillance connections; TJP2 and AFDN provide junction and adhesion biology; SEC23IP, AP1M1, ATP6V1A, and SNX6 support ER-to-Golgi, vesicular, endosomal, and organelle trafficking; and USP15, UCHL5, and UBA5 support ubiquitin-related regulation and proteostasis. The co-abundance structure therefore appears more consistent with a shared cellular state involving stress handling, RNA and protein turnover, membrane organization, and cell-type composition than with a single narrowly defined biochemical pathway. The lack of enriched GO or KEGG terms does not invalidate the module.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only one secreted gene, while the proteins represented are mainly intracellular, nuclear, cytosolic, vesicular, mitochondrial, or junctional. Most genes have low tissue specificity, which is compatible with broadly used cellular machinery rather than a specialized bone or liver program. There is nevertheless a possible cellular-composition contribution. HPA shows cell-type enhancement across several unrelated cell populations, including neutrophils, monocytes, B cells, erythrocyte progenitors, endothelial cells, epithelial cells, and spermatid populations. Immune-cell specificity is low for most genes, but a subset is immune-cell enhanced or enriched, especially among neutrophil and monocyte-associated annotations. Liver protein detection is common in the available HPA evidence, whereas bone protein evidence is unavailable. Thus, shared liver and bone abundance may partly reflect ubiquitous cellular programs and shared blood or stromal content, rather than a secreted plasma signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a small set of established physical or functional relationships within the module: AFDN--TJP2, CNOT1--DDX6, DDX6--UPF1, and UCHL5--USP15. These links independently reinforce junction organization, messenger-RNA turnover and surveillance, and ubiquitin-dependent regulation. STRING reports no functional-enrichment result for the module, so the network should not be presented as a STRING-enriched pathway. hu.MAP adds two partial complex overlaps. (hu.MAP huMAP3_05613.1) contains RAI14 and TJP2 among the module members, consistent with a junction or cytoskeletal-associated complex, while (hu.MAP huMAP3_13535.1) contains PRRC1 and SEC23IP, consistent with secretory-pathway or vesicle-related organization. Because each hu.MAP result contains only a minority of the corresponding complex members, these are supporting relationships rather than evidence that the whole module is one intact complex. Most co-abundance edges are not represented by the supplied high-confidence STRING or hu.MAP evidence, suggesting that co-abundance captures shared regulation, cell composition, or indirect coordination in addition to direct physical interaction.

**STRING interactions (score >= 0.7)**: 4 of 1128 gene pairs: AFDN–TJP2 (0.999); CNOT1–DDX6 (0.999); DDX6–UPF1 (0.93); UCHL5–USP15 (0.855)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05613.1 (RAI14, TJP2; 2/11); huMAP3_13535.1 (PRRC1, SEC23IP; 2/14)

### Novelty

The module should not be claimed as a wholly new molecular complex or a newly discovered pathway. Several relationships are already established in external resources, including AFDN with TJP2, CNOT1 with DDX6, DDX6 with UPF1, and USP15 with UCHL5, as well as the partial hu.MAP overlaps in (hu.MAP huMAP3_05613.1) and (hu.MAP huMAP3_13535.1). Conversely, the supplied resources do not establish the full co-abundance network as a known entity, and the module has no globally significant GO or KEGG label or STRING enrichment label. A cautious novelty claim is therefore that the bone--liver co-abundance association and its particular combination of redox, RNA, trafficking, junction, and proteostasis signals may be a new cross-tissue observation. This requires replication in independent cohorts, control for blood and cell-type composition, and comparison with published cross-tissue co-expression modules before being considered a novel biological mechanism.

**Hypothesis.** Hypothesis: the module represents a conserved cellular-adaptation state shared by liver and bone samples. In this state, oxidative and metabolic pressure engages GCLM and related stress machinery, while DDX6, UPF1, CNOT1, and associated RNA-control components adjust transcript stability and translation. SEC23IP, ATP6V1A, AP1M1, and SNX6 could coordinate secretory, endosomal, and organelle trafficking, while AFDN and TJP2 preserve cell-cell junction architecture. USP15, UCHL5, and UBA5 may tune protein stability and stress-responsive signaling. The observed cross-tissue conservation could arise from a shared response in resident cells, or from a mixture of parenchymal, stromal, epithelial, and blood-derived cells. This is a testable hypothesis, not an established pathway assignment; single-cell deconvolution, matched tissue histology, perturbation of the central genes, and replication across cohorts would be needed to distinguish these explanations.

### Important genes

#### GCLM

- **Related proteins** (co-abundance neighbors): USP15 (0.88), TJP2 (0.87), SWAP70 (0.87), LBR (0.87), UBA5 (0.84), FARSB (0.82), SEC23IP (0.81), XPO1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate-cysteine ligase modifier subunit. Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase, is the first rate limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. Gamma glutamylcysteine synthetase deficiency has been implicated in some forms of hemolytic anemia. Alternative splicing results in multiple transcript variants encoding…
- **Diseases (Open Targets)**: non-autoimmune hemolytic anemia (0.370); refractive error (0.175); alcohol drinking (0.163); Abnormality of refraction (0.143); device complication (0.096)
- **Europe PMC papers**: 6416
- **Why important**: GCLM has the strongest network position in the supplied ordering and connects to several module regions, including USP15, TJP2, SWAP70, LBR, UBA5, FARSB, SEC23IP, and XPO1. Its established function as the regulatory subunit of glutamate-cysteine ligase directly links the module to glutathione biosynthesis and oxidative-stress handling. It is tissue enhanced in liver, is detected there by HPA, and has a substantial literature base. Its association with hemolytic anemia also makes blood contamination or erythroid biology a relevant alternative explanation.
- **Conclusion**: Established evidence supports GCLM as a redox and glutathione-related anchor of the module. The hypothesis that it is the central driver of the bone--liver co-abundance pattern remains unproven; its network position may instead reflect shared stress state or abundance of particular cell populations.

#### DDX6

- **Related proteins** (co-abundance neighbors): UBA5 (0.87), RAI14 (0.83), AFDN (0.80); STRING partners: CNOT1 (0.999), UPF1 (0.93)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 connects UBA5, RAI14, and AFDN in the module and has high-confidence STRING relationships with CNOT1 and UPF1. Its established role in P-bodies, translation suppression, microRNA-mediated silencing, and messenger-RNA degradation provides a coherent RNA-turnover bridge between otherwise diverse module components. It is detected in liver and has a large literature base, while its disease associations include intellectual disability and neurodevelopmental conditions.
- **Conclusion**: Established evidence supports DDX6 as an RNA-processing and post-transcriptional-control component that helps explain the module's coherence. It is plausible, but not demonstrated, that DDX6 couples cellular stress to coordinated changes in transcript stability across bone and liver.

#### TJP2

- **Related proteins** (co-abundance neighbors): GCLM (0.87); STRING partners: AFDN (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_05613.1
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 is linked to GCLM in the co-abundance graph and has a very strong STRING relationship with AFDN; it also participates with RAI14 in hu.MAP complex (hu.MAP huMAP3_05613.1). Its established role as a tight-junction scaffold connects the module to epithelial and endothelial barrier organization. HPA places it at plasma-membrane cell junctions and detects it in liver. Its associations with hypercholanemia, cholestasis, and hearing loss provide clinically relevant evidence and indicate substantial biological specificity despite the absence of global enrichment.
- **Conclusion**: Established evidence supports TJP2 as a junctional and barrier-related anchor, particularly relevant to liver tissue. A direct role in coordinating the entire module with redox or RNA control is a hypothesis based on co-abundance and network context, not an established mechanism.

#### SEC23IP

- **Related proteins** (co-abundance neighbors): CPNE1 (0.84), CNOT1 (0.83), USP15 (0.83), ATP6V1A (0.82), GCLM (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13535.1
- **Function (MyGene.info)**: SEC23 interacting protein. This gene encodes a member of the phosphatidic acid preferring-phospholipase A1 family. The encoded protein is localized to endoplasmic reticulum exit sites and plays a critical role in ER-Golgi transport as part of the multimeric coat protein II complex. An orthologous gene in frogs is required for normal neural crest cell development, suggesting that this gene may play a role in Waardenburg synd…
- **Diseases (Open Targets)**: Parkinson disease (0.409); type 2 diabetes mellitus (0.372); cardiomyopathy (0.326); diabetes mellitus (0.294); Genu valgum (0.269)
- **Europe PMC papers**: 265
- **Why important**: SEC23IP has a central position among the supplied network genes, connecting CPNE1, CNOT1, USP15, ATP6V1A, and GCLM. Its established localization at ER exit sites and role in ER-to-Golgi transport provide a mechanistic link to the module's vesicle and membrane-trafficking signals. It is one of the members of hu.MAP complex (hu.MAP huMAP3_13535.1), alongside PRRC1, and has disease associations including diabetes, cardiomyopathy, and Parkinson disease. Its literature volume is more limited than that of the best-studied anchors, making it useful for testing module-specific predictions.
- **Conclusion**: Established evidence supports SEC23IP as a vesicle-trafficking component and a plausible bridge between membrane transport and the broader cellular-maintenance program. Whether it is a tissue-conserved regulatory node rather than a passenger requires perturbation and replication.

#### USP15

- **Related proteins** (co-abundance neighbors): GCLM (0.88), SEC23IP (0.83); STRING partners: UCHL5 (0.855)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 15. This gene encodes a member of the ubiquitin specific protease (USP) family of deubiquitinating enzymes. USP enzymes play critical roles in ubiquitin-dependent processes through polyubiquitin chain disassembly and hydrolysis of ubiquitin-substrate bonds. The encoded protein associates with the COP9 signalosome, and also plays a role in transforming growth factor beta signalling through deubiquitina…
- **Diseases (Open Targets)**: neurodegenerative disease (0.548); alcohol drinking (0.294); post term pregnancy (0.272); smoking initiation (0.217); injury (0.162)
- **Europe PMC papers**: 1872
- **Why important**: USP15 connects GCLM and SEC23IP and has a high-confidence STRING relationship with UCHL5. Its established deubiquitinating activity, COP9 signalosome association, and regulation of TGF-beta and BMP signaling connect protein stability to signaling and tissue remodeling. HPA shows bone-marrow tissue enhancement, neutrophil-related cell enhancement, immune-cell enhancement, and liver protein detection. Its disease and signaling relevance, together with an intermediate literature base, makes it a useful candidate for distinguishing a true regulatory module from a composition-driven correlation.
- **Conclusion**: Established evidence supports USP15 as a proteostasis and signaling regulator with potential relevance to both tissue remodeling and blood-cell composition. A causal role in the shared bone--liver module is a hypothesis and should be tested while explicitly controlling for neutrophil and bone-marrow contributions.

## Module 3

**Tissue pair**: bone and liver  
**Genes (19)**: AIMP1, CAPZB, CARHSP1, CLIC1, CNN2, GMPPB, EIF6, LSM5, MAT2A, PFDN4, PFDN6, RPA3, SEC23B, NANS, CTTN, TCEA1, TPD52L2, UBA3, VTA1

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. Therefore, the module does not support a single statistically established pathway interpretation. Its gene annotations instead suggest a mixed cellular-maintenance program involving proteostasis and cytoskeletal handling through PFDN6 and PFDN4, vesicle and membrane trafficking through VTA1 and SEC23B, actin organization through CTTN, CAPZB and CNN2, RNA processing and translation through LSM5, TCEA1 and EIF6, protein modification through UBA3, and intermediary metabolism through NANS and MAT2A. The strongest direct functional anchor is the prefoldin relationship between PFDN6 and PFDN4, while the remaining associations are mainly co-abundance relationships rather than demonstrated physical interactions. The module is therefore best interpreted as a heterogeneous cellular homeostasis module rather than a validated bone-liver-specific pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins: AIMP1 is the only gene annotated as secreted to blood. Most genes have low tissue specificity, and the cell-type annotations are diverse, including epithelial, reproductive, neural, smooth-muscle, platelet, megakaryocyte and gastrointestinal cell types. Blood-cell specificity is generally low, with CTTN being the notable immune-cell-enhanced gene and several genes showing neutrophil, basophil or platelet-related annotations. This pattern does not strongly support a blood-cell contamination explanation, although shared cellular composition, epithelial content or general housekeeping activity could contribute to the bone-liver co-abundance signal. Liver protein detection is broad but incomplete across the module, whereas the fact sheet provides no matching HPA bone protein-detection result. AIMP1 may additionally contribute a circulating component, but the module as a whole is not a plasma-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one high-confidence relationship within the module, between PFDN6 and PFDN4. This is consistent with their shared membership in the prefoldin chaperone complex. hu.MAP independently places the same pair together in each reported complex, with the complexes containing additional prefoldin subunits and, in some cases, chaperonin, tubulin, trafficking, cytoskeletal or regulatory proteins (hu.MAP huMAP3_09234.1) (hu.MAP huMAP3_10942.1) (hu.MAP huMAP3_14626.1) (hu.MAP huMAP3_14584.1). Thus, the prefoldin connection is an established relationship represented by both resources. No other module pair has a reported high-confidence STRING interaction, and no other module gene has a reported hu.MAP complex containing at least two module members. The broader module edges should consequently be treated as co-abundance structure, not as a known physical complex or interaction network.

**STRING interactions (score >= 0.7)**: 1 of 171 gene pairs: PFDN4–PFDN6 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09234.1 (PFDN6, PFDN4; 2/8); huMAP3_10942.1 (PFDN6, PFDN4; 2/13); huMAP3_14626.1 (PFDN6, PFDN4; 2/25); huMAP3_14584.1 (PFDN6, PFDN4; 2/61)

### Novelty

The gene functions and the PFDN4-PFDN6 relationship are not new biological observations. The potentially novel result is the coordinated abundance of this particular mixture of genes across bone and liver, but the fact sheet does not establish that this cross-tissue module has not been reported elsewhere. The lack of STRING or hu.MAP support for most pairs is evidence of limited prior interaction annotation, not proof of novelty. The absence of globally significant GO or KEGG enrichment and the heterogeneous annotations further argue against claiming discovery of a new canonical pathway. A cautious conclusion is that the cross-tissue co-abundance pattern may be a new systems-level observation requiring replication and comparison with published tissue-network studies.

**Hypothesis.** Hypothesis: the module reflects a shared baseline cellular-maintenance state present in both bone and liver, in which prefoldin-mediated proteostasis is coupled with cytoskeletal remodeling, vesicle trafficking, RNA handling and metabolic capacity. PFDN6 and PFDN4 may provide the most concrete proteostasis anchor, while CTTN and CAPZB could reflect actin-structure requirements, SEC23B and VTA1 could reflect intracellular trafficking, and MAT2A and NANS could reflect metabolic support for biosynthesis and glycan-related processes. AIMP1 could connect intracellular translation machinery with extracellular signaling in some samples. This is a mechanistic model rather than an established pathway claim, because most within-module relationships lack independent interaction support and no GO or KEGG term passed global correction.

### Important genes

#### PFDN6

- **Related proteins** (co-abundance neighbors): AIMP1 (0.92), NANS (0.88), VTA1 (0.86), EIF6 (0.86), CLIC1 (0.86), CTTN (0.85), TPD52L2 (0.81), MAT2A (0.80); STRING partners: PFDN4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09234.1, huMAP3_10942.1, huMAP3_14626.1, huMAP3_14584.1
- **Function (MyGene.info)**: prefoldin subunit 6. PFDN6 is a subunit of the heteromeric prefoldin complex that chaperones nascent actin (see MIM 102560) and alpha- and beta-tubulin (see MIM 602529 and MIM 191130, respectively) chains pending their transfer to the cytosolic chaperonin containing TCP1 (MIM 186980) (CCT) complex (Hansen et al., 1999 [PubMed 10209023]).[supplied by OMIM, Jul 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.472); colorectal carcinoma (0.074); neoplasm (0.056); hemoglobin D disease (0.046); dehydrated hereditary stomatocytosis (0.043)
- **Europe PMC papers**: 230
- **Why important**: PFDN6 is the most network-central gene in the supplied module and connects the prefoldin pair to AIMP1, NANS, VTA1, EIF6, CLIC1, CTTN, TPD52L2 and MAT2A. Its established prefoldin function supports chaperoning of nascent actin and tubulin chains, providing a plausible proteostasis and cytoskeletal anchor. It is represented in every hu.MAP complex listed for the module together with PFDN4 (hu.MAP huMAP3_09234.1) (hu.MAP huMAP3_10942.1) (hu.MAP huMAP3_14626.1) (hu.MAP huMAP3_14584.1), and it has substantial literature coverage and disease associations involving neurodegenerative disease and neoplasia.
- **Conclusion**: Established evidence supports PFDN6 as a prefoldin subunit and as an important structural hub of this module. It is reasonable to hypothesize that PFDN6 helps organize the module around protein-folding and cytoskeletal maintenance, but the co-abundance data do not prove that PFDN6 regulates the other module genes or explains the bone-liver sharing.

#### PFDN4

- **Related proteins** (co-abundance neighbors): CTTN (0.85); STRING partners: PFDN6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09234.1, huMAP3_10942.1, huMAP3_14626.1, huMAP3_14584.1
- **Function (MyGene.info)**: prefoldin subunit 4. This gene encodes a member of the prefoldin beta subunit family. The encoded protein is one of six subunits of prefoldin, a molecular chaperone complex that binds and stabilizes newly synthesized polypeptides, thereby allowing them to fold correctly. The complex, consisting of two alpha and four beta subunits, forms a double beta barrel assembly with six protruding coiled-coils. [provided by RefSe…
- **Diseases (Open Targets)**: neurodegenerative disease (0.451); colorectal cancer (0.341); cervical carcinoma (0.291); atopic eczema (0.193); liver disorder (0.126)
- **Europe PMC papers**: 256
- **Why important**: PFDN4 is the direct STRING partner of PFDN6 with the strongest reported relationship in the module and is the only other module gene repeatedly present with PFDN6 in all listed hu.MAP complexes (hu.MAP huMAP3_09234.1) (hu.MAP huMAP3_10942.1) (hu.MAP huMAP3_14626.1) (hu.MAP huMAP3_14584.1). Its established role as a prefoldin beta subunit provides the clearest physical-complex interpretation available in the module. It also has reported links to neurodegenerative disease, colorectal cancer, cervical carcinoma, atopic eczema and liver disorder.
- **Conclusion**: Established evidence identifies PFDN4 as a prefoldin component physically connected to PFDN6. Its importance here is strongest as part of the proteostasis anchor; any role in a shared bone-liver cellular state remains a hypothesis rather than a demonstrated tissue-specific function.

#### AIMP1

- **Related proteins** (co-abundance neighbors): PFDN6 (0.92), TPD52L2 (0.85), MAT2A (0.80), VTA1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 1. The protein encoded by this gene is a cytokine that is specifically induced by apoptosis, and it is involved in the control of angiogenesis, inflammation, and wound healing. The release of this cytokine renders the tumor-associated vasculature sensitive to tumor necrosis factor. The precursor protein is identical to the p43 subunit, which is associated with the multi-tRNA synthetase complex, and i…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 3 (0.790); Pelizaeus-Merzbacher-like disease (0.657); POLR-related leukodystrophy (0.657); leukodystrophy (0.372); autosomal recessive non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 663
- **Why important**: AIMP1 links the high-centrality PFDN6 and VTA1 neighborhood with TPD52L2 and MAT2A. It has dual biological context as a component associated with the multi-tRNA synthetase complex and as a cytokine involved in angiogenesis, inflammation and wound healing. It is the only module gene annotated as secreted to blood, making it relevant when considering possible extracellular or circulating contributions. It also has substantial literature coverage and strong disease associations involving leukodystrophy-related conditions.
- **Conclusion**: Established evidence supports AIMP1 in translation-associated protein complexes and in extracellular signaling functions. A circulating AIMP1 contribution could help couple tissue states, but the module evidence does not establish secretion from bone or liver, nor does it show that AIMP1 drives the co-abundance pattern.

#### MAT2A

- **Related proteins** (co-abundance neighbors): CNN2 (0.82), AIMP1 (0.80), PFDN6 (0.80), SEC23B (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine adenosyltransferase 2A. The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); familial thoracic aortic aneurysm and aortic dissection (0.416); autoimmune disorder of central nervous system (0.340); prostate carcinoma (0.252); Abnormality of the cardiovascular system (0.192)
- **Europe PMC papers**: 2615
- **Why important**: MAT2A connects PFDN6 and AIMP1 with CNN2 and SEC23B. It catalyzes production of S-adenosylmethionine, a key cellular methyl donor, and is annotated for methionine responses, protein oligomerization and TORC1 regulation. Its extensive literature and disease associations make it a biologically informative metabolic candidate, while its connection to CNN2 provides a possible bridge between metabolic state and actin organization.
- **Conclusion**: Established evidence supports MAT2A as a central metabolic enzyme supplying methyl-donor capacity. It may mark biosynthetic or growth-related cellular demand within the module, but there is no evidence here that MAT2A activity mechanistically controls the other module members or specifically explains conservation between bone and liver.

#### CTTN

- **Related proteins** (co-abundance neighbors): PFDN6 (0.85), PFDN4 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cortactin. This gene is overexpressed in breast cancer and squamous cell carcinomas of the head and neck. The encoded protein is localized in the cytoplasm and in areas of the cell-substratum contacts. This gene has two roles: (1) regulating the interactions between components of adherens-type junctions and (2) organizing the cytoskeleton and cell adhesion structures of epithelia and carcinoma cells. During …
- **Diseases (Open Targets)**: drug allergy (0.349); placenta praevia (0.265); response to antihypertensive drug (0.260); gallbladder disorder (0.258); non-autoimmune hemolytic anemia (0.240)
- **Europe PMC papers**: 2395
- **Why important**: CTTN is connected to both members of the prefoldin pair and is annotated for actin cytoskeleton organization, receptor-mediated endocytosis, intracellular transport and cell adhesion. Its localization in vesicles and at the plasma membrane is compatible with the module's cytoskeletal and trafficking features. It is also the clearest blood-cell-related outlier in the module because HPA annotates immune-cell enhancement in basophils and neutrophils, and it has extensive literature and disease associations including cancer and hematologic phenotypes.
- **Conclusion**: Established evidence supports CTTN as an actin-associated trafficking and adhesion regulator. It could connect prefoldin-dependent cytoskeletal proteostasis with membrane dynamics, but its immune-cell annotation means that a contribution from shared cellular composition should be considered before assigning a specialized bone-liver mechanism.

## Module 4

**Tissue pair**: bone and liver  
**Genes (10)**: ATP1B1, ATP2A2, DHCR24, DLG1, DNM2, ENOPH1, LAMC1, MANF, SCFD1, SRP54

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent, so the module does not support a statistically established single pathway annotation. Its structure instead suggests a mixed membrane and organelle-associated program involving vesicle trafficking, membrane organization, calcium and ion homeostasis, cholesterol or sterol handling, and extracellular-matrix connectivity. DLG1 is the main network connector, linking DNM2, SCFD1, and ENOPH1, while DHCR24 connects SRP54 with LAMC1 and ATP2A2 connects LAMC1 with the ion-transport arm. These annotations support a coordinated cellular-state interpretation more strongly than a discrete biochemical pathway.

**Cell composition.** The module is not dominated by plasma or broadly secreted proteins: only LAMC1 and MANF are identified as secreted, with LAMC1 directed to extracellular matrix and MANF secreted to blood. Most genes have low tissue specificity, while the tissue-enhanced genes point to diverse tissues rather than a single shared organ. HPA evidence shows low immune-cell specificity for most genes, with only ATP1B1 and MANF immune-cell enhanced and one gene not detected in immune cells. Thus, the module does not strongly resemble a blood-cell contaminant or a plasma-protein module. The varied single-cell enrichments, including epithelial, muscle, stromal, neural, and secretory cell types, are more consistent with shared cellular components or a conserved membrane and trafficking state. Liver protein detection is substantial but not universal, whereas there is no matching HPA bone tissue dataset for comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a high-confidence relationship only between ATP1B1 and ATP2A2. This supports a known connection between the sodium-potassium pump subunit and the calcium pump, but does not validate the entire co-abundance network. hu.MAP places ATP1B1 with DHCR24 in (hu.MAP huMAP3_07410.1), ATP2A2 with DHCR24 in (hu.MAP huMAP3_06247.1), and ATP2A2 with DHCR24 again in (hu.MAP huMAP3_09592.1). These findings support recurring complex-level or membrane-system associations around DHCR24 and ATP2A2, but the module contains only a small subset of each large complex. DLG1, SRP54, SCFD1, DNM2, LAMC1, ENOPH1, and MANF have no reported STRING partners or hu.MAP complex memberships in the supplied evidence. Therefore, most module edges are co-abundance relationships rather than previously catalogued physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: ATP1B1–ATP2A2 (0.878)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07410.1 (ATP1B1, DHCR24; 2/35); huMAP3_06247.1 (ATP2A2, DHCR24; 2/65); huMAP3_09592.1 (ATP2A2, DHCR24; 2/95)

### Novelty

The bone-liver co-abundance module may represent a dataset-specific or tissue-pair-specific association because most of its edges are not supported by the supplied STRING or hu.MAP records. However, absence from those resources does not establish novelty: the genes individually have established functions, disease links, and substantial literature, and the module combines several familiar biological systems. The appropriate conclusion is that the coordinated co-abundance pattern is potentially novel, but it requires independent replication, comparison with published co-expression studies, and experimental or perturbational validation before being called a new biological module.

**Hypothesis.** Hypothesis: the conserved module reflects a shared membrane-organelle maintenance state present in relevant bone and liver cell populations. In this model, SRP54 and SCFD1 support protein targeting and vesicle traffic, DLG1 and DNM2 organize polarized membranes and endocytic remodeling, DHCR24 maintains sterol composition in the endoplasmic-reticulum membrane, ATP1B1 and ATP2A2 coordinate sodium and calcium handling, and LAMC1 links the cellular membrane state to extracellular matrix architecture. MANF may mark or buffer endoplasmic-reticulum stress, while ENOPH1 may reflect accompanying metabolic activity. This hypothesis is not established by enrichment, because no GO/KEGG term passed global correction and the network has limited known physical support.

### Important genes

#### DLG1

- **Related proteins** (co-abundance neighbors): DNM2 (0.83), SCFD1 (0.83), ENOPH1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: discs large MAGUK scaffold protein 1. This gene encodes a multi-domain scaffolding protein that is required for normal development. This protein may have a role in septate junction formation, signal transduction, cell proliferation, synaptogenesis and lymphocyte activation. A multitude of transcript variants deriving from alternative splicing and the use of multiple alternate promoter have been observed, including some splice variants…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.375); ovarian neoplasm (0.310); multinodular goiter (0.255); diabetes mellitus (0.254); Peyronie disease (0.252)
- **Europe PMC papers**: 4288
- **Why important**: DLG1 has the strongest network connectivity in the module and links DNM2, SCFD1, and ENOPH1. Its established scaffold functions in cell polarity, actin organization, vesicle-associated signaling, and tissue development make it a plausible organizer of the module's membrane and trafficking signals. It has extensive literature and disease associations involving skeletal-system abnormalities and other disorders, giving it strong interpretive and biological relevance.
- **Conclusion**: Established evidence supports DLG1 as the central network scaffold and a regulator of polarity and membrane-linked signaling. It is a plausible module organizer, but the module does not prove that DLG1 drives the shared bone-liver co-abundance pattern.

#### DHCR24

- **Related proteins** (co-abundance neighbors): SRP54 (0.83), LAMC1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_07410.1, huMAP3_06247.1, huMAP3_09592.1
- **Function (MyGene.info)**: 24-dehydrocholesterol reductase. This gene encodes a flavin adenine dinucleotide (FAD)-dependent oxidoreductase which catalyzes the reduction of the delta-24 double bond of sterol intermediates during cholesterol biosynthesis. The protein contains a leader sequence that directs it to the endoplasmic reticulum membrane. Missense mutations in this gene have been associated with desmosterolosis. Also, reduced expression of the gene …
- **Diseases (Open Targets)**: desmosterolosis (0.821); Non-immune hydrops fetalis (0.425); hereditary disease (0.193); digestive system disorder (0.159); schizophrenia (0.112)
- **Europe PMC papers**: 2845
- **Why important**: DHCR24 connects SRP54 and LAMC1 in the co-abundance network and is the recurring module member in all supplied hu.MAP complexes (hu.MAP huMAP3_07410.1), (hu.MAP huMAP3_06247.1), and (hu.MAP huMAP3_09592.1). Its established endoplasmic-reticulum sterol-reductase activity provides a mechanistic link to membrane composition, and its desmosterolosis association makes it especially informative for interpreting lipid and organelle biology. It also has substantial literature support.
- **Conclusion**: Established evidence supports DHCR24 as the strongest candidate for a sterol and endoplasmic-reticulum component of the module. Its repeated complex membership is supportive, but it remains a hypothesis that DHCR24 coordinates the other module processes in bone and liver.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): LAMC1 (0.81); STRING partners: ATP1B1 (0.878)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06247.1, huMAP3_09592.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 connects LAMC1 in the module and has the supplied high-confidence STRING relationship with ATP1B1. It encodes a calcium pump involved in intracellular calcium homeostasis and muscle contraction-relaxation biology, and it recurs with DHCR24 in (hu.MAP huMAP3_06247.1) and (hu.MAP huMAP3_09592.1). Its extensive literature and association with Darier disease make it a strong marker of calcium-handling and membrane-system biology.
- **Conclusion**: Established evidence supports ATP2A2 as a calcium-homeostasis component with a known relationship to ATP1B1 and recurring complex context with DHCR24. The hypothesis that this calcium system is functionally coupled to the bone-liver module requires direct testing.

#### LAMC1

- **Related proteins** (co-abundance neighbors): DHCR24 (0.81), ATP2A2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: laminin subunit gamma 1. Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectivel…
- **Diseases (Open Targets)**: Fuchs' endothelial dystrophy (0.487); prostate carcinoma (0.467); colorectal cancer (0.447); eye disorder (0.434); benign colon neoplasm (0.427)
- **Europe PMC papers**: 4227
- **Why important**: LAMC1 is the module's extracellular-matrix and basement-membrane component, connects DHCR24 with ATP2A2, and is annotated as secreted to extracellular matrix. Its established roles in adhesion, migration, differentiation, signaling, and tissue architecture, together with extensive literature and cancer and tissue-disease associations, make it important for linking intracellular membrane biology to the extracellular environment.
- **Conclusion**: Established evidence supports LAMC1 as an extracellular-matrix structural and signaling component. Its co-abundance with membrane and sterol genes may indicate shared cell-state regulation or matrix-associated cell composition, but a direct mechanistic coupling is not demonstrated.

#### DNM2

- **Related proteins** (co-abundance neighbors): DLG1 (0.83), MANF (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 connects DLG1 with MANF and is annotated for endocytosis, receptor-mediated endocytosis, post-Golgi trafficking, autophagy, and cell motility. Its relevance to membrane remodeling and osteoclast-associated bone resorption provides a biologically meaningful bridge to the bone side of the tissue pair. It has extensive literature and strong neuromuscular disease associations.
- **Conclusion**: Established evidence supports DNM2 as a membrane-remodeling and trafficking component that could connect DLG1-dependent organization with MANF-associated stress biology. Its specific contribution to the conserved bone-liver pattern remains a hypothesis.

## Module 5

**Tissue pair**: bone and liver  
**Genes (11)**: ATL3, ATP5F1C, GET3, HYOU1, CCDC51, NUP205, PSMA1, RMND1, SMS, SYNJ2BP, UGGT1

### Function

The module most plausibly reflects coordinated cellular proteostasis and organelle maintenance, linking endoplasmic-reticulum folding and trafficking with mitochondrial function, membrane organization, protein quality control, nuclear transport, polyamine metabolism, and proteasomal degradation. HYOU1 and UGGT1 support an endoplasmic-reticulum stress and glycoprotein-quality-control interpretation; ATL3 and GET3 support endoplasmic-reticulum architecture and insertion of tail-anchored membrane proteins; ATP5F1C, CCDC51, RMND1, and SYNJ2BP support mitochondrial energy, ion transport, translation, and signaling; PSMA1 supports proteasomal protein turnover. NUP205 and SMS add nuclear transport and polyamine biology. No GO or KEGG term passed global correction, so this is a network-based functional interpretation rather than a claim of globally significant pathway enrichment. The lack of significant enrichment does not invalidate the module.

**Cell composition.** The HPA profile argues against a blood-cell-derived module: all listed genes have low immune-cell specificity, and no blood-cell enrichment is reported. It also does not resemble a predominantly secreted plasma-protein module; the HPA summary identifies only a small secreted subset, while the gene annotations mainly indicate intracellular, mitochondrial, nuclear, or endoplasmic-reticulum localization. Most genes have low tissue specificity, which is compatible with broadly expressed cellular maintenance functions. The frequent cell-type enhancements in reproductive, epithelial, neuronal, and other specialized cells should be interpreted cautiously and do not establish contamination by any one shared cell type. Liver protein detection is present for several members, whereas bone lacks a matching HPA tissue assessment, so the HPA evidence does not demonstrate a bone-specific or liver-specific protein program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, between HYOU1 and UGGT1. This directly supports a shared endoplasmic-reticulum protein-folding or quality-control component. STRING reports no functional enrichment for the module, and hu.MAP reports no complex containing multiple module members. Therefore, most co-abundance edges are not independently supported as stable physical interactions or as a known multiprotein complex. The module is better viewed as a coordinated expression neighborhood spanning related cellular maintenance processes than as a demonstrated single biochemical complex.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: HYOU1–UGGT1 (0.791)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a definitively new biological complex or pathway. Its individual functions are established, and the HYOU1–UGGT1 relationship is already represented in STRING. The absence of a hu.MAP complex, the sparse STRING support, and the absence of globally significant GO or KEGG enrichment make a novel shared mechanism possible but unproven. The potentially novel observation is the conserved co-abundance of these otherwise heterogeneous organelle-maintenance genes across bone and liver. That pattern could reflect a tissue-shared physiological state, coordinated housekeeping, or sample composition rather than a newly discovered molecular assembly. Additional replication, perturbation, and independent protein-level interaction testing would be required to establish novelty.

**Hypothesis.** Hypothesis: the module represents a conserved cellular stress-adaptation program that couples endoplasmic-reticulum proteostasis and membrane remodeling to mitochondrial energy and quality control. In this model, HYOU1 and UGGT1 manage folding and glycoprotein surveillance, ATL3 and GET3 maintain the endoplasmic-reticulum network and membrane-protein insertion, and ATP5F1C, CCDC51, RMND1, and SYNJ2BP coordinate mitochondrial energetics, ion handling, translation, and signaling. PSMA1 could remove damaged proteins, while NUP205 and SMS may connect the response to nucleocytoplasmic transport and polyamine metabolism. This is a mechanistic hypothesis inferred from co-abundance and known gene functions, not an established pathway or physical complex.

### Important genes

#### HYOU1

- **Related proteins** (co-abundance neighbors): ATP5F1C (0.86), PSMA1 (0.82), UGGT1 (0.80); STRING partners: UGGT1 (0.791)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is a central connector in the module and has the strongest direct functional link to the proposed stress-proteostasis interpretation. It is an HSP seventy-family protein induced in hypoxic and endoplasmic-reticulum stress contexts and is implicated in protein folding, secretion, stress responses, and protection from apoptosis. It also has substantial literature support and disease associations spanning immune, metabolic, cardiovascular, and neurodegenerative conditions.
- **Conclusion**: Established: HYOU1 is an endoplasmic-reticulum stress and protein-folding factor and is directly connected to UGGT1 in STRING. Hypothesis: its module position may make it a regulatory bridge coupling the endoplasmic-reticulum response to mitochondrial and proteasomal maintenance in bone and liver.

#### UGGT1

- **Related proteins** (co-abundance neighbors): SMS (0.84), HYOU1 (0.80); STRING partners: HYOU1 (0.791)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UDP-glucose glycoprotein glucosyltransferase 1. UDP-glucose:glycoprotein glucosyltransferase (UGT) is a soluble protein of the endoplasmic reticulum (ER) that selectively reglucosylates unfolded glycoproteins, thus providing quality control for protein transport out of the ER.[supplied by OMIM, Oct 2009].
- **Diseases (Open Targets)**: congenital disorder of glycosylation (0.416); hypercholesterolemia, familial, 1 (0.333); connective tissue disorder (0.234); ovarian dysfunction (0.216); chronic laryngitis (0.147)
- **Europe PMC papers**: 507
- **Why important**: UGGT1 is the other member of the only high-confidence STRING relationship within the module. Its established role is reglucosylation and quality control of incompletely folded glycoproteins in the endoplasmic reticulum, with links to glycoprotein biosynthesis and post-translational folding. Its position alongside HYOU1 and SMS makes it a useful anchor for interpreting the module as a proteostasis program rather than a generic expression cluster.
- **Conclusion**: Established: UGGT1 performs endoplasmic-reticulum glycoprotein quality control and has a known STRING relationship with HYOU1. Hypothesis: coordinated UGGT1 and HYOU1 abundance may indicate increased endoplasmic-reticulum folding demand or adaptive surveillance in the shared tissue context.

#### ATP5F1C

- **Related proteins** (co-abundance neighbors): PSMA1 (0.86), HYOU1 (0.86), ATL3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP synthase F1 subunit gamma. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: late-onset Alzheimers disease (0.350); scleritis (0.189); diaphragm disorder (0.082); glioblastoma (0.044); external ear disorder (0.042)
- **Europe PMC papers**: 306
- **Why important**: ATP5F1C is among the most connected module members and links HYOU1 and PSMA1 with ATL3. It encodes the gamma subunit of mitochondrial ATP synthase, directly placing oxidative phosphorylation and proton-motive force-driven ATP production in the module. Its substantial literature and disease associations provide strong biological context, although its HPA profile is not a liver-exclusive pattern.
- **Conclusion**: Established: ATP5F1C is a mitochondrial ATP-synthase component involved in oxidative phosphorylation and ATP biosynthesis. Hypothesis: it may connect energetic demand with endoplasmic-reticulum stress handling and proteasomal turnover, but the co-abundance data do not prove direct regulation or physical binding.

#### ATL3

- **Related proteins** (co-abundance neighbors): CCDC51 (0.81), ATP5F1C (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: atlastin GTPase 3. This gene encodes a member of a family of dynamin-like, integral membrane GTPases. The encoded protein is required for the proper formation of the network of interconnected tubules of the endoplasmic reticulum. Mutations in this gene may be associated with hereditary sensory neuropathy type IF. Alternatively spliced transcript variants that encode distinct isoforms have been described. [provided b…
- **Diseases (Open Targets)**: neuropathy, hereditary sensory, type 1F (0.718); hereditary sensory and autonomic neuropathy type 1 (0.617); hereditary disease (0.193); Familial prostate cancer (0.112); prostate cancer (0.112)
- **Europe PMC papers**: 672
- **Why important**: ATL3 connects ATP5F1C with CCDC51 and is the clearest structural endoplasmic-reticulum membrane factor in the module. It is an ER dynamin-like GTPase required for interconnected ER tubule formation, membrane fusion, and ER organization. Its disease association with hereditary sensory neuropathy and its established cellular function make it informative despite the absence of a hu.MAP complex.
- **Conclusion**: Established: ATL3 organizes the endoplasmic-reticulum tubular network and supports ER membrane fusion. Hypothesis: ATL3 may provide the structural interface through which ER proteostasis is coordinated with mitochondrial function in the shared module.

#### CCDC51

- **Related proteins** (co-abundance neighbors): ATL3 (0.81), SYNJ2BP (0.80), RMND1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil domain containing 51. Enables mitochondrial ATP-gated potassium channel activity. Involved in potassium ion transmembrane transport. Is integral component of mitochondrial inner membrane. Part of mitochondrial ATP-gated potassium channel complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.242); inherited retinal dystrophy (0.139); maturity-onset diabetes of the young (0.087); Abnormality of the skeletal system (0.081); maturity-onset diabetes of the young type 3 (0.068)
- **Europe PMC papers**: 1095
- **Why important**: CCDC51 links ATL3 to SYNJ2BP and RMND1 and is annotated as an integral mitochondrial-inner-membrane component of an ATP-gated potassium channel complex. Its mitochondrial localization and links to ion transport, skeletal abnormalities, retinal disease, and neurodegeneration make it a plausible bridge between membrane organization and mitochondrial physiology. Its substantial literature volume supports biological relevance, although the module itself does not establish the proposed channel interaction.
- **Conclusion**: Established: CCDC51 is associated with mitochondrial potassium transport and mitochondrial inner-membrane biology. Hypothesis: it may couple ER membrane architecture to mitochondrial ion homeostasis through coordinated abundance with ATL3, SYNJ2BP, and RMND1; this remains to be tested experimentally.

## Module 6

**Tissue pair**: bone and liver  
**Genes (5)**: KRT10, KRT9, KRT2, KRT1, KRT5

### Function

This module is a coherent epithelial keratin intermediate-filament program. The primary evidence is exceptionally consistent: the full module supports keratin filament and intermediate-filament organization (4 globally significant GO/KEGG terms, q_global 8.05e-08–5.52e-07; see the table), intermediate-filament cytoskeleton (GO:CC intermediate filament; q_global = 5.26e-06) (GO:CC intermediate filament cytoskeleton; q_global = 8.96e-06), cornified-envelope formation (KEGG Cornified envelope formation - Homo sapiens (human); q_global = 1.79e-05), skin and epidermis development (GO:BP skin development; q_global = 6.16e-05) (GO:BP epidermis development; q_global = 9.58e-05), cadherin signaling (KEGG Cadherin signaling - Homo sapiens (human); q_global = 0.00018), keratinocyte and epidermal differentiation (4 globally significant GO/KEGG terms, q_global 0.000679–0.00127; see the table), and structural cytoskeletal activity (9 globally significant GO/KEGG terms, q_global 0.00476–0.0318; see the table). The strongest interpretation is a program of epithelial structural reinforcement and keratinocyte differentiation, rather than a liver- or bone-specific metabolic pathway. The fact that all module genes participate in the core filament-related terms makes the functional assignment biologically coherent.

**Cell composition.** The module is dominated by tissue-enriched epithelial keratins rather than plasma proteins, secreted proteins, blood-cell proteins, or broadly expressed housekeeping genes. HPA assigns most members to skin and especially suprabasal keratinocytes, with additional basal-epithelial associations. KRT5 is group-enriched across epithelial tissues, while KRT9 has an unusual lymphoid-tissue tissue annotation despite its keratin biology. One member is annotated as secreted in other tissues, but the module as a whole is not a secreted-protein module. The immune-cell annotations for some genes should be treated cautiously because the dominant HPA pattern is epithelial. Protein detection is absent in liver for every tested member, and there is no matching bone HPA tissue measurement. Therefore, the apparent conservation between bone and liver may reflect shared epithelial contamination, epithelial-like cell content, sample handling, or a common keratin-containing cellular component rather than a functional program intrinsic to hepatocytes and bone cells.

**GO/KEGG enrichment**: 24 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 8.05e-08 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament organization | 1.73e-07 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament-based process | 5.52e-07 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 5.52e-07 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:MF structural constituent of skin epidermis | 1.81e-06 | KRT1, KRT10, KRT2, KRT5 |
| GO:CC intermediate filament | 5.26e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:CC intermediate filament cytoskeleton | 8.96e-06 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| KEGG Cornified envelope formation - Homo sapiens (human) | 1.79e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP skin development | 6.16e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP epidermis development | 9.58e-05 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| KEGG Cadherin signaling - Homo sapiens (human) | 0.00018 | KRT1, KRT10, KRT2, KRT5, KRT9 |
| GO:BP keratinocyte differentiation | 0.000679 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP keratinization | 0.000811 | KRT1, KRT2, KRT5 |
| GO:BP epidermal cell differentiation | 0.0012 | KRT1, KRT10, KRT2, KRT5 |
| GO:BP epithelial cell differentiation | 0.00127 | KRT1, KRT10, KRT2, KRT5, KRT9 |

### STRING and hu.MAP

STRING supports the interpretation as a known keratin interaction neighborhood. The reported high-confidence relationships connect KRT1 with KRT10, KRT2, and KRT5; KRT10 with KRT2 and KRT5; and KRT2 with KRT5. KRT1, KRT10, and KRT2 are especially central within the supplied module network, whereas KRT5 has a more peripheral position. STRING functional annotations independently support keratin, intermediate-filament, keratin-filament, cornified-envelope, and epidermolytic-hyperkeratosis themes (9 supplementary STRING terms; within-query FDR 2e-08–3.13e-06). These are supplementary because their reported FDR values were not corrected across all module-term tests. KRT9 has strong co-abundance links within the module but no reported STRING partner among the listed genes, showing that network co-abundance can extend beyond the available curated STRING links. No hu.MAP complex contains at least two module members, so there is no reported hu.MAP multi-protein complex supporting a distinct complex-level interpretation. Overall, the module is better viewed as a coordinated filament-family expression program than as a newly defined molecular complex.

**STRING interactions (score >= 0.7)**: 6 of 10 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT2 (0.956); KRT1–KRT5 (0.923); KRT10–KRT2 (0.904); KRT10–KRT5 (0.793); KRT2–KRT5 (0.871)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Keratin (FDR = 2e-08, 5 genes); SMART Intermediate filament protein (FDR = 2.92e-08, 5 genes); Component Keratin filament (FDR = 3.92e-08, 5 genes); COMPARTMENTS Keratin filament (FDR = 4.06e-08, 5 genes); Keyword Intermediate filament (FDR = 5.53e-08, 5 genes); InterPro Intermediate filament protein, conserved site (FDR = 1.75e-07, 5 genes); InterPro Intermediate filament, rod domain (FDR = 1.75e-07, 5 genes); RCTM Formation of the cornified envelope (FDR = 4.45e-07, 5 genes); DISEASES Epidermolytic hyperkeratosis (FDR = 3.13e-06, 4 genes); PMID (2025) Mass spectrometric detection of keratins in tear fluid. (FDR = 3.41e-06, 5 genes); PMID (2023) Key Factors in the Complex and Coordinated Network of Skin Keratinization: Their Significance and Involvement in Common Skin Conditions. (FDR = 3.41e-06, 5 genes); PMID (2022) A metatranscriptomic approach to explore longitudinal tissue specimens from non-healing diabetes related foot ulcers. (FDR = 3.41e-06, 5 genes); PMID (2022) Palmoplantar Keratoderma: A Molecular Genetic Analysis of Family Cases. (FDR = 3.41e-06, 5 genes); PMID (2021) Keratin Biomaterials in Skin Wound Healing, an Old Player in Modern Medicine: A Mini Review. (FDR = 3.41e-06, 5 genes); PMID (2019) Keratin 9 L164P mutation in a Chinese pedigree with epidermolytic palmoplantar keratoderma, cytokeratin analysis, and literature review. (FDR = 3.41e-06, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be claimed as a new keratin mechanism. Its composition, epithelial annotations, disease links, STRING relationships, and literature associations all point to well-established keratin biology. The potentially new observation is the recurrence of this co-abundance pattern as a conserved module across bone and liver, especially because HPA does not support liver protein detection for these genes. That cross-tissue observation may be useful as a sample-composition or shared-cell-state finding, but it requires independent validation with cell-type-resolved data, pathology review, and replication. Lack of a matching hu.MAP complex does not establish novelty, and the presence of known STRING relationships argues against interpreting the module as a previously unknown physical interaction system.

**Hypothesis.** Hypothesis: the conserved bone–liver module reflects coordinated abundance of epithelial keratin material, most plausibly arising from shared epithelial or contaminating cellular content, tissue interfaces, or a common keratinization-related state rather than from a specialized hepatocyte–osteoblast pathway. In this model, basal and suprabasal keratin programs represented by KRT5, KRT1, KRT10, KRT2, and KRT9 contribute to cytoskeletal stability and epithelial barrier structure, while the cross-tissue signal is driven by cellular composition or sample context. This hypothesis predicts that the module will track epithelial-cell abundance and keratin protein or transcript contamination, and will weaken after epithelial-cell deconvolution or single-cell restriction. It remains a hypothesis because the fact sheet does not establish the cellular origin of the signal in bone or liver.

### Important genes

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT9 (0.95), KRT10 (0.89), KRT2 (0.80); STRING partners: KRT10 (0.999), KRT2 (0.956), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a central module connector with strong links to KRT9, KRT10, and KRT2. It participates in every listed globally corrected GO/KEGG term (24 globally significant GO/KEGG terms, q_global 8.05e-08–0.0318; see the table), including keratin filaments, epidermal differentiation, and cornified-envelope formation. It is enriched in skin and suprabasal keratinocytes, has extensive literature, and is associated with several epidermolytic and palmoplantar keratoderma disorders.
- **Conclusion**: Established: KRT1 is a core structural and differentiation marker of the module and a major indicator of keratinized epithelial content. Hypothesis: its central network position may make it a useful proxy for the overall epithelial keratin signal, but the data do not show that KRT1 causally drives the cross-tissue association.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT1 (0.89), KRT9 (0.87), KRT2 (0.82); STRING partners: KRT1 (0.999), KRT2 (0.904), KRT5 (0.793)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is a central connector and has strong STRING relationships with KRT1, KRT2, and KRT5. It is a type I intermediate-filament protein enriched in suprabasal keratinocytes and is annotated for keratinocyte differentiation, epidermis development, cornification, and intermediate-filament organization. It has a substantial literature and established associations with epidermolytic hyperkeratosis and related ichthyotic disorders.
- **Conclusion**: Established: KRT10 marks the differentiated suprabasal keratin program and provides strong support for the module's epithelial interpretation. Hypothesis: its annotated presence outside the liver may reflect keratin-containing material or epithelial cell contribution rather than a liver-intrinsic differentiation process.

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT9 (0.80); STRING partners: KRT1 (0.923), KRT10 (0.793), KRT2 (0.871)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 represents the basal epithelial arm of the module and connects to KRT9 within the supplied co-abundance network. It is localized to intermediate filaments, is associated with basal keratinocytes and multiple epithelial tissues, and is annotated for epidermis development, mechanical response, migration, keratinization, and intermediate-filament polymerization. It has extensive literature and well-established links to several forms of epidermolysis bullosa and related epithelial disorders.
- **Conclusion**: Established: KRT5 broadens the module beyond terminally differentiated suprabasal keratins and supports a basal-to-suprabasal epithelial program. Hypothesis: its presence may indicate basal epithelial material or tissue-interface sampling in the bone and liver datasets.

#### KRT2

- **Related proteins** (co-abundance neighbors): KRT10 (0.82), KRT1 (0.80); STRING partners: KRT1 (0.956), KRT10 (0.904), KRT5 (0.871)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is a central connector to KRT1 and KRT10 and participates in the full set of globally corrected terms (24 globally significant GO/KEGG terms, q_global 8.05e-08–0.0318; see the table). It is enriched in suprabasal keratinocytes and is annotated for epidermis development, keratinization, keratinocyte activation and proliferation, and intermediate-filament organization. It also has extensive literature and disease associations involving epidermolytic and exfoliative ichthyosis and palmoplantar hyperkeratosis.
- **Conclusion**: Established: KRT2 is a strong marker of the suprabasal keratinization state and reinforces the functional interpretation. Hypothesis: its network position may reflect coordinated differentiation-state variation rather than a distinct KRT2-led mechanism in either internal tissue.

#### KRT9

- **Related proteins** (co-abundance neighbors): KRT1 (0.95), KRT10 (0.87), KRT5 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 9. This gene encodes the type I keratin 9, an intermediate filament chain expressed only in the terminally differentiated epidermis of palms and soles. Mutations in this gene cause epidermolytic palmoplantar keratoderma. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: epidermolytic palmoplantar keratoderma, 1 (0.828); palmoplantar keratoderma, epidermolytic (0.682); Localized epidermolytic hyperkeratosis (0.511); Palmoplantar hyperkeratosis (0.456); Palmoplantar keratoderma (0.438)
- **Europe PMC papers**: 773
- **Why important**: KRT9 has a strong module-network position and links to KRT1, KRT10, and KRT5, even though no STRING partner is reported for it among the listed genes. It is a type I keratin associated with terminally differentiated palmoplantar epidermis, and its mutations cause epidermolytic palmoplantar keratoderma. Its HPA annotations are more atypical than those of the other members, including lymphoid tissue and several specialized cell-type annotations, making it informative for assessing tissue composition and annotation discordance.
- **Conclusion**: Established: KRT9 contributes a specialized keratinization and disease signal and is co-abundant with the module despite limited listed STRING support. Hypothesis: KRT9 may be especially useful for distinguishing a palmoplantar-like or specialized epithelial signature from a generic housekeeping keratin signal, although the current data cannot determine its cellular source in bone or liver.
