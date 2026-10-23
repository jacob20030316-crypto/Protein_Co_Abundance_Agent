# Conserved co-abundance modules: breast and skin

## Module 0

**Tissue pair**: breast and skin  
**Genes (25)**: AATF, C2orf49, BOD1L1, BRD2, CDK13, CHD8, CIZ1, CKAP2, CTDSPL2, FADS1, GGA3, TCF12, ITPRID2, MAP2K6, NAV1, NOL8, PARD3, PHACTR4, PHF8, QSER1, POLRMT, SDE2, SKA3, SNIP1, SNRNP27

### Function

The module does not have a globally significant GO or KEGG enrichment term: no globally significant GO/KEGG term passed global correction. Its gene-level annotations nevertheless converge on nuclear gene regulation and genome maintenance. SDE2 is the strongest network connector and is associated with spliceosome-related RNA processing, DNA-damage responses, ubiquitination, and the mitotic G1 DNA-damage checkpoint. SNIP1 and CDK13 support an RNA-processing and transcriptional-regulation interpretation, while CHD8, PHF8, BRD2, TCF12, and AATF provide chromatin, transcriptional, or nucleolar regulatory context. BOD1L1 adds replication-fork processing and DNA-damage-response biology, and CKAP2, SKA3, and CIZ1 connect the module to mitosis, microtubules, chromosome segregation, and cell-cycle control. MAP2K6 provides a stress- and inflammation-responsive signaling link, whereas POLRMT and SNRNP27 connect mitochondrial transcription with RNA splicing. Thus, the most defensible interpretation is a broadly expressed regulatory module reflecting coordinated control of RNA metabolism, chromatin and transcription, genome integrity, and proliferative or stress-responsive cellular state. This is an interpretation from convergent annotations, not evidence of a formally enriched pathway.

**Cell composition.** The module is predominantly intracellular rather than plasma or secreted: the HPA summary reports no secreted genes, and most proteins are localized to the nucleus, nuclear speckles, nucleoplasm, nucleoli, mitochondria, or intracellular structures. The proteins are detected in both breast and skin for most genes, while tissue specificity is generally low. Many genes are cell-type enhanced, including genes associated with reproductive cells, stromal or epithelial populations, and several hematopoietic populations. A minority show blood-cell-related patterns, including neutrophil, basophil, monocyte, dendritic-cell, or megakaryocyte associations, but the overall HPA summary indicates low immune-cell specificity for most genes and no secreted-protein pattern. Therefore, the shared module is more consistent with a common intracellular cellular-state program, such as transcriptional, RNA-processing, genome-maintenance, or proliferation-related activity, than with a conventional circulating plasma-protein module. Sample admixture or shared cell types, including blood-derived cells, cannot be excluded and should be assessed with cell-composition analyses.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supplies very limited direct support. The only high-confidence STRING relationship within the module is the GGA3–PHF8 pair, so most module edges are not independently supported as known protein interactions by STRING. This means the co-abundance structure should not be interpreted as a densely validated physical complex. hu.MAP identifies BOD1L1 and CHD8 together in two related chromatin or transcription-associated complexes, (hu.MAP huMAP3_09422.1) and (hu.MAP huMAP3_10027.1). However, each complex contains many members outside the module, so these observations support a shared molecular context rather than a complete complex being captured. The limited overlap between the co-abundance network and established interaction resources suggests that the module may combine several functional processes or reflect coordinated regulation rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 1 of 300 gene pairs: GGA3–PHF8 (0.789)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09422.1 (BOD1L1, CHD8; 2/28); huMAP3_10027.1 (BOD1L1, CHD8; 2/33)

### Novelty

The exact breast–skin co-abundance module may represent a potentially novel tissue-shared organization, because most of its within-module relationships are absent from the supplied STRING and hu.MAP evidence and the module has no STRING functional enrichment. However, these absences do not establish novelty: interaction databases are incomplete, co-abundance edges need not be physical interactions, and the component genes have established roles in splicing, chromatin regulation, DNA damage, mitosis, signaling, and intracellular trafficking. The appropriate conclusion is therefore that the module appears data-driven and not reducible to a previously catalogued single complex or pathway, but its novelty as a biological mechanism remains unproven. Independent replication, preservation across cohorts, cell-type adjustment, and perturbation or co-immunoprecipitation experiments would be needed.

**Hypothesis.** Hypothesis: in breast and skin, a shared cellular state coordinates nuclear RNA processing with chromatin regulation and genome surveillance, while coupling these activities to cell-cycle progression, cytoskeletal organization, mitochondrial transcription, and stress signaling. SDE2 may organize or report this state through its links to spliceosome-associated, checkpoint, and mitotic genes; SNIP1, CHD8, PHF8, and BOD1L1 could connect transcriptional or chromatin regulation to RNA processing and replication-fork protection. The observed module could consequently reflect coordinated transcriptional adaptation in proliferating, differentiating, or stressed cells rather than a single physical molecular machine. This hypothesis should be tested by measuring module activity after DNA damage or inflammatory stress, separating epithelial, stromal, and blood-derived cells, and examining whether perturbation of the proposed central genes changes the other module members.

### Important genes

#### SDE2

- **Related proteins** (co-abundance neighbors): POLRMT (0.87), SNIP1 (0.86), CKAP2 (0.85), FADS1 (0.85), CDK13 (0.84), CIZ1 (0.83), PHACTR4 (0.83), SKA3 (0.83), PARD3 (0.82), PHF8 (0.81), GGA3 (0.81), CHD8 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spliceosome associated SDE2. Enables damaged DNA binding activity. Involved in several processes, including cellular response to UV; mitotic G1 DNA damage checkpoint signaling; and protein ubiquitination. Located in several cellular components, including Golgi apparatus; cytosol; and nuclear speck. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.358); myasthenia gravis (0.232); Back pain (0.222); response to surgery (0.222); nephritis (0.220)
- **Europe PMC papers**: 185
- **Why important**: SDE2 is the central network connector in the supplied graph, linking genes involved in mitochondrial transcription, RNA processing, mitosis, fatty-acid biology, cell-cycle regulation, DNA replication-associated control, and cytoskeletal or polarity-related processes. Its annotations include spliceosome association, damaged-DNA binding, cellular response to ultraviolet stress, protein ubiquitination, and the mitotic G1 DNA-damage checkpoint. It is detected in both breast and skin and has substantial literature support, making it the strongest integrative candidate.
- **Conclusion**: Established evidence supports SDE2 as a multifunctional nuclear regulator associated with RNA processing and genome surveillance. In this module, its central network position supports the interpretation that it may report or help coordinate the shared cellular state. Direct control of the other module genes remains a hypothesis.

#### SNIP1

- **Related proteins** (co-abundance neighbors): CTDSPL2 (0.87), QSER1 (0.86), SDE2 (0.86), BOD1L1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Smad nuclear interacting protein 1. This gene encodes a protein that contains a coiled-coil motif and C-terminal forkhead-associated (FHA) domain. The encoded protein functions as a transcriptional coactivator that increases c-Myc activity and inhibits transforming growth factor beta (TGF-beta) and nuclear factor kappa-B (NF-kB) signaling. The encoded protein also regulates the stability of cyclin D1 mRNA, and may play a role in cel…
- **Diseases (Open Targets)**: psychomotor retardation, epilepsy, and craniofacial dysmorphism (0.639); neurodegenerative disease (0.521); self-limited epilepsy with centrotemporal spikes (0.333); asthma (0.238); open-angle glaucoma (0.110)
- **Europe PMC papers**: 531
- **Why important**: SNIP1 is connected to SDE2, CTDSPL2, QSER1, and BOD1L1, placing it at the interface of the module's RNA-processing and genome-maintenance portions. Its established annotations include spliceosome-associated mRNA processing, transcriptional regulation, microRNA processing, mRNA stabilization, and negative regulation of NF-kappa-B signaling. It also has disease associations involving neurodevelopment and neurological disease and a substantial literature base.
- **Conclusion**: Established evidence supports SNIP1 as a nuclear transcriptional and RNA-regulatory protein with links to signaling and proliferation. Its network position makes it a plausible bridge between RNA processing and DNA-damage-related co-abundance, but a module-specific mechanistic role has not been demonstrated.

#### CHD8

- **Related proteins** (co-abundance neighbors): BRD2 (0.82), C2orf49 (0.81), SDE2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09422.1, huMAP3_10027.1
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 8. This gene encodes a member of the chromodomain-helicase-DNA binding protein family, which is characterized by a SNF2-like domain and two chromatin organization modifier domains. The encoded protein also contains brahma and kismet domains, which are common to the subfamily of chromodomain-helicase-DNA binding proteins to which this protein belongs. This gene has been shown to function in several pr…
- **Diseases (Open Targets)**: autism (0.679); hereditary disease (0.550); autism spectrum disorder (0.547); Intellectual disability (0.515); neurodevelopmental disorder (0.497)
- **Europe PMC papers**: 2541
- **Why important**: CHD8 is one of the two module members recurring in the hu.MAP complexes (hu.MAP huMAP3_09422.1) and (hu.MAP huMAP3_10027.1), together with BOD1L1. Its annotations include chromatin remodeling, transcriptional regulation, mRNA processing, and regulation of Wnt and apoptotic processes. It has extensive literature and strong disease associations with autism, intellectual disability, and other neurodevelopmental conditions. Its connection to SDE2 and C2orf49 also places it within the module's nuclear regulatory core.
- **Conclusion**: Established evidence supports CHD8 as a chromatin and transcriptional regulator that can influence RNA processing and cellular developmental programs. Its hu.MAP recurrence strengthens the case for a real molecular context, but the module does not show that CHD8 physically binds most of its co-abundant partners.

#### BOD1L1

- **Related proteins** (co-abundance neighbors): SNIP1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: huMAP3_09422.1, huMAP3_10027.1
- **Function (MyGene.info)**: biorientation of chromosomes in cell division 1 like 1. Predicted to enable protein phosphatase 2A binding activity and protein phosphatase inhibitor activity. Involved in cellular response to DNA damage stimulus and replication fork processing. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.515); luminal B breast carcinoma (0.321); sialolithiasis (0.292); Paralysis (0.284); hypopituitarism (0.236)
- **Europe PMC papers**: 151
- **Why important**: BOD1L1 is linked to SNIP1 and appears with CHD8 in both hu.MAP complexes (hu.MAP huMAP3_09422.1) and (hu.MAP huMAP3_10027.1). Its established annotations include DNA-damage response and replication-fork processing, with predicted protein-phosphatase-related activities. It is detected in both breast and skin, and its HPA profile includes neutrophil enhancement, which is relevant when considering possible cellular-composition effects.
- **Conclusion**: Established evidence supports BOD1L1 as a genome-maintenance factor and provides an independent connection between the module and replication stress. Its co-occurrence with CHD8 in hu.MAP supports shared complex context, while the neutrophil signal means that cell composition should be controlled before assigning the module to epithelial biology.

#### PHF8

- **Related proteins** (co-abundance neighbors): SDE2 (0.81), ITPRID2 (0.81); STRING partners: GGA3 (0.789)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PHD finger protein 8. The protein encoded by this gene is a histone lysine demethylase that preferentially acts on histones in the monomethyl or dimethyl states. The encoded protein requires Fe(2+) ion, 2-oxoglutarate, and oxygen for its catalytic activity. The protein has an N-terminal PHD finger and a central Jumonji C domain. This gene is thought to function as a transcription activator. Defects in this gene are a c…
- **Diseases (Open Targets)**: syndromic X-linked intellectual disability Siderius type (0.770); hereditary disease (0.415); cleft lip (0.372); neurodegenerative disease (0.370); Intellectual disability (0.348)
- **Europe PMC papers**: 1435
- **Why important**: PHF8 is a chromatin enzyme with a PHD finger and Jumonji C domain and is annotated as a histone lysine demethylase and transcriptional activator. It is connected to SDE2 and ITPRID2 in the module, and its GGA3 relationship is the sole high-confidence STRING interaction supplied for the module. PHF8 has established links to chromatin remodeling, transcription, the G1/S transition, and Siderius-type intellectual disability, with extensive literature support.
- **Conclusion**: Established evidence supports PHF8 as a chromatin-regulatory enzyme and gives the module one independently catalogued protein interaction through GGA3. Its position supports a chromatin component in the proposed module function, but the co-abundance data do not establish that PHF8 enzymatically regulates the other module members.

## Module 1

**Tissue pair**: breast and skin  
**Genes (18)**: ACSS1, ATRX, ESS2, EYA3, FAM107B, GGT7, HOMER1, KDM3A, MAP3K7, MAP4K3, MTA3, PAK1, PLEKHA5, PPM1B, RLIG1, SHTN1, STX6, SARS2

### Function

The strongest interpretation is regulation of chromatin state and transcription, supported by (GO:BP chromatin remodeling; q_global = 0.0302), the sole GO/KEGG term passing global correction. (GO:BP chromatin remodeling; q_global = 0.0302) contains ATRX, EYA3, KDM3A, MAP3K7, MAP4K3, MTA3, PAK1, and PPM1B. The module also contains genes involved in signaling, phosphorylation, cytoskeletal regulation, vesicle trafficking, mitochondrial metabolism, and RNA processing. Therefore, chromatin remodeling is the primary shared functional signal, but it does not explain every gene. The GGT7-centered structure may additionally reflect a broader cellular stress, signaling, or membrane-associated state.

**Cell composition.** The module is not dominated by plasma or secreted proteins: HPA reports no secreted genes. Most genes have low tissue specificity, while many show cell-type enhancement. Recurrent HPA signals include brain-related cells, choroid plexus epithelial cells, glial cells, neutrophils, monocytes, dendritic cells, and other immune populations. Most genes have low immune-cell specificity, but several show blood-cell enrichment. The shared module may therefore reflect a common epithelial or stromal cellular program, a shared cell state, or some contribution from immune-cell composition in bulk samples. Protein detection in both breast and skin supports presence in the sampled tissues but does not establish a common cellular origin.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP chromatin remodeling | 0.0302 | ATRX, EYA3, KDM3A, MAP3K7, MAP4K3, MTA3, PAK1, PPM1B |

### STRING and hu.MAP

The co-abundance graph is sparse and centered on GGT7, with many genes connected only to that hub. STRING supplies one high-confidence known relationship, MAP3K7–PPM1B. This supports a biologically plausible connection between kinase signaling and phosphatase regulation of stress and NF-kappa-B pathways, but it does not validate the complete module. No STRING functional-enrichment term was reported, and no hu.MAP complex contained multiple module members. Most module edges should therefore be treated as co-abundance relationships rather than established physical interactions or complex membership.

**STRING interactions (score >= 0.7)**: 1 of 153 gene pairs: MAP3K7–PPM1B (0.946)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This should not be described as a newly discovered molecular complex or a proven novel pathway. The chromatin-remodeling interpretation is consistent with established functions of ATRX, EYA3, KDM3A, and MTA3, and MAP3K7–PPM1B is already represented in STRING. Nevertheless, the breast–skin co-abundance pattern, its GGT7-centered organization, and the combination of chromatin regulators with signaling, trafficking, and metabolic genes are not directly explained by the available interaction resources. The appropriate conclusion is that this is a potentially novel cross-tissue co-abundance pattern requiring independent validation, not a demonstrated novel mechanism.

**Hypothesis.** Hypothesis: a shared breast–skin cellular state couples chromatin remodeling to stress-responsive signaling and membrane or vesicle biology. ATRX, EYA3, KDM3A, and MTA3 may help establish or maintain transcriptional states; MAP3K7 and PPM1B may tune stress, inflammatory, and NF-kappa-B-related signaling; PAK1 may connect signaling to cytoskeletal and cell-state changes; and GGT7 may mark or contribute to glutathione- and vesicle-associated responses. The module could arise within a shared epithelial or stromal population, or from coordinated signals across multiple cell types with some immune contribution. This remains a hypothesis because most edges lack external interaction support and enrichment indicates association rather than causality.

### Important genes

#### GGT7

- **Related proteins** (co-abundance neighbors): PAK1 (0.88), PLEKHA5 (0.86), EYA3 (0.83), MAP3K7 (0.83), FAM107B (0.83), RLIG1 (0.82), PPM1B (0.81), SHTN1 (0.81), STX6 (0.80), ATRX (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gamma-glutamyltransferase 7. This gene is a member of a gene family that encodes enzymes involved in both the metabolism of glutathione and in the transpeptidation of amino acids. Changes in the activity of gamma-glutamyltransferase may signal preneoplastic or toxic conditions in the liver or kidney. The protein encoded by this gene consists of a heavy and a light chain, and it can interact with CT120, a plasma membrane-assoc…
- **Diseases (Open Targets)**: angina pectoris (0.292); coronary artery disorder (0.285); poisoning (0.259); intermediate coronary syndrome (0.225); myocardial infarction (0.225)
- **Europe PMC papers**: 279
- **Why important**: GGT7 is the principal network hub and connects to many other module genes. Its annotations include glutathione metabolism, glutathione catabolism, leukotriene biosynthesis, and negative regulation of oxidative-stress responses. HPA places it in vesicles and detects it in both breast and skin. It has a substantial literature base and is important as a module marker even though it is absent from (GO:BP chromatin remodeling; q_global = 0.0302).
- **Conclusion**: Established evidence supports GGT7 as the central co-abundance marker and as a gene compatible with redox and vesicle-associated biology. It is not established that GGT7 drives the chromatin-remodeling signal; that possibility remains hypothetical.

#### MAP3K7

- **Related proteins** (co-abundance neighbors): GGT7 (0.83), HOMER1 (0.81); STRING partners: PPM1B (0.946)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase kinase kinase 7. The protein encoded by this gene is a member of the serine/threonine protein kinase family. This kinase mediates the signaling transduction induced by TGF beta and morphogenetic protein (BMP), and controls a variety of cell functions including transcription regulation and apoptosis. In response to IL-1, this protein forms a kinase complex including TRAF6, MAP3K7P1/TAB1 and MAP3K7P2/TAB2; this comp…
- **Diseases (Open Targets)**: frontometaphyseal dysplasia 2 (0.753); cardiospondylocarpofacial syndrome (0.746); frontometaphyseal dysplasia (0.504); neurodegenerative disease (0.487); COVID-19 (0.374)
- **Europe PMC papers**: 3598
- **Why important**: MAP3K7 is a signaling kinase involved in TGF-beta and BMP signaling, MAPK activation, inflammatory signaling, apoptosis, and NF-kappa-B activation. It is included in (GO:BP chromatin remodeling; q_global = 0.0302), detected in both tissues, and forms the only high-confidence STRING relationship in the module with PPM1B. Its connections to GGT7 and HOMER1 place it at the interface between the module hub and signaling-related genes. It also has extensive literature and disease-association evidence.
- **Conclusion**: Established evidence supports MAP3K7 as an important signaling component and as part of the globally supported chromatin-remodeling-associated module. Its precise role in the breast–skin co-abundance pattern, including a possible link between signaling and chromatin state, remains hypothetical.

#### PPM1B

- **Related proteins** (co-abundance neighbors): GGT7 (0.81); STRING partners: MAP3K7 (0.946)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Cytosol; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase, Mg2+/Mn2+ dependent 1B. The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase has been shown to dephosphorylate cyclin-dependent kinases (CDKs), and thus may be involved in cell cycle control. Overexpression of this phosphatase is reported to cause cell-growth arrest or cel…
- **Diseases (Open Targets)**: cancer (0.509); neurodegenerative disease (0.301); ovarian dysfunction (0.201); hypertrophic cardiomyopathy (0.185); refractive error (0.157)
- **Europe PMC papers**: 745
- **Why important**: PPM1B is a PP2C-family serine/threonine phosphatase included in (GO:BP chromatin remodeling; q_global = 0.0302). It is annotated for protein dephosphorylation and regulation, including negative regulation of NF-kappa-B signaling. Its high-confidence STRING relationship with MAP3K7 provides the clearest externally supported molecular link within the module. It is detected in both tissues and has disease and cancer-related associations supported by a substantial literature base.
- **Conclusion**: Established evidence supports PPM1B as a regulatory phosphatase and known MAP3K7 partner that could counterbalance kinase-driven signaling. Its involvement in chromatin remodeling is supported at the module-enrichment level, not by a demonstrated direct chromatin mechanism.

#### EYA3

- **Related proteins** (co-abundance neighbors): MAP4K3 (0.84), GGT7 (0.83), KDM3A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EYA transcriptional coactivator and phosphatase 3. This gene encodes a member of the eyes absent (EYA) family of proteins. The encoded protein may act as a transcriptional activator and have a role during development. It can act as a mediator of chemoresistance and cell survival in Ewing sarcoma cells, where this gene is up-regulated via a micro-RNA that binds to the 3' UTR of the transcript. A similar protein in mice acts as a transcriptional act…
- **Diseases (Open Targets)**: alcohol drinking (0.106); stroke disorder (0.106); Genu varum (0.097); Genu valgum (0.097); neoplasm (0.093)
- **Europe PMC papers**: 563
- **Why important**: EYA3 is included in (GO:BP chromatin remodeling; q_global = 0.0302) and is annotated as a transcriptional coactivator and phosphatase involved in chromatin remodeling, DNA repair, radiation response, differentiation, and morphogenesis. It connects the GGT7-centered portion of the network to KDM3A and MAP4K3. Its transcriptional, developmental, and cancer-related functions make it a plausible regulatory bridge, with a meaningful literature base.
- **Conclusion**: Established evidence supports EYA3 as a chromatin- and transcription-related regulator consistent with (GO:BP chromatin remodeling; q_global = 0.0302). Its connection to GGT7 and the other module genes is a co-abundance observation, so a direct functional bridge remains hypothetical.

#### KDM3A

- **Related proteins** (co-abundance neighbors): EYA3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lysine demethylase 3A. This gene encodes a zinc finger protein that contains a jumonji domain and may play a role in hormone-dependent transcriptional activation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2009]
- **Diseases (Open Targets)**: atrial fibrillation (0.363); neurodegenerative disease (0.307); Familial prostate cancer (0.133); prostate cancer (0.133); neoplasm (0.111)
- **Europe PMC papers**: 2114
- **Why important**: KDM3A is a chromatin-associated lysine demethylase included in (GO:BP chromatin remodeling; q_global = 0.0302). It is annotated for chromatin remodeling, transcriptional regulation, hormone-mediated signaling, and androgen-receptor signaling. Its direct module connection to EYA3 is notable because both genes provide compatible chromatin-regulatory evidence. KDM3A also has a substantial literature base and disease associations involving cancer and neurodegenerative disease.
- **Conclusion**: Established evidence supports KDM3A as a plausible contributor to the chromatin-remodeling interpretation. It is not established that KDM3A causes the shared breast–skin pattern or acts directly with EYA3 in this module.

#### PAK1

- **Related proteins** (co-abundance neighbors): GGT7 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cytosol; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: p21 (RAC1) activated kinase 1. This gene encodes a family member of serine/threonine p21-activating kinases, known as PAK proteins. These proteins are critical effectors that link RhoGTPases to cytoskeleton reorganization and nuclear signaling, and they serve as targets for the small GTP binding proteins Cdc42 and Rac. This specific family member regulates cell motility and morphology. Mutations in this gene have been associate…
- **Diseases (Open Targets)**: intellectual developmental disorder with macrocephaly, seizures, and speech delay (0.712); neurodevelopmental disorder (0.477); hereditary disease (0.339); cutaneous melanoma (0.187); Myoclonus (0.187)
- **Europe PMC papers**: 9937
- **Why important**: PAK1 is included in (GO:BP chromatin remodeling; q_global = 0.0302) and links Rho-family GTPases to cytoskeletal remodeling, cell motility, morphology, and nuclear signaling. Its annotations also include chromatin remodeling, DNA-damage response, MAPK signaling, and cell-population proliferation. HPA reports tissue enhancement in brain and enrichment across several myeloid and granulocyte populations, making it relevant to possible cell-composition effects. PAK1 has an extensive literature base and strong disease-association evidence.
- **Conclusion**: Established evidence supports PAK1 as a signaling and cytoskeletal regulator compatible with the module's chromatin and cell-state interpretation. Its immune-cell enrichment means that part of its co-abundance signal could reflect cellular composition; a direct role in the shared tissue mechanism remains hypothetical.

## Module 2

**Tissue pair**: breast and skin  
**Genes (28)**: ADAM9, AFAP1L2, AFAP1, ATXN2L, BCAR1, CAAP1, CAV1, DDX10, EPHA2, ERBIN, ERCC5, PTK2, IRS2, ITSN2, LIMD1, LPXN, MINK1, MPDZ, RASAL2, OBSL1, PEAK1, PHF23, PTBP2, PTPN14, RIPK2, RSF1, TNS3, ZNF106

### Function

The module is most consistently associated with epithelial cell adhesion, cell-substrate junctions, focal adhesions, integrin-mediated adhesion, and receptor-linked tyrosine-kinase signaling. The primary evidence is the set of globally corrected GO terms (GO:CC cell-substrate junction; q_global = 0.000217) through (GO:BP cell adhesion; q_global = 0.0498), which collectively point to an adhesion-signaling apparatus rather than to a single metabolic pathway. PTK2, BCAR1, EPHA2, CAV1, PEAK1, TNS3, AFAP1, LIMD1, LPXN, and related scaffold proteins connect cytoskeletal organization with receptor signaling. The presence of ERBB and epidermal-growth-factor receptor terms (GO:BP enzyme-linked receptor protein signaling pathway; q_global = 0.00357), (GO:BP epidermal growth factor receptor signaling pathway; q_global = 0.00759), and (GO:BP ERBB signaling pathway; q_global = 0.0108), together with integrin terms (GO:BP regulation of cell adhesion mediated by integrin; q_global = 0.00116) and (GO:BP cell adhesion mediated by integrin; q_global = 0.0239), supports a model in which extracellular signals are integrated at membrane-associated adhesion structures. The sparse co-abundance graph nevertheless contains a hub-like adhesion core, especially around PEAK1, AFAP1L2, TNS3, AFAP1, and EPHA2, with additional peripheral genes involved in endocytosis, cytoskeletal organization, transcriptional regulation, RNA processing, and innate signaling.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, and most proteins are intracellular, membrane-associated, or focal-adhesion-associated. Protein detection is broadly supported in both breast and skin, while most genes have low tissue specificity. The module therefore appears compatible with a shared structural or epithelial program in both tissues rather than being explained primarily by a single tissue-specific secreted product. There is some immune and blood-cell signal, including enhanced or enriched patterns for several genes in lymphoid cells, monocytes, dendritic cells, neutrophils, basophils, memory B cells, and other immune populations. LPXN, IRS2, TNS3, ADAM9, CAV1, EPHA2, and AFAP1 have particularly relevant immune-cell annotations. Thus, contribution from shared stromal or immune cell types, or variation in their abundance, remains a plausible alternative or additional explanation. HPA also shows cell-type-enhanced expression across diverse epithelial, endothelial, neural-lineage, and immune cell types, arguing against a narrowly breast-specific or skin-specific interpretation.

**GO/KEGG enrichment**: 13 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC cell-substrate junction | 0.000217 | ADAM9, AFAP1, BCAR1, CAV1, EPHA2, ERBIN, LIMD1, LPXN, PEAK1, PTK2, TNS3 |
| GO:CC anchoring junction | 0.000334 | ADAM9, AFAP1, BCAR1, CAV1, EPHA2, ERBIN, LIMD1, LPXN, MPDZ, OBSL1, PEAK1, PTK2, TNS3 |
| GO:BP regulation of cell adhesion mediated by integrin | 0.00116 | ADAM9, EPHA2, LPXN, PTK2 |
| GO:CC focal adhesion | 0.00134 | ADAM9, AFAP1, BCAR1, CAV1, EPHA2, LIMD1, LPXN, PEAK1, PTK2, TNS3 |
| GO:BP enzyme-linked receptor protein signaling pathway | 0.00357 | ADAM9, AFAP1L2, BCAR1, CAV1, EPHA2, ERBIN, IRS2, LPXN, PTK2, ZNF106 |
| GO:BP epidermal growth factor receptor signaling pathway | 0.00759 | AFAP1L2, BCAR1, EPHA2, ERBIN, PTK2 |
| GO:CC cell junction | 0.00764 | ADAM9, AFAP1, BCAR1, CAV1, EPHA2, ERBIN, ITSN2, LIMD1, LPXN, MINK1, MPDZ, OBSL1, PEAK1, PTK2, TNS3 |
| GO:BP ERBB signaling pathway | 0.0108 | AFAP1L2, BCAR1, EPHA2, ERBIN, PTK2 |
| GO:BP cell adhesion mediated by integrin | 0.0239 | ADAM9, EPHA2, LPXN, PTK2 |
| GO:MF non-membrane spanning protein tyrosine kinase activity | 0.0334 | PEAK1, PTK2, RIPK2 |
| GO:MF protein tyrosine kinase activity | 0.0421 | EPHA2, PEAK1, PTK2, RIPK2 |
| GO:BP cellular response to peptide hormone stimulus | 0.0479 | BCAR1, CAV1, EPHA2, IRS2, PTK2, ZNF106 |
| GO:BP cell adhesion | 0.0498 | ADAM9, BCAR1, CAV1, EPHA2, ERBIN, LPXN, MINK1, PEAK1, PTK2, RIPK2 |

### STRING and hu.MAP

STRING supports a small set of high-confidence relationships within the module: BCAR1 with PTK2, BCAR1 with TNS3, CAV1 with EPHA2, CAV1 with ERBIN, and PTK2 with TNS3. These known links independently reinforce the focal-adhesion and membrane-signaling interpretation. STRING functional results (STRING COMPARTMENTS Anchoring junction; within-query FDR = 1.54e-06) through (STRING Component Cell junction; within-query FDR = 0.0003) reproduce the anchoring-junction, cell-substrate-junction, focal-adhesion, and cell-junction themes, while (STRING PMID (2020) Topological features of integrin adhesion complexes revealed by multiplexed proximity biotinylation.; within-query FDR = 0.00064), (STRING PMID (2022) Identification of Src Family Kinases as Potential Therapeutic Targets for Chemotherapy-Resistant Triple Negative Breast Cancer.; within-query FDR = 0.0098), (STRING Process Enzyme-linked receptor protein signaling pathway; within-query FDR = 0.0102), (STRING Process Regulation of cell adhesion mediated by integrin; within-query FDR = 0.0102), and (STRING PMID (2010) Profiling Y561-dependent and -independent substrates of CSF-1R in epithelial cells.; within-query FDR = 0.0108) connect the module to integrin complexes, Src-family signaling, receptor signaling, and epithelial signaling. These are supplementary confirmations, not additional globally corrected enrichment claims. The module also contains ZNF106 and ITSN2 in the hu.MAP complexes (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1). Those complexes are broad trafficking and clathrin-associated assemblies, so their partial representation suggests possible endocytic or receptor-trafficking context but does not establish a complete physical complex for the module. Overall, the network combines a known adhesion-signaling core with peripheral genes that may be co-regulated or indirectly connected rather than all forming one stable complex.

**STRING interactions (score >= 0.7)**: 5 of 378 gene pairs: BCAR1–PTK2 (0.999); BCAR1–TNS3 (0.906); CAV1–EPHA2 (0.798); CAV1–ERBIN (0.733); PTK2–TNS3 (0.783)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Anchoring junction (FDR = 1.54e-06, 13 genes); COMPARTMENTS Cell-substrate junction (FDR = 2.23e-06, 11 genes); COMPARTMENTS Focal adhesion (FDR = 1.82e-05, 10 genes); Component Cell-substrate junction (FDR = 5.26e-05, 11 genes); Component Anchoring junction (FDR = 5.26e-05, 14 genes); Component Focal adhesion (FDR = 0.00017, 10 genes); Keyword Cell junction (FDR = 0.00029, 10 genes); Component Cell junction (FDR = 0.0003, 15 genes); PMID (2020) Topological features of integrin adhesion complexes revealed by multiplexed proximity biotinylation. (FDR = 0.00064, 8 genes); Keyword Phosphoprotein (FDR = 0.0083, 28 genes); PMID (2022) Identification of Src Family Kinases as Potential Therapeutic Targets for Chemotherapy-Resistant Triple Negative Breast Cancer. (FDR = 0.0098, 6 genes); Process Enzyme-linked receptor protein signaling pathway (FDR = 0.0102, 8 genes); Process Peptidyl-tyrosine phosphorylation (FDR = 0.0102, 5 genes); Process Regulation of cell adhesion mediated by integrin (FDR = 0.0102, 4 genes); PMID (2010) Profiling Y561-dependent and -independent substrates of CSF-1R in epithelial cells. (FDR = 0.0108, 7 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10762.1 (ZNF106, ITSN2; 2/62); huMAP3_12918.1 (ZNF106, ITSN2; 2/62); huMAP3_12394.1 (ZNF106, ITSN2; 2/98)

### Novelty

The module should not be described as an entirely new molecular pathway. Its central biology is already established by the known STRING relationships, the focal-adhesion and receptor-signaling annotations, and the literature associated with PTK2, EPHA2, CAV1, BCAR1, and related genes. The potentially new aspect is the conserved co-abundance organization of this particular gene set across breast and skin, especially the way established adhesion components are combined with less-characterized or peripheral genes. The limited STRING connectivity and the partial hu.MAP representation may indicate a tissue-level regulatory or compositional association rather than a previously unrecognized physical complex. Absence from STRING or hu.MAP cannot by itself establish novelty. A defensible conclusion is that this is a potentially novel cross-tissue co-abundance module built around well-established adhesion and receptor-signaling biology, requiring independent validation before being claimed as a new mechanism.

**Hypothesis.** Hypothesis: in shared breast and skin cellular environments, receptor and integrin inputs converge on a focal-adhesion scaffold containing PTK2, BCAR1, PEAK1, TNS3, CAV1, EPHA2, and associated adaptors. This scaffold may coordinate adhesion-dependent cytoskeletal remodeling, cell spreading, migration, and receptor trafficking. ADAM9 could modify cell-surface or cell-matrix interactions, while ERBIN and CAV1 could organize receptor and membrane signaling. AFAP1L2, IRS2, and related adaptors could connect receptor inputs to downstream signaling, whereas ITSN2 and the hu.MAP-associated trafficking context could influence endocytic handling of activated receptors. The immune-cell annotations raise a second hypothesis that part of the conserved signal reflects shared immune or stromal-cell composition. These mechanistic links are hypotheses inferred from the combined evidence and should not be treated as demonstrated physical interactions for every module member.

### Important genes

#### PTK2

- **Related proteins** (co-abundance neighbors): PEAK1 (0.84), PTPN14 (0.82), AFAP1L2 (0.81); STRING partners: BCAR1 (0.999), TNS3 (0.783)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein tyrosine kinase 2. This gene encodes a cytoplasmic protein tyrosine kinase which is found concentrated in the focal adhesions that form between cells growing in the presence of extracellular matrix constituents. The encoded protein is a member of the FAK subfamily of protein tyrosine kinases but lacks significant sequence similarity to kinases from other subfamilies. Activation of this gene may be an important early…
- **Diseases (Open Targets)**: neurodegenerative disease (0.551); Abnormality of the skeletal system (0.450); atrial fibrillation (0.396); Dupuytren Contracture (0.390); non-small cell lung carcinoma (0.327)
- **Europe PMC papers**: 7056
- **Why important**: PTK2 is a central focal-adhesion kinase with a strong position in the module and extensive representation across the globally corrected adhesion, integrin, receptor-signaling, and tyrosine-kinase terms (GO:CC cell-substrate junction; q_global = 0.000217) through (GO:BP cell adhesion; q_global = 0.0498). It has direct STRING support with BCAR1 and TNS3 and is located at focal adhesion sites in HPA. Its established roles include cell-matrix adhesion, signal-complex assembly, and epidermal-growth-factor receptor signaling. Its substantial literature volume and disease associations make it the clearest mechanistic anchor.
- **Conclusion**: Established evidence supports PTK2 as a core adhesion-signaling component and a plausible organizer of the module. It is reasonable to hypothesize that PTK2 activity contributes to the shared co-abundance pattern, but co-abundance does not demonstrate kinase activation or causality.

#### EPHA2

- **Related proteins** (co-abundance neighbors): ADAM9 (0.87), CAV1 (0.83), TNS3 (0.81), ERBIN (0.81); STRING partners: CAV1 (0.798)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EPH receptor A2. This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are d…
- **Diseases (Open Targets)**: early-onset posterior polar cataract (0.770); total early-onset cataract (0.770); early-onset non-syndromic cataract (0.681); colorectal cancer (0.594); chronic myeloid leukemia (0.583)
- **Europe PMC papers**: 8524
- **Why important**: EPHA2 has one of the strongest annotation footprints in the module, appearing in nearly all of the primary adhesion, receptor-signaling, integrin, and tyrosine-kinase terms (GO:CC cell-substrate junction; q_global = 0.000217) through (GO:BP cell adhesion; q_global = 0.0498). It occupies a membrane and junctional location, connects to ADAM9, CAV1, TNS3, and ERBIN in the module graph, and has STRING support with CAV1. Its established receptor-kinase, lamellipodium, stress-response, and epithelial signaling functions are highly relevant to breast and skin biology. It also has a large literature base and multiple disease associations.
- **Conclusion**: Established evidence supports EPHA2 as a membrane signaling node linking receptor activity to adhesion and cytoskeletal behavior. A role in coordinating the conserved breast-skin module is plausible, but the module alone does not establish the direction or state of EPHA2 signaling.

#### BCAR1

- **Related proteins** (co-abundance neighbors): PEAK1 (0.80); STRING partners: PTK2 (0.999), TNS3 (0.906)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Focal adhesion sites; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCAR1 scaffold protein, Cas family member. The protein encoded by this gene is a member of the Crk-associated substrate (CAS) family of scaffold proteins, characterized by the presence of multiple protein-protein interaction domains and many serine and tyrosine phosphorylation sites. The encoded protein contains a Src-homology 3 (SH3) domain, a proline-rich domain, a substrate domain which contains 15 repeat of the YxxP consensus phosphory…
- **Diseases (Open Targets)**: neurodegenerative disease (0.551); Abnormality of the skeletal system (0.525); exocrine pancreatic carcinoma (0.413); alcohol drinking (0.307); stroke disorder (0.289)
- **Europe PMC papers**: 1423
- **Why important**: BCAR1 is a scaffold and phosphorylation substrate positioned at the plasma membrane and focal adhesions. It is included in many primary terms spanning junctions, focal adhesions, receptor signaling, and cell adhesion (GO:CC cell-substrate junction; q_global = 0.000217), (GO:CC anchoring junction; q_global = 0.000334), (GO:CC focal adhesion; q_global = 0.00134) through (GO:BP ERBB signaling pathway; q_global = 0.0108), and (GO:BP cellular response to peptide hormone stimulus; q_global = 0.0479) through (GO:BP cell adhesion; q_global = 0.0498). It has strong STRING relationships with PTK2 and TNS3 and provides a plausible adaptor between Src-family or receptor-tyrosine-kinase inputs and actin organization. Its substantial literature volume supports a well-established signaling role.
- **Conclusion**: Established evidence supports BCAR1 as a key signal-integrating scaffold in the module. Its co-abundance with PTK2 and TNS3 is consistent with coordinated focal-adhesion regulation, while any specific breast-skin mechanism remains a hypothesis.

#### PEAK1

- **Related proteins** (co-abundance neighbors): RASAL2 (0.88), LIMD1 (0.85), PTK2 (0.84), TNS3 (0.83), MINK1 (0.81), BCAR1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Focal adhesion sites; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pseudopodium enriched atypical kinase 1. This gene encodes a non-receptor tyrosine kinase that is a member of the new kinase family three (NFK3) family. In migrating cells, the encoded protein is associated with the actin cytoskeleton and focal adhesions and promotes developing focal adhesion elongation. This protein may play a role in the regulation of cell migration, proliferation and cancer metastasis. [provided by RefSeq, Mar 2014].
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.501); neurodegenerative disease (0.423); diabetes mellitus (0.397); diabetic eye disease (0.351); diabetic neuropathy (0.300)
- **Europe PMC papers**: 882
- **Why important**: PEAK1 has the highest network connectivity and links RASAL2, LIMD1, PTK2, TNS3, MINK1, and BCAR1. It is located at focal adhesion sites and appears in the primary junction, focal-adhesion, adhesion, and tyrosine-kinase terms (GO:CC cell-substrate junction; q_global = 0.000217), (GO:CC anchoring junction; q_global = 0.000334), (GO:CC focal adhesion; q_global = 0.00134), (GO:CC cell junction; q_global = 0.00764), (GO:MF non-membrane spanning protein tyrosine kinase activity; q_global = 0.0334), (GO:MF protein tyrosine kinase activity; q_global = 0.0421), and (GO:BP cell adhesion; q_global = 0.0498). The supplied annotation describes a non-receptor tyrosine kinase associated with actin cytoskeleton organization, focal-adhesion elongation, migration, and metastasis. Its literature volume is substantial, although lower than that of the best-established core genes.
- **Conclusion**: Established evidence supports PEAK1 as a highly connected focal-adhesion and migration-associated kinase. Its network position makes it an important candidate mediator of the module, but its precise causal contribution to the conserved tissue pattern remains to be tested.

#### CAV1

- **Related proteins** (co-abundance neighbors): EPHA2 (0.83), LIMD1 (0.82); STRING partners: EPHA2 (0.798), ERBIN (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Golgi apparatus; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caveolin 1. The scaffolding protein encoded by this gene is the main component of the caveolae plasma membranes found in most cell types. The protein links integrin subunits to the tyrosine kinase FYN, an initiating step in coupling integrins to the Ras-ERK pathway and promoting cell cycle progression. The gene is a tumor suppressor gene candidate and a negative regulator of the Ras-p42/44 mitogen-activated k…
- **Diseases (Open Targets)**: congenital generalized lipodystrophy type 3 (0.661); pulmonary hypertension, primary, 3 (0.626); partial lipodystrophy, congenital cataracts, and neurodegeneration syndrome (0.615); atrial fibrillation (0.581); glaucoma (0.528)
- **Europe PMC papers**: 19537
- **Why important**: CAV1 is a membrane caveolar scaffold detected in both breast and skin and is annotated to junctional, focal-adhesion, receptor-signaling, hormone-response, and cell-adhesion terms (GO:CC cell-substrate junction; q_global = 0.000217), (GO:CC anchoring junction; q_global = 0.000334), (GO:CC focal adhesion; q_global = 0.00134), (GO:BP enzyme-linked receptor protein signaling pathway; q_global = 0.00357), (GO:CC cell junction; q_global = 0.00764), (GO:BP cellular response to peptide hormone stimulus; q_global = 0.0479), and (GO:BP cell adhesion; q_global = 0.0498). Its STRING relationships with EPHA2 and ERBIN support a membrane-signaling connection. The supplied annotation links CAV1 to integrin coupling, FYN, Ras-ERK signaling, hypoxia responses, and endothelial regulation. It has the largest literature volume among the selected genes and broad disease associations.
- **Conclusion**: Established evidence supports CAV1 as a membrane-organizing scaffold that could connect caveolae, integrins, and receptor signaling. Its broad expression means that the module may reflect shared cellular architecture rather than a tissue-exclusive program; a specific causal role is therefore a hypothesis.

## Module 3

**Tissue pair**: breast and skin  
**Genes (10)**: ANKHD1, BACC1, CHAF1A, CARD19, ENTR1, MT-ND3, PIP4K2B, SUN1, TNFRSF10B, WFS1

### Function

The module does not have any GO or KEGG term passing global correction, so no globally significant pathway assignment can be made from enrichment. Its gene content instead suggests a mixed cellular maintenance and stress-response program. Established functions represented in the module include extrinsic apoptosis and death-receptor signaling through TNFRSF10B, mitochondrial electron transport through MT-ND3, chromatin assembly through CHAF1A, phosphatidylinositol metabolism and autophagy-related signaling through PIP4K2B, endocytic recycling and cilium-related trafficking through ENTR1, nuclear-envelope anchorage through SUN1, and endoplasmic-reticulum homeostasis through WFS1. ANKHD1 is the central network connector and is annotated as a possible scaffold involved in caspase regulation and cell survival. Because these functions span several cellular compartments and no globally significant GO/KEGG term is significant, the module is best interpreted as a coordinated cellular-state signature rather than a specific pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It also does not resemble a blood-cell module, because nearly all genes have low immune-cell specificity and only CHAF1A is immune-cell enhanced, with plasmacytoid dendritic cells represented. Most genes have low tissue specificity, while two are tissue enhanced in heart muscle or bone marrow. The single-cell annotations are diverse and include neuronal, epithelial, reproductive, hepatic, pancreatic, endothelial, and progenitor populations. This argues against a simple breast- or skin-specific program and is more consistent with broadly expressed cellular machinery, possibly influenced by shared cell states or cellular composition.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING functional-enrichment result is available, and no STRING interaction meets the stated confidence threshold. No hu.MAP complex contains multiple module members. Therefore, the co-abundance relationships are not supported here by high-confidence prior protein-interaction or complex evidence. The strongest within-module connections are co-abundance observations rather than established physical interactions. The ANKHD1-centered structure is therefore useful for prioritization, but it should not be interpreted as a validated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 45 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module cannot be declared a newly discovered biological mechanism solely because it is absent from STRING and hu.MAP; those resources are incomplete and focus on different evidence types. The module may represent a novel cross-tissue co-abundance pattern because its breast-skin association is not accompanied by a recognized shared complex or high-confidence interaction network. However, its individual biology is not wholly novel: apoptosis, mitochondrial respiration, chromatin assembly, lipid signaling, trafficking, nuclear-envelope function, and ER homeostasis are established functions of its constituent genes. The defensible conclusion is that the cross-tissue co-abundance organization is potentially novel, while a new molecular pathway remains unproven.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program linking survival and stress handling across breast and skin samples. ANKHD1 may coordinate several components of this state, while TNFRSF10B represents death-receptor and apoptotic signaling, MT-ND3 represents mitochondrial energetic and oxidative-stress status, PIP4K2B represents membrane-lipid and autophagy-related signaling, and WFS1 represents ER homeostasis. CHAF1A may connect the state to replication-associated chromatin maintenance. The observed co-abundance pattern could therefore arise from coordinated variation in cell survival, organelle stress, and proliferative or differentiation state rather than from direct physical binding among the proteins. This hypothesis requires validation with independent cohorts, cell-type-aware analysis, perturbation experiments, and targeted protein measurements.

### Important genes

#### ANKHD1

- **Related proteins** (co-abundance neighbors): TNFRSF10B (0.91), MT-ND3 (0.86), ENTR1 (0.81), CHAF1A (0.81), PIP4K2B (0.80), WFS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location None; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ankyrin repeat and KH domain containing 1. This gene encodes a protein with multiple ankyrin repeat domains and a single KH-domain. The protein is thought to function as a scaffolding protein, and it may be involved in the regulation of caspases and thereby play an antiapoptotic role in cell survival. Alternative splicing results in multiple transcript variants, one of which generates a fusion transcript (MASK-BP3) with the downstream eIF4…
- **Diseases (Open Targets)**: neurodegenerative disease (0.438); non-small cell lung carcinoma (0.089); breast carcinoma (0.082); colorectal carcinoma (0.080); autosomal dominant polycystic kidney disease (0.078)
- **Europe PMC papers**: 333
- **Why important**: ANKHD1 is the principal network connector in the module and links TNFRSF10B, MT-ND3, ENTR1, CHAF1A, PIP4K2B, and WFS1. Its annotated ankyrin-repeat and KH-domain architecture is compatible with a scaffolding role, and the fact sheet describes a possible role in caspase regulation and cell survival. It has broad tissue specificity, neuronal and glial single-cell associations, breast and skin protein detection, disease links including neurodegenerative disease and breast carcinoma, and a substantial literature base.
- **Conclusion**: Established: ANKHD1 is the module's main co-abundance connector and has a plausible scaffold or survival-related function. Hypothesis: it may organize the cross-compartment cellular-state signal represented by this module. The network position does not establish direct physical interaction or causality.

#### TNFRSF10B

- **Related proteins** (co-abundance neighbors): ANKHD1 (0.91), BACC1 (0.83), SUN1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TNF receptor superfamily member 10b. The protein encoded by this gene is a member of the TNF-receptor superfamily, and contains an intracellular death domain. This receptor can be activated by tumor necrosis factor-related apoptosis inducing ligand (TNFSF10/TRAIL/APO-2L), and transduces an apoptosis signal. Studies with FADD-deficient mice suggested that FADD, a death domain containing adaptor protein, is required for the apoptosis m…
- **Diseases (Open Targets)**: basal cell carcinoma (0.509); head and neck squamous cell carcinoma (0.457); renal carcinoma (0.442); Iron deficiency anemia (0.435); clear cell renal carcinoma (0.423)
- **Europe PMC papers**: 2980
- **Why important**: TNFRSF10B is connected to ANKHD1, BACC1, and SUN1 and encodes a death-domain-containing TNF-receptor family member activated by TRAIL. Its established functions include extrinsic apoptotic signaling, defense response to tumor cells, and NF-kappaB-related signaling. It is detected in both breast and skin, has disease associations involving skin and other carcinomas, and has a large literature base.
- **Conclusion**: Established: TNFRSF10B provides the clearest apoptosis and receptor-signaling anchor in the module. Hypothesis: coordinated abundance with ANKHD1 and the nuclear-envelope component SUN1 may mark variation in death-receptor sensitivity or survival state. The module does not show that these proteins physically interact.

#### MT-ND3

- **Related proteins** (co-abundance neighbors): ANKHD1 (0.86), CARD19 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH dehydrogenase subunit 3. Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone. Part of mitochondrial respiratory chain complex I. Implicated in Leber hereditary optic neuropathy; Leigh disease; and Parkinson's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Leigh syndrome (0.717); mitochondrial disease (0.671); mitochondrial complex I deficiency (0.667); type 2 diabetes mellitus (0.609); diabetes mellitus (0.584)
- **Europe PMC papers**: 2660
- **Why important**: MT-ND3 is connected to ANKHD1 and CARD19 and encodes a mitochondrial respiratory-chain complex component involved in NADH-to-ubiquinone electron transfer. Its annotations include aerobic respiration and response to oxidative stress, while disease associations include mitochondrial disorders, Leigh syndrome, and Leber hereditary optic neuropathy. It is tissue enhanced in heart muscle and detected in both breast and skin.
- **Conclusion**: Established: MT-ND3 is a marker of mitochondrial respiratory function and energetic or oxidative status. Hypothesis: its co-abundance with apoptosis- and stress-related genes may indicate coupling between mitochondrial state and cellular survival. This does not demonstrate mitochondrial dysfunction in the samples.

#### WFS1

- **Related proteins** (co-abundance neighbors): ANKHD1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: wolframin ER transmembrane glycoprotein. This gene encodes a transmembrane protein, which is located primarily in the endoplasmic reticulum and ubiquitously expressed with highest levels in brain, pancreas, heart, and insulinoma beta-cell lines. Mutations in this gene are associated with Wolfram syndrome, also called DIDMOAD (Diabetes Insipidus, Diabetes Mellitus, Optic Atrophy, and Deafness), an autosomal recessive disorder. The disease…
- **Diseases (Open Targets)**: Wolfram syndrome (0.851); Wolfram-like syndrome (0.818); type 2 diabetes mellitus (0.764); autosomal dominant nonsyndromic hearing loss (0.749); cataract (0.703)
- **Europe PMC papers**: 3064
- **Why important**: WFS1 is connected to ANKHD1 and encodes an ER transmembrane glycoprotein involved in ER overload response and other homeostatic processes. It is broadly expressed, detected in both breast and skin, strongly associated with Wolfram syndrome and Wolfram-like disease, and represented by a substantial literature base. Its disease biology makes it a particularly informative indicator of ER and metabolic stress.
- **Conclusion**: Established: WFS1 is an ER-homeostasis gene with well-established human disease relevance. Hypothesis: its co-abundance with ANKHD1 and MT-ND3 may reflect coordinated ER-mitochondrial stress handling. The module alone cannot establish that ER stress is active.

#### CHAF1A

- **Related proteins** (co-abundance neighbors): ANKHD1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromatin assembly factor 1 subunit A. Chromatin assembly factor I (CAF1) is a nuclear complex consisting of p50, p60 (CHAF1B; MIM 601245), and p150 (CHAF1A) subunits that assembles histone octamers onto replicating DNA in vitro (Kaufman et al., 1995 [PubMed 7600578]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: craniofacial microsomia (0.446); neurodegenerative disease (0.441); Abnormality of the skeletal system (0.116); neoplasm (0.105); gastric cancer (0.098)
- **Europe PMC papers**: 845
- **Why important**: CHAF1A is connected to ANKHD1 and encodes a core subunit of chromatin assembly factor one, which participates in nucleosome assembly and replication-dependent chromatin assembly. It is tissue enhanced in bone marrow, immune-cell enhanced in plasmacytoid dendritic cells, and associated with progenitor populations. Its literature base is substantial, and its chromatin function provides a possible link to replication or cellular differentiation state.
- **Conclusion**: Established: CHAF1A is a chromatin-assembly factor and may reflect proliferative or progenitor-related cellular activity. Hypothesis: its connection to ANKHD1 may integrate chromatin maintenance with the broader survival and stress state. The HPA evidence does not justify assigning the whole module to bone marrow or immune-cell contamination.

## Module 4

**Tissue pair**: breast and skin  
**Genes (25)**: ANAPC1, CAMSAP2, CCDC43, DDX55, DHX57, GAB2, GIGYF2, GIT1, HEXIM2, KIF1B, LARP7, MED24, OTUD7B, PRRC2B, PRP4K, RICTOR, RNF31, SASH1, SCAF8, SRPK2, STRN, TRIM3, VIRMA, ZFR, ZNF687

### Function

No GO or KEGG term passed global correction, so the module does not support a formally significant pathway assignment. Its annotations nevertheless point toward a nuclear gene expression and RNA-regulatory program. HEXIM2 and LARP7 are components of the seven-SK small nuclear ribonucleoprotein system that restrains P-TEFb and RNA polymerase II transcriptional elongation. PRP4K and SRPK2 connect the module to spliceosome assembly, pre-mRNA splicing, and serine or arginine-rich protein regulation. Other members support RNA processing, transcriptional control, translation, ubiquitin signaling, cytoskeletal organization, and receptor signaling. The network is therefore best interpreted as a mixed regulatory module centered on transcriptional elongation and RNA processing, with additional signaling and cell-structure components, rather than as a single proven metabolic or signaling pathway.

**Cell composition.** The module contains no secreted genes, so it is not a plasma-protein module. Most genes have low tissue specificity, and protein detection is broadly compatible with both breast and skin. However, many genes show cell-type-enhanced HPA patterns, especially for spermatid-related cells, neutrophils, glial or neuronal populations, and muscle-related cells. Several genes are immune-cell enhanced or enriched in neutrophils and related myeloid populations, including GAB2, RICTOR, KIF1B, ZNF687, and OTUD7B, while SASH1 is associated with monocyte populations. This makes shared cell composition, including immune or stromal contamination, a plausible contributor to co-abundance. The evidence does not establish that the module is blood-derived, because most genes have low immune specificity and the module also contains broadly expressed nuclear regulators.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small amount of high-confidence support: HEXIM2 is linked to LARP7, and LARP7 is also linked to DHX57. No STRING functional-enrichment result was reported. These known relationships support a real RNA-regulatory core but leave most module edges unconfirmed by STRING. hu.MAP provides stronger structural context. (hu.MAP huMAP3_05807.1) places SRPK2, PRP4K, and LARP7 in the same large complex; (hu.MAP huMAP3_08467.1) and (hu.MAP huMAP3_09621.1) place SRPK2 and PRP4K in spliceosome-related complexes; (hu.MAP huMAP3_09943.1) links PRP4K and VIRMA within a large RNA-processing complex; and (hu.MAP huMAP3_12897.1) links SASH1 and GAB2 within a signaling-related complex. Because each complex contains only a subset of the module, the co-abundance network is not equivalent to one physical complex. Instead, it appears to combine a known seven-SK or transcriptional component, spliceosome-associated components, and signaling-associated components.

**STRING interactions (score >= 0.7)**: 2 of 300 gene pairs: DHX57–LARP7 (0.74); HEXIM2–LARP7 (0.998)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05807.1 (SRPK2, PRP4K, LARP7; 3/81); huMAP3_08467.1 (SRPK2, PRP4K; 2/22); huMAP3_09621.1 (SRPK2, PRP4K; 2/56); huMAP3_09943.1 (PRP4K, VIRMA; 2/78); huMAP3_12897.1 (SASH1, GAB2; 2/93)

### Novelty

The module may represent a previously unreported cross-tissue co-abundance pattern, but novelty cannot be established from the supplied evidence alone. Most module edges are absent from high-confidence STRING, and only selected subsets are represented in hu.MAP; this may indicate a new co-expression relationship, context dependence, indirect regulation, or technical coupling rather than a new physical interaction. The presence of established seven-SK, spliceosome, RNA-processing, and signaling relationships argues that at least part of the biology is already known. A defensible claim is therefore that the breast-skin conservation and the particular combination of known regulatory components may be novel, pending comparison with published co-expression modules, independent cohorts, and perturbation or protein-interaction experiments.

**Hypothesis.** Hypothesis: the conserved module reflects a shared cellular state in breast and skin in which transcriptional elongation and RNA maturation are coordinated with growth-factor or cytokine signaling and cytoskeletal adaptation. HEXIM2-LARP7 may regulate P-TEFb availability, while PRP4K and SRPK2 may couple that state to spliceosome activity. GAB2 and SASH1 could connect receptor or inflammatory signals to transcriptional and cell-migration responses, with the remaining genes representing downstream RNA, translation, ubiquitin, microtubule, and cell-cycle processes. A competing explanation is that the pattern reflects shared immune or stromal cell abundance rather than coordinated regulation within epithelial cells. Testing these alternatives requires cell-resolved data, directional expression analysis, and perturbation of the proposed regulatory core.

### Important genes

#### HEXIM2

- **Related proteins** (co-abundance neighbors): SASH1 (0.87), STRN (0.87), PRP4K (0.87), LARP7 (0.86), DHX57 (0.86), PRRC2B (0.86), ANAPC1 (0.85), TRIM3 (0.85), CAMSAP2 (0.85), VIRMA (0.84), GIT1 (0.84), CCDC43 (0.83), SCAF8 (0.83), DDX55 (0.83), ZFR (0.82), RNF31 (0.82), SRPK2 (0.82), RICTOR (0.82), GIGYF2 (0.81), ZNF687 (0.81), OTUD7B (0.81), KIF1B (0.81), MED24 (0.81); STRING partners: LARP7 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: HEXIM P-TEFb complex subunit 2. This gene encodes a member of the HEXIM family of proteins. This protein is a component of the 7SK small nuclear ribonucleoprotein. This protein has been found to negatively regulate the kinase activity of the cyclin-dependent kinase P-TEFb, which phosphorylates multiple target proteins to promote transcriptional elongation. This gene is located approximately 7 kb downstream from related family me…
- **Diseases (Open Targets)**: neurodegenerative disease (0.240); aortic stenosis (0.229); intelligence (0.179); femur fracture (0.095); essential hypertension (0.071)
- **Europe PMC papers**: 256
- **Why important**: HEXIM2 is the dominant network hub in the module and has the strongest direct connection to LARP7 in STRING. It is a seven-SK-associated regulator of P-TEFb and transcriptional elongation, with breast and skin protein detection. Its tissue and cell-type associations include muscle and germ-cell contexts, and it has a substantial literature and disease-association record.
- **Conclusion**: Established: HEXIM2 is the strongest network anchor and has a documented role in negative regulation of RNA polymerase II transcriptional elongation through the seven-SK system. Hypothesis: its centrality indicates that the module may track variation in transcriptional elongation, although co-abundance alone does not prove that HEXIM2 drives the other genes.

#### LARP7

- **Related proteins** (co-abundance neighbors): HEXIM2 (0.86); STRING partners: DHX57 (0.74), HEXIM2 (0.998)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in breast, skin
- **hu.MAP 3.0**: huMAP3_05807.1
- **Function (MyGene.info)**: La ribonucleoprotein 7, transcriptional regulator. This gene encodes a protein which is found in the 7SK snRNP (small nuclear ribonucleoprotein). This snRNP complex inhibits a cyclin-dependent kinase, positive transcription elongation factor b, which is required for paused RNA polymerase II at a promoter to begin transcription elongation. A pseudogene of this gene is located on chromosome 3. Alternative splicing results in multiple transcript vari…
- **Diseases (Open Targets)**: microcephalic primordial dwarfism, Alazami type (0.791); Intellectual disability (0.484); hereditary disease (0.415); isolated growth hormone deficiency type IA (0.373); Epileptic encephalopathy (0.340)
- **Europe PMC papers**: 892
- **Why important**: LARP7 has a direct high-confidence STRING relationship with HEXIM2 and another relationship with DHX57, and it is included in hu.MAP complex (hu.MAP huMAP3_05807.1). It is a documented component of seven-SK that restrains P-TEFb-dependent transcriptional elongation, has nuclear localization, and is detected in both relevant tissues.
- **Conclusion**: Established: LARP7 provides the clearest molecular bridge between the network and transcriptional elongation control. Hypothesis: the HEXIM2-LARP7 pair may form the mechanistic core of the conserved module, but the sparse STRING support means that most remaining associations may be indirect.

#### PRP4K

- **Related proteins** (co-abundance neighbors): HEXIM2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Nuclear speckles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05807.1, huMAP3_08467.1, huMAP3_09621.1, huMAP3_09943.1
- **Function (MyGene.info)**: pre-mRNA processing factor kinase PRP4K. Pre-mRNA splicing occurs in two sequential transesterification steps, and the protein encoded by this gene is thought to be involved in pre-mRNA splicing and in signal transduction. This protein belongs to a kinase family that includes serine/arginine-rich protein-specific kinases and cyclin-dependent kinases (CDKs). This protein is regarded as a CDK-like kinase (Clk) with homology to mitogen-acti…
- **Diseases (Open Targets)**: skin neoplasm (0.235); cardiomyopathy (0.227); placenta praevia (0.225); ovarian dysfunction (0.194); glomerulonephritis (0.096)
- **Europe PMC papers**: 126
- **Why important**: PRP4K connects the module to pre-mRNA splicing and is represented in several hu.MAP complexes, including (hu.MAP huMAP3_05807.1), (hu.MAP huMAP3_08467.1), (hu.MAP huMAP3_09621.1), and (hu.MAP huMAP3_09943.1). It is a nuclear-speckle kinase with a role related to spliceosome assembly and has disease associations including skin neoplasm and cardiomyopathy, despite a comparatively limited literature.
- **Conclusion**: Established: PRP4K is a plausible RNA-processing bridge between the seven-SK core and spliceosome-associated complexes. Hypothesis: it may couple changes in transcriptional elongation to alternative splicing in the shared tissue state.

#### SRPK2

- **Related proteins** (co-abundance neighbors): HEXIM2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_05807.1, huMAP3_08467.1, huMAP3_09621.1
- **Function (MyGene.info)**: SRSF protein kinase 2. Enables ATP binding activity; magnesium ion binding activity; and protein serine/threonine kinase activity. Involved in several processes, including nucleic acid metabolic process; peptidyl-serine phosphorylation; and regulation of viral genome replication. Located in chromatin; cytosol; and nuclear lumen. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: COVID-19 (0.404); neurodegenerative disease (0.371); schizophrenia (0.303); skin aging (0.272); smoking cessation (0.268)
- **Europe PMC papers**: 1379
- **Why important**: SRPK2 is a serine or threonine kinase involved in RNA splicing and is present with PRP4K in (hu.MAP huMAP3_08467.1) and (hu.MAP huMAP3_09621.1), as well as with LARP7 in (hu.MAP huMAP3_05807.1). It has substantial literature, broad regulatory relevance, and HPA associations with testis, spermatid populations, and neutrophils.
- **Conclusion**: Established: SRPK2 supplies an additional, independently annotated link to spliceosomal regulation and is supported by multiple hu.MAP contexts. Hypothesis: coordinated SRPK2 and PRP4K activity could explain part of the module's conserved RNA-processing signal, but the module contains no globally significant enrichment proving this interpretation.

#### GAB2

- **Related proteins** (co-abundance neighbors): GIT1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in breast, skin
- **hu.MAP 3.0**: huMAP3_12897.1
- **Function (MyGene.info)**: GRB2 associated binding protein 2. This gene is a member of the GRB2-associated binding protein (GAB) gene family. These proteins contain pleckstrin homology (PH) domain, and bind SHP2 tyrosine phosphatase and GRB2 adapter protein. They act as adapters for transmitting various signals in response to stimuli through cytokine and growth factor receptors, and T- and B-cell antigen receptors. The protein encoded by this gene is the pri…
- **Diseases (Open Targets)**: cancer (0.608); chronic myeloid leukemia (0.541); hair color (0.521); Abnormality of the skeletal system (0.452); smoking initiation (0.399)
- **Europe PMC papers**: 2763
- **Why important**: GAB2 is a signaling adaptor that transmits cytokine, growth-factor, and antigen receptor signals and activates phosphatidylinositol three-kinase or protein kinase B signaling. It is paired with SASH1 in hu.MAP complex (hu.MAP huMAP3_12897.1), has the largest literature volume among the highlighted signaling genes, and shows HPA enrichment in neutrophils, basophils, monocytes, microglia, and other immune-related cell types.
- **Conclusion**: Established: GAB2 provides a credible receptor-signaling and immune-cell interpretation for part of the module. Hypothesis: GAB2 may connect extracellular or inflammatory cues to the nuclear RNA-regulatory core, although its abundance could instead reflect variation in myeloid-cell representation.

#### SASH1

- **Related proteins** (co-abundance neighbors): HEXIM2 (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cytosol; IHC detected in breast, skin
- **hu.MAP 3.0**: huMAP3_12897.1
- **Function (MyGene.info)**: SAM and SH3 domain containing 1. This gene encodes a scaffold protein involved in the TLR4 signaling pathway that may stimulate cytokine production and endothelial cell migration in response to invading pathogens. The encoded protein has also been described as a potential tumor suppressor that may negatively regulate proliferation, apoptosis, and invasion of cancer cells, and reduced expression of this gene has been observed in m…
- **Diseases (Open Targets)**: dyschromatosis universalis hereditaria (0.754); pigmentation defects-palmoplantar keratoderma-skin carcinoma syndrome (0.476); hypothyroidism (0.441); cardiovascular disorder (0.421); glaucoma (0.406)
- **Europe PMC papers**: 848
- **Why important**: SASH1 is paired with GAB2 in (hu.MAP huMAP3_12897.1), is associated with epithelial and endothelial migration, innate immune signaling, angiogenesis, pigmentation abnormalities, and cancer-related biology. It is detected in both breast and skin and shows monocyte-associated HPA patterns, making it informative for both tissue biology and the possible immune or vascular contribution.
- **Conclusion**: Established: SASH1 is a signaling scaffold with relevance to migration, innate immune responses, pigmentation, and cancer biology, and it has a known complex association with GAB2. Hypothesis: SASH1 may help explain why the module is conserved in breast and skin, but the data cannot distinguish epithelial regulation from shared monocyte or endothelial composition.

## Module 5

**Tissue pair**: breast and skin  
**Genes (5)**: ARRB2, LMCD1, MAPK7, MSRA, SMG1

### Function

The module is best interpreted as a coordinated intracellular signaling, stress-response, gene-regulatory, and protein-quality-control program rather than a formally enriched pathway. MAPK7 is the central co-abundance hub and is annotated in MAPK signaling, stress response, proliferation, differentiation, and transcriptional regulation. ARRB2 contributes receptor desensitization and receptor internalization functions. MSRA provides a protein-repair and oxidative-stress component. SMG1 contributes nonsense-mediated mRNA decay, mRNA export, DNA-damage response, and phosphorylation functions. LMCD1 is a LIM-domain transcriptional co-regulator associated with vascular, smooth-muscle, and cardiac regulatory biology. No GO/KEGG term passed global correction, so these annotations support a biologically plausible functional interpretation but do not establish pathway-level enrichment. The sparse star-like network, centered on MAPK7, is more consistent with a coordinated expression or cell-composition signal than with a demonstrated physical complex.

**Cell composition.** This is not a plasma-protein or secreted-protein module: none of the genes is classified as secreted, and the proteins are intracellular or membrane-associated. The module is not uniformly housekeeping-like. HPA profiles show tissue enhancement in bone marrow, lymphoid tissue, kidney, liver, blood vessel, and skeletal muscle, while single-cell enhancement spans immune, stromal, vascular, muscle, epithelial, and neural-related cell types. Immune associations are mixed rather than dominant, including dendritic cells, macrophages, microglia, eosinophils, basophils, and T-reg cells. Therefore, the shared breast-skin signal could reflect common stromal, vascular, muscle-like, epithelial, or immune-associated cell populations, or a shared cellular stress state, rather than circulating plasma contamination. Protein detection in breast and skin is present for most genes with available HPA evidence, but this does not prove that every gene is expressed in the same cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was reported among the module genes, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. The observed co-abundance edges therefore should not be described as established protein-protein interactions or as membership in a known multiprotein complex. The network may capture coordinated regulation, shared cellular composition, indirect biology, or technical co-abundance. Known functions of the individual proteins remain informative, but the module-level connection among them is not supported by the listed interaction resources.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module appears novel as a breast-skin co-abundance configuration because it is not represented by a reported STRING interaction pattern or a hu.MAP complex and has no globally significant GO/KEGG enrichment. However, absence from STRING or hu.MAP alone does not establish biological novelty. The individual genes and their functions are already well established, and the sparse topology could arise from shared expression, cell-type composition, or context-specific regulation. The defensible claim is novelty of the observed cross-tissue co-abundance arrangement, not discovery of previously unknown gene functions or physical interactions.

**Hypothesis.** Hypothesis: the module represents a shared tissue-state program in breast and skin in which MAPK7 integrates receptor and environmental signals, ARRB2 modulates receptor desensitization and internalization, MSRA limits oxidative damage, SMG1 maintains transcript surveillance and damage-responsive phosphorylation, and LMCD1 helps couple signaling to transcriptional or structural programs in vascular, stromal, smooth-muscle, or related cells. A second, nonexclusive hypothesis is that the signal is driven partly by coordinated abundance of several cell populations rather than by regulation within one cell type. These hypotheses require validation with cell-resolved expression, perturbation, and protein-level interaction assays; the co-abundance network does not itself demonstrate causality.

### Important genes

#### MAPK7

- **Related proteins** (co-abundance neighbors): ARRB2 (0.82), MSRA (0.82), SMG1 (0.82), LMCD1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase 7. The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. This kinase is specifically activated by mitogen-activated protein kinase kinase 5 (MAP2K5/MEK5). It is involved in …
- **Diseases (Open Targets)**: self-injurious ideation (0.142); neoplasm (0.117); cancer (0.113); breast cancer (0.112); breast carcinoma (0.111)
- **Europe PMC papers**: 1419
- **Why important**: MAPK7 is the network hub, connecting every other module member in the supplied subgraph. It is a MAP kinase activated by MAP2K5 and is annotated in signal transduction, MAPK cascade biology, stress responses, proliferation, differentiation, transcriptional regulation, and cell-adhesion-related processes. It is detected in both breast and skin and has extensive literature support, with disease links including neoplasm, cancer, breast cancer, and breast carcinoma.
- **Conclusion**: Established: MAPK7 is the strongest candidate for an organizing signaling role because of its central network position and well-supported kinase biology. Hypothesis: MAPK7 may coordinate the other co-abundance patterns in the shared tissue state, but the network does not establish direct molecular interactions or causality.

#### ARRB2

- **Related proteins** (co-abundance neighbors): MAPK7 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: arrestin beta 2. Members of arrestin/beta-arrestin protein family are thought to participate in agonist-mediated desensitization of G-protein-coupled receptors and cause specific dampening of cellular responses to stimuli such as hormones, neurotransmitters, or sensory signals. Arrestin beta 2, like arrestin beta 1, was shown to inhibit beta-adrenergic receptor function in vitro. It is expressed at high levels in …
- **Diseases (Open Targets)**: cancer (0.599); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.503); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2757
- **Why important**: ARRB2 is directly connected to MAPK7 and provides a receptor-proximal regulatory interpretation through GPCR desensitization, receptor internalization, and signal modulation. HPA associates it with bone marrow and lymphoid tissue and with antigen-presenting or macrophage-lineage cell types. It has substantial literature support and disease associations including cancer and several RASopathy or cardiomyopathy-related conditions.
- **Conclusion**: Established: ARRB2 is a recognized regulator of receptor signaling and is biologically relevant to immune-associated cell contexts. Hypothesis: its co-abundance with MAPK7 may indicate coordinated control of receptor responsiveness, although no direct interaction is reported here.

#### MSRA

- **Related proteins** (co-abundance neighbors): MAPK7 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in breast
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine sulfoxide reductase A. This gene encodes a ubiquitous and highly conserved protein that carries out the enzymatic reduction of methionine sulfoxide to methionine. Human and animal studies have shown the highest levels of expression in kidney and nervous tissue. The protein functions in the repair of oxidatively damaged proteins to restore biological activity. Alternative splicing results in multiple transcript variants.…
- **Diseases (Open Targets)**: hypertensive disorder (0.487); alcohol drinking (0.480); type 2 diabetes mellitus (0.467); bipolar disorder (0.446); Irritability (0.429)
- **Europe PMC papers**: 8330
- **Why important**: MSRA is connected to the MAPK7 hub and contributes a distinct oxidative-stress and protein-repair function by reducing methionine sulfoxide. It is described as ubiquitous and highly conserved, with tissue emphasis in kidney and nervous tissue, and is associated in HPA with eosinophils and neural cell types. It has the largest literature footprint among the module genes and disease associations involving hypertension, type two diabetes, alcohol-related behavior, and psychiatric traits.
- **Conclusion**: Established: MSRA is a credible marker of protein redox maintenance and oxidative-stress handling. Hypothesis: its coupling to MAPK7 may reflect a shared stress-adaptation program in breast and skin, but the module data do not prove that oxidative damage drives the co-abundance pattern.

#### SMG1

- **Related proteins** (co-abundance neighbors): MAPK7 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SMG1 nonsense mediated mRNA decay associated PI3K related kinase. This gene encodes a protein involved in nonsense-mediated mRNA decay (NMD) as part of the mRNA surveillance complex. The protein has kinase activity and is thought to function in NMD by phosphorylating the regulator of nonsense transcripts 1 protein. Alternatively spliced transcript variants have been described, but their full-length nature has yet to be determined. [provided by RefSeq, Mar 2013].
- **Diseases (Open Targets)**: alcohol drinking (0.251); stroke disorder (0.251); contracture (0.158); neoplasm (0.107); refractive error (0.098)
- **Europe PMC papers**: 1969
- **Why important**: SMG1 is connected to MAPK7 and supplies a transcript-surveillance and genome-integrity component through nonsense-mediated decay, mRNA export, DNA-damage response, telomere-related regulation, and serine phosphorylation. HPA places it in myonuclei and thymic myoid cells and associates it with basophils. It has a substantial literature base and disease associations including neoplasm and stroke-related disease.
- **Conclusion**: Established: SMG1 is a multifunctional kinase involved in RNA quality control and damage responses. Hypothesis: its co-abundance with MAPK7 could indicate a broader stress-responsive state linking signaling to RNA and genome surveillance, but no module-level mechanistic link is demonstrated.

#### LMCD1

- **Related proteins** (co-abundance neighbors): MAPK7 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm, Plasma membrane; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LIM and cysteine rich domains 1. This gene encodes a member of the LIM-domain family of zinc finger proteins. The encoded protein contains an N-terminal cysteine-rich domain and two C-terminal LIM domains. The presence of LIM domains suggests involvement in protein-protein interactions. The protein may act as a co-regulator of transcription along with other transcription factors. Alternate splicing results in multiple transcript …
- **Diseases (Open Targets)**: mitral valve prolapse (0.385); refractive error (0.377); Varicose veins (0.362); ovarian neoplasm (0.334); placenta praevia (0.332)
- **Europe PMC papers**: 694
- **Why important**: LMCD1 is connected to MAPK7 and is a LIM-domain protein with potential transcriptional co-regulatory and protein-interaction functions. Its HPA profile emphasizes blood vessel and skeletal muscle, with single-cell associations spanning stromal, pericyte, smooth-muscle, and muscle populations. It is detected in both breast and skin and has disease associations involving mitral valve prolapse, varicose veins, refractive error, ovarian neoplasm, and placenta praevia. Its literature volume is more limited than that of the other selected genes, which makes it useful as a potentially under-characterized tissue-context marker.
- **Conclusion**: Established: LMCD1 is linked to transcriptional regulation and vascular or muscle-related biology. Hypothesis: LMCD1 may connect MAPK7 signaling to stromal, vascular, or contractile cell states shared by breast and skin, but this proposed role requires direct cell-type and perturbation studies.

## Module 6

**Tissue pair**: breast and skin  
**Genes (14)**: BLOC1S3, CABP7, CCDC137, PRKCA, LDAH, MIB1, NFRKB, RAI1, CRCP, SCAF11, VIPAS39, SUGP1, ZC3H13, ZGPAT

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically established pathway-level function from enrichment. Its genes instead suggest a heterogeneous nuclear and intracellular regulatory program: RNA binding, RNA processing and splicing, mRNA methylation, chromatin and DNA-repair regulation, transcriptional control, Notch-related ubiquitination, calcium-linked signaling, vesicle and lysosomal trafficking, melanosome biology, and lipid-droplet regulation. The co-abundance network is internally connected, especially around CCDC137, but this connectivity does not establish a single biochemical pathway. The most defensible interpretation is a shared cellular-state module involving gene-expression regulation together with membrane-organelle and signaling processes, rather than a defined canonical pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also unlikely to be driven primarily by blood contamination or blood-cell abundance, because the genes have low immune-cell specificity or are not detected in immune cells, and no blood-cell type is repeatedly enriched. Most genes have low tissue specificity, while several show cell-type-enhanced expression across diverse non-blood cell types, including neural, cardiac, reproductive, hepatic, epithelial, and glial populations. Protein detection is present for much of the module in both breast and skin, although individual genes differ. Thus, the shared signal is more consistent with broadly present cellular biology, or with shared non-immune cell states, than with a breast- or skin-specific secretory or hematologic component.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no hu.MAP complex containing multiple module members. Therefore, the observed co-abundance edges are not corroborated by the supplied external protein-interaction or complex resources. This argues against interpreting the module as a known physical complex. It may represent coordinated expression, indirect regulation, shared cell-state composition, or context-dependent interactions that are absent from these databases; database absence is not evidence that the co-abundance relationships are biologically meaningless.

**STRING interactions (score >= 0.7)**: 0 of 91 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new co-abundance observation, but a claim of a new biological mechanism is not justified. Supporting reasons for caution are the absence of globally significant GO/KEGG enrichment, the absence of supplementary STRING enrichment, and the lack of STRING and hu.MAP support. Conversely, these negative database results do not prove novelty, because the genes have established functions and several have substantial disease and literature annotation. The appropriate conclusion is that the breast-skin co-abundance pattern appears insufficiently characterized as a unified module and requires independent replication, cell-composition analysis, and perturbational or biochemical validation before being called novel.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial or stromal cellular state in breast and skin in which transcriptional and RNA-processing regulation is coordinated with signaling, vesicle-organelle trafficking, and lipid handling. A possible organizing axis is CCDC137-linked coordination of nuclear regulators with PRKCA- and VIPAS39-associated signaling or trafficking, while ZC3H13 and NFRKB connect RNA or chromatin regulation. This is a mechanistic hypothesis only; the lack of globally significant enrichment and external interaction support means that the proposed links are not established by this dataset.

### Important genes

#### CCDC137

- **Related proteins** (co-abundance neighbors): CABP7 (0.86), ZGPAT (0.82), PRKCA (0.82), RAI1 (0.81), LDAH (0.80), ZC3H13 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coiled-coil domain containing 137. Enables RNA binding activity. Located in chromosome and fibrillar center. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.105); myopia (0.100); neoplasm (0.094); colorectal carcinoma (0.075); urinary bladder carcinoma (0.074)
- **Europe PMC papers**: 148
- **Why important**: CCDC137 is the central network connector in the supplied subgraph, linking CABP7, ZGPAT, PRKCA, RAI1, LDAH, and ZC3H13. Its annotation supports RNA binding and a nucleolar or fibrillar-center location, while its HPA profile is broadly distributed and detected in skin. It therefore provides the strongest network-based anchor for a coordinated regulatory-state interpretation, despite having no STRING or hu.MAP support and relatively limited functional characterization compared with the better-known genes.
- **Conclusion**: Established: CCDC137 is the principal co-abundance connector and is annotated as an RNA-binding, nucleolar protein. Hypothesis: it may organize or mark the shared regulatory state. Its causal role is unproven, and the network position alone does not demonstrate physical interaction.

#### ZC3H13

- **Related proteins** (co-abundance neighbors): MIB1 (0.82), NFRKB (0.81), CCDC137 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing 13. Enables RNA binding activity. Involved in mRNA methylation. Located in nuclear speck. Part of RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.547); type 2 diabetes mellitus (0.332); liver disorder (0.332); renal dialysis (0.290); poisoning (0.213)
- **Europe PMC papers**: 2616
- **Why important**: ZC3H13 connects CCDC137 with NFRKB and MIB1 and is annotated as an RNA-binding component of the RNA N6-methyladenosine methyltransferase complex. Its additional annotations include mRNA processing and regulation of stem-cell population maintenance, and it has extensive literature and disease-association coverage. This makes it a strong candidate for linking transcript regulation to the broader module.
- **Conclusion**: Established: ZC3H13 participates in mRNA methylation and RNA processing and occupies a bridging position in the module. Hypothesis: altered RNA modification or RNA-state control may contribute to the shared breast-skin signal. The module does not establish that ZC3H13 drives the co-abundance pattern.

#### NFRKB

- **Related proteins** (co-abundance neighbors): SCAF11 (0.83), SUGP1 (0.82), ZC3H13 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear factor related to kappaB binding protein. Enables protease binding activity. Predicted to be involved in DNA recombination and DNA repair. Located in nucleoplasm. Colocalizes with Ino80 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); gastric cancer (0.076); ventricular fibrillation (0.047); male reproductive organ cancer (0.045); bronchial disorder (0.044)
- **Europe PMC papers**: 376
- **Why important**: NFRKB connects SCAF11, SUGP1, and ZC3H13 and is annotated in relation to DNA repair, DNA replication regulation, telomere maintenance, chromatin remodeling, and chromosome organization. Its nucleoplasmic localization and disease associations make it a plausible nuclear-regulatory anchor, while its literature base is substantial.
- **Conclusion**: Established: NFRKB has documented or predicted roles in nuclear genome maintenance and chromatin-related regulation and is positioned at a small RNA-processing or nuclear-regulatory branch of the network. Hypothesis: the module may capture coordinated genome-maintenance and transcript-processing activity. Direct involvement in this breast-skin module remains untested.

#### PRKCA

- **Related proteins** (co-abundance neighbors): CCDC137 (0.82), VIPAS39 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C alpha. Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and the second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC family members also serve as major receptors for phorbol esters, a class of tumor promoters. Each mem…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.554); hypertrophic cardiomyopathy (0.506); mast cell leukemia (0.475); systemic mastocytosis (0.471); heart failure (0.462)
- **Europe PMC papers**: 5462
- **Why important**: PRKCA is a well-studied signaling kinase connected in the module to CCDC137 and VIPAS39. Its annotation includes calcium- and diacylglycerol-responsive protein phosphorylation, reactive-oxygen responses, desmosome assembly, endothelial proliferation, and chromatin-related processes. It has extensive literature and multiple disease associations, providing a biologically credible signaling anchor that could connect cellular state to adhesion or stress responses.
- **Conclusion**: Established: PRKCA is a multifunctional serine-threonine kinase with roles in signaling, phosphorylation, and desmosome biology. Hypothesis: PRKCA-dependent signaling could couple the nuclear and trafficking components of the module. The co-abundance data do not show that PRKCA directly regulates the other module genes.

#### VIPAS39

- **Related proteins** (co-abundance neighbors): BLOC1S3 (0.83), PRKCA (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS33B interacting protein, apical-basolateral polarity regulator, spe-39 homolog. This gene encodes a protein involved in the sorting of lysosomal proteins. Mutations in this gene are associated with ARCS2 (arthrogryposis, renal dysfunction, and cholestasis-2). Alternative splicing results in multiple transcript variants.[provided by RefSeq, Jul 2010]
- **Diseases (Open Targets)**: arthrogryposis-renal dysfunction-cholestasis syndrome (0.828); arthrogryposis, renal dysfunction, and cholestasis 1 (0.425); hereditary disease (0.193); atrial fibrillation (0.028); neoplasm (0.021)
- **Europe PMC papers**: 190
- **Why important**: VIPAS39 links PRKCA with BLOC1S3 and is annotated in intracellular, vacuolar, endosome-to-lysosome, and phagosome-lysosome transport, as well as collagen metabolism. Its established association with arthrogryposis-renal dysfunction-cholestasis syndrome gives it a clear disease and organelle-trafficking context. It is a useful complementary anchor because it connects the signaling branch to vesicle and lysosomal biology rather than to nuclear regulation.
- **Conclusion**: Established: VIPAS39 participates in intracellular protein and lysosomal trafficking and is disease-associated. Hypothesis: organelle trafficking or epithelial polarity may be part of the shared cellular state represented by the module. A direct functional relationship with PRKCA or BLOC1S3 in breast and skin is not established here.

## Module 7

**Tissue pair**: breast and skin  
**Genes (5)**: BPTF, CENPH, TRIP10, COX19, HELLS

### Function

No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Therefore, the module does not support a statistically established single pathway or biological process. Its genes span mitochondrial complex IV assembly and intracellular copper handling through COX19, chromatin remodeling and transcriptional regulation through BPTF, kinetochore organization and chromosome segregation through CENPH, DNA repair and DNA-methylation-dependent heterochromatin through HELLS, and actin-cytoskeleton, endocytic, and signal-transduction processes through TRIP10. The co-abundance graph is a connected chain linking these functional areas, but the absent enrichment means that a unifying pathway should be treated as interpretive rather than demonstrated.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its genes is annotated as secreted, and all are intracellular or vesicular. Most genes have low immune-cell specificity, although TRIP10 is immune-cell enriched in plasmacytoid dendritic cells. HPA profiles show tissue enhancement in bone marrow, testis, skeletal muscle, and lymphoid tissue, with cell-type enrichment involving spermatogenic, erythrocyte-progenitor, megakaryocyte-progenitor, monocyte-progenitor, trophoblast, and esophageal cell populations. This mixed pattern is not typical of a single blood-cell program, but it leaves open the possibility that the breast and skin signal reflects a shared proliferative or stromal-associated cell state, or shared representation of particular cell types, rather than a breast-skin-specific biochemical pathway. Protein detection is broader in skin than breast, while COX19, BPTF, and TRIP10 are detected in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship is present among the module genes, and no STRING functional-enrichment term is reported. No hu.MAP complex contains multiple module members. Thus, the co-abundance edges are not supported here as already established physical interactions or membership in a known multiprotein complex. The network may represent coordinated expression, indirect regulation, shared cellular state, or technical and compositional covariance rather than direct molecular binding. The absence of STRING and hu.MAP support weakens a direct-complex interpretation but does not invalidate the reproducible co-abundance pattern.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel co-abundance association because the module has no recorded high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO or KEGG enrichment. Those absences do not by themselves prove biological novelty: the genes are individually well studied, and their functions are already established in several cellular systems. The strongest defensible claim is that their coordinated abundance in the breast-skin comparison is not explained by a recognized interaction complex or canonical enriched pathway in the supplied resources. Replication in independent cohorts, adjustment for cell composition and proliferation, and experimental testing would be required before calling it a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program in breast and skin that couples mitochondrial capacity, chromatin and centromere control, DNA maintenance, and cytoskeletal or membrane remodeling. In this model, COX19 may represent respiratory and mitochondrial support, BPTF and HELLS may represent transcriptional and epigenetic control, CENPH may mark chromosome segregation during proliferation, and TRIP10 may connect the state to actin remodeling and membrane trafficking. The tissue and cell-type annotations are compatible with a proliferative or remodeling state, but the absence of global enrichment and known interaction support makes this a hypothesis rather than an established pathway.

### Important genes

#### COX19

- **Related proteins** (co-abundance neighbors): BPTF (0.87), TRIP10 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome c oxidase assembly factor COX19. COX19 encodes a cytochrome c oxidase (COX)-assembly protein. The S. cerevisiae Cox19 protein may play a role in metal transport to the mitochondrial intermembrane space and assembly of complex IV of the mitochondrial respiratory chain (Sacconi et al., 2005 [PubMed 16212937]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.492); inflammatory bowel disease (0.211); metabolic syndrome (0.073); chronic obstructive pulmonary disease (0.057); Crohn disease (0.040)
- **Europe PMC papers**: 377
- **Why important**: COX19 is the highest-positioned bridge on one side of the co-abundance chain and connects BPTF with TRIP10. Its established annotation places it in cytochrome c oxidase assembly, mitochondrial respiratory-chain complex maturation, protein folding, and intracellular copper homeostasis. It is detected in both breast and skin, has low tissue and cell-type specificity, and has disease associations including neurodegenerative, inflammatory bowel, metabolic, pulmonary, and Crohn disease categories. Its literature footprint is more limited than those of BPTF and HELLS, making its presence useful for prioritizing a potentially underinterpreted mitochondrial component.
- **Conclusion**: Established evidence supports COX19 as a mitochondrial complex-assembly factor and as a network bridge in this module. It is not established that COX19 functionally links mitochondrial respiration to the chromatin or cytoskeletal genes here. That bridging role is a hypothesis suggested by co-abundance, not a demonstrated physical interaction.

#### BPTF

- **Related proteins** (co-abundance neighbors): COX19 (0.87), CENPH (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: bromodomain PHD finger transcription factor. This gene was identified by the reactivity of its encoded protein to a monoclonal antibody prepared against brain homogenates from patients with Alzheimer's disease. Analysis of the original protein (fetal Alz-50 reactive clone 1, or FAC1), identified as an 810 aa protein containing a DNA-binding domain and a zinc finger motif, suggested it might play a role in the regulation of transcription. Hig…
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and distal limb anomalies (0.788); Intellectual disability (0.539); hereditary disease (0.538); neurodegenerative disease (0.536); Global developmental delay (0.507)
- **Europe PMC papers**: 1741
- **Why important**: BPTF occupies a central position in the chain, linking COX19 to CENPH. Its established functions include chromatin remodeling and regulation of transcription, with additional annotations involving brain development and negative regulation of transcription. It is detected in both breast and skin and has the largest literature footprint among the module genes, as well as disease associations involving neurodevelopmental disorders, intellectual disability, developmental delay, and neurodegeneration. Its central network position and broad regulatory function make it a strong candidate for coordinating a cell-state program.
- **Conclusion**: Established evidence supports BPTF as a chromatin and transcriptional regulator with important developmental and disease relevance. It is plausible that BPTF contributes to coordinated expression of other module genes, but this module does not establish direct regulation or a breast-skin-specific BPTF mechanism.

#### CENPH

- **Related proteins** (co-abundance neighbors): HELLS (0.87), BPTF (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli rim; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: centromere protein H. Centromere and kinetochore proteins play a critical role in centromere structure, kinetochore formation, and sister chromatid separation. The protein encoded by this gene colocalizes with inner kinetochore plate proteins CENP-A and CENP-C in both interphase and metaphase. It localizes outside of centromeric heterochromatin, where CENP-B is localized, and inside the kinetochore corona, where CENP-E…
- **Diseases (Open Targets)**: neurodegenerative disease (0.519); Abnormality of the skeletal system (0.142); sensorineural hearing loss disorder (0.134); hearing loss disorder (0.134); cardiovascular disorder (0.132)
- **Europe PMC papers**: 415
- **Why important**: CENPH is an internal connector between BPTF and HELLS and is annotated to kinetochore assembly, kinetochore organization, mitotic spindle organization, and chromosome segregation. HPA indicates tissue enhancement in bone marrow and testis and cell-type enhancement in differentiating spermatogonia, early primary spermatocytes, erythrocyte progenitors, extravillous trophoblasts, and megakaryocyte progenitors. It is detected in skin but not breast, which may indicate tissue-specific abundance or sampling-related differences. Its disease associations include neurodegenerative, skeletal, hearing, and cardiovascular categories.
- **Conclusion**: Established evidence supports CENPH as a centromere and kinetochore component associated with chromosome segregation. Its expression pattern is compatible with proliferative or progenitor-rich cellular contexts. A role as the proliferative anchor of this breast-skin module remains a hypothesis because no enriched cell-cycle term or independent interaction evidence is supplied.

#### HELLS

- **Related proteins** (co-abundance neighbors): CENPH (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: helicase, lymphoid specific. This gene encodes a lymphoid-specific helicase. Other helicases function in processes involving DNA strand separation, including replication, repair, recombination, and transcription. This protein is thought to be involved with cellular proliferation and may play a role in leukemogenesis. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSe…
- **Diseases (Open Targets)**: immunodeficiency-centromeric instability-facial anomalies syndrome (0.724); neurodegenerative disease (0.319); hereditary disease (0.195); hepatocellular carcinoma (0.102); cancer (0.102)
- **Europe PMC papers**: 1652
- **Why important**: HELLS forms the other terminal connection from CENPH and has a strong established relationship to DNA maintenance and epigenetic regulation. Its annotations include homologous-recombination repair, double-strand-break repair, DNA-methylation-dependent constitutive heterochromatin, pericentric heterochromatin, and methylation-linked gene repression. HPA shows enhancement in lymphoid tissue and several progenitor populations, including spermatogenic and hematopoietic progenitors. HELLS has a substantial literature footprint and disease associations including immunodeficiency-centromeric instability-facial anomalies syndrome, neurodegeneration, hepatocellular carcinoma, and cancer.
- **Conclusion**: Established evidence supports HELLS as a chromatin-remodeling and genome-maintenance factor with clear disease relevance. Its adjacency to CENPH makes a shared proliferation or chromosome-maintenance state plausible, but the module does not prove that HELLS directly controls CENPH or that their co-abundance reflects a single repair pathway.

#### TRIP10

- **Related proteins** (co-abundance neighbors): COX19 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enriched; location Vesicles; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thyroid hormone receptor interactor 10. Enables identical protein binding activity. Predicted to be involved in actin cytoskeleton organization; endocytosis; and signal transduction. Located in nucleoplasm. Biomarker of Huntington's disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); auditory system disorder (0.219); neoplasm (0.105); colorectal carcinoma (0.084); nasopharyngeal carcinoma (0.076)
- **Europe PMC papers**: 516
- **Why important**: TRIP10 is the terminal gene on the cytoskeletal side of the chain and connects to COX19. Its established annotations include cell communication, signal transduction, actin-cytoskeleton organization, plasma-membrane tubulation, and endocytosis. HPA shows tissue enhancement in skeletal muscle, cell-type enrichment in esophageal apical cells, and immune-cell enrichment in plasmacytoid dendritic cells; it is detected in both breast and skin. It has disease associations involving neurodegeneration, auditory disorders, neoplasia, colorectal carcinoma, and nasopharyngeal carcinoma.
- **Conclusion**: Established evidence supports TRIP10 as a membrane, cytoskeletal, and signaling regulator. Its position suggests that the module may include a remodeling or trafficking component, but the connection between TRIP10 and the mitochondrial or chromatin genes is not established by STRING, hu.MAP, or enrichment analysis.

## Module 8

**Tissue pair**: breast and skin  
**Genes (22)**: CAMSAP1, CTNNBIP1, CHTF18, CTR9, EXOC7, GEMIN8, KLHL7, LARP4, NBAS, NELFA, NUP188, ORC3, PIK3C2A, PSME4, SMC5, SMARCD1, GTF2H3, GTF3C2, THOC1, TTF1, TXNL4A, UBE4B

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway annotation from those analyses. Its gene annotations nevertheless point to a predominantly nuclear and intracellular regulatory program involving chromatin remodeling, transcriptional regulation and elongation, RNA processing and export, DNA replication and repair, proteasomal quality control, and selected membrane-trafficking functions. The supplementary STRING categories for protein-containing complexes and nuclear localization (STRING COMPARTMENTS Protein-containing complex; within-query FDR = 0.0069), (STRING Keyword Nucleus; within-query FDR = 0.01), and (STRING Component Protein-containing complex; within-query FDR = 0.0383) are consistent with this interpretation but are not global enrichment evidence. The co-abundance network is centered on KLHL7, with many weaker links radiating from that gene, suggesting a coordinated expression program rather than a single well-defined biochemical complex.

**Cell composition.** The module is predominantly composed of broadly expressed intracellular proteins rather than plasma or secreted proteins. HPA reports no secreted genes, generally low tissue specificity, and generally low immune-cell specificity. Protein detection is widespread in both breast and skin, supporting the existence of the module in both tissues. The module therefore does not strongly resemble a blood-derived or secreted-protein signature. A few genes show tissue or cell-type enhancement, including CTNNBIP1 in skin and esophageal cell populations, KLHL7 in heart muscle and several reproductive cell types, CAMSAP1 in retinal and epithelial populations, and PSME4 in skeletal muscle. These selective signals may reflect contributions from shared structural or proliferative cell populations, but the overall composition is more consistent with a broadly expressed cellular maintenance program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest known STRING relationship is the CTR9–NELFA interaction, which provides direct external support for a transcription-related connection within the module. The STRING supplementary categories also place many module genes in nuclear or protein-containing-complex annotations (STRING COMPARTMENTS Protein-containing complex; within-query FDR = 0.0069), (STRING Keyword Nucleus; within-query FDR = 0.01), and (STRING Component Protein-containing complex; within-query FDR = 0.0383), but these are supplementary within-query results and should not be interpreted as globally corrected enrichment. hu.MAP identifies TXNL4A and GEMIN8 together in two spliceosome- and SMN-related complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). This supports a real connection to spliceosomal snRNP assembly and pre-mRNA splicing, although the module contains only a small subset of the much larger complexes. Most other module genes have no listed STRING partner and no listed hu.MAP complex, so the co-abundance edges should not be equated with established physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 231 gene pairs: CTR9–NELFA (0.935)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Protein-containing complex (FDR = 0.0069, 20 genes); Keyword Nucleus (FDR = 0.01, 18 genes); Component Protein-containing complex (FDR = 0.0383, 19 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06511.1 (TXNL4A, GEMIN8; 2/79); huMAP3_08980.1 (TXNL4A, GEMIN8; 2/97)

### Novelty

This appears more plausibly to be a new tissue-shared co-abundance pattern than a newly discovered molecular complex. Its conservation across breast and skin, the coherent intracellular annotations, and the central position of KLHL7 support biological reproducibility. However, the absence of a globally significant GO or KEGG term, the sparse known physical-interaction support, and the limited overlap with hu.MAP complexes prevent a strong claim that it represents a new pathway. Absence from STRING or hu.MAP alone cannot establish novelty. The most defensible conclusion is that the module may capture a previously uncharacterized coordination of broadly expressed nuclear, RNA-processing, genome-maintenance, and proteostasis genes, requiring independent replication and perturbation experiments.

**Hypothesis.** Hypothesis: the module reflects a shared cellular homeostasis program in breast and skin cells that coordinates nuclear gene regulation and RNA maturation with genome maintenance and protein quality control. KLHL7 may act as a co-abundance hub linking proteostasis-related activity to transcriptional, chromatin, replication, trafficking, and cytoskeletal components. The CTR9–NELFA relationship and the TXNL4A–GEMIN8 complex membership suggest that transcriptional elongation and spliceosomal assembly may be mechanistically connected within this program, while SMARCD1 and TTF1 could connect chromatin or transcriptional regulation to nucleolar and genome-maintenance functions. This is a hypothesis based on co-abundance and annotations, not proof of direct physical cooperation or causality.

### Important genes

#### KLHL7

- **Related proteins** (co-abundance neighbors): EXOC7 (0.92), ORC3 (0.86), NBAS (0.84), SMARCD1 (0.84), THOC1 (0.83), UBE4B (0.83), PIK3C2A (0.83), CHTF18 (0.82), NELFA (0.82), GTF3C2 (0.82), CTR9 (0.81), PSME4 (0.80), NUP188 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: kelch like family member 7. This gene encodes a BTB-Kelch-related protein. The encoded protein may be involved in protein degradation. Mutations in this gene have been associated with retinitis pigmentosa 42. [provided by RefSeq, Feb 2010].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.773); cold-induced sweating syndrome (0.755); inherited retinal dystrophy (0.503); Cold-induced sweating syndrome 1 (0.478); hereditary disease (0.468)
- **Europe PMC papers**: 369
- **Why important**: KLHL7 is the dominant network hub, connecting to many module members with relatively strong co-abundance links. Its BTB-Kelch-related protein function and annotations involving ubiquitination and proteasome-mediated protein catabolism provide a plausible proteostasis component. It is detected in both breast and skin, while its disease associations include retinitis pigmentosa and related inherited retinal disorders. Its literature volume is substantial, making it a well-characterized anchor for interpreting a less well-connected module.
- **Conclusion**: Established evidence supports KLHL7 as the principal co-abundance hub with a role related to protein degradation and a documented retinal-disease association. It is not established that KLHL7 physically organizes the other module proteins. A possible role as a regulatory bridge between proteostasis and nuclear maintenance is therefore a hypothesis.

#### SMARCD1

- **Related proteins** (co-abundance neighbors): CAMSAP1 (0.87), KLHL7 (0.84), GTF2H3 (0.82), GEMIN8 (0.81), TTF1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SWI/SNF related BAF chromatin remodeling complex subunit D1. The protein encoded by this gene is a member of the SWI/SNF family of proteins, whose members display helicase and ATPase activities and which are thought to regulate transcription of certain genes by altering the chromatin structure around those genes. The encoded protein is part of the large ATP-dependent chromatin remodeling complex SNF/SWI and has sequence similarity to the yeast Swp73 protein…
- **Diseases (Open Targets)**: Coffin-Siris syndrome 11 (0.736); syndromic intellectual disability (0.416); Intellectual disability (0.372); Coffin-Siris syndrome (0.371); Global developmental delay (0.370)
- **Europe PMC papers**: 1063
- **Why important**: SMARCD1 occupies a connecting position between KLHL7 and several genes involved in nuclear or structural functions, including GTF2H3, GEMIN8, and TTF1. It is a component of the ATP-dependent SWI/SNF chromatin-remodeling system and is annotated for transcriptional regulation, chromatin remodeling, and cell-proliferation control. It has a strong literature base and disease associations including Coffin-Siris syndrome and intellectual disability.
- **Conclusion**: Established evidence supports SMARCD1 as a chromatin-remodeling and transcriptional regulator that could explain part of the module's nuclear character. Its participation in the breast–skin co-abundance program and any direct functional interaction with KLHL7 or the other module genes remain unproven.

#### TTF1

- **Related proteins** (co-abundance neighbors): SMC5 (0.81), TXNL4A (0.81), SMARCD1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transcription termination factor 1. This gene encodes a transcription termination factor that is localized to the nucleolus and plays a critical role in ribosomal gene transcription. The encoded protein mediates the termination of RNA polymerase I transcription by binding to Sal box terminator elements downstream of pre-rRNA coding regions. Alternatively spliced transcript variants encoding multiple isoforms have been observed for t…
- **Diseases (Open Targets)**: neurodegenerative disease (0.299); Precordial pain (0.206); hypothyroidism, congenital, nongoitrous, 2 (0.118); neoplasm (0.114); small cell lung carcinoma (0.109)
- **Europe PMC papers**: 4088
- **Why important**: TTF1 links SMC5, TXNL4A, and SMARCD1 in the module and is localized to the nucleolar fibrillar center. Its established function in RNA polymerase I transcription termination gives the module a nucleolar and ribosomal-gene regulatory dimension. It also has the largest literature volume among the selected genes and documented links to developmental and neoplastic disease contexts.
- **Conclusion**: Established evidence supports TTF1 as a nucleolar transcription-termination factor and a meaningful connector between RNA processing, transcriptional regulation, and genome-maintenance genes. The module does not establish that altered TTF1 activity drives the shared tissue pattern; that connection remains hypothetical.

#### TXNL4A

- **Related proteins** (co-abundance neighbors): TTF1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: thioredoxin like 4A. The protein encoded by this gene is a member of the U5 small ribonucleoprotein particle (snRNP), and is involved in pre-mRNA splicing. This protein contains a thioredoxin-like fold and it is expected to interact with multiple proteins. Protein-protein interactions have been observed with the polyglutamine tract-binding protein 1 (PQBP1). Mutations in both the coding region and promoter region of t…
- **Diseases (Open Targets)**: choanal atresia-hearing loss-cardiac defects-craniofacial dysmorphism syndrome (0.765); cleft palate (0.370); dengue disease (0.370); hereditary disease (0.176); neurodegenerative disease (0.167)
- **Europe PMC papers**: 292
- **Why important**: TXNL4A is linked to TTF1 in the co-abundance network and is independently supported by hu.MAP complexes (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1) through its partnership with GEMIN8. It is a U5 snRNP component involved in spliceosomal assembly and pre-mRNA splicing, and it has a documented association with Burn-McKeown syndrome and craniofacial developmental disorders. Its complex membership gives it stronger mechanistic support than many of the isolated module genes.
- **Conclusion**: Established evidence supports TXNL4A as a spliceosomal and snRNP-associated protein, with corroborating hu.MAP complex membership. It is reasonable to propose that RNA-splicing capacity contributes to the module, but the tissue-shared co-abundance pattern does not prove that TXNL4A controls the other genes.

#### CTR9

- **Related proteins** (co-abundance neighbors): KLHL7 (0.81); STRING partners: NELFA (0.935)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CTR9 component of Paf1/RNA polymerase II complex. The protein encoded by this gene is a component of the PAF1 complex, which associates with RNA polymerase II and functions in transcriptional regulation and elongation. This complex also plays a role in the modification of histones. [provided by RefSeq, Oct 2016].
- **Diseases (Open Targets)**: CTR9-related neurodevelopmental disorder (0.615); neurodegenerative disease (0.518); Wilms tumor (0.486); hereditary disease (0.477); Nephroblastoma (0.465)
- **Europe PMC papers**: 882
- **Why important**: CTR9 is a component of the PAF1 RNA polymerase II complex and is annotated for transcriptional regulation, elongation, chromatin organization, and histone-related regulation. It has a known high-confidence STRING relationship with NELFA, the only explicitly listed strong STRING interaction among module members. CTR9 also has substantial literature and disease associations including CTR9-related neurodevelopmental disorder and Wilms tumor.
- **Conclusion**: Established evidence supports CTR9 as a transcription-elongation and chromatin-regulatory factor, and the CTR9–NELFA relationship is an externally supported interaction within the module. Its role as a central driver of the breast–skin module is not established because its network degree within the co-abundance graph is limited.

## Module 9

**Tissue pair**: breast and skin  
**Genes (14)**: CDKN2AIP, EMC10, ISY1, MAD1L1, MED6, RAD18, ROBO1, POLR2A, POLR2B, SYNRG, TCERG1, TP53BP1, UTRN, YEATS2

### Function

This is a conserved nuclear regulatory module rather than a narrowly defined pathway module. Its strongest functional themes are RNA polymerase II transcription and transcriptional regulation, chromatin-associated control, DNA-damage response and repair, mitotic surveillance, and pre-mRNA processing. These themes are supported by the individual gene annotations and by the network arrangement linking YEATS2 with POLR2A, POLR2B, TP53BP1, MAD1L1, UTRN, and CDKN2AIP, together with a separate RAD18-centered branch. However, no GO or KEGG term passed global multiple-testing correction, so there is no globally significant GO/KEGG enrichment claim for this module. The module may therefore represent coordinated expression of several related nuclear maintenance processes rather than a single canonical pathway.

**Cell composition.** The module is predominantly composed of broadly expressed, intracellular or membrane-associated proteins, with low tissue specificity for most genes. HPA does not support a predominantly plasma-protein, secreted-protein, or blood-cell-enriched composition: only EMC10 is annotated as secreted to blood, most genes have low immune-cell specificity, and only UTRN is immune-cell enhanced. Protein detection is broadly compatible with both breast and skin. The cell-type annotations are heterogeneous, including epithelial, neural, muscle-associated, and other specialized cell types, so the shared signal is more consistent with a broadly maintained cellular program or shared resident-cell expression than with a simple blood contamination signature. EMC10 and UTRN could reflect membrane, structural, or stromal contributions, but they do not define the module as a secreted or blood-derived module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a small set of specific relationships rather than a globally enriched interaction network. The strongest known relationships connect MED6 with POLR2A and POLR2B, and connect POLR2A with POLR2B, providing direct support for a Mediator–RNA polymerase II transcriptional submodule. STRING also supports the RAD18–TP53BP1 relationship, consistent with a DNA-damage response branch. hu.MAP independently places POLR2A and POLR2B together in (hu.MAP huMAP3_09843.1), (hu.MAP huMAP3_14318.1), and (hu.MAP huMAP3_11092.1), although each complex contains many additional proteins and only these two members occur in the module. Thus, the module contains a validated transcriptional core and a validated DNA-repair relationship, while most co-abundance links are not established physical interactions in the supplied resources. The network should therefore be interpreted as a co-abundance structure that partially overlays known molecular complexes, not as a confirmed physical complex.

**STRING interactions (score >= 0.7)**: 4 of 91 gene pairs: MED6–POLR2A (0.995); MED6–POLR2B (0.993); POLR2A–POLR2B (0.999); RAD18–TP53BP1 (0.931)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09843.1 (POLR2A, POLR2B; 2/29); huMAP3_14318.1 (POLR2A, POLR2B; 2/58); huMAP3_11092.1 (POLR2A, POLR2B; 2/65)

### Novelty

The molecular components themselves are not new: RNA polymerase II, Mediator, RAD18, TP53BP1, mitotic-checkpoint proteins, and transcription or splicing regulators are well-established biology. The STRING and hu.MAP evidence argues against claiming a newly discovered physical complex. Nevertheless, the breast–skin co-abundance combination and the particular cross-process organization could be a new systems-level observation. That conclusion remains provisional because the fact sheet does not provide an independent replication cohort, preservation statistics, tissue deconvolution, or comparison with previously reported co-expression modules. Absence of STRING or hu.MAP support for most links does not prove novelty; it mainly indicates that those links are not established in the supplied interaction resources.

**Hypothesis.** Hypothesis: this conserved module reflects a shared epithelial or tissue-cellular program that coordinates transcriptional output with genome surveillance. A YEATS2-associated chromatin and transcriptional scaffold may be co-regulated with the RNA polymerase II machinery, while RAD18 and TP53BP1 represent repair and checkpoint protection of actively transcribed genomes. MED6 and TCERG1 could connect transcription initiation or elongation with RNA processing, and MAD1L1 and CDKN2AIP could couple this nuclear program to cell-cycle and damage-response control. UTRN, ROBO1, and EMC10 may reflect the membrane, structural, or tissue-context component of the same cellular state. This is a mechanistic hypothesis based on convergent annotations and partial interaction support, not evidence that the proteins form one physical complex or that one gene causally regulates the others.

### Important genes

#### YEATS2

- **Related proteins** (co-abundance neighbors): MAD1L1 (0.86), POLR2A (0.85), POLR2B (0.84), TP53BP1 (0.83), UTRN (0.82), CDKN2AIP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: YEATS domain containing 2. Summary: The protein encoded by this gene is a scaffolding subunit of the ATAC complex, which is a complex with acetyltransferase activity on histones H3 and H4. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, May 2017].
- **Diseases (Open Targets)**: benign adult familial myoclonic epilepsy (0.485); epilepsy, familial adult myoclonic (0.378); prostate carcinoma (0.262); response to antibiotic (0.162); poisoning (0.162)
- **Europe PMC papers**: 556
- **Why important**: YEATS2 is the central network hub by weighted degree and links the transcriptional, DNA-damage, checkpoint, and membrane-associated portions of the module. Its annotation identifies it as a scaffolding subunit of the ATAC histone-acetyltransferase complex, with roles in chromatin remodeling and RNA polymerase II transcriptional regulation. It has an association with familial adult myoclonic epilepsy and a substantial literature base, making it both mechanistically informative and experimentally tractable.
- **Conclusion**: Established evidence supports YEATS2 as the principal co-abundance organizer and as a chromatin/transcription regulator. The hypothesis that it coordinates the other module branches is plausible from its network position, but causality and physical assembly with the module partners are not established by the supplied STRING or hu.MAP results.

#### POLR2A

- **Related proteins** (co-abundance neighbors): YEATS2 (0.85); STRING partners: MED6 (0.995), POLR2B (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09843.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A is the largest subunit of RNA polymerase II and is directly connected in STRING to POLR2B and MED6. It occurs with POLR2B in all listed hu.MAP complexes, providing convergent support for a genuine transcriptional machinery component. Its carboxy-terminal domain is central to regulated transcription, and it has extensive literature and disease associations involving neurodevelopmental and infectious disease contexts.
- **Conclusion**: Established evidence identifies POLR2A as a core RNA polymerase II component and the strongest-supported anchor of the transcriptional submodule. Its participation in the breast–skin co-abundance module is credible, but the module does not demonstrate tissue-specific regulation of POLR2A.

#### POLR2B

- **Related proteins** (co-abundance neighbors): YEATS2 (0.84); STRING partners: MED6 (0.993), POLR2A (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: huMAP3_09843.1, huMAP3_14318.1, huMAP3_11092.1
- **Function (MyGene.info)**: RNA polymerase II subunit B. This gene encodes the second largest subunit of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase that catalyzes the transcription of DNA into precursors of mRNA, snRNA and microRNA. This subunit and the largest subunit form opposite sides of the center cleft of Pol II. Deletion of the flap loop region of this subunit results in a decrease in the rate of transcriptional elongation. Altern…
- **Diseases (Open Targets)**: HIV infectious disease (0.600); Orthomyxoviridae infectious disease (0.370); dengue disease (0.370); acrocephalosyndactyly (0.370); neurodegenerative disease (0.341)
- **Europe PMC papers**: 589
- **Why important**: POLR2B forms the complementary major subunit of RNA polymerase II and is directly linked to POLR2A and MED6 in STRING. Its presence with POLR2A in (hu.MAP huMAP3_09843.1), (hu.MAP huMAP3_14318.1), and (hu.MAP huMAP3_11092.1) reinforces the interpretation that part of the module tracks transcriptional machinery rather than an isolated gene function. Its annotation specifically supports transcription initiation and elongation, and it has disease and virus-related literature.
- **Conclusion**: Established evidence supports POLR2B as a genuine transcriptional-core member that validates the POLR2A-centered interpretation. The hypothesis that POLR2A and POLR2B drive the broader module is not proven, because most module relationships are co-abundance links rather than documented physical interactions.

#### RAD18

- **Related proteins** (co-abundance neighbors): SYNRG (0.83), ISY1 (0.81), MAD1L1 (0.80); STRING partners: TP53BP1 (0.931)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear bodies; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAD18 E3 ubiquitin protein ligase. The protein encoded by this gene is highly similar to S. cerevisiae DNA damage repair protein Rad18. Yeast Rad18 functions through its interaction with Rad6, which is an ubiquitin-conjugating enzyme required for post-replication repair of damaged DNA. Similar to its yeast counterpart, this protein is able to interact with the human homolog of yeast Rad6 protein through a conserved ring-finger moti…
- **Diseases (Open Targets)**: neurodegenerative disease (0.434); cervical carcinoma (0.283); myocardial ischemia (0.269); lysosomal storage disease (0.258); generalized dystonia (0.205)
- **Europe PMC papers**: 2815
- **Why important**: RAD18 is a highly studied DNA-damage-tolerance and ubiquitin-ligase factor. It occupies a bridge-like position linking MAD1L1 with SYNRG and ISY1, while STRING independently supports its relationship with TP53BP1. Its functions in DNA repair, damage tolerance, and ubiquitination provide a mechanistic explanation for the genome-maintenance branch, and its literature and disease-association record is substantial.
- **Conclusion**: Established evidence supports RAD18 as the main DNA-damage-response representative in the module and supports a known RAD18–TP53BP1 relationship. It remains a hypothesis that RAD18-mediated repair activity is coordinated with the transcriptional and mitotic programs represented by the other module genes.

#### TP53BP1

- **Related proteins** (co-abundance neighbors): YEATS2 (0.83); STRING partners: RAD18 (0.931)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tumor protein p53 binding protein 1. This gene encodes a protein that functions in the DNA double-strand break repair pathway choice, promoting non-homologous end joining (NHEJ) pathways, and limiting homologous recombination. This protein plays multiple roles in the DNA damage response, including promoting checkpoint signaling following DNA damage, acting as a scaffold for recruitment of DNA damage response proteins to damaged chrom…
- **Diseases (Open Targets)**: neurodegenerative disease (0.367); microcephaly and chorioretinopathy 3 (0.353); alcohol drinking (0.269); urolithiasis (0.269); microcephaly and chorioretinopathy 1 (0.266)
- **Europe PMC papers**: 2200
- **Why important**: TP53BP1 is a well-established DNA double-strand-break response scaffold that promotes non-homologous end joining, limits homologous recombination, and supports checkpoint signaling. It is connected to the central YEATS2 neighborhood in the co-abundance network and has an independent STRING relationship with RAD18. Its extensive literature and disease associations make it an important biological readout of genome surveillance.
- **Conclusion**: Established evidence supports TP53BP1 as a DNA-damage checkpoint and repair component and supports its relationship with RAD18. Its direct co-abundance connection to YEATS2 may indicate coordinated regulation, but it does not establish a direct YEATS2–TP53BP1 mechanism.

## Module 10

**Tissue pair**: breast and skin  
**Genes (9)**: CGREF1, COQ9, FLYWCH2, MED7, MOCOS, MTX3, PYM1, GTF2H5, FTSJ1

### Function

No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. The module therefore does not support a single statistically established pathway assignment. Its gene annotations instead indicate a mixed cellular program involving transcriptional initiation and repair through MED7 and GTF2H5, RNA processing and translation through PYM1 and FTSJ1, mitochondrial organization through MTX3, mitochondrial ubiquinone production through COQ9, molybdenum-cofactor-dependent metabolism through MOCOS, and a possible extracellular or Golgi-associated regulatory role for CGREF1. The sparse co-abundance structure and the absence of broad functional enrichment argue for cautious interpretation: the module may represent coordinated expression of several cellular maintenance processes rather than a discrete canonical pathway.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. Only CGREF1 has a secretome annotation, while the other genes are intracellular or have no secretome annotation. Most genes have low tissue specificity, and several are detected in breast and skin at the protein level, which is compatible with broadly expressed cellular programs. The cell-type annotations are heterogeneous, with enrichment in reproductive-cell populations and esophageal epithelial populations rather than immune cells. The absence of immune-cell enrichment makes a blood-cell explanation less likely, although shared cellular composition or technical co-variation in the two tissues cannot be excluded. CGREF1 is tissue enhanced in brain and salivary gland and is annotated as secreted in brain, whereas MOCOS and COQ9 show tissue enhancement in metabolically active tissues. These patterns do not identify a breast-skin-specific biological process.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is between GTF2H5 and MED7. This provides limited support for a connection between transcriptional regulation and DNA-repair-related machinery, but it does not establish the whole module as a physical complex. The remaining module relationships are not supported by the reported high-confidence STRING network. No hu.MAP complex contains multiple module members. Thus, the co-abundance network extends well beyond currently catalogued protein-protein or complex relationships and may primarily reflect coordinated regulation, shared cell-state effects, indirect biology, or measurement structure rather than one stable multiprotein assembly.

**STRING interactions (score >= 0.7)**: 1 of 36 gene pairs: GTF2H5–MED7 (0.825)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact conserved breast-skin co-abundance module appears potentially novel as a network-level observation because it has no reported multi-member hu.MAP complex and only a limited known STRING connection. However, absence from STRING or hu.MAP does not prove biological novelty. Several component functions are already established, including mediator activity, transcription-coupled repair, mitochondrial organization, ubiquinone biosynthesis, RNA modification, and mRNA surveillance. The defensible novelty claim is therefore that this particular cross-tissue co-abundance combination may be new, while its individual genes and many of their functions are not new. Its novelty should be tested by replication in independent breast and skin datasets, preservation across cohorts, adjustment for cell composition, and comparison with other tissue-pair modules.

**Hypothesis.** Hypothesis: the module reflects a shared, broadly expressed cellular maintenance state in breast and skin in which transcriptional control and repair are coordinated with RNA processing, translation, and mitochondrial quality or energy metabolism. MED7 and GTF2H5 may represent the most plausible regulatory anchor because they are the only pair with a reported high-confidence STRING relationship. MTX3, COQ9, and MOCOS could reflect a linked mitochondrial or metabolic component, while FTSJ1 and PYM1 could reflect coupled RNA maturation and translation. CGREF1 may be a tissue or cell-state marker rather than a physical member of the same pathway. This hypothesis is not established by the enrichment results and requires perturbation, protein-level interaction testing, and cell-composition-aware replication.

### Important genes

#### MED7

- **Related proteins** (co-abundance neighbors): PYM1 (0.91), MOCOS (0.87), FLYWCH2 (0.85); STRING partners: GTF2H5 (0.825)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mediator complex subunit 7. The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); chronic atrophic gastritis (0.208); thyroid gland disorder (0.183); Hashimoto thyroiditis (0.079); hypothyroidism (0.055)
- **Europe PMC papers**: 457
- **Why important**: MED7 is among the most connected genes in the module and is the central regulatory node linking PYM1, MOCOS, and FLYWCH2. Its established role as a mediator-complex subunit connects the module to RNA polymerase II transcription. It is also the partner in the only reported high-confidence STRING relationship, with GTF2H5. Its literature base is substantial, supporting a comparatively strong evidential foundation.
- **Conclusion**: Established evidence supports MED7 as a transcriptional co-regulator and as a network connector. It is plausible that MED7 marks a shared transcriptional state in breast and skin, but the module does not establish a MED7-containing physical complex or a tissue-specific function.

#### GTF2H5

- **Related proteins** (co-abundance neighbors): MTX3 (0.83); STRING partners: MED7 (0.825)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: general transcription factor IIH subunit 5. This gene encodes a subunit of transcription/repair factor TFIIH, which functions in gene transcription and DNA repair. This protein stimulates ERCC3/XPB ATPase activity to trigger DNA opening during DNA repair, and is implicated in regulating cellular levels of TFIIH. Mutations in this gene result in trichothiodystrophy, complementation group A. [provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: trichothiodystrophy 3, photosensitive (0.707); trichothiodystrophy (0.686); photosensitive trichothiodystrophy (0.595); HIV infectious disease (0.593); trichothiodystrophy 1, photosensitive (0.462)
- **Europe PMC papers**: 371
- **Why important**: GTF2H5 connects the module to transcription and nucleotide-excision repair and has a reported high-confidence STRING relationship with MED7. Its disease associations with photosensitive trichothiodystrophy provide biological relevance to genome maintenance and skin-related phenotypes. Its network link to MTX3 also places it at a possible interface between nuclear maintenance and mitochondrial organization.
- **Conclusion**: Established evidence supports a role for GTF2H5 in TFIIH function, RNA polymerase II transcription, and nucleotide-excision repair. A coordinated relationship with mitochondrial genes in this module is a hypothesis rather than an established mechanism.

#### MTX3

- **Related proteins** (co-abundance neighbors): CGREF1 (0.84), GTF2H5 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Mitochondria; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: metaxin 3. Predicted to be involved in mitochondrion organization. Part of MIB complex and SAM complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: response to stimulus (0.304); adverse effect (0.304); poisoning (0.304); ovarian neoplasm (0.247); smoking initiation (0.218)
- **Europe PMC papers**: 188
- **Why important**: MTX3 is a module connector linking CGREF1 with GTF2H5 and is detected in both breast and skin by immunohistochemistry. Its annotation places it in mitochondrial organization and mitochondrial membrane translocase-related processes, giving the module a defined organelle-maintenance component despite the absence of global enrichment.
- **Conclusion**: Established evidence supports MTX3 in mitochondrial organization and outer-membrane protein insertion. Its co-abundance with transcription and repair genes may indicate a shared cellular maintenance state, but a direct mechanistic bridge is not demonstrated.

#### COQ9

- **Related proteins** (co-abundance neighbors): CGREF1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coenzyme Q9. This locus represents a mitochondrial ubiquinone biosynthesis gene. The encoded protein is likely necessary for biosynthesis of coenzyme Q10, as mutations at this locus have been associated with autosomal-recessive neonatal-onset primary coenzyme Q10 deficiency.[provided by RefSeq, Sep 2010].
- **Diseases (Open Targets)**: encephalopathy-hypertrophic cardiomyopathy-renal tubular disease syndrome (0.766); coenzyme Q10 deficiency (0.635); hereditary disease (0.415); mitochondrial disease (0.372); coenzyme Q10 deficiency, primary, 1 (0.370)
- **Europe PMC papers**: 958
- **Why important**: COQ9 connects to the highest-connectivity node, CGREF1, and is detected in both breast and skin. It is an established mitochondrial ubiquinone-biosynthesis gene with strong disease relevance through primary coenzyme Q deficiency and related mitochondrial disease. This makes it an informative marker of respiratory or redox capacity within an otherwise functionally heterogeneous module.
- **Conclusion**: Established evidence supports COQ9 in coenzyme Q biosynthesis and mitochondrial disease biology. Its inclusion supports a mitochondrial interpretation of part of the module, but does not show that the entire module controls ubiquinone production.

#### MOCOS

- **Related proteins** (co-abundance neighbors): MED7 (0.87), CGREF1 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: molybdenum cofactor sulfurase. This gene encodes an enzyme that sulfurates the molybdenum cofactor which is required for activation of the xanthine dehydrogenase (XDH) and aldehyde oxidase (AO) enzymes. XDH catalyzes the conversion of hypoxanthine to uric acid via xanthine, as well as the conversion of allopurinol to oxypurinol, and pyrazinamide to 5-hydroxy pyrazinamide. Mutations in this gene cause the metabolic disorder clas…
- **Diseases (Open Targets)**: xanthinuria type II (0.783); hereditary xanthinuria (0.507); autism spectrum disorder (0.335); stricture (0.192); primary hyperoxaluria (0.131)
- **Europe PMC papers**: 346
- **Why important**: MOCOS is connected to both MED7 and CGREF1 and contributes a distinct metabolic function through molybdenum-cofactor sulfurase activity. Its tissue enhancement in adrenal gland and liver and its association with xanthinuria type II provide independent biological context. Its position between regulatory and extracellularly annotated module members makes it useful for evaluating whether the network reflects coordinated metabolism rather than one canonical complex.
- **Conclusion**: Established evidence supports MOCOS in molybdenum-cofactor metabolism and activation of xanthine dehydrogenase and aldehyde oxidase. Its connection to transcriptional and CGREF1-related signals is currently a co-abundance observation, not a proven biochemical pathway.

## Module 11

**Tissue pair**: breast and skin  
**Genes (13)**: APPL2, SMG6, GULP1, HYPK, INTS9, ITSN1, KDM3B, PLCB3, RAD50, RNASEH2A, TRIM24, TLK1, WAPL

### Function

The module does not have a globally significant GO or KEGG enrichment term, and STRING reports no supplementary functional enrichment. Its structure instead suggests a mixed cellular-maintenance program. The most connected component is centered on TLK1 and links chromatin and cell-cycle-related genes, including WAPL, RAD50, RNASEH2A, KDM3B, and HYPK. A second local component links SMG6 with APPL2, TRIM24, and GULP1, while GULP1 connects to ITSN1. The annotations support themes of genome integrity, chromatin regulation, RNA surveillance, telomere maintenance, endosomal trafficking, and signal transduction. These themes should be treated as an integrated interpretation of gene functions and network structure, not as enrichment results. The module may therefore represent coordinated cellular maintenance across breast and skin rather than a single canonical pathway.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and the proteins are detected in breast and skin for most genes with available data. Most genes also have low immune-cell specificity, arguing against a simple blood-protein or broad blood-cell contamination explanation. Nevertheless, several genes show enhanced immune-cell or particular cell-type expression, including myeloid, platelet, trophoblast, epithelial, glial, and intestinal-associated patterns. The shared signal could consequently reflect common cellular states or cell-type mixtures in breast and skin samples. HPA does not support interpreting the module as a secreted inflammatory signature, but it also does not establish that the signal is intrinsic to one uniform tissue cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING relationships among the module genes, so the co-abundance edges are not corroborated by known STRING protein interactions. This weakens a claim that the entire module is a physically interacting complex, while not invalidating co-regulation or shared cell-state biology. hu.MAP provides the clearest prior structural support: ITSN1 and GULP1 occur together in (hu.MAP huMAP3_12918.1) and (hu.MAP huMAP3_12394.1). Those complexes are broad trafficking-associated assemblies containing many proteins outside the module, so the evidence supports a known ITSN1-GULP1 complex context rather than a module-wide complex. The remaining genes have no reported hu.MAP membership in the fact sheet. Overall, the network is better viewed as a co-abundance module containing a known endocytic-adaptor pair plus several functionally related but not database-confirmed genes.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12918.1 (ITSN1, GULP1; 2/62); huMAP3_12394.1 (ITSN1, GULP1; 2/98)

### Novelty

The exact conserved breast-skin co-abundance module may be a new observation because it is not represented as a high-confidence STRING interaction network or as a compact hu.MAP complex. However, database absence does not prove biological novelty: many module genes have established functions, and the ITSN1-GULP1 relationship is already represented in (hu.MAP huMAP3_12918.1) and (hu.MAP huMAP3_12394.1). The potentially novel result is therefore the cross-tissue co-abundance organization and its combination of genome-maintenance, RNA-surveillance, chromatin, signaling, and endocytic genes, not the discovery of previously unknown functions for the individual genes. Independent replication, preservation in additional cohorts, control for cell composition, and perturbation or interaction experiments would be needed to establish novelty and mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-maintenance state in breast and skin in which genome replication and repair, chromatin and transcriptional regulation, RNA quality control, and membrane trafficking are coordinated. TLK1 may organize the genome-maintenance side of the signal, with RAD50 and RNASEH2A reporting DNA-repair or replication stress, while SMG6 and TRIM24 connect RNA surveillance and chromatin-transcription control. In parallel, GULP1 and ITSN1 may represent endocytic or engulfment-related remodeling, with APPL2 and PLCB3 providing signaling or membrane-trafficking context. This could arise from a common proliferative, stress-responsive, or cell-composition state rather than direct physical interaction among all module members. The hypothesis remains unproven because no GO or KEGG term passed global correction and STRING supplied no interaction enrichment.

### Important genes

#### TLK1

- **Related proteins** (co-abundance neighbors): WAPL (0.85), RAD50 (0.84), RNASEH2A (0.82), PLCB3 (0.81), KDM3B (0.81), HYPK (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tousled like kinase 1. The protein encoded by this gene is a serine/threonine kinase that may be involved in the regulation of chromatin assembly. The encoded protein is only active when it is phosphorylated, and this phosphorylation is cell cycle-dependent, with the maximal activity of this protein coming during S phase. The catalytic activity of this protein is diminished by DNA damage and by blockage of DNA replicati…
- **Diseases (Open Targets)**: neurodegenerative disease (0.508); cancer (0.295); mixed connective tissue disease (0.262); autoimmune disorder of central nervous system (0.184); oropharynx cancer (0.145)
- **Europe PMC papers**: 635
- **Why important**: TLK1 is the central network connector in the module, linking WAPL, RAD50, RNASEH2A, PLCB3, KDM3B, and HYPK. Its established function as a cell-cycle-regulated serine/threonine kinase involved in chromatin assembly provides a plausible organizing point for the genome-maintenance and chromatin-related part of the module. It has substantial literature and disease associations involving cancer, neurodegenerative disease, and autoimmune disease.
- **Conclusion**: Established evidence supports TLK1 as the strongest network-centered candidate and as a regulator of chromatin and replication-associated biology. It is a plausible module coordinator, but the co-abundance data do not prove that TLK1 regulates the other module genes. A coordinating role is therefore a hypothesis.

#### RAD50

- **Related proteins** (co-abundance neighbors): TLK1 (0.84), SMG6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Group enriched; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAD50 double strand break repair protein. The protein encoded by this gene is highly similar to Saccharomyces cerevisiae Rad50, a protein involved in DNA double-strand break repair. This protein forms a complex with MRE11 and NBS1. The protein complex binds to DNA and displays numerous enzymatic activities that are required for nonhomologous joining of DNA ends. This protein, cooperating with its partners, is important for DNA double-stra…
- **Diseases (Open Targets)**: Nijmegen breakage syndrome-like disorder (0.780); cancer (0.593); hereditary neoplastic syndrome (0.579); hereditary breast ovarian cancer syndrome (0.539); breast carcinoma (0.490)
- **Europe PMC papers**: 13311
- **Why important**: RAD50 connects directly to TLK1 and SMG6, placing it between the module's genome-maintenance and RNA-surveillance neighborhoods. Its established role in the MRE11-NBS1 DNA double-strand-break repair complex, checkpoint activation, and telomere maintenance gives the module a strong mechanistic genome-integrity anchor. It also has extensive literature and well-established associations with Nijmegen breakage syndrome-like disease and hereditary cancer risk.
- **Conclusion**: Established evidence supports RAD50 as a biologically important DNA-repair component and a meaningful bridge in this network. The module may report genome stress or repair capacity, but RAD50 cannot by itself establish that such stress caused the shared breast-skin pattern.

#### SMG6

- **Related proteins** (co-abundance neighbors): APPL2 (0.84), RAD50 (0.82), TRIM24 (0.82), GULP1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SMG6 nonsense mediated mRNA decay factor. This gene encodes a component of the telomerase ribonucleoprotein complex responsible for the replication and maintenance of chromosome ends. The encoded protein also plays a role in the nonsense-mediated mRNA decay (NMD) pathway, providing the endonuclease activity near the premature translation termination codon that is needed to initiate NMD. Alternatively spliced transcript variants encoding d…
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); coronary artery disorder (0.354); androgenetic alopecia (0.312); Abnormality of the skeletal system (0.298); myocardial ischemia (0.291)
- **Europe PMC papers**: 1149
- **Why important**: SMG6 is a network bridge connecting APPL2, RAD50, TRIM24, and GULP1. It combines two relevant established functions: endonucleolytic activity in nonsense-mediated mRNA decay and participation in telomerase-related telomere maintenance. Its substantial literature makes it a stronger interpretive candidate than a poorly characterized peripheral gene.
- **Conclusion**: Established evidence supports SMG6 as a link between RNA quality control and chromosome-end maintenance. Its position suggests a possible bridge between the module's nuclear and trafficking-associated signals, but that cross-compartment interpretation remains a hypothesis.

#### GULP1

- **Related proteins** (co-abundance neighbors): ITSN1 (0.83), INTS9 (0.80), SMG6 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in breast, skin
- **hu.MAP 3.0**: huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: GULP PTB domain containing engulfment adaptor 1. The protein encoded by this gene is an adapter protein necessary for the engulfment of apoptotic cells by phagocytes. Several transcript variants, some protein coding and some thought not to be protein coding, have been found for this gene. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: smoking initiation (0.419); intracranial hemorrhage (0.308); ovarian dysfunction (0.270); alcohol drinking (0.250); urolithiasis (0.250)
- **Europe PMC papers**: 573
- **Why important**: GULP1 forms the module's clearest database-supported relationship with ITSN1, appearing with ITSN1 in both (hu.MAP huMAP3_12918.1) and (hu.MAP huMAP3_12394.1). It is an engulfment adaptor associated with apoptotic-cell uptake and is localized to vesicles. Its tissue-enhanced and cell-type-enhanced HPA patterns make it informative for considering cell composition or vesicle-mediated tissue remodeling.
- **Conclusion**: Established evidence supports GULP1 as an adaptor involved in engulfment and as part of a known complex context with ITSN1. Its co-abundance with nuclear maintenance genes may reflect coordinated tissue remodeling or shared cellular composition, but a direct mechanistic connection to TLK1 or SMG6 is not established.

#### ITSN1

- **Related proteins** (co-abundance neighbors): GULP1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in breast, skin
- **hu.MAP 3.0**: huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: intersectin 1. The protein encoded by this gene is a cytoplasmic membrane-associated protein that indirectly coordinates endocytic membrane traffic with the actin assembly machinery. In addition, the encoded protein may regulate the formation of clathrin-coated vesicles and could be involved in synaptic vesicle recycling. This protein has been shown to interact with dynamin, CDC42, SNAP23, SNAP25, SPIN90, EPS15,…
- **Diseases (Open Targets)**: hereditary disease (0.531); neurodevelopmental disorder (0.451); Autistic behavior (0.404); Intellectual disability (0.378); autosomal dominant non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 1094
- **Why important**: ITSN1 is the partner of GULP1 in the module and is present in both (hu.MAP huMAP3_12918.1) and (hu.MAP huMAP3_12394.1). Its established functions in clathrin-coated vesicle formation, endosomal transport, actin coordination, and signal regulation provide the strongest membrane-trafficking interpretation in the module. It has substantial literature and disease associations involving neurodevelopmental phenotypes.
- **Conclusion**: Established evidence supports ITSN1 as an endocytic and membrane-associated adaptor and supports its relationship with GULP1 through hu.MAP. Its presence does not demonstrate that the entire module is an endocytic complex; the broader trafficking-to-genome-maintenance link remains hypothetical.

#### TRIM24

- **Related proteins** (co-abundance neighbors): SMG6 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tripartite motif containing 24. The protein encoded by this gene mediates transcriptional control by interaction with the activation function 2 (AF2) region of several nuclear receptors, including the estrogen, retinoic acid, and vitamin D3 receptors. The protein localizes to nuclear bodies and is thought to associate with chromatin and heterochromatin-associated factors. The protein is a member of the tripartite motif (TRIM) fa…
- **Diseases (Open Targets)**: cancer (0.609); neurodegenerative disease (0.540); leukemia (0.380); lung adenocarcinoma (0.374); acute lymphoblastic leukemia (0.372)
- **Europe PMC papers**: 2114
- **Why important**: TRIM24 connects to SMG6 and is an established chromatin-associated transcriptional regulator that interacts with nuclear receptors, including estrogen, retinoic acid, and vitamin D receptors. Its roles in transcriptional control, chromatin organization, ubiquitination, and protein stability are particularly relevant to breast and skin biology. It also has substantial literature and disease associations involving cancer and leukemia.
- **Conclusion**: Established evidence supports TRIM24 as a plausible tissue-relevant chromatin and transcriptional component. Its co-abundance with SMG6 may indicate a shared nuclear regulatory state, but the module does not establish a direct TRIM24-SMG6 mechanism.

## Module 12

**Tissue pair**: breast and skin  
**Genes (7)**: EZH2, MED16, MTMR1, RASA3, SLC20A1, SP3, YRDC

### Function

The module does not have a statistically supported shared GO/KEGG function: no GO/KEGG term passed global correction. Its gene-level annotations instead suggest a mixed regulatory and cellular-maintenance program. SLC20A1 is a plasma-membrane sodium-phosphate transporter involved in phosphate transport and phosphate-containing compound metabolism. RASA3 is a negative regulator of Ras signalling and is also annotated in platelet activation. SP3 and MED16 support transcriptional regulation, with MED16 being a Mediator component and SP3 a GC- and GT-box-binding transcription factor. EZH2 supports Polycomb-mediated transcriptional repression and chromatin regulation. MTMR1 is associated with phosphatidylinositol metabolism, while YRDC is associated with mitochondrial tRNA modification and translational fidelity. The network is therefore more consistent with a co-abundance pattern linking membrane transport, signalling, transcriptional control, chromatin state, and intracellular maintenance than with a single established pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins, because none of its genes is annotated as secreted. Most genes have low tissue specificity, and all are detected in skin while nearly all are detected in breast. The HPA evidence shows cell-type enhancement for most genes, particularly patterns involving neutrophil progenitors, platelets, megakaryocyte progenitors, erythrocyte progenitors, and other hematopoietic or blood-associated populations. EZH2 is tissue enhanced in bone marrow and lymphoid tissue and is immune-cell enhanced, while YRDC is tissue enhanced in bone marrow and immune-cell enriched in basophils. This raises a credible possibility that the shared breast-skin signal reflects blood-derived cells, vascular or immune admixture, or a shared progenitor-related cellular component rather than a breast-and-skin-specific program. The evidence does not establish which of these explanations is correct.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not corroborated here by high-confidence physical or functional interactions, and the module should not be interpreted as a known protein complex. The strongest network relationships are consequently co-abundance relationships within this dataset rather than established molecular interactions. The absence of STRING or hu.MAP support may reflect context-specific co-regulation, incomplete database coverage, indirect relationships, or a compositional signal.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module is a potentially interesting dataset-level association, but it cannot be called a newly discovered biological pathway or complex. Its novelty is supported only in the limited sense that this particular breast-skin co-abundance configuration was observed in the supplied analysis and is not represented by a matching high-confidence STRING interaction set or hu.MAP complex. Those database absences do not prove biological novelty. The lack of globally significant GO/KEGG enrichment, the mixed annotations, and the hematopoietic signals make a novel unified mechanism less secure. Independent replication, adjustment for blood-cell composition, and validation at the protein or single-cell level would be needed before claiming a new module mechanism.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state or sample-composition program involving phosphate and membrane homeostasis, Ras and phosphoinositide signalling, and transcriptional or chromatin regulation in cells present in both tissues. Hematopoietic or platelet-related cells may contribute substantially to the observed co-abundance pattern, while EZH2, SP3, and MED16 could couple cellular state to transcriptional control and SLC20A1 or MTMR1 could connect that state to membrane or phosphoinositide biology. This is a mechanistic hypothesis, not an established pathway assignment; the absence of global enrichment and external interaction support makes it especially important to test against cell composition and technical covariates.

### Important genes

#### SLC20A1

- **Related proteins** (co-abundance neighbors): MTMR1 (0.85), MED16 (0.83), SP3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 20 member 1. The protein encoded by this gene is a sodium-phosphate symporter that absorbs phosphate from interstitial fluid for use in cellular functions such as metabolism, signal transduction, and nucleic acid and lipid synthesis. The encoded protein is also a retroviral receptor, causing human cells to be susceptible to infection by gibbon ape leukemia virus, simian sarcoma-associated virus, feline leukemi…
- **Diseases (Open Targets)**: neurodegenerative disease (0.319); prostate carcinoma (0.295); pancreatic ductal adenocarcinoma (0.095); placental retention (0.086); head and neck squamous cell carcinoma (0.075)
- **Europe PMC papers**: 1113
- **Why important**: SLC20A1 is the most connected node in the supplied network and links MTMR1, MED16, and SP3. Its established function as a sodium-phosphate symporter gives the module a plausible membrane and phosphate-homeostasis anchor. It is detected in both tissues, has broad tissue distribution, and has substantial literature coverage. Its disease associations include neurodegenerative disease and several carcinomas, although those associations do not establish a role in this module.
- **Conclusion**: Established evidence supports SLC20A1 as a broadly expressed phosphate transporter and as a network hub. It is a plausible module anchor, but the co-abundance data do not demonstrate that its transporter activity drives the other genes or that the module is tissue-specific.

#### RASA3

- **Related proteins** (co-abundance neighbors): EZH2 (0.81), YRDC (0.81), SP3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAS p21 protein activator 3. This gene encodes a protein that binds inositol 1,3,4,5-tetrakisphosphate and stimulates the GTPase activity of Ras p21. This protein functions as a negative regulator of the Ras signalling pathway. It is localized to the cell membrane via a pleckstrin homology (PH) domain in the C-terminal region. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2016].
- **Diseases (Open Targets)**: Short stature (0.397); neurodegenerative disease (0.323); post term pregnancy (0.293); placental retention (0.274); oral mucosa leukoplakia (0.263)
- **Europe PMC papers**: 642
- **Why important**: RASA3 is among the most connected nodes and links EZH2, YRDC, and SP3. Its established Ras-GTPase-activating function provides a signalling explanation for coordinated abundance with transcriptional and chromatin regulators. Its annotations also include platelet activation, which is relevant to the HPA evidence for platelet and hematopoietic cell-type patterns. It has meaningful literature coverage and disease associations including short stature and neurodegenerative disease.
- **Conclusion**: Established evidence supports RASA3 as a negative regulator of Ras signalling with relevance to platelet biology. Within this module, it is a strong candidate for connecting signalling to the other genes, but a direct molecular connection is not established because STRING reports no qualifying partner.

#### EZH2

- **Related proteins** (co-abundance neighbors): RASA3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: enhancer of zeste 2 polycomb repressive complex 2 subunit. This gene encodes a member of the Polycomb-group (PcG) family. PcG family members form multimeric protein complexes, which are involved in maintaining the transcriptional repressive state of genes over successive cell generations. This protein associates with the embryonic ectoderm development protein, the VAV1 oncoprotein, and the X-linked nuclear protein. This protein may play a role in the hema…
- **Diseases (Open Targets)**: Weaver syndrome (0.837); diffuse large B-cell lymphoma (0.615); neurodegenerative disease (0.525); follicular lymphoma (0.517); viral infectious disease (0.486)
- **Europe PMC papers**: 43112
- **Why important**: EZH2 connects directly to RASA3 and has the strongest tissue and blood-cell specificity signals in the module, including bone marrow, lymphoid tissue, progenitor populations, and T-reg-associated evidence. Its Polycomb and chromatin-regulatory functions provide a biologically important route from cellular identity to gene-expression state. It has very extensive literature coverage and disease associations including Weaver syndrome and lymphomas.
- **Conclusion**: Established evidence supports EZH2 as a major chromatin regulator with hematopoietic and disease relevance. It is a high-priority marker of the module's possible cell-state or blood-derived component, but its presence does not prove that Polycomb repression is the shared functional output of the module.

#### SP3

- **Related proteins** (co-abundance neighbors): RASA3 (0.80), SLC20A1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Sp3 transcription factor. This gene belongs to a family of Sp1 related genes that encode transcription factors that regulate transcription by binding to consensus GC- and GT-box regulatory elements in target genes. This protein contains a zinc finger DNA-binding domain and several transactivation domains, and has been reported to function as a bifunctional transcription factor that either stimulates or represses the transc…
- **Diseases (Open Targets)**: hypothyroidism (0.457); plasma cell myeloma (0.404); prostate carcinoma (0.349); alopecia (0.345); autoimmune thyroid disease (0.338)
- **Europe PMC papers**: 14573
- **Why important**: SP3 is a central connector between RASA3 and SLC20A1 and is annotated as a transcription factor capable of activating or repressing transcription through GC- and GT-box elements. Its HPA profile includes neutrophil progenitors and neutrophils, which fits the module's hematopoietic compositional signal. It has extensive literature coverage and disease associations including plasma-cell myeloma, prostate carcinoma, alopecia, and autoimmune thyroid disease.
- **Conclusion**: Established evidence supports SP3 as a broadly acting transcriptional regulator and a network bridge in this module. It could coordinate expression of several module genes, but the supplied data do not identify direct SP3 targets or show that its transcriptional activity explains the co-abundance pattern.

#### MTMR1

- **Related proteins** (co-abundance neighbors): SLC20A1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Vesicles; IHC detected in breast, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myotubularin related protein 1. This gene encodes a member of the myotubularin related family of proteins. Members of this family contain the consensus sequence for the active site of protein tyrosine phosphatases. Alternatively spliced variants have been described but their biological validity has not been determined. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: post-traumatic stress disorder (0.140); autosomal dominant macrothrombocytopenia (0.073); platelet-type bleeding disorder 15 (0.051); macrothrombocytopenia, isolated, 2, autosomal dominant (0.050); Thrombocytopenia (0.049)
- **Europe PMC papers**: 344
- **Why important**: MTMR1 is connected to SLC20A1 and contributes a phosphoinositide-metabolism perspective that complements the membrane transport annotation of SLC20A1. Its disease associations include platelet-type bleeding disorders and macrothrombocytopenia, which are notable given the platelet-related HPA signals. Its literature coverage is more limited than that of the principal regulatory genes, making it potentially informative but less established.
- **Conclusion**: Established evidence supports MTMR1 as a myotubularin-related phosphoinositide regulator with platelet-related disease associations. It is a plausible metabolic or membrane-state component of the module, but its peripheral network position and limited annotation support make a central mechanistic role uncertain.
