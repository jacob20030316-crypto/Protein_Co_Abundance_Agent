# Conserved co-abundance modules: brain and circulatory_system

## Module 0

**Tissue pair**: brain and circulatory_system  
**Genes (8)**: ANKRD28, DNAJC21, GNL3, HOMER3, NDC80, PBK, TTK, UBE2S

### Function

The strongest interpretation is a cell-division and chromosome-segregation module. The primary evidence is (GO:BP meiotic cell cycle phase transition; q_global = 0.0356), which links NDC80 and TTK to meiotic cell-cycle phase transition. This is supported functionally by the established roles of NDC80 in kinetochore microtubule attachment and chromosome segregation, TTK in the mitotic spindle checkpoint and centrosome duplication, UBE2S in ubiquitin-dependent exit from mitosis, and PBK in the mitotic cell cycle. Supplementary STRING enrichment (STRING NetworkNeighborAL Mixed, incl. Mitotic Spindle Checkpoint, and Mitotic sister chromatid segregation; within-query FDR = 0.0147) also points to the mitotic spindle checkpoint and mitotic sister-chromatid segregation through NDC80, UBE2S, TTK, and PBK. The module is therefore more consistent with proliferative or germ-cell and hematopoietic cell-cycle biology than with a brain-specific neuronal process. No other GO or KEGG term passed global correction; the absence of additional enriched terms does not invalidate the module.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Its composition instead suggests a mixture of broadly expressed intracellular proteins and cell-state-enriched genes. Several genes are enriched in bone marrow, lymphoid tissue, testis, spermatogenic cell types, erythrocyte progenitors, or megakaryocyte progenitors. ANKRD28 is immune-cell enriched, while HOMER3 is immune-cell enhanced and UBE2S, NDC80, and TTK show hematopoietic or lymphoid associations. PBK is not detected in immune cells and is enriched in testis-related contexts. Thus, the shared brain and circulatory-system signal may reflect proliferating or progenitor cell populations present in the sampled material, shared cell types, or a general cell-cycle state rather than a function intrinsic to mature neurons or circulating plasma. HPA protein detection supports expression of some module proteins in brain, but there is no matching circulatory-system tissue entry in the supplied HPA summary.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP meiotic cell cycle phase transition | 0.0356 | NDC80, TTK |

### STRING and hu.MAP

STRING provides a coherent, partially connected core: NDC80 is strongly connected to TTK and PBK, and PBK is strongly connected to TTK. These relationships are consistent with a known checkpoint and chromosome-segregation program and support the functional interpretation rather than establishing a new physical complex. STRING supplementary enrichment (STRING NetworkNeighborAL Mixed, incl. Mitotic Spindle Checkpoint, and Mitotic sister chromatid segregation; within-query FDR = 0.0147) independently points toward mitotic spindle checkpoint and sister-chromatid segregation biology. The co-abundance network also connects TTK to DNAJC21, ANKRD28, and GNL3, and connects DNAJC21 to UBE2S; NDC80 connects to HOMER3. Those co-abundance links are not established physical interactions in the supplied STRING results and should be interpreted as expression relationships. No hu.MAP complex contains at least two module members, so the module has no supported hu.MAP multi-member complex assignment.

**STRING interactions (score >= 0.7)**: 3 of 28 gene pairs: NDC80–PBK (0.934); NDC80–TTK (0.992); PBK–TTK (0.969)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Mixed, incl. Mitotic Spindle Checkpoint, and Mitotic sister chromatid segregation (FDR = 0.0147, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be claimed as a newly discovered molecular pathway. Its central biological theme is already well established through the known functions of NDC80, TTK, PBK, and UBE2S and through the STRING relationships among NDC80, TTK, and PBK. The potentially novel aspect is the cross-tissue co-abundance pattern linking this cell-cycle-associated gene set across brain and circulatory-system samples, together with peripheral genes such as DNAJC21, ANKRD28, HOMER3, and GNL3. However, the supplied evidence cannot determine whether that pattern reflects a previously undescribed regulatory relationship, shared proliferative cell populations, sample composition, or correlated cell-state variation. The absence of a hu.MAP complex is not evidence of novelty, and the absence of some STRING partners is likewise insufficient to establish a new finding.

**Hypothesis.** Hypothesis: the shared module reflects coordinated abundance of a proliferative progenitor or germ-cell-like program that couples spindle-checkpoint control and chromosome segregation with supporting processes such as ribosome biogenesis, ubiquitin-mediated cell-cycle progression, and nucleolar or scaffold functions. TTK may occupy a coordinating position because it has the highest weighted connectivity and links the STRING-supported NDC80–PBK core to DNAJC21, ANKRD28, and GNL3. In brain and circulatory-system datasets, this could arise from shared low-abundance progenitor or immune-related populations, or from a common proliferative state, rather than from mature brain tissue performing meiosis. This is a hypothesis and requires cell-resolved expression, pathology or proliferation markers, and experimental interaction or perturbation studies for testing.

### Important genes

#### TTK

- **Related proteins** (co-abundance neighbors): DNAJC21 (0.86), ANKRD28 (0.86), PBK (0.85), GNL3 (0.81), NDC80 (0.81); STRING partners: NDC80 (0.992), PBK (0.969)
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TTK protein kinase. This gene encodes a dual specificity protein kinase with the ability to phosphorylate tyrosine, serine and threonine. Associated with cell proliferation, this protein is essential for chromosome alignment at the centromere during mitosis and is required for centrosome duplication. It has been found to be a critical mitotic checkpoint protein for accurate segregation of chromosomes during mitosis. …
- **Diseases (Open Targets)**: neurodegenerative disease (0.551); Alzheimer disease (0.380); Parkinson disease (0.375); lysosomal storage disease (0.375); ulna fracture (0.300)
- **Europe PMC papers**: 4437
- **Why important**: TTK is the most connected and strongest node in the module. It is a dual-specificity protein kinase required for chromosome alignment, centrosome duplication, and accurate chromosome segregation, and it is part of the globally significant (GO:BP meiotic cell cycle phase transition; q_global = 0.0356) signal and the supplementary STRING signal (STRING NetworkNeighborAL Mixed, incl. Mitotic Spindle Checkpoint, and Mitotic sister chromatid segregation; within-query FDR = 0.0147). Its STRING links to NDC80 and PBK are among the strongest relationships in the module. HPA places it in bone marrow, lymphoid tissue, and testis-associated contexts and in erythrocyte and megakaryocyte progenitors. Its substantial literature volume and disease associations make it the clearest anchor for interpretation.
- **Conclusion**: Established evidence supports TTK as a central spindle-checkpoint and chromosome-segregation component whose abundance is compatible with proliferating or progenitor cell states. It is plausible, but not established, that TTK coordinates the additional co-abundance links in this module.

#### NDC80

- **Related proteins** (co-abundance neighbors): HOMER3 (0.82), TTK (0.81); STRING partners: PBK (0.934), TTK (0.992)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NDC80 kinetochore complex component. This gene encodes a component of the NDC80 kinetochore complex. The encoded protein consists of an N-terminal microtubule binding domain and a C-terminal coiled-coiled domain that interacts with other components of the complex. This protein functions to organize and stabilize microtubule-kinetochore interactions and is required for proper chromosome segregation. [provided by RefSeq, Oct 2011].
- **Diseases (Open Targets)**: alcohol drinking (0.466); hemorrhage (0.344); gastric ulcer (0.344); heart conduction disease (0.344); bronchial disorder (0.324)
- **Europe PMC papers**: 3155
- **Why important**: NDC80 is a core kinetochore component with a high-strength STRING connection to TTK and an additional connection to PBK. It contributes directly to microtubule-kinetochore attachment and chromosome segregation and is one of the two genes in the globally significant (GO:BP meiotic cell cycle phase transition; q_global = 0.0356) term. HPA associates it with bone marrow and lymphoid tissue and with erythrocyte progenitors, trophoblasts, and spermatocyte populations. It also has extensive literature and multiple disease associations.
- **Conclusion**: Established evidence identifies NDC80 as a mechanistic core of chromosome segregation and supports the cell-division interpretation. Its participation in the brain and circulatory-system co-abundance pattern is more likely to indicate proliferating or progenitor cells than a mature neuronal function, although the supplied data do not identify the responsible cells.

#### PBK

- **Related proteins** (co-abundance neighbors): TTK (0.85); STRING partners: NDC80 (0.934), TTK (0.969)
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ binding kinase. This gene encodes a serine/threonine protein kinase related to the dual specific mitogen-activated protein kinase kinase (MAPKK) family. Evidence suggests that mitotic phosphorylation is required for its catalytic activity. The encoded protein may be involved in the activation of lymphoid cells and support testicular functions, with a suggested role in the process of spermatogenesis. Overexpressio…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.120); neoplasm (0.117); central nervous system cancer (0.116); breast carcinoma (0.115); cancer (0.115)
- **Europe PMC papers**: 4202
- **Why important**: PBK is part of the tightly connected STRING-supported NDC80–TTK core and is included in the supplementary spindle-checkpoint and sister-chromatid-segregation signal (STRING NetworkNeighborAL Mixed, incl. Mitotic Spindle Checkpoint, and Mitotic sister chromatid segregation; within-query FDR = 0.0147). It encodes a serine/threonine kinase associated with mitotic phosphorylation, lymphoid-cell activation, testicular function, and spermatogenesis. HPA shows lymphoid and testis-related enrichment but no detection in immune cells or brain. Its literature volume is substantial, and its disease associations include several cancers.
- **Conclusion**: Established evidence supports PBK as a cell-cycle-associated kinase linked to the NDC80–TTK core and to testis or lymphoid biology. Its absence from detected brain protein argues against interpreting it as a constitutive neuronal component; its role in this shared module may instead reflect a proliferative or cell-composition signal.

#### UBE2S

- **Related proteins** (co-abundance neighbors): DNAJC21 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin conjugating enzyme E2 S. This gene encodes a member of the ubiquitin-conjugating enzyme family. The encoded protein is able to form a thiol ester linkage with ubiquitin in a ubiquitin activating enzyme-dependent manner, a characteristic property of ubiquitin carrier proteins. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.444); hepatocellular carcinoma (0.115); neoplasm (0.102); Female infertility due to fertilization defect (0.092); ovarian carcinoma (0.091)
- **Europe PMC papers**: 2306
- **Why important**: UBE2S links the module to ubiquitin-dependent cell-cycle control, including protein polyubiquitination, exit from mitosis, and anaphase-promoting-complex-dependent catabolism. It contributes to the supplementary STRING term (STRING NetworkNeighborAL Mixed, incl. Mitotic Spindle Checkpoint, and Mitotic sister chromatid segregation; within-query FDR = 0.0147) and is connected in the co-abundance network to DNAJC21. HPA associates it with bone marrow and testis and with several specialized cell types. Its disease associations include neurodegenerative disease and neoplasia, and it has a substantial literature base.
- **Conclusion**: Established evidence supports UBE2S as a cell-cycle proteolysis component that complements the kinetochore and kinase signals. The DNAJC21 connection may indicate coordinated expression with nucleolar or ribosome-biogenesis activity, but that relationship is a module-level hypothesis rather than an established physical interaction.

#### DNAJC21

- **Related proteins** (co-abundance neighbors): TTK (0.86), UBE2S (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member C21. This gene encodes a member of the DNAJ heat shock protein 40 family of proteins that is characterized by two N-terminal tetratricopeptide repeat domains and a C-terminal DNAJ domain. This protein binds the precursor 45S ribosomal RNA and may be involved in early nuclear ribosomal RNA biogenesis and maturation of the 60S ribosomal subunit. Mutations in this gene result in Bone marrow failure syndro…
- **Diseases (Open Targets)**: autosomal dominant aplasia and myelodysplasia (0.773); neurodegenerative disease (0.502); inherited bone marrow failure syndrome (0.474); Bone marrow hypocellularity (0.463); Pancytopenia (0.462)
- **Europe PMC papers**: 417
- **Why important**: DNAJC21 has an intermediate network position through connections to TTK and UBE2S, despite lacking direct GO or STRING enrichment evidence in the supplied results. It is involved in precursor ribosomal RNA binding and early maturation of the large ribosomal subunit, and mutations are associated with bone marrow failure syndrome. HPA describes low tissue and cell-type specificity with brain protein detection. Its disease associations and bone-marrow relevance make it a potentially informative bridge between proliferation and biosynthetic capacity.
- **Conclusion**: Established evidence supports DNAJC21 in ribosome biogenesis and bone-marrow biology, but does not establish it as a spindle-checkpoint component. Its placement beside TTK and UBE2S suggests a hypothesis of coordinated growth or progenitor-state expression that requires independent validation.

## Module 1

**Tissue pair**: brain and circulatory_system  
**Genes (5)**: CPSF4, NUP37, RRP15, RSBN1L, ZMYM4

### Function

This is a small, hub-centered nuclear co-abundance module rather than a module with a demonstrated pathway-level function. ZMYM4 is the central network node and is co-abundant with NUP37, CPSF4, RSBN1L, and RRP15. The annotations collectively point toward nuclear gene-expression infrastructure: nucleocytoplasmic transport through NUP37, messenger RNA three-prime-end processing through CPSF4, nuclear or nuclear-speckle functions for ZMYM4 and RSBN1L, and ribosomal RNA processing through RRP15. No GO or KEGG term passed global correction, so no pathway or biological-process enrichment can be claimed as primary evidence. The module may therefore reflect coordinated expression of broadly used nuclear maintenance processes, but its precise biological function remains unresolved.

**Cell composition.** The module does not appear to be composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and all members have nucleoplasmic, nuclear-speckle, nucleolar, or related intracellular localizations. All members have low tissue specificity, and protein detection is reported throughout the sampled brain regions. The available HPA summary has no matching circulatory-system tissue, so it cannot establish protein detection there. Most members have low cell-type specificity and low immune-cell specificity. Some cell-type enhancement is reported in trophoblast populations, Sertoli cells, or neutrophils, but this does not support a dominant blood-cell composition. The shared brain and circulatory-system signal is therefore more consistent with broadly expressed cellular machinery, or with shared cellular composition, than with a secreted blood-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction among the module members meets the stated high-confidence threshold, and no STRING functional-enrichment result is available. No hu.MAP complex contains at least two module members. Thus, the observed co-abundance edges are not supported here by known high-confidence physical or functional interactions, and the module is not recognizable as a known hu.MAP complex. The network is nevertheless structured: ZMYM4 connects to every other member, while NUP37, CPSF4, RSBN1L, and RRP15 are peripheral single-neighbor nodes. This topology supports a possible common regulatory or cellular-state signal, but it does not establish direct molecular binding among the proteins.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact shared co-abundance module may represent a previously unreported association, because its internal relationships are absent from the supplied high-confidence STRING and hu.MAP evidence. However, this is not sufficient to call it a new biological mechanism. The genes themselves have established functions, substantial literature for several members, and broad nuclear roles that could produce correlated expression without a novel physical complex. The lack of globally significant GO or KEGG enrichment also limits claims of a newly defined pathway. A cautious conclusion is that the cross-tissue co-abundance pattern is a candidate novel observation, while biological novelty remains unproven and requires independent cohorts, replication, cell-composition adjustment, and experimental testing.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of a general nuclear gene-expression state in which ZMYM4-associated regulation is coupled with nuclear transport, messenger RNA three-prime-end processing, nuclear-speckle activity, and ribosomal RNA maturation. Such coordination could arise from a shared transcriptional program or cellular-state effect in brain and circulatory-system samples, rather than from a stable protein complex. This hypothesis is consistent with the topology and intracellular annotations, but it is not demonstrated by the available enrichment, STRING, or hu.MAP evidence.

### Important genes

#### ZMYM4

- **Related proteins** (co-abundance neighbors): NUP37 (0.86), CPSF4 (0.83), RSBN1L (0.82), RRP15 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger MYM-type containing 4. Predicted to enable DNA binding activity. Involved in cytoskeleton organization and regulation of cell morphogenesis. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.456); post-traumatic stress disorder (0.264); Abnormal pupillary function (0.171); Proptosis (0.120); homozygous familial hypercholesterolemia (0.059)
- **Europe PMC papers**: 200
- **Why important**: ZMYM4 is the network hub, connecting all other module members, and is annotated as a zinc-finger MYM-type protein with predicted DNA-binding activity. Its reported roles include cytoskeleton organization and regulation of cell morphogenesis. It is detected in brain, has low tissue and cell-type specificity, and has the largest literature representation among the module members in the supplied evidence. Open Targets links it to neurodegenerative disease and other disorders.
- **Conclusion**: Established: ZMYM4 is the principal network-centered candidate and has predicted nuclear regulatory capacity. Hypothesis: it may coordinate the shared expression of the other genes, but the co-abundance data do not prove that it regulates them directly.

#### NUP37

- **Related proteins** (co-abundance neighbors): ZMYM4 (0.86); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 37. Nuclear pore complexes (NPCs) are used for transporting macromolecules between the cytoplasm and the nucleus. NPCs consist of multiple copies of 30 distinct proteins (nucleoporins), which assemble into biochemically-separable subcomplexes. The protein encoded by this gene is part of a subcomplex (Nup107-160) that is required for proper NPC function as well as for normal kinetochore-microtubule int…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); microcephaly 24, primary, autosomal recessive (0.492); neurodegenerative disease (0.463)
- **Europe PMC papers**: 481
- **Why important**: NUP37 is the module member most directly connected to nuclear pore biology. It is a component of the Nup107-160 nuclear pore subcomplex, which supports nucleocytoplasmic transport and kinetochore-microtubule interaction during mitosis. It is the sole partner of ZMYM4 in the module topology and has substantial literature representation. Its disease associations include microcephaly and neurodegenerative disease.
- **Conclusion**: Established: NUP37 contributes to nuclear pore-complex function and nucleocytoplasmic transport. Hypothesis: its co-abundance with ZMYM4 may indicate coordinated control of nuclear organization or transport, not necessarily direct binding.

#### CPSF4

- **Related proteins** (co-abundance neighbors): ZMYM4 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 4. Inhibition of the nuclear export of poly(A)-containing mRNAs caused by the influenza A virus NS1 protein requires its effector domain. The NS1 effector domain functionally interacts with the cellular 30 kDa subunit of cleavage and polyadenylation specific factor 4, an essential component of the 3' end processing machinery of cellular pre-mRNAs. In influenza virus-infected cells, the NS1 protein is…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.377); dengue disease (0.370); neurodegenerative disease (0.227); placental abruption (0.124); Abnormality of the skeletal system (0.102)
- **Europe PMC papers**: 486
- **Why important**: CPSF4 connects to the hub and represents messenger RNA maturation. It is an essential component of the cleavage and polyadenylation machinery for pre-messenger RNA three-prime-end processing. The supplied evidence also describes its physical and functional interaction with influenza A virus NS1, and it has substantial literature representation and disease associations involving viral infection and neurodegenerative disease.
- **Conclusion**: Established: CPSF4 participates in messenger RNA three-prime-end processing. Hypothesis: its association with ZMYM4 could reflect coordinated regulation of transcriptional output and RNA maturation in the shared tissue signal.

#### RRP15

- **Related proteins** (co-abundance neighbors): ZMYM4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal RNA processing 15 homolog. This gene encodes a protein that co-purifies with human nucleoli. A similar protein in budding yeast is a component of pre-60S ribosomal particles, and is required for the early maturation steps of the 60S subunit. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: Alzheimer disease (0.483); Parkinson disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462); diaphragmatic hernia (0.282)
- **Europe PMC papers**: 239
- **Why important**: RRP15 is connected to the hub and supplies a distinct nucleolar function. It co-purifies with human nucleoli and is associated with early maturation of the large ribosomal subunit, including ribosomal RNA processing. It is detected in brain and has disease associations involving Alzheimer disease, Parkinson disease, neurodegenerative disease, and lysosomal storage disease.
- **Conclusion**: Established: RRP15 is involved in ribosomal RNA processing and large-subunit maturation. Hypothesis: its co-abundance with the RNA-processing and nuclear-organization genes may mark a broader cellular demand for coordinated gene expression and ribosome production.

#### RSBN1L

- **Related proteins** (co-abundance neighbors): ZMYM4 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Immune cell enhanced; location Nuclear speckles; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: round spermatid basic protein 1 like. Predicted to enable dioxygenase activity and metal ion binding activity. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hypertensive disorder (0.272); hypothyroidism (0.269); myopathy (0.264); neurodegenerative disease (0.255); obesity disorder (0.241)
- **Europe PMC papers**: 113
- **Why important**: RSBN1L is a peripheral member linked only to ZMYM4, but it adds a potentially distinctive nuclear component. It is predicted to have dioxygenase and metal-ion-binding activities and is localized to nuclear speckles. HPA reports immune-cell enhancement in neutrophils, while the overall tissue and cell-type specificity is low. Its reported disease associations include hypertensive disorder, myopathy, obesity disorder, and neurodegenerative disease.
- **Conclusion**: Established: RSBN1L is a nuclear-speckle protein with predicted enzymatic and metal-binding functions, but the supplied evidence does not establish its precise biological role. Hypothesis: it may connect the hub-centered module to RNA-processing or nuclear-speckle state, although this remains especially tentative.

## Module 2

**Tissue pair**: brain and circulatory_system  
**Genes (6)**: DHX9, EIF3C, HNRNPR, RPL12, RPL3, RPL6

### Function

This is a conserved RNA and protein-synthesis module centered on cytoplasmic translation and the large ribosomal subunit. The strongest primary evidence is the enrichment of cytoplasmic translation (GO:BP cytoplasmic translation; q_global = 2.5e-05), cytosolic large ribosomal subunit (GO:CC cytosolic large ribosomal subunit; q_global = 0.000137), ribonucleoprotein complex (GO:CC ribonucleoprotein complex; q_global = 0.000171), cytosolic ribosome (GO:CC cytosolic ribosome; q_global = 0.0065), translation and protein biosynthetic process (GO:BP translation; q_global = 0.00782) (GO:BP protein biosynthetic process; q_global = 0.00782), structural constituent of ribosome (GO:MF structural constituent of ribosome; q_global = 0.00816), and the human ribosome pathway (KEGG Ribosome - Homo sapiens (human); q_global = 0.0132). All module genes are annotated with RNA binding (GO:MF RNA binding; q_global = 0.0314). The network therefore most plausibly represents coordinated abundance of ribosome-associated and RNA-processing machinery rather than a specialized brain or circulatory signaling pathway. The ribosomal genes form a tightly connected core, while EIF3C, DHX9, and HNRNPR extend the module toward translation initiation, RNA helicase activity, RNA processing, and ribonucleoprotein organization.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes, and every gene has low immune-cell specificity. It also does not show a clear blood-cell-enriched signature. Instead, all genes have low tissue specificity, consistent with broadly expressed intracellular housekeeping or core gene-expression machinery. HPA detects the proteins in the surveyed brain regions, whereas there is no matching HPA tissue for the circulatory-system category. Several genes show cell-type enhancement in particular stromal, epithelial, glial, or neuronal populations, but the pattern is heterogeneous rather than evidence for one shared specialized cell type. Consequently, the cross-tissue module may primarily reflect general translational capacity, cellular composition, or sample-level RNA and protein abundance rather than a brain–circulatory-system-specific biological program.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cytoplasmic translation | 2.5e-05 | DHX9, EIF3C, RPL12, RPL3, RPL6 |
| GO:CC cytosolic large ribosomal subunit | 0.000137 | RPL12, RPL3, RPL6 |
| GO:CC ribonucleoprotein complex | 0.000171 | DHX9, EIF3C, HNRNPR, RPL12, RPL3, RPL6 |
| GO:CC large ribosomal subunit | 0.00325 | RPL12, RPL3, RPL6 |
| GO:CC cytosolic ribosome | 0.0065 | RPL12, RPL3, RPL6 |
| GO:BP translation | 0.00782 | DHX9, EIF3C, RPL12, RPL3, RPL6 |
| GO:BP protein biosynthetic process | 0.00782 | DHX9, EIF3C, RPL12, RPL3, RPL6 |
| GO:MF structural constituent of ribosome | 0.00816 | RPL12, RPL3, RPL6 |
| KEGG Ribosome - Homo sapiens (human) | 0.0132 | RPL12, RPL3, RPL6 |
| GO:CC ribosomal subunit | 0.0144 | RPL12, RPL3, RPL6 |
| GO:MF RNA binding | 0.0314 | DHX9, EIF3C, HNRNPR, RPL12, RPL3, RPL6 |

### STRING and hu.MAP

STRING supports a coherent but incomplete interaction structure. The strongest documented relationships connect RPL3, RPL12, and RPL6 into a large-ribosomal-subunit core. STRING also links DHX9 with HNRNPR and DHX9 with RPL6, supporting an RNA-processing and ribonucleoprotein bridge to the ribosomal core. The supplementary STRING annotations are consistent with free small-subunit formation, subunit joining, peptide-chain elongation, cytoplasmic translation, and other translation-related processes (4 supplementary STRING terms; within-query FDR 2.43e-06–6.6e-05). These are supplementary contextual evidence, not globally corrected enrichment claims. No hu.MAP complex contains at least two module members. Thus, known interactions explain much of the module, especially the ribosomal core, but the complete six-gene co-abundance pattern is not represented as a validated hu.MAP complex.

**STRING interactions (score >= 0.7)**: 5 of 15 gene pairs: DHX9–HNRNPR (0.909); DHX9–RPL6 (0.958); RPL12–RPL3 (0.999); RPL12–RPL6 (0.999); RPL3–RPL6 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Formation of a pool of free 40S subunits (FDR = 2.43e-06, 4 genes); RCTM L13a-mediated translational silencing of Ceruloplasmin expression (FDR = 2.88e-06, 4 genes); RCTM GTP hydrolysis and joining of the 60S ribosomal subunit (FDR = 2.88e-06, 4 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 1.66e-05, 6 genes); COMPARTMENTS Cytosolic large ribosomal subunit (FDR = 2.54e-05, 3 genes); Component Ribonucleoprotein complex (FDR = 4.37e-05, 6 genes); RCTM Peptide chain elongation (FDR = 6.5e-05, 3 genes); Process Cytoplasmic translation (FDR = 6.6e-05, 4 genes); COMPARTMENTS Ribosome (FDR = 6.98e-05, 4 genes); RCTM Viral mRNA Translation (FDR = 7.66e-05, 3 genes); RCTM Selenocysteine synthesis (FDR = 7.66e-05, 3 genes); RCTM Eukaryotic Translation Termination (FDR = 7.66e-05, 3 genes); RCTM Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC) (FDR = 8.44e-05, 3 genes); Component Cytosolic large ribosomal subunit (FDR = 9.53e-05, 3 genes); RCTM Response of EIF2AK4 (GCN2) to amino acid deficiency (FDR = 9.84e-05, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be described as a newly discovered translation pathway. Its central biology is well established: the ribosomal genes have very strong known STRING relationships, and the primary GO/KEGG results recover canonical ribosome and translation annotations (10 globally significant GO/KEGG terms, q_global 2.5e-05–0.0144; see the table). The absence of a hu.MAP complex does not prove novelty, and absence from a particular interaction resource would not by itself establish a new biological mechanism. A potentially new observation may be the coordinated abundance of this specific combination across brain and circulatory-system samples, especially the association of the ribosomal core with DHX9, EIF3C, and HNRNPR, but that claim requires replication in independent cohorts and comparison with other tissue-pair modules. The present evidence supports a reproducible module-level pattern, not a novel molecular function.

**Hypothesis.** Hypothesis: the shared module reflects coordinated control of cellular protein-production capacity across brain and circulatory-system samples. The RPL3–RPL12–RPL6 core may represent large-subunit availability, EIF3C may connect that core to translation initiation, and DHX9 with HNRNPR may connect translation to RNA remodeling, pre-mRNA processing, transport, or RNA quality control. Variation in the abundance of this integrated RNA–ribosome system could therefore generate the conserved co-abundance signal across tissues. This remains a hypothesis because co-abundance does not demonstrate physical assembly, causal regulation, or tissue-specific function.

### Important genes

#### RPL3

- **Related proteins** (co-abundance neighbors): EIF3C (0.85), RPL12 (0.85), RPL6 (0.85), DHX9 (0.81); STRING partners: RPL12 (0.999), RPL6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L3. Ribosomes, the complexes that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L3P family of ribosomal proteins and it is located in the cytoplasm. The p…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.506); Orthomyxoviridae infectious disease (0.463); cystic fibrosis (0.389); neuromuscular disease caused by qualitative or quantitative defects of dystrophin (0.323); inflammatory bowel disease (0.308)
- **Europe PMC papers**: 2316
- **Why important**: RPL3 is the most central module member by network position, linking EIF3C, RPL12, RPL6, and DHX9. It is a component of the cytoplasmic large ribosomal subunit and appears in every primary GO/KEGG term (11 globally significant GO/KEGG terms, q_global 2.5e-05–0.0314; see the table) and every listed STRING annotation (15 supplementary STRING terms; within-query FDR 2.43e-06–9.84e-05). Its extensive literature record and disease associations make it the strongest marker of the module's canonical ribosomal biology.
- **Conclusion**: Established evidence supports RPL3 as a core large-subunit ribosomal component and a principal structural anchor of the module. Its centrality makes it important for interpreting the module, but the available evidence does not show that RPL3 specifically drives the cross-tissue co-abundance pattern.

#### RPL12

- **Related proteins** (co-abundance neighbors): RPL3 (0.85), HNRNPR (0.80); STRING partners: RPL3 (0.999), RPL6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal protein L12. Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L11P family of ribosomal proteins. It is located in the cytoplasm. The pr…
- **Diseases (Open Targets)**: Duchenne muscular dystrophy (0.503); Orthomyxoviridae infectious disease (0.462); neurodegenerative disease (0.460); cystic fibrosis (0.390); neuromuscular disease caused by qualitative or quantitative defects of dystrophin (0.323)
- **Europe PMC papers**: 1865
- **Why important**: RPL12 is part of the tightly connected ribosomal core with RPL3 and RPL6 and is included in all primary enrichment terms (11 globally significant GO/KEGG terms, q_global 2.5e-05–0.0314; see the table). It binds ribosomal RNA and is represented across the STRING translation annotations (15 supplementary STRING terms; within-query FDR 2.43e-06–9.84e-05). Its substantial literature and reported associations with neuromuscular and neurodegenerative disease make it relevant to a module shared with brain samples.
- **Conclusion**: Established evidence identifies RPL12 as a large-subunit ribosomal protein and a strong indicator of coordinated translation machinery. Its disease associations provide biological relevance, but they do not establish that this module is pathogenic or specifically linked to those disorders.

#### EIF3C

- **Related proteins** (co-abundance neighbors): RPL3 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 3 subunit C. Enables ribosome binding activity. Contributes to translation initiation factor activity. Involved in positive regulation of mRNA binding activity; positive regulation of translation; and translational initiation. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neoplasm (0.103); hepatocellular carcinoma (0.093); ovarian carcinoma (0.082); ovarian cancer (0.082); scalp defects-postaxial polydactyly syndrome (0.082)
- **Europe PMC papers**: 1168
- **Why important**: EIF3C is the module's direct translation-initiation component and connects to the ribosomal core through RPL3. It contributes to translation-initiation-factor activity, ribosome binding, and positive regulation of translation, and it appears in the primary translation and RNA-binding evidence (5 globally significant GO/KEGG terms, q_global 2.5e-05–0.0314; see the table). Its STRING links to translation-initiation and ribosome-joining processes (STRING RCTM Formation of a pool of free 40S subunits; within-query FDR = 2.43e-06) (STRING RCTM GTP hydrolysis and joining of the 60S ribosomal subunit; within-query FDR = 2.88e-06) (STRING Process Cytoplasmic translation; within-query FDR = 6.6e-05) provide mechanistic context despite the absence of a separately listed STRING partner in the gene-level summary.
- **Conclusion**: Established evidence supports EIF3C as a functional bridge between ribosome abundance and initiation of protein synthesis. Its position suggests a plausible role in module coordination, but the co-abundance data do not establish direct regulation of the ribosomal genes by EIF3C.

#### DHX9

- **Related proteins** (co-abundance neighbors): RPL3 (0.81); STRING partners: HNRNPR (0.909), RPL6 (0.958)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 connects the module's translational core to RNA metabolism. It is an ATP-dependent RNA and DNA–RNA helicase with nuclear and cytoplasmic functions, appears in the primary translation, ribonucleoprotein, protein-biosynthetic, and RNA-binding terms (5 globally significant GO/KEGG terms, q_global 2.5e-05–0.0314; see the table), and has documented STRING relationships with HNRNPR and RPL6. It has the largest literature record among the module genes and disease associations involving neurodevelopmental and neurodegenerative conditions.
- **Conclusion**: Established evidence supports DHX9 as an RNA-remodeling and RNA-regulatory component associated with the ribonucleoprotein and translation signals. Its placement suggests a hypothesis of coordination between RNA handling and translation, but it does not prove that DHX9 mediates the tissue-pair conservation.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): RPL12 (0.80); STRING partners: DHX9 (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is an RNA-binding heterogeneous nuclear ribonucleoprotein involved in spliceosome-associated pre-mRNA processing and transport. It is linked in the module to RPL12 and in STRING to DHX9, and it contributes to the globally significant ribonucleoprotein and RNA-binding terms (GO:CC ribonucleoprotein complex; q_global = 0.000171) (GO:MF RNA binding; q_global = 0.0314). Its disease associations include neurodevelopmental and intellectual-disability phenotypes, making it relevant to the brain component despite its peripheral network position.
- **Conclusion**: Established evidence supports HNRNPR as an RNA-processing component that extends the module beyond structural ribosomal proteins. Its inclusion is compatible with coordinated RNA maturation and translation, but the current data cannot distinguish a mechanistic connection from correlated abundance of broadly expressed cellular machinery.

## Module 3

**Tissue pair**: brain and circulatory_system  
**Genes (7)**: TMEM68, DOCK7, DYSF, ELP1, EXD2, PARP4, PDZD8

### Function

 The co-abundance structure is hub-and-spoke-like, centered on TMEM68, with a smaller DOCK7–DYSF branch and single links from TMEM68 to EXD2, ELP1, PARP4, and PDZD8. No GO or KEGG term passed global correction, so there is no statistically supported pathway assignment from enrichment. The individual annotations suggest several biological themes rather than one established pathway: membrane lipid handling through TMEM68 and PDZD8, neuronal polarization and small-GTPase signaling through DOCK7, membrane repair and calcium-dependent fusion through DYSF, nucleic-acid damage and RNA-related processes through EXD2 and ELP1, and DNA-damage or inflammatory responses through PARP4. These annotations support a possible interface between membrane organization, cellular stress responses, and neural or immune-cell biology, but the module itself does not establish that these processes form one biochemical pathway.

**Cell composition.**  The module is not dominated by plasma or secreted proteins: none of the members is annotated as secreted. Most members have low tissue specificity, while the tissue-enhanced signal includes bone marrow and skeletal muscle. Cell-type annotations are much more prominent than tissue-level specificity, with recurring neutrophil and neutrophil-progenitor signals and additional annotations involving myeloid dendritic cells, basophils, astrocytes, ciliated cells, and progenitor populations. This composition argues against interpreting the module as a brain-specific neuronal program. It may partly reflect shared blood or immune-cell content, or a cell-composition effect in the sampled tissues. Brain protein detection is broadly compatible with the genes being present in brain, but there is no matching HPA circulatory-system tissue assessment, so the cross-tissue interpretation should remain cautious.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

 No reported high-confidence STRING interaction connects any pair of module members, and STRING functional enrichment is absent. No hu.MAP complex contains multiple members of the module. Thus, the co-abundance relationships are not supported here as a known physical interaction network or a recognized protein complex. This does not disprove biological coordination: co-abundance can arise from shared cellular composition, transcriptional regulation, membrane or organelle state, or indirect physiology. It does mean that the module should not be described as a validated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module-level observation may be a new co-abundance association because the reported relationships are absent from the high-confidence STRING set and no multi-member hu.MAP complex is present. However, those absences do not prove novelty: the individual genes and their functions are already well represented in biological literature, and several pairwise co-abundance links could reflect indirect regulation or cell composition. The defensible conclusion is therefore that this is a potentially novel cross-tissue expression pattern, not a newly discovered protein complex or mechanism. Independent cohorts, cell-composition adjustment, and targeted pairwise validation would be needed to establish novelty.

**Hypothesis.** Hypothesis: the shared brain–circulatory-system module reflects a conserved cell-state or cell-mixture program organized around membrane and lipid homeostasis, with contributions from neural-support cells and myeloid or progenitor populations. TMEM68 may mark the central membrane-associated co-abundance state; PDZD8 could connect that state to organelle contact sites and calcium or lipid handling; DOCK7 and DYSF could represent cytoskeletal, membrane-remodeling, or repair components; and EXD2, ELP1, and PARP4 could reflect accompanying nucleic-acid, translation, DNA-damage, or inflammatory stress. This is a testable interpretation rather than an established pathway, particularly because enrichment, STRING, and complex evidence are all negative.

### Important genes

#### TMEM68

- **Related proteins** (co-abundance neighbors): EXD2 (0.86), DOCK7 (0.83), ELP1 (0.82), PARP4 (0.82), PDZD8 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transmembrane protein 68. Predicted to enable acyltransferase activity. Predicted to be integral component of membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.416); placenta praevia (0.271); spondylolisthesis (0.229); shortness of breath (0.207); thyroid cancer (0.185)
- **Europe PMC papers**: 235
- **Why important**:  TMEM68 is the central hub, connected to EXD2, DOCK7, ELP1, PARP4, and PDZD8. It is predicted to be an integral membrane acyltransferase and is linked to triglyceride biosynthesis; its vesicular localization is compatible with a membrane or lipid homeostasis role. It has broad tissue specificity and brain protein detection, while its cell-type annotation points to ciliated cells. Its literature volume is comparatively limited relative to several other members, making the hub relationship especially important to test.
- **Conclusion**: Established evidence supports TMEM68 as the network-centered membrane-associated gene with a plausible lipid-related function. Hypothesis: it is a marker or organizer of the shared module state. The data do not establish that it physically binds the neighboring proteins or causally controls their abundance.

#### DOCK7

- **Related proteins** (co-abundance neighbors): DYSF (0.90), TMEM68 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dedicator of cytokinesis 7. The protein encoded by this gene is a guanine nucleotide exchange factor (GEF) that plays a role in axon formation and neuronal polarization. The encoded protein displays GEF activity toward RAC1 and RAC3 Rho small GTPases but not toward CDC42. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2012].
- **Diseases (Open Targets)**: genetic developmental and epileptic encephalopathy (0.766); familial hypobetalipoproteinemia 2 (0.533); hereditary disease (0.488); metabolic syndrome (0.373); infantile epileptic encephalopathy (0.372)
- **Europe PMC papers**: 822
- **Why important**:  DOCK7 links the TMEM68 hub to DYSF, forming the only multi-step branch in the module. It is a RAC-directed guanine-nucleotide exchange factor involved in axon formation, neuronal polarization, cytoskeletal organization, and small-GTPase signaling. HPA annotations include astrocytes and myeloid dendritic cells, fitting the brain and immune-cell mixture suggested by the module. It also has a substantial literature and disease links to developmental and epileptic encephalopathy.
- **Conclusion**: Established evidence supports DOCK7 as a neural cytoskeletal and RAC-signaling gene with an informative bridge position. Hypothesis: it may connect membrane remodeling to neural or immune-cell state in this module. The co-abundance data do not show that its GEF activity is altered.

#### DYSF

- **Related proteins** (co-abundance neighbors): DOCK7 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Plasma membrane, Centriolar satellite, Mid piece; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dysferlin. The protein encoded by this gene belongs to the ferlin family and is a skeletal muscle protein found associated with the sarcolemma. It is involved in muscle contraction and contains C2 domains that play a role in calcium-mediated membrane fusion events, suggesting that it may be involved in membrane regeneration and repair. In addition, the protein encoded by this gene binds caveolin-3, a skeleta…
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type 2B (0.838); Miyoshi muscular dystrophy 1 (0.826); distal myopathy with anterior tibial onset (0.770); autosomal recessive limb-girdle muscular dystrophy (0.722); Miyoshi myopathy (0.638)
- **Europe PMC papers**: 2135
- **Why important**:  DYSF is the terminal member of the DOCK7 branch. Dysferlin is a membrane-repair and calcium-dependent membrane-fusion protein associated with skeletal muscle, and its annotations also include immune activation and regulation of phagocytosis. HPA evidence highlights bone marrow, skeletal muscle, and neutrophils. DYSF has strong disease relevance for muscular dystrophies and the largest literature volume among the selected genes.
- **Conclusion**: Established evidence supports DYSF as a membrane-repair protein with muscle and immune-cell relevance. Hypothesis: its association with DOCK7 may represent coordinated membrane or cytoskeletal remodeling, or may instead reflect shared cell composition. No physical interaction is established by the reported STRING or hu.MAP results.

#### ELP1

- **Related proteins** (co-abundance neighbors): TMEM68 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongator acetyltransferase complex subunit 1. The protein encoded by this gene is a scaffold protein and a regulator for three different kinases involved in proinflammatory signaling. The encoded protein can bind NF-kappa-B-inducing kinase and I-kappa-B kinases through separate domains and assemble them into an active kinase complex. Mutations in this gene have been associated with familial dysautonomia. Alternative splicing results in multip…
- **Diseases (Open Targets)**: Riley-Day syndrome (0.807); medulloblastoma (0.721); primary dysautonomia (0.407); hereditary sensory and autonomic neuropathy (0.374); mathematical ability (0.361)
- **Europe PMC papers**: 960
- **Why important**:  ELP1 is directly connected to the central TMEM68 hub. It is a scaffold for signaling kinases involved in proinflammatory signaling and is also part of the elongator-related tRNA modification and translation machinery. HPA annotations include basophils, and the gene has substantial literature and a strong association with familial dysautonomia.
- **Conclusion**: Established evidence supports ELP1 as a multifunctional gene linking translation-related biology with inflammatory signaling and autonomic disease. Hypothesis: it could couple the module's membrane-associated state to translational or inflammatory cell state. The module does not determine which ELP1 function is relevant.

#### PDZD8

- **Related proteins** (co-abundance neighbors): TMEM68 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in brain
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ domain containing 8. Predicted to enable lipid binding activity and metal ion binding activity. Involved in several processes, including mitochondrial calcium ion homeostasis; mitochondrion-endoplasmic reticulum membrane tethering; and regulation of cell morphogenesis. Located in endoplasmic reticulum membrane and mitochondria-associated endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Apr 20…
- **Diseases (Open Targets)**: intellectual developmental disorder with autism and dysmorphic facies (0.577); Global developmental delay (0.372); Intellectual disability (0.371); Hypertelorism (0.370); Abnormality of the face (0.370)
- **Europe PMC papers**: 424
- **Why important**:  PDZD8 is directly connected to TMEM68. It is associated with lipid binding, mitochondria–endoplasmic-reticulum membrane tethering, mitochondrial calcium homeostasis, lipophagy, and neuron projection development. HPA evidence emphasizes bone marrow and several hematopoietic progenitor populations, while disease associations include developmental and intellectual disorders. Its literature volume is moderate, and its organelle localization gives it a mechanistically distinctive position.
- **Conclusion**: Established evidence supports PDZD8 as an organelle-contact, lipid, and calcium-homeostasis gene with neural and progenitor relevance. Hypothesis: PDZD8 may connect TMEM68-associated membrane biology to mitochondrial or endoplasmic-reticulum state. The co-abundance pattern alone cannot establish organelle tethering activity in these tissues.
