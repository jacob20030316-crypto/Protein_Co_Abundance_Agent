# Conserved co-abundance modules: cervix_uterine and placenta

## Module 0

**Tissue pair**: cervix_uterine and placenta  
**Genes (8)**: ACTN1, CAPN2, CD44, CORO1C, FLNA, ITGB1, PDLIM5, WDR1

### Function

The strongest primary evidence indicates a cell-shape and cytoskeletal remodeling module centered on cell projections. The globally corrected terms support cell morphogenesis (GO:BP cell morphogenesis; q_global = 0.0107) and cell projection (GO:CC cell projection; q_global = 0.0387), while the synapse term (GO:CC synapse; q_global = 0.0066) is best interpreted cautiously as an annotation shared by actin- and adhesion-related proteins rather than evidence that the module is neuronal. The genes collectively support actin organization, membrane anchoring, cell adhesion, migration, and junctional remodeling. STRING supplementary results independently point to cell projections, cell junctions, and anchoring junctions (4 supplementary STRING terms; within-query FDR 0.0101–0.0154). The sparse network is nevertheless biologically coherent because several edges connect integrin, actin-crosslinking, actin-remodeling, and adhesion components.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only CD44 is annotated as secreted to blood, and the other genes are intracellular or membrane-associated. Most genes have low tissue specificity, while all have cell-type-enhanced HPA expression. Platelets are the most recurrent enriched single-cell type, with additional signals involving neutrophils, megakaryocytes, smooth muscle, trophoblast-related cells, and other structural cell types. ACTN1, WDR1, and CORO1C have platelet or neutrophil-related evidence, and PDLIM5 has immune-cell enrichment for basophils. Thus, the shared module could reflect a conserved structural program in cervix and placenta, but contribution from blood-derived cells or platelet-associated material should be considered, especially because protein detection is broadly present in both tissues and the module is not tissue-specific.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC synapse | 0.0066 | ACTN1, CAPN2, CORO1C, FLNA, ITGB1, PDLIM5, WDR1 |
| GO:BP cell morphogenesis | 0.0107 | ACTN1, CD44, CORO1C, FLNA, ITGB1, PDLIM5, WDR1 |
| GO:CC cell projection | 0.0387 | ACTN1, CAPN2, CD44, CORO1C, FLNA, ITGB1, PDLIM5, WDR1 |

### STRING and hu.MAP

STRING supports established relationships among ACTN1, FLNA, ITGB1, CD44, and WDR1. In particular, ITGB1 is strongly connected to ACTN1, CD44, and FLNA, while FLNA connects to ACTN1 and WDR1. These relationships provide external support for an integrin–actin adhesion network rather than an arbitrary co-abundance grouping. CAPN2 and CORO1C have no listed STRING partners within this module despite their biological annotations and module connectivity. hu.MAP provides partial complex-level support: WDR1 and CORO1C occur together in an actin-remodeling-related complex (hu.MAP huMAP3_11076.1), and WDR1 and ACTN1 occur together in a larger membrane, cytoskeletal, and signaling complex (hu.MAP huMAP3_09165.1). Because only a small subset of each hu.MAP complex is represented, the module should not be treated as a complete purified complex. Overall, the evidence supports a functional interaction neighborhood composed of several known physical or curated relationships, not necessarily one discrete molecular complex.

**STRING interactions (score >= 0.7)**: 5 of 28 gene pairs: ACTN1–FLNA (0.716); ACTN1–ITGB1 (0.974); CD44–ITGB1 (0.957); FLNA–ITGB1 (0.993); FLNA–WDR1 (0.874)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Cell projection (FDR = 0.0101, 8 genes); COMPARTMENTS Cell junction (FDR = 0.0106, 8 genes); Keyword Cell projection (FDR = 0.0114, 6 genes); Component Anchoring junction (FDR = 0.0154, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11076.1 (WDR1, CORO1C; 2/10); huMAP3_09165.1 (WDR1, ACTN1; 2/39)

### Novelty

The exact shared co-abundance module may be a new observation for the cervix–placenta tissue pair, but the available evidence does not establish that it is a wholly new biological mechanism. Several of its relationships and functional themes are already represented in STRING and hu.MAP, particularly the integrin–actin–filamin connections and the WDR1-associated complexes. Absence of some genes from STRING or hu.MAP does not demonstrate novelty. A defensible conclusion is that the tissue-pair co-abundance pattern may be novel, whereas the underlying adhesion and cytoskeletal biology is established. Demonstrating module-level novelty would require a systematic comparison with published tissue co-expression modules, prior cervix and placenta studies, and independent cohorts.

**Hypothesis.** Hypothesis: the module represents a conserved cell-projection and adhesion-remodeling program shared by structural or interface-forming cells in cervix and placenta. ITGB1 and CD44 could provide membrane adhesion and extracellular-matrix or hyaluronan-linked signaling, FLNA and ACTN1 could mechanically couple membrane receptors to actin, and CORO1C, WDR1, and CAPN2 could regulate actin turnover and remodeling. PDLIM5 may help organize signaling or cytoskeletal components in specialized structural cells. In placenta, this program could support trophoblast or vascular-interface remodeling; in cervix, it could support epithelial, stromal, vascular, or smooth-muscle architecture. The platelet enrichment means an alternative or additional explanation is contribution from platelet-associated material or blood-derived cells, which should be tested with cell-resolved expression and histological localization rather than inferred from co-abundance alone.

### Important genes

#### ITGB1

- **Related proteins** (co-abundance neighbors): CAPN2 (0.88), CORO1C (0.81); STRING partners: ACTN1 (0.974), CD44 (0.957), FLNA (0.993)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin subunit beta 1. Integrins are heterodimeric proteins made up of alpha and beta subunits. At least 18 alpha and 8 beta subunits have been described in mammals. Integrin family members are membrane receptors involved in cell adhesion and recognition in a variety of processes including embryogenesis, hemostasis, tissue repair, immune response and metastatic diffusion of tumor cells. This gene encodes a beta subunit.…
- **Diseases (Open Targets)**: Crohn disease (0.560); viral infectious disease (0.527); inflammation (0.371); Anisometropia (0.331); type 1 diabetes mellitus (0.323)
- **Europe PMC papers**: 12192
- **Why important**: ITGB1 is a central membrane adhesion receptor in the module, connected to CAPN2 and CORO1C in the co-abundance graph and to ACTN1, CD44, and FLNA in STRING. Its HPA localization at the plasma membrane and focal adhesions, together with established roles in cell adhesion, embryogenesis, angiogenesis, phagocytosis, and tissue repair, makes it a strong mechanistic anchor. It also has a large literature base and disease associations involving inflammation and tissue pathology.
- **Conclusion**: Established evidence supports ITGB1 as a major adhesion and mechanotransduction component of the module. Its role as the initiating driver of the tissue-pair pattern remains a hypothesis because co-abundance does not establish causality.

#### FLNA

- **Related proteins** (co-abundance neighbors): CAPN2 (0.81); STRING partners: ACTN1 (0.716), ITGB1 (0.993), WDR1 (0.874)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is an actin crosslinker that links actin filaments to membrane glycoproteins and interacts with integrins and receptor complexes. It is connected in STRING to ITGB1, ACTN1, and WDR1, and its module annotations pass all primary global terms (GO:CC synapse; q_global = 0.0066) (GO:BP cell morphogenesis; q_global = 0.0107) (GO:CC cell projection; q_global = 0.0387). Its HPA evidence includes blood-vessel, intestinal, placental, and several structural cell contexts. It has extensive literature and well-established disease associations involving cytoskeletal and developmental abnormalities.
- **Conclusion**: Established evidence supports FLNA as a structural bridge between adhesion receptors and the actin cytoskeleton. Its placement in this shared module is consistent with coordinated cell-shape and migration control, but a specific cervix–placenta mechanism is not directly demonstrated.

#### CORO1C

- **Related proteins** (co-abundance neighbors): WDR1 (0.82), ITGB1 (0.81), CD44 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: huMAP3_11076.1
- **Function (MyGene.info)**: coronin 1C. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.453); Parkinson disease (0.322); Alzheimer disease (0.312); lysosomal storage disease (0.310); liver disorder (0.261)
- **Europe PMC papers**: 774
- **Why important**: CORO1C has the strongest weighted connectivity in the module and links WDR1, ITGB1, and CD44 in the co-abundance graph. It appears in every primary globally corrected term (GO:CC synapse; q_global = 0.0066) (GO:BP cell morphogenesis; q_global = 0.0107) (GO:CC cell projection; q_global = 0.0387) and every STRING supplementary category (4 supplementary STRING terms; within-query FDR 0.0101–0.0154). Its WD-repeat architecture and annotations involving actin organization, phagocytosis, migration-related biology, and signaling fit a role in dynamic actin remodeling. It also has disease associations involving neurodegenerative and lysosomal disorders and a substantial literature base.
- **Conclusion**: Established evidence supports CORO1C as a likely organizational hub for the actin-remodeling aspect of the module. Its exact molecular role in cervix and placenta is a hypothesis, particularly because it lacks a listed STRING partner within this module.

#### ACTN1

- **Related proteins** (co-abundance neighbors): WDR1 (0.82); STRING partners: FLNA (0.716), ITGB1 (0.974)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Actin filaments, Focal adhesion sites; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: huMAP3_09165.1
- **Function (MyGene.info)**: actinin alpha 1. Alpha actinins belong to the spectrin gene superfamily which represents a diverse group of cytoskeletal proteins, including the alpha and beta spectrins and dystrophins. Alpha actinin is an actin-binding protein with multiple roles in different cell types. In nonmuscle cells, the cytoskeletal isoform is found along microfilament bundles and adherens-type junctions, where it is involved in binding …
- **Diseases (Open Targets)**: platelet-type bleeding disorder 15 (0.781); Macrothrombocytopenia (0.622); autosomal dominant macrothrombocytopenia (0.550); Thrombocytopenia (0.482); type 2 diabetes mellitus (0.410)
- **Europe PMC papers**: 3070
- **Why important**: ACTN1 connects to WDR1 in the module and to FLNA and ITGB1 in STRING. It binds and organizes actin at microfilament bundles and adherens-type junctions, and its HPA evidence includes smooth muscle, trophoblast-related cells, neutrophils, and platelets. Its primary annotations cover actin organization, platelet activation, platelet formation, and platelet morphogenesis, and it has strong disease associations involving inherited platelet disorders.
- **Conclusion**: Established evidence supports ACTN1 as an actin–membrane and junctional scaffold that can explain both the projection signature and the platelet-associated HPA signal. Whether its abundance primarily reflects tissue structural cells or platelet contribution is unresolved.

#### WDR1

- **Related proteins** (co-abundance neighbors): CORO1C (0.82), ACTN1 (0.82); STRING partners: FLNA (0.874)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Cytosol; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: huMAP3_11076.1, huMAP3_09165.1
- **Function (MyGene.info)**: WD repeat domain 1. This gene encodes a protein containing 9 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, mostly including a trp-asp at the C-terminal end. WD domains are involved in protein-protein interactions. The encoded protein may help induce the disassembly of actin filaments. Two transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: periodic fever, immunodeficiency, and thrombocytopenia syndrome (0.705); gout (0.528); neurodegenerative disease (0.526); atrial fibrillation (0.519); intellectual developmental disorder 61 (0.416)
- **Europe PMC papers**: 1861
- **Why important**: WDR1 connects to CORO1C and ACTN1 in the module, to FLNA in STRING, and participates in both hu.MAP complexes (hu.MAP huMAP3_11076.1) (hu.MAP huMAP3_09165.1). Its established functions include actin-filament depolymerization, cortical cytoskeleton organization, platelet formation, and neutrophil-mediated immunity. HPA evidence highlights megakaryocytes and platelets, while its disease associations include thrombocytopenia-related and inflammatory conditions.
- **Conclusion**: Established evidence supports WDR1 as an actin-turnover component linking cytoskeletal remodeling with platelet and immune-cell biology. It is a plausible mediator of the module's dynamic remodeling behavior, but the tissue-level source of its signal remains a hypothesis.

## Module 1

**Tissue pair**: cervix_uterine and placenta  
**Genes (15)**: AHNAK, LAP3, CNDP2, DPYSL2, IQGAP1, ITIH2, LTA4H, MYOF, PDLIM1, PLEC, SEPTIN2, SEPTIN9, SPTBN1, TLN1, TXNDC5

### Function

The strongest functional interpretation is a cytoskeleton-dependent cytokinesis and cell-architecture module. The globally corrected GO evidence (GO:BP cytokinesis; q_global = 0.0493) and (GO:BP cytoskeleton-dependent cytokinesis; q_global = 0.0493) identifies cytokinesis, with IQGAP1, PLEC, SEPTIN2, SEPTIN9, and SPTBN1 contributing to both terms. The network also connects actin, intermediate-filament, microtubule, membrane-adhesion, and septin biology: IQGAP1 regulates cytoskeletal organization and cell morphology; PLEC links cytoskeletal systems; SEPTIN2 and SEPTIN9 participate in septin assemblies and cytokinesis; SPTBN1 connects cortical actin to the plasma membrane; and TLN1 supports integrin-mediated adhesion and cell migration. These annotations support a structural and proliferative interpretation rather than a specialized secretory pathway. No STRING functional-enrichment term was reported, so STRING does not provide an independent pathway-level enrichment signal. The lack of additional globally corrected GO or KEGG terms does not invalidate the module, especially because the cytokinesis signal is coherent across several structurally related genes.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. ITIH2 is secreted to blood, while TXNDC5 is annotated as intracellular and membrane-associated; the remaining proteins are primarily intracellular, cytoskeletal, membrane, or vesicular. Most genes have low tissue specificity, and most have low immune-cell specificity, arguing against a module composed mainly of a single blood-cell population. Nevertheless, the HPA annotations show cell-type enhancement across several epithelial, stromal, vascular, neural, placental, and myeloid populations, including Hofbauer cells and monocytes. PDLIM1 is associated with decidual stromal cells, megakaryocytes, and platelets, while TLN1 is associated with megakaryocytes and platelets. Thus, the shared cervix-uterine and placenta signal may reflect a conserved structural program in adherent tissue cells, with possible contributions from shared stromal, epithelial, vascular, or placental cell types. The high protein detection in both tissues supports biological presence rather than an exclusively technical signal.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cytokinesis | 0.0493 | IQGAP1, PLEC, SEPTIN2, SEPTIN9, SPTBN1 |
| GO:BP cytoskeleton-dependent cytokinesis | 0.0493 | IQGAP1, PLEC, SEPTIN2, SEPTIN9, SPTBN1 |

### STRING and hu.MAP

STRING supports a limited but biologically coherent interaction backbone. The strongest known relationship is SEPTIN2 with SEPTIN9, consistent with a septin complex and the cytokinesis interpretation. IQGAP1 connects to TLN1, and PLEC connects to TLN1 and AHNAK, linking adhesion and cytoskeletal scaffolding. AHNAK also connects to MYOF. These known relationships support parts of the module but do not explain every co-abundance edge, and STRING reported no functional-enrichment term. hu.MAP provides additional complex-level support: SEPTIN2 and SEPTIN9 occur together in a septin complex (hu.MAP huMAP3_02362.1); SPTBN1 and AHNAK occur together in a larger membrane and cytoskeletal complex (hu.MAP huMAP3_09165.1); and PDLIM1, LTA4H, and LAP3 occur together in (hu.MAP huMAP3_14442.1). The confidence of these complexes is heterogeneous, so they should be treated as supporting evidence rather than proof that the entire module is one physical complex. Overall, the module appears to combine several known cytoskeletal and membrane-associated relationships with tissue-level co-abundance relationships that are not yet represented as direct physical interactions.

**STRING interactions (score >= 0.7)**: 5 of 105 gene pairs: AHNAK–MYOF (0.849); AHNAK–PLEC (0.73); IQGAP1–TLN1 (0.893); PLEC–TLN1 (0.706); SEPTIN2–SEPTIN9 (0.997)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PDLIM1, LTA4H, LAP3; 3/57); huMAP3_02362.1 (SEPTIN2, SEPTIN9; 2/14); huMAP3_09165.1 (SPTBN1, AHNAK; 2/39)

### Novelty

The module should not be called a wholly new molecular complex. Several internal relationships are already established by STRING or hu.MAP, especially the SEPTIN2–SEPTIN9 pair and selected cytoskeletal or adhesion associations. However, the conserved co-abundance organization across cervix_uterine and placenta may still be a new systems-level observation, because the databases do not establish this exact tissue-pair module or its complete set of coordinated genes. Absence of many module pairs from STRING and hu.MAP is compatible with tissue-contextual co-regulation, indirect coupling, incomplete interaction coverage, or cell-composition effects; it is not evidence of novelty by itself. The most defensible conclusion is that the module represents a potentially novel cross-tissue co-abundance configuration assembled around partly known cytoskeletal relationships, requiring validation in independent cohorts and cell-resolved data.

**Hypothesis.** Hypothesis: a shared adherent-cell program in cervix_uterine and placenta coordinates cytokinesis with remodeling of cortical actin, intermediate filaments, microtubules, and cell–matrix contacts. In this model, SEPTIN2 and SEPTIN9 organize a cytokinetic scaffold; IQGAP1 couples that scaffold to signaling and membrane organization; SPTBN1 and PLEC stabilize the cortical and intermediate-filament architecture; and TLN1 links the remodeled cytoskeleton to integrin adhesion. AHNAK and MYOF could support membrane organization or repair, while the remaining metabolic and proteolytic genes may reflect the physiological state of the participating cells rather than a single biochemical pathway. This is a mechanistic hypothesis, not an established physical model. A useful test would be cell-resolved co-expression and perturbation experiments examining whether disruption of the septin–IQGAP1–adhesion axis alters cytokinesis and epithelial, stromal, or placental cell architecture.

### Important genes

#### SEPTIN9

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.92), TXNDC5 (0.88), TLN1 (0.85), DPYSL2 (0.83), IQGAP1 (0.83); STRING partners: SEPTIN2 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 9. This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic l…
- **Diseases (Open Targets)**: neuralgic amyotrophy (0.564); hypertensive disorder (0.496); cataract (0.437); essential hypertension (0.426); alcohol drinking (0.420)
- **Europe PMC papers**: 748
- **Why important**: SEPTIN9 is among the most connected genes in the module and links SEPTIN2, TXNDC5, TLN1, DPYSL2, and IQGAP1. It is present in both globally corrected cytokinesis terms (GO:BP cytokinesis; q_global = 0.0493) and (GO:BP cytoskeleton-dependent cytokinesis; q_global = 0.0493), localizes to actin filaments, and forms the strongest STRING-supported pair in the module with SEPTIN2. Its septin biology and substantial literature support make it a central structural and cell-division marker. Disease associations include hereditary neuralgic amyotrophy and leukemia-related rearrangement, showing that altered SEPTIN9 can have clinically relevant consequences.
- **Conclusion**: Established evidence supports SEPTIN9 as a core cytokinesis and cytoskeletal component of the module. It is a strong candidate for an organizing hub, but the tissue-specific causal role of SEPTIN9 in the shared cervix-uterine and placenta program remains a hypothesis.

#### IQGAP1

- **Related proteins** (co-abundance neighbors): PLEC (0.87), SEPTIN9 (0.83), AHNAK (0.83); STRING partners: TLN1 (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 1. This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer ce…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.515); Costello syndrome (0.503); allergic rhinitis (0.474)
- **Europe PMC papers**: 3787
- **Why important**: IQGAP1 is a highly connected bridge linking PLEC, SEPTIN9, AHNAK, and the known STRING partner TLN1. It contributes to (GO:BP cytokinesis; q_global = 0.0493) and (GO:BP cytoskeleton-dependent cytokinesis; q_global = 0.0493), is located at the plasma membrane and cell junctions, and is annotated in cytoskeletal regulation, mitotic control, signaling, and cell migration. Its extensive literature and disease associations involving cancer and developmental signaling make it an important integrator between cytokinesis, adhesion, and cell morphology.
- **Conclusion**: Established evidence supports IQGAP1 as a cytoskeletal and signaling adaptor compatible with the module function. It may connect septin organization to adhesion and migration in these tissues, but that tissue-specific connection is a mechanistic hypothesis rather than a demonstrated fact.

#### PLEC

- **Related proteins** (co-abundance neighbors): IQGAP1 (0.87), DPYSL2 (0.87); STRING partners: AHNAK (0.73), TLN1 (0.706)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments, Cytosol; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plectin. Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 5B, with muscular dystrophy (0.796); epidermolysis bullosa simplex 5A, Ogna type (0.775); autosomal recessive limb-girdle muscular dystrophy type 2Q (0.768); epidermolysis bullosa simplex 5C, with pyloric atresia (0.755); epidermolysis bullosa simplex with nail dystrophy (0.695)
- **Europe PMC papers**: 2578
- **Why important**: PLEC contributes to the globally corrected cytokinesis terms (GO:BP cytokinesis; q_global = 0.0493) and (GO:BP cytoskeleton-dependent cytokinesis; q_global = 0.0493) and connects IQGAP1 with DPYSL2 in the module. STRING also links PLEC with AHNAK and TLN1. As a plakin and cytolinker, PLEC can interlink cytoskeletal systems and maintain cell and tissue integrity. Its tissue enhancement in skeletal muscle, cell-type enhancement in urothelial cells, and strong disease associations with epidermolysis bullosa and muscular dystrophy underscore its structural importance.
- **Conclusion**: Established evidence supports PLEC as a major structural scaffold consistent with coordinated cytokinesis and cytoskeletal remodeling. Its role as the physical integrator of this particular cross-tissue module remains a hypothesis.

#### TLN1

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.86), MYOF (0.86), SEPTIN9 (0.85); STRING partners: IQGAP1 (0.893), PLEC (0.706)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 connects DPYSL2, MYOF, and SEPTIN9 in the module and has known STRING relationships with IQGAP1 and PLEC. It is located at focal adhesion sites and supports integrin activation, cell adhesion, actin organization, and migration. HPA associates it with blood vessels and with megakaryocyte and platelet populations, while its extensive literature and disease associations place it at the interface of tissue mechanics and pathology.
- **Conclusion**: Established evidence supports TLN1 as an adhesion and cytoskeletal regulator that could couple cell division to cell–matrix interactions. Its contribution to the shared tissue module may reflect adherent stromal, epithelial, vascular, or platelet-associated biology, but the exact source is unresolved.

#### SPTBN1

- **Related proteins** (co-abundance neighbors): ITIH2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: huMAP3_09165.1
- **Function (MyGene.info)**: spectrin beta, non-erythrocytic 1. Spectrin is an actin crosslinking and molecular scaffold protein that links the plasma membrane to the actin cytoskeleton, and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. It is composed of two antiparallel dimers of alpha- and beta- subunits. This gene is one member of a family of beta-spectrin genes. The encoded protein cont…
- **Diseases (Open Targets)**: developmental delay, impaired speech, and behavioral abnormalities (0.802); cancer (0.597); hereditary disease (0.516); hearing loss disorder (0.459); neurodevelopmental disorder (0.453)
- **Europe PMC papers**: 1635
- **Why important**: SPTBN1 is one of the genes in (GO:BP cytokinesis; q_global = 0.0493) and (GO:BP cytoskeleton-dependent cytokinesis; q_global = 0.0493) and is a spectrin scaffold linking the plasma membrane to cortical actin. It is associated with vascular and lymphatic endothelial cell types and occurs with AHNAK in hu.MAP complex (hu.MAP huMAP3_09165.1). Its broad disease and developmental associations, together with its role in membrane organization and cytokinesis, make it an informative marker of the module's cortical architecture.
- **Conclusion**: Established evidence supports SPTBN1 as a membrane–actin scaffold contributing to the cytokinesis signal. Its presence may indicate vascular or other adherent-cell architecture in the shared tissues, but that cellular attribution is a hypothesis.

## Module 2

**Tissue pair**: cervix_uterine and placenta  
**Genes (9)**: ANXA1, FBLN1, FGB, HBA1, EIF4A2, KRT19, TF, VDAC2, VPS35

### Function

No GO or KEGG term passed global multiple-testing correction. Therefore, the module does not have a statistically established pathway annotation from the supplied enrichment analysis. Its gene composition nevertheless suggests a mixed epithelial–vascular or extracellular-compartment signal: KRT19 marks epithelial structural biology; TF and FGB are circulating secreted proteins involved in iron transport and coagulation; FBLN1 is an extracellular-matrix glycoprotein linked to adhesion and implantation; ANXA1 is associated with membrane organization and inflammatory-cell regulation; VPS35 represents intracellular endosomal protein transport; and the isolated HBA1 signal is consistent with erythrocyte material. This is a biological interpretation of the genes and network, not a claim of GO/KEGG enrichment. The absence of a globally significant term does not invalidate the module.

**Cell composition.** The module is compositionally mixed rather than a coherent intracellular pathway. It contains secreted-to-blood or extracellular proteins, especially TF, FGB, ANXA1, and FBLN1, alongside epithelial and broadly expressed intracellular proteins. HPA supports epithelial representation through KRT19 and FBLN1-associated trophoblast or epithelial cell types, while TF and FGB show liver or hepatocyte enrichment and secretion to blood. HBA1 is associated with erythrocytes, bone marrow, lymphoid tissue, and several blood-cell categories, but is not detected by HPA in either target tissue. This raises the possibility that part of the shared signal reflects blood, vascular leakage, erythrocyte material, or common stromal and epithelial cell types in cervix and placenta rather than a dedicated tissue-specific program. Protein detection is present for most module genes in both tissues, although FGB is not detected by the cited tissue IHC evidence and TF is detected in placenta but not cervix.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no high-confidence pairwise interactions and no supplementary functional enrichment for this gene set. Thus, the co-abundance edges should not be interpreted as established physical interactions. In contrast, hu.MAP repeatedly places FGB and TF together in several complexes (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), and FGB, TF, and HBA1 co-occur in the broader complex (hu.MAP huMAP3_15040.1). These complexes contain many circulating, coagulation, complement, and transport proteins, so the hu.MAP evidence supports a shared extracellular or plasma-protein context, especially for FGB and TF, but does not establish that all module members form one molecular complex. The absence of hu.MAP assignments for most other genes and the lack of STRING support indicate a weakly connected molecular-interaction interpretation. The observed co-abundance network may instead reflect shared cell composition, secretion, tissue sampling, or correlated regulation.

**STRING interactions (score >= 0.7)**: 0 of 36 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (FGB, TF, HBA1; 3/64); huMAP3_07432.1 (FGB, TF; 2/18); huMAP3_09434.1 (FGB, TF; 2/33); huMAP3_08395.1 (FGB, TF; 2/43); huMAP3_09531.1 (FGB, TF; 2/47); huMAP3_10101.1 (FGB, TF; 2/49); huMAP3_10678.1 (FGB, TF; 2/71)

### Novelty

This module should not be called a newly discovered molecular complex or pathway. Its central circulating-protein relationship is not evidently novel because FGB and TF recur together in multiple hu.MAP complexes (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), with HBA1 also represented in (hu.MAP huMAP3_15040.1). Conversely, the exact cross-tissue co-abundance pattern linking epithelial KRT19, plasma proteins, FBLN1, ANXA1, VPS35, EIF4A2, VDAC2, and HBA1 is not established by the supplied STRING or hu.MAP evidence. That makes the module potentially novel as a tissue-pair-level co-abundance observation, but not demonstrably novel as a biological mechanism. Absence from STRING or hu.MAP alone cannot establish novelty. Confirmation would require replication in independent cervix and placenta cohorts, adjustment for blood and cell-type composition, and testing whether the signal persists within relevant cell populations.

**Hypothesis.** Hypothesis: the shared module reflects a composite interface between epithelial or trophoblast-associated tissue, extracellular matrix and vascular material, and intracellular stress or trafficking states. In this model, KRT19 and FBLN1 report epithelial or trophoblast and stromal context, TF and FGB report a plasma or vascular component, ANXA1 reports inflammatory or membrane-associated regulation, and VPS35, EIF4A2, and VDAC2 report intracellular trafficking, translation, and mitochondrial processes that covary with those tissue states. HBA1 may indicate erythrocyte admixture or blood exposure rather than participation in the same intracellular program. This hypothesis predicts that the module will weaken after deconvolution or removal of blood-associated transcripts, while the epithelial and extracellular components may remain associated in vascularized or remodeling regions of both tissues.

### Important genes

#### KRT19

- **Related proteins** (co-abundance neighbors): HBA1; HBA2 (0.90), FGB (0.87), TF (0.83), ANXA1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 19. The protein encoded by this gene is a member of the keratin family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. The type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains. Unlike its related family members, this smallest known ac…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.134); neoplasm (0.119); hereditary breast ovarian cancer syndrome (0.118); breast carcinoma (0.118); thyroid gland papillary carcinoma (0.117)
- **Europe PMC papers**: 6566
- **Why important**: KRT19 has the strongest network position in the module and connects the epithelial component to HBA1, FGB, TF, and ANXA1. HPA supports tissue enhancement in epithelial organs, epithelial cell-type enhancement, and detection in both cervix and placenta. Its keratin function provides a plausible structural marker for epithelial or trophoblast-associated tissue context. It also has extensive literature and cancer associations, making it the best-established epithelial anchor.
- **Conclusion**: Established evidence supports KRT19 as an epithelial structural and tissue-context marker that may organize the module's shared epithelial signal. It is not established that KRT19 mechanistically regulates the secreted proteins in this module; that relationship remains a co-abundance hypothesis.

#### TF

- **Related proteins** (co-abundance neighbors): FBLN1 (0.92), HBA1; HBA2 (0.90), KRT19 (0.83); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF is a highly connected network member and is the most recurrent module member in hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), where it repeatedly co-occurs with FGB and broader plasma-protein assemblies. It is secreted to blood, enriched in liver-related contexts, and functions in iron transport and antibacterial humoral biology. It has a very large literature base and strong disease associations involving transferrin deficiency and iron homeostasis.
- **Conclusion**: Established evidence supports TF as a circulating iron-transport and plasma-context marker, and hu.MAP supports its repeated association with FGB-containing protein assemblies. The module does not establish a cervix-specific or placenta-specific role for TF, nor does it prove that TF physically interacts with the other module members.

#### FGB

- **Related proteins** (co-abundance neighbors): KRT19 (0.87), EIF4A2 (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: fibrinogen beta chain. The protein encoded by this gene is the beta component of fibrinogen, a blood-borne glycoprotein comprised of three pairs of nonidentical polypeptide chains. Following vascular injury, fibrinogen is cleaved by thrombin to form fibrin which is the most abundant component of blood clots. In addition, various cleavage products of fibrinogen and fibrin regulate cell adhesion and spreading, display vas…
- **Diseases (Open Targets)**: congenital afibrinogenemia (0.786); familial dysfibrinogenemia (0.705); congenital fibrinogen deficiency (0.622); familial hypodysfibrinogenemia (0.597); cancer (0.592)
- **Europe PMC papers**: 4215
- **Why important**: FGB connects KRT19 with EIF4A2 and is repeatedly represented with TF in hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). It encodes a fibrinogen chain involved in clot formation, platelet activation, adhesion, and fibrinolysis. HPA indicates liver and hepatocyte enrichment and secretion to blood, while the protein is not detected in the cited cervix or placenta IHC results. Its disease associations and substantial literature make it an important indicator of coagulation or plasma contribution.
- **Conclusion**: Established evidence supports FGB as a blood-borne coagulation and extracellular-adhesion component, with repeated complex-level association with TF. Its absence from the cited tissue IHC and its plasma biology make blood-derived material a plausible explanation for its module membership. A local tissue-production mechanism is not established.

#### FBLN1

- **Related proteins** (co-abundance neighbors): TF (0.92); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibulin 1. Fibulin 1 is a secreted glycoprotein that becomes incorporated into a fibrillar extracellular matrix. Calcium-binding is apparently required to mediate its binding to laminin and nidogen. It mediates platelet adhesion via binding fibrinogen. Four splice variants which differ in the 3' end have been identified. Each variant encodes a different isoform, but no functional distinctions have been ident…
- **Diseases (Open Targets)**: synpolydactyly type 2 (0.447); FBLN1-related developmental delay-central nervous system anomaly-syndactyly syndrome (0.377); synpolydactyly (0.371); adolescent idiopathic scoliosis (0.306); alcohol drinking (0.219)
- **Europe PMC papers**: 2655
- **Why important**: FBLN1 is the strongest bridge from TF to extracellular-matrix biology in the network. HPA associates it with choroid plexus, cytotrophoblasts, decidual stromal cells, and endometrial stromal or glandular cells, and identifies it as secreted to extracellular matrix. Its documented roles in matrix incorporation, laminin or nidogen binding, platelet adhesion, integrin signaling, and embryo implantation make it especially relevant to placenta and reproductive-tissue remodeling.
- **Conclusion**: Established evidence supports FBLN1 as an extracellular-matrix and adhesion-related contributor compatible with stromal, trophoblast, and implantation biology. Its link to TF is a network association rather than proof of a direct functional partnership, so its proposed role in connecting plasma and matrix compartments remains a hypothesis.

#### ANXA1

- **Related proteins** (co-abundance neighbors): VPS35 (0.81), KRT19 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A1. This gene encodes a membrane-localized protein that binds phospholipids. This protein inhibits phospholipase A2 and has anti-inflammatory activity. Loss of function or expression of this gene has been detected in multiple tumors. [provided by RefSeq, Dec 2014].
- **Diseases (Open Targets)**: schizophrenia (0.434); myopathy (0.413); type 1 diabetes mellitus (0.346); spinal cord injury (0.335); Abnormal nasolacrimal system morphology (0.327)
- **Europe PMC papers**: 9690
- **Why important**: ANXA1 connects to KRT19 and VPS35, providing a bridge between epithelial structure, membrane biology, and intracellular trafficking. It is detected in both target tissues, is secreted to blood, and is associated with esophageal epithelial cells and basophils. Its established functions include phospholipid binding, phospholipase A2 inhibition, anti-inflammatory activity, leukocyte migration, phagocytosis, and inflammatory signaling. It also has a substantial literature base and multiple disease associations.
- **Conclusion**: Established evidence supports ANXA1 as an inflammation- and membrane-regulatory protein that could mark epithelial or immune-interface biology. The module does not show STRING support for its interactions, so any role for ANXA1 as a mechanistic bridge to KRT19 or VPS35 is provisional.

#### VPS35

- **Related proteins** (co-abundance neighbors): ANXA1 (0.81), VDAC2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS35 retromer complex component. This gene belongs to a group of vacuolar protein sorting (VPS) genes. The encoded protein is a component of a large multimeric complex, termed the retromer complex, involved in retrograde transport of proteins from endosomes to the trans-Golgi network. The close structural similarity between the yeast and human proteins that make up this complex suggests a similarity in function. Expression studie…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.743); neurodegenerative disease (0.553); young-onset Parkinson disease (0.503); Parkinson disease (0.482); Parkinson disease, dominant (0.370)
- **Europe PMC papers**: 3611
- **Why important**: VPS35 occupies the intracellular branch connecting ANXA1 and VDAC2. HPA describes broad tissue and cell-type distribution, endosomal and lysosomal localization, and detection in both target tissues. Its established function in retromer-mediated retrograde transport, lysosome organization, protein transport, and mitochondrial regulation gives the module an intracellular trafficking component distinct from its secreted proteins. It also has substantial literature and strong Parkinson-disease-related associations.
- **Conclusion**: Established evidence supports VPS35 as a conserved intracellular trafficking component that may report cellular homeostasis rather than plasma or extracellular-matrix biology. Its membership could reflect a correlated epithelial or stress state, but the supplied data do not establish a mechanistic connection between VPS35 and the circulating proteins.

## Module 3

**Tissue pair**: cervix_uterine and placenta  
**Genes (8)**: ATP5F1B, CLTC, GANAB, HNRNPK, KRT18, KRT7, KRT8, LMNB1

### Function

The most defensible interpretation is a shared epithelial and trophoblast-associated intracellular structural module, with linked protein-folding, vesicle-trafficking, nuclear-envelope, RNA-processing, and mitochondrial-energy functions. The strongest functional signal is the keratin relationship among KRT18, KRT8, and KRT7: KRT8 and KRT18 form a canonical simple-epithelial intermediate-filament pair, while KRT7 is a coexpressed keratin of simple epithelia and glandular or epithelial tissues. The STRING intermediate-filament annotation supports this interpretation only as supplementary evidence (STRING SMART Intermediate filament protein; within-query FDR = 0.021). No GO or KEGG term passed global correction, so no GO or KEGG enrichment is claimed. The remaining genes connect this structural signal to endoplasmic-reticulum glycoprotein quality control through GANAB, intracellular cargo trafficking through CLTC, nuclear organization and RNA-associated regulation through LMNB1 and HNRNPK, and mitochondrial ATP production through ATP5F1B.

**Cell composition.** This does not look primarily like a plasma-protein or secreted-protein module. The HPA summary reports only a single secreted gene overall, and the individual annotations are predominantly intracellular, cytoskeletal, nuclear, mitochondrial, endosomal, or membrane-associated. All module proteins are detected in both cervix and placenta, supporting biological detectability in the shared tissues. The single-cell evidence is dominated by trophoblast populations, including syncytiotrophoblasts, extravillous trophoblasts, cytotrophoblasts, and migrating cytotrophoblasts, with epithelial populations also represented. Several genes have low tissue specificity or broadly expressed housekeeping-like functions, especially GANAB, CLTC, HNRNPK, LMNB1, and ATP5F1B. Blood contamination is not the leading interpretation because most genes have low immune-cell specificity and KRT7 is not detected in immune cells, although the HPA annotations include limited immune-cell associations for some genes and therefore do not completely exclude shared cellular or sample-composition effects.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides direct, strong support for the KRT18-KRT8 relationship and additional support for KRT7-KRT8. The supplementary STRING intermediate-filament annotation contains LMNB1, KRT7, KRT18, and KRT8 (STRING SMART Intermediate filament protein; within-query FDR = 0.021), which is consistent with a structural cytoskeletal interpretation, but it is not global enrichment evidence. The module network also links KRT18 with GANAB and LMNB1, KRT8 with GANAB, and GANAB with ATP5F1B and CLTC, indicating that the co-abundance structure extends beyond the known keratin pair. STRING reports no listed partners for GANAB, LMNB1, ATP5F1B, CLTC, or HNRNPK within the supplied high-confidence interaction summary. No hu.MAP complex contains multiple module members. Thus, the module is not explained by a single experimentally supported multiprotein complex; rather, it combines a known epithelial filament relationship with correlated cellular subsystems.

**STRING interactions (score >= 0.7)**: 2 of 28 gene pairs: KRT18–KRT8 (0.999); KRT7–KRT8 (0.746)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Intermediate filament protein (FDR = 0.021, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The tissue-pair co-abundance observation may be a useful context-specific finding, but it should not be called a newly discovered molecular mechanism. The keratin relationships are established, KRT8 and KRT18 are canonical partners in simple epithelia, and the functions of GANAB, CLTC, LMNB1, ATP5F1B, and HNRNPK are already well described. The absence of a multi-member hu.MAP complex and the limited STRING coverage for several edges indicate that the precise cross-tissue co-abundance configuration may not be represented in those resources, but database absence alone does not establish novelty. A cautious claim is that this is a potentially novel shared cervix-placenta co-abundance pattern built largely from known epithelial, trophoblast, and housekeeping biology. Its novelty would require replication in independent tissue cohorts and testing against cell-composition and technical explanations.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of epithelial or trophoblast cells that maintain intermediate-filament architecture while supporting secretory and membrane-trafficking demands. In this model, KRT8, KRT18, and KRT7 provide the structural scaffold; GANAB supports endoplasmic-reticulum glycoprotein maturation; CLTC supports receptor and cargo trafficking; ATP5F1B supplies mitochondrial energy; and LMNB1 and HNRNPK couple nuclear architecture with gene-expression and RNA processing states. The shared signal between cervix and placenta could therefore reflect a common epithelial or trophoblast-like cellular program rather than a single dedicated complex. This remains a hypothesis because no globally corrected GO or KEGG term and no multi-member hu.MAP complex independently demonstrate the proposed mechanism.

### Important genes

#### KRT18

- **Related proteins** (co-abundance neighbors): GANAB (0.88), LMNB1 (0.88), KRT8 (0.86), KRT7 (0.84); STRING partners: KRT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 18. KRT18 encodes the type I intermediate filament chain keratin 18. Keratin 18, together with its filament partner keratin 8, are perhaps the most commonly found members of the intermediate filament gene family. They are expressed in single layer epithelial tissues of the body. Mutations in this gene have been linked to cryptogenic cirrhosis. Two transcript variants encoding the same protein have bee…
- **Diseases (Open Targets)**: cirrhosis of liver (0.623); cirrhosis, familial (0.396); prostate carcinoma (0.140); neoplasm (0.117); breast carcinoma (0.113)
- **Europe PMC papers**: 6539
- **Why important**: KRT18 is the most connected module member in the supplied network and links the keratin core to GANAB and LMNB1 as well as KRT8 and KRT7. Established evidence identifies it as a type I intermediate-filament chain that commonly pairs with KRT8 in simple epithelial tissues. HPA detects it in both tissues and associates it with trophoblast and epithelial cell populations. It also has extensive literature and disease associations involving liver cirrhosis and neoplasia. The STRING KRT18-KRT8 relationship is especially well supported (STRING SMART Intermediate filament protein; within-query FDR = 0.021).
- **Conclusion**: Established conclusion: KRT18 is a central structural marker of the module and strongly supports an epithelial or trophoblast interpretation. Hypothesis: its network centrality may make it a useful indicator of the shared cellular state, but it should not be treated as a causal driver from co-abundance alone.

#### KRT8

- **Related proteins** (co-abundance neighbors): KRT7 (0.91), KRT18 (0.86), GANAB (0.83); STRING partners: KRT18 (0.999), KRT7 (0.746)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Intermediate filaments; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 8. This gene is a member of the type II keratin family clustered on the long arm of chromosome 12. Type I and type II keratins heteropolymerize to form intermediate-sized filaments in the cytoplasm of epithelial cells. The product of this gene typically dimerizes with keratin 18 to form an intermediate filament in simple single-layered epithelial cells. This protein plays a role in maintaining cellul…
- **Diseases (Open Targets)**: cirrhosis of liver (0.596); cirrhosis, familial (0.401); neurodegenerative disease (0.371); prostate carcinoma (0.314); Abnormality of the liver (0.306)
- **Europe PMC papers**: 5942
- **Why important**: KRT8 occupies the keratin core and connects KRT7, KRT18, and GANAB. It is established as a type II keratin that heteropolymerizes with KRT18 in simple epithelial cells and contributes to structural integrity, differentiation, and signaling. HPA associates it with extravillous trophoblasts and several epithelial populations, with detection in both tissues. It has extensive literature and disease associations including liver and neoplastic disorders. STRING directly supports its relationships with KRT18 and KRT7 (STRING SMART Intermediate filament protein; within-query FDR = 0.021).
- **Conclusion**: Established conclusion: KRT8 is a core epithelial-filament component and one of the strongest biological anchors for the module. Hypothesis: coordinated KRT8 abundance may report epithelial or trophoblast composition and mechanical state rather than a module-specific biochemical pathway.

#### KRT7

- **Related proteins** (co-abundance neighbors): KRT8 (0.91), KRT18 (0.84); STRING partners: KRT8 (0.746)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments, Cytosol; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 7. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the simple epithelia lining the cavities of the internal organs and in th…
- **Diseases (Open Targets)**: neoplasm (0.118); lung carcinoma (0.105); cancer (0.102); lung cancer (0.099); colorectal carcinoma (0.099)
- **Europe PMC papers**: 3815
- **Why important**: KRT7 is part of the keratin subnetwork and connects to both KRT8 and KRT18. Its established expression in simple epithelia, gland ducts, and blood-vessel lining is consistent with the cervix and placenta context. HPA places it in cytotrophoblast and extravillous-trophoblast populations and detects it in both tissues, while not detecting it in immune cells. It has substantial literature and associations with epithelial cancers. Its STRING relationship with KRT8 and inclusion in the supplementary intermediate-filament annotation support the structural interpretation (STRING SMART Intermediate filament protein; within-query FDR = 0.021).
- **Conclusion**: Established conclusion: KRT7 reinforces the epithelial and trophoblast identity of the keratin core. Hypothesis: its presence may help distinguish this shared module from a generic stress or blood-derived signal, although that inference requires cell-composition controls.

#### GANAB

- **Related proteins** (co-abundance neighbors): KRT18 (0.88), ATP5F1B (0.84), KRT8 (0.83), CLTC (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB has high network connectivity and bridges the keratin-related part of the module to ATP5F1B and CLTC. It encodes the alpha subunit of glucosidase II, an endoplasmic-reticulum enzyme involved in glycoprotein folding and quality control. HPA detects it in both tissues and associates it with extravillous trophoblasts. Its disease associations include autosomal dominant polycystic kidney and liver disease, and it has a substantial literature base. Unlike the keratins, it lacks listed STRING partners in the supplied interaction summary, so its network role is primarily a co-abundance bridge rather than a confirmed physical interaction.
- **Conclusion**: Established conclusion: GANAB provides a plausible endoplasmic-reticulum protein-quality-control component connected to the epithelial structural signal. Hypothesis: it may indicate increased glycoprotein-processing demand in trophoblast or epithelial cells, but the module data do not prove that this demand is mechanistically coupled to the keratins.

#### ATP5F1B

- **Related proteins** (co-abundance neighbors): GANAB (0.84), CLTC (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP synthase F1 subunit beta. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: hypermetabolism due to uncoupled mitochondrial oxidative phosphorylation 2 (0.499); hypertrophic cardiomyopathy (0.212); Alzheimer disease (0.177); hypertensive disorder (0.117); response to xenobiotic stimulus (0.117)
- **Europe PMC papers**: 735
- **Why important**: ATP5F1B links GANAB with CLTC in the module network and encodes the catalytic beta subunit of mitochondrial ATP synthase. Its established function is proton-motive-force-driven ATP synthesis and energy production. HPA detects it in both tissues and associates it with cytotrophoblasts and syncytiotrophoblasts. It has disease associations involving mitochondrial energy dysregulation, cardiovascular disease, and neurodegeneration, with a meaningful literature base. No corresponding high-confidence STRING partner is listed in the supplied evidence.
- **Conclusion**: Established conclusion: ATP5F1B represents a mitochondrial energy component within the module and is compatible with metabolically active trophoblasts. Hypothesis: its co-abundance may reflect energetic support for trafficking, glycoprotein processing, and epithelial maintenance, but this causal chain is not established by the network.

## Module 4

**Tissue pair**: cervix_uterine and placenta  
**Genes (5)**: COTL1, FHL2, S100A13, TIMP1, LTF

### Function

No GO or KEGG term passed global correction, so the module cannot be assigned a statistically supported pathway label from enrichment. The gene annotations and co-abundance structure instead suggest a mixed extracellular, inflammatory, cytoskeletal, and tissue-remodelling signal. TIMP1 is the network hub and is associated with inhibition of matrix metalloproteinases, cell proliferation, cytokine responses, and anti-apoptotic activity. LTF contributes mucosal innate defence, iron handling, and antimicrobial activity. S100A13 is associated with calcium-binding functions, cytokine production, interleukin-one-alpha production, NF-kappa-B signalling, and mast-cell degranulation. COTL1 represents actin regulation and leukotriene-related biology, while FHL2 represents focal-adhesion and actin-associated regulation, hormone responses, apoptosis, and muscle or osteoblast-related processes. These annotations support a broad tissue-interface or inflammatory-remodelling interpretation, but not a single established pathway. There were no STRING supplementary enrichment terms.

**Cell composition.** The module is compositionally mixed rather than a coherent housekeeping set. Three genes are secreted or reported as secreted, and LTF is associated with neutrophils and non-classical monocytes, making blood or mucosal material a plausible contributor. COTL1 is enriched across several myeloid populations, including monocytes, eosinophils, dendritic cells, and neutrophils. Several genes also show enrichment in extravillous trophoblasts, decidual stromal cells, or other placental-associated cell types. HPA evidence therefore supports contributions from immune or blood-associated cells as well as resident reproductive-tissue cells. Protein detection is incomplete across the two tissues, and the absence of immunohistochemical detection for some genes does not negate the co-abundance result. The module should not be described as broadly expressed housekeeping biology.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was reported among the module genes, no STRING functional-enrichment result was reported, and no hu.MAP complex contained at least two module members. Thus, the co-abundance links are not corroborated here as established physical interactions or membership in a known multiprotein complex. The strongest internal association places TIMP1 alongside S100A13, LTF, and FHL2, while FHL2 is linked to COTL1; these are expression-level relationships in this module and should not be interpreted as direct binding. Known biology still provides functional context: TIMP1 is a matrix-metalloproteinase inhibitor, LTF is an antimicrobial iron-binding secreted protein, COTL1 regulates actin and interacts with five-lipoxygenase according to the supplied annotation, and FHL2 is associated with focal adhesions and actin-related structures.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially interesting shared co-abundance pattern, but it cannot be called a new molecular complex or a new pathway discovery. Its novelty is supported only in the limited sense that this particular cervix-uterine and placenta co-abundance configuration is not represented by a reported STRING interaction set or hu.MAP complex in the supplied evidence. Absence from those resources does not establish biological novelty, because co-abundance can reflect shared cell composition, secretion, tissue injury, inflammation, or regulation without direct protein binding. The mixed HPA profile and the lack of globally significant GO or KEGG enrichment make a cell-composition or tissue-interface explanation at least as plausible as a novel conserved intracellular program. Independent validation with transcript or protein measurements, cell deconvolution, and replication would be required.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cervix-placenta tissue-interface state in which immune or blood-associated material and reproductive-tissue cells jointly contribute a matrix-remodelling and innate-defence signature. In this model, TIMP1 may coordinate extracellular-matrix protection and survival or cytokine responses; LTF may provide antimicrobial and iron-sequestering activity; S100A13 may mark calcium-sensitive inflammatory signalling; COTL1 may connect myeloid or trophoblast-associated biology to actin and leukotriene regulation; and FHL2 may connect focal-adhesion or cytoskeletal state to hormone-responsive tissue remodelling. This is a mechanistic proposal, not an established interaction model, and the available evidence does not demonstrate that these proteins form one complex.

### Important genes

#### TIMP1

- **Related proteins** (co-abundance neighbors): S100A13 (0.87), LTF (0.86), FHL2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TIMP metallopeptidase inhibitor 1. This gene belongs to the TIMP gene family. The proteins encoded by this gene family are natural inhibitors of the matrix metalloproteinases (MMPs), a group of peptidases involved in degradation of the extracellular matrix. In addition to its inhibitory role against most of the known MMPs, the encoded protein is able to promote cell proliferation in a wide range of cell types, and may also have an …
- **Diseases (Open Targets)**: neoplasm (0.120); Sepsis (0.119); glioblastoma (0.119); colorectal carcinoma (0.119); neurodegenerative disease (0.117)
- **Europe PMC papers**: 25183
- **Why important**: TIMP1 is the network hub, connected to S100A13, LTF, and FHL2, and it has the largest literature base among the module genes in the fact sheet. Its established functions include inhibition of matrix metalloproteinases, promotion of cell proliferation, anti-apoptotic activity, and cytokine-responsive transcription. It is also secreted to blood, making it relevant to both tissue remodelling and possible blood or extracellular-fluid contributions.
- **Conclusion**: Established evidence supports TIMP1 as the principal integrative marker of the module's matrix-remodelling and cytokine-responsive aspect. It is a strong module marker, but its central co-abundance position does not prove that it regulates the other genes or physically interacts with them.

#### LTF

- **Related proteins** (co-abundance neighbors): TIMP1 (0.86); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactotransferrin. This gene is a member of the transferrin family of genes and its protein product is found in the secondary granules of neutrophils. The protein is a major iron-binding protein in milk and body secretions with an antimicrobial activity, making it an important component of the non-specific immune system. The protein demonstrates a broad spectrum of properties, including regulation of iron homeostasi…
- **Diseases (Open Targets)**: tuberculosis (0.517); AL amyloidosis (0.467); Abnormality of the skeletal system (0.435); schizophrenia (0.235); inflammatory bowel disease (0.218)
- **Europe PMC papers**: 7000
- **Why important**: LTF is connected to TIMP1 and has substantial literature support. Its supplied annotations identify it as a secreted transferrin-family protein found in neutrophil secondary granules, with antimicrobial, iron-homeostatic, mucosal, anti-inflammatory, and host-defence functions. HPA evidence strongly links it to neutrophils and monocyte populations, making it important for interpreting possible blood-cell or mucosal contributions.
- **Conclusion**: Established evidence supports LTF as an innate-defence and cell-composition indicator. In this module, LTF may reflect immune-cell or secretion-related biology rather than a placenta-specific intracellular mechanism.

#### FHL2

- **Related proteins** (co-abundance neighbors): COTL1 (0.83), TIMP1 (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Actin filaments, Focal adhesion sites; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: four and a half LIM domains 2. This gene encodes a member of the four-and-a-half-LIM-only protein family. Family members contain two highly conserved, tandemly arranged, zinc finger domains with four highly conserved cysteines binding a zinc atom in each zinc finger. This protein is thought to have a role in the assembly of extracellular membranes. Also, this gene is down-regulated during transformation of normal myoblasts to r…
- **Diseases (Open Targets)**: familial isolated dilated cardiomyopathy (0.372); alcohol drinking (0.367); seasonal allergic rhinitis (0.307); stroke disorder (0.240); poisoning (0.215)
- **Europe PMC papers**: 2785
- **Why important**: FHL2 links TIMP1 to COTL1 in the module and is detected by immunohistochemistry in both tissues. Its location at actin filaments and focal-adhesion sites, together with annotations involving hormone response, apoptosis, muscle development, and osteoblast differentiation, gives it a plausible structural and signalling bridge between tissue cells and the inflammatory or extracellular components.
- **Conclusion**: Established evidence supports FHL2 as a tissue-structural and signalling-associated component with relevance to trophoblast and reproductive-tissue cell contexts. Its bridging position suggests a hypothesis about cytoskeletal coupling, but does not establish that it connects the other module proteins directly.

#### COTL1

- **Related proteins** (co-abundance neighbors): FHL2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coactosin like F-actin binding protein 1. This gene encodes one of the numerous actin-binding proteins which regulate the actin cytoskeleton. This protein binds F-actin, and also interacts with 5-lipoxygenase, which is the first committed enzyme in leukotriene biosynthesis. Although this gene has been reported to map to chromosome 17 in the Smith-Magenis syndrome region, the best alignments for this gene are to chromosome 16. The Smith-Ma…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.419); placental abruption (0.272); placenta praevia (0.272); placental retention (0.267); cervical carcinoma (0.262)
- **Europe PMC papers**: 1073
- **Why important**: COTL1 connects to FHL2 and is strongly associated in the supplied HPA evidence with monocytes, neutrophils, eosinophils, dendritic cells, megakaryocytes, and placental Hofbauer cells. Its established annotation concerns F-actin regulation and interaction with five-lipoxygenase, while disease associations include placental and cervical disorders. It therefore links immune-cell state, cytoskeletal regulation, and the shared tissue context.
- **Conclusion**: Established evidence supports COTL1 as an immune and actin-regulatory marker, especially relevant to placental myeloid populations. Its module role may be to report immune-cell participation or cytoskeletal activation, but a causal role in the shared tissue program remains hypothetical.

#### S100A13

- **Related proteins** (co-abundance neighbors): TIMP1 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in cervix_uterine, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: S100 calcium binding protein A13. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: neurodegenerative disease (0.413); Alzheimer disease (0.349); Parkinson disease (0.338); lysosomal storage disease (0.338); thyroid gland carcinoma (0.078)
- **Europe PMC papers**: 920
- **Why important**: S100A13 is directly connected to TIMP1 and is detected in both tissues. Its supplied annotations associate it with calcium binding, cytokine production, interleukin-one-alpha production, canonical NF-kappa-B signalling, and mast-cell degranulation. It also has evidence of expression in decidual stromal and endometrial cells, providing a possible resident-tissue counterpart to the immune-associated genes.
- **Conclusion**: Established evidence supports S100A13 as a candidate inflammatory-signalling component that may connect resident reproductive-tissue cells with TIMP1-associated remodelling. The proposed connection is biologically plausible but not demonstrated as a direct molecular interaction in this module.
