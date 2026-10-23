# Conserved co-abundance modules: heart and placenta

## Module 0

**Tissue pair**: heart and placenta  
**Genes (10)**: AHNAK, CNDP2, DPYSL2, FLNB, IQGAP1, LTA4H, SPTBN1, CCT5, CCT3, TLN1

### Function

The module is best interpreted as a cytoskeletal and cell-adhesion-associated co-abundance program, with an additional protein-folding component and a limited inflammatory-lipid and peptide-metabolism component. The central network relationships connect DPYSL2, TLN1, IQGAP1, AHNAK, and SPTBN1, which are annotated for cytoskeletal organization, membrane architecture, cell adhesion, migration, and signaling. The CCT3–CCT5 pair adds the established CCT/TRiC chaperonin machinery, while LTA4H and CNDP2 provide a more peripheral metabolic and proteolytic branch. No GO/KEGG term passed global correction, so no pathway-level enrichment can be claimed. The functional interpretation therefore rests on the convergence of gene annotations, network structure, STRING relationships, and hu.MAP memberships rather than on enrichment significance.

**Cell composition.** The module is not dominated by plasma or secreted proteins: all module genes are annotated as non-secreted. Most genes have low tissue specificity, and blood-cell specificity is generally low, arguing against a module that is simply a canonical blood-cell or plasma-protein signature. Nevertheless, several genes have cell-type-enhanced patterns involving vascular, platelet, endothelial, trophoblast, epithelial, Schwann, neuronal, or myeloid populations. TLN1 is associated with megakaryocytes and platelets, FLNB with extravillous trophoblasts, SPTBN1 with vascular endothelial cells, and DPYSL2 with several neural and myeloid-related cell populations. Protein detection is broader in placenta than in heart, with several genes undetected in heart despite being detected in placenta. Thus, the shared signal may partly reflect vascular, stromal, trophoblast, or other shared cellular constituents rather than a uniform heart-and-placenta parenchymal program. The evidence does not support attributing the module primarily to blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The known STRING relationships are CCT3–CCT5, FLNB–TLN1, and IQGAP1–TLN1. These links support two recognizable pieces of biology: the CCT/TRiC chaperonin system and an adhesion or cytoskeletal interaction centered on talin. The remaining co-abundance relationships are not supported by high-confidence STRING edges in the fact sheet, so they should not be treated as established physical interactions. hu.MAP independently places CCT3 and CCT5 together across several CCT-related complexes, supporting their interpretation as a chaperonin module. hu.MAP also places FLNB with AHNAK and SPTBN1 with AHNAK in membrane or cytoskeletal-associated complexes, although these complexes contain many proteins and only a small subset is represented in this module. Together, STRING and hu.MAP show that parts of the module recapitulate known protein machinery, while the full ten-gene pattern is not established as a single complex.

**STRING interactions (score >= 0.7)**: 3 of 45 gene pairs: CCT3–CCT5 (0.999); FLNB–TLN1 (0.995); IQGAP1–TLN1 (0.893)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01951.1 (CCT5, CCT3; 2/8); huMAP3_05674.1 (FLNB, AHNAK; 2/12); huMAP3_07938.1 (CCT5, CCT3; 2/23); huMAP3_06559.1 (CCT5, CCT3; 2/25); huMAP3_09191.1 (CCT5, CCT3; 2/32); huMAP3_10656.1 (CCT5, CCT3; 2/36); huMAP3_09165.1 (SPTBN1, AHNAK; 2/39); huMAP3_14584.1 (CCT5, CCT3; 2/61)

### Novelty

This is not demonstrably a wholly new molecular mechanism. The CCT3–CCT5 chaperonin relationship, the FLNB–TLN1 relationship, the IQGAP1–TLN1 relationship, and the hu.MAP memberships involving CCT3, CCT5, FLNB, AHNAK, and SPTBN1 are already established or catalogued. What may be novel is the tissue-pair-specific co-abundance combination linking these cytoskeletal, chaperone, and metabolic genes across heart and placenta. However, the fact sheet does not provide an external catalogue of previously reported heart–placenta modules, replication data, perturbation experiments, or independent cohorts. Therefore, the appropriate conclusion is that the module is a potentially novel systems-level association, not a proven new complex or pathway. Absence of STRING or hu.MAP support for several pairwise links does not by itself establish novelty.

**Hypothesis.** Hypothesis: the module reflects coordinated remodeling and maintenance of the cytoskeleton and cell–matrix interface in shared vascular, stromal, trophoblast, or related cellular populations of heart and placenta. In this model, TLN1, IQGAP1, AHNAK, FLNB, and SPTBN1 organize adhesion-linked actin and membrane scaffolds; DPYSL2 connects this scaffold to microtubule organization and signaling; CCT3 and CCT5 support folding or stability of the associated cytoskeletal proteins; and LTA4H with CNDP2 represents a peripheral inflammatory or peptide-processing state. This hypothesis is consistent with the annotations and network structure, but it is not established by the enrichment analysis because no GO/KEGG term passed global correction and most of the inferred edges lack independent interaction evidence.

### Important genes

#### TLN1

- **Related proteins** (co-abundance neighbors): IQGAP1 (0.95), SPTBN1 (0.87), AHNAK (0.86), DPYSL2 (0.85); STRING partners: FLNB (0.995), IQGAP1 (0.893)
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 is a central connector in the co-abundance network and is the module member with established STRING links to both IQGAP1 and FLNB. Its focal-adhesion and integrin-related annotations provide a direct mechanistic bridge between cell adhesion, actin organization, membrane contacts, and migration. HPA links it to vascular tissue and megakaryocyte or platelet populations, which is relevant to both vascular biology and the possibility of shared cellular composition. It is also strongly represented in disease literature, including cardiac and developmental disorders.
- **Conclusion**: Established evidence supports TLN1 as a key adhesion and cytoskeletal organizer and as an anchor for the best-supported interaction cluster. It is a plausible module driver, but the co-abundance data do not establish that TLN1 physically binds every central module partner in heart or placenta.

#### IQGAP1

- **Related proteins** (co-abundance neighbors): TLN1 (0.95), DPYSL2 (0.84), AHNAK (0.83), SPTBN1 (0.82); STRING partners: TLN1 (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in heart, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: IQ motif containing GTPase activating protein 1. This gene encodes a member of the IQGAP family. The protein contains four IQ domains, one calponin homology domain, one Ras-GAP domain and one WW domain. It interacts with components of the cytoskeleton, with cell adhesion molecules, and with several signaling molecules to regulate cell morphology and motility. Expression of the protein is upregulated by gene amplification in two gastric cancer ce…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.515); Costello syndrome (0.503); allergic rhinitis (0.474)
- **Europe PMC papers**: 3787
- **Why important**: IQGAP1 occupies a central position alongside TLN1, DPYSL2, AHNAK, and SPTBN1. Its annotated functions in cytoskeletal regulation, cell morphology, motility, growth-factor signaling, and membrane or junctional organization fit the principal structural interpretation of the module. It has a direct STRING relationship with TLN1, is detected in both tissues, and has extensive disease and literature representation.
- **Conclusion**: Established evidence supports IQGAP1 as a signaling and cytoskeletal scaffold that could connect adhesion to cell migration or remodeling. Its central network position makes it an important candidate mediator, but a specific heart–placenta mechanism remains a hypothesis.

#### AHNAK

- **Related proteins** (co-abundance neighbors): FLNB (0.87), TLN1 (0.86), IQGAP1 (0.83), DPYSL2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in heart, placenta
- **hu.MAP 3.0**: huMAP3_05674.1, huMAP3_09165.1
- **Function (MyGene.info)**: AHNAK nucleoprotein. The protein encoded by this gene is a large (700 kDa) structural scaffold protein consisting of a central domain with 128 aa repeats. The encoded protein may play a role in such diverse processes as blood-brain barrier formation, cell structure and migration, cardiac calcium channel regulation, and tumor metastasis. A much shorter variant encoding a 17 kDa isoform exists for this gene, and the sho…
- **Diseases (Open Targets)**: Aganglionic megacolon (0.266); neoplasm (0.108); hepatocellular carcinoma (0.093); cancer (0.085); melanoma (0.085)
- **Europe PMC papers**: 2886
- **Why important**: AHNAK is centrally connected to TLN1, IQGAP1, DPYSL2, and FLNB and is detected in both heart and placenta. Its large structural scaffold architecture, plasma-membrane localization, reported roles in membrane repair and cardiac calcium-channel regulation, and participation with FLNB and SPTBN1 in hu.MAP complexes make it a strong candidate for organizing the module's membrane-cytoskeletal component. Its substantial literature supports biological relevance, while its broad and varied cell-type associations caution against assigning a single cell origin.
- **Conclusion**: Established evidence supports AHNAK as a membrane-associated structural scaffold with relevance to cardiac and migratory cell biology. The hypothesis that it organizes the shared module across heart and placenta is plausible but not proven by the available co-abundance relationships.

#### DPYSL2

- **Related proteins** (co-abundance neighbors): CCT3 (0.88), TLN1 (0.85), IQGAP1 (0.84), LTA4H (0.82), AHNAK (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Microtubules, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dihydropyrimidinase like 2. This gene encodes a member of the collapsin response mediator protein family. Collapsin response mediator proteins form homo- and hetero-tetramers and facilitate neuron guidance, growth and polarity. The encoded protein promotes microtubule assembly and is required for Sema3A-mediated growth cone collapse, and also plays a role in synaptic signaling through interactions with calcium channels. This…
- **Diseases (Open Targets)**: hypertensive disorder (0.431); autosomal dominant non-syndromic intellectual disability (0.370); cardiovascular disorder (0.297); ovarian neoplasm (0.292); glomerulonephritis (0.269)
- **Europe PMC papers**: 1328
- **Why important**: DPYSL2 has the strongest network connectivity in the module and links the adhesion-associated cluster to LTA4H and the CCT3 branch. Its established functions in microtubule assembly, neuronal guidance, cell polarity, and cytoskeletal organization provide a plausible microtubule-side complement to the actin and membrane scaffolds. HPA shows tissue enhancement in brain and detection in placenta but not heart, while disease evidence spans neurological and cardiovascular associations.
- **Conclusion**: Established evidence supports DPYSL2 as a cytoskeletal and signaling regulator, especially for microtubule organization and cellular polarity. Its role in this heart–placenta module may reflect a shared remodeling or cell-state program, but the tissue-pair-specific interpretation remains a hypothesis because its tissue evidence is asymmetric.

#### CCT3

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.88), CCT5 (0.85); STRING partners: CCT5 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in heart, placenta
- **hu.MAP 3.0**: huMAP3_01951.1, huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is directly connected to CCT5 by a very strong STRING relationship and is repeatedly represented with CCT5 in hu.MAP CCT-related complexes. As a subunit of the CCT/TRiC chaperonin, it provides established protein-folding capacity for substrates including actin and tubulin, which are central to the cytoskeletal interpretation. It is detected in both heart and placenta and has broad tissue and cell-type distribution, consistent with a general support function rather than a tissue-specific marker.
- **Conclusion**: Established evidence supports CCT3 as part of the CCT/TRiC folding machinery and as a plausible maintainer of cytoskeletal-protein proteostasis. Its presence does not prove that the entire module is a chaperone complex; instead, it likely represents a supportive proteostasis component associated with the structural program.

## Module 1

**Tissue pair**: heart and placenta  
**Genes (11)**: ANXA5, ARPC4, HSPA5, CLTC, EZR, GANAB, SLC2A1, HNRNPK, SEC23A, SEPTIN7, CCT8

### Function

No GO or KEGG term passed global correction, so the module should not be assigned a formally significant pathway annotation. The gene combination nevertheless suggests a coordinated intracellular protein-handling and membrane-trafficking program. HSPA5 and GANAB support endoplasmic-reticulum protein folding, glycoprotein quality control, and ER homeostasis; SEC23A supports COPII-dependent ER-to-Golgi transport; CLTC supports coated-vesicle trafficking and endocytosis; and CCT8 supports cytosolic chaperoning and protein assembly. SEPTIN7, EZR, and ARPC4 connect this machinery to cytoskeletal organization, membrane structure, and actin-dependent processes. SLC2A1 adds a nutrient-transport component, while HNRNPK may represent linked RNA-processing and gene-regulatory activity. Thus, the most defensible interpretation is a broad proteostasis, vesicle-trafficking, membrane-remodeling, and cellular-transport module rather than a narrowly defined tissue-specific pathway. The STRING melanoma-cell-line tissue term (STRING TISSUES Melanoma cell line; within-query FDR = 0.0235) is supplementary and does not establish global enrichment.

**Cell composition.** The HPA profile argues against a module composed mainly of plasma proteins, secreted proteins, or blood-cell markers. HPA reports low tissue specificity for most genes, low immune-cell specificity for the module, and no recurrent enriched blood-cell category. The summary reports only a minority of secreted genes, while the listed proteins are predominantly intracellular, membrane-associated, or part of core cellular machinery. Many genes have enhanced expression in particular cell types, especially extravillous, syncytio-, cyto-, and migrating trophoblasts, with additional signals in other specialized cells. Placenta shows protein detection for nearly the whole listed module, whereas heart shows detection for a smaller subset. This pattern is compatible with shared cellular processes and with trophoblast-related representation in placenta, but it does not support a simple blood-contamination explanation. The low tissue specificity of most genes also means that the shared heart–placenta signal may reflect broadly used housekeeping-like machinery rather than a heart–placenta-specific biological program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest directly documented STRING relationships within the module are CCT8–HSPA5 and GANAB–HSPA5. These links support a proteostasis-centered interpretation, especially the connection between chaperoning and ER glycoprotein quality control. The supplementary STRING tissue association (STRING TISSUES Melanoma cell line; within-query FDR = 0.0235) groups ANXA5, HSPA5, EZR, GANAB, HNRNPK, SLC2A1, and CLTC in a melanoma-cell-line context, but it is not global enrichment evidence. Most module pairs are not represented by high-confidence STRING links, so the co-abundance structure is substantially broader than the currently catalogued physical-interaction network. hu.MAP provides one relevant complex observation: CLTC and SEC23A occur together in the large trafficking-associated complex (hu.MAP huMAP3_12394.1). Because only these module members are represented from that complex, (hu.MAP huMAP3_12394.1) supports a trafficking connection but does not establish that the entire module is one physical complex. Overall, known interaction evidence supports selected edges and functional neighborhoods, while the full module appears to be a co-abundance association rather than a single established molecular complex.

**STRING interactions (score >= 0.7)**: 2 of 55 gene pairs: CCT8–HSPA5 (0.701); GANAB–HSPA5 (0.846)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Melanoma cell line (FDR = 0.0235, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (CLTC, SEC23A; 2/98)

### Novelty

The individual functions of the genes and the documented HSPA5-centered, clathrin-related, COPII-related, cytoskeletal, and glucose-transport relationships are established biology rather than new discoveries. The potentially novel result is the conserved heart–placenta co-abundance combination and its organization into one module in this dataset. However, the fact sheet provides no comparison with previously published co-abundance modules, no independent replication, and no evidence that this exact gene combination has not been reported elsewhere. Therefore the module can be described as a potentially novel dataset-level association, not as a demonstrated new biological pathway. Its limited STRING connectivity and partial hu.MAP support may indicate that the co-abundance relationship captures coordinated regulation, shared cell-state composition, or context-dependent coupling that is not fully represented in physical-interaction databases; absence from those resources alone does not prove novelty.

**Hypothesis.** Hypothesis: in cells represented in both heart and placenta, a shared demand for synthesis, folding, glycosylation, export, and surface delivery of proteins couples ER quality control to vesicle trafficking and cytoskeletal remodeling. HSPA5 and GANAB could coordinate ER proteostasis, SEC23A could support onward COPII transport, and CLTC could mediate endocytic and coated-vesicle traffic. CCT8 may buffer cytosolic folding demands, while SEPTIN7, EZR, and ARPC4 could organize the cytoskeletal and membrane structures needed for trafficking. SLC2A1 may provide metabolic support or reflect a placenta-associated transport state. The trophoblast-associated HPA pattern suggests that cell-type composition or a migratory and metabolically active trophoblast-like state could contribute to the shared signal, but this remains a hypothesis requiring perturbation, cell-resolved analysis, and independent validation.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): SEPTIN7 (0.88), CCT8 (0.83), GANAB (0.81); STRING partners: CCT8 (0.701), GANAB (0.846)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in heart, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a central connector in the module and has the strongest directly documented STRING support, linking it to CCT8 and GANAB. Its established role as an ER HSP70 chaperone and regulator of ER homeostasis provides a mechanistic anchor for the proteostasis interpretation. It is detected in both heart and placenta, is enhanced in several trophoblast-related cell types, and has extensive literature coverage and disease-related investigation.
- **Conclusion**: Established evidence supports HSPA5 as a core ER-folding and stress-homeostasis component and as the best-supported interaction hub in this module. The hypothesis that it organizes the broader heart–placenta co-abundance program is plausible but is not proven by the available data.

#### GANAB

- **Related proteins** (co-abundance neighbors): CCT8 (0.85), CLTC (0.84), ANXA5 (0.83), HSPA5 (0.81); STRING partners: HSPA5 (0.846)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB has a highly connected position and links the HSPA5-centered proteostasis neighborhood to CLTC, CCT8, and ANXA5. Its established glucosidase-II function directly connects the module to ER glycoprotein processing and quality control. It is enhanced in extravillous trophoblasts, detected in placenta, has an intracellular and membrane-associated secretome annotation, and has substantial literature and disease association, including polycystic kidney and liver disease.
- **Conclusion**: Established evidence supports GANAB as a functional bridge between ER glycoprotein maturation and the module's trafficking-related genes. Its contribution to a shared tissue-pair mechanism remains a hypothesis because the co-abundance data do not establish causality.

#### CLTC

- **Related proteins** (co-abundance neighbors): CCT8 (0.95), GANAB (0.84), SLC2A1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endosomes, Lysosomes; IHC detected in heart, placenta
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: clathrin heavy chain. Clathrin is a major protein component of the cytoplasmic face of intracellular organelles, called coated vesicles and coated pits. These specialized organelles are involved in the intracellular trafficking of receptors and endocytosis of a variety of macromolecules.  The basic subunit of the clathrin coat is composed of three heavy chains and three light chains. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: intellectual disability, autosomal dominant 56 (0.787); cancer (0.576); hereditary disease (0.540); Alzheimer disease (0.466); neurodegenerative disease (0.465)
- **Europe PMC papers**: 2902
- **Why important**: CLTC connects the chaperone and glycoprotein-processing neighborhood to SLC2A1 and is one of the two module members represented in hu.MAP complex (hu.MAP huMAP3_12394.1), where the complex context is related to intracellular trafficking. Its established role in clathrin-coated vesicles, receptor-mediated endocytosis, and intracellular transport gives the module a clear membrane-trafficking component. It is detected in both heart and placenta and has extensive literature and disease association.
- **Conclusion**: Established evidence supports CLTC as a major membrane-trafficking component and as the strongest bridge from the module to the hu.MAP evidence. Its position does not show that clathrin trafficking drives the entire module; that broader interpretation remains hypothetical.

#### CCT8

- **Related proteins** (co-abundance neighbors): CLTC (0.95), SEPTIN7 (0.91), EZR (0.86), GANAB (0.85), HSPA5 (0.83); STRING partners: HSPA5 (0.701)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in heart, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 has the highest network centrality in the listed subgraph and connects CLTC, SEPTIN7, EZR, GANAB, and HSPA5. Its established role as a subunit of the cytosolic CCT chaperonin links protein folding and assembly to the ER and membrane-trafficking neighborhoods. It is detected in both tissues, has a cell-type-enhanced HPA profile, and has substantial literature coverage.
- **Conclusion**: Established evidence supports CCT8 as a broad protein-assembly and chaperoning component that may help explain the module's coherence. A specific role in coordinating heart–placenta biology is not established and should be treated as a hypothesis.

#### SLC2A1

- **Related proteins** (co-abundance neighbors): CLTC (0.84), HNRNPK (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 2 member 1. This gene encodes a major glucose transporter in the mammalian blood-brain barrier. The encoded protein is found primarily in the cell membrane and on the cell surface, where it can also function as a receptor for human T-cell leukemia virus (HTLV) I and II. Mutations in this gene have been found in a family with paroxysmal exertion-induced dyskinesia. [provided by RefSeq, Apr 2013].
- **Diseases (Open Targets)**: encephalopathy due to GLUT1 deficiency (0.852); childhood onset GLUT1 deficiency syndrome 2 (0.833); dystonia 9 (0.804); hereditary cryohydrocytosis with reduced stomatin (0.778); idiopathic generalized epilepsy (0.757)
- **Europe PMC papers**: 14405
- **Why important**: SLC2A1 provides a distinct metabolic and transport axis within the module, connecting CLTC to HNRNPK. It is tissue-enhanced in placenta and cell-type-enhanced in cytotrophoblast, extravillous trophoblast, and migrating cytotrophoblast populations. Its established function as a glucose transporter and its strong disease literature make it biologically important even though its network position is more peripheral than the chaperone-centered genes.
- **Conclusion**: Established evidence supports SLC2A1 as a placenta-associated glucose-transport marker and a plausible indicator of metabolic demand. Whether it functionally couples glucose transport to the module's proteostasis and trafficking program, rather than merely reflecting cell composition, remains a hypothesis.

## Module 2

**Tissue pair**: heart and placenta  
**Genes (7)**: CAPZB, EIF4A2, RTN4, SEPTIN11, SEPTIN2, SEPTIN9, TXNDC5

### Function

The strongest interpretation is a cytoskeletal and membrane-organization module centered on septin biology. SEPTIN2, SEPTIN9, and SEPTIN11 form a tightly connected septin core supported by STRING (STRING Pfam 50S ribosome-binding GTPase; within-query FDR = 0.0213) and by the hu.MAP septin complex (hu.MAP huMAP3_02362.1). The broader module also links this core to actin regulation through CAPZB, endoplasmic-reticulum organization and stress-related protein folding through TXNDC5 and RTN4, and translational control through EIF4A2. No GO or KEGG term passed global correction, so the functional interpretation is based on the gene annotations, network structure, STRING evidence, and hu.MAP evidence rather than on globally significant enrichment. The module may therefore represent coordinated cytoskeletal organization, vesicle or membrane trafficking, and cellular adaptation to secretory or hypoxic conditions.

**Cell composition.** The genes have low tissue specificity in HPA, with no recurrent enriched tissue signal, which argues against a heart- or placenta-exclusive program. Most genes are intracellular and broadly detected rather than plasma or classically secreted proteins; only one module gene is listed as secreted, and TXNDC5 is described as an intracellular and membrane protein. Several genes show cell-type enhancement, including extravillous trophoblasts, platelets, Hofbauer cells, epithelial cells, and other specialized cell populations. Blood-cell specificity is generally low, although individual genes show enrichment in selected B-cell, dendritic-cell, basophil, or related populations. Thus, the shared module could partly reflect common cellular composition or stress and structural states in the sampled tissues, but the HPA evidence does not support describing it primarily as a plasma-protein or blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides strong, mutually reinforcing evidence for the SEPTIN2–SEPTIN9–SEPTIN11 relationships, and these genes are also members of the same hu.MAP septin complex (hu.MAP huMAP3_02362.1). This establishes that the central septin subnetwork is already known and biologically coherent. The other module relationships, including links involving TXNDC5, RTN4, EIF4A2, and CAPZB, are not represented by the listed high-confidence STRING partners or by a listed hu.MAP complex. Consequently, the module contains a validated septin core embedded in a less-established cross-functional network rather than constituting a wholly known protein complex.

**STRING interactions (score >= 0.7)**: 3 of 21 gene pairs: SEPTIN11–SEPTIN2 (0.999); SEPTIN11–SEPTIN9 (0.996); SEPTIN2–SEPTIN9 (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam 50S ribosome-binding GTPase (FDR = 0.0213, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02362.1 (SEPTIN2, SEPTIN11, SEPTIN9; 3/14)

### Novelty

The septin core is not a new molecular relationship because it is supported by both STRING (STRING Pfam 50S ribosome-binding GTPase; within-query FDR = 0.0213) and hu.MAP (hu.MAP huMAP3_02362.1). The potentially novel aspect is the conserved co-abundance association of that core with TXNDC5, RTN4, EIF4A2, and CAPZB across heart and placenta. However, this cannot be called a new physical complex or a novel mechanism from the present evidence alone. Absence of the peripheral relationships from STRING or hu.MAP is not proof of novelty; it may reflect incomplete interaction databases, tissue context, indirect regulation, or correlated cell composition. The most defensible conclusion is that this is a potentially novel tissue-level co-abundance configuration built around a previously recognized septin subsystem.

**Hypothesis.** Hypothesis: in shared heart and placenta cellular states, a septin-based cytoskeletal scaffold coordinates actin architecture and membrane trafficking while interacting functionally with endoplasmic-reticulum protein-folding and membrane-shaping processes. TXNDC5 may mark protein-folding or hypoxia-related adaptation, RTN4 may connect the state to endoplasmic-reticulum organization and membrane trafficking, EIF4A2 may reflect coordinated translational regulation, and CAPZB may couple the state to actin filament-end control. The observed co-abundance could also be generated partly by shared trophoblast, vascular, platelet, or immune-related cellular composition, so physical interaction and causal regulation remain to be tested.

### Important genes

#### SEPTIN2

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.95), SEPTIN11 (0.93), SEPTIN9 (0.89), EIF4A2 (0.85); STRING partners: SEPTIN11 (0.999), SEPTIN9 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Actin filaments; IHC detected in heart, placenta
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 2. Enables identical protein binding activity. Predicted to be involved in several processes, including cilium assembly; regulation of exocytosis; and smoothened signaling pathway. Predicted to act upstream of or within regulation of L-glutamate import across plasma membrane and regulation of protein localization. Located in several cellular components, including cytoskeleton; photoreceptor connectin…
- **Diseases (Open Targets)**: hypothyroidism (0.239); squamous cell carcinoma (0.201); ischemic stroke (0.189); coronary artery disorder (0.181); skin cancer (0.181)
- **Europe PMC papers**: 281
- **Why important**: SEPTIN2 is the most central connector in the module and links the septin core to TXNDC5 and EIF4A2 as well as to SEPTIN9 and SEPTIN11. It is located at actin filaments, is detected in both tissues, belongs to a septin complex, and has annotations involving cytoskeleton organization, cytokinesis, cilium assembly, exocytosis, and protein localization. Its substantial literature and disease-association record make it a strong anchor for interpreting the module.
- **Conclusion**: Established evidence supports SEPTIN2 as a central septin cytoskeletal organizer and as part of the known septin relationships (STRING Pfam 50S ribosome-binding GTPase; within-query FDR = 0.0213) (hu.MAP huMAP3_02362.1). It is plausible, but not established, that SEPTIN2 coordinates the peripheral ER and translation-related associations in this module.

#### SEPTIN9

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.89), RTN4 (0.84); STRING partners: SEPTIN11 (0.996), SEPTIN2 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 9. This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic l…
- **Diseases (Open Targets)**: neuralgic amyotrophy (0.564); hypertensive disorder (0.496); cataract (0.437); essential hypertension (0.426); alcohol drinking (0.420)
- **Europe PMC papers**: 748
- **Why important**: SEPTIN9 is a member of the tightly connected STRING and hu.MAP septin core (STRING Pfam 50S ribosome-binding GTPase; within-query FDR = 0.0213) (hu.MAP huMAP3_02362.1). Its annotations include cytoskeleton organization, cytokinesis, intracellular protein localization, and cilium-related biology. It also has disease associations involving neuralgic amyotrophy, hypertension-related disorders, cataract, and leukemia-related biology in the supplied description, giving it broad biomedical relevance.
- **Conclusion**: Established evidence identifies SEPTIN9 as a component of a known septin assembly with a cytoskeletal and cell-division role. The association with RTN4 in this module may indicate a tissue-state relationship involving membrane or ER organization, but the supplied data do not establish direct binding or causality.

#### SEPTIN11

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.93), EIF4A2 (0.92), TXNDC5 (0.88); STRING partners: SEPTIN2 (0.999), SEPTIN9 (0.996)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 11. SEPT11 belongs to the conserved septin family of filament-forming cytoskeletal GTPases that are involved in a variety of cellular functions including cytokinesis and vesicle trafficking (Hanai et al., 2004 [PubMed 15196925]; Nagata et al., 2004 [PubMed 15485874]).[supplied by OMIM, Jul 2009].
- **Diseases (Open Targets)**: autosomal recessive cerebellar ataxia (0.119); corneal edema (0.093); neoplasm (0.077); hepatocellular carcinoma (0.076); glomerulonephritis (0.050)
- **Europe PMC papers**: 113
- **Why important**: SEPTIN11 is part of the high-confidence septin triad in STRING and the hu.MAP complex (STRING Pfam 50S ribosome-binding GTPase; within-query FDR = 0.0213) (hu.MAP huMAP3_02362.1). Its stated functions include filament-forming cytoskeletal GTPase activity, intracellular protein localization, cytokinesis, and vesicle trafficking. Its cell-type enhancement in extravillous trophoblasts, platelets, podocytes, and hepatic stellate cells is particularly relevant to interpreting a heart–placenta shared module.
- **Conclusion**: Established evidence supports SEPTIN11 as a septin cytoskeletal and trafficking component within the known core. Its trophoblast and platelet-related expression patterns make shared cellular composition a possible contributor, while a specific heart–placenta mechanism remains a hypothesis.

#### TXNDC5

- **Related proteins** (co-abundance neighbors): SEPTIN2 (0.95), RTN4 (0.89), SEPTIN11 (0.88), EIF4A2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Group enriched; location Endoplasmic reticulum; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin domain containing 5. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal endoplasmic reticulum (ER)-signal sequence, three catalytically active thioredoxin domains and a C-terminal ER-retention sequence. Its expression is induced by hypoxia and its role ma…
- **Diseases (Open Targets)**: colorectal carcinoma (0.321); spinal stenosis (0.203); neoplasm (0.096); central nervous system cancer (0.092); glioma (0.091)
- **Europe PMC papers**: 1026
- **Why important**: TXNDC5 is a highly connected peripheral bridge linking both the septin core and RTN4 and EIF4A2. It is an ER protein disulfide isomerase with several thioredoxin domains, is involved in protein folding and negative regulation of apoptosis, and is induced by hypoxia according to the supplied annotation. Its placenta detection, plasma-cell and selected B-cell associations, and substantial literature make it important for distinguishing a structural module from an ER-stress or cell-composition signal.
- **Conclusion**: Established evidence supports TXNDC5 as an ER protein-folding and hypoxia-responsive factor that is co-abundant with the septin-centered network. Its connection to septins is a network association rather than a demonstrated physical interaction, so a role in coupling cytoskeletal organization to ER adaptation remains a hypothesis.

#### EIF4A2

- **Related proteins** (co-abundance neighbors): SEPTIN11 (0.92), SEPTIN2 (0.85), CAPZB (0.82), TXNDC5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in heart, placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4A2. Enables ATP hydrolysis activity. Involved in negative regulation of RNA-directed 5'-3' RNA polymerase activity. Located in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and speech delay, with or without seizures (0.744); neurodevelopmental disorder (0.565); hereditary disease (0.448); dengue disease (0.370); complex neurodevelopmental disorder (0.370)
- **Europe PMC papers**: 2227
- **Why important**: EIF4A2 is a highly connected bridge between the septin genes, TXNDC5, and CAPZB. It is a translation-initiation factor with ATP-hydrolysis activity and annotations involving translational initiation and its regulation. It is detected in both tissues and has extensive literature and disease-association coverage, making it a useful indicator of coordinated protein-production state rather than a specialized secreted marker.
- **Conclusion**: Established evidence supports EIF4A2 as a broadly expressed translation-related component associated with the module network. The data do not show that EIF4A2 is regulated by septins or that it drives the module; its participation may instead reflect shared cellular state or indirect co-abundance.

