# Conserved co-abundance modules: brain and placenta

## Module 0

**Tissue pair**: brain and placenta  
**Genes (8)**: AHNAK, CALU, CAPN2, FASN, FLNA, FLNB, IQGAP1, TLN1

### Function

The module is most consistent with a cell-adhesion and actin-cytoskeleton remodeling program that links membrane-associated scaffolding, integrin-related attachment, cell shape, migration, and mechanically responsive tissue organization. FLNA, FLNB, TLN1, and IQGAP1 provide convergent evidence for cytoskeletal–membrane coupling, while CAPN2 can support calcium-responsive cytoskeletal remodeling and proteolysis. AHNAK adds a structural and plasma-membrane-repair component, and CALU adds an endoplasmic-reticulum calcium-binding and protein-folding component. FASN is compatible with a membrane and lipid-biosynthetic context but is less directly connected to the dominant adhesion network. No GO or KEGG term passed global correction; therefore the functional interpretation is driven by the gene annotations, network structure, and supplementary interaction evidence rather than by globally significant pathway enrichment. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module is not dominated by secreted or plasma proteins: the HPA summary identifies only one secretome-associated gene, and the proteins are predominantly intracellular, cytosolic, membrane-associated, focal-adhesion, actin-filament, or endoplasmic-reticulum proteins. Most genes have low tissue specificity, suggesting a broadly distributed structural or cellular program rather than a brain- or placenta-exclusive signature. HPA detects all module proteins in brain and detects most of them in placenta, with CAPN2 and FASN not detected in placenta. The single-cell annotations include extravillous trophoblasts, vascular-related cells, megakaryocytes, and platelets, but the blood-cell summary shows low immune-cell specificity and no recurrent enriched blood-cell category. Thus, blood contamination is not the leading explanation, although vascular, platelet-related, trophoblast, and other shared cell populations could contribute to the conserved signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a coherent adhesion and cytoskeletal core. FLNA is strongly connected with FLNB and TLN1 and also connects with IQGAP1; FLNB connects with TLN1; TLN1 connects with CAPN2 and IQGAP1. These relationships are consistent with known protein-level associations and indicate that part of the co-abundance module recapitulates an established cytoskeletal network rather than an arbitrary gene set. The supplementary STRING tissue result (STRING TISSUES Gut; within-query FDR = 0.016) links FASN, TLN1, FLNA, AHNAK, and FLNB with gut tissue, but it is supplementary and was not corrected across modules, so it should not be treated as global enrichment evidence. hu.MAP provides one partial complex relationship (hu.MAP huMAP3_05674.1), containing FLNB and AHNAK together with membrane, lipid-raft, signaling, and trafficking proteins. The fact that several strong STRING relationships lack a corresponding hu.MAP complex suggests a network of functional associations and shared cellular machinery rather than proof that all module members form one physical complex.

**STRING interactions (score >= 0.7)**: 6 of 28 gene pairs: CAPN2–TLN1 (0.971); FLNA–FLNB (0.979); FLNA–IQGAP1 (0.952); FLNA–TLN1 (0.998); FLNB–TLN1 (0.995); IQGAP1–TLN1 (0.893)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Gut (FDR = 0.016, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05674.1 (FLNB, AHNAK; 2/12)

### Novelty

The module should not be described as a wholly new molecular interaction system, because many of its central relationships are already supported by STRING and the FLNB–AHNAK pairing occurs in hu.MAP (hu.MAP huMAP3_05674.1). Its potentially novel aspect is the conserved co-abundance of this adhesion, cytoskeletal, membrane-repair, calcium-handling, and lipid-associated combination across brain and placenta. That cross-tissue co-abundance configuration may be a new systems-level observation, but novelty cannot be established from the fact that some relationships are absent from hu.MAP or STRING. The lack of globally significant GO or KEGG enrichment also limits claims of a newly discovered pathway. Independent replication, comparison with published brain–placenta co-abundance modules, and testing in purified cell populations would be needed to establish novelty.

**Hypothesis.** Hypothesis: the module represents a conserved membrane–cytoskeleton remodeling state shared by selected brain and placental cells, especially vascular, trophoblast, and mechanically active adherent cells. In this model, FLNA and FLNB organize actin-linked membrane structures, TLN1 couples integrins to the cytoskeleton, IQGAP1 coordinates adhesion and signaling, AHNAK supports membrane architecture and repair, CAPN2 provides calcium-responsive remodeling, CALU supports endoplasmic-reticulum calcium and protein handling, and FASN supplies lipid biosynthetic capacity for membrane maintenance. The shared signal could therefore reflect common requirements for adhesion, migration, barrier or junction organization, and adaptation to mechanical or membrane stress. This is a mechanistic hypothesis, not an experimentally established causal pathway.

### Important genes

#### FLNA

- **Related proteins** (co-abundance neighbors): CALU (0.83), FLNB (0.83); STRING partners: FLNB (0.979), IQGAP1 (0.952), TLN1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in brain, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a central network connector within the module and has strong STRING relationships with FLNB, TLN1, and IQGAP1. Its annotation as an actin crosslinker and membrane-glycoprotein linker directly matches the dominant adhesion and cytoskeletal interpretation. It is detected in both tissues, has vascular and intestinal tissue enhancement, appears in several relevant cell types including decidual stromal cells and megakaryocytes, and has extensive disease and literature support including cerebral cortical developmental disorders.
- **Conclusion**: Established evidence supports FLNA as a core actin–membrane scaffold and a major anchor of the module. Its presence is compatible with shared adhesion, migration, vascular, and tissue-architecture biology in brain and placenta. It is a strong mechanistic candidate, but the module does not establish that FLNA causes the cross-tissue co-abundance pattern.

#### FLNB

- **Related proteins** (co-abundance neighbors): CAPN2 (0.83), FLNA (0.83), AHNAK (0.82), CALU (0.81); STRING partners: FLNA (0.979), TLN1 (0.995)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in brain, placenta
- **hu.MAP 3.0**: huMAP3_05674.1
- **Function (MyGene.info)**: filamin B. This gene encodes a member of the filamin family. The encoded protein interacts with glycoprotein Ib alpha as part of the process to repair vascular injuries. The platelet glycoprotein Ib complex includes glycoprotein Ib alpha, and it binds the actin cytoskeleton. Mutations in this gene have been found in several conditions: atelosteogenesis type 1 and type 3; boomerang dysplasia; autosomal domina…
- **Diseases (Open Targets)**: Larsen syndrome (0.829); spondylocarpotarsal synostosis syndrome (0.775); atelosteogenesis type I (0.763); atelosteogenesis type III (0.756); Boomerang dysplasia (0.723)
- **Europe PMC papers**: 2274
- **Why important**: FLNB has the greatest network connectivity in the module and links CAPN2, FLNA, AHNAK, and CALU. It is a filamin-family actin-associated protein involved in vascular-injury repair through interaction with the platelet glycoprotein Ib complex. It is detected in brain and placenta, is associated with extravillous trophoblasts, and has well-established developmental disease associations including Larsen syndrome and skeletal dysplasias. It also participates in the partial hu.MAP complex with AHNAK (hu.MAP huMAP3_05674.1).
- **Conclusion**: Established evidence identifies FLNB as a central structural organizer with vascular, platelet-interface, and developmental relevance. Its network position makes it a plausible integrator of the module. A specific role in coordinating the brain–placenta shared state remains a hypothesis.

#### TLN1

- **Related proteins** (co-abundance neighbors): IQGAP1 (0.87), AHNAK (0.84); STRING partners: CAPN2 (0.971), FLNA (0.998), FLNB (0.995), IQGAP1 (0.893)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in brain, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 connects IQGAP1 and AHNAK in the module and has strong STRING associations with CAPN2, FLNA, FLNB, and IQGAP1. Its established functions in integrin activation, cell adhesion, cell–cell junction assembly, actin organization, and cell migration provide a direct functional bridge between the network and the proposed module function. HPA places it in focal adhesions and associates it with megakaryocytes and platelets as well as blood vessels, while detecting it in both tissues.
- **Conclusion**: Established evidence supports TLN1 as a key adhesion and integrin-coupling component. The data support interpreting it as a functional core of the conserved module, particularly in mechanically attached or migratory cells. The contribution of platelet-associated expression versus tissue-cell expression cannot be resolved from this module alone.

#### IQGAP1

- **Related proteins** (co-abundance neighbors): TLN1 (0.87), FASN (0.82); STRING partners: FLNA (0.952), TLN1 (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in brain, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 1. This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer ce…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.515); Costello syndrome (0.503); allergic rhinitis (0.474)
- **Europe PMC papers**: 3787
- **Why important**: IQGAP1 links TLN1 and FASN in the module and is additionally supported by STRING relationships with FLNA and TLN1. Its domains and annotations connect cytoskeletal organization with cell-adhesion molecules, MAPK and growth-factor signaling, cell morphology, and migration. It is detected in both tissues and has cell-type enhancement in neutrophils, although the overall HPA blood-cell summary does not support a broad immune-cell signature.
- **Conclusion**: Established evidence supports IQGAP1 as a signaling and cytoskeletal coordinator that can connect adhesion to cell morphology and migration. Its position makes it a plausible bridge between the structural core and FASN-associated membrane or metabolic biology. Whether it actively regulates this conserved module in brain and placenta is not established.

#### AHNAK

- **Related proteins** (co-abundance neighbors): TLN1 (0.84), FLNB (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in brain, placenta
- **hu.MAP 3.0**: huMAP3_05674.1
- **Function (MyGene.info)**: AHNAK nucleoprotein. The protein encoded by this gene is a large (700 kDa) structural scaffold protein consisting of a central domain with 128 aa repeats. The encoded protein may play a role in such diverse processes as blood-brain barrier formation, cell structure and migration, cardiac calcium channel regulation, and tumor metastasis. A much shorter variant encoding a 17 kDa isoform exists for this gene, and the sho…
- **Diseases (Open Targets)**: Aganglionic megacolon (0.266); neoplasm (0.108); hepatocellular carcinoma (0.093); cancer (0.085); melanoma (0.085)
- **Europe PMC papers**: 2886
- **Why important**: AHNAK connects TLN1 and FLNB, participates with FLNB in the hu.MAP complex (hu.MAP huMAP3_05674.1), and is included in the supplementary STRING tissue result (STRING TISSUES Gut; within-query FDR = 0.016). Its annotation describes a large membrane-associated structural scaffold implicated in blood–brain barrier formation, cell structure, migration, and plasma-membrane repair. It is detected in both tissues and has cell-type enhancement in epithelial and Schwann-cell populations.
- **Conclusion**: Established evidence supports AHNAK as a large structural scaffold with plausible roles in membrane integrity, repair, barrier biology, and migration. Its pairing with FLNB provides independent complex-level support for the module's structural interpretation. The proposed role in coordinating brain and placental barrier or trophoblast mechanics remains a hypothesis.

## Module 1

**Tissue pair**: brain and placenta  
**Genes (9)**: ANXA1, ANXA5, HSPA5, GANAB, HYOU1, PDIA4, PDLIM1, PRDX4, TXNDC5

### Function

The strongest interpretation is endoplasmic-reticulum protein quality control, folding, disulfide-bond formation, glycan processing, and stress adaptation. (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0302) is the only GO/KEGG term passing global correction and links GANAB, HSPA5, HYOU1, PDIA4, and TXNDC5 to protein processing in the endoplasmic reticulum. The supplementary STRING results independently support ER localization, protein disulfide-isomerase activity, unfolded-protein-response biology, and stress-related ER interactions (4 supplementary STRING terms; within-query FDR 0.0012–0.0261). The annexin genes and PDLIM1 broaden the module toward membrane, cytoskeletal, inflammatory, and cell-state biology, but they do not override the coherent ER-centered signal.

**Cell composition.** HPA summarizes the module as containing mostly secreted genes, but the principal functional core is largely composed of intracellular or ER proteins rather than a simple plasma-protein signature. ANXA1 is explicitly secreted to blood, whereas PDIA4, HSPA5, GANAB, PRDX4, TXNDC5, and PDLIM1 are annotated as intracellular, membrane-associated, or ER-localized. Most genes have low immune-cell specificity, arguing against a purely blood-cell module, although plasma-cell, B-cell, trophoblast, and related cell-type enrichments indicate that cellular composition could contribute to the shared brain–placenta pattern. Detection of every module protein in both brain and placenta supports biological presence in both tissues, but does not establish that the co-abundance relationship is intrinsic to the same cell type in each tissue.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.0302 | GANAB, HSPA5, HYOU1, PDIA4, TXNDC5 |

### STRING and hu.MAP

STRING provides known support for an ER quality-control network. HSPA5 is strongly connected with HYOU1 and PDIA4, GANAB connects with HSPA5, HYOU1, and PDIA4, and PRDX4 is strongly connected with TXNDC5; these relationships are consistent with chaperoning, disulfide processing, and redox control. The STRING enrichment terms (4 supplementary STRING terms; within-query FDR 0.0012–0.0261) are supplementary and should not be interpreted as additional globally corrected evidence. hu.MAP places PDIA4, GANAB, and HYOU1 together in complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), while HSPA5 and HYOU1 occur together in (hu.MAP huMAP3_07455.1). These complexes support the interpretation that part of the module reflects known molecular machinery, although the complexes are broad and include many proteins not in the module. ANXA1, ANXA5, and PDLIM1 have no reported STRING or hu.MAP relationships within the supplied evidence, so their co-abundance links may reflect shared cellular state, tissue composition, or relationships not represented in those resources.

**STRING interactions (score >= 0.7)**: 8 of 36 gene pairs: GANAB–HSPA5 (0.846); GANAB–HYOU1 (0.83); GANAB–PDIA4 (0.717); HSPA5–HYOU1 (0.999); HSPA5–PDIA4 (0.99); HSPA5–TXNDC5 (0.798); HYOU1–PDIA4 (0.997); PRDX4–TXNDC5 (0.994)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Protein disulfide isomerase activity (FDR = 0.0012, 5 genes); Keyword Endoplasmic reticulum (FDR = 0.0016, 6 genes); KEGG Protein processing in endoplasmic reticulum (FDR = 0.0115, 5 genes); NetworkNeighborAL Photodynamic therapy-induced unfolded protein response, and IRE1-TRAF2-ASK1 complex (FDR = 0.0261, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PDIA4, GANAB, HYOU1; 3/60); huMAP3_09327.1 (PDIA4, GANAB, HYOU1; 3/93); huMAP3_07455.1 (HSPA5, HYOU1; 2/4)

### Novelty

The ER quality-control biology is not a new molecular concept: the core genes have established functions, STRING relationships, and partial hu.MAP support. The potentially new result is the conserved co-abundance of this particular combination across brain and placenta, especially the inclusion of annexins and PDLIM1 alongside the ER core. However, the supplied evidence does not establish that this tissue-pair module has never been reported elsewhere. Lack of a STRING or hu.MAP relationship for some genes cannot by itself demonstrate novelty. The most defensible conclusion is that the module is a potentially dataset-specific or context-specific conserved network built around known ER stress and secretory pathway biology.

**Hypothesis.** Hypothesis: the module represents a shared secretory and stress-adaptation program active in selected brain and placental cell populations. HSPA5 and HYOU1 could provide chaperone capacity, GANAB could support glycan maturation, PDIA4 and TXNDC5 could catalyze disulfide rearrangement, and PRDX4 could help control ER oxidative conditions. ANXA1, ANXA5, and PDLIM1 may couple this secretory stress state to membrane signaling, inflammatory or trophoblast-associated cell behavior, and cytoskeletal organization. A composition-based explanation remains plausible because HPA points to trophoblast and plasma-cell enrichment; testing this hypothesis would require cell-resolved co-expression, perturbation of ER stress or secretory pathways, and validation in independent brain and placenta cohorts.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): PRDX4 (0.89), GANAB (0.87), HYOU1 (0.82), TXNDC5 (0.80); STRING partners: GANAB (0.846), HYOU1 (0.999), PDIA4 (0.99), TXNDC5 (0.798)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in brain, placenta
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a highly connected central node in the module and is linked by STRING to GANAB, HYOU1, PDIA4, and TXNDC5. It is an ER HSP70 chaperone and master regulator of ER homeostasis, appears in the globally supported term (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0302) and all supplied STRING enrichment terms (4 supplementary STRING terms; within-query FDR 0.0012–0.0261), and is represented in hu.MAP complex (hu.MAP huMAP3_07455.1). Its large literature base and disease associations make it the best-established functional anchor.
- **Conclusion**: Established evidence supports HSPA5 as a central ER folding and stress regulator in this module. It is a plausible driver of the observed co-abundance pattern, but the fact sheet does not prove that HSPA5 causes the tissue-pair module.

#### PDIA4

- **Related proteins** (co-abundance neighbors): ANXA1 (0.89), ANXA5 (0.86), GANAB (0.85), PRDX4 (0.82); STRING partners: GANAB (0.717), HSPA5 (0.99), HYOU1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain, placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is among the most connected module nodes and links the ER core to GANAB, HSPA5, HYOU1, and the annexins in the co-abundance graph. It is an ER protein-disulfide isomerase with multiple thioredoxin domains, supports protein folding and antibody assembly, appears in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0302) and (4 supplementary STRING terms; within-query FDR 0.0012–0.0261), and occurs in hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its disease associations and substantial literature support make it an important candidate for secretory and proteostasis biology.
- **Conclusion**: Established evidence identifies PDIA4 as a core ER disulfide-processing component. Its connection to ANXA1 and ANXA5 in the module suggests a possible interface with membrane-associated biology, but that interface is a hypothesis rather than an established mechanism here.

#### GANAB

- **Related proteins** (co-abundance neighbors): HSPA5 (0.87), PDIA4 (0.85), ANXA5 (0.82), PRDX4 (0.81); STRING partners: HSPA5 (0.846), HYOU1 (0.83), PDIA4 (0.717)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in brain, placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB is a highly connected ER node associated with HSPA5, HYOU1, PDIA4, and ANXA5. Its glucosidase-II function supports N-glycan processing and quality control of immature glycoproteins. It contributes to (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0302), (STRING Keyword Endoplasmic reticulum; within-query FDR = 0.0016), and (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0115) and is present with PDIA4 and HYOU1 in hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its established link to autosomal-dominant polycystic kidney and liver disease adds disease relevance.
- **Conclusion**: Established evidence supports GANAB as the glycan-processing component of the ER quality-control core. Its co-abundance with the chaperone and disulfide-isomerase genes is consistent with coordinated glycoprotein maturation, although the module does not demonstrate direct regulation among these proteins.

#### HYOU1

- **Related proteins** (co-abundance neighbors): HSPA5 (0.82); STRING partners: GANAB (0.83), HSPA5 (0.999), PDIA4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in brain, placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1, huMAP3_07455.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is a stress-inducible ER HSP70-family protein with documented roles in hypoxia, ER stress, folding, secretion, vesicle transport, and survival. It is strongly connected to HSPA5 and also connects to GANAB and PDIA4 in STRING. It appears in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0302) and (4 supplementary STRING terms; within-query FDR 0.0012–0.0261) and occurs in all supplied hu.MAP complexes (hu.MAP huMAP3_06775.1) (hu.MAP huMAP3_09327.1) (hu.MAP huMAP3_07455.1), making it a bridge between the ER quality-control signals and stress adaptation.
- **Conclusion**: Established evidence supports HYOU1 as the module's hypoxia- and stress-responsive component. Its presence in brain and placenta is compatible with a shared adaptation to secretory or metabolic stress, but the specific physiological trigger remains unresolved.

#### TXNDC5

- **Related proteins** (co-abundance neighbors): PDLIM1 (0.86), HSPA5 (0.80); STRING partners: HSPA5 (0.798), PRDX4 (0.994)
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Endoplasmic reticulum; IHC detected in brain, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role ma…
- **Diseases (Open Targets)**: colorectal carcinoma (0.321); spinal stenosis (0.203); neoplasm (0.096); central nervous system cancer (0.092); glioma (0.091)
- **Europe PMC papers**: 1026
- **Why important**: TXNDC5 is an ER thioredoxin-family protein involved in disulfide isomerization, protein folding, and protection from hypoxia-associated cell death. It contributes to (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.0302) and (STRING NetworkNeighborAL Mixed, incl. Photodynamic therapy-induced unfolded protein response, and Protein disulfide isomerase activity; within-query FDR = 0.0012) (STRING Keyword Endoplasmic reticulum; within-query FDR = 0.0016) (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0115), has a strong STRING relationship with PRDX4 and a relationship with HSPA5, and connects the ER core to the module's redox dimension. Its hypoxia-related biology and disease associations make it informative despite its more peripheral module position.
- **Conclusion**: Established evidence supports TXNDC5 as a redox and disulfide-folding component of the ER program. Its link with PRDX4 suggests coordinated oxidative-stress handling, but whether that relationship explains the brain–placenta conservation is a hypothesis.
