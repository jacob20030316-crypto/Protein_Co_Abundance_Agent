# Conserved co-abundance modules: bone_marrow and stem_cells

## Module 0

**Tissue pair**: bone_marrow and stem_cells  
**Genes (32)**: ABR, ACTR5, C1GALT1, MLYCD, EMC10, FASTKD5, GMIP, GSTCD, H1-0, HAUS7, PHKA2, RPS6KA3, LCLAT1, ALDH18A1, PARP4, PBXIP1, PDXP, PSMB8, PTBP3, GM2A, CARS2, SYNPO, GTF2A1, TSPO, UBE2D1, UBE2E2, UBAC2, VIL1, VRK2, WDR36, ZC3H6, ZNF106

### Function

No GO or KEGG term passed global correction, and there was no supplementary STRING enrichment. The module therefore does not support a statistically established pathway-level functional assignment. Its genes nevertheless span several cellular processes: ubiquitin and ISG15 conjugation through UBE2D1 and UBE2E2, RNA and transcriptional regulation through ZNF106, PTBP3, ZC3H6 and GTF2A1, cytoskeletal and small-GTPase regulation through GMIP and ABR, mitochondrial and metabolic functions through PHKA2, ALDH18A1, LCLAT1 and MLYCD, and protein quality control through PSMB8 and PARP4. The network is consequently best interpreted as a heterogeneous co-abundance program rather than evidence for one defined biochemical pathway. Established evidence supports cellular maintenance, protein modification, gene-expression control, metabolism and differentiation-related functions; a single integrated function remains a hypothesis.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary identifies only a small secreted component, with GM2A described as intracellular and membrane-associated and EMC10 as secreted to blood. It is also not uniformly blood-cell specific. Most genes have low tissue specificity, while many show cell-type enhancement, particularly in neutrophils and neutrophil progenitors, with additional representation of myonuclei, microglia and epithelial populations. Several genes are enhanced in bone marrow or lymphoid tissue, including GMIP and H1-0, and most proteins are detected in bone marrow. This pattern is consistent with a shared hematopoietic or progenitor-cell component in the samples, potentially mixed with broadly expressed cellular maintenance programs, rather than a module restricted to a single lineage. VIL1, EMC10 and other tissue-biased genes also indicate that co-abundance may partly reflect cellular composition or shared state rather than a common pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no STRING functional enrichment. Thus, STRING provides no established physical interaction network connecting the module. hu.MAP supplies limited complex-level support: UBE2D1 and UBE2E2 co-occur in complexes C1, C2 and C3, each of which also contains other ubiquitin-system proteins outside the module. This supports a plausible ubiquitin-conjugation component centered on these two genes, but only a minority of each complex is represented. The absence of STRING links and the sparse hu.MAP overlap argue against treating the whole module as a known protein complex. The co-abundance relationships may instead reflect shared cell state, transcriptional regulation, protein turnover, or indirect cellular composition effects.

**STRING interactions (score >= 0.7)**: 0 of 496 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08883.1 (UBE2D1, UBE2E2; 2/7); huMAP3_09089.1 (UBE2D1, UBE2E2; 2/8); huMAP3_09037.1 (UBE2D1, UBE2E2; 2/9)

### Novelty

This module may be a new co-abundance observation, but the available evidence does not establish a new biological mechanism. Its novelty is supported only in the limited sense that the complete module is not represented as a connected STRING network or as a single hu.MAP complex. That absence alone cannot prove novelty, because co-abundance can capture indirect regulation, cell-type mixtures, transient interactions, or relationships not represented in those resources. The presence of established ubiquitin-conjugating complexes involving UBE2D1 and UBE2E2, together with well-characterized functions distributed across other genes, suggests that the strongest claim is a potentially novel combination or expression program rather than discovery of a new pathway.

**Hypothesis.** Hypothesis: the module reflects a shared hematopoietic or progenitor-cell state involving coordinated protein quality control, ubiquitin-dependent regulation, RNA and transcriptional control, cytoskeletal remodeling, and metabolic adaptation. UBE2D1 and UBE2E2 could provide a protein-conjugation axis, while ZNF106, PTBP3 and related nuclear regulators could coordinate gene-expression or RNA-processing states. GMIP and ABR could connect this state to Rho-family signaling and cell morphology, and PHKA2, ALDH18A1 or LCLAT1 could reflect energetic and membrane-lipid adaptation. The neutrophil and progenitor enrichment in HPA makes shared cellular composition a competing explanation. Testing this hypothesis would require cell-resolved expression, independent cohorts and perturbation or biochemical validation; the present module alone does not distinguish mechanism from co-occurring cell states.

### Important genes

#### ZNF106

- **Related proteins** (co-abundance neighbors): LCLAT1 (0.94), CARS2 (0.92), PARP4 (0.90), GMIP (0.88), ABR (0.88), TSPO (0.86), PTBP3 (0.85), UBE2E2 (0.82), MLYCD (0.82); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Immune cell enhanced; location Nucleoli; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger protein 106. Enables RNA binding activity. Predicted to be involved in insulin receptor signaling pathway. Predicted to be located in nuclear speck and nucleolus. Predicted to be active in cytosol and membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: urethritis (0.352); hyperaldosteronism (0.191); benign neoplasm of eye (0.179); preeclampsia (0.179); Complete right bundle branch block (0.178)
- **Europe PMC papers**: 130
- **Why important**: ZNF106 has the strongest network position in the module and connects genes spanning lipid remodeling, mitochondrial function, signaling, RNA regulation and ubiquitin conjugation. It is enriched in muscle-related tissues and enhanced in neutrophils, while its annotation supports RNA binding and nuclear-speck or nucleolar localization. It therefore provides a plausible network-level integrator, although its direct molecular role in this module is not established.
- **Conclusion**: Established evidence: ZNF106 is a highly connected module member with RNA-binding annotation and neutrophil enhancement. Hypothesis: it may coordinate the heterogeneous nuclear and metabolic program represented by the module. Its centrality supports prioritization, not proof that it regulates the other genes.

#### UBE2E2

- **Related proteins** (co-abundance neighbors): VIL1 (1.00), GSTCD (0.91), ZNF106 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_08883.1, huMAP3_09089.1, huMAP3_09037.1
- **Function (MyGene.info)**: ubiquitin conjugating enzyme E2 E2. Enables ISG15 transferase activity and ubiquitin conjugating enzyme activity. Involved in protein modification by small protein conjugation. Acts upstream of or within cellular response to DNA damage stimulus and positive regulation of G1/S transition of mitotic cell cycle. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.589); diabetes mellitus (0.573); Abnormality of the skeletal system (0.510); hypothyroidism (0.470); diabetic eye disease (0.433)
- **Europe PMC papers**: 1699
- **Why important**: UBE2E2 is one of the module's clearest mechanistic anchors. It is a ubiquitin-conjugating enzyme with annotated ubiquitin and ISG15 conjugation functions, DNA-damage response involvement and cell-cycle associations. It also participates with UBE2D1 in all of the hu.MAP complexes detected for this module and is enhanced across several myeloid and lymphoid cell types.
- **Conclusion**: Established evidence: UBE2E2 has a defined protein-conjugation function, broad immune-cell associations and repeated hu.MAP complex support with UBE2D1. Hypothesis: its co-abundance may indicate regulated protein turnover or stress-response activity in shared hematopoietic cells. The data do not identify its substrates or demonstrate that it drives the module.

#### UBE2D1

- **Related proteins** (co-abundance neighbors): PHKA2 (1.00), C1GALT1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_08883.1, huMAP3_09089.1, huMAP3_09037.1
- **Function (MyGene.info)**: ubiquitin conjugating enzyme E2 D1. The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. This enz…
- **Diseases (Open Targets)**: digestive system disorder (0.215); gastrointestinal disease (0.215); biliary tract disorder (0.142); secondary malignant neoplasm (0.103); hepatocellular carcinoma (0.094)
- **Europe PMC papers**: 993
- **Why important**: UBE2D1 is a ubiquitin-conjugating enzyme and the second member of the repeated hu.MAP overlap. It connects to PHKA2 and C1GALT1 in the co-abundance graph and is enhanced in neutrophils and neutrophil progenitors. Its annotation includes protein ubiquitination, protein catabolism and regulation of BMP signaling.
- **Conclusion**: Established evidence: UBE2D1 has a recognized ubiquitination role and is supported by three hu.MAP complexes that also contain UBE2E2. Hypothesis: it may connect proteostasis to differentiation or signaling in the shared cell state. The sparse network position and lack of STRING partners make a broader module-wide role uncertain.

#### GMIP

- **Related proteins** (co-abundance neighbors): GSTCD (0.89), ZNF106 (0.88), C1GALT1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GEM interacting protein. This gene encodes a member of the ARHGAP family of Rho/Rac/Cdc42-like GTPase activating proteins. The encoded protein interacts with the Ras-related protein Gem through its N-terminal domain. Separately, it interacts with RhoA through a RhoGAP domain, and stimulates RhoA-dependent GTPase activity. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014].
- **Diseases (Open Targets)**: major depressive disorder (0.220); schizophrenia (0.213); bipolar disorder (0.213); Tourette syndrome (0.213); autism spectrum disorder (0.213)
- **Europe PMC papers**: 215
- **Why important**: GMIP is tissue enhanced in bone marrow and lymphoid tissue and is cell-type enhanced in monocyte and neutrophil progenitor populations. Its annotated Rho-family GTPase-activating activity provides a direct link to cytoskeletal organization, cell shape and intracellular signaling. It also occupies a locally connected position with GSTCD, ZNF106 and C1GALT1.
- **Conclusion**: Established evidence: GMIP is associated with bone marrow and progenitor populations and regulates small-GTPase signaling according to its annotation. Hypothesis: it may mediate morphological or migratory changes accompanying the shared hematopoietic state. The module does not establish that GMIP physically interacts with its neighboring genes.

#### C1GALT1

- **Related proteins** (co-abundance neighbors): HAUS7 (0.94), GSTCD (0.92), GMIP (0.87), LCLAT1 (0.84), ACTR5 (0.82), UBE2D1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: core 1 synthase, glycoprotein-N-acetylgalactosamine 3-beta-galactosyltransferase 1. The protein encoded by this gene generates the common core 1 O-glycan structure, Gal-beta-1-3GalNAc-R, by the transfer of Gal from UDP-Gal to GalNAc-alpha-1-R. Core 1 is a precursor for many extended mucin-type O-glycans on cell surface and secreted glycoproteins. Studies in mice suggest that this gene plays a key role in thrombopoiesis and kidney homeostasis.[provided by RefSeq, Sep 2010].
- **Diseases (Open Targets)**: hypertensive disorder (0.561); essential hypertension (0.486); alcohol drinking (0.433); cardiovascular disorder (0.424); refractive error (0.409)
- **Europe PMC papers**: 1157
- **Why important**: C1GALT1 has a relatively central local position and encodes the enzyme that generates the common core one mucin-type O-glycan structure on cell-surface and secreted glycoproteins. It has reported roles in thrombopoiesis and kidney homeostasis and connects in the module to ubiquitin-related and cytoskeletal or regulatory genes. Its extensive literature and disease associations make it biologically interpretable despite the absence of enrichment evidence.
- **Conclusion**: Established evidence: C1GALT1 performs a defined glycosylation reaction and has reported relevance to thrombopoiesis. Hypothesis: its co-abundance may reflect glycoprotein remodeling during hematopoietic maturation or changes in cell-surface state. The module does not show that glycosylation is globally enriched or that C1GALT1 controls the other members.

#### PSMB8

- **Related proteins** (co-abundance neighbors): VIL1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome 20S subunit beta 8. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: proteosome-associated autoinflammatory syndrome (0.829); plasma cell myeloma (0.618); mantle cell lymphoma (0.542); neoplasm (0.536); amyloidosis (0.472)
- **Europe PMC papers**: 3589
- **Why important**: PSMB8 encodes an immunoproteasome-associated proteasome subunit with roles in proteasomal degradation and immune signaling. It is enhanced in megakaryocytes and platelets and is detected in bone marrow. Its connection to VIL1 is weakly informative at the module level but places protein degradation alongside an epithelial or cytoskeletal branch.
- **Conclusion**: Established evidence: PSMB8 is a proteasome component with immune-system and inflammatory annotations and a known disease association with proteasome-related autoinflammation. Hypothesis: it may mark increased antigen-processing or protein-quality-control demand in the shared cell population. The absence of STRING support means the co-abundance link to VIL1 should not be interpreted as a demonstrated physical interaction.

## Module 1

**Tissue pair**: bone_marrow and stem_cells  
**Genes (17)**: ACSL4, NCAPH2, CRYM, FASTKD1, GEMIN6, HIRA, JADE2, KIF2A, METAP2, NDUFA9, OSGEP, PRPF4, TARS2, TERF1, TFAM, TTN, VPS13A

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The module therefore does not support a single statistically established pathway annotation. Its internal structure instead suggests several coordinated cellular programs: HIRA is the main network hub and is associated with histone H3.3 deposition, chromatin organization, and transcriptional regulation; TERF1 connects a telomere-maintenance program; GEMIN6 and PRPF4 connect spliceosomal and snRNP assembly; NDUFA9, TFAM, TARS2, and FASTKD1 indicate mitochondrial respiration, mitochondrial gene expression, or mitochondrial translation; NCAPH2 and KIF2A are compatible with chromosome condensation and mitotic organization. Taken together, the most defensible interpretation is a broad nuclear-maintenance and proliferative-cell state rather than a narrowly defined biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the secreted-gene annotation is absent, and the proteins are predominantly intracellular, with nuclear, nucleoplasmic, mitochondrial, cytosolic, or organellar locations. HPA indicates generally low tissue specificity for most genes and low immune-cell specificity for nearly all genes, arguing against a strongly blood-lineage-specific program. There are, however, cell-type-enhanced signals involving megakaryocytes, platelets, erythrocyte progenitors, spermatogenic cells, and myonuclei, plus a muscle-enhanced TTN signal and tissue-enhanced CRYM signal. Bone-marrow protein detection is common among the genes with available data, whereas there is no matching HPA tissue for stem cells. Thus, the shared module may partly reflect broadly expressed housekeeping and cell-cycle or biosynthetic requirements, with possible contributions from shared proliferative or lineage-associated cell populations rather than a blood-specific secretory program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only one high-confidence pair within the module, NCAPH2–TERF1, so most module edges are not supported by the supplied STRING interaction network. The pair is biologically coherent with chromosome organization and telomere biology, but it does not establish the whole module as a physical complex. hu.MAP identifies PRPF4 and GEMIN6 together in C1 and C2. These are large spliceosome or snRNP-related complexes in which only a small subset of members occurs in this module, so the evidence supports a real spliceosomal connection but not recruitment of the complete complexes. The remaining module relationships lack supplied STRING or hu.MAP support and should be treated as co-abundance relationships rather than proven direct interactions.

**STRING interactions (score >= 0.7)**: 1 of 136 gene pairs: NCAPH2–TERF1 (0.713)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06511.1 (PRPF4, GEMIN6; 2/79); huMAP3_08980.1 (PRPF4, GEMIN6; 2/97)

### Novelty

This module could represent a data-derived co-abundance pattern that is not readily reducible to one previously catalogued complex, because external interaction support is sparse and the genes span chromatin, telomere, splicing, mitochondrial, and cytoskeletal functions. However, it cannot be called a new biological discovery from these data alone. Absence from STRING or hu.MAP does not prove novelty, and the lack of globally significant GO/KEGG enrichment limits claims of a newly defined functional pathway. The strongest novelty claim is therefore a provisional one: coordinated abundance of these programs across bone marrow and stem-cell samples may be a useful reproducible module, but it requires replication, cell-composition control, and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative or progenitor-cell state in which chromatin assembly and transcriptional regulation are coordinated with telomere protection, pre-mRNA processing, mitochondrial capacity, and chromosome segregation. HIRA may organize the central chromatin-associated component, while TERF1 and NCAPH2 mark genome-end and chromosome-architecture requirements, GEMIN6 and PRPF4 support RNA-processing capacity, and NDUFA9 with TFAM support mitochondrial energy and gene-expression demands. This is a mechanistic hypothesis rather than an enrichment result; the observed co-abundance could also arise from shared cell composition or broadly expressed housekeeping programs.

### Important genes

#### HIRA

- **Related proteins** (co-abundance neighbors): JADE2 (1.00), NCAPH2 (0.93), GEMIN6 (0.90), NDUFA9 (0.83), VPS13A (0.83), ACSL4 (0.83), KIF2A (0.82), METAP2 (0.81), OSGEP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: histone cell cycle regulator. This gene encodes a histone chaperone that preferentially places the variant histone H3.3 in nucleosomes. Orthologs of this gene in yeast, flies, and plants are necessary for the formation of transcriptionally silent heterochomatin. This gene plays an important role in the formation of the senescence-associated heterochromatin foci. These foci likely mediate the irreversible cell cycle changes tha…
- **Diseases (Open Targets)**: neurodegenerative disease (0.348); neurodevelopmental disorder (0.223); complex neurodevelopmental disorder (0.185); Fanconi anemia (0.119); Familial prostate cancer (0.113)
- **Europe PMC papers**: 4192
- **Why important**: HIRA is the central network hub and connects chromatin, telomere-associated, mitochondrial, lipid, trafficking, and mitotic-related genes in the module. Its established function as an H3.3 histone chaperone, with roles in nucleosome assembly, chromatin remodeling, transcriptional regulation, and senescence-associated heterochromatin, gives it the strongest functional basis for interpreting the module. It has broad HPA expression, bone-marrow protein detection, disease links including neurodevelopmental and Fanconi-anemia associations, and a substantial literature base.
- **Conclusion**: Established: HIRA is a chromatin regulator and the principal network organizer in this module. Hypothesis: HIRA may coordinate the shared progenitor-cell state by coupling chromatin maintenance to the other module branches; this causal role is not demonstrated by co-abundance alone.

#### TERF1

- **Related proteins** (co-abundance neighbors): CRYM (0.91), TARS2 (0.89), JADE2 (0.88), NDUFA9 (0.86), GEMIN6 (0.82), FASTKD1 (0.80); STRING partners: NCAPH2 (0.713)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: telomeric repeat binding factor 1. This gene encodes a telomere specific protein which is a component of the telomere nucleoprotein complex. This protein is present at telomeres throughout the cell cycle and functions as an inhibitor of telomerase, acting in cis to limit the elongation of individual chromosome ends. The protein structure contains a C-terminal Myb motif, a dimerization domain near its N-terminus and an acidic N-term…
- **Diseases (Open Targets)**: neurodegenerative disease (0.516); major depressive disorder (0.425); insomnia (0.387); thyroid gland carcinoma (0.359); secondary malignant neoplasm (0.355)
- **Europe PMC papers**: 1259
- **Why important**: TERF1 is a major network connector and is the only gene participating in the supplied STRING pair, where it connects to NCAPH2. Its established role in telomere capping, telomere maintenance, and inhibition of telomerase provides a coherent genome-stability interpretation. It also connects in the module to HIRA, GEMIN6, mitochondrial genes, and other nuclear-maintenance genes, and it has disease associations spanning neurodegenerative, psychiatric, and thyroid-cancer contexts.
- **Conclusion**: Established: TERF1 supports a telomere and chromosome-stability component, with an externally supported relationship to NCAPH2. Hypothesis: its co-abundance with HIRA and RNA-processing genes may indicate coordinated genome-protection demands in proliferating progenitor cells.

#### GEMIN6

- **Related proteins** (co-abundance neighbors): HIRA (0.90), TERF1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: gem nuclear organelle associated protein 6. GEMIN6 is part of a large macromolecular complex, localized to both the cytoplasm and the nucleus, that plays a role in the cytoplasmic assembly of small nuclear ribonucleoproteins (snRNPs). Other members of this complex include SMN (MIM 600354), GEMIN2 (SIP1; MIM 602595), GEMIN3 (DDX20; MIM 606168), GEMIN4 (MIM 606969), and GEMIN5 (MIM 607005).[supplied by OMIM, Jul 2002].
- **Diseases (Open Targets)**: neurodegenerative disease (0.503); lung adenocarcinoma (0.074); cystitis (0.056); smoking initiation (0.033); sensory perception of smell (0.024)
- **Europe PMC papers**: 734
- **Why important**: GEMIN6 is one of the two module genes jointly represented in both hu.MAP complexes C1 and C2, together with PRPF4. Its established role in cytoplasmic snRNP assembly and spliceosomal complex assembly provides the clearest complex-level evidence in the module. It is detected in bone marrow, has cell-type-enhanced annotations in spermatogenic populations, has neurodegenerative disease associations, and has a substantial literature base.
- **Conclusion**: Established: GEMIN6 marks an snRNP and spliceosome-related component supported by hu.MAP. Hypothesis: GEMIN6 may couple increased RNA-processing capacity to the chromatin and mitochondrial demands of the shared cell state.

#### PRPF4

- **Related proteins** (co-abundance neighbors): VPS13A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: pre-mRNA splicing tri-snRNP complex factor PRPF4. The protein encoded by this gene is part of a heteromeric complex that binds U4, U5, and U6 small nuclear RNAs and is involved in pre-mRNA splicing. The encoded protein also is a mitotic checkpoint protein and a regulator of chemoresistance in human ovarian cancer. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.634); retinitis pigmentosa 70 (0.578); inherited retinal dystrophy (0.377); neurodegenerative disease (0.203); refractive error (0.083)
- **Europe PMC papers**: 461
- **Why important**: PRPF4 is the second module member present with GEMIN6 in hu.MAP complexes C1 and C2. Its established functions include U4, U5, and U6 tri-snRNP assembly, spliceosome conformational change, pre-mRNA splicing, and mitotic checkpoint regulation. Its nuclear-speckle localization, bone-marrow detection, retinal-dystrophy associations, and literature support make it important for distinguishing a genuine RNA-processing signal from a generic expression correlation.
- **Conclusion**: Established: PRPF4 contributes spliceosomal and possibly mitotic-checkpoint functions and shares complex evidence with GEMIN6. Hypothesis: the PRPF4–GEMIN6 relationship may represent coordinated RNA maturation during progenitor proliferation, although the module does not establish direct regulation.

#### NDUFA9

- **Related proteins** (co-abundance neighbors): TERF1 (0.86), TTN (0.85), HIRA (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A9. The encoded protein is a subunit of the hydrophobic protein fraction of the NADH:ubiquinone oxidoreductase (complex I), the first enzyme complex in the electron transport chain located in the inner mitochondrial membrane. A pseudogene has been identified on chromosome 12. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 26 (0.660); mitochondrial complex I deficiency (0.621); type 2 diabetes mellitus (0.607); Parkinson disease (0.579); diabetes mellitus (0.579)
- **Europe PMC papers**: 2098
- **Why important**: NDUFA9 links the HIRA and TERF1 portions of the network with TTN and is annotated as a subunit of mitochondrial respiratory complex I. Its established role in NADH-to-ubiquinone electron transport and aerobic respiration provides a mitochondrial-energy interpretation that complements the nuclear maintenance genes. It is detected in bone marrow and has disease associations involving mitochondrial complex I deficiency, diabetes, and Parkinson disease, with a substantial literature base.
- **Conclusion**: Established: NDUFA9 represents mitochondrial respiratory-chain function within the module. Hypothesis: its position between nuclear-maintenance genes may reflect energetic support for biosynthesis and proliferation, but the co-abundance data do not show a direct nuclear–mitochondrial regulatory mechanism.

## Module 2

**Tissue pair**: bone_marrow and stem_cells  
**Genes (5)**: AKAP12, CNOT12, COL8A1, HMGN5, NEXN

### Function

The module is most consistent with a cell-structural and signaling-associated program rather than a canonical pathway-defined module. NEXN and COL8A1 point toward actin organization, adhesion, migration, basement-membrane, and extracellular-matrix biology. AKAP12 supports localized kinase and G-protein-coupled receptor signaling, while CNOT12 and HMGN5 provide links to mRNA regulation, chromatin organization, transcription, and genome-maintenance processes. The co-abundance structure is centered on CNOT12 and NEXN, with NEXN connecting the intracellular structural genes to COL8A1. No GO/KEGG term passed global correction, and there was no supplementary STRING functional enrichment; therefore this functional interpretation is based on convergent gene annotations and network architecture, not on significant pathway enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only COL8A1 is annotated as secreted to the extracellular matrix. It is also not primarily an immune-cell module. HPA evidence includes genes not detected in immune cells, genes with low immune-cell specificity, and one gene enriched in basophils. The tissue annotations are heterogeneous, including blood vessel, heart muscle, skeletal muscle, tongue, and testis, while single-cell annotations include vascular and smooth-muscle-related cells, cardiomyocytes, stromal cells, germline-associated cells, erythrocyte progenitors, and megakaryocytes. This pattern argues against a simple bone-marrow immune signature and is compatible with shared structural, vascular, stromal, or other non-immune cell contributions in the sampled tissues. Protein detection in bone marrow is incomplete, and there is no matching HPA tissue for stem cells, so the tissue-level protein evidence is limited.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

None of the possible gene pairs met the supplied high-confidence STRING interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not supported here as established physical protein interactions or as membership in a known multiprotein complex. The strongest co-abundance links connect CNOT12 with AKAP12, HMGN5, and NEXN, and connect NEXN with COL8A1, but these relationships should be interpreted as coordinated abundance rather than direct molecular binding.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unrecognized co-abundance association in the bone-marrow and stem-cell comparison because its internal relationships are absent from the supplied high-confidence STRING and hu.MAP results. However, absence from those resources does not establish biological novelty: the relationships could reflect indirect regulation, shared cell composition, tissue sampling, or technical co-variation. The lack of globally significant GO/KEGG enrichment and the heterogeneous HPA profile further argue for a cautious claim. The defensible conclusion is that this is a potentially novel co-abundance pattern requiring replication, cell-composition analysis, and experimental validation rather than a proven new molecular complex or pathway.

**Hypothesis.** Hypothesis: the module reflects coordinated remodeling of a structural and signaling compartment shared by a subset of stromal, vascular, muscle-related, or progenitor-associated cells in bone marrow and stem-cell samples. In this model, COL8A1 contributes extracellular-matrix or basement-membrane context, NEXN links actin architecture to adhesion and migration, and AKAP12 organizes localized kinase and receptor signaling. CNOT12 and HMGN5 could couple this structural state to post-transcriptional regulation, chromatin organization, and cell-state maintenance. This is a mechanistic hypothesis, not an established causal pathway; it should be tested with cell-resolved expression, perturbation of NEXN or AKAP12, and assays of matrix organization, adhesion, migration, and signaling.

### Important genes

#### NEXN

- **Related proteins** (co-abundance neighbors): CNOT12 (0.84), AKAP12 (0.83), COL8A1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nexilin F-actin binding protein. This gene encodes a filamentous actin-binding protein that may function in cell adhesion and migration. Mutations in this gene have been associated with dilated cardiomyopathy, also known as CMD1CC. Alternatively spliced transcript variants have been described.[provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: dilated cardiomyopathy 1CC (0.792); hypertrophic cardiomyopathy 20 (0.746); familial isolated dilated cardiomyopathy (0.667); hypertrophic cardiomyopathy (0.584); cardiomyopathy, dilated, 2M (0.565)
- **Europe PMC papers**: 1090
- **Why important**: NEXN is a central structural connector in the module, co-abundant with CNOT12, AKAP12, and COL8A1. Its established annotation as a filamentous actin-binding protein involved in adhesion, migration, and cytoskeletal organization provides the clearest bridge between the intracellular structural and extracellular-matrix aspects of the module. Its HPA profile includes heart and skeletal muscle enrichment and several structural or stromal cell types. It has a substantial literature record and strong disease associations with dilated and hypertrophic cardiomyopathy.
- **Conclusion**: Established evidence supports NEXN as an actin-associated adhesion and cytoskeletal gene with cardiac disease relevance. Its role as the principal structural bridge in this module is a network-based interpretation. It is a strong candidate for testing whether the module reflects coordinated adhesion, migration, or contractile-cell biology.

#### AKAP12

- **Related proteins** (co-abundance neighbors): CNOT12 (0.91), NEXN (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: A-kinase anchoring protein 12. The A-kinase anchor proteins (AKAPs) are a group of structurally diverse proteins, which have the common function of binding to the regulatory subunit of protein kinase A (PKA) and confining the holoenzyme to discrete locations within the cell. This gene encodes a member of the AKAP family. The encoded protein is expressed in endothelial cells, cultured fibroblasts, and osteosarcoma cells. It asso…
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); hair color (0.460); cutaneous melanoma (0.403); skin aging (0.376); Abnormality of the skeletal system (0.329)
- **Europe PMC papers**: 2075
- **Why important**: AKAP12 is a signaling scaffold that binds protein kinase A and organizes kinase and phosphatase activities. It is directly co-abundant with the two most connected structural or regulatory members, CNOT12 and NEXN. Its annotations include signal transduction, G-protein-coupled receptor signaling, and inflammatory signaling, while HPA identifies enrichment in several specialized cell types including lymphatic endothelial cells and ovarian stromal cells. It has a large literature record and broad disease associations.
- **Conclusion**: Established evidence supports AKAP12 as a spatial organizer of intracellular signaling rather than as an extracellular matrix component. Its possible role in coupling signaling to the NEXN-associated structural state is a hypothesis suggested by co-abundance, not a demonstrated interaction in this module.

#### COL8A1

- **Related proteins** (co-abundance neighbors): NEXN (0.82); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VIII alpha 1 chain. This gene encodes one of the two alpha chains of type VIII collagen. The gene product is a short chain collagen and a major component of the basement membrane of the corneal endothelium. The type VIII collagen fibril can be either a homo- or a heterotrimer. Alternatively spliced transcript variants encoding the same protein have been observed. [provided by RefSeq, Dec 2011].
- **Diseases (Open Targets)**: Inguinal hernia (0.444); open-angle glaucoma (0.412); glaucoma (0.403); Hernia (0.383); Hernia of the abdominal wall (0.382)
- **Europe PMC papers**: 2630
- **Why important**: COL8A1 is the module’s extracellular-matrix component and is the only member annotated as secreted to the extracellular matrix. It is tissue enriched in blood vessels and is connected to NEXN in the co-abundance graph, making it important for interpreting the module as potentially vascular, stromal, or basement-membrane-associated. Its established functions include extracellular-matrix organization and basement-membrane assembly. It has a large literature record and disease associations involving hernia and glaucoma.
- **Conclusion**: Established evidence supports COL8A1 as a matrix and basement-membrane gene with vascular relevance. Its connection to NEXN suggests a possible structural module, but the module data do not establish that COL8A1 directly drives the intracellular signaling or transcriptional components.

#### CNOT12

- **Related proteins** (co-abundance neighbors): AKAP12 (0.91), HMGN5 (0.88), NEXN (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CCR4-NOT transcription complex subunit 12. Enables ankyrin repeat binding activity and enzyme binding activity. Involved in cellular response to ionizing radiation; double-strand break repair; and positive regulation of protein phosphorylation. Located in several cellular components, including actin cytoskeleton; adherens junction; and heterochromatin. Part of CCR4-NOT complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.225); aging (0.201); insomnia (0.138); hypertensive disorder (0.112); myoepithelial tumor (0.111)
- **Europe PMC papers**: 2
- **Why important**: CNOT12 has the broadest co-abundance connectivity in the module and links AKAP12, HMGN5, and NEXN. It is a subunit of the CCR4-NOT complex and is annotated in mRNA polyadenylation control, double-strand break repair, telomere maintenance, and cellular responses to ionizing radiation. Its HPA profile is broadly nonspecific and not immune-cell detected, which is compatible with a general regulatory role rather than a specialized blood-cell marker. Its disease and literature record is comparatively limited relative to the other selected genes, making its position in this module particularly informative but less well characterized.
- **Conclusion**: Established evidence supports CNOT12 as a CCR4-NOT-associated RNA-regulatory and genome-maintenance factor. Its hub-like position suggests that it may coordinate the structural and nuclear components of the module, but this is an inference from co-abundance and does not demonstrate regulatory causality.

#### HMGN5

- **Related proteins** (co-abundance neighbors): CNOT12 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: high mobility group nucleosome binding domain 5. This gene encodes a nuclear protein with similarities to the high mobility group proteins, HMG14 and HMG17, which suggests that this protein may function as a nucleosomal binding and transcriptional activating protein. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: Abnormality of refraction (0.200); urinary bladder carcinoma (0.097); urinary bladder cancer (0.097); osteosarcoma (0.091); gastric cancer (0.086)
- **Europe PMC papers**: 403
- **Why important**: HMGN5 is the module’s nuclear chromatin-associated member and is connected to CNOT12. Its annotations include chromatin organization, regulation of DNA-templated transcription, cell-population proliferation, gene expression, and apoptosis. HPA identifies testis enrichment and cell-type enhancement in Sertoli cells, epididymal cells, and erythrocyte progenitors, while showing low immune-cell specificity. Its literature record is established but smaller than that of NEXN, AKAP12, or COL8A1.
- **Conclusion**: Established evidence supports HMGN5 as a chromatin and transcriptional regulator. Its inclusion may indicate that the module captures a cell-state or differentiation program in addition to structural biology. A direct connection between HMGN5-mediated chromatin regulation and the extracellular or cytoskeletal genes remains hypothetical.
