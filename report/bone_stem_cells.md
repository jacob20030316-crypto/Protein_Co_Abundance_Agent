# Conserved co-abundance modules: bone and stem_cells

## Module 0

**Tissue pair**: bone and stem_cells  
**Genes (33)**: NUDT1, ACO1, ADK, ARL3, BPNT1, CFL2, COMMD1, CSRP1, CTNNA2, DOCK7, DUSP3, ELOC, FLNC, GALNS, GCC2, GCA, ILK, METTL15, FAM114A1, PALLD, PDIA5, PRPS2, GINS3, TP53I3, S100A11, SUDS3, STAT2, HARS2, TUBB6, TPM1, TSG101, TWF1, URB2

### Function

The strongest supported interpretation is a contractile actin-cytoskeleton and muscle-structural module. The primary evidence is the globally significant enrichment for sarcomere organization (GO:BP sarcomere organization; q_global = 0.0122), myofibril (GO:CC myofibril; q_global = 0.0249), contractile muscle fiber (GO:CC contractile muscle fiber; q_global = 0.0273), and myofibril assembly (GO:BP myofibril assembly; q_global = 0.035). These terms converge on organization and assembly of actin-rich contractile structures rather than on a single metabolic or signaling pathway. CFL2, CSRP1, FLNC, and TPM1 recur across the primary terms, while ILK, PALLD, and TWF1 extend the signal to adhesion, actin organization, and cytoskeletal remodeling. The remaining genes may represent connected regulatory, metabolic, ves trafficking, replication, stress-response, or cell-state components rather than core sarcomeric constituents. The co-abundance structure therefore most plausibly reflects coordinated cytoskeletal and contractile-cell biology, with possible contributions from shared stromal, smooth-muscle, vascular, or myogenic cell populations.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a small secreted fraction, and the listed genes are largely intracellular or membrane-associated. It is also not uniformly blood-cell specific, because most genes have low immune-cell specificity. Nevertheless, some blood-related signal is present, including immune-cell enhancement for selected genes and particularly strong bone-marrow and neutrophil associations for GCA, with additional myeloid or platelet-related annotations among other genes. The clearest composition signal is instead structural and contractile: skeletal-muscle and heart-muscle enrichment occurs for several genes, and smooth-muscle or cardiomyocyte cell-type associations are frequent. Many genes also have low tissue specificity or broad cell-type distributions, so the shared bone and stem-cell module could reflect a common contractile or stromal cell population, tissue remodeling, or sample composition rather than a process unique to either tissue. HPA provides no matching protein-detection result for either named tissue, so the protein-level presence of the module in those tissues cannot be confirmed from this fact sheet.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP sarcomere organization | 0.0122 | CFL2, CSRP1, FLNC, TPM1 |
| GO:CC myofibril | 0.0249 | CFL2, CSRP1, FLNC, ILK, PALLD, TPM1, TWF1 |
| GO:CC contractile muscle fiber | 0.0273 | CFL2, CSRP1, FLNC, ILK, PALLD, TPM1, TWF1 |
| GO:BP myofibril assembly | 0.035 | CFL2, CSRP1, FLNC, TPM1 |

### STRING and hu.MAP

STRING provides direct high-confidence support for selected relationships within the structural core: CFL2 is linked with FLNC and TWF1, and FLNC is linked with ILK. STRING also identifies the myofibril and sarcomere components (STRING Component Myofibril; within-query FDR = 0.019) and (STRING Component Sarcomere; within-query FDR = 0.029), concordant with the primary GO evidence, although these are supplementary annotations and their STRING FDR must not be treated as global enrichment significance. A separate STRING-supported island connects COMMD1, ELOC, and GINS3, indicating that the module also contains a transcriptional, ubiquitin-related, or replication-associated substructure that is not explained by the contractile terms. hu.MAP gives partial complex-level support rather than a complete module explanation: TPM1 and DOCK7 co-occur in two large complexes (hu.MAP huMAP3_08205.1) and (hu.MAP huMAP3_09542.1), while BPNT1 and HARS2 co-occur in a broad metabolic and mitochondrial complex (hu.MAP huMAP3_13468.1). Because each hu.MAP result contains only a small subset of its full complex membership, these findings support compatibility with known molecular assemblies but do not establish that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 5 of 528 gene pairs: CFL2–FLNC (0.841); CFL2–TWF1 (0.831); COMMD1–ELOC (0.955); ELOC–GINS3 (0.813); FLNC–ILK (0.714)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Myofibril (FDR = 0.019, 7 genes); Component Sarcomere (FDR = 0.029, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08205.1 (TPM1, DOCK7; 2/17); huMAP3_09542.1 (TPM1, DOCK7; 2/38); huMAP3_13468.1 (BPNT1, HARS2; 2/99)

### Novelty

The module is unlikely to represent a wholly new molecular function, because its central interpretation is already well established by sarcomere and myofibril annotations (GO:BP sarcomere organization; q_global = 0.0122) through (GO:BP myofibril assembly; q_global = 0.035), known STRING relationships, and the established roles of FLNC, TPM1, CFL2, CSRP1, ILK, and PALLD in actin organization, adhesion, contraction, or muscle structure. The potentially novel aspect is the observation of this coordinated co-abundance pattern shared between bone and stem_cells, including its peripheral metabolic, stress-response, trafficking, and cell-cycle genes. However, absence of a complete match in STRING or hu.MAP would not prove novelty, since those resources represent curated or experimentally supported physical and functional relationships rather than every tissue-level co-expression pattern. A defensible claim is therefore that the module may be a tissue-pair-specific or dataset-specific organization of known contractile biology, not a newly discovered contractile mechanism.

**Hypothesis.** Hypothesis: a shared contractile or stromal cell state in bone and stem_cells coordinately increases expression of actin-filament remodeling, sarcomere-associated structural proteins, focal-adhesion machinery, and cytoskeletal transport components. In this model, TPM1 stabilizes actin filaments, CFL2 and TWF1 regulate filament turnover, FLNC crosslinks actin and couples it to membrane-associated structures, while ILK and PALLD connect adhesion and cytoskeletal organization. CSRP1 may support differentiation-linked structural regulation. The additional genes could reflect the metabolic, transcriptional, oxidative-stress, and trafficking requirements of the same cell state. This should be tested by cell-resolved expression, microscopy for sarcomeric or contractile structures, and perturbation of the structural genes; the proposed mechanism is not established by co-abundance alone.

### Important genes

#### FLNC

- **Related proteins** (co-abundance neighbors): ACO1 (0.87), PALLD (0.84), ARL3 (0.81); STRING partners: CFL2 (0.841), ILK (0.714)
- **HPA**: Tissue enhanced; Group enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin C. This gene encodes one of three related filamin genes, specifically gamma filamin. These filamin proteins crosslink actin filaments into orthogonal networks in cortical cytoplasm and participate in the anchoring of membrane proteins for the actin cytoskeleton. Three functional domains exist in filamin: an N-terminal filamentous actin-binding domain, a C-terminal self-association domain, and a membr…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy 26 (0.833); myofibrillar myopathy 5 (0.791); distal myopathy with posterior leg and anterior hand involvement (0.742); dilated cardiomyopathy (0.714); familial restrictive cardiomyopathy (0.660)
- **Europe PMC papers**: 3861
- **Why important**: FLNC is a central annotated structural gene in the module. It contributes to every primary enrichment term (GO:BP sarcomere organization; q_global = 0.0122) through (GO:BP myofibril assembly; q_global = 0.035), appears in both STRING structural summaries (STRING Component Myofibril; within-query FDR = 0.019) and (STRING Component Sarcomere; within-query FDR = 0.029), and has STRING links to CFL2 and ILK. Its known function is to crosslink actin networks and anchor membrane-associated proteins, while HPA shows enhancement in skeletal and heart muscle and in cardiomyocyte and myonuclear populations. Its disease associations include cardiomyopathy and myofibrillar myopathy, with substantial literature support.
- **Conclusion**: Established evidence supports FLNC as a core structural marker and plausible organizer of the contractile signal. Its role as the initiating driver of this shared bone and stem-cell module remains a hypothesis.

#### TPM1

- **Related proteins** (co-abundance neighbors): METTL15 (0.86), GALNS (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08205.1, huMAP3_09542.1
- **Function (MyGene.info)**: tropomyosin 1. This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the fi…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.798); left ventricular noncompaction (0.760); left ventricular noncompaction 9 (0.664); familial isolated dilated cardiomyopathy (0.639); hypertrophic cardiomyopathy 3 (0.596)
- **Europe PMC papers**: 6278
- **Why important**: TPM1 is present in every primary enrichment term (GO:BP sarcomere organization; q_global = 0.0122) through (GO:BP myofibril assembly; q_global = 0.035), both STRING functional summaries (STRING Component Myofibril; within-query FDR = 0.019) and (STRING Component Sarcomere; within-query FDR = 0.029), and two hu.MAP complexes (hu.MAP huMAP3_08205.1) and (hu.MAP huMAP3_09542.1). It is an actin-binding tropomyosin that stabilizes actin filaments and participates in muscle and non-muscle contractile systems. HPA shows enhancement in heart and skeletal muscle, and its disease associations include hypertrophic and dilated cardiomyopathy. Its literature volume is substantial, supporting a well-established biological interpretation.
- **Conclusion**: Established evidence identifies TPM1 as a strong marker of the module's contractile and actin-filament identity. Its co-abundance here does not by itself demonstrate a pathogenic TPM1 variant or a direct causal role in either tissue.

#### CFL2

- **Related proteins** (co-abundance neighbors): GCC2 (0.87), TUBB6 (0.83), PDIA5 (0.81); STRING partners: FLNC (0.841), TWF1 (0.831)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cofilin 2. This gene encodes an intracellular protein that is involved in the regulation of actin-filament dynamics. This protein is a major component of intranuclear and cytoplasmic actin rods. It can bind G- and F-actin in a 1:1 ratio of cofilin to actin, and it reversibly controls actin polymerization and depolymerization in a pH-dependent manner. Mutations in this gene cause nemaline myopathy type 7, a f…
- **Diseases (Open Targets)**: nemaline myopathy 7 (0.758); typical nemaline myopathy (0.599); atrial fibrillation (0.525); nemaline myopathy (0.376); Takayasu arteritis (0.303)
- **Europe PMC papers**: 1415
- **Why important**: CFL2 is present in every primary enrichment term (GO:BP sarcomere organization; q_global = 0.0122) through (GO:BP myofibril assembly; q_global = 0.035) and both STRING structural summaries (STRING Component Myofibril; within-query FDR = 0.019) and (STRING Component Sarcomere; within-query FDR = 0.029). It has direct STRING relationships with FLNC and TWF1 and is HPA-enriched in heart muscle, skeletal muscle, and tongue, with smooth-muscle and myoid cell associations. Its established function is actin filament severing and regulation of polymerization and depolymerization, and it is associated with nemaline myopathy.
- **Conclusion**: Established evidence supports CFL2 as the actin-dynamics component of the contractile core. A specific role for CFL2 in coordinating the shared bone and stem-cell state is a hypothesis requiring functional testing.

#### CSRP1

- **Related proteins** (co-abundance neighbors): DUSP3 (0.90), ILK (0.88), TUBB6 (0.84), HARS2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cysteine and glycine rich protein 1. This gene encodes a member of the cysteine-rich protein (CSRP) family. This gene family includes a group of LIM domain proteins, which may be involved in regulatory processes important for development and cellular differentiation. The LIM/double zinc-finger motif found in this gene product occurs in proteins with critical functions in gene regulation, cell growth, and somatic differentiation. Alte…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.272); placenta praevia (0.160); Varicose veins (0.113); acute myeloid leukemia (0.091); hepatocellular carcinoma (0.084)
- **Europe PMC papers**: 822
- **Why important**: CSRP1 is the most consistently annotated gene in the primary evidence, occurring in (GO:BP sarcomere organization; q_global = 0.0122) through (GO:BP myofibril assembly; q_global = 0.035), and it also appears in (STRING Component Myofibril; within-query FDR = 0.019) and (STRING Component Sarcomere; within-query FDR = 0.029). Its LIM-domain protein biology is compatible with differentiation and structural regulation, while the supplied annotations include sarcomere organization, muscle development, and platelet aggregation. HPA links it to blood vessels, myoepithelial, stromal, hepatic stellate, and megakaryocyte populations. It has disease associations involving hypertrophic cardiomyopathy and vascular conditions.
- **Conclusion**: Established evidence supports CSRP1 as a differentiation-linked structural regulator and a useful marker of the module's contractile program. Whether it mediates the bone-to-stem-cell shared signal rather than merely tracking cell state remains unresolved.

#### ILK

- **Related proteins** (co-abundance neighbors): PALLD (0.91), CSRP1 (0.88), DUSP3 (0.86), FAM114A1 (0.85), TUBB6 (0.83), SUDS3 (0.80); STRING partners: FLNC (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK occupies a relatively central position in the module and connects to PALLD, CSRP1, DUSP3, FAM114A1, and TUBB6. It participates in the primary myofibril and contractile-muscle terms (GO:CC myofibril; q_global = 0.0249) and (GO:CC contractile muscle fiber; q_global = 0.0273), both STRING structural summaries (STRING Component Myofibril; within-query FDR = 0.019) and (STRING Component Sarcomere; within-query FDR = 0.029), and has a high-confidence STRING link to FLNC. Its established function involves integrin-linked signaling, focal adhesion, cell-matrix adhesion, and morphogenesis. HPA places it at focal adhesion sites and associates it with smooth-muscle cells, megakaryocytes, and platelets.
- **Conclusion**: Established evidence supports ILK as a bridge between extracellular-matrix adhesion and the contractile cytoskeleton. Its possible role in coupling the module to stem-cell adhesion or bone remodeling is a hypothesis, not a conclusion from this network alone.

#### PALLD

- **Related proteins** (co-abundance neighbors): ILK (0.91), TUBB6 (0.87), FLNC (0.84), ARL3 (0.83), DUSP3 (0.82), FAM114A1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: palladin, cytoskeletal associated protein. This gene encodes a cytoskeletal protein that is required for organizing the actin cytoskeleton. The protein is a component of actin-containing microfilaments, and it is involved in the control of cell shape, adhesion, and contraction. Polymorphisms in this gene are associated with a susceptibility to pancreatic cancer type 1, and also with a risk for myocardial infarction. Alternative splicing re…
- **Diseases (Open Targets)**: coronary artery disorder (0.444); exocrine pancreatic carcinoma (0.372); coronary atherosclerosis (0.360); Bicuspid aortic valve (0.325); aortic stenosis (0.319)
- **Europe PMC papers**: 1170
- **Why important**: PALLD is a highly connected structural component linked within the module to ILK, TUBB6, FLNC, ARL3, DUSP3, and FAM114A1. It occurs in the primary myofibril and contractile-muscle terms (GO:CC myofibril; q_global = 0.0249) and (GO:CC contractile muscle fiber; q_global = 0.0273) and in both STRING summaries (STRING Component Myofibril; within-query FDR = 0.019) and (STRING Component Sarcomere; within-query FDR = 0.029). Its established function is organization of actin-containing microfilaments and control of cell shape, adhesion, migration, and contraction. HPA associates it with cardiomyocytes, myonuclei, and smooth-muscle cells, and the supplied disease associations include coronary and valve disorders.
- **Conclusion**: Established evidence supports PALLD as a cytoskeletal and adhesion-related component that helps connect the contractile core to cell morphology. Its contribution to the shared tissue-pair pattern remains a testable hypothesis.

## Module 1

**Tissue pair**: bone and stem_cells  
**Genes (12)**: ATP5F1A, ATP5F1B, HSPA5, CLIC1, GSTP1, HSP90AA1, PHB1, PHB2, RAN, SERPINH1, TKT, PBK

### Function

The module most strongly supports a conserved cellular energy, mitochondrial organization, and proteostasis program. The primary evidence is cell-surface annotation for ATP5F1A, ATP5F1B, HSP90AA1, HSPA5, PHB1, and PHB2 (GO:CC cell surface; q_global = 0.00392), mitochondrial prohibitin complex membership for PHB1 and PHB2 (GO:CC mitochondrial prohibitin complex; q_global = 0.0454), and angiostatin binding for ATP5F1A and ATP5F1B (GO:MF angiostatin binding; q_global = 0.0454). The ATP synthase subunits indicate oxidative-phosphorylation capacity, while the prohibitin pair supports mitochondrial membrane organization. HSPA5, HSP90AA1, and SERPINH1 add protein-folding and stress-response biology, and TKT links the module to pentose-phosphate metabolism. The module therefore appears multifunctional rather than a narrowly lineage-specific pathway. The cell-surface result should be interpreted cautiously because several contributing proteins are primarily annotated to mitochondria, cytosol, nucleoplasm, or the endoplasmic reticulum.

**Cell composition.** This is not predominantly a plasma-protein or classical secreted-protein module. HPA reports three secreted genes, but the individual annotations chiefly describe intracellular, membrane-associated, mitochondrial, cytosolic, nucleoplasmic, or endoplasmic-reticulum localization. Most genes have low tissue specificity, and most have low immune-cell specificity, arguing for a broadly expressed housekeeping or stress-related component rather than a module restricted to bone or stem cells. HPA also shows recurrent enrichment in epithelial and trophoblast cell types, with additional signals in bone marrow and lymphoid tissue. The supplementary STRING tissue results include blood-cancer, leukemia, lymphoid, and multiple organ categories, so shared cell composition or general cellular stress could contribute to the bone and stem-cell signal. However, the available HPA protein-detection fields contain no matching data for either target tissue, so tissue-level protein localization cannot be confirmed from this fact sheet.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC cell surface | 0.00392 | ATP5F1A, ATP5F1B, HSP90AA1, HSPA5, PHB1, PHB2 |
| GO:CC mitochondrial prohibitin complex | 0.0454 | PHB1, PHB2 |
| GO:MF angiostatin binding | 0.0454 | ATP5F1A, ATP5F1B |

### STRING and hu.MAP

STRING supports a coherent but selective core of known relationships: ATP5F1A with ATP5F1B, PHB1 with PHB2, ATP5F1B with both prohibitin proteins, HSP90AA1 with HSPA5, and HSPA5 with SERPINH1. The strongest-supported relationships are the ATP synthase alpha-beta pair, the prohibitin pair, and the HSP90AA1-HSPA5 pair. hu.MAP independently places PHB1 and PHB2 together in a complete prohibitin complex and in larger membrane or mitochondrial-associated complexes, while ATP5F1A and ATP5F1B occur together in several ATP synthase-related complexes. These results show that part of the module recapitulates established protein complexes. The remaining genes have little or no direct STRING or hu.MAP support within the supplied resources, so co-abundance should not be equated with direct physical interaction. The STRING tissue enrichments are supplementary only (15 supplementary STRING terms; within-query FDR 7.3e-05–0.0024) and do not replace the globally corrected GO/KEGG evidence.

**STRING interactions (score >= 0.7)**: 6 of 66 gene pairs: ATP5F1A–ATP5F1B (0.999); ATP5F1B–PHB1 (0.782); ATP5F1B–PHB2 (0.712); HSP90AA1–HSPA5 (0.968); HSPA5–SERPINH1 (0.747); PHB1–PHB2 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Blood cancer cell (FDR = 7.3e-05, 10 genes); TISSUES Lung (FDR = 7.3e-05, 10 genes); TISSUES Interstitial cell of Cajal (FDR = 7.3e-05, 7 genes); TISSUES Brain cell line (FDR = 0.0001, 6 genes); TISSUES Gastrointestinal tract (FDR = 0.00012, 10 genes); TISSUES Leukemia cell (FDR = 0.0002, 9 genes); TISSUES Connective tissue (FDR = 0.00021, 8 genes); TISSUES Liver (FDR = 0.00063, 11 genes); TISSUES Skin (FDR = 0.00063, 8 genes); TISSUES Integument (FDR = 0.0012, 9 genes); TISSUES Trunk (FDR = 0.0014, 7 genes); TISSUES Lymphoid tissue (FDR = 0.0015, 8 genes); TISSUES Lymphoblast (FDR = 0.0016, 5 genes); Component Cell surface (FDR = 0.0018, 6 genes); TISSUES Male reproductive gland (FDR = 0.0024, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01706.1 (PHB1, PHB2; 2/2); huMAP3_09671.1 (PHB1, PHB2; 2/10); huMAP3_11743.1 (PHB1, PHB2; 2/10); huMAP3_08750.1 (ATP5F1B, ATP5F1A; 2/12); huMAP3_09307.1 (ATP5F1B, ATP5F1A; 2/35); huMAP3_11095.1 (ATP5F1B, ATP5F1A; 2/45); huMAP3_10725.1 (PHB1, PHB2; 2/59)

### Novelty

The module-level observation may be biologically useful, but it cannot be called a wholly new molecular mechanism. Its central prohibitin and ATP synthase relationships are already established by STRING and hu.MAP, and several genes are broadly expressed housekeeping or stress-response factors. A potentially novel aspect is the conserved co-abundance of mitochondrial energy, prohibitin, endoplasmic-reticulum chaperone, pentose-phosphate, and collagen-folding genes across bone and stem-cell groups. That interpretation remains a hypothesis because absence from interaction databases does not establish novelty, and the module may partly reflect shared cell types, broad cellular metabolism, or sample stress. Demonstrating novelty would require comparison with prior co-expression or co-abundance modules and validation in independent tissue datasets.

**Hypothesis.** Hypothesis: the module represents a shared adaptation program in which mitochondrial ATP production and prohibitin-dependent mitochondrial organization support cells experiencing biosynthetic or proteotoxic demand. Endoplasmic-reticulum chaperoning by HSPA5 and collagen-specific folding by SERPINH1 may help maintain protein quality and extracellular-matrix production, while TKT supplies non-oxidative pentose-phosphate flux and metabolic flexibility. This coordinated state could be relevant to metabolically active bone-associated cells and stem or progenitor populations, but it could also arise from shared epithelial, stromal, trophoblast-like, or other contaminating cell states. The hypothesis should be tested by cell-resolved expression, mitochondrial and unfolded-protein-response measurements, and perturbation of the ATP synthase-prohibitin core.

### Important genes

#### ATP5F1B

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.97), SERPINH1 (0.93), PHB2 (0.82), HSPA5 (0.81), PHB1 (0.81); STRING partners: ATP5F1A (0.999), PHB1 (0.782), PHB2 (0.712)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08750.1, huMAP3_09307.1, huMAP3_11095.1
- **Function (MyGene.info)**: ATP synthase F1 subunit beta. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: hypermetabolism due to uncoupled mitochondrial oxidative phosphorylation 2 (0.499); hypertrophic cardiomyopathy (0.212); Alzheimer disease (0.177); hypertensive disorder (0.117); response to xenobiotic stimulus (0.117)
- **Europe PMC papers**: 735
- **Why important**: ATP5F1B is the most connected module member and links ATP5F1A, both prohibitin proteins, HSPA5, and SERPINH1 in the co-abundance network. It is an established mitochondrial ATP synthase subunit, contributes to ATP biosynthesis and proton-motive-force-driven energy production, and is present in the primary cell-surface and angiostatin-binding terms (GO:CC cell surface; q_global = 0.00392) (GO:MF angiostatin binding; q_global = 0.0454). Its strong STRING relationship with ATP5F1A and connections to prohibitin proteins make it a useful anchor for the module. Its extensive literature and disease associations also make it experimentally tractable.
- **Conclusion**: Established evidence supports ATP5F1B as a central energy-metabolism and mitochondrial-complex marker of the module. It is plausible, but not proven, that its coordinated abundance helps couple oxidative phosphorylation to the proteostasis and matrix-related features of the module.

#### PHB1

- **Related proteins** (co-abundance neighbors): ATP5F1A (0.85), HSPA5 (0.83), ATP5F1B (0.81); STRING partners: ATP5F1B (0.782), PHB2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01706.1, huMAP3_09671.1, huMAP3_11743.1, huMAP3_10725.1
- **Function (MyGene.info)**: prohibitin 1. This gene is evolutionarily conserved, and its product is proposed to play a role in human cellular senescence and tumor suppression. Antiproliferative activity is reported to be localized to the 3' UTR, which is proposed to function as a trans-acting regulatory RNA. Several pseudogenes of this gene have been identified. Alternative splicing results in multiple transcript variants. [provided by Re…
- **Diseases (Open Targets)**: coronary artery disorder (0.458); myocardial ischemia (0.454); hypertensive disorder (0.396); heart disorder (0.343); asthma (0.339)
- **Europe PMC papers**: 1249
- **Why important**: PHB1 is a network bridge between ATP5F1A, ATP5F1B, and HSPA5. It forms a high-confidence STRING pair with PHB2 and is present with PHB2 in the primary mitochondrial prohibitin-complex term (GO:CC mitochondrial prohibitin complex; q_global = 0.0454) and in several hu.MAP complexes (hu.MAP huMAP3_01706.1) (hu.MAP huMAP3_09671.1) (hu.MAP huMAP3_11743.1) (hu.MAP huMAP3_10725.1). Its annotations include mitochondrion organization, osteoblast differentiation, transcriptional regulation, and proposed senescence and tumor-suppression functions. It therefore connects the energy core to cell-state regulation and is relevant to the bone context.
- **Conclusion**: Established evidence identifies PHB1 as a core prohibitin-complex component and a plausible mitochondrial-organizational hub. Its contribution to a shared bone and stem-cell state is a hypothesis, because the co-abundance data do not demonstrate that PHB1 drives osteoblast or stem-cell behavior.

#### PHB2

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.82), ATP5F1A (0.82); STRING partners: ATP5F1B (0.712), PHB1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_01706.1, huMAP3_09671.1, huMAP3_11743.1, huMAP3_10725.1
- **Function (MyGene.info)**: prohibitin 2. Enables several functions, including protein C-terminus binding activity; protein N-terminus binding activity; and protein dimerization activity. Involved in several processes, including defense response to virus; positive regulation of cell cycle phase transition; and regulation of transcription, DNA-templated. Located in several cellular components, including cell surface; mitochondrial membrane…
- **Diseases (Open Targets)**: breast cancer (0.101); breast carcinoma (0.101); neoplasm (0.100); non-small cell lung carcinoma (0.096); colorectal carcinoma (0.085)
- **Europe PMC papers**: 2714
- **Why important**: PHB2 is the partner of PHB1 in the strongest prohibitin relationship in the supplied evidence and participates in the same globally corrected mitochondrial prohibitin-complex annotation (GO:CC mitochondrial prohibitin complex; q_global = 0.0454). It connects to both ATP synthase subunits and appears in multiple hu.MAP mitochondrial or membrane-associated complexes (hu.MAP huMAP3_01706.1) (hu.MAP huMAP3_09671.1) (hu.MAP huMAP3_11743.1) (hu.MAP huMAP3_10725.1). Its reported roles include mitophagy, mitochondrion organization, transcriptional regulation, and protein or nuclear interactions, giving it a plausible role at the interface of mitochondrial quality control and cellular state.
- **Conclusion**: Established evidence supports PHB2 as the second core component of the module's mitochondrial prohibitin signal. A role in coordinating mitochondrial quality control with stem or bone-cell adaptation remains a mechanistic hypothesis rather than a demonstrated causal function.

#### HSPA5

- **Related proteins** (co-abundance neighbors): PHB1 (0.83), ATP5F1B (0.81); STRING partners: HSP90AA1 (0.968), SERPINH1 (0.747)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is linked in the module to PHB1 and ATP5F1B and has a very strong STRING relationship with HSP90AA1, with an additional relationship to SERPINH1. It is an endoplasmic-reticulum HSP70 chaperone and master regulator of ER homeostasis, and it contributes to the primary cell-surface annotation (GO:CC cell surface; q_global = 0.00392). Its broad tissue profile and repeated supplementary tissue associations are consistent with a general proteostasis or stress component rather than a narrowly tissue-specific marker.
- **Conclusion**: Established evidence supports HSPA5 as the module's principal ER-proteostasis component. Its coordinated abundance with mitochondrial genes suggests cross-organelle stress adaptation, but the data do not establish a direct mitochondrial-to-ER signaling mechanism.

#### TKT

- **Related proteins** (co-abundance neighbors): GSTP1 (0.86), ATP5F1A (0.82), PBK (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transketolase. This gene encodes a thiamine-dependent enzyme which plays a role in the channeling of excess sugar phosphates to glycolysis in the pentose phosphate pathway. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: transketolase deficiency (0.663); neurodegenerative disease (0.409); cardiomyopathy (0.382); alcohol drinking (0.261); urolithiasis (0.259)
- **Europe PMC papers**: 3981
- **Why important**: TKT connects ATP5F1A with GSTP1 and PBK in the module and is tissue enhanced in bone marrow, with HPA group enrichment across several myeloid cell types. Its established function in the non-oxidative pentose-phosphate pathway provides a metabolic link between carbon remodeling, precursor supply, and cellular redox or biosynthetic demand. It has no supplied STRING or hu.MAP interaction support, making its co-abundance with the mitochondrial and chaperone core especially informative but less mechanistically resolved.
- **Conclusion**: Established evidence supports TKT as a metabolic-flexibility marker and a possible contributor to the marrow-associated aspect of the module. Its direct functional integration with the ATP synthase-prohibitin core is a hypothesis based on co-abundance rather than a known physical interaction.

#### SERPINH1

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.93); STRING partners: HSPA5 (0.747)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family H member 1. This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymo…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 10 (0.714); preterm premature rupture of the membranes (0.559); coronary artery disorder (0.554); myocardial infarction (0.510); Abnormality of the skeletal system (0.474)
- **Europe PMC papers**: 2762
- **Why important**: SERPINH1 is the module's collagen-specific endoplasmic-reticulum chaperone and is linked in the network to ATP5F1B. Its HPA cell-type annotations include stromal and trophoblast-related populations, and its established functions include collagen fibril organization and response to unfolded protein. Its disease associations include osteogenesis imperfecta type ten and skeletal-system abnormality, making it particularly relevant to bone biology. The STRING relationship with HSPA5 supports a proteostasis connection, although it is not a hu.MAP member in the supplied complexes.
- **Conclusion**: Established evidence supports SERPINH1 as the strongest extracellular-matrix and collagen-folding marker in the module. Its coupling to mitochondrial energy and ER-stress genes may reflect matrix-producing cell activity, but a causal role in the shared bone and stem-cell module remains to be tested.

## Module 2

**Tissue pair**: bone and stem_cells  
**Genes (7)**: CAPRIN1, CTNNA1, SHMT1, NPM3, PRR14L, PTMS, SLC12A7

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway assignment from enrichment analysis. The annotated genes instead span several biological themes: SHMT1 supports cytosolic one-carbon metabolism and nucleotide precursor production; CAPRIN1 is associated with RNA regulation and stress-granule biology; NPM3 is a nuclear chaperone-related protein associated with chromatin remodeling; CTNNA1 supports cadherin adhesion and mechanosensing; and SLC12A7 supports ion and chloride transport. The co-abundance graph links these otherwise heterogeneous functions, but the pattern should be interpreted as a co-regulation or shared-cellular-context signal rather than proof of a single biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: all listed genes are annotated as non-secreted. It is also not strongly blood-cell enriched, because nearly all genes have low immune cell specificity and only PTMS is immune-cell enriched, in basophils. Several genes have low tissue specificity, which is compatible with broadly expressed or housekeeping-like behavior, while the cell-type annotations are diverse and include germ-cell, epithelial, stromal, muscle, and renal cell types. Liver, kidney, and heart-muscle tissue enhancement further suggests that the module is not a specific bone or stem-cell signature based on HPA evidence alone. Shared cell composition, general cellular state, or sample-related effects therefore remain plausible explanations. HPA protein-detection evidence is unavailable for the matching bone and stem-cell tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction was detected among the module genes, and no hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported here by known physical interactions or membership in a recognized multiprotein complex. This does not disprove functional coordination: co-abundance can arise through shared regulation, cell state, indirect pathway coupling, or cellular composition. It does mean that the network should not be described as a validated protein-interaction complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The specific conserved co-abundance pattern may represent a novel observation because it is not recapitulated by the available high-confidence STRING or hu.MAP evidence. However, absence from those resources alone cannot establish novelty, and the lack of globally significant GO or KEGG enrichment makes a new pathway claim premature. The most defensible interpretation is a potentially new cross-tissue co-abundance association requiring replication in independent cohorts, control for cell-type composition, and experimental or perturbational validation.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program that couples biosynthetic capacity and nuclear or RNA regulation with adhesion, mechanosensing, and ion homeostasis. SHMT1 could represent metabolic support for nucleotide and methyl-group-related demands, while CAPRIN1 and NPM3 could reflect post-transcriptional and nuclear organization states. CTNNA1 and SLC12A7 could capture the mechanical and ionic conditions of the participating cells. PRR14L may act as a co-abundance hub linking these otherwise distinct components. This is a mechanistic hypothesis, not an established pathway assignment; an alternative explanation is shared abundance of broadly expressed genes or mixed cell populations.

### Important genes

#### PRR14L

- **Related proteins** (co-abundance neighbors): CAPRIN1 (0.91), PTMS (0.89), NPM3 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proline rich 14 like
- **Diseases (Open Targets)**: musculoskeletal system disorder (0.343); type 2 diabetes mellitus (0.260); cervical carcinoma (0.239); Abnormality of the skeletal system (0.209); flatulence (0.207)
- **Europe PMC papers**: 108
- **Why important**: PRR14L is the topological hub of the module, connecting CAPRIN1, PTMS, and NPM3. Its annotation is limited to a proline-rich protein identity, but its central network position makes it important for testing whether the module is organized around a regulatory scaffold. Its disease associations include musculoskeletal and skeletal-system abnormalities, which are relevant to the tissue pair, although the evidence is associative and its literature base is comparatively limited.
- **Conclusion**: Established: PRR14L is the most connected module member and has reported musculoskeletal associations. Hypothesis: it may coordinate the module or mark the underlying cellular state, but a causal role is not established.

#### CAPRIN1

- **Related proteins** (co-abundance neighbors): PRR14L (0.91), SLC12A7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cell cycle associated protein 1. Enables RNA binding activity. Predicted to be involved in negative regulation of translation and positive regulation of dendritic spine morphogenesis. Located in cell leading edge and cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with language impairment, autism, and attention deficit-hyperactivity disorder (0.692); neurodegeneration, childhood-onset, with cerebellar ataxia and cognitive decline (0.677); complex neurodevelopmental disorder (0.370); juvenile myoclonic epilepsy (0.340); Seizure (0.333)
- **Europe PMC papers**: 1194
- **Why important**: CAPRIN1 is a network bridge between PRR14L and SLC12A7 and has substantially broader functional annotation and literature than PRR14L. It is associated with RNA binding, translation control, stress-granule assembly, and dendritic or cellular morphology. Its cell-type enhancement in spermatogenic cells shows that its expression context is not specific to bone or stem cells. Its neurodevelopmental and seizure-related disease associations indicate biological importance but do not identify the module function.
- **Conclusion**: Established: CAPRIN1 participates in RNA-regulatory and membraneless-organelle processes and occupies a bridging position in this graph. Hypothesis: it could connect RNA or stress state to ion and cellular-architecture changes in the module.

#### SHMT1

- **Related proteins** (co-abundance neighbors): CTNNA1 (0.89), NPM3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 1. This gene encodes the cytosolic form of serine hydroxymethyltransferase, a pyridoxal phosphate-containing enzyme that catalyzes the reversible conversion of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. This reaction provides one-carbon units for synthesis of methionine, thymidylate, and purines in the cytoplasm. This gene is located within the Smith-Magenis syndrome …
- **Diseases (Open Targets)**: neurodegenerative disease (0.458); Parkinson disease (0.351); Alzheimer disease (0.350); lysosomal storage disease (0.346); preeclampsia (0.314)
- **Europe PMC papers**: 2070
- **Why important**: SHMT1 is the metabolic branch point linking CTNNA1 and NPM3. It encodes the cytosolic serine hydroxymethyltransferase that generates glycine and one-carbon units used in methionine, thymidylate, and purine production. Its tissue enhancement in liver and kidney and cell enrichment in proximal tubule cells argue for a metabolically informative signal, but not a bone-specific one. It has extensive literature and disease associations involving neurodegenerative and developmental conditions.
- **Conclusion**: Established: SHMT1 supports cytosolic one-carbon metabolism and nucleotide precursor biosynthesis. Hypothesis: its co-abundance may indicate proliferative or biosynthetic demand in a shared cell state, but enrichment does not establish that metabolism drives the complete module.

#### CTNNA1

- **Related proteins** (co-abundance neighbors): SHMT1 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin alpha 1. This gene encodes a member of the catenin family of proteins that play an important role in cell adhesion process by connecting cadherins located on the plasma membrane to the actin filaments inside the cell. The encoded mechanosensing protein contains three vinculin homology domains and undergoes conformational changes in response to cytoskeletal tension, resulting in the reconfiguration of cadhe…
- **Diseases (Open Targets)**: Butterfly-shaped pigment dystrophy (0.750); hereditary neoplastic syndrome (0.557); hereditary diffuse gastric adenocarcinoma (0.555); colorectal cancer (0.506); exudative vitreoretinopathy (0.390)
- **Europe PMC papers**: 2688
- **Why important**: CTNNA1 connects SHMT1 to a distinct structural theme. It links cadherins to actin, functions in cell adhesion and mechanosensing, and is located at the plasma membrane and cell junctions. Its disease associations include pigment dystrophy, hereditary neoplastic syndromes, and gastric cancer, and it has a substantial literature base. Its epithelial cell-type enhancement is consistent with a possible cell-architecture or composition signal.
- **Conclusion**: Established: CTNNA1 is an adhesion and mechanosensing component with disease-relevant functions. Hypothesis: it may connect tissue architecture or mechanical state to the metabolic and nuclear features of the module; the present data do not demonstrate that mechanism.

#### SLC12A7

- **Related proteins** (co-abundance neighbors): CAPRIN1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 12 member 7. Enables protein kinase binding activity. Predicted to be involved in several processes, including cell volume homeostasis; inorganic ion homeostasis; and inorganic ion transmembrane transport. Part of protein-containing complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: clonal hematopoiesis (0.462); myasthenia gravis (0.342); edema (0.233); brain compression (0.233); preeclampsia (0.198)
- **Europe PMC papers**: 577
- **Why important**: SLC12A7 is the terminal network member connected to CAPRIN1 and represents ion and volume homeostasis, chloride transport, and potassium transport. Its enhancement in heart muscle and several epithelial or excitable-cell types suggests that it may report a general physiological-state or cell-composition effect rather than a bone-specific function. It also has disease associations involving clonal hematopoiesis, neuromuscular disease, edema, and preeclampsia, with a meaningful literature base.
- **Conclusion**: Established: SLC12A7 contributes to transmembrane ion transport and cell-volume regulation. Hypothesis: it may couple osmotic or ionic state to RNA-regulatory and structural programs in the module, but the co-abundance data do not establish direct regulation or interaction.
