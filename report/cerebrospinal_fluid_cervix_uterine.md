# Conserved co-abundance modules: cerebrospinal_fluid and cervix_uterine

## Module 0

**Tissue pair**: cerebrospinal_fluid and cervix_uterine  
**Genes (6)**: SLC3A2, ASPH, HSPA5, CPD, IGF2R, PLXNB2

### Function

The module does not have a GO or KEGG term that passes global correction, so no pathway-level function can be claimed from enrichment. Its structure instead links IGF2R, SLC3A2, ASPH, and PLXNB2 as a relatively coherent membrane, trafficking, adhesion, and cellular-response cluster, with CPD and HSPA5 connected at the periphery. Established annotations support several compatible processes: IGF2R participates in lysosomal-enzyme trafficking, transforming growth factor beta activation, and IGF2 degradation; SLC3A2 supports amino-acid transport and calcium regulation; PLXNB2 participates in semaphorin-related axon guidance, cell migration, adhesion, and endocytosis; ASPH is associated with calcium homeostasis; CPD with proteolysis and peptide processing; and HSPA5 with ER protein folding and unfolded-protein response. These annotations suggest a broad cell-surface, intracellular-trafficking, proteostasis, and signaling context rather than a narrowly defined pathway. The lack of enriched terms does not invalidate the module, but it limits the strength of any functional assignment.

**Cell composition.** The HPA profile argues against interpreting this as a specialized cerebrospinal-fluid or cervix tissue program. Most genes have low tissue specificity, while several show immune-cell or myeloid associations. Neutrophil-related enrichment is recurrent, and PLXNB2 is associated with several monocyte and dendritic-cell populations; ASPH is associated with plasmacytoid dendritic cells; and IGF2R and CPD are associated with neutrophils. Other associations include syncytiotrophoblasts, epithelial populations, adipocytes, and lactating cells. Only one module gene is annotated as secreted, while the proteins are otherwise intracellular, membrane, ER, Golgi, or cytosolic. All module proteins are detected by immunohistochemistry in cervix_uterine, whereas cerebrospinal-fluid protein detection has no matching HPA tissue result. The shared co-abundance signal may therefore reflect a broadly expressed cellular program, immune or myeloid material, or shared cell-type composition in the samples rather than a tissue-specific secreted module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides limited direct support: the only high-confidence listed interaction is CPD with IGF2R. There is no STRING functional enrichment. hu.MAP provides one complex-level relationship, with PLXNB2 and IGF2R co-occurring in huMAP3_06775.1 (hu.MAP huMAP3_06775.1), although the module represents only a small part of that larger complex. The network's additional strong co-abundance links, including IGF2R with SLC3A2, ASPH, PLXNB2, and HSPA5, and SLC3A2 with ASPH, PLXNB2, and CPD, are not independently confirmed by the listed STRING or hu.MAP evidence. Thus, the module contains a small known interaction and a partial known complex association, but much of its network structure is an abundance correlation rather than an established physical complex.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: CPD–IGF2R (0.738)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PLXNB2, IGF2R; 2/60)

### Novelty

This is not sufficient evidence for declaring a new biological complex or pathway. The module combines proteins with established and fairly broad functions, and part of its structure is supported by an existing STRING interaction and a hu.MAP complex association (hu.MAP huMAP3_06775.1). The absence of additional STRING or hu.MAP links does not prove novelty, because those resources are incomplete and co-abundance relationships need not be physical interactions. The potentially novel result is the conserved co-abundance pattern across cerebrospinal_fluid and cervix_uterine, especially the combination of trafficking, membrane, calcium-related, proteostasis, and immune-associated genes. That cross-tissue pattern should be treated as a finding requiring replication and cell-composition control, not as evidence of a newly discovered mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state or cell-composition program in which membrane trafficking and receptor handling are coordinated with amino-acid transport, calcium-sensitive signaling, proteolytic processing, and ER proteostasis. IGF2R could provide a trafficking and lysosomal-processing axis, PLXNB2 and SLC3A2 could represent membrane signaling and transport components, ASPH could link the state to calcium-related regulation, CPD could contribute peptide processing, and HSPA5 could indicate ER folding demand. The recurring HPA immune and neutrophil associations make it plausible that the cross-tissue signal is partly driven by shared myeloid or other immune material in the samples. This is a mechanistic interpretation, not an established causal pathway, and should be tested by cell-type deconvolution, independent cohorts, and protein-level validation.

### Important genes

#### IGF2R

- **Related proteins** (co-abundance neighbors): SLC3A2 (0.96), ASPH (0.92), PLXNB2 (0.87), HSPA5 (0.81); STRING partners: CPD (0.738)
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Golgi apparatus; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06775.1
- **Function (MyGene.info)**: insulin like growth factor 2 receptor. This gene encodes a receptor for both insulin-like growth factor 2 and mannose 6-phosphate. The binding sites for each ligand are located on different segments of the protein. This receptor has various functions, including in the intracellular trafficking of lysosomal enzymes, the activation of transforming growth factor beta, and the degradation of insulin-like growth factor 2. Mutation or loss o…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.498); coronary artery disorder (0.477); Hypercholesterolemia (0.369); myocardial ischemia (0.359); coronary atherosclerosis (0.349)
- **Europe PMC papers**: 12245
- **Why important**: IGF2R is the most connected hub in the module and links the central membrane and intracellular-trafficking portion of the network to CPD through the only listed high-confidence STRING interaction. Its established functions include binding IGF2 and mannose six-phosphate, trafficking lysosomal enzymes, activating transforming growth factor beta, and degrading IGF2. It also has the largest literature volume among the module genes in the fact sheet and documented disease associations including hepatocellular carcinoma and cardiovascular disorders.
- **Conclusion**: Established evidence supports IGF2R as the strongest functional anchor for a trafficking and lysosomal-processing interpretation, and (hu.MAP huMAP3_06775.1) places it with PLXNB2 in a known hu.MAP complex. The hypothesis that IGF2R organizes the entire conserved module is plausible from its network position but is not established by the enrichment or interaction evidence.

#### SLC3A2

- **Related proteins** (co-abundance neighbors): IGF2R (0.96), ASPH (0.88), PLXNB2 (0.84), CPD (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 3 member 2. This gene is a member of the solute carrier family and encodes a cell surface, transmembrane protein. The protein exists as the heavy chain of a heterodimer, covalently bound through di-sulfide bonds to one of several possible light chains. The encoded transporter plays a role in regulation of intracellular calcium levels and transports L-type amino acids. Alternatively spliced transcript variants…
- **Diseases (Open Targets)**: sensorineural hearing loss disorder (0.370); neurodegenerative disease (0.324); neoplasm (0.117); breast cancer (0.113); breast carcinoma (0.110)
- **Europe PMC papers**: 6815
- **Why important**: SLC3A2 is a highly connected central membrane component linked to IGF2R, ASPH, PLXNB2, and CPD. It forms the heavy chain of amino-acid transporter heterodimers and is annotated for amino-acid transport and calcium regulation. Its associations with epithelial and trophoblast cell types, along with disease links involving hearing loss, neurodegeneration, and breast cancer, make it relevant to both tissue contexts and to possible shared cell composition.
- **Conclusion**: Established evidence supports SLC3A2 as a membrane transport and cellular-homeostasis component of the module. Its central co-abundance position suggests coordination with the other genes, but the fact sheet does not establish direct physical interactions or a causal role in the shared tissue signal.

#### PLXNB2

- **Related proteins** (co-abundance neighbors): IGF2R (0.87), ASPH (0.86), SLC3A2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06775.1
- **Function (MyGene.info)**: plexin B2. Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Intellectual disability (0.519); amelogenesis imperfecta (0.518); sensorineural hearing loss disorder (0.516); cutaneous melanoma (0.486); neurodegenerative disease (0.455)
- **Europe PMC papers**: 2109
- **Why important**: PLXNB2 is a central network member connected to IGF2R, ASPH, and SLC3A2, and it is one of the two module proteins represented in the hu.MAP complex (hu.MAP huMAP3_06775.1). Its established receptor role in semaphorin-related axon guidance, cell migration, adhesion, endocytosis, and neuroblast proliferation provides a plausible bridge between neural and epithelial or immune-associated biology. HPA associates it with monocyte and dendritic-cell populations as well as several epithelial cell types.
- **Conclusion**: Established evidence supports PLXNB2 as a receptor involved in cell interaction, migration, and trafficking, with a known complex-level association to IGF2R (hu.MAP huMAP3_06775.1). Its cross-tissue co-abundance may reflect a shared migration or membrane-state program, but the immune-cell associations also make cell mixture a substantial alternative explanation.

#### HSPA5

- **Related proteins** (co-abundance neighbors): IGF2R (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is connected to the IGF2R hub and is the clearest proteostasis-related member of the module. It is an ER HSP70 chaperone involved in protein folding, assembly, ER homeostasis, and the unfolded-protein response. HPA places it in several secretory-lineage and trophoblast-associated cell types and describes intracellular and membrane localization. It also has a large literature volume and disease associations including neurodegenerative disease.
- **Conclusion**: Established evidence supports HSPA5 as an indicator of ER folding and stress-handling capacity. Its peripheral position means it should not be treated as the primary network driver, but it provides a biologically coherent proteostasis dimension. Whether it reports a shared stress state or merely broad expression remains unresolved.

#### ASPH

- **Related proteins** (co-abundance neighbors): IGF2R (0.92), SLC3A2 (0.88), PLXNB2 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartate beta-hydroxylase. This gene is thought to play an important role in calcium homeostasis. The gene is expressed from two promoters and undergoes extensive alternative splicing. The encoded set of proteins share varying amounts of overlap near their N-termini but have substantial variations in their C-terminal domains resulting in distinct functional properties. The longest isoforms (a and f) include a C-terminal Asp…
- **Diseases (Open Targets)**: facial dysmorphism-lens dislocation-anterior segment abnormalities-spontaneous filtering blebs syndrome (0.770); Abnormality of the skeletal system (0.505); malignant hyperthermia of anesthesia (0.427); exercise-induced malignant hyperthermia (0.416); alcohol drinking (0.374)
- **Europe PMC papers**: 1346
- **Why important**: ASPH is a central connector among IGF2R, SLC3A2, and PLXNB2. Its established annotation relates to calcium homeostasis and calcium-dependent cellular processes, while HPA identifies adipose tissue enhancement and associations with adipocytes, neutrophil-related populations, ocular epithelial cells, and plasmacytoid dendritic cells. Its disease associations include developmental, skeletal, and anesthesia-related phenotypes.
- **Conclusion**: Established evidence supports ASPH as a calcium-related and ER-localized component that may connect membrane signaling with intracellular homeostasis. Its central position makes it an important candidate for follow-up, but the module does not establish that ASPH mediates the co-abundance relationship or that calcium signaling is the dominant module function.

## Module 1

**Tissue pair**: cerebrospinal_fluid and cervix_uterine  
**Genes (11)**: SERPINA1, HBA1, HBB, IGHA1, IGHA2, IGHG1, IGHG2, IGHG3, IGHG4, IGHM, TF

### Function

The strongest interpretation is an antibody-rich humoral immune module. The primary evidence is the globally corrected enrichment for antigen receptor-mediated signaling and B cell receptor signaling (GO:BP antigen receptor-mediated signaling pathway; q_global = 0.000265) (GO:BP B cell receptor signaling pathway; q_global = 0.000265), immunoglobulin receptor binding and antigen binding (GO:MF immunoglobulin receptor binding; q_global = 0.00119) (GO:MF antigen binding; q_global = 0.00825), circulating and general immunoglobulin complexes (GO:CC immunoglobulin complex; q_global = 0.00352) (GO:CC immunoglobulin complex, circulating; q_global = 0.00352), and antimicrobial or antibacterial humoral responses (GO:BP antibacterial humoral response; q_global = 0.000809) (GO:BP antimicrobial humoral response; q_global = 0.00619) (GO:BP defense response to bacterium; q_global = 0.0105). The immunoglobulin heavy-chain genes form the core functional signal, while TF contributes to the antibacterial humoral-response terms. The co-abundance network therefore most plausibly reflects coordinated abundance of circulating antibodies together with blood-derived carrier, protease-inhibitory, and erythrocyte-associated proteins rather than a unified intracellular pathway.

**Cell composition.** The module is dominated by secreted or extracellular proteins and immunoglobulin genes. HPA assigns the immunoglobulin genes to plasma cells and to memory or naive B-cell populations, with lymphoid tissue frequently enriched. This strongly supports a plasma-cell or B-cell contribution. TF and SERPINA1 are secreted to blood and have liver-associated enrichment, whereas HBA1 and HBB are erythrocyte-associated. Thus the shared signal between cerebrospinal fluid and cervix uterine may reflect circulating protein carryover, vascular exposure, blood-cell material, or shared immune-cell content. It should not be interpreted as evidence that all module proteins are produced by resident cells of both tissues. HPA also reports cervix uterine protein detection for some immunoglobulin genes but not for several other module members, which is consistent with a mixed extracellular and cellular-source signal.

**GO/KEGG enrichment**: 13 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP antigen receptor-mediated signaling pathway | 0.000265 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM |
| GO:BP B cell receptor signaling pathway | 0.000265 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM |
| GO:BP antibacterial humoral response | 0.000809 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM, TF |
| GO:MF immunoglobulin receptor binding | 0.00119 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM |
| GO:CC immunoglobulin complex | 0.00352 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM |
| GO:CC immunoglobulin complex, circulating | 0.00352 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM |
| GO:BP antimicrobial humoral response | 0.00619 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM, TF |
| GO:BP immune response-activating cell surface receptor signaling pathway | 0.00825 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM |
| GO:MF antigen binding | 0.00825 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM |
| GO:BP defense response to bacterium | 0.0105 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM, TF |
| GO:BP immune response-activating signaling pathway | 0.0166 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM |
| GO:BP immune response-regulating cell surface receptor signaling pathway | 0.0166 | IGHA1, IGHA2, IGHG1, IGHG2, IGHG4, IGHM |
| GO:CC IgG immunoglobulin complex | 0.0341 | IGHA1, IGHG1, IGHG2, IGHG4 |

### STRING and hu.MAP

STRING provides limited direct interaction support within this module. The established high-confidence relationships are HBA1 with HBB and SERPINA1 with TF. STRING supplementary tissue and function results also connect HBA1, HBB, TF, and SERPINA1 with cardiac tissue, molecular carrier activity, and a congestive heart-failure phenotype, but these are supplementary within-query findings and are not global enrichment evidence for the module. hu.MAP repeatedly places HBA1 with HBB in hemoglobin-related complexes and places SERPINA1 with TF in broad extracellular or plasma-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_04556.1) (hu.MAP huMAP3_06991.1) (hu.MAP huMAP3_10486.1) (hu.MAP huMAP3_13522.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). The immunoglobulin genes have no recorded STRING partners or hu.MAP complex membership in this fact sheet. Consequently, the co-abundance structure is partly anchored by known hemoglobin and plasma-protein relationships, while the coordinated immunoglobulin block is more consistent with shared abundance or common cellular and extracellular origin than with a demonstrated physical complex.

**STRING interactions (score >= 0.7)**: 2 of 55 gene pairs: HBA1–HBB (0.999); SERPINA1–TF (0.848)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Left ventricle (FDR = 0.0077, 4 genes); TISSUES Left atrium (FDR = 0.0077, 4 genes); TISSUES Right atrium (FDR = 0.0077, 4 genes); HPO Congestive heart failure (FDR = 0.0217, 4 genes); Pfam Globin (FDR = 0.0303, 2 genes); Function Molecular carrier activity (FDR = 0.0493, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINA1, TF, HBB, HBA1; 4/64); huMAP3_04556.1 (HBB, HBA1; 2/3); huMAP3_06991.1 (HBB, HBA1; 2/4); huMAP3_10486.1 (HBB, HBA1; 2/4); huMAP3_13522.1 (HBB, HBA1; 2/10); huMAP3_07432.1 (SERPINA1, TF; 2/18); huMAP3_07265.1 (SERPINA1, TF; 2/20); huMAP3_09434.1 (SERPINA1, TF; 2/33); huMAP3_08395.1 (SERPINA1, TF; 2/43); huMAP3_09531.1 (SERPINA1, TF; 2/47); huMAP3_10101.1 (SERPINA1, TF; 2/49); huMAP3_10678.1 (SERPINA1, TF; 2/71)

### Novelty

This module should not be claimed as a wholly new molecular complex or pathway. Its principal biology, namely immunoglobulin production, circulating antibody activity, hemoglobin association, transferrin transport, and alpha-one-antitrypsin biology, is already established. The limited direct STRING coverage of the immunoglobulin genes does not demonstrate novelty, because immunoglobulin constant-region genes can be poorly represented as interaction nodes and co-abundance is not equivalent to physical interaction. The potentially novel observation is the cross-tissue co-abundance pattern between cerebrospinal fluid and cervix uterine, especially the way an antibody-rich signal is coupled to erythrocyte and plasma proteins. That observation requires independent replication, control for blood contamination and cell composition, and comparison with other tissue pairs before it can be considered a new biological finding.

**Hypothesis.** Hypothesis: the shared module represents a circulating humoral-immune environment sampled in both tissues. Plasma-cell or B-cell-derived immunoglobulins may enter or be retained in extracellular fluid, while vascular leakage or blood-derived material contributes HBA1 and HBB. Liver-derived TF and SERPINA1 may travel with the same plasma fraction and covary with antibody abundance. In cerebrospinal fluid this could reflect blood-CSF barrier permeability or local immune surveillance; in cervix uterine it could reflect mucosal or vascular immune exposure. This is a mechanistic model, not an established conclusion from the co-abundance data alone.

### Important genes

#### IGHG1

- **Related proteins** (co-abundance neighbors): IGHG2 (0.99), IGHG3 (0.95), IGHA2 (0.90), IGHM (0.85), IGHG4 (0.82), HBA1; HBA2 (0.81), HBB (0.81); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Immune cell enriched; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant gamma 1 (G1m marker)
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 3057
- **Why important**: IGHG1 is the most central immunoglobulin node in the module and is connected to several other immunoglobulin heavy-chain genes as well as hemoglobin-associated nodes. It appears in every globally corrected GO term listed for the antibody-rich core (13 globally significant GO/KEGG terms, q_global 0.000265–0.0341; see the table). HPA links it to plasma cells and memory B cells, and its substantial literature volume makes it the best-supported marker of the module's antibody component.
- **Conclusion**: Established: IGHG1 marks a plasma-cell or B-cell-associated IgG signal and supports the humoral immune interpretation. Hypothesis: its central co-abundance position may make it a useful tracer of the shared circulating antibody fraction, but the data do not show that IGHG1 physically binds the other module proteins.

#### IGHG2

- **Related proteins** (co-abundance neighbors): IGHG1 (0.99), IGHG3 (0.95), IGHA2 (0.89), TF (0.88), IGHG4 (0.84), HBB (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Group enriched; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: immunoglobulin heavy constant gamma 2 (G2m marker)
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 1063
- **Why important**: IGHG2 is another highly connected immunoglobulin node and participates in all globally corrected terms associated with the antibody core (13 globally significant GO/KEGG terms, q_global 0.000265–0.0341; see the table). HPA assigns it to lymphoid tissue, plasma cells, and B-cell populations. Its strong co-abundance with IGHG1 and with TF gives it an important bridging position between the antibody signal and the extracellular carrier-protein signal.
- **Conclusion**: Established: IGHG2 supports a coordinated IgG and B-cell or plasma-cell signature. Hypothesis: its relationship with TF may reflect shared circulation or sample composition rather than a direct functional interaction.

#### TF

- **Related proteins** (co-abundance neighbors): IGHG3 (0.93), HBA1; HBA2 (0.92), IGHG2 (0.88), HBB (0.87); STRING partners: SERPINA1 (0.848)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: transferrin. This gene encodes a glycoprotein with an approximate molecular weight of 76.5 kDa. It is thought to have been created as a result of an ancient gene duplication event that led to generation of homologous C and N-terminal domains each of which binds one ion of ferric iron. The function of this protein is to transport iron from the intestine, reticuloendothelial system, and liver parenchymal cells t…
- **Diseases (Open Targets)**: atransferrinemia (0.776); alcohol drinking (0.492); hemochromatosis type 1 (0.471); neurodegenerative disease (0.400); urolithiasis (0.329)
- **Europe PMC papers**: 143656
- **Why important**: TF occupies a network position linking immunoglobulin-associated nodes with hemoglobin and SERPINA1. It contributes to the globally corrected antibacterial and antimicrobial humoral-response terms (GO:BP antibacterial humoral response; q_global = 0.000809) (GO:BP antimicrobial humoral response; q_global = 0.00619) (GO:BP defense response to bacterium; q_global = 0.0105). HPA identifies it as secreted to blood and enriched in liver-associated contexts, and the fact sheet describes its established role in iron transport. It also has extensive literature and disease-association coverage.
- **Conclusion**: Established: TF is a circulating iron-transport protein that can connect the immune-rich module to plasma and blood biology. Hypothesis: TF may serve as a biochemical indicator of the shared plasma fraction or inflammatory milieu, rather than being a driver of antibody production.

#### SERPINA1

- **Related proteins** (co-abundance neighbors): IGHM (0.84); STRING partners: TF (0.848)
- **HPA**: Tissue enriched; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: serpin family A member 1. The protein encoded by this gene is a serine protease inhibitor belonging to the serpin superfamily whose targets include elastase, plasmin, thrombin, trypsin, chymotrypsin, and plasminogen activator. This protein is produced in the liver, the bone marrow, by lymphocytic and monocytic cells in lymphoid tissue, and by the Paneth cells of the gut. Defects in this gene are associated with chronic obs…
- **Diseases (Open Targets)**: alpha 1-antitrypsin deficiency (0.768); chronic obstructive pulmonary disease (0.690); cirrhosis of liver (0.573); cholelithiasis (0.569); pulmonary emphysema (0.569)
- **Europe PMC papers**: 6526
- **Why important**: SERPINA1 links the module's immunoglobulin component through IGHM and is the partner of TF in STRING. It is included in many hu.MAP extracellular or plasma-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). HPA identifies it as liver-enriched, secreted to blood, and associated with several myeloid populations. The fact sheet provides established serine-protease inhibitor functions and disease associations, giving it a strong interpretation as a circulating inflammatory and protease-regulatory component.
- **Conclusion**: Established: SERPINA1 represents a secreted antiprotease and plasma-associated component with known links to inflammatory and liver disease biology. Hypothesis: its co-abundance with antibodies may reflect coordinated vascular or inflammatory leakage into both sample types.

#### HBA1

- **Related proteins** (co-abundance neighbors): none; STRING partners: HBB (0.999)
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_04556.1, huMAP3_06991.1, huMAP3_10486.1, huMAP3_13522.1
- **Function (MyGene.info)**: hemoglobin subunit alpha 1. The human alpha globin gene cluster located on chromosome 16 spans about 30 kb and includes seven loci: 5'- zeta - pseudozeta - mu - pseudoalpha-1 - alpha-2 - alpha-1 - theta - 3'. The alpha-2 (HBA2) and alpha-1 (HBA1) coding sequences are identical. These genes differ slightly over the 5' untranslated regions and the introns, but they differ significantly over the 3' untranslated regions. Two alp…
- **Diseases (Open Targets)**: alpha thalassemia spectrum (0.758); hemoglobin H disease (0.755); hemoglobin M disease (0.735); Heinz body anemia (0.698); primary familial polycythemia due to EPO receptor mutation (0.689)
- **Europe PMC papers**: 4551
- **Why important**: HBA1 is part of the hemoglobin signal, has a STRING relationship with HBB, and occurs in several hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_04556.1) (hu.MAP huMAP3_06991.1) (hu.MAP huMAP3_10486.1) (hu.MAP huMAP3_13522.1). HPA associates it with erythrocytes and blood-related cell populations. Although it has no direct network neighbors in the supplied co-abundance graph, its known hemoglobin role and coupling to HBB make it important for recognizing a possible blood-derived component.
- **Conclusion**: Established: HBA1 marks erythrocyte or hemoglobin-associated material and is not evidence for an antibody mechanism. Hypothesis: its presence may indicate vascular carryover or blood contamination that partly shapes the apparent cross-tissue module.

## Module 2

**Tissue pair**: cerebrospinal_fluid and cervix_uterine  
**Genes (20)**: A1BG, A2M, ANPEP, APOA2, ASAH1, ASTN2, CTSC, CD47, CLIC1, FGB, FN1, GSN, HPX, HRG, SERPINB1, SERPINA5, LGALS1, SERPINF1, TTR, GC

### Function

No GO or KEGG term passed global correction, so the module does not have a formally established enriched pathway. Its most coherent biological interpretation is a circulating extracellular-protein module involving plasma transport, protease and protease-inhibitor balance, heme handling, lipid-associated proteins, extracellular matrix interaction, and cerebrospinal-fluid transport. This interpretation is supported by the dense STRING relationships among A2M, FGB, GC, TTR, HPX, HRG, APOA2, FN1, SERPINF1, and GSN, together with the hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_02236.1) (hu.MAP huMAP3_08700.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_10501.1) (hu.MAP huMAP3_08218.1). The co-abundance pattern therefore appears more consistent with coordinated abundance of secreted and extracellular proteins than with a single intracellular pathway. ASTN2 is a highly connected module node and has annotations related to neuronal migration and neuron cell-cell adhesion, but its relationship to the secreted-protein component remains mechanistically uncertain.

**Cell composition.** The module is strongly dominated by secreted or plasma-associated proteins: sixteen genes have secretome annotations, including A2M, APOA2, FGB, GC, HRG, SERPINF1, GSN, SERPINA5, TTR, HPX, and FN1. HPA evidence points especially toward liver and hepatocytes, with additional signal from choroid plexus, fibroblasts, Hofbauer cells, and stromal or epithelial populations. This composition argues that the shared signal may reflect blood-derived or extracellular protein abundance in both tissues, rather than a cervix-specific or cerebrospinal-fluid-specific cellular program. The module is not predominantly blood-cell enriched: most genes are not detected or have low immune-cell specificity, although selected genes show immune-cell associations. The presence of TTR, SERPINF1, and A1BG with choroid-plexus or neural-interface annotations leaves open a genuine cerebrospinal-fluid contribution, but the strong plasma and hepatocyte signature makes sample composition and vascular or fluid exchange important alternative explanations.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains a connected set of high-confidence relationships centered on known associations among plasma and extracellular proteins. Particularly prominent links include A2M with TTR, SERPINF1, FN1, HPX, FGB, and APOA2; FGB with FN1, GC, HRG, and APOA2; and GC with TTR, HPX, and GSN. FN1 also connects to GSN, LGALS1, CD47, and SERPINF1. These relationships indicate that much of the module recapitulates known extracellular, carrier-protein, coagulation, protease-regulation, and matrix-associated biology rather than revealing an entirely uncharacterized interaction system. hu.MAP independently supports this interpretation: multiple complexes contain overlapping subsets of A2M, APOA2, FGB, TTR, GC, HPX, HRG, and A1BG, with the broadest complexes also containing many other plasma, complement, coagulation, and acute-phase proteins (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_02236.1) (hu.MAP huMAP3_08700.1) (hu.MAP huMAP3_09434.1). Smaller complexes connect TTR with HRG (hu.MAP huMAP3_10501.1) (hu.MAP huMAP3_08218.1). The complexes are partial matches, not proof that all module proteins form one physical complex. CD47, ASTN2, ASAH1, SERPINB1, CLIC1, CTSC, ANPEP, and LGALS1 have little or no direct STRING or hu.MAP support within the supplied evidence, so their co-abundance may reflect shared regulation, cell mixture, or indirect extracellular context.

**STRING interactions (score >= 0.7)**: 25 of 190 gene pairs: A2M–APOA2 (0.772); A2M–FGB (0.841); A2M–FN1 (0.851); A2M–HPX (0.824); A2M–HRG (0.762); A2M–SERPINF1 (0.88); A2M–TTR (0.905); APOA2–FGB (0.849); APOA2–GC (0.765); APOA2–TTR (0.843); CD47–FN1 (0.703); FGB–FN1 (0.922); FGB–GC (0.931); FGB–HPX (0.712); FGB–HRG (0.851); FGB–SERPINA5 (0.716); FN1–GSN (0.809); FN1–LGALS1 (0.878); FN1–SERPINF1 (0.846); GC–GSN (0.826); GC–HPX (0.827); GC–HRG (0.706); GC–TTR (0.899); GSN–TTR (0.861); HPX–TTR (0.793)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (A2M, APOA2, FGB, TTR, GC, HPX, HRG, A1BG; 8/64); huMAP3_10678.1 (A2M, APOA2, FGB, TTR, GC, HPX, HRG, A1BG; 8/71); huMAP3_09531.1 (A2M, APOA2, FGB, TTR, HPX, HRG, A1BG; 7/47); huMAP3_10101.1 (A2M, APOA2, FGB, TTR, HPX, HRG, A1BG; 7/49); huMAP3_09273.1 (A2M, APOA2, TTR, HPX, HRG; 5/28); huMAP3_08395.1 (A2M, APOA2, FGB, HPX, A1BG; 5/43); huMAP3_07432.1 (APOA2, FGB, HPX, A1BG; 4/18); huMAP3_07265.1 (A2M, APOA2, HPX, A1BG; 4/20); huMAP3_02236.1 (APOA2, HPX, A1BG; 3/7); huMAP3_08700.1 (APOA2, HPX, A1BG; 3/11); huMAP3_09434.1 (FGB, GC, A1BG; 3/33); huMAP3_10501.1 (TTR, HRG; 2/4); huMAP3_08218.1 (TTR, HRG; 2/5)

### Novelty

This module should not be called a new molecular complex or a newly discovered pathway. Much of its core is already represented in STRING and in several hu.MAP complexes, and the proteins have established plasma, extracellular-matrix, transport, coagulation, protease-regulatory, and choroid-plexus biology. A potentially novel aspect is the conserved co-abundance of this particular combination across cerebrospinal fluid and cervix uterine, especially the coupling of a plasma-protein core with ASTN2, CD47, ASAH1, CLIC1, CTSC, and LGALS1. However, absence of some module genes from STRING or hu.MAP does not establish novelty, because co-abundance can arise from shared secretion, tissue admixture, transport, or common regulation. The defensible conclusion is that the cross-tissue module organization may be a useful systems-level observation, while its individual molecular relationships are largely established.

**Hypothesis.** Hypothesis: the conserved module reflects a shared extracellular-fluid homeostasis program in which liver-derived plasma proteins and locally produced matrix or cell-surface proteins co-vary because of vascular or fluid exchange, tissue remodeling, and inflammatory-protease control. A2M, SERPINA5, and SERPINB1 could restrain proteolytic activity; FGB and FN1 could represent coagulation and matrix interfaces; GC and TTR could contribute vitamin or hormone transport; HPX could limit heme-associated oxidative stress; and SERPINF1 and LGALS1 could influence vascular, stromal, or neural-interface behavior. In cerebrospinal fluid, choroid-plexus-associated TTR and SERPINF1 may provide a local component, whereas in cervix uterine the same abundance pattern may be influenced by stromal, epithelial, vascular, or blood-derived material. This is a mechanistic hypothesis, not an enrichment result or demonstrated causal pathway.

### Important genes

#### A2M

- **Related proteins** (co-abundance neighbors): ASTN2 (1.00), CD47 (0.85), CLIC1 (0.84), ASAH1 (0.80); STRING partners: APOA2 (0.772), FGB (0.841), FN1 (0.851), HPX (0.824), HRG (0.762), SERPINF1 (0.88), TTR (0.905)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_09273.1, huMAP3_08395.1, huMAP3_07265.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M is a central connector to several major module proteins in STRING and occurs in many of the overlapping hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_08395.1) and (hu.MAP huMAP3_07265.1). It is secreted to blood and is annotated as a broad protease inhibitor and cytokine transporter, with roles in inflammatory-cascade control and protein clearance. Its disease associations include alpha-two-macroglobulin deficiency and Alzheimer disease relevance through amyloid-beta clearance. Its literature volume is substantial, supporting strong prior biological interpretation.
- **Conclusion**: Established evidence supports A2M as a plausible extracellular regulatory hub linking protease control, inflammatory signaling, and the plasma-protein core. The hypothesis that it coordinates the entire cross-tissue module is not established; its high connectivity could instead reflect common abundance in circulating protein mixtures.

#### GC

- **Related proteins** (co-abundance neighbors): ASTN2 (1.00), A1BG (0.87), ASAH1 (0.83), CLIC1 (0.81), LGALS1 (0.81), CTSC (0.80); STRING partners: APOA2 (0.765), FGB (0.931), GSN (0.826), HPX (0.827), HRG (0.706), TTR (0.899)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is a highly connected secreted-to-blood protein with strong STRING links to FGB, TTR, GSN, HPX, HRG, and APOA2, and it appears in several hu.MAP complexes (hu.MAP huMAP3_15040.1), (hu.MAP huMAP3_10678.1), and (hu.MAP huMAP3_09434.1). It is liver enriched and hepatocyte associated, while its annotated function includes vitamin D and vitamin metabolite transport. It is also documented in plasma and cerebrospinal fluid, making it especially relevant to the tissue pair. Its disease associations include vitamin D deficiency and central nervous system cancer, and it has a very large literature base.
- **Conclusion**: Established evidence supports GC as a carrier-protein bridge between systemic plasma biology and cerebrospinal-fluid biology. Its presence does not demonstrate local production in cervix uterine or a causal role in the module; shared fluid composition remains a strong alternative explanation.

#### TTR

- **Related proteins** (co-abundance neighbors): ASTN2 (1.00); STRING partners: A2M (0.905), APOA2 (0.843), GC (0.899), GSN (0.861), HPX (0.793)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_09273.1, huMAP3_10501.1, huMAP3_08218.1
- **Function (MyGene.info)**: transthyretin. This gene encodes one of the three prealbumins, which include alpha-1-antitrypsin, transthyretin and orosomucoid. The encoded protein, transthyretin, is a homo-tetrameric carrier protein, which transports thyroid hormones in the plasma and cerebrospinal fluid. It is also involved in the transport of retinol (vitamin A) in the plasma by associating with retinol-binding protein. The protein may also…
- **Diseases (Open Targets)**: amyloidosis, hereditary systemic 1 (0.846); hereditary ATTR amyloidosis (0.809); cardiomyopathy (0.733); carpal tunnel syndrome 1 (0.716); amyloidosis (0.714)
- **Europe PMC papers**: 15599
- **Why important**: TTR is enriched in choroid plexus and is annotated as a carrier of thyroid hormone in plasma and cerebrospinal fluid, with a further role in retinol transport. It connects in STRING to A2M, APOA2, GC, GSN, and HPX and occurs in numerous hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_09273.1) and (hu.MAP huMAP3_10501.1) (hu.MAP huMAP3_08218.1). Its disease associations include hereditary transthyretin amyloidosis and cardiomyopathy, and it has extensive literature support.
- **Conclusion**: Established evidence makes TTR a strong marker of the cerebrospinal-fluid or choroid-plexus-facing component of the module and of extracellular carrier biology. It is not evidence that the whole module is neuron-specific, because most of its partners are also abundant plasma proteins.

#### FN1

- **Related proteins** (co-abundance neighbors): CD47 (0.97), GSN (0.86), SERPINA5 (0.82); STRING partners: A2M (0.851), CD47 (0.703), FGB (0.922), GSN (0.809), LGALS1 (0.878), SERPINF1 (0.846)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibronectin 1. This gene encodes fibronectin, a glycoprotein present in a soluble dimeric form in plasma, and in a dimeric or multimeric form at the cell surface and in extracellular matrix. The encoded preproprotein is proteolytically processed to generate the mature protein. Fibronectin is involved in cell adhesion and migration processes including embryogenesis, wound healing, blood coagulation, host defense,…
- **Diseases (Open Targets)**: spondylometaphyseal dysplasia, 'corner fracture' type (0.799); glomerulopathy with fibronectin deposits 2 (0.742); cancer (0.625); coronary artery disorder (0.591); Noonan syndrome (0.526)
- **Europe PMC papers**: 100765
- **Why important**: FN1 is a secreted extracellular-matrix protein with established roles in adhesion, migration, wound healing, coagulation, and integrin-mediated signaling. It links in STRING to FGB, GSN, LGALS1, SERPINF1, A2M, and CD47, including particularly strong associations with FGB and LGALS1. HPA associates it with blood vessels, liver, placenta, fibroblasts, hepatic stellate cells, and hepatocytes. Its disease associations include fibronectin-deposit glomerulopathy, coronary artery disorder, cancer, and Noonan syndrome, and it has an exceptionally large literature volume.
- **Conclusion**: Established evidence supports FN1 as the principal matrix and cell-interface anchor of the module. The hypothesis that FN1 drives the shared cervix and cerebrospinal-fluid signature is unproven; its abundance may simply report extracellular matrix remodeling or vascular contamination.

#### SERPINF1

- **Related proteins** (co-abundance neighbors): ASTN2 (1.00), ASAH1 (0.98), CLIC1 (0.94), CD47 (0.92); STRING partners: A2M (0.88), FN1 (0.846)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family F member 1. This gene encodes a member of the serpin family that does not display the serine protease inhibitory activity shown by many of the other serpin proteins. The encoded protein is secreted and strongly inhibits angiogenesis. In addition, this protein is a neurotrophic factor involved in neuronal differentiation in retinoblastoma cells. Mutations in this gene were found in individuals with osteogenesi…
- **Diseases (Open Targets)**: osteogenesis imperfecta (0.716); osteogenesis imperfecta, recessive (0.462); osteogenesis imperfecta type 3 (0.447); osteogenesis imperfecta type 4 (0.371); refractive error (0.348)
- **Europe PMC papers**: 2744
- **Why important**: SERPINF1 is secreted to blood, enriched in choroid plexus, and associated with decidual stromal cells and retinal pigment epithelial cells. It is linked in STRING to A2M and FN1 and is connected within the module to ASTN2, ASAH1, CLIC1, and CD47. Its known functions include strong inhibition of angiogenesis and neurotrophic activity, and its disease associations include osteogenesis imperfecta and related skeletal disorders. Its literature volume is substantial enough to support a focused biological interpretation.
- **Conclusion**: Established evidence supports SERPINF1 as a plausible neural-interface, stromal, and vascular-regulatory component that may help explain conservation across the two tissues. The proposed role as a mediator coupling the plasma core to local tissue biology remains a hypothesis rather than a demonstrated mechanism.

## Module 3

**Tissue pair**: cerebrospinal_fluid and cervix_uterine  
**Genes (25)**: SERPINF2, LRG1, SERPINA3, ALDOC, PAM, SERPINC1, CFB, CFD, COL5A1, C5, C9, ENDOD1, FBLN1, GSTP1, SERPIND1, ITIH1, ITIH4, LDHB, LUM, LYZ, MDH1, HSPG2, RNASET2, CLEC3B, AZGP1

### Function

The module is best interpreted as a coordinated extracellular, circulating protease-regulation and innate-defense protein program, with an extracellular-matrix component. The strongest biological signal comes from the gene identities and network structure rather than enrichment statistics: CFB, CFD, C5 and C9 support alternative-pathway and terminal complement biology; SERPINC1, SERPIND1 and SERPINF2 support regulation of coagulation and fibrinolysis; and ITIH1, ITIH4, FBLN1, LUM, COL5A1 and HSPG2 support hyaluronan-associated and collagen-containing extracellular matrices. No GO or KEGG term passed global correction, so no GO or KEGG term is claimed as globally significant. The co-abundance pattern therefore most plausibly represents a shared extracellular-fluid or stromal-protein environment rather than a tightly defined intracellular pathway.

**Cell composition.** The module is strongly dominated by secreted or extracellular proteins, including complement components, plasma serpins, inter-alpha-trypsin inhibitor proteins, lysozyme, fibulin, lumican, perlecan and collagen. HPA indicates frequent liver and hepatocyte enrichment, consistent with a circulating plasma-protein contribution. Choroid-plexus, astrocyte, fibroblast and decidual-stromal associations provide plausible local tissue sources, but the pattern is not primarily blood-cell specific: many genes are not detected in immune cells or have low immune-cell specificity. LYZ, LRG1, CFD, FBLN1 and SERPINF2 have some immune-cell associations, but these do not establish that the module is a leukocyte program. The shared signal between cerebrospinal fluid and cervix_uterine may therefore reflect blood-derived protein carryover, vascular or stromal extracellular material, and shared secretory or barrier-associated cell types. HPA reports that most module proteins are secreted, while cervix_uterine protein detection is incomplete; this limits tissue-localized interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a known complement core through C5-C9 and CFB-CFD, and supports links among coagulation regulators through SERPINC1-SERPIND1 and SERPINC1-SERPINF2. It also supports extracellular-matrix relationships involving COL5A1-LUM, FBLN1-HSPG2 and HSPG2-LUM, plus LRG1-SERPINA3. These are established relationships and explain part of the observed network coherence, but STRING reports no supplementary functional-enrichment result. hu.MAP provides broader complex-level support: CFB, C5, ITIH1 and ITIH4 recur together across several complexes, while SERPINA3 and SERPIND1 join related plasma-protein complexes. LRG1-LUM and LRG1-SERPINF2 occur in additional complexes (hu.MAP huMAP3_14295.1) and (hu.MAP huMAP3_11660.1). Thus, the module contains a recognizable plasma-complement and extracellular-matrix architecture, but many co-abundance edges are not represented as direct physical interactions in STRING or hu.MAP. Co-abundance should therefore not be equated with direct binding.

**STRING interactions (score >= 0.7)**: 10 of 300 gene pairs: C5–C9 (0.999); C5–CFB (0.774); C9–SERPINC1 (0.735); CFB–CFD (0.997); COL5A1–LUM (0.912); FBLN1–HSPG2 (0.904); HSPG2–LUM (0.78); LRG1–SERPINA3 (0.711); SERPINC1–SERPIND1 (0.837); SERPINC1–SERPINF2 (0.788)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (CFB, SERPINC1, SERPINA3, SERPIND1, ITIH1, ITIH4; 6/64); huMAP3_10678.1 (CFB, SERPINA3, C5, SERPIND1, ITIH1, ITIH4; 6/71); huMAP3_09531.1 (CFB, SERPINA3, C5, ITIH1, ITIH4; 5/47); huMAP3_10101.1 (CFB, SERPINA3, C5, ITIH1, ITIH4; 5/49); huMAP3_08796.1 (CFB, C5, ITIH1, ITIH4; 4/15); huMAP3_09832.1 (CFB, C5, ITIH1, ITIH4; 4/18); huMAP3_09434.1 (SERPINA3, C5, SERPIND1, ITIH4; 4/33); huMAP3_08395.1 (CFB, SERPINA3, C5, ITIH1; 4/43); huMAP3_00178.1 (C5, SERPINF2, ITIH1; 3/9); huMAP3_08224.1 (SERPINA3, C5, SERPIND1; 3/21); huMAP3_07119.1 (C5, SERPINF2; 2/6); huMAP3_06724.1 (CFB, ITIH1; 2/6); huMAP3_02811.1 (C5, ITIH1; 2/8); huMAP3_07541.1 (C5, ITIH1; 2/19); huMAP3_07701.1 (CFB, ITIH1; 2/22); huMAP3_09273.1 (CFB, ITIH1; 2/28); huMAP3_14295.1 (LRG1, LUM; 2/38); huMAP3_11660.1 (LRG1, SERPINF2; 2/43)

### Novelty

The biological components are not a new pathway: complement, coagulation inhibitors, inter-alpha-trypsin inhibitor proteins and extracellular-matrix proteins have established functions, and several relationships are already represented in STRING and hu.MAP. The potentially novel observation is the conservation of this particular co-abundance module across cerebrospinal fluid and cervix_uterine. However, the fact sheet does not compare this module with published tissue-proteomic modules or prior cross-tissue studies, so a claim of a new discovery is not justified. Absence of some module edges from STRING or hu.MAP is compatible with an informative co-abundance pattern, but it does not prove novelty. The most defensible conclusion is that this is a potentially useful cross-tissue association of known extracellular proteins whose tissue independence and biological reproducibility require external validation.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular-fluid interface in which liver-derived complement and protease inhibitors enter or circulate through cerebrospinal fluid and cervix_uterine-associated fluids, while local stromal, vascular, choroid-plexus or epithelial sources contribute matrix proteins. Complement components could provide innate surveillance, serpins could restrain proteolysis and coagulation, and ITIH and matrix proteins could organize hyaluronan- and collagen-associated extracellular material. The co-abundance may therefore arise from coordinated barrier or stromal remodeling, but it could also be driven mainly by variable plasma admixture. Testing paired fluid and tissue samples, blood-protein contamination markers, cell-type deconvolution, and orthogonal protein measurements would distinguish these alternatives.

### Important genes

#### C5

- **Related proteins** (co-abundance neighbors): ITIH1 (0.97), ITIH4 (0.96), ENDOD1 (0.93), CFB (0.92), PAM (0.92), C9 (0.83); STRING partners: C9 (0.999), CFB (0.774)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_00178.1, huMAP3_08224.1, huMAP3_07119.1, huMAP3_02811.1, huMAP3_07541.1
- **Function (MyGene.info)**: complement C5. This gene encodes a component of the complement system, a part of the innate immune system that plays an important role in inflammation, host homeostasis, and host defense against pathogens. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the C5 alpha chain, C5 beta chain, C5a anaphylatoxin and C5b. The C5 protein is comprised of the C5 alpha…
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.744); paroxysmal nocturnal hemoglobinuria (0.610); myasthenia gravis (0.586); atypical hemolytic-uremic syndrome (0.544); neuromyelitis optica (0.516)
- **Europe PMC papers**: 81450
- **Why important**: C5 is a central complement component and has one of the stronger positions in the module. It connects to ITIH1, ITIH4, CFB, ENDOD1 and PAM within the co-abundance graph, has direct STRING support with C9 and CFB, and recurs across many hu.MAP complexes (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_08796.1), (hu.MAP huMAP3_09832.1), (hu.MAP huMAP3_09434.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_00178.1), (hu.MAP huMAP3_08224.1), (hu.MAP huMAP3_07119.1), (hu.MAP huMAP3_02811.1) and (hu.MAP huMAP3_07541.1). Its established functions include complement activation, inflammatory signaling, chemotaxis and generation of C5-derived products. It is also extensively studied and strongly associated with complement deficiency and immune-mediated disease.
- **Conclusion**: Established evidence supports C5 as a key anchor of the module's complement-related extracellular biology. The hypothesis that C5 activity is functionally coordinated with the matrix and protease-regulator components in these two sample types remains unproven.

#### CFB

- **Related proteins** (co-abundance neighbors): ENDOD1 (0.98), CFD (0.93), C5 (0.92), ITIH1 (0.89), ITIH4 (0.88), SERPINC1 (0.87), PAM (0.84), CLEC3B (0.83), GSTP1 (0.83); STRING partners: C5 (0.774), CFD (0.997)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_08395.1, huMAP3_06724.1, huMAP3_07701.1, huMAP3_09273.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB is a highly connected complement factor linking ENDOD1, CFD, C5, ITIH1, ITIH4, SERPINC1, PAM and CLEC3B. Its STRING relationship with CFD is particularly well established, and it also connects to C5. CFB recurs across numerous hu.MAP complexes, including (hu.MAP huMAP3_15040.1), (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_09531.1), (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_08796.1), (hu.MAP huMAP3_09832.1), (hu.MAP huMAP3_08395.1), (hu.MAP huMAP3_06724.1), (hu.MAP huMAP3_07701.1) and (hu.MAP huMAP3_09273.1). Its established function is activation of the alternative complement pathway through formation of the C3 convertase after cleavage by factor D. It has substantial literature and disease associations involving complement deficiency and atypical hemolytic-uremic disease.
- **Conclusion**: Established evidence identifies CFB as a central alternative-pathway component and a strong mechanistic anchor for the module. Its co-abundance with matrix and coagulation proteins may indicate shared extracellular regulation, but this is a hypothesis rather than demonstrated pathway coupling.

#### ITIH4

- **Related proteins** (co-abundance neighbors): C5 (0.96), C9 (0.96), PAM (0.90), AZGP1 (0.88), CFB (0.88), LUM (0.87), RNASET2 (0.84), FBLN1 (0.84), SERPINF2 (0.83), LRG1 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_09434.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 is a prominent network connector linking C5, C9, CFB, LUM, FBLN1, RNASET2, PAM and AZGP1. It is present in multiple hu.MAP complexes (hu.MAP huMAP3_15040.1) through (hu.MAP huMAP3_09434.1) and (hu.MAP huMAP3_08395.1), alongside complement and plasma proteins. HPA identifies liver enrichment and astrocyte, neuronal and ependymal associations, while the protein is secreted to blood. Its established biology includes secretion by the liver, cleavage by plasma kallikrein, acute-phase behavior, cytokine response and hyaluronan metabolism. Its literature is smaller than that of C5 but sufficient to support a recognized extracellular and inflammatory role.
- **Conclusion**: Established evidence supports ITIH4 as a bridge between circulating acute-phase proteins and extracellular-matrix or hyaluronan biology, making it especially informative for a cerebrospinal-fluid and cervix_uterine module. Whether it actively organizes the conserved module, rather than merely tracking shared protein exposure, remains a hypothesis.

#### FBLN1

- **Related proteins** (co-abundance neighbors): LYZ (0.93), SERPINF2 (0.90), PAM (0.86), AZGP1 (0.86), CLEC3B (0.84), ITIH4 (0.84), LUM (0.83), C9 (0.82); STRING partners: HSPG2 (0.904)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fibulin 1. Fibulin 1 is a secreted glycoprotein that becomes incorporated into a fibrillar extracellular matrix. Calcium-binding is apparently required to mediate its binding to laminin and nidogen. It mediates platelet adhesion via binding fibrinogen. Four splice variants which differ in the 3' end have been identified. Each variant encodes a different isoform, but no functional distinctions have been ident…
- **Diseases (Open Targets)**: synpolydactyly type 2 (0.447); FBLN1-related developmental delay-central nervous system anomaly-syndactyly syndrome (0.377); synpolydactyly (0.371); adolescent idiopathic scoliosis (0.306); alcohol drinking (0.219)
- **Europe PMC papers**: 2655
- **Why important**: FBLN1 links the module's secreted plasma-like proteins to extracellular matrix through LYZ, SERPINF2, PAM, AZGP1, CLEC3B, ITIH4 and LUM. It has STRING support with HSPG2 and is associated by HPA with choroid plexus epithelial cells, decidual stromal cells and endometrial stromal cells, as well as secretion to extracellular matrix. Its established function is incorporation into fibrillar extracellular matrix, interaction with laminin and nidogen, platelet adhesion and regulation of matrix organization. It has substantial literature and disease associations involving connective-tissue and developmental disorders.
- **Conclusion**: Established evidence supports FBLN1 as a plausible local matrix contributor linking cerebrospinal-fluid interfaces and reproductive-tract stroma. A direct role in generating the cross-tissue co-abundance pattern is plausible but not established by the available data.

#### LUM

- **Related proteins** (co-abundance neighbors): C9 (0.91), ITIH4 (0.87), AZGP1 (0.85), FBLN1 (0.83), PAM (0.80); STRING partners: COL5A1 (0.912), HSPG2 (0.78)
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14295.1
- **Function (MyGene.info)**: lumican. This gene encodes a member of the small leucine-rich proteoglycan (SLRP) family that includes decorin, biglycan, fibromodulin, keratocan, epiphycan, and osteoglycin. In these bifunctional molecules, the protein moiety binds collagen fibrils and the highly charged hydrophilic glycosaminoglycans regulate interfibrillar spacings. Lumican is the major keratan sulfate proteoglycan of the cornea but is …
- **Diseases (Open Targets)**: lumbar disc herniation (0.359); Dupuytren Contracture (0.357); fibroblastic disorder (0.357); Hallux valgus (0.357); preeclampsia (0.154)
- **Europe PMC papers**: 14825
- **Why important**: LUM connects C9, ITIH4, AZGP1, FBLN1 and PAM and has STRING relationships with COL5A1 and HSPG2. It is represented in hu.MAP complex (hu.MAP huMAP3_14295.1). HPA associates it with placenta, gallbladder and decidual stromal cells and identifies secretion to extracellular matrix. Its established functions include collagen-fibril organization, regulation of growth-factor responses and organization of interstitial collagenous matrices. It has extensive literature and recognized associations with fibroblastic and connective-tissue disorders.
- **Conclusion**: Established evidence supports LUM as an extracellular-matrix organizer that may account for the stromal component of the module. Its association with complement and plasma proteins may reflect shared matrix-fluid biology, but a causal interaction is not demonstrated.

#### SERPINC1

- **Related proteins** (co-abundance neighbors): ENDOD1 (0.90), C9 (0.89), CFB (0.87), PAM (0.83), RNASET2 (0.81); STRING partners: C9 (0.735), SERPIND1 (0.837), SERPINF2 (0.788)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 connects ENDOD1, C9, CFB, PAM and RNASET2 and has STRING relationships with C9, SERPIND1 and SERPINF2. It is included in hu.MAP complex (hu.MAP huMAP3_15040.1). HPA identifies liver and hepatocyte enrichment and secretion to blood. Its established function is antithrombin-mediated inhibition of thrombin and other activated coagulation proteases, with enhancement by heparin. It is extensively studied and strongly associated with hereditary antithrombin deficiency and venous thrombotic disease.
- **Conclusion**: Established evidence supports SERPINC1 as the module's clearest coagulation-regulatory anchor and as evidence that the module is partly plasma derived. The possibility that coagulation control is biologically coordinated with complement and matrix remodeling in these samples remains a hypothesis.

## Module 4

**Tissue pair**: cerebrospinal_fluid and cervix_uterine  
**Genes (22)**: GOT1, AFM, BASP1, C1QC, CP, CHI3L1, COL1A2, COL6A1, FCGBP, AHSG, FGA, FMOD, IGFBP2, SERPING1, ITIH2, KNG1, LDHA, PLTP, GM2A, SELENBP1, TXN, TIMP1

### Function

The module is most consistent with a circulating extracellular-plasma and tissue-remodelling program rather than a narrowly defined intracellular pathway. Its genes include coagulation and kinin-system components, complement regulation, extracellular-matrix proteins, lipid and metal transport proteins, and inflammatory or redox-associated proteins. The strongest functional interpretation is coordinated abundance of secreted blood proteins together with extracellular-matrix and stromal signals. No GO/KEGG term passed global correction, so no pathway is claimed as statistically enriched. The interpretation is therefore based on gene functions, the co-abundance structure, STRING links, hu.MAP complexes, and tissue-expression evidence. The network also contains a smaller intracellular metabolic/redox component involving GOT1, LDHA, TXN, and related genes, which may reflect shared sample biology or protein carryover rather than a unified biochemical pathway.

**Cell composition.** The module is dominated by secreted or extracellular proteins: most genes have HPA secretome annotations indicating secretion to blood, secretion in other tissues, or secretion to the extracellular matrix. Many members are liver-enriched or hepatocyte-associated, including FGA, CP, KNG1, AHSG, AFM, ITIH2, and SERPING1. COL1A2, COL6A1, FMOD, and TIMP1 support a stromal and extracellular-matrix component, with several associated with fibroblasts or decidual stromal cells. C1QC, CHI3L1, PLTP, BASP1, GM2A, and SERPING1 have immune-cell or myeloid-associated signals, but many other members are not detected in immune cells or have low immune-cell specificity. FCGBP is associated with goblet cells and several mucosal tissues. The overall composition strongly suggests that the shared cerebrospinal-fluid and cervix-uterine signal could reflect circulating plasma proteins, vascular or stromal material, and shared extracellular or immune-associated cell types, rather than a tissue-specific module produced uniformly by both tissues. HPA protein detection is available for cervix but not for cerebrospinal fluid in this summary, so direct protein-level confirmation in cerebrospinal fluid is unavailable here.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains a coherent but incomplete set of high-confidence relationships. AHSG links strongly with FGA, ITIH2, KNG1, and CP; FGA links with ITIH2 and KNG1; KNG1 links with SERPING1; and C1QC links with SERPING1. COL1A2 links with COL6A1, while GOT1 links with LDHA. These relationships support known associations among plasma proteins, complement or protease regulation, extracellular matrix, and metabolism, but STRING does not connect every module member. hu.MAP provides stronger systems-level support for the plasma-protein interpretation: the recurring complexes C1 through C9 repeatedly contain CP, KNG1, FGA, AHSG, SERPING1, and ITIH2, with C1QC included in several of them. C10 and C11 connect C1QC with CHI3L1, while C17 and C18 connect GM2A with FCGBP. Thus, part of the module reproduces known shared protein-complex or plasma-protein contexts. The module also contains genes with no listed hu.MAP complex or STRING partner, so the full co-abundance pattern extends beyond established physical interactions and should not be interpreted as a single experimentally demonstrated complex.

**STRING interactions (score >= 0.7)**: 10 of 231 gene pairs: AHSG–CP (0.776); AHSG–FGA (0.984); AHSG–ITIH2 (0.922); AHSG–KNG1 (0.936); C1QC–SERPING1 (0.959); COL1A2–COL6A1 (0.875); FGA–ITIH2 (0.811); FGA–KNG1 (0.908); GOT1–LDHA (0.972); KNG1–SERPING1 (0.964)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (CP, KNG1, FGA, C1QC, AHSG, SERPING1, ITIH2; 7/64); huMAP3_10678.1 (CP, KNG1, FGA, AHSG, SERPING1, ITIH2, FCGBP; 7/71); huMAP3_09531.1 (CP, KNG1, FGA, AHSG, SERPING1, ITIH2; 6/47); huMAP3_10101.1 (CP, KNG1, FGA, AHSG, SERPING1, ITIH2; 6/49); huMAP3_08395.1 (CP, KNG1, FGA, AHSG, ITIH2; 5/43); huMAP3_07265.1 (CP, KNG1, AHSG, ITIH2; 4/20); huMAP3_09273.1 (CP, KNG1, SERPING1, ITIH2; 4/28); huMAP3_02236.1 (CP, KNG1, ITIH2; 3/7); huMAP3_07432.1 (CP, FGA, AHSG; 3/18); huMAP3_04714.1 (C1QC, CHI3L1; 2/4); huMAP3_03784.1 (C1QC, CHI3L1; 2/5); huMAP3_02242.1 (FGA, AHSG; 2/9); huMAP3_08700.1 (CP, AHSG; 2/11); huMAP3_07541.1 (KNG1, ITIH2; 2/19); huMAP3_07701.1 (KNG1, ITIH2; 2/22); huMAP3_09434.1 (FGA, AHSG; 2/33); huMAP3_09125.1 (GM2A, FCGBP; 2/53); huMAP3_09929.1 (GM2A, FCGBP; 2/75)

### Novelty

This is not established as a wholly new molecular complex or pathway. Several relationships and recurring protein groupings are already represented in STRING and hu.MAP, especially the CP–KNG1–FGA–AHSG–ITIH2–SERPING1 group and the C1QC–SERPING1 relationship. The co-abundance module may nevertheless be a new observation at the level of a conserved cerebrospinal-fluid and cervix-uterine sample pattern, particularly because the module combines plasma proteins, extracellular matrix, mucosal or stromal signals, immune-associated proteins, and intracellular metabolic proteins. However, absence of some members from STRING or hu.MAP does not establish novelty: it may reflect incomplete interaction coverage, tissue-specific abundance, indirect regulation, sample composition, or technical co-variation. A claim of novelty would require comparison with prior cross-tissue co-abundance studies and independent replication, neither of which is supplied here.

**Hypothesis.** Hypothesis: the module represents a shared extracellular milieu generated by vascular leakage or transport, stromal and extracellular-matrix activity, and regulated inflammatory or complement-related protein abundance. Liver-derived plasma proteins may enter or influence both sample environments, while cervix-associated stromal and extracellular-matrix proteins contribute a local tissue component. The C1QC, CHI3L1, and SERPING1 signals could reflect macrophage or innate-immune-associated material, whereas COL1A2, COL6A1, FMOD, and TIMP1 could reflect matrix-producing stromal cells. GOT1, LDHA, and TXN may indicate accompanying metabolic or oxidative-state variation. This model predicts that the module will track plasma contamination or vascular permeability, stromal content, and inflammatory state more strongly than a single tissue-intrinsic pathway. It should be tested by measuring plasma-protein contamination, cell-type proportions, vascular or matrix markers, and the module in independent cerebrospinal-fluid and cervix-uterine cohorts.

### Important genes

#### COL1A2

- **Related proteins** (co-abundance neighbors): C1QC (0.93), CHI3L1 (0.91), IGFBP2 (0.91), PLTP (0.90), FCGBP (0.90), GOT1 (0.90), CP (0.87), TIMP1 (0.87), FGA (0.86), ITIH2 (0.86), BASP1 (0.85), LDHA (0.85), GM2A (0.84), AFM (0.82), AHSG (0.82), TXN (0.81); STRING partners: COL6A1 (0.875)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type I alpha 2 chain. This gene encodes the pro-alpha2 chain of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIB, recessive Ehlers-Danlos syndrome Classi…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 2 (0.845); osteogenesis imperfecta type 3 (0.830); osteogenesis imperfecta type 4 (0.820); Ehlers-Danlos syndrome, cardiac valvular type (0.777); osteogenesis imperfecta type 1 (0.770)
- **Europe PMC papers**: 67901
- **Why important**: COL1A2 is the strongest network hub in the supplied module and connects the extracellular-matrix branch with C1QC, CHI3L1, IGFBP2, PLTP, FCGBP, GOT1, CP, and TIMP1. HPA supports cervix, ovary, smooth-muscle, decidual-stromal, and fibroblast-associated expression, and identifies secretion to the extracellular matrix. Its documented functions include collagen fibril organization, tissue development, and transforming-growth-factor signalling. It has extensive literature and strong disease associations with osteogenesis imperfecta, Ehlers-Danlos syndromes, osteoporosis, and atypical Marfan syndrome.
- **Conclusion**: Established evidence supports COL1A2 as a central extracellular-matrix and stromal marker in this module. Its position makes it a plausible indicator of matrix-producing cell content or tissue remodelling, but the module does not establish that COL1A2 regulates the plasma-protein branch.

#### FGA

- **Related proteins** (co-abundance neighbors): C1QC (0.96), FCGBP (0.92), TXN (0.92), GM2A (0.89), TIMP1 (0.87), KNG1 (0.87), COL1A2 (0.86), BASP1 (0.85), GOT1 (0.84), PLTP (0.84), CHI3L1 (0.82), AHSG (0.80); STRING partners: AHSG (0.984), ITIH2 (0.811), KNG1 (0.908)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_02242.1, huMAP3_09434.1
- **Function (MyGene.info)**: fibrinogen alpha chain. This gene encodes the alpha subunit of the coagulation factor fibrinogen, which is a component of the blood clot. Following vascular injury, the encoded preproprotein is proteolytically processed by thrombin during the conversion of fibrinogen to fibrin. Mutations in this gene lead to several disorders, including dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia and renal amyloidosis. Alterna…
- **Diseases (Open Targets)**: familial dysfibrinogenemia (0.789); familial visceral amyloidosis (0.765); congenital afibrinogenemia (0.757); familial hypodysfibrinogenemia (0.659); congenital fibrinogen deficiency (0.619)
- **Europe PMC papers**: 7516
- **Why important**: FGA is a highly connected module member and is linked in STRING to AHSG, ITIH2, and KNG1. It appears repeatedly in hu.MAP plasma-protein complexes C1 through C5, as well as additional complexes. HPA identifies liver and hepatocyte enrichment and secretion to blood. Its established function is the fibrinogen alpha chain, contributing to clot formation, platelet activation, cell-matrix adhesion, fibrinolysis, and plasminogen activation. It has substantial literature and disease associations involving dysfibrinogenemia, hypofibrinogenemia, afibrinogenemia, and familial visceral amyloidosis.
- **Conclusion**: Established evidence supports FGA as a major circulating coagulation and extracellular-adhesion component of the module. Its abundance may report plasma or vascular content in the samples; the module alone does not show active coagulation or prove local synthesis in either tissue.

#### CP

- **Related proteins** (co-abundance neighbors): C1QC (0.93), LDHA (0.91), COL1A2 (0.87), TXN (0.86), TIMP1 (0.86), SELENBP1 (0.85), PLTP (0.82), CHI3L1 (0.82), GOT1 (0.82), FCGBP (0.81), SERPING1 (0.80); STRING partners: AHSG (0.776)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_07265.1, huMAP3_09273.1, huMAP3_02236.1, huMAP3_07432.1, huMAP3_08700.1
- **Function (MyGene.info)**: ceruloplasmin. The protein encoded by this gene is a metalloprotein that binds most of the copper in plasma and is involved in the peroxidation of Fe(II)transferrin to Fe(III) transferrin. Mutations in this gene cause aceruloplasminemia, which results in iron accumulation and tissue damage, and is associated with diabetes and neurologic abnormalities. Two transcript variants, one protein-coding and the other not…
- **Diseases (Open Targets)**: aceruloplasminemia (0.827); cerebellar ataxia (0.572); Hermansky-Pudlak syndrome 3 (0.564); Hermansky-Pudlak syndrome (0.543); neurodegeneration with brain iron accumulation (0.510)
- **Europe PMC papers**: 171928
- **Why important**: CP is a highly connected member bridging C1QC, LDHA, COL1A2, TXN, TIMP1, SELENBP1, PLTP, and CHI3L1. It is linked by STRING to AHSG and appears across many hu.MAP complexes, especially those containing the recurring plasma-protein group. HPA supports liver enrichment and choroid-plexus, endometrial-glandular, endometrial-luminal, and endometrial-secretory cell associations. Ceruloplasmin transports copper and participates in iron handling and oxidant detoxification. It has very extensive literature and disease associations including aceruloplasminemia, cerebellar ataxia, and neurodegeneration with brain iron accumulation.
- **Conclusion**: Established evidence supports CP as a circulating metal-transport and redox-related marker that connects plasma biology with the cerebrospinal-fluid context. Its presence is compatible with altered extracellular iron or copper handling, but the module does not demonstrate metal dysregulation or a causal neurological mechanism.

#### C1QC

- **Related proteins** (co-abundance neighbors): FGA (0.96), TXN (0.94), CP (0.93), COL1A2 (0.93), LDHA (0.91), KNG1 (0.88), AHSG (0.83), ITIH2 (0.81); STRING partners: SERPING1 (0.959)
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_04714.1, huMAP3_03784.1
- **Function (MyGene.info)**: complement C1q C chain. This gene encodes the C-chain polypeptide of serum complement subcomponent C1q, which associates with C1r and C1s to yield the first component of the serum complement system. C1q is composed of 18 polypeptide chains which include 6 A-chains, 6 B-chains, and 6 C-chains. Each chain contains an N-terminal collagen-like region and a C-terminal C1q globular domain. C1q deficiency is associated with lup…
- **Diseases (Open Targets)**: immunodeficiency due to a classical component pathway complement deficiency (0.619); C1Q deficiency (0.597); neurodegenerative disease (0.540); complement deficiency (0.462); C1Q deficiency 1 (0.462)
- **Europe PMC papers**: 4647
- **Why important**: C1QC occupies a central position in the network and links strongly with FGA, TXN, CP, COL1A2, LDHA, KNG1, AHSG, and ITIH2. It is linked in STRING to SERPING1 and appears in hu.MAP complexes C1, C10, and C11. HPA associates it with lymphoid tissue, Hofbauer cells, Kupffer cells, macrophages, and intermediate monocytes, and identifies secretion to blood. Its established functions include classical complement activation, immune response, macrophage-related regulation, and synapse pruning. It has disease associations with C1Q deficiency, immunodeficiency, lupus-related pathology, and neurodegenerative disease.
- **Conclusion**: Established evidence supports C1QC as the module's clearest innate-immune and complement-associated marker. It may indicate macrophage or complement-related material in the samples, but co-abundance cannot distinguish local production from transported or contaminating extracellular protein.

#### KNG1

- **Related proteins** (co-abundance neighbors): BASP1 (0.96), AFM (0.93), AHSG (0.91), PLTP (0.90), SELENBP1 (0.89), C1QC (0.88), FGA (0.87), FCGBP (0.86), GOT1 (0.80); STRING partners: AHSG (0.936), FGA (0.908), SERPING1 (0.964)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_07265.1, huMAP3_09273.1, huMAP3_02236.1, huMAP3_07541.1, huMAP3_07701.1
- **Function (MyGene.info)**: kininogen 1. This gene uses alternative splicing to generate two different proteins- high molecular weight kininogen (HMWK) and low molecular weight kininogen (LMWK). HMWK is essential for blood coagulation and assembly of the kallikrein-kinin system. Also, bradykinin, a peptide causing numerous physiological effects, is released from HMWK. Bradykinin also functions as an antimicrobial peptide with antibacteri…
- **Diseases (Open Targets)**: congenital high-molecular-weight kininogen deficiency (0.733); venous thromboembolism (0.547); hereditary angioedema (0.458); serum lipopolysaccharide activity (0.367); ischemic stroke (0.363)
- **Europe PMC papers**: 2325
- **Why important**: KNG1 is a highly connected bridge among BASP1, AFM, AHSG, PLTP, SELENBP1, C1QC, FGA, and FCGBP. It has high-confidence STRING relationships with AHSG, FGA, and SERPING1 and appears in many recurring hu.MAP plasma-protein complexes. HPA supports liver and hepatocyte association and secretion to blood. Its products participate in coagulation, the kallikrein-kinin system, bradykinin release, vasodilation, cell-adhesion regulation, and antimicrobial activity. Its disease associations include high-molecular-weight kininogen deficiency, venous thromboembolism, hereditary angioedema, and ischemic stroke.
- **Conclusion**: Established evidence supports KNG1 as a key circulating protease-regulation and vasoactive-protein component. It provides a plausible bridge between coagulation, vascular permeability, and inflammation, but the module does not demonstrate activation of the kallikrein-kinin system.

#### AHSG

- **Related proteins** (co-abundance neighbors): FMOD (0.98), AFM (0.94), KNG1 (0.91), PLTP (0.85), C1QC (0.83), COL6A1 (0.82), COL1A2 (0.82), TIMP1 (0.81), FGA (0.80); STRING partners: CP (0.776), FGA (0.984), ITIH2 (0.922), KNG1 (0.936)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08395.1, huMAP3_07265.1, huMAP3_07432.1, huMAP3_02242.1, huMAP3_08700.1, huMAP3_09434.1
- **Function (MyGene.info)**: alpha 2-HS glycoprotein. The protein encoded by this gene is a negatively-charged serum glycoprotein that is synthesized by hepatocytes. The encoded protein consists of two polypeptide chains, which are both cleaved from a proprotein encoded from a single mRNA. It is involved in several processes, including endocytosis, brain development, and the formation of bone tissue. Defects in this gene are a cause of susceptibility…
- **Diseases (Open Targets)**: alopecia - intellectual disability syndrome (0.476); otosclerosis (0.465); nephrolithiasis, calcium oxalate (0.417); calcium oxalate urolithiasis (0.416); neurodegenerative disease (0.204)
- **Europe PMC papers**: 2310
- **Why important**: AHSG is a central plasma-protein node with strong STRING links to CP, FGA, ITIH2, and KNG1 and repeated membership in hu.MAP complexes C1 through C6, C9, C12, C13, and C16. HPA identifies liver and hepatocyte enrichment and secretion to blood. Its established functions include acute-phase response, endocytosis, brain development, and regulation of bone mineralization and insulin-receptor signalling. It has disease associations involving neurodegenerative disease, calcium-oxalate urolithiasis, otosclerosis, and alopecia-intellectual disability syndrome.
- **Conclusion**: Established evidence supports AHSG as an important integrator of the recurring circulating-protein cluster and of extracellular mineral or inflammatory biology. It is a plausible marker of systemic plasma composition, but the module does not establish a direct AHSG-mediated mechanism in either tissue.

## Module 5

**Tissue pair**: cerebrospinal_fluid and cervix_uterine  
**Genes (24)**: ADAM10, ALB, APOA1, APOD, APOH, SMPDL3B, CPM, CD109, CLU, C3, GNS, GOLM1, HYOU1, JCHAIN, IGKC, ITGAM, ITGB2, CD58, LGALS3BP, MSLN, LCN2, PIGR, SORL1, TNC

### Function

No GO/KEGG term passed global correction, so there is no globally significant pathway annotation for this module. The gene pattern nevertheless supports a composite extracellular and immune-interface function: plasma lipid and carrier proteins, complement activity, immunoglobulin transport, epithelial secretion, leukocyte adhesion, endocytosis, and extracellular-matrix or stress-related biology. The strongest functional interpretation is not a single canonical pathway but coordination between secreted host-defense material and epithelial or myeloid handling of that material. The co-abundance network connects complement C3 with ITGAM and ITGB2, while PIGR connects with JCHAIN, supporting links between complement-associated innate defense, leukocyte interactions, and polymeric immunoglobulin transcytosis. These are functional interpretations from gene annotations and network structure, not globally significant enrichment claims.

**Cell composition.** The module is strongly dominated by secreted, circulating, or extracellular proteins. The HPA summary identifies most genes as secreted, and several prominent members, including ALB, APOA1, APOH, C3, CLU, SORL1, JCHAIN, IGKC, LGALS3BP, and SMPDL3B, are secreted to blood or associated with extracellular vesicles or immunoglobulin material. HPA tissue and single-cell evidence points repeatedly to liver and hepatocytes, intestine and secretory epithelial cells, bone marrow, neutrophils, monocytes, macrophages, and other myeloid populations. PIGR, JCHAIN, LCN2, C3, CLU, MSLN, and TNC also show epithelial or stromal associations relevant to cervix_uterine. This composition makes blood or plasma carryover, immune-cell content, and shared secretory or epithelial cell types plausible contributors to the conserved signal. HPA protein detection is unavailable for cerebrospinal_fluid in this sheet, whereas cervix_uterine has selective detection rather than uniform detection across the module. The module should therefore not be interpreted as proof of a cerebrospinal-fluid-specific tissue mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a pre-existing interaction backbone rather than an isolated set of unrelated genes. The most coherent known relationships are among ALB, APOA1, APOH, APOD, C3, and CLU, and between C3 and the leukocyte integrin pair ITGAM–ITGB2. CD58 also connects to ITGB2, while JCHAIN and PIGR form a particularly strong known pair. These interactions are consistent with plasma lipoprotein and carrier biology, complement handling, immune-cell adhesion or phagocytosis, and epithelial immunoglobulin transport. hu.MAP independently places C3, APOA1, ALB, APOH, and LCN2 together across several complexes (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1), places JCHAIN and PIGR together across multiple secretory or mucosal complexes (hu.MAP huMAP3_02710.1) (hu.MAP huMAP3_07637.1) (hu.MAP huMAP3_10720.1) (hu.MAP huMAP3_06906.1) (hu.MAP huMAP3_08928.1) (hu.MAP huMAP3_08525.1) and (hu.MAP huMAP3_13577.1), and places ITGAM with ITGB2 in immune-associated complexes (hu.MAP huMAP3_08988.1) and (hu.MAP huMAP3_14295.1). ADAM10 and HYOU1 recur in complexes (hu.MAP huMAP3_09327.1) and (hu.MAP huMAP3_06775.1). Thus, part of the module reflects known protein associations and recurring complex membership. The remaining co-abundance links, especially those joining these biochemical and cellular compartments, may reflect shared sample composition or coordinated trafficking rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 20 of 276 gene pairs: ALB–APOA1 (0.998); ALB–APOH (0.933); ALB–C3 (0.959); ALB–CLU (0.831); ALB–ITGAM (0.727); ALB–LCN2 (0.712); APOA1–APOD (0.96); APOA1–APOH (0.985); APOA1–C3 (0.957); APOA1–CLU (0.998); APOD–APOH (0.804); APOD–CLU (0.939); APOH–CLU (0.911); C3–CLU (0.803); C3–ITGAM (0.999); C3–ITGB2 (0.998); CD58–ITGB2 (0.778); CLU–SORL1 (0.862); ITGAM–ITGB2 (0.999); JCHAIN–PIGR (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09434.1 (C3, APOA1, ALB, LCN2; 4/33); huMAP3_15040.1 (C3, APOA1, APOH, ALB; 4/64); huMAP3_10678.1 (C3, APOA1, ALB, LCN2; 4/71); huMAP3_07432.1 (C3, APOA1, ALB; 3/18); huMAP3_08395.1 (C3, APOA1, ALB; 3/43); huMAP3_09531.1 (C3, APOA1, ALB; 3/47); huMAP3_10101.1 (C3, APOA1, ALB; 3/49); huMAP3_09327.1 (ADAM10, CD109, HYOU1; 3/93); huMAP3_02710.1 (JCHAIN, PIGR; 2/6); huMAP3_07637.1 (JCHAIN, PIGR; 2/8); huMAP3_10720.1 (JCHAIN, PIGR; 2/8); huMAP3_06906.1 (JCHAIN, PIGR; 2/9); huMAP3_08928.1 (JCHAIN, PIGR; 2/9); huMAP3_08525.1 (JCHAIN, PIGR; 2/12); huMAP3_08988.1 (ITGB2, ITGAM; 2/17); huMAP3_07265.1 (APOA1, ALB; 2/20); huMAP3_08224.1 (C3, APOA1; 2/21); huMAP3_13577.1 (JCHAIN, PIGR; 2/35); huMAP3_14295.1 (ITGB2, ITGAM; 2/38); huMAP3_11343.1 (JCHAIN, PIGR; 2/54); huMAP3_06775.1 (ADAM10, HYOU1; 2/60)

### Novelty

This module should not be called a wholly new protein interaction module. Several relationships and complexes are already represented in STRING and hu.MAP, especially the plasma-protein cluster, the C3–ITGAM–ITGB2 axis, and the JCHAIN–PIGR pair. The potentially novel aspect is the conserved co-abundance organization across cerebrospinal_fluid and cervix_uterine, particularly the combination of circulating proteins, mucosal immunoglobulin transport, and myeloid-associated components. That claim remains provisional because the module is compositionally compatible with shared blood, immune, secretory, or epithelial contributions, and because absence of a relationship from STRING or hu.MAP would not establish novelty. Demonstrating novelty would require comparison with matched tissue cohorts, contamination-aware analyses, independent datasets, and controls for cell-type abundance and plasma protein leakage.

**Hypothesis.** Hypothesis: the conserved module reflects a shared extracellular host-defense and cargo-handling environment rather than one tissue-restricted pathway. In this model, liver-derived carrier and complement proteins enter or are represented in extracellular fluids; epithelial cells use PIGR to transport polymeric immunoglobulin complexes containing JCHAIN; C3-derived material is sensed or cleared through ITGAM–ITGB2-bearing myeloid cells; and CLU, APOA1, APOH, LCN2, SORL1, ADAM10, and HYOU1 contribute to extracellular cargo stabilization, uptake, processing, or stress adaptation. In cervix_uterine, epithelial and secretory-cell expression could generate this signal locally, while in cerebrospinal_fluid the signal could arise from circulating proteins, barrier-associated secretion, choroid-plexus-related biology, or immune-cell material. This is a mechanistic hypothesis and requires validation by cell-resolved measurements, fluid proteomics, and assays distinguishing local production from blood-derived protein.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): CPM (1.00), SMPDL3B (0.96), ITGAM (0.92), SORL1 (0.84), CD58 (0.82), ITGB2 (0.81); STRING partners: ALB (0.959), APOA1 (0.957), CLU (0.803), ITGAM (0.999), ITGB2 (0.998)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09434.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_08224.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is a central network bridge linking CPM, ITGAM, ITGB2, SORL1, CD58, ALB, APOA1, and CLU. It is liver-enriched, secreted to blood, associated with non-classical monocytes and endometrial secretory cells, and is represented in many hu.MAP complexes (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) and (hu.MAP huMAP3_08224.1). Its literature volume is very large, and its disease associations include complement deficiency, complement-mediated renal disease, and age-related macular degeneration.
- **Conclusion**: Established evidence supports C3 as the principal complement and innate-defense anchor of the module, with plausible links to myeloid-cell recognition through ITGAM–ITGB2. It is not established that C3 drives the cross-tissue co-abundance pattern; shared plasma content or immune-cell abundance could produce the association.

#### PIGR

- **Related proteins** (co-abundance neighbors): SORL1 (1.00), MSLN (1.00), CPM (0.97), ADAM10 (0.97), JCHAIN (0.96), GOLM1 (0.91), CD109 (0.89), ITGAM (0.82); STRING partners: JCHAIN (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_02710.1, huMAP3_07637.1, huMAP3_10720.1, huMAP3_06906.1, huMAP3_08928.1, huMAP3_08525.1, huMAP3_13577.1, huMAP3_11343.1
- **Function (MyGene.info)**: polymeric immunoglobulin receptor. This gene is a member of the immunoglobulin superfamily. The encoded poly-Ig receptor binds polymeric immunoglobulin molecules at the basolateral surface of epithelial cells; the complex is then transported across the cell to be secreted at the apical surface. A significant association was found between immunoglobulin A nephropathy and several SNPs in this gene.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: clear cell renal carcinoma (0.453); renal carcinoma (0.279); IgA glomerulonephritis (0.120); breast carcinoma (0.120); neoplasm (0.112)
- **Europe PMC papers**: 5864
- **Why important**: PIGR is a high-connectivity epithelial and secretory node linked to JCHAIN, SORL1, ADAM10, CPM, CD109, ITGAM, and MSLN. HPA places it in intestine and salivary gland, in endometrial secretory cells, and as detected in cervix_uterine. Its repeated membership with JCHAIN across hu.MAP complexes (hu.MAP huMAP3_02710.1) (hu.MAP huMAP3_07637.1) (hu.MAP huMAP3_10720.1) (hu.MAP huMAP3_06906.1) (hu.MAP huMAP3_08928.1) (hu.MAP huMAP3_08525.1) and (hu.MAP huMAP3_13577.1) supports a known mucosal immunoglobulin-transport context.
- **Conclusion**: Established evidence supports PIGR as the strongest epithelial-transcytosis marker in the module and makes local cervix_uterine secretion biologically plausible. A role in the cerebrospinal_fluid component is a hypothesis, because the sheet lacks matching HPA protein-detection data for that fluid and does not establish local cerebrospinal-fluid production.

#### JCHAIN

- **Related proteins** (co-abundance neighbors): CD109 (0.99), LCN2 (0.99), PIGR (0.96), ADAM10 (0.92), CLU (0.90), ITGAM (0.84); STRING partners: PIGR (0.999)
- **HPA**: Tissue enhanced; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02710.1, huMAP3_07637.1, huMAP3_10720.1, huMAP3_06906.1, huMAP3_08928.1, huMAP3_08525.1, huMAP3_13577.1, huMAP3_11343.1
- **Function (MyGene.info)**: joining chain of multimeric IgA and IgM. Enables IgA binding activity and protein homodimerization activity. Contributes to several functions, including immunoglobulin receptor binding activity; peptidoglycan binding activity; and phosphatidylcholine binding activity. Involved in several processes, including defense response to other organism; glomerular filtration; and positive regulation of respiratory burst. Located in extracellular s…
- **Diseases (Open Targets)**: breast carcinoma (0.101); breast cancer (0.093); neoplasm (0.089); cancer (0.081); Barrett esophagus (0.062)
- **Europe PMC papers**: 2428
- **Why important**: JCHAIN is connected to PIGR, LCN2, CD109, ADAM10, CLU, and ITGAM, and has a direct high-confidence STRING relationship with PIGR. HPA associates it with plasma cells and B-cell populations and identifies it as secreted to blood. Its repeated hu.MAP co-membership with PIGR (hu.MAP huMAP3_02710.1) (hu.MAP huMAP3_07637.1) (hu.MAP huMAP3_10720.1) (hu.MAP huMAP3_06906.1) (hu.MAP huMAP3_08928.1) (hu.MAP huMAP3_08525.1), (hu.MAP huMAP3_13577.1), and (hu.MAP huMAP3_11343.1) supports polymeric immunoglobulin and mucosal-secretory biology.
- **Conclusion**: Established evidence supports JCHAIN as an immunoglobulin-complex and secretory component, potentially linking plasma-cell material to epithelial transport. Its presence does not by itself prove active local antibody production in either sampled tissue, because blood-derived or cell-composition effects remain plausible.

#### APOA1

- **Related proteins** (co-abundance neighbors): ITGB2 (0.98), CD58 (0.97), CPM (0.97), SORL1 (0.96); STRING partners: ALB (0.998), APOD (0.96), APOH (0.985), C3 (0.957), CLU (0.998)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09434.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_07432.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_07265.1, huMAP3_08224.1
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is liver-enriched, secreted to blood, and a major plasma HDL component involved in lipid transport and cholesterol efflux. It connects in STRING to ALB, APOD, APOH, C3, and CLU and appears in numerous hu.MAP complexes (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1), (hu.MAP huMAP3_07265.1), and (hu.MAP huMAP3_08224.1). It also has extensive literature and disease associations involving lipoprotein deficiency and cardiovascular or metabolic phenotypes.
- **Conclusion**: Established evidence supports APOA1 as a plasma-lipoprotein anchor that helps explain the extracellular carrier-protein portion of the module. Its network association with immune proteins may represent shared extracellular cargo or known biochemical associations, but it does not establish that lipid transport is the primary biological function of the entire module.

#### ITGAM

- **Related proteins** (co-abundance neighbors): CLU (0.94), C3 (0.92), LCN2 (0.92), LGALS3BP (0.85), JCHAIN (0.84), PIGR (0.82); STRING partners: ALB (0.727), C3 (0.999), ITGB2 (0.999)
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08988.1, huMAP3_14295.1
- **Function (MyGene.info)**: integrin subunit alpha M. This gene encodes the integrin alpha M chain. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. This I-domain containing alpha integrin combines with the beta 2 chain (ITGB2) to form a leukocyte-specific integrin referred to as macrophage receptor 1 ('Mac-1'), or inactivated-C3b (iC3b) receptor 3 ('CR3'). The alpha M beta 2 integrin is important in…
- **Diseases (Open Targets)**: systemic lupus erythematosus (0.416); IgA glomerulonephritis (0.338); autoimmune disorder of musculoskeletal system (0.265); hearing loss disorder (0.264); cutaneous lupus erythematosus (0.133)
- **Europe PMC papers**: 8991
- **Why important**: ITGAM is a myeloid-associated membrane receptor and a central partner of ITGB2. The pair has very strong STRING support, and ITGAM also connects to C3, CLU, LCN2, LGALS3BP, JCHAIN, and PIGR. HPA associates it with dendritic cells, Hofbauer cells, Kupffer cells, macrophages, and mast cells, while hu.MAP places it with ITGB2 in immune complexes (hu.MAP huMAP3_08988.1) and (hu.MAP huMAP3_14295.1).
- **Conclusion**: Established evidence supports ITGAM as the cellular myeloid and complement-receptor arm of the module, consistent with adhesion, phagocytosis, and receptor-mediated uptake. The hypothesis that it actively clears or processes the module's secreted cargo across both tissues remains unproven and could instead reflect myeloid-cell abundance.

## Module 6

**Tissue pair**: cerebrospinal_fluid and cervix_uterine  
**Genes (12)**: APOA4, APOB, APOC1, APOE, GUSB, ECM1, HEXA, PGK1, PLG, SOD2, F2, VTN

### Function

No GO or KEGG term passed global correction, and STRING reported no supplementary functional enrichment. The biological interpretation therefore comes from the gene annotations and network structure rather than from statistically significant pathway enrichment. The module is most consistent with a secreted extracellular-plasma program combining lipoprotein and cholesterol transport, coagulation and fibrinolysis, extracellular-matrix adhesion, and some redox and lysosomal biology. APOA4, APOC1, APOE, and APOB connect the lipoprotein component; F2 and PLG connect coagulation with fibrinolysis; VTN and ECM1 support extracellular adhesion and matrix interactions; SOD2 contributes an oxidative-stress axis; and GUSB and HEXA represent intracellular vesicular and glycan or lipid catabolism. These annotations support a coherent extracellular-fluid and tissue-interface interpretation, but they do not establish enrichment of any pathway.

**Cell composition.** The module is strongly dominated by secreted or extracellular proteins, with most genes annotated as secreted to blood or secreted to the extracellular matrix. HPA points especially toward liver and hepatocytes, with additional intestine and enterocyte associations, rather than a uniform cervix- or cerebrospinal-fluid-specific cellular program. Several genes are not detected in immune cells, while a smaller subset has myeloid dendritic-cell or neutrophil associations. APOE also has brain and decidual stromal-cell associations, and HEXA has choroid-plexus and microglial associations, but these do not outweigh the liver and plasma-protein pattern. The shared module may therefore reflect circulating protein carryover, vascular or plasma exposure, or a shared extracellular-fluid environment in the two sample groups. SOD2, PGK1, ECM1, GUSB, and HEXA provide some tissue or cellular signal, and several of these are detected in cervix tissue, so a purely blood-derived explanation should remain a hypothesis rather than a conclusion.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a pre-existing interaction backbone among APOA4, APOB, APOC1, and APOE, with additional links from this lipoprotein cluster to F2, PLG, and VTN. F2 and PLG are also connected, while PGK1 links to PLG. These relationships are biologically compatible with known plasma lipoprotein, coagulation, fibrinolysis, and extracellular-matrix biology. In contrast, STRING provides no functional-enrichment result for the module, and it reports no listed interaction support for several co-abundance links involving SOD2, ECM1, GUSB, or HEXA. hu.MAP repeatedly places F2, PLG, and APOA4 together in broad plasma-protein and complement or coagulation-related complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1), and places F2 with PLG in additional complexes (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1). APOC1 and APOA4 co-occur in another hu.MAP complex (hu.MAP huMAP3_09434.1), while PLG and APOA4 co-occur in a further broad complex (hu.MAP huMAP3_15040.1). These resources show that part of the module recapitulates known extracellular protein organization. They do not demonstrate that all module members form one physical complex or that the observed co-abundance relationships are causal.

**STRING interactions (score >= 0.7)**: 12 of 66 gene pairs: APOA4–APOB (0.992); APOA4–APOC1 (0.969); APOA4–APOE (0.995); APOB–APOC1 (0.996); APOB–APOE (0.999); APOB–F2 (0.832); APOB–PLG (0.774); APOC1–APOE (0.999); APOE–VTN (0.989); F2–PLG (0.826); PGK1–PLG (0.77); PLG–VTN (0.995)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08395.1 (F2, PLG, APOA4; 3/43); huMAP3_09531.1 (F2, PLG, APOA4; 3/47); huMAP3_10101.1 (F2, PLG, APOA4; 3/49); huMAP3_10678.1 (F2, PLG, APOA4; 3/71); huMAP3_08796.1 (F2, PLG; 2/15); huMAP3_09832.1 (F2, PLG; 2/18); huMAP3_07701.1 (F2, PLG; 2/22); huMAP3_09273.1 (F2, PLG; 2/28); huMAP3_09434.1 (APOC1, APOA4; 2/33); huMAP3_15040.1 (PLG, APOA4; 2/64)

### Novelty

The module should not be described as a wholly new molecular system. Its central lipoprotein, coagulation, fibrinolysis, and extracellular-matrix relationships are already represented in STRING and hu.MAP, and the component genes have extensive prior biological and disease literature. The potentially novel aspect is the conserved co-abundance of this particular combination across cerebrospinal fluid and cervix uterine, especially the coupling of established plasma proteins with SOD2, PGK1, ECM1, GUSB, and HEXA. However, the supplied evidence does not include independent replication, perturbation, tissue-origin deconvolution, or a direct comparison with previously published cross-tissue modules. Therefore the most defensible conclusion is that this may be a new dataset-level co-abundance observation built partly from well-known biology, not a proven novel pathway or complex. Lack of STRING or hu.MAP support for some edges is evidence of limited prior cataloguing, not proof of novelty.

**Hypothesis.** Hypothesis: the shared module reflects a circulating extracellular-fluid milieu in which liver- and intestine-derived lipoproteins associate with coagulation and fibrinolytic proteins, while vitronectin and ECM1 connect that milieu to tissue adhesion and matrix remodeling. In cerebrospinal fluid and cervix uterine samples, vascular or barrier-interface exposure could produce coordinated abundance of these proteins. PLG activation and thrombin-related biology may influence matrix turnover and cell migration, while SOD2 could mark accompanying oxidative stress and GUSB or HEXA could reflect vesicular or lysosomal processing by local or admixed cells. This model predicts that the module will be reduced after rigorous removal of plasma contamination, will track circulating protein abundance, and will separate into a plasma-protein submodule and a smaller local-cell or tissue-response component when cell composition and sample origin are experimentally controlled.

### Important genes

#### APOA4

- **Related proteins** (co-abundance neighbors): SOD2 (0.98), F2 (0.91), APOE (0.89), VTN (0.88), PLG (0.87), PGK1 (0.85), APOC1 (0.84); STRING partners: APOB (0.992), APOC1 (0.969), APOE (0.995)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_09434.1, huMAP3_15040.1
- **Function (MyGene.info)**: apolipoprotein A4. Apoliprotein (apo) A-IV gene contains 3 exons separated by two introns. A sequence polymorphism has been identified in the 3'UTR of the third exon.  The primary translation product is a 396-residue preprotein which after proteolytic processing is secreted its primary site of synthesis, the intestine, in association with chylomicron particles.  Although its precise function is not known, apo A-IV i…
- **Diseases (Open Targets)**: tubulointerstitial kidney disease, autosomal dominant, 2 (0.482); AL amyloidosis (0.463); metabolic syndrome (0.425); familial hyperlipidemia (0.359); diabetes mellitus (0.336)
- **Europe PMC papers**: 4955
- **Why important**: APOA4 is the highest-ranked network hub in the module and connects the lipoprotein cluster to F2, PLG, VTN, PGK1, SOD2, APOE, and APOC1. HPA places it in intestine and enterocytes and identifies it as secreted to blood. Its annotated roles include lipid transport, cholesterol metabolism, mucosal innate responses, and stress responses. It has substantial disease and literature coverage, including metabolic and amyloid-related associations. Its repeated participation in hu.MAP complexes with F2 and PLG (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_15040.1) makes it a useful bridge between the established plasma-protein core and the broader module.
- **Conclusion**: Established evidence supports APOA4 as a secreted intestinal lipoprotein-associated protein and a central network connector. The hypothesis that it organizes the cross-tissue module or links lipid transport to fibrinolytic and matrix biology remains untested.

#### PLG

- **Related proteins** (co-abundance neighbors): F2 (0.94), APOC1 (0.91), VTN (0.91), SOD2 (0.91), PGK1 (0.87), APOA4 (0.87); STRING partners: APOB (0.774), F2 (0.826), PGK1 (0.77), VTN (0.995)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1, huMAP3_15040.1
- **Function (MyGene.info)**: plasminogen. The plasminogen protein encoded by this gene is a serine protease that circulates in blood plasma as an inactive zymogen and is converted to the active protease, plasmin, by several plasminogen activators such as tissue plasminogen activator (tPA), urokinase plasminogen activator (uPA), kallikrein, and factor XII (Hageman factor). The conversion of plasminogen to plasmin involves the cleavage of t…
- **Diseases (Open Targets)**: hypoplasminogenemia (0.813); hereditary angioedema (0.737); hemorrhage (0.605); dysplasminogenemia (0.598); Menorrhagia (0.579)
- **Europe PMC papers**: 17740
- **Why important**: PLG is a highly connected module member and one of the strongest bridges between F2, VTN, APOA4, APOC1, PGK1, and APOB. It is liver- and hepatocyte-associated, secreted to blood, and encodes the zymogen that can become plasmin, with established roles in fibrinolysis, extracellular-matrix disassembly, collagen catabolism, and cell-substrate adhesion. It has extensive literature and disease associations involving plasminogen deficiency, bleeding, dysplasminogenemia, and menorrhagia. Its recurrence with F2 and APOA4 across many hu.MAP complexes (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) (hu.MAP huMAP3_15040.1) strongly anchors the extracellular coagulation and matrix interpretation.
- **Conclusion**: Established evidence supports PLG as a circulating fibrinolytic and matrix-remodeling factor and as a known component of the module's plasma-protein backbone. It is plausible, but not demonstrated, that PLG-mediated proteolysis drives the observed cross-tissue co-abundance.

#### F2

- **Related proteins** (co-abundance neighbors): ECM1 (0.95), PLG (0.94), APOA4 (0.91), APOC1 (0.90), APOB (0.80); STRING partners: APOB (0.832), PLG (0.826)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1, huMAP3_09273.1
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is a central bridge from the lipoprotein proteins to PLG and ECM1. It encodes prothrombin, whose activated product thrombin has established roles in fibrin formation, platelet activation, coagulation-factor activation, wound response, tissue repair, and angiogenesis. HPA associates it with liver and hepatocytes and secretion to blood. It has exceptionally extensive literature and disease links involving prothrombin deficiency, thrombophilia, venous thromboembolism, and deep-vein thrombosis. Its repeated hu.MAP co-occurrence with PLG and APOA4 (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1) and with PLG in additional complexes (hu.MAP huMAP3_08796.1) (hu.MAP huMAP3_09832.1) (hu.MAP huMAP3_07701.1) (hu.MAP huMAP3_09273.1) supports the coagulation-fibrinolysis interpretation.
- **Conclusion**: Established evidence supports F2 as a circulating coagulation factor that links the module to hemostasis and tissue repair. A direct thrombin-driven mechanism for the shared cerebrospinal-fluid and cervix-uterine signal is a hypothesis requiring activity measurements rather than abundance data alone.

#### APOE

- **Related proteins** (co-abundance neighbors): APOC1 (0.94), SOD2 (0.92), APOA4 (0.89), PGK1 (0.85); STRING partners: APOA4 (0.995), APOB (0.999), APOC1 (0.999), VTN (0.989)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein E. The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hype…
- **Diseases (Open Targets)**: hyperlipoproteinemia type 3 (0.803); coronary artery disorder (0.782); lipoprotein glomerulopathy (0.759); Alzheimer disease (0.696); familial hypercholesterolemia (0.651)
- **Europe PMC papers**: 74272
- **Why important**: APOE is a highly connected member of the lipoprotein cluster, linked in STRING to APOA4, APOB, APOC1, and VTN, and linked in the module network to SOD2, PGK1, and APOA4. HPA gives it enhanced associations with brain, liver, and adrenal gland and with decidual stromal cells, hepatocytes, macrophages, and melanocytes; it is also secreted to blood. Its established functions include lipid transport, triglyceride metabolism, receptor-mediated uptake, and responses to reactive oxygen species. It has very extensive literature and disease associations spanning dyslipidemia, coronary disease, and Alzheimer disease. Its brain association makes it especially relevant to the cerebrospinal-fluid side, although it does not establish local brain origin.
- **Conclusion**: Established evidence supports APOE as a broadly important secreted lipid-transport and disease-associated protein that may connect systemic lipid biology with neural-fluid biology. The idea that APOE provides a tissue-specific bridge between cerebrospinal fluid and cervix uterine is plausible but not established by this module.

#### VTN

- **Related proteins** (co-abundance neighbors): ECM1 (0.93), PLG (0.91), APOA4 (0.88), APOC1 (0.86), GUSB (0.82), HEXA (0.81); STRING partners: APOE (0.989), PLG (0.995)
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN connects PLG and the lipoprotein-associated proteins in the module network and has strong STRING relationships with APOE and PLG. HPA associates it with liver, cholangiocytes, and hepatocytes and identifies secretion to blood with vesicular and endoplasmic-reticulum localization. Its annotated functions include cell adhesion, cell-matrix adhesion, integrin signaling, migration, and interaction with plasminogen-activation regulators. It has substantial literature and disease associations involving vascular, inflammatory, neurodegenerative, and age-related disorders. VTN therefore provides a mechanistic link between a circulating plasma signature and extracellular matrix or cell-migration biology.
- **Conclusion**: Established evidence supports VTN as a secreted adhesive glycoprotein that interfaces with fibrinolytic and matrix-related processes. Its role as the mediator of tissue-interface behavior in this shared module remains a hypothesis.

#### ECM1

- **Related proteins** (co-abundance neighbors): SOD2 (0.99), F2 (0.95), VTN (0.93); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: extracellular matrix protein 1. This gene encodes a soluble protein that is involved in endochondral bone formation, angiogenesis, and tumor biology. It also interacts with a variety of extracellular and structural proteins, contributing to the maintenance of skin integrity and homeostasis. Mutations in this gene are associated with lipoid proteinosis disorder (also known as hyalinosis cutis et mucosae or Urbach-Wiethe disease) …
- **Diseases (Open Targets)**: lipoid proteinosis (0.780); gout (0.206); hereditary disease (0.194); neoplasm (0.114); autism (0.111)
- **Europe PMC papers**: 3258
- **Why important**: ECM1 is less connected than the plasma-protein hubs but is strategically positioned between SOD2, F2, and VTN. HPA associates it with epididymis and esophagus, with esophageal apical cells, and with secretion to the extracellular matrix; it is detected in cervix uterine tissue. Its established annotations include angiogenesis, extracellular and structural maintenance, peptidase regulation, bone-mineralization control, and NF-kappaB signaling. It has substantial literature and a strong disease association with lipoid proteinosis, a disorder affecting skin, mucosa, and viscera. ECM1 may therefore represent a local tissue-interface component rather than a simple plasma contaminant.
- **Conclusion**: Established evidence supports ECM1 as an extracellular-matrix and tissue-homeostasis protein with cervix detection and disease relevance. Its network placement suggests a possible local matrix bridge to coagulation and redox biology, but that interpretation requires tissue-specific validation.
