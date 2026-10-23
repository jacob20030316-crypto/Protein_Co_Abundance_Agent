# Conserved co-abundance modules: cervix_uterine and liver

## Module 0

**Tissue pair**: cervix_uterine and liver  
**Genes (32)**: PPP2R2A, NT5E, ARHGEF10L, CENPV, GPS1, DSP, ADAR, GFM1, GCLC, HACD3, HNRNPH1, IDE, CKB, TMPO, TMPO, ME1, IMMT, NRDC, OPA1, P4HA1, PDCD6IP, UQCRC2, RPRD1B, SEC23A, SMS, SPTBN1, SPTBN2, TM9SF2, UGGT1, USO1, WASHC4, ZC3HAV1

### Function

The module does not support a single statistically established GO or KEGG function: no GO/KEGG term passed global correction. Its gene-level evidence instead points to a mixed cellular-maintenance program involving mitochondrial integrity and respiration through OPA1, IMMT, UQCRC2, and GFM1; intracellular protein trafficking and ER-to-Golgi transport through SEC23A and USO1; membrane–actin organization through SPTBN1, SPTBN2, DSP, and ARHGEF10L; and oxidative-stress or biosynthetic support through GCLC, ME1, and HACD3. RNA processing and antiviral or innate-defense functions are represented by HNRNPH1, ADAR, and ZC3HAV1. Because the subgraph is sparse and contains several weakly connected functional groupings, the most defensible interpretation is a broad cellular homeostasis and maintenance module rather than a narrowly defined pathway. The enrichment result should not be described as evidence against the module itself.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only a minority of genes are annotated as secreted, and most are intracellular or membrane-associated. The HPA profile is broadly distributed, with many genes having low tissue specificity and many showing cell-type enhancement rather than a uniform tissue program. Protein detection is common in both cervix_uterine and liver, although several genes are not detected in one or both tissues. Most genes have low immune-cell specificity, while a smaller subset is enhanced or enriched in neutrophils, monocytes, lymphoid cells, or other blood-related populations. Therefore, a simple blood-contamination explanation is not supported, but shared cell types, common housekeeping or organelle activity, and cellular composition differences remain plausible contributors. The presence of liver-enhanced, cervix-enhanced, epithelial, endothelial, stromal, and immune-associated signals argues for a mixed-composition interpretation rather than a tissue-exclusive function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING evidence is limited to three high-confidence relationships: IMMT with UQCRC2, SEC23A with USO1, and SPTBN1 with SPTBN2. These relationships are biologically coherent with mitochondrial organization or respiratory-chain function, ER-to-Golgi trafficking, and spectrin-based membrane–cytoskeleton organization, respectively. hu.MAP independently supports the SPTBN1–SPTBN2 pair in several complexes, including complexes containing spectrin or membrane-cytoskeleton partners. hu.MAP also places UQCRC2 with HACD3 in a broad membrane and organelle-associated complex and places SEC23A with USO1 in a large trafficking-related complex. Thus, the databases validate several local edges or functional anchors, but they do not establish one unified complex containing the whole module. Most module relationships are not supported by these resources, so co-abundance should not be interpreted as direct physical interaction.

**STRING interactions (score >= 0.7)**: 3 of 496 gene pairs: IMMT–UQCRC2 (0.811); SEC23A–USO1 (0.704); SPTBN1–SPTBN2 (0.738)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07940.1 (SPTBN2, SPTBN1; 2/5); huMAP3_05473.1 (SPTBN2, SPTBN1; 2/7); huMAP3_09165.1 (SPTBN2, SPTBN1; 2/39); huMAP3_06247.1 (UQCRC2, HACD3; 2/65); huMAP3_12394.1 (USO1, SEC23A; 2/98)

### Novelty

The module may represent a novel cross-tissue co-abundance pattern, but the available evidence is insufficient to call it a new biological pathway or a newly discovered physical complex. The strongest known components recapitulate established biology involving mitochondrial machinery, COPII and Golgi trafficking, spectrin scaffolding, redox metabolism, and RNA or antiviral regulation. The potentially novel aspect is their coordinated abundance across cervix_uterine and liver, especially because the network joins several otherwise distinct cellular systems. Absence of STRING or hu.MAP support for many edges is compatible with novelty, but it can also reflect incomplete databases, indirect regulation, shared cell composition, or technical co-variation. A novelty claim would require replication in independent cohorts, control for cell-type composition, and comparison with published cross-tissue co-expression modules.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-stress and structural-maintenance state present in selected cervix_uterine and liver cell populations. In this model, mitochondrial organization and respiratory capacity are coordinated with glutathione-dependent redox protection, ER-to-Golgi trafficking, vesicle handling, membrane–cytoskeleton integrity, and RNA-based antiviral surveillance. The co-abundance could arise from a common physiological demand for organelle quality control and membrane remodeling, or from a reproducible mixture of epithelial, endothelial, stromal, and limited immune populations. This is a hypothesis rather than an established pathway, because global GO/KEGG enrichment was not significant and the network contains only a few database-supported interactions.

### Important genes

#### OPA1

- **Related proteins** (co-abundance neighbors): IDE (0.86), WASHC4 (0.84), SPTBN2 (0.84), GFM1 (0.84), PDCD6IP (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 is among the most connected genes in the module and links mitochondrial biology to several otherwise different module components, including GFM1, IDE, WASHC4, SPTBN2, and PDCD6IP. Its established function in inner-mitochondrial-membrane organization, mitochondrial fusion, stability, and energy output makes it a strong anchor for the mitochondrial-maintenance interpretation. Its extensive literature and associations with dominant optic atrophy and other mitochondrial disorders provide substantial external biological support.
- **Conclusion**: Established evidence supports OPA1 as a mitochondrial-organization and quality-control gene that is prominently positioned in this module. It is plausible that OPA1 marks a shared mitochondrial state across the two tissues, but the module does not establish that OPA1 regulates the other genes or that mitochondrial dysfunction drives the co-abundance pattern.

#### GCLC

- **Related proteins** (co-abundance neighbors): WASHC4 (0.84), ME1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate-cysteine ligase catalytic subunit. Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase is the first rate-limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. This locus encodes the catalytic subunit, while the regulatory subunit is derived from a different gene located on chromosome 1p22-p21. Mutations at this locus have been …
- **Diseases (Open Targets)**: gamma-glutamylcysteine synthetase deficiency (0.766); cystic fibrosis (0.375); neurodegenerative disease (0.373); non-autoimmune hemolytic anemia (0.370); lung adenocarcinoma (0.331)
- **Europe PMC papers**: 8941
- **Why important**: GCLC connects WASHC4 and ME1 and is tissue-enhanced in liver while detected in both tissues. It encodes the catalytic component of the rate-limiting step in glutathione synthesis and is annotated for oxidative-stress responses. Its substantial literature and association with glutathione-synthesis deficiency make it an informative marker of redox capacity within a module otherwise containing mitochondrial and trafficking genes.
- **Conclusion**: Established evidence supports GCLC as a central redox and glutathione-biosynthesis component. Its co-abundance with mitochondrial and membrane-trafficking genes is consistent with coordinated protection from metabolic or cellular stress, but a causal redox role for the entire module remains hypothetical.

#### SEC23A

- **Related proteins** (co-abundance neighbors): PDCD6IP (0.82), USO1 (0.81); STRING partners: USO1 (0.704)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is linked to PDCD6IP and USO1, with both the STRING and hu.MAP evidence supporting its relationship with USO1. Its established role in COPII vesicle budding, cargo loading, and ER-to-Golgi transport provides a clear trafficking anchor. Its disease association with craniolenticulosutural dysplasia further demonstrates the importance of this pathway for tissue and organismal biology.
- **Conclusion**: Established evidence supports SEC23A as a vesicle-trafficking component and as part of a known SEC23A–USO1 relationship represented in the module. The module may therefore include coordinated secretory-pathway activity, but the shared abundance pattern does not prove altered COPII flux or direct regulation of the mitochondrial and redox genes.

#### SPTBN1

- **Related proteins** (co-abundance neighbors): GPS1 (0.84), CKB (0.81); STRING partners: SPTBN2 (0.738)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_05473.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin beta, non-erythrocytic 1. Spectrin is an actin crosslinking and molecular scaffold protein that links the plasma membrane to the actin cytoskeleton, and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. It is composed of two antiparallel dimers of alpha- and beta- subunits. This gene is one member of a family of beta-spectrin genes. The encoded protein cont…
- **Diseases (Open Targets)**: developmental delay, impaired speech, and behavioral abnormalities (0.802); cancer (0.597); hereditary disease (0.516); hearing loss disorder (0.459); neurodevelopmental disorder (0.453)
- **Europe PMC papers**: 1635
- **Why important**: SPTBN1 is connected to GPS1 and CKB and forms the STRING-supported SPTBN1–SPTBN2 pair. Both genes occur together in several hu.MAP complexes, providing the clearest repeated complex-level support in the module. SPTBN1 is an actin-associated membrane scaffold involved in plasma-membrane organization, vesicle transport, and cell shape. Its disease and developmental associations add biological relevance beyond network position.
- **Conclusion**: Established evidence supports SPTBN1 as a membrane–cytoskeleton scaffold and validates its relationship with SPTBN2 at the database level. It is a credible structural anchor for the module, while any connection to mitochondrial or redox regulation should be regarded as an inferred systems-level association rather than a demonstrated mechanism.

#### ZC3HAV1

- **Related proteins** (co-abundance neighbors): HNRNPH1 (0.90), TMPO (0.85), TM9SF2 (0.84), GPS1 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: zinc finger CCCH-type containing, antiviral 1. This gene encodes a CCCH-type zinc finger protein. This antiviral protein inhibits viral replication by recruiting cellular RNA degradation machineries to degrade viral mRNAs. The encoded protein plays an important role in the innate immune response against multiple DNA and RNA viruses, including Ebola virus, HIV and SARS-CoV-2 (which causes COVID-19). [provided by RefSeq, Sep 2021].
- **Diseases (Open Targets)**: cancer (0.549); hypothyroidism (0.429); neurodegenerative disease (0.358); autoimmune disease (0.308); Hashimoto thyroiditis (0.306)
- **Europe PMC papers**: 979
- **Why important**: ZC3HAV1 is one of the more connected genes and links HNRNPH1, TMPO, TM9SF2, and GPS1. Its established antiviral activity, recruitment of RNA-degradation machinery, and roles in interferon and NF-kappaB-related responses provide a biologically distinctive signal. HPA data show enhancement in several endometrial and immune-related cell types, which is relevant to interpretation of a shared cervix_uterine and liver module.
- **Conclusion**: Established evidence supports ZC3HAV1 as an antiviral RNA-surveillance factor with cell-type-specific expression. It may indicate innate-defense or RNA-quality-control activity in part of the module, but the available evidence does not demonstrate that antiviral signaling is the dominant function of the full module or that it explains the mitochondrial and trafficking associations.

## Module 1

**Tissue pair**: cervix_uterine and liver  
**Genes (16)**: HIBADH, PYCARD, CBR1, CSTB, CZIB, HSPB1, IQGAP2, ISG15, MX1, LCN2, HPGD, PSMB8, SCP2, SUCLG1, SYNE2, TXN

### Function

The module does not have a GO or KEGG term passing global correction, so no pathway-level enrichment can be claimed from those analyses. Its strongest biological signal is a mixed stress and innate-defense context centered on MX1, with links to interferon-associated antiviral response, inflammatory signaling, redox and proteostasis responses, epithelial biology, and tissue metabolism. These interpretations are supported by the supplied gene annotations and network structure, not by globally significant enrichment. The module should therefore be interpreted as a co-abundance state rather than as a demonstrated single biochemical pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only a minority are annotated as secreted, while most are intracellular or membrane-associated. It is also not uniformly blood-cell enriched. HPA instead shows a mixed composition, with many genes tissue enhanced or cell-type enhanced in esophageal and intestinal epithelial populations, enterocytes, hepatocytes, and selected immune-cell populations. Several genes have low immune-cell specificity, but LCN2, IQGAP2, PYCARD, HPGD, and related genes show blood or immune-cell associations. Protein detection is broad in both cervix and liver, although ISG15 is not detected in either tissue and some genes show tissue-specific detection differences. Thus, the shared module may partly reflect common epithelial or enterocyte-like cell states, inflammatory or blood-cell admixture, or a conserved response state rather than a cervix-and-liver-specific pathway.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, between MX1 and ISG15. This is consistent with a biologically established antiviral or interferon-linked connection, but it does not establish the entire module as one physical complex. The supplied STRING functional-enrichment result is empty. hu.MAP identifies one partial complex, (hu.MAP huMAP3_01364.1), containing HPGD and MX1 among the module genes, while the remaining members of that complex are outside the module. Most module edges therefore lack corresponding high-confidence STRING support, and most genes have no listed hu.MAP complex assignment. The co-abundance network consequently extends beyond currently catalogued physical interactions and may combine co-regulation, shared cell composition, tissue context, or indirect biology.

**STRING interactions (score >= 0.7)**: 1 of 120 gene pairs: ISG15–MX1 (0.994)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01364.1 (HPGD, MX1; 2/5)

### Novelty

This is not sufficient evidence to call the module a wholly new biological discovery. The MX1-ISG15 relationship is already strongly represented in STRING, and HPGD-MX1 occurs together in a hu.MAP complex, so part of the signal overlaps established biology. Conversely, the broader sixteen-gene co-abundance pattern is not reproduced as a well-supported known interaction network, and there is no STRING functional-enrichment signal. The appropriate conclusion is that the cross-tissue co-abundance configuration may be a potentially novel tissue-pair observation, but its novelty remains provisional. It requires replication, adjustment for cell composition and technical effects, and testing in independent cervix and liver datasets before being considered a new conserved mechanism.

**Hypothesis.** Hypothesis: the module represents a shared epithelial or parenchymal stress state that combines interferon-linked antiviral defense with oxidative, proteostatic, inflammatory, and tissue-metabolic adaptation. MX1 and ISG15 may mark the antiviral component; PYCARD and PSMB8 may represent innate-inflammatory and antigen-processing context; TXN, HSPB1, and CSTB may reflect redox and protein-stress buffering; and CBR1, SCP2, HPGD, SUCLG1, and HIBADH may reflect metabolic adaptation. LCN2 could connect this state to epithelial innate defense and iron-sequestering secretory biology. This is a mechanistic model, not a demonstrated pathway, and the mixed HPA cell-type pattern means that shared cell composition or inflammatory admixture is an important alternative explanation.

### Important genes

#### MX1

- **Related proteins** (co-abundance neighbors): ISG15 (0.93), PYCARD (0.89), CSTB (0.88), HSPB1 (0.83), TXN (0.82), CBR1 (0.82), CZIB (0.82), PSMB8 (0.81); STRING partners: ISG15 (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane, Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_01364.1
- **Function (MyGene.info)**: MX dynamin like GTPase 1. This gene encodes a guanosine triphosphate (GTP)-metabolizing protein that participates in the cellular antiviral response. The encoded protein is induced by type I and type II interferons and antagonizes the replication process of several different RNA and DNA viruses. There is a related gene located adjacent to this gene on chromosome 21, and there are multiple pseudogenes located in a cluster o…
- **Diseases (Open Targets)**: salivary gland disorder (0.217); prostate cancer (0.137); Familial prostate cancer (0.120); cancer (0.108); infection (0.106)
- **Europe PMC papers**: 16839
- **Why important**: MX1 is the highest-connectivity and highest-weighted-strength node in the supplied module. It is annotated as an interferon-induced antiviral GTPase, connects to ISG15 with the strongest STRING relationship in the module, and also links to PYCARD, CSTB, HSPB1, TXN, CBR1, CZIB, and PSMB8. Its large literature base and infection-related disease associations make it the clearest biological anchor.
- **Conclusion**: Established evidence supports MX1 as an antiviral and interferon-responsive marker and as the main network hub. It is reasonable to regard MX1 as a driver or marker of the module’s defense-related component. It is not established that MX1 mechanistically organizes the other co-abundant genes in cervix or liver.

#### ISG15

- **Related proteins** (co-abundance neighbors): MX1 (0.93); STRING partners: MX1 (0.994)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ISG15 ubiquitin like modifier. The protein encoded by this gene is a ubiquitin-like protein that is conjugated to intracellular target proteins upon activation by interferon-alpha and interferon-beta. Several functions have been ascribed to the encoded protein, including chemotactic activity towards neutrophils, direction of ligated target proteins to intermediate filaments, cell-to-cell signaling, and antiviral activity during…
- **Diseases (Open Targets)**: COVID-19 (0.470); bilateral striopallidodentate calcinosis (0.462); Orthomyxoviridae infectious disease (0.375); neoplasm (0.118); infection (0.118)
- **Europe PMC papers**: 17727
- **Why important**: ISG15 forms the module’s only high-confidence STRING pair, with MX1. It is a ubiquitin-like interferon-responsive modifier with reported antiviral, signaling, and neutrophil-related functions, and it has a substantial literature base. Its lack of protein detection in the two named tissues contrasts with its transcript-level module membership and makes it particularly important for interpreting regulation, cell composition, or assay-layer differences.
- **Conclusion**: Established evidence supports ISG15 as an interferon-linked antiviral and immune signaling gene closely related to MX1. Its co-abundance with MX1 strengthens the interpretation of an antiviral response component. The absence of tissue protein detection means that a functional protein-level role in this particular module remains a hypothesis.

#### LCN2

- **Related proteins** (co-abundance neighbors): HPGD (0.81), SUCLG1 (0.81), SCP2 (0.81), IQGAP2 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Endoplasmic reticulum; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lipocalin 2. This gene encodes a protein that belongs to the lipocalin family. Members of this family transport small hydrophobic molecules such as lipids, steroid hormones and retinoids. The protein encoded by this gene is a neutrophil gelatinase-associated lipocalin and plays a role in innate immunity by limiting bacterial growth as a result of sequestering iron-containing siderophores. The presence of this …
- **Diseases (Open Targets)**: psoriasis (0.124); type 2 diabetes mellitus (0.122); acute kidney injury (0.121); coronary artery disorder (0.121); neoplasm (0.120)
- **Europe PMC papers**: 11549
- **Why important**: LCN2 has a central bridging position between the HPGD, SUCLG1, SCP2, and IQGAP2 portion of the network. It is a secreted lipocalin associated with innate defense, iron sequestration, acute-phase response, oxidative stress, bacterium response, epithelial cell types, and several blood-cell populations. Its detection in cervix but not liver and its HPA association with neutrophil-lineage populations are important for evaluating tissue composition and inflammatory admixture.
- **Conclusion**: Established evidence supports LCN2 as an epithelial and innate-defense protein with secretory and blood-cell relevance. It may connect inflammatory state to epithelial or metabolic context in the module. A direct mechanistic bridge from LCN2 to the other module genes is not established by the supplied interaction resources.

#### PYCARD

- **Related proteins** (co-abundance neighbors): MX1 (0.89); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PYD and CARD domain containing. This gene encodes an adaptor protein that is composed of two protein-protein interaction domains: a N-terminal PYRIN-PAAD-DAPIN domain (PYD) and a C-terminal caspase-recruitment domain (CARD). The PYD and CARD domains are members of the six-helix bundle death domain-fold superfamily that mediates assembly of large signaling complexes in the inflammatory and apoptotic signaling pathways via the act…
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.370); neoplasm (0.086); Alzheimer disease (0.086); prostate cancer (0.085); Familial prostate cancer (0.085)
- **Europe PMC papers**: 3928
- **Why important**: PYCARD is a network neighbor of MX1 and encodes an adaptor with interaction domains that assemble inflammatory and apoptotic signaling complexes. Its annotations include innate immune activation, pattern-recognition signaling, antiviral defense, and antigen-presentation-related biology. HPA links it to multiple myeloid and dendritic-cell populations, making it informative for distinguishing a true epithelial response from immune-cell contribution.
- **Conclusion**: Established evidence supports PYCARD as an innate-inflammatory signaling adaptor and supports its relevance to immune-cell composition. Its connection to MX1 in this co-abundance network suggests coordinated defense-state biology, but does not prove direct physical interaction or a shared inflammasome mechanism here.

#### SCP2

- **Related proteins** (co-abundance neighbors): CBR1 (0.81), LCN2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sterol carrier protein 2. This gene encodes two proteins: sterol carrier protein X (SCPx) and sterol carrier protein 2 (SCP2), as a result of transcription initiation from 2 independently regulated promoters. The transcript initiated from the proximal promoter encodes the longer SCPx protein, and the transcript initiated from the distal promoter encodes the shorter SCP2 protein, with the 2 proteins sharing a common C-termi…
- **Diseases (Open Targets)**: sterol carrier protein 2 deficiency (0.708); spermatogenic failure (0.191); stroke disorder (0.187); alcohol drinking (0.186); leukodystrophy (0.119)
- **Europe PMC papers**: 2268
- **Why important**: SCP2 is connected to both CBR1 and LCN2 and is tissue enhanced in liver, with hepatocyte and enterocyte cell-type associations. Its annotations implicate peroxisomal lipid handling, fatty-acid oxidation, steroid biology, and bile-acid metabolism. This makes it a useful metabolic anchor that can connect the immune or epithelial interpretation to liver-relevant cellular metabolism.
- **Conclusion**: Established evidence supports SCP2 as a peroxisomal lipid and sterol metabolism protein with particular relevance to liver-associated cell states. Its placement beside LCN2 suggests a possible metabolic-inflammatory co-abundance relationship. The supplied data do not establish that SCP2 participates directly in antiviral signaling.

#### HPGD

- **Related proteins** (co-abundance neighbors): LCN2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_01364.1
- **Function (MyGene.info)**: 15-hydroxyprostaglandin dehydrogenase. This gene encodes a member of the short-chain nonmetalloenzyme alcohol dehydrogenase protein family. The encoded enzyme is responsible for the metabolism of prostaglandins, which function in a variety of physiologic and cellular processes such as inflammation. Mutations in this gene result in primary autosomal recessive hypertrophic osteoarthropathy and cranioosteoarthropathy. Multiple transcript …
- **Diseases (Open Targets)**: hypertrophic osteoarthropathy, primary, autosomal recessive, 1 (0.756); cranio-osteoarthropathy (0.707); isolated congenital digital clubbing (0.695); primary hypertrophic osteoarthropathy (0.561); hereditary disease (0.193)
- **Europe PMC papers**: 1939
- **Why important**: HPGD is the module member appearing with MX1 in the partial hu.MAP complex (hu.MAP huMAP3_01364.1), and it connects to LCN2 in the co-abundance graph. It metabolizes prostaglandins and is associated with inflammatory physiology, pregnancy and parturition, and disease involving abnormal bone and connective-tissue phenotypes. Its epithelial and selected immune-cell annotations make it relevant to both tissue biology and inflammatory context.
- **Conclusion**: Established evidence supports HPGD as a prostaglandin-metabolizing enzyme and confirms a partial complex-level association with MX1 in the supplied hu.MAP result. Its co-abundance with LCN2 and MX1 may indicate coordination between lipid mediator turnover and defense state. Whether HPGD functionally regulates the proposed module is a hypothesis.

## Module 2

**Tissue pair**: cervix_uterine and liver  
**Genes (49)**: SLC3A2, ACLY, ATP2A2, CKAP4, DDX5, DDX6, DHCR24, DHX9, DPYSL2, EIF3L, FKBP4, FLOT1, FSCN1, FUS, G6PD, HNRNPK, HNRNPR, KRT18, KRT8, LUC7L2, LMNB1, LMNB2, MATR3, IGF2R, NDUFS2, NOP56, NUP155, NUCB2, NUP93, PCNA, NUP210, PPM1G, PTBP1, CAD, RUVBL2, SEC23IP, SERPINH1, SF3A1, SF3B3, SUPT16H, SRP54, SRP68, SRRT, SRSF7, DARS1, NARS1, TOMM40, EFTUD2, ZFR

### Function

The module is best interpreted as a conserved nuclear gene-expression and RNA-processing module, with a particularly strong spliceosome and pre-mRNA splicing component. The primary evidence is the globally corrected enrichment for nucleic-acid binding (GO:MF nucleic acid binding; q_global = 3.72e-07), RNA binding (GO:MF RNA binding; q_global = 4.03e-05), ribonucleoprotein complexes (GO:CC ribonucleoprotein complex; q_global = 0.000186), nuclear protein-containing complexes (GO:CC nuclear protein-containing complex; q_global = 0.001), RNA processing (GO:BP RNA processing; q_global = 0.00163), RNA splicing (GO:BP RNA splicing; q_global = 0.00207), spliceosome-mediated splicing (GO:BP mRNA splicing, via spliceosome; q_global = 0.00331), mRNA processing (GO:BP mRNA processing; q_global = 0.00864), the catalytic step two spliceosome (GO:CC catalytic step 2 spliceosome; q_global = 0.0201), mRNA metabolism (GO:BP mRNA metabolic process; q_global = 0.0383), mRNA binding (GO:MF mRNA binding; q_global = 0.0448), and the human spliceosome pathway (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0479). Nuclear localization is also supported by (GO:CC nuclear lumen; q_global = 0.000599), (GO:CC nucleus; q_global = 0.00343), and (GO:CC nucleoplasm; q_global = 0.0412). The network contains a densely connected RNA-binding and spliceosomal core, including DDX5, DHX9, EFTUD2, HNRNPK, HNRNPR, PTBP1, SF3A1, SF3B3, SRSF7, and SRRT, alongside nuclear-pore, nuclear-lamina, translation-targeting, metabolic, epithelial, and membrane-associated genes. Thus, the most defensible function is coordinated RNA maturation, spliceosome activity, nuclear transport, and associated expression-state regulation rather than a narrowly tissue-specific pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a small secreted subset, and most annotated proteins are intracellular, especially nuclear or nucleoplasmic. It is also not strongly blood-cell specific overall: most genes have low immune-cell specificity, although selected genes show enhancement in neutrophils, progenitors, or other hematopoietic populations. Most genes have low tissue specificity, consistent with a broadly expressed housekeeping-like program. The module includes tissue-enhanced genes such as DHCR24 in liver and several genes with bone-marrow, lymphoid, reproductive, epithelial, or muscle-associated signals, but these do not override the dominant ubiquitous nuclear RNA-processing signature. Detection in both cervix_uterine and liver supports technical and biological presence in both tissues, while the isolated non-detection of selected genes in one tissue cautions that the module may also reflect differing cell composition or expression intensity. The data do not support interpreting this module primarily as blood contamination.

**GO/KEGG enrichment**: 18 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleic acid binding | 3.72e-07 | ATP2A2, CKAP4, DARS1, DDX5, DDX6, DHX9, EFTUD2, EIF3L, FKBP4, FSCN1, FUS, HNRNPK, HNRNPR, KRT18, LMNB1, LUC7L2, MATR3, NARS1, NOP56, NUCB2, PCNA, PTBP1, RUVBL2, SEC23IP, SERPINH1, SF3A1, SF3B3, SLC3A2, SRP54, SRP68, SRRT, SRSF7, SUPT16H, ZFR |
| GO:MF RNA binding | 4.03e-05 | ATP2A2, CKAP4, DARS1, DDX5, DDX6, DHX9, EFTUD2, EIF3L, FKBP4, FSCN1, FUS, HNRNPK, HNRNPR, KRT18, LUC7L2, MATR3, NOP56, PTBP1, SEC23IP, SERPINH1, SF3A1, SF3B3, SLC3A2, SRP54, SRP68, SRRT, SRSF7, SUPT16H, ZFR |
| GO:CC ribonucleoprotein complex | 0.000186 | DDX5, DDX6, DHX9, EFTUD2, EIF3L, HNRNPK, HNRNPR, LUC7L2, NOP56, RUVBL2, SF3A1, SF3B3, SRP54, SRP68, SRRT |
| GO:CC nuclear lumen | 0.000599 | ACLY, CAD, CKAP4, DDX5, DHX9, EFTUD2, EIF3L, FKBP4, FUS, HNRNPK, HNRNPR, KRT18, KRT8, LMNB1, LMNB2, LUC7L2, MATR3, NOP56, NUP93, PCNA, PPM1G, PTBP1, RUVBL2, SF3A1, SF3B3, SLC3A2, SRP54, SRP68, SRRT, SRSF7, SUPT16H |
| GO:CC nuclear protein-containing complex | 0.001 | DDX5, EFTUD2, FLOT1, HNRNPK, HNRNPR, LUC7L2, NOP56, NUP155, NUP210, NUP93, PCNA, RUVBL2, SF3A1, SF3B3, SUPT16H |
| GO:BP RNA processing | 0.00163 | DDX5, DHX9, EFTUD2, FUS, HNRNPK, HNRNPR, LUC7L2, NOP56, NUP155, PTBP1, SF3A1, SF3B3, SRRT, SRSF7 |
| GO:BP RNA splicing | 0.00207 | DDX5, DHX9, EFTUD2, FUS, HNRNPK, HNRNPR, LUC7L2, PTBP1, SF3A1, SF3B3, SRSF7 |
| GO:BP RNA splicing, via transesterification reactions | 0.00331 | DDX5, DHX9, EFTUD2, HNRNPK, HNRNPR, LUC7L2, PTBP1, SF3A1, SF3B3, SRSF7 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.00331 | DDX5, DHX9, EFTUD2, HNRNPK, HNRNPR, LUC7L2, PTBP1, SF3A1, SF3B3, SRSF7 |
| GO:BP mRNA splicing, via spliceosome | 0.00331 | DDX5, DHX9, EFTUD2, HNRNPK, HNRNPR, LUC7L2, PTBP1, SF3A1, SF3B3, SRSF7 |
| GO:CC nucleus | 0.00343 | ACLY, CAD, CKAP4, DDX5, DDX6, DHCR24, DHX9, EFTUD2, EIF3L, FKBP4, FLOT1, FUS, HNRNPK, HNRNPR, IGF2R, KRT18, KRT8, LMNB1, LMNB2, LUC7L2, MATR3, NOP56, NUCB2, NUP155, NUP210, NUP93, PCNA, PPM1G, PTBP1, RUVBL2, SF3A1, SF3B3, SLC3A2, SRP54, SRP68, SRRT, SRSF7, SUPT16H, ZFR |
| GO:BP mRNA processing | 0.00864 | DDX5, DHX9, EFTUD2, HNRNPK, HNRNPR, LUC7L2, PTBP1, SF3A1, SF3B3, SRRT, SRSF7 |
| GO:BP regulatory ncRNA-mediated gene silencing | 0.0201 | DDX5, DDX6, DHX9, HNRNPK, NUP155, SRRT |
| GO:CC catalytic step 2 spliceosome | 0.0201 | DDX5, EFTUD2, HNRNPK, HNRNPR, SF3A1, SF3B3 |
| GO:BP mRNA metabolic process | 0.0383 | DDX5, DHX9, EFTUD2, FUS, HNRNPK, HNRNPR, LUC7L2, PTBP1, SF3A1, SF3B3, SRRT, SRSF7 |

### STRING and hu.MAP

STRING provides substantial support for an established RNA-processing interaction neighborhood. Particularly strong relationships include DDX5 with DHX9, HNRNPK, HNRNPR, MATR3, and SRRT; DHX9 with several heterogeneous nuclear ribonucleoproteins and splicing factors; EFTUD2 with SF3A1 and SF3B3; HNRNPK with HNRNPR, MATR3, PTBP1, SF3B3, SRRT, and SRSF7; the SF3A1-SF3B3 pair; the NUP155-NUP210-NUP93 group; the LMNB1-LMNB2 pair; and the SRP54-SRP68 pair. STRING supplementary enrichment independently points to mRNA processing, capped pre-mRNA processing, major-pathway mRNA splicing, RNA metabolism, and nuclear compartments (STRING WikiPathways mRNA processing; within-query FDR = 9.46e-06), (STRING RCTM Processing of Capped Intron-Containing Pre-mRNA; within-query FDR = 3.37e-05), (STRING RCTM Metabolism of RNA; within-query FDR = 0.0003), (STRING RCTM mRNA Splicing - Major Pathway; within-query FDR = 0.00035), (STRING COMPARTMENTS Nucleoplasm; within-query FDR = 0.00041), and (STRING Component Ribonucleoprotein complex; within-query FDR = 0.00055), but these are supplementary rather than globally corrected evidence. hu.MAP supports several coherent complexes: heterogeneous nuclear ribonucleoprotein assemblies containing HNRNPR, MATR3, HNRNPK, and ZFR (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_07581.1); SR-related splicing assemblies containing SRSF7, SRRT, and LUC7L2 (hu.MAP huMAP3_09587.1) (hu.MAP huMAP3_10564.1) (hu.MAP huMAP3_09621.1) (hu.MAP huMAP3_11073.1) (hu.MAP huMAP3_09943.1); spliceosomal assemblies containing EFTUD2, SF3B3, and SF3A1 (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_04549.1), and (hu.MAP huMAP3_06511.1); nuclear-pore assemblies containing NUP155 and NUP210 (hu.MAP huMAP3_07645.1); and nuclear-lamina assemblies containing LMNB1 and LMNB2 (hu.MAP huMAP3_03501.1) (hu.MAP huMAP3_00325.1) (hu.MAP huMAP3_13519.1) (hu.MAP huMAP3_10433.1), (hu.MAP huMAP3_09259.1), (hu.MAP huMAP3_10492.1), and (hu.MAP huMAP3_10614.1). These concordant resources indicate that much of the module reflects known molecular machinery. They do not, by themselves, prove that the complete co-abundance module is a physical complex or that every edge is direct.

**STRING interactions (score >= 0.7)**: 51 of 1176 gene pairs: ACLY–G6PD (0.785); ACLY–NDUFS2 (0.797); DDX5–DHX9 (0.996); DDX5–FUS (0.872); DDX5–HNRNPK (0.935); DDX5–HNRNPR (0.844); DDX5–MATR3 (0.894); DDX5–SRRT (0.855); DDX6–DHX9 (0.967); DDX6–HNRNPK (0.748); DHX9–FUS (0.87); DHX9–HNRNPK (0.939); DHX9–HNRNPR (0.909); DHX9–MATR3 (0.786); DHX9–PTBP1 (0.868); DHX9–SF3B3 (0.73); DHX9–SRRT (0.92); DHX9–SRSF7 (0.789); EFTUD2–PTBP1 (0.771); EFTUD2–RUVBL2 (0.793); EFTUD2–SF3A1 (0.999); EFTUD2–SF3B3 (0.999); EFTUD2–SRSF7 (0.751); FUS–HNRNPK (0.927); FUS–HNRNPR (0.869); FUS–MATR3 (0.91); FUS–PTBP1 (0.852); HNRNPK–HNRNPR (0.962); HNRNPK–MATR3 (0.923); HNRNPK–PTBP1 (0.997); HNRNPK–SF3B3 (0.971); HNRNPK–SRRT (0.868); HNRNPK–SRSF7 (0.896); HNRNPR–MATR3 (0.714); HNRNPR–PTBP1 (0.875); HNRNPR–SRSF7 (0.833); HNRNPR–ZFR (0.793); KRT18–KRT8 (0.999); LMNB1–LMNB2 (0.999); LUC7L2–SF3A1 (0.835); LUC7L2–SF3B3 (0.823); LUC7L2–SRSF7 (0.874); MATR3–PTBP1 (0.83); NOP56–RUVBL2 (0.847); NUP155–NUP210 (0.991); NUP155–NUP93 (0.999); NUP210–NUP93 (0.993); PTBP1–SRRT (0.78); PTBP1–SRSF7 (0.933); SF3A1–SF3B3 (0.999); SRP54–SRP68 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Nucleic acid binding (FDR = 1.73e-06, 33 genes); WikiPathways mRNA processing (FDR = 9.46e-06, 11 genes); Keyword Isopeptide bond (FDR = 1.53e-05, 24 genes); Keyword Ubl conjugation (FDR = 1.72e-05, 25 genes); RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 3.37e-05, 14 genes); COMPARTMENTS Nuclear lumen (FDR = 6.76e-05, 21 genes); Keyword Nucleus (FDR = 7e-05, 30 genes); Function RNA binding (FDR = 8.05e-05, 28 genes); RCTM Metabolism of RNA (FDR = 0.0003, 16 genes); Component Nuclear lumen (FDR = 0.00034, 31 genes); RCTM mRNA Splicing - Major Pathway (FDR = 0.00035, 11 genes); COMPARTMENTS Nucleoplasm (FDR = 0.00041, 15 genes); Component Ribonucleoprotein complex (FDR = 0.00055, 15 genes); COMPARTMENTS Nucleus (FDR = 0.00057, 32 genes); Component Nucleus (FDR = 0.0013, 39 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPR, MATR3, HNRNPK, ZFR; 4/57); huMAP3_07581.1 (HNRNPR, MATR3, ZFR; 3/21); huMAP3_09587.1 (SRSF7, SRRT, LUC7L2; 3/21); huMAP3_10564.1 (SRSF7, SRRT, LUC7L2; 3/37); huMAP3_09621.1 (SRSF7, SRRT, LUC7L2; 3/56); huMAP3_11073.1 (SRSF7, SRRT, LUC7L2; 3/67); huMAP3_09943.1 (SRSF7, SRRT, LUC7L2; 3/78); huMAP3_08980.1 (EFTUD2, SF3B3, SF3A1; 3/97); huMAP3_03501.1 (LMNB1, LMNB2; 2/2); huMAP3_00325.1 (LMNB1, LMNB2; 2/3); huMAP3_13519.1 (LMNB1, LMNB2; 2/4); huMAP3_10433.1 (LMNB1, LMNB2; 2/5); huMAP3_07817.1 (MATR3, ZFR; 2/5); huMAP3_08817.1 (MATR3, ZFR; 2/6); huMAP3_07645.1 (NUP155, NUP210; 2/7); huMAP3_09259.1 (LMNB1, LMNB2; 2/8); huMAP3_09490.1 (SRRT, LUC7L2; 2/9); huMAP3_10492.1 (LMNB1, LMNB2; 2/9); huMAP3_10614.1 (LMNB1, LMNB2; 2/9); huMAP3_06081.1 (SRSF7, SRRT; 2/13); huMAP3_09281.1 (HNRNPR, ZFR; 2/14); huMAP3_09223.1 (MATR3, ZFR; 2/15); huMAP3_06391.1 (SRSF7, SRRT; 2/16); huMAP3_07267.1 (SRSF7, SRRT; 2/16); huMAP3_10473.1 (ATP2A2, LMNB1; 2/24); huMAP3_10659.1 (HNRNPR, HNRNPK; 2/28); huMAP3_14523.1 (FUS, HNRNPK; 2/33); huMAP3_10862.1 (PPM1G, SUPT16H; 2/33); huMAP3_04549.1 (SF3B3, SF3A1; 2/52); huMAP3_14306.1 (PPM1G, RUVBL2; 2/55); huMAP3_06247.1 (ATP2A2, DHCR24; 2/65); huMAP3_06511.1 (SF3B3, SF3A1; 2/79); huMAP3_09592.1 (ATP2A2, DHCR24; 2/95)

### Novelty

The module should not be called a wholly new molecular pathway. Its central RNA-binding, spliceosomal, nuclear-pore, and nuclear-lamina relationships are already represented in STRING and hu.MAP, and its dominant functional themes are established by GO and KEGG. The potentially novel result is the conserved co-abundance organization of these otherwise partly separate systems across cervix_uterine and liver, including their association with metabolic, membrane, epithelial, and trafficking genes. Database absence for some genes or edges is not evidence of novelty, because incomplete coverage, indirect associations, tissue context, and co-expression-specific relationships can all explain missing records. A strong novelty claim would require replication in independent cohorts, preservation after adjustment for cell composition and technical effects, and experimental or perturbational validation of the cross-system coupling.

**Hypothesis.** Hypothesis: in both cervix_uterine and liver, a shared cellular state coordinates transcriptional output with RNA maturation, spliceosome assembly, nuclear export, and proteome-supporting metabolism. The RNA-binding and spliceosomal core may regulate transcript processing, while the nuclear-pore and lamina components organize transport and nuclear architecture. Coupling to SLC3A2, ACLY, CAD, DHCR24, SRP54, SRP68, and related trafficking or metabolic genes may reflect the demand to translate, target, and process proteins during this state. Epithelial, stromal, hepatic, or progenitor-related genes could represent cell-state context rather than a single universal mechanism. This is a hypothesis from co-abundance and annotations, not proof of direct regulation or a shared cell type.

### Important genes

#### DDX5

- **Related proteins** (co-abundance neighbors): SLC3A2 (0.91), EFTUD2 (0.89), FKBP4 (0.86), TOMM40 (0.86), MATR3 (0.86), SUPT16H (0.85), LMNB1 (0.84), DDX6 (0.84), HNRNPR (0.84), DHX9 (0.84), HNRNPK (0.84), SERPINH1 (0.84), CAD (0.83), SEC23IP (0.83), NUP93 (0.83), LUC7L2 (0.83), PPM1G (0.83), NOP56 (0.83), SRRT (0.82), EIF3L (0.82), CKAP4 (0.82), NUP155 (0.81), DHCR24 (0.80); STRING partners: DHX9 (0.996), FUS (0.872), HNRNPK (0.935), HNRNPR (0.844), MATR3 (0.894), SRRT (0.855)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 5. This gene encodes a member of the DEAD box family of RNA helicases that are involved in a variety of cellular processes as a result of its role as an adaptor molecule, promoting interactions with a large number of other factors. This protein is involved in pathways that include the alteration of RNA structures, plays a role as a coregulator of transcription, a regulator of splicing, and in the pro…
- **Diseases (Open Targets)**: COVID-19 (0.374); severe acute respiratory syndrome (0.371); colon adenocarcinoma (0.370); colorectal adenocarcinoma (0.370); dengue disease (0.370)
- **Europe PMC papers**: 4163
- **Why important**: DDX5 is among the most network-connected genes in the module and links the central RNA-processing neighborhood to DHX9, FUS, HNRNPK, HNRNPR, MATR3, SRRT, and DDX6 in STRING. It is present across the globally corrected nucleic-acid binding, RNA-binding, ribonucleoprotein, RNA-processing, splicing, mRNA-processing, mRNA-binding, and spliceosome terms (GO:MF nucleic acid binding; q_global = 3.72e-07) (GO:MF RNA binding; q_global = 4.03e-05) (GO:CC ribonucleoprotein complex; q_global = 0.000186), (13 globally significant GO/KEGG terms, q_global 0.00163–0.0479; see the table). Its annotation describes an RNA helicase and adaptor involved in RNA structure, transcriptional regulation, splicing, and small noncoding RNA processing. It has extensive literature and disease-related associations, making it a strong representative hub.
- **Conclusion**: Established evidence supports DDX5 as a central RNA-processing and splicing-associated component of the module. It is plausible that DDX5 helps coordinate the module's RNA-processing neighborhood, but the co-abundance data do not establish that it drives the shared tissue pattern.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): SF3A1 (0.95), SLC3A2 (0.92), NUP210 (0.92), PPM1G (0.90), DDX5 (0.89), SRP54 (0.89), HNRNPK (0.88), DHX9 (0.88), SRP68 (0.88), SF3B3 (0.87), SRRT (0.87), NUP93 (0.87), HNRNPR (0.87), IGF2R (0.86), SUPT16H (0.86), ZFR (0.85), DHCR24 (0.85), MATR3 (0.83), NUP155 (0.83), EIF3L (0.82), SEC23IP (0.81), FKBP4 (0.81), ACLY (0.80), RUVBL2 (0.80), LMNB1 (0.80); STRING partners: PTBP1 (0.771), RUVBL2 (0.793), SF3A1 (0.999), SF3B3 (0.999), SRSF7 (0.751)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 has the strongest network position in the supplied module ranking and connects to spliceosomal, nuclear, transport, and ribonucleoprotein genes. It is represented across many globally corrected terms, including RNA processing, RNA splicing, the catalytic step two spliceosome, and the KEGG spliceosome term (GO:CC ribonucleoprotein complex; q_global = 0.000186), (8 globally significant GO/KEGG terms, q_global 0.001–0.00864; see the table), (GO:CC catalytic step 2 spliceosome; q_global = 0.0201) (GO:BP mRNA metabolic process; q_global = 0.0383) (GO:CC nucleoplasm; q_global = 0.0412), and (KEGG Spliceosome - Homo sapiens (human); q_global = 0.0479). STRING shows very strong relationships with SF3A1 and SF3B3, and hu.MAP places EFTUD2 with these spliceosomal components (hu.MAP huMAP3_08980.1). Its established function is as a spliceosome-associated GTPase involved in spliceosome assembly and conformational change, with a disease association to mandibulofacial dysostosis with microcephaly.
- **Conclusion**: Established evidence identifies EFTUD2 as a core spliceosomal anchor and a strong mechanistic marker of the module's principal function. Its network centrality supports importance, but does not demonstrate tissue-specific causal activity.

#### SF3A1

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.95), FKBP4 (0.90), SLC3A2 (0.90), PTBP1 (0.87), EIF3L (0.87), IGF2R (0.87), ATP2A2 (0.85), NUP210 (0.85), PPM1G (0.85), RUVBL2 (0.85), ACLY (0.85), SEC23IP (0.84), HNRNPR (0.84), SUPT16H (0.83), NARS1 (0.81), NOP56 (0.81), SRRT (0.80); STRING partners: EFTUD2 (0.999), LUC7L2 (0.835), SF3B3 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_08980.1, huMAP3_04549.1, huMAP3_06511.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a U2 small nuclear ribonucleoprotein component and is strongly connected to EFTUD2, SF3B3, PTBP1, LUC7L2, and other module genes. It appears in the globally corrected RNA-binding, ribonucleoprotein, RNA-processing, splicing, catalytic step two spliceosome, mRNA-processing, mRNA-binding, and KEGG spliceosome terms (GO:MF nucleic acid binding; q_global = 3.72e-07) (GO:MF RNA binding; q_global = 4.03e-05) (GO:CC ribonucleoprotein complex; q_global = 0.000186), (7 globally significant GO/KEGG terms, q_global 0.00163–0.00864; see the table), (5 globally significant GO/KEGG terms, q_global 0.0201–0.0479; see the table). STRING supports its relationships with EFTUD2 and SF3B3, while hu.MAP places SF3A1 and SF3B3 in multiple spliceosomal complexes (hu.MAP huMAP3_08980.1), (hu.MAP huMAP3_04549.1), and (hu.MAP huMAP3_06511.1). Its disease associations include neurodevelopmental and other disorders, although those associations do not specifically explain this module.
- **Conclusion**: Established evidence supports SF3A1 as a core U2-spliceosome component that reinforces the interpretation of the module as RNA splicing machinery. Its co-abundance with non-spliceosomal genes is consistent with coordinated cellular state, but the direction and mechanism of that coordination remain unresolved.

#### HNRNPK

- **Related proteins** (co-abundance neighbors): SUPT16H (0.89), EFTUD2 (0.88), NUP155 (0.87), SF3B3 (0.85), DDX5 (0.84), SLC3A2 (0.83), SRRT (0.83), NUP93 (0.83), ZFR (0.83), MATR3 (0.83), LMNB1 (0.82), HNRNPR (0.81); STRING partners: DDX5 (0.935), DDX6 (0.748), DHX9 (0.939), FUS (0.927), HNRNPR (0.962), MATR3 (0.923), PTBP1 (0.997), SF3B3 (0.971), SRRT (0.868), SRSF7 (0.896)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_10659.1, huMAP3_14523.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein K. This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in …
- **Diseases (Open Targets)**: Au-Kline syndrome (0.787); neurodevelopmental disorder-craniofacial dysmorphism-cardiac defect-hip dysplasia syndrome (0.687); hereditary disease (0.507); neurodegenerative disease (0.466); dengue disease (0.463)
- **Europe PMC papers**: 3619
- **Why important**: HNRNPK occupies a highly connected position within the RNA-binding subnetwork and has STRING relationships with DDX5, DHX9, FUS, HNRNPR, MATR3, PTBP1, SF3B3, SRRT, and SRSF7. It is included in every major globally corrected RNA-binding, RNA-processing, splicing, mRNA-processing, mRNA-binding, and spliceosome-related category listed for the module (GO:MF nucleic acid binding; q_global = 3.72e-07) (GO:MF RNA binding; q_global = 4.03e-05) (GO:CC ribonucleoprotein complex; q_global = 0.000186), (13 globally significant GO/KEGG terms, q_global 0.00163–0.0479; see the table). hu.MAP places it in heterogeneous nuclear ribonucleoprotein complexes with HNRNPR, MATR3, and ZFR, and in a complex with FUS (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_10659.1), and (hu.MAP huMAP3_14523.1). Its established roles include pre-mRNA processing, RNA metabolism, transcriptional regulation, and signal-linked gene regulation, with substantial developmental and hereditary disease literature.
- **Conclusion**: Established evidence supports HNRNPK as an integrative RNA-binding and transcriptional regulator within the module. It is a plausible bridge between splicing and broader gene-expression control, but this bridging role is a hypothesis rather than a demonstrated causal property of this module.

#### DHX9

- **Related proteins** (co-abundance neighbors): SUPT16H (0.92), NUP210 (0.90), EFTUD2 (0.88), MATR3 (0.87), SLC3A2 (0.87), ACLY (0.85), SF3B3 (0.84), DDX5 (0.84), SRRT (0.84), NOP56 (0.84), NUP155 (0.82), SEC23IP (0.82), IGF2R (0.81), HNRNPR (0.81), DHCR24 (0.81); STRING partners: DDX5 (0.996), DDX6 (0.967), FUS (0.87), HNRNPK (0.939), HNRNPR (0.909), MATR3 (0.786), PTBP1 (0.868), SF3B3 (0.73), SRRT (0.92), SRSF7 (0.789)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a well-connected RNA helicase in the module and has strong STRING relationships with DDX5, DDX6, FUS, HNRNPK, HNRNPR, MATR3, PTBP1, SF3B3, SRRT, and SRSF7. It occurs in the globally corrected nucleic-acid binding, RNA-binding, ribonucleoprotein, RNA-processing, splicing, mRNA-processing, mRNA-binding, and spliceosome categories (GO:MF nucleic acid binding; q_global = 3.72e-07) (GO:MF RNA binding; q_global = 4.03e-05) (GO:CC ribonucleoprotein complex; q_global = 0.000186), (8 globally significant GO/KEGG terms, q_global 0.00163–0.0201; see the table), (4 globally significant GO/KEGG terms, q_global 0.0383–0.0479; see the table). Its annotation supports ATP-dependent unwinding of RNA and DNA-RNA complexes, transcriptional regulation, alternative splicing, and interferon-related regulation. It also has substantial literature and disease associations.
- **Conclusion**: Established evidence supports DHX9 as a multifunctional RNA helicase that connects RNA processing with transcriptional and nucleic-acid regulatory functions. Its position makes it a plausible coordinator of the module's RNA-centered interactions, but the cross-tissue coordination remains an untested hypothesis.

## Module 3

**Tissue pair**: cervix_uterine and liver  
**Genes (15)**: LRG1, A2M, APOD, CP, CFB, C3, C9, CES2, RAP1GDS1, GBE1, ITIH4, PCCB, NAPRT, PPCS, ALDH5A1

### Function

The strongest supported interpretation is a secreted hepatic and extracellular complement-associated module, centered on alternative-pathway activity. The primary evidence is (GO:BP complement activation, alternative pathway; q_global = 0.0388), in which C3, CFB, and C9 jointly support complement activation through the alternative pathway. C3 is a central complement component, CFB supplies the alternative-pathway convertase protease activity, and C9 is a terminal membrane-attack-complex component. The broader pattern is consistent with extracellular protease regulation, acute-phase biology, lipid or metal transport, and tissue injury responses, but these additional interpretations are supported only by supplementary STRING terms and by the supplied gene annotations. The module is not a uniform intracellular metabolic pathway: a smaller set of genes, including CES2, ALDH5A1, GBE1, RAP1GDS1, PPCS, PCCB, and NAPRT, has liver-associated metabolic or biosynthetic functions and may represent a secondary co-abundance component.

**Cell composition.** The module is strongly biased toward secreted or plasma-associated proteins. HPA identifies nine secreted genes, and (STRING TISSUES Plasma cell; within-query FDR = 0.00019), (STRING Keyword Signal; within-query FDR = 0.0045), and (STRING Keyword Secreted; within-query FDR = 0.0073) support plasma-cellular, signal-peptide, and secreted-protein characteristics. Ten genes are liver-enriched in HPA, and hepatocytes are the most frequent enriched single-cell population. This makes hepatocyte production and circulating protein abundance a plausible major source of the shared signal. The module does not appear primarily blood-cell derived: most genes have low immune-cell specificity or are not detected in immune cells, although selected genes show enrichment in neutrophils, memory B cells, non-classical monocytes, or gdT cells. The shared cervix and liver module could therefore partly reflect circulating plasma proteins or common extracellular material in the samples rather than a cervix-specific cellular program. HPA protein detection is incomplete in both tissues, so absence of tissue staining should not be treated as evidence of absent transcript-level co-abundance.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP complement activation, alternative pathway | 0.0388 | C3, C9, CFB |

### STRING and hu.MAP

STRING provides a concentrated set of known relationships around C3, CFB, CP, A2M, and ITIH4. The strongest reported link is C3 with CFB, while C3 also connects to CP and ITIH4, and A2M connects to CFB and CP. These interactions support a biologically coherent extracellular complement and protease-regulatory neighborhood rather than an entirely arbitrary gene grouping. hu.MAP independently places CP, CFB, A2M, C3, and ITIH4 together across several serum-protein-rich complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_10678.1), with additional partial complex support in (hu.MAP huMAP3_08395.1) through (hu.MAP huMAP3_09434.1). The repeated presence of these genes in complexes containing many other plasma proteins suggests that the core is already represented in known extracellular protein assemblies. Conversely, CES2, ALDH5A1, GBE1, RAP1GDS1, PPCS, PCCB, NAPRT, C9, APOD, LRG1, and several other module members lack corresponding reported STRING or hu.MAP relationships in the supplied data. Thus, the network combines a known plasma-protein core with weaker or potentially indirect co-abundance links.

**STRING interactions (score >= 0.7)**: 5 of 105 gene pairs: A2M–CFB (0.726); A2M–CP (0.889); C3–CFB (0.999); C3–CP (0.751); C3–ITIH4 (0.745)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Plasma cell (FDR = 0.00019, 8 genes); Keyword Disulfide bond (FDR = 0.0012, 10 genes); Keyword Signal (FDR = 0.0045, 9 genes); Keyword Secreted (FDR = 0.0073, 8 genes); Keyword Glycoprotein (FDR = 0.0076, 9 genes); Keyword Age-related macular degeneration (FDR = 0.0076, 3 genes); Keyword Complement alternate pathway (FDR = 0.008, 3 genes); PMID (2022) Effects of Omega-3 and Antioxidant Cocktail Supplement on Prolonged Bed Rest: Results from Serum Proteome and Sphingolipids Analysis. (FDR = 0.0327, 7 genes); PMID (2017) Identification of candidate diagnostic serum biomarkers for Kawasaki disease using proteomic analysis. (FDR = 0.0327, 6 genes); PMID (2012) Serum profiling of leptospirosis patients to investigate proteomic alterations. (FDR = 0.0327, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09531.1 (CP, CFB, A2M, C3, ITIH4; 5/47); huMAP3_10101.1 (CP, CFB, A2M, C3, ITIH4; 5/49); huMAP3_15040.1 (CP, CFB, A2M, C3, ITIH4; 5/64); huMAP3_10678.1 (CP, CFB, A2M, C3, ITIH4; 5/71); huMAP3_08395.1 (CP, CFB, A2M, C3; 4/43); huMAP3_09273.1 (CP, CFB, A2M; 3/28); huMAP3_08796.1 (CFB, ITIH4; 2/15); huMAP3_07432.1 (CP, C3; 2/18); huMAP3_09832.1 (CFB, ITIH4; 2/18); huMAP3_07265.1 (CP, A2M; 2/20); huMAP3_07701.1 (CFB, A2M; 2/22); huMAP3_09434.1 (C3, ITIH4; 2/33)

### Novelty

The individual biology is not new: complement activation, hepatic secretion, plasma transport, and the relationships among C3, CFB, A2M, CP, and ITIH4 are established by (GO:BP complement activation, alternative pathway; q_global = 0.0388), STRING, hu.MAP, and the supplied literature annotations. The potentially novel observation is the conserved co-abundance organization of this particular mixture across cervix_uterine and liver, especially the coupling of a known secreted complement core to liver metabolic genes and to genes with sparse interaction-resource support. This should be described as a new network-level observation rather than a newly discovered complement mechanism. The absence of STRING or hu.MAP support for some module edges does not establish novelty, because those resources are incomplete and the co-abundance edges may reflect shared regulation, secretion, tissue composition, or indirect biology. Independent replication, adjustment for plasma contamination and cell composition, and experimental validation would be required before claiming a novel mechanism.

**Hypothesis.** Hypothesis: the conserved module reflects a circulating hepatocyte-derived extracellular program in which hepatic secretion of complement and protease-regulatory proteins is co-regulated with tissue metabolic and stress-response programs. Within this model, C3 and CFB form the alternative-pathway core, C9 represents downstream membrane-attack-complex capacity, ITIH4 and A2M modulate extracellular proteolysis or inflammatory signaling, and CP and APOD contribute metal-handling or lipid-transport context. The cervix signal may arise partly from exposure to or retention of circulating proteins and partly from shared secretory or stromal cell states. The links to CES2, ALDH5A1, GBE1, RAP1GDS1, PPCS, PCCB, and NAPRT may indicate coordinated hepatic metabolic state, but this is a hypothesis rather than evidence that these intracellular enzymes participate directly in the complement machinery.

### Important genes

#### C3

- **Related proteins** (co-abundance neighbors): ITIH4 (0.89), CFB (0.85), CP (0.85), PCCB (0.83), CES2 (0.82); STRING partners: CFB (0.999), CP (0.751), ITIH4 (0.745)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_07432.1, huMAP3_09434.1
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is the highest-connectivity complement-centered gene in the module and connects in STRING to CFB, CP, and ITIH4. It is one of the genes in the globally corrected primary term (GO:BP complement activation, alternative pathway; q_global = 0.0388), is liver-enriched and secreted to blood in HPA, and has extensive disease and literature support involving complement deficiency, complement-mediated renal disease, atypical hemolytic-uremic syndrome, and age-related macular degeneration.
- **Conclusion**: Established evidence: C3 is the principal anchor of the module's alternative-pathway interpretation and a major secreted hepatic complement component. Hypothesis: variation in C3 abundance may coordinate the module's broader extracellular inflammatory signal, but the co-abundance data do not establish pathway activation or causality.

#### CFB

- **Related proteins** (co-abundance neighbors): C3 (0.85), ITIH4 (0.85); STRING partners: A2M (0.726), C3 (0.999)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_07701.1
- **Function (MyGene.info)**: complement factor B. This gene encodes complement factor B, a component of the alternative pathway of complement activation. Factor B circulates in the blood as a single chain polypeptide. Upon activation of the alternative pathway, it is cleaved by complement factor D yielding the noncatalytic chain Ba and the catalytic subunit Bb. The active subunit Bb is a serine protease which associates with C3b to form the alter…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with B factor anomaly (0.764); atypical hemolytic-uremic syndrome (0.705); Immunodeficiency due to a complement cascade protein anomaly (0.614); paroxysmal nocturnal hemoglobinuria (0.561); complement 3 glomerulopathy (0.546)
- **Europe PMC papers**: 7226
- **Why important**: CFB is directly represented in (GO:BP complement activation, alternative pathway; q_global = 0.0388), has a strong STRING relationship with C3, and occupies many hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_08796.1) and (hu.MAP huMAP3_09832.1) through (hu.MAP huMAP3_07701.1). It is liver-enriched, secreted to blood, and its annotated function directly describes formation of the alternative-pathway C3 convertase. Its disease associations include factor B anomaly, atypical hemolytic-uremic syndrome, complement-related immunodeficiency, and paroxysmal nocturnal hemoglobinuria.
- **Conclusion**: Established evidence: CFB provides the clearest mechanistic bridge from the co-abundance pattern to alternative-pathway complement biology. Hypothesis: coordinated C3 and CFB abundance could alter alternative-pathway potential in these tissues or their surrounding fluids, but functional complement activity was not measured.

#### ITIH4

- **Related proteins** (co-abundance neighbors): C3 (0.89), PPCS (0.87), LRG1 (0.85), CFB (0.85), C9 (0.84), APOD (0.83); STRING partners: C3 (0.745)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08796.1, huMAP3_09832.1, huMAP3_09434.1
- **Function (MyGene.info)**: inter-alpha-trypsin inhibitor heavy chain 4. The protein encoded by this gene is secreted into the blood, where it is cleaved by plasma kallikrein into two smaller forms. Expression of this gene has been detected only in liver, and it seems to be upregulated during surgical trauma. This gene is part of a cluster of similar genes on chromosome 3. Two transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.466); coronary artery disorder (0.417); type 2 diabetes mellitus (0.397); osteoarthritis (0.387); diabetes mellitus (0.363)
- **Europe PMC papers**: 1710
- **Why important**: ITIH4 has the greatest weighted network strength and the broadest local connectivity, linking complement genes and several secreted proteins. It appears repeatedly in hu.MAP complexes (hu.MAP huMAP3_09531.1) through (hu.MAP huMAP3_10678.1), (hu.MAP huMAP3_08796.1), (hu.MAP huMAP3_09832.1), and (hu.MAP huMAP3_09434.1), is liver-enriched and secreted to blood, and is annotated for acute-phase response, hyaluronan metabolism, and cytokine response. Its disease associations include skeletal abnormalities, coronary artery disorder, type two diabetes mellitus, and osteoarthritis.
- **Conclusion**: Established evidence: ITIH4 is a high-position extracellular acute-phase component that may explain why the complement core is embedded in a broader secreted inflammatory network. Hypothesis: ITIH4 could link hepatic acute-phase secretion to extracellular matrix or cytokine-related processes in the cervix, but the supplied evidence does not demonstrate such a causal bridge.

#### C9

- **Related proteins** (co-abundance neighbors): ITIH4 (0.84), APOD (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C9. This gene encodes the final component of the complement system. It participates in the formation of the Membrane Attack Complex (MAC). The MAC assembles on bacterial membranes to form a pore, permitting disruption of bacterial membrane organization. Mutations in this gene cause component C9 deficiency. [provided by RefSeq, Feb 2009].
- **Diseases (Open Targets)**: immunodeficiency due to a late component of complement deficiency (0.747); age-related macular degeneration (0.584); complement component 9 deficiency (0.548); macular degeneration (0.541); complement deficiency (0.463)
- **Europe PMC papers**: 28081
- **Why important**: C9 is one of the genes supporting (GO:BP complement activation, alternative pathway; q_global = 0.0388) and is annotated as the terminal complement component participating in membrane attack complex formation. It connects to ITIH4 and APOD in the module, is liver-enriched, and is secreted to blood. It has substantial literature support and disease associations involving C9 deficiency, complement deficiency, immunodeficiency, and age-related macular degeneration.
- **Conclusion**: Established evidence: C9 gives the module a plausible downstream complement-effector dimension beyond initiation and amplification. Hypothesis: its co-abundance with C3 and CFB may reflect coordinated production of complement effector capacity, although co-abundance does not show that membrane attack complexes are assembled.

#### A2M

- **Related proteins** (co-abundance neighbors): CES2 (0.80); STRING partners: CFB (0.726), CP (0.889)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_09531.1, huMAP3_10101.1, huMAP3_15040.1, huMAP3_10678.1, huMAP3_08395.1, huMAP3_09273.1, huMAP3_07265.1, huMAP3_07701.1
- **Function (MyGene.info)**: alpha-2-macroglobulin. The protein encoded by this gene is a protease inhibitor and cytokine transporter. It uses a bait-and-trap mechanism to inhibit a broad spectrum of proteases, including trypsin, thrombin and collagenase. It can also inhibit inflammatory cytokines, and it thus disrupts inflammatory cascades. Mutations in this gene are a cause of alpha-2-macroglobulin deficiency. This gene is implicated in Alzheimer…
- **Diseases (Open Targets)**: myopia (0.206); refractive error (0.151); primary angle-closure glaucoma (0.148); Abnormality of refraction (0.144); Aganglionic megacolon (0.118)
- **Europe PMC papers**: 5133
- **Why important**: A2M links the module's metabolic branch to its plasma-protein core through CES2 and connects in STRING to CFB and CP. It is secreted to blood, is enhanced in hepatocytes among the listed cell types, and is annotated as a broad protease inhibitor and cytokine transporter with a role in negative regulation of complement activation. It has substantial literature support and disease relevance including A2M deficiency and Alzheimer's disease.
- **Conclusion**: Established evidence: A2M is a plausible extracellular counter-regulatory component that can contextualize complement-associated co-abundance rather than simply indicating complement activation. Hypothesis: A2M may buffer proteolytic or inflammatory consequences of the C3 and CFB-centered program, but the module does not establish the direction of that regulation.

## Module 4

**Tissue pair**: cervix_uterine and liver  
**Genes (43)**: ABCF1, APOA2, ATP1A1, DAZAP1, DDX46, DYNC1H1, ECHDC1, TUFM, EIF3C, EZR, GARS1, GMPS, HSPH1, HSP90AA1, IMPDH2, IPO4, PKM, LRBA, MAN2A1, NAA25, OLA1, ALDH18A1, PRKDC, GART, PAICS, UPF1, SCFD1, SUCLA2, AARS1, EPRS1, IARS1, KARS1, LARS1, RARS1, SARS1, YARS1, CCT5, CCT3, CCT7, CCT8, TXNRD1, SNRNP200, XRCC6

### Function

The strongest interpretation is a broadly expressed intracellular biosynthetic and proteostasis module. Globally corrected GO and KEGG evidence supports ATP and nucleotide binding (12 globally significant GO/KEGG terms, q_global 1.4e-10–3.63e-06; see the table), ATP-dependent activity (GO:MF ATP hydrolysis activity; q_global = 0.000183) (GO:MF ATP-dependent activity; q_global = 0.00111), protein translation and protein biosynthesis (GO:BP translation; q_global = 0.00089) (GO:BP protein biosynthetic process; q_global = 0.00089), aminoacyl-tRNA ligase activity and tRNA aminoacylation (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000394)–(4 globally significant GO/KEGG terms, q_global 0.000394–0.0334; see the table), RNA binding and nucleic-acid-related catalysis (5 globally significant GO/KEGG terms, q_global 0.00081–0.0438; see the table), and ATP-dependent protein folding by the chaperonin-containing T-complex (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00394) (GO:CC chaperonin-containing T-complex; q_global = 0.00658) (GO:MF protein folding chaperone; q_global = 0.0107). A purine and nucleotide-supply component is also supported by GART, GMPS, IMPDH2, PAICS and related genes in the globally corrected nucleotide-binding and nucleobase-metabolism terms (GO:MF ATP binding; q_global = 1.4e-10)–(4 globally significant GO/KEGG terms, q_global 3.63e-06–0.0384; see the table). DNA repair and telomere-related annotations are present, particularly for PRKDC, XRCC6, UPF1, HSP90AA1 and the CCT subunits (GO:BP telomere maintenance; q_global = 0.000253) (GO:BP telomere organization; q_global = 0.000405)–(GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.000486) (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.00191)–(GO:BP regulation of telomere maintenance; q_global = 0.00214) (GO:BP RNA-templated DNA biosynthetic process; q_global = 0.0109)–(GO:BP positive regulation of telomere maintenance; q_global = 0.0202), but these annotations should be interpreted as a secondary functional axis rather than evidence that the whole module is a dedicated telomere module. Overall, the module appears to capture coordinated abundance of core translation, RNA processing, nucleotide metabolism, chaperoning, and genome-maintenance machinery in both tissues.

**Cell composition.** This is not predominantly a plasma or secreted-protein module and it is not blood-cell enriched. HPA reports low immune-cell specificity for almost all genes, with no enriched blood-cell pattern, while only a small minority are secreted. Most genes have low tissue specificity, and protein detection is widespread in cervix_uterine and liver. The composition therefore resembles broadly expressed housekeeping machinery rather than a tissue-restricted program. There are tissue-enhanced examples, including APOA2 in liver and hepatocytes, but APOA2 is an outlying secreted liver-associated component rather than a defining feature of the module. Cell-type-enhanced annotations, including germ-cell, epithelial, muscle, neural and other cell types, are heterogeneous and do not support a single shared cell population. The shared signal could consequently reflect conserved cellular activity, sample composition, or a mixture of both; it should not be interpreted as evidence for a common blood contaminant.

**GO/KEGG enrichment**: 70 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ATP binding | 1.4e-10 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, UPF1, XRCC6, YARS1 |
| GO:MF adenyl ribonucleotide binding | 1.65e-10 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, UPF1, XRCC6, YARS1 |
| GO:MF purine ribonucleoside triphosphate binding | 5.57e-09 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, TUFM, UPF1, XRCC6, YARS1 |
| GO:MF purine ribonucleotide binding | 6.25e-09 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, TUFM, UPF1, XRCC6, YARS1 |
| GO:MF adenyl nucleotide binding | 7.8e-09 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, UPF1, XRCC6, YARS1 |
| GO:MF ribonucleotide binding | 7.98e-09 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, TUFM, UPF1, XRCC6, YARS1 |
| GO:MF nucleotide binding | 3.02e-08 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, IMPDH2, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, TUFM, TXNRD1, UPF1, XRCC6, YARS1 |
| GO:MF nucleoside phosphate binding | 5.44e-08 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, IMPDH2, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, TUFM, TXNRD1, UPF1, XRCC6, YARS1 |
| GO:MF purine nucleotide binding | 1.34e-07 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, TUFM, UPF1, XRCC6, YARS1 |
| GO:MF carbohydrate derivative binding | 2.19e-07 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, TUFM, UPF1, XRCC6, YARS1 |
| GO:MF heterocyclic compound binding | 3.86e-07 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, IMPDH2, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, TUFM, TXNRD1, UPF1, XRCC6, YARS1 |
| GO:MF anion binding | 3.63e-06 | AARS1, ABCF1, ALDH18A1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, EPRS1, GARS1, GART, GMPS, HSP90AA1, HSPH1, IARS1, KARS1, LARS1, OLA1, PAICS, PKM, PRKDC, RARS1, SARS1, SNRNP200, SUCLA2, TUFM, TXNRD1, UPF1, XRCC6, YARS1 |
| GO:MF ATP hydrolysis activity | 0.000183 | ABCF1, ATP1A1, CCT3, CCT5, CCT7, CCT8, DDX46, DYNC1H1, HSP90AA1, OLA1, SNRNP200, UPF1, XRCC6 |
| GO:BP telomere maintenance | 0.000253 | CCT3, CCT5, CCT7, CCT8, HSP90AA1, PRKDC, UPF1, XRCC6 |
| GO:MF aminoacyl-tRNA ligase activity | 0.000394 | AARS1, EPRS1, GARS1, IARS1, KARS1, LARS1, RARS1, SARS1, YARS1 |

### STRING and hu.MAP

STRING supports several coherent, already known interaction neighborhoods. The aminoacyl-tRNA synthetases form a dense, established network involving AARS1, EPRS1, GARS1, IARS1, KARS1, LARS1, RARS1, SARS1 and YARS1, with supplementary enrichment for aminoacyl-tRNA ligase activity (STRING Keyword Ligase; within-query FDR = 6.69e-05) (STRING Function aminoacyl-tRNA ligase activity; within-query FDR = 8.29e-05). The CCT subunits form a highly connected chaperonin group, with links among CCT3, CCT5, CCT7 and CCT8 and additional links to HSP90AA1 (8 supplementary STRING terms; within-query FDR 4.42e-12–3.27e-08). Purine-biosynthesis proteins such as GART, GMPS, IMPDH2 and PAICS are also linked, as are the DNA-repair proteins PRKDC and XRCC6. STRING enrichment is supplementary here and its FDR is not global module significance; the primary enrichment conclusions come from the globally significant GO/KEGG terms. hu.MAP independently identifies multisynthetase complexes containing EPRS1, IARS1, RARS1, KARS1 and LARS1 (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1), multiple CCT-containing complexes containing CCT3, CCT5, CCT7 and CCT8 (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), and additional metabolic or protein-associated complexes (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_13695.1)–(hu.MAP huMAP3_10115.1). These convergent observations show that substantial portions of the module recapitulate known molecular machinery. They do not establish that every co-abundance edge is a direct physical interaction or that the entire module is one biochemical complex.

**STRING interactions (score >= 0.7)**: 73 of 903 gene pairs: AARS1–EPRS1 (0.976); AARS1–GARS1 (0.983); AARS1–IARS1 (0.98); AARS1–KARS1 (0.992); AARS1–LARS1 (0.968); AARS1–RARS1 (0.85); AARS1–SARS1 (0.881); AARS1–YARS1 (0.996); ALDH18A1–EPRS1 (0.723); ALDH18A1–GMPS (0.909); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT3–HSP90AA1 (0.767); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT5–HSP90AA1 (0.868); CCT7–CCT8 (0.999); CCT7–EIF3C (0.728); CCT7–HSP90AA1 (0.849); CCT7–IMPDH2 (0.758); CCT8–HSP90AA1 (0.823); DDX46–SNRNP200 (0.874); DYNC1H1–HSP90AA1 (0.909); EIF3C–EPRS1 (0.755); EPRS1–GARS1 (0.973); EPRS1–GART (0.752); EPRS1–GMPS (0.912); EPRS1–HSP90AA1 (0.701); EPRS1–IARS1 (0.999); EPRS1–KARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–RARS1 (0.999); EPRS1–SARS1 (0.86); EPRS1–YARS1 (0.999); EZR–HSP90AA1 (0.954); GARS1–IARS1 (0.97); GARS1–KARS1 (0.915); GARS1–LARS1 (0.895); GARS1–RARS1 (0.892); GARS1–SARS1 (0.975); GARS1–YARS1 (0.989); GART–GMPS (0.937); GART–IMPDH2 (0.811); GART–PAICS (0.999); GMPS–IMPDH2 (0.998); GMPS–IPO4 (0.861); GMPS–KARS1 (0.835); GMPS–PAICS (0.85); GMPS–RARS1 (0.872); GMPS–TUFM (0.745); HSP90AA1–HSPH1 (0.938); HSP90AA1–PRKDC (0.733); IARS1–KARS1 (0.999); IARS1–LARS1 (0.999); IARS1–RARS1 (0.999); IARS1–SARS1 (0.908); IARS1–YARS1 (0.966); IMPDH2–PAICS (0.744); KARS1–LARS1 (0.999); KARS1–RARS1 (0.999); KARS1–SARS1 (0.882); KARS1–TUFM (0.855); KARS1–YARS1 (0.988); LARS1–RARS1 (0.999); LARS1–SARS1 (0.933); LARS1–YARS1 (0.98); OLA1–RARS1 (0.747); OLA1–YARS1 (0.824); PRKDC–XRCC6 (0.999); RARS1–SARS1 (0.933); RARS1–YARS1 (0.942); SARS1–YARS1 (0.941)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword ATP-binding (FDR = 4.42e-12, 30 genes); Function ATP binding (FDR = 3.73e-11, 30 genes); Keyword Nucleotide-binding (FDR = 2.46e-10, 31 genes); Function Purine ribonucleoside triphosphate binding (FDR = 3.42e-10, 31 genes); Function Purine ribonucleotide binding (FDR = 8.13e-10, 31 genes); Function Nucleotide binding (FDR = 1.61e-09, 33 genes); Function Small molecule binding (FDR = 9.57e-09, 34 genes); Function Anion binding (FDR = 3.27e-08, 32 genes); TISSUES Lymphoblast (FDR = 3.07e-06, 16 genes); Function Organic cyclic compound binding (FDR = 2.37e-05, 37 genes); Function Catalytic activity, acting on a nucleic acid (FDR = 4.23e-05, 13 genes); Function Heterocyclic compound binding (FDR = 6.42e-05, 36 genes); Function Catalytic activity, acting on RNA (FDR = 6.67e-05, 12 genes); Keyword Ligase (FDR = 6.69e-05, 13 genes); Function aminoacyl-tRNA ligase activity (FDR = 8.29e-05, 9 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PKM, GARS1, AARS1, GMPS, YARS1, OLA1; 6/57); huMAP3_02637.1 (EPRS1, IARS1, RARS1, KARS1, LARS1; 5/14); huMAP3_13688.1 (EPRS1, IARS1, RARS1, KARS1, LARS1; 5/14); huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_13695.1 (PKM, GMPS; 2/4); huMAP3_04783.1 (AARS1, YARS1; 2/4); huMAP3_11534.1 (GARS1, AARS1; 2/5); huMAP3_12823.1 (PKM, GMPS; 2/7); huMAP3_10281.1 (EZR, AARS1; 2/9); huMAP3_10302.1 (AARS1, YARS1; 2/9); huMAP3_10115.1 (AARS1, YARS1; 2/14); huMAP3_08980.1 (SNRNP200, DDX46; 2/97)

### Novelty

The module should not be called a newly discovered molecular complex or a wholly novel pathway. Its principal components are well-established translation, chaperonin, purine-metabolism, RNA-processing and DNA-repair systems, and many of the corresponding relationships are represented in STRING and hu.MAP. The potentially novel result is the cross-tissue co-abundance organization of these otherwise known systems in cervix_uterine and liver, especially their recurrence as one conserved module. That observation may be biologically useful, but novelty requires validation against independent tissue cohorts, cell-composition controls, perturbation data and comparison with published co-expression or proteomic modules. Lack of a STRING or hu.MAP relationship for some genes cannot by itself establish novelty, because those resources capture different evidence types and are incomplete.

**Hypothesis.** Hypothesis: this conserved module reflects a shared cellular capacity for protein production and quality control that is coupled to nucleotide supply and genome or RNA maintenance. In this model, aminoacyl-tRNA synthetases and translation factors support cytosolic protein synthesis, CCT and heat-shock chaperones fold newly produced proteins, purine enzymes supply nucleotide precursors, and RNA-processing and DNA-repair factors maintain transcript and genome integrity. The co-abundance signal may arise because metabolically active cells coordinate these processes across tissues. The telomere-related enrichment suggests a possible connection to genome maintenance, but it does not demonstrate that telomere regulation is the module’s central mechanism. A testable prediction is that experimental or physiological changes in translational demand, proteotoxic stress or nucleotide availability will shift several of these gene groups together, after controlling for cell composition.

### Important genes

#### PRKDC

- **Related proteins** (co-abundance neighbors): IPO4 (0.89), ALDH18A1 (0.88), KARS1 (0.87), IMPDH2 (0.87), MAN2A1 (0.86), GART (0.86), AARS1 (0.85), LARS1 (0.85), DDX46 (0.85), UPF1 (0.85), CCT5 (0.85), HSP90AA1 (0.83), PKM (0.82), CCT3 (0.81), EIF3C (0.80); STRING partners: HSP90AA1 (0.733), XRCC6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is among the strongest network-connected genes and bridges the module to XRCC6 and to multiple translation, nucleotide-binding and chaperone-associated genes. Its established function is the catalytic subunit of DNA-dependent protein kinase, acting with the Ku complex in DNA double-strand-break repair and recombination. It contributes to the globally corrected telomere and nucleic-acid-related annotations (7 globally significant GO/KEGG terms, q_global 0.000253–0.0438; see the table), has a known STRING relationship with XRCC6, and has extensive disease and literature support.
- **Conclusion**: Established evidence supports PRKDC as a genome-maintenance and DNA-repair anchor that is co-abundant with the module’s protein-production machinery. It is plausible, but not established, that PRKDC helps couple genome integrity to the broader conserved module.

#### EPRS1

- **Related proteins** (co-abundance neighbors): DDX46 (0.94), XRCC6 (0.85), IPO4 (0.84), CCT7 (0.83), ALDH18A1 (0.82), DAZAP1 (0.82), CCT5 (0.82); STRING partners: AARS1 (0.976), ALDH18A1 (0.723), EIF3C (0.755), GARS1 (0.973), GART (0.752), GMPS (0.912), HSP90AA1 (0.701), IARS1 (0.999), KARS1 (0.999), LARS1 (0.999), RARS1 (0.999), SARS1 (0.86), YARS1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a central member of the aminoacyl-tRNA synthetase network and participates in known hu.MAP multisynthetase complexes (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1). It is linked by STRING to many synthetases and to translation- and chaperone-associated proteins. Its established glutamyl- and prolyl-tRNA charging functions directly support the globally corrected aminoacyl-tRNA biosynthesis and translation evidence (GO:MF aminoacyl-tRNA ligase activity; q_global = 0.000394)–(5 globally significant GO/KEGG terms, q_global 0.000394–0.00247; see the table). Its network position makes it a strong representative of the module’s translational core.
- **Conclusion**: Established evidence identifies EPRS1 as a translation and tRNA-aminoacylation component that helps explain the module’s strongest functional signal. The data do not show that EPRS1 specifically drives the cross-tissue conservation.

#### CCT5

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.89), HSPH1 (0.88), AARS1 (0.87), PKM (0.87), ALDH18A1 (0.85), PRKDC (0.85), CCT7 (0.85), DDX46 (0.84), SARS1 (0.83), EPRS1 (0.82), HSP90AA1 (0.82), IPO4 (0.81), YARS1 (0.81), GART (0.81), CCT3 (0.81); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999), HSP90AA1 (0.868)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is a highly connected representative of the CCT chaperonin group and occurs with CCT3, CCT7 and CCT8 in several hu.MAP complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Its established ATP-dependent protein-folding role is supported by the globally corrected chaperone and chaperonin terms (GO:MF ATP-dependent protein folding chaperone; q_global = 0.00394) (GO:CC chaperonin-containing T-complex; q_global = 0.00658) (GO:MF protein folding chaperone; q_global = 0.0107). It also appears in the telomere and Cajal-body-related annotations (GO:BP telomere maintenance; q_global = 0.000253) (GO:BP telomere organization; q_global = 0.000405)–(GO:BP positive regulation of telomere maintenance via telomere lengthening; q_global = 0.000486) (GO:BP regulation of telomere maintenance via telomerase; q_global = 0.00191)–(GO:BP regulation of telomere maintenance; q_global = 0.00214) (GO:CC chaperonin-containing T-complex; q_global = 0.00658)–(GO:BP protein localization to nucleoplasm; q_global = 0.00658), although those annotations do not prove a direct telomere function for the whole module. Its disease associations and substantial literature make it a well-supported proteostasis anchor.
- **Conclusion**: Established evidence supports CCT5 as a chaperonin component coordinating protein folding within the module. A role in coupling proteostasis to telomere-related processes remains a hypothesis rather than a demonstrated property of this co-abundance module.

#### IMPDH2

- **Related proteins** (co-abundance neighbors): GMPS (0.90), CCT5 (0.89), GART (0.88), PRKDC (0.87), ABCF1 (0.84), KARS1 (0.82), SUCLA2 (0.81); STRING partners: CCT7 (0.758), GART (0.811), GMPS (0.998), PAICS (0.744)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inosine monophosphate dehydrogenase 2. This gene encodes the rate-limiting enzyme in the de novo guanine nucleotide biosynthesis. It is thus involved in maintaining cellular guanine deoxy- and ribonucleotide pools needed for DNA and RNA synthesis. The encoded protein catalyzes the NAD-dependent oxidation of inosine-5'-monophosphate into xanthine-5'-monophosphate, which is then converted into guanosine-5'-monophosphate. This gene is up-…
- **Diseases (Open Targets)**: acute lymphoblastic leukemia (0.529); Crohn disease (0.447); acute myeloid leukemia (0.421); lupus nephritis (0.408); myelodysplastic syndrome (0.403)
- **Europe PMC papers**: 1438
- **Why important**: IMPDH2 connects the module’s nucleotide-metabolism neighborhood with chaperone, translation and DNA-associated genes. It is the rate-limiting enzyme in de novo guanine-nucleotide biosynthesis and is linked in STRING to GMPS, GART, PAICS and CCT7. Its participation in globally corrected nucleotide-binding and nucleobase-metabolism terms (8 globally significant GO/KEGG terms, q_global 3.02e-08–0.0384; see the table) gives the module a concrete metabolic component rather than a purely generic housekeeping interpretation. It also has substantial disease and literature support.
- **Conclusion**: Established evidence supports IMPDH2 as a guanine-nucleotide supply component that may sustain RNA, DNA and protein-production demands. The hypothesis that it functionally coordinates the other module neighborhoods requires metabolic or perturbational validation.

#### DDX46

- **Related proteins** (co-abundance neighbors): EPRS1 (0.94), LARS1 (0.92), UPF1 (0.89), KARS1 (0.89), SNRNP200 (0.88), IARS1 (0.87), PRKDC (0.85), CCT5 (0.84), ABCF1 (0.84), CCT7 (0.82), ALDH18A1 (0.82); STRING partners: SNRNP200 (0.874)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_08980.1
- **Function (MyGene.info)**: DEAD-box helicase 46. This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribu…
- **Diseases (Open Targets)**: neurodegenerative disease (0.526); dengue disease (0.370); Hypercholesterolemia (0.203); lung adenocarcinoma (0.074); osteosarcoma (0.053)
- **Europe PMC papers**: 592
- **Why important**: DDX46 is a network connector between the synthetase group, UPF1 and SNRNP200, and it is represented in a hu.MAP spliceosomal complex with SNRNP200 (hu.MAP huMAP3_08980.1). Its established DEAD-box helicase role in RNA processing and spliceosome-related functions is consistent with globally corrected RNA-binding and RNA-catalytic terms (5 globally significant GO/KEGG terms, q_global 0.00081–0.0438; see the table). Its presence broadens the interpretation from translation alone to coordinated RNA maturation and surveillance.
- **Conclusion**: Established evidence supports DDX46 as an RNA-processing component linking transcript handling to the module’s translation machinery. It is not established that DDX46 creates the shared tissue module, but its position makes coordinated RNA metabolism a credible part of the module’s biology.

## Module 5

**Tissue pair**: cervix_uterine and liver  
**Genes (30)**: ACIN1, ADAM10, AP3D1, CAPRIN1, CAPZB, CFH, CLIP1, CPSF6, CTNND1, EPS15, EPS8L2, FXR1, GFPT1, GNS, HACD2, EIF4A2, EIF4G1, EIF5, MAL2, MAP2K3, NHERF1, NSFL1C, PPP4C, PYGB, SACM1L, SAE1, SEPTIN2, SNX6, SRP72, SWAP70

### Function

The module does not support a single, statistically established GO or KEGG function: no GO or KEGG term passed global correction. Its architecture instead suggests a mixed intracellular program. The most coherent themes are translation initiation and translational control, RNA handling, vesicle and endosomal trafficking, membrane and cytoskeletal organization, and cell adhesion. The strongest functional interpretation comes from the combination of the module genes, their positions in the co-abundance network, the known interaction cluster around EIF4G1, EIF4A2, EIF5, FXR1 and CAPRIN1, and the roles of SRP72, AP3D1, SACM1L, CTNND1 and GNS. These observations are compatible with coordinated regulation of protein synthesis, intracellular transport and epithelial or hepatocellular organization, but they do not establish a single pathway. The absence of globally significant GO or KEGG enrichment should be reported explicitly and does not invalidate the module.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module. CFH is the clearest secreted-to-blood component, while GNS is annotated as intracellular and membrane associated; the remainder are mainly intracellular, membrane, cytoskeletal or nuclear proteins. HPA indicates broadly distributed expression for most genes, with many showing low tissue specificity. The module is therefore not strongly blood-cell dominated, although several genes have immune-cell-enhanced or monocyte-associated patterns, including CTNND1, SWAP70, GNS and MAP2K3. HPA also shows a recurring esophageal epithelial signal and more limited signals in skeletal muscle, bone marrow and liver. The shared cervix and liver module may consequently reflect a broadly expressed cellular program, with contributions from epithelial, hepatocellular and occasional immune or stromal cell composition, rather than a specialized secreted blood signature. Protein detection in both tissues for many genes supports biological presence, but the lack of detection for selected genes means that tissue-level protein evidence is incomplete.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a focused, already known interaction neighborhood rather than a densely interconnected module. The most coherent known relationships connect EIF4G1 with EIF4A2 and EIF5, and also link EIF4G1 and EIF4A2 to FXR1; CAPRIN1 has known relationships with FXR1 and EIF4G1, while CAPZB and EPS8L2 form another supported pair. These interactions support a translation and RNA-regulatory substructure, but STRING provides no functional enrichment for the module as a whole. hu.MAP independently places EIF4G1 and EIF4A2 together in each of the reported complexes (hu.MAP huMAP3_00975.1), (hu.MAP huMAP3_06085.1), (hu.MAP huMAP3_09957.1), (hu.MAP huMAP3_13175.1) and (hu.MAP huMAP3_11246.1). In every case, they are only a subset of a larger complex, so the evidence supports a real translation-initiation-related core but not membership of the entire co-abundance module in one physical complex. Most module genes lack reported STRING partners or hu.MAP complexes in the supplied evidence. Thus, the network combines a known translation-initiation core with less directly connected trafficking, adhesion, cytoskeletal, metabolic and complement-related genes.

**STRING interactions (score >= 0.7)**: 8 of 435 gene pairs: CAPRIN1–EIF4G1 (0.758); CAPRIN1–FXR1 (0.891); CAPZB–EPS8L2 (0.759); EIF4A2–EIF4G1 (0.999); EIF4A2–EIF5 (0.988); EIF4A2–FXR1 (0.745); EIF4G1–EIF5 (0.99); EIF4G1–FXR1 (0.83)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00975.1 (EIF4G1, EIF4A2; 2/3); huMAP3_06085.1 (EIF4G1, EIF4A2; 2/5); huMAP3_09957.1 (EIF4G1, EIF4A2; 2/9); huMAP3_13175.1 (EIF4G1, EIF4A2; 2/20); huMAP3_11246.1 (EIF4G1, EIF4A2; 2/24)

### Novelty

The module should not be called a wholly new molecular complex or a newly discovered pathway. Several relationships are established in STRING and the repeated EIF4G1–EIF4A2 membership in hu.MAP complexes shows that part of the signal recapitulates known biology. At the same time, the specific cross-tissue co-abundance grouping of these genes in cervix and liver is not demonstrated to be present or absent in the supplied external resources. Absence from STRING or hu.MAP would not prove novelty, and the sheet provides no matched-dataset comparison, replication analysis or literature search specifically testing this module. The defensible conclusion is that the cross-tissue co-abundance configuration may be a useful or potentially novel systems-level observation, but novelty remains unestablished and requires independent replication and comparison with published tissue co-expression studies.

**Hypothesis.** Hypothesis: the module represents a shared cellular state in which translational initiation and RNA regulation are coordinated with membrane trafficking, cytoskeletal remodeling, adhesion and stress-responsive signaling. EIF4G1, EIF4A2 and EIF5 could form a translational-control core, while SRP72, AP3D1, SACM1L, SNX6 and GNS could connect protein targeting, Golgi or endosomal traffic and lysosomal handling. CTNND1, SWAP70, CAPZB, EPS8L2, CLIP1 and SEPTIN2 could reflect coupled regulation of cell junctions, actin and microtubule organization. CFH may represent a liver-associated secreted complement component that enters the shared abundance pattern through hepatocyte or local tissue composition rather than through the intracellular core. This model predicts that the module will vary with epithelial or hepatocellular content, translational demand, intracellular trafficking and immune or stromal admixture; it is a hypothesis rather than a demonstrated causal mechanism.

### Important genes

#### EIF4G1

- **Related proteins** (co-abundance neighbors): AP3D1 (0.82); STRING partners: CAPRIN1 (0.758), EIF4A2 (0.999), EIF5 (0.99), FXR1 (0.83)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_00975.1, huMAP3_06085.1, huMAP3_09957.1, huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4 gamma 1. The protein encoded by this gene is a component of the multi-subunit protein complex EIF4F. This complex facilitates the recruitment of mRNA to the ribosome, which is a rate-limiting step during the initiation phase of protein synthesis. The recognition of the mRNA cap and the ATP-dependent unwinding of 5'-terminal secondary structure is catalyzed by factors in this complex. The subunit encoded by…
- **Diseases (Open Targets)**: late-onset Parkinson disease (0.601); neurodegenerative disease (0.501); dengue disease (0.372); preeclampsia (0.252); young-onset Parkinson disease (0.232)
- **Europe PMC papers**: 2810
- **Why important**: EIF4G1 is part of the most coherent known interaction and complex substructure in the module. It connects to EIF4A2 and EIF5 in STRING and appears with EIF4A2 across all reported hu.MAP complexes (hu.MAP huMAP3_00975.1), (hu.MAP huMAP3_06085.1), (hu.MAP huMAP3_09957.1), (hu.MAP huMAP3_13175.1) and (hu.MAP huMAP3_11246.1). Its established function as a scaffold for cap-dependent translation makes it a strong anchor for interpreting the module as involving translational control. It is broadly detected in both tissues and has extensive literature and disease annotation.
- **Conclusion**: Established evidence supports EIF4G1 as a translation-initiation scaffold and as the central component of the module's known protein-interaction core. It is plausible, but not proven, that its co-abundance links the module to tissue-wide translational demand.

#### EIF4A2

- **Related proteins** (co-abundance neighbors): MAL2 (0.82); STRING partners: EIF4G1 (0.999), EIF5 (0.988), FXR1 (0.745)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_00975.1, huMAP3_06085.1, huMAP3_09957.1, huMAP3_13175.1, huMAP3_11246.1
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4A2. Enables ATP hydrolysis activity. Involved in negative regulation of RNA-directed 5'-3' RNA polymerase activity. Located in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and speech delay, with or without seizures (0.744); neurodevelopmental disorder (0.565); hereditary disease (0.448); dengue disease (0.370); complex neurodevelopmental disorder (0.370)
- **Europe PMC papers**: 2227
- **Why important**: EIF4A2 is the clearest partner of EIF4G1 in the supplied network resources. It has very strong STRING relationships with EIF4G1 and EIF5 and is present with EIF4G1 in every reported hu.MAP complex (hu.MAP huMAP3_00975.1), (hu.MAP huMAP3_06085.1), (hu.MAP huMAP3_09957.1), (hu.MAP huMAP3_13175.1) and (hu.MAP huMAP3_11246.1). Its annotated role in cytoplasmic translational initiation gives direct biological meaning to the module's translation-related substructure. Its broad tissue detection and substantial literature make it a robust interpretive marker rather than an isolated low-confidence gene.
- **Conclusion**: Established evidence supports EIF4A2 as part of a known translation-initiation machinery core. The hypothesis that its abundance coordinates translation with the trafficking and epithelial features of the module requires experimental or independent co-expression validation.

#### CTNND1

- **Related proteins** (co-abundance neighbors): SRP72 (0.88), AP3D1 (0.85), ACIN1 (0.82), MAL2 (0.81), GNS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin delta 1. This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the…
- **Diseases (Open Targets)**: blepharocheilodontic syndrome (0.724); listeriosis (0.526); cleft lip (0.510); hereditary disease (0.415); exudative vitreoretinopathy (0.376)
- **Europe PMC papers**: 3021
- **Why important**: CTNND1 is among the more connected genes in the module and links to SRP72, AP3D1, ACIN1, MAL2 and GNS. Its established functions in cadherin-mediated cell adhesion, cell migration and signal transduction provide a plausible bridge between intracellular machinery and tissue architecture. HPA places it at the plasma membrane and shows enhanced patterns in several epithelial or specialized cell types, as well as group enrichment in monocyte populations. It also has a large literature base and disease associations involving developmental and adhesion phenotypes.
- **Conclusion**: Established evidence supports CTNND1 as an adhesion and signaling component that could explain why the module is shared across structurally distinct tissues. It remains a hypothesis that CTNND1 is the main biological bridge between the translation-related core and tissue or cell-composition effects.

#### CFH

- **Related proteins** (co-abundance neighbors): MAP2K3 (0.85); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement factor H. This gene is a member of the Regulator of Complement Activation (RCA) gene cluster and encodes a protein with twenty short consensus repeat (SCR) domains. This protein is secreted into the bloodstream and has an essential role in the regulation of complement activation, restricting this innate defense mechanism to microbial infections. Mutations in this gene have been associated with hemolytic-ure…
- **Diseases (Open Targets)**: complement factor H deficiency (0.769); age-related macular degeneration (0.750); atypical hemolytic-uremic syndrome (0.729); age related macular degeneration 4 (0.711); Doyne honeycomb retinal dystrophy (0.688)
- **Europe PMC papers**: 9287
- **Why important**: CFH is a biologically distinctive member of the module because it is liver tissue enriched, secreted to blood and associated with regulation of the alternative complement pathway. It has a direct module connection to MAP2K3 and an extensive disease literature involving complement-related and retinal or renal disorders. Although its network position is peripheral, its tissue specificity and secreted biology make it important for interpreting the shared liver and cervix signal and for testing whether sample composition contributes to the module.
- **Conclusion**: Established evidence supports CFH as a liver-associated extracellular complement regulator rather than as a member of the intracellular translation machinery. Its presence may indicate hepatocyte contribution or inflammatory context, but the supplied data do not establish that CFH mechanistically drives the rest of the module.

#### GNS

- **Related proteins** (co-abundance neighbors): CAPZB (0.86), EPS8L2 (0.83), CTNND1 (0.81), NSFL1C (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glucosamine (N-acetyl)-6-sulfatase. The product of this gene is a lysosomal enzyme found in all cells. It is involved in the catabolism of heparin, heparan sulphate, and keratan sulphate. Deficiency of this enzyme results in the accumulation of undegraded substrate and the lysosomal storage disorder mucopolysaccharidosis type IIID (Sanfilippo D syndrome). Mucopolysaccharidosis type IIID is the least common of the four subtypes of Sa…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 3D (0.811); mucopolysaccharidosis type 3 (0.610); mucopolysaccharidosis (0.372); ventricular fibrillation (0.233); preeclampsia (0.223)
- **Europe PMC papers**: 3078
- **Why important**: GNS has a relatively connected position linking CTNND1, CAPZB, EPS8L2 and NSFL1C. Its established lysosomal role in glycosaminoglycan degradation adds a degradative and vesicular dimension to the module. HPA shows expression in Kupffer cells, monocytes and neutrophils, including immune-cell enhancement for non-classical monocytes, while protein is detected in both tissues. Its strong disease association with mucopolysaccharidosis provides a well-defined functional and clinical context.
- **Conclusion**: Established evidence supports GNS as a lysosomal catabolic enzyme and a possible indicator of endolysosomal or immune-cell-related biology. It is plausible that GNS connects tissue-cell composition with intracellular trafficking in the module, but that connection is not demonstrated causally.

## Module 6

**Tissue pair**: cervix_uterine and liver  
**Genes (22)**: ADPRS, FDXR, ANXA6, C1QC, CYBA, DLG1, GCA, HEXA, LGALS3BP, MYO1C, NCKAP1, NIBAN2, NSF, PDIA4, RNASET2, USP5, UNC45A, UTRN, ATP6V1H, VCL, WDR1, TJP2

### Function

The strongest functional interpretation is an epithelial or endothelial junction and cortical-cytoskeleton module, with an immune and vesicle-handling context. The primary enrichment evidence is (GO:BP apical junction assembly; q_global = 0.0447), apical junction assembly, supported by DLG1, MYO1C, VCL, and WDR1. This is biologically coherent with TJP2, a tight-junction scaffold; DLG1, a polarity and junction-associated scaffold; VCL, an actin-to-membrane adhesion protein; MYO1C, an actin-based motor involved in membrane targeting and endocytosis; and WDR1, an actin-filament remodeling factor. Additional module members support complementary processes rather than a single complete pathway: ATP6V1H supports acidic vesicle and lysosomal function, NSF supports vesicle trafficking, PDIA4 supports endoplasmic-reticulum folding and secretion, and CYBA supports phagocyte oxidase and superoxide biology. No other GO or KEGG term passed global correction. The absence of additional globally significant terms does not invalidate the module; it indicates that the most defensible functional claim is centered on junctional organization and actin remodeling, with immune, vesicular, and secretory features treated as supporting interpretation.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only a minority of its members are annotated as secreted, while most are intracellular, membrane-associated, junctional, cytoskeletal, or broadly expressed. The HPA data nevertheless suggest substantial cellular-composition influence. Most genes have low tissue specificity but many show cell-type-enhanced patterns, including Hofbauer cells, Kupffer cells, macrophages, neutrophils, and other immune-associated populations. CYBA, GCA, and C1QC provide particularly clear phagocyte or myeloid signals, while LGALS3BP and RNASET2 are secreted to blood. Thus, the shared cervix and liver signal may combine a conserved epithelial or tissue-barrier program with infiltrating or resident myeloid-cell abundance. The matching protein detection in both tissues supports detectability, but the lack of immunohistochemical detection for several immune-associated genes cautions against treating the module as a uniformly expressed tissue-cell program.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP apical junction assembly | 0.0447 | DLG1, MYO1C, VCL, WDR1 |

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no STRING functional-enrichment result. Consequently, STRING does not independently establish a known physical interaction network for this module, and the co-abundance edges should not be interpreted as experimentally demonstrated protein binding. hu.MAP provides one limited complex-level connection, (hu.MAP huMAP3_08115.1), containing C1QC and NIBAN2 among the module genes. This is evidence that a small part of the module may overlap a catalogued complex, but it does not explain the whole subgraph. The combination of a coherent co-abundance pattern, a globally supported junction term (GO:BP apical junction assembly; q_global = 0.0447), and sparse external physical-complex support suggests coordinated expression across related cell or tissue states rather than a single established multiprotein complex.

**STRING interactions (score >= 0.7)**: 0 of 231 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08115.1 (C1QC, NIBAN2; 2/15)

### Novelty

The module can reasonably be considered a potentially new co-abundance association, but not a proven novel molecular complex or pathway. Its novelty is supported by the absence of high-confidence STRING pairings, the lack of a broad hu.MAP representation, and the unusual combination of junctional and actin genes with myeloid, lysosomal, secretory, and redox-associated genes across cervix and liver. However, absence from STRING or hu.MAP alone cannot establish novelty: those resources favor previously studied physical interactions and curated complexes, whereas co-abundance can reflect shared cell composition, coordinated regulation, tissue injury, or parallel functions. The most cautious conclusion is that the cross-tissue co-abundance signature is under-characterized and hypothesis-generating, with (GO:BP apical junction assembly; q_global = 0.0447) providing a biologically interpretable anchor.

**Hypothesis.** Hypothesis: the module reflects a conserved tissue-interface state in which epithelial or endothelial junction remodeling and actin organization are coordinated with vesicle trafficking, lysosomal processing, redox activity, and myeloid-cell functions. In this model, TJP2, DLG1, VCL, MYO1C, and WDR1 represent the structural junction and cortical-cytoskeleton axis; CYBA, C1QC, and GCA reflect resident or recruited phagocyte activity; ATP6V1H, HEXA, and NSF reflect endolysosomal and vesicle biology; and LGALS3BP, RNASET2, and PDIA4 represent extracellular or secretory handling. The shared signal could therefore arise from a common barrier-remodeling or inflammatory microenvironment in both tissues, potentially amplified by similar resident macrophage or other immune-cell proportions. This is a hypothesis rather than a demonstrated mechanism and requires cell-resolved expression, spatial localization, and perturbation or longitudinal validation.

### Important genes

#### TJP2

- **Related proteins** (co-abundance neighbors): RNASET2 (0.90), UTRN (0.85), GCA (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 is a direct structural anchor for the module interpretation. It has a network connection to RNASET2, UTRN, and GCA, is localized to the plasma membrane and cell junctions, and its established function includes tight-junction barrier assembly and cell-cell junction organization. Its liver disease associations are also consistent with the relevance of epithelial barrier integrity in liver tissue. Although it is not itself listed in (GO:BP apical junction assembly; q_global = 0.0447), it provides strong biological support for extending the enriched apical-junction signal beyond the four genes in that term.
- **Conclusion**: Established evidence supports TJP2 as a junction and barrier organizer that is relevant to the module's structural interpretation. Its co-abundance with immune-associated and secreted genes may indicate barrier remodeling near inflammatory cells, but that tissue-level mechanism remains a hypothesis.

#### DLG1

- **Related proteins** (co-abundance neighbors): ATP6V1H (0.93), UTRN (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: discs large MAGUK scaffold protein 1. This gene encodes a multi-domain scaffolding protein that is required for normal development. This protein may have a role in septate junction formation, signal transduction, cell proliferation, synaptogenesis and lymphocyte activation. A multitude of transcript variants deriving from alternative splicing and the use of multiple alternate promoter have been observed, including some splice variants…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.375); ovarian neoplasm (0.310); multinodular goiter (0.255); diabetes mellitus (0.254); Peyronie disease (0.252)
- **Europe PMC papers**: 4288
- **Why important**: DLG1 is a junction-associated scaffold and one of the genes in the globally corrected apical-junction term (GO:BP apical junction assembly; q_global = 0.0447). It connects the module to ATP6V1H and UTRN and has functions involving cell polarity, actin organization, signal transduction, and lymphocyte activation. Its substantial literature base and broad developmental and disease relevance make it a well-supported architectural marker rather than an obscure association.
- **Conclusion**: Established evidence supports DLG1 as a core polarity and junction scaffold contributing directly to the module function. Its connection to vesicle acidification through ATP6V1H is compatible with coordinated membrane trafficking, but the specific direction of regulation in this module is unknown.

#### CYBA

- **Related proteins** (co-abundance neighbors): HEXA (0.91), NSF (0.88), ANXA6 (0.86), VCL (0.84), WDR1 (0.83), PDIA4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome b-245 alpha chain. Cytochrome b is comprised of a light chain (alpha) and a heavy chain (beta). This gene encodes the light, alpha subunit which has been proposed as a primary component of the microbicidal oxidase system of phagocytes. Mutations in this gene are associated with autosomal recessive chronic granulomatous disease (CGD), that is characterized by the failure of activated phagocytes to generate superoxide…
- **Diseases (Open Targets)**: chronic granulomatous disease (0.735); autoimmune polyendocrine syndrome type 1 (0.340); nerve plexus disorder (0.239); hereditary disease (0.191); oral cavity squamous cell carcinoma (0.095)
- **Europe PMC papers**: 5638
- **Why important**: CYBA is the most connected node in the supplied module network and links several otherwise distinct branches, including HEXA, NSF, ANXA6, VCL, WDR1, and PDIA4. It encodes the alpha component of the phagocyte microbicidal oxidase and is associated with superoxide metabolism, inflammatory response, and chronic granulomatous disease. HPA places it in bone-marrow and lymphoid contexts and enhances it in several immune-related cell types, including Kupffer cells and Hofbauer cells. Its extensive literature and strong disease connection make it an important bridge between the structural module and an immune or redox interpretation.
- **Conclusion**: Established evidence supports CYBA as a phagocyte-associated redox gene and a topological bridge in this module. Its presence may reflect myeloid-cell contribution or inflammatory tissue state; it does not by itself prove that epithelial cells express a functional oxidase program.

#### WDR1

- **Related proteins** (co-abundance neighbors): USP5 (0.84), CYBA (0.83), NCKAP1 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 1. This gene encodes a protein containing 9 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, mostly including a trp-asp at the C-terminal end. WD domains are involved in protein-protein interactions. The encoded protein may help induce the disassembly of actin filaments. Two transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: periodic fever, immunodeficiency, and thrombocytopenia syndrome (0.705); gout (0.528); neurodegenerative disease (0.526); atrial fibrillation (0.519); intellectual developmental disorder 61 (0.416)
- **Europe PMC papers**: 1861
- **Why important**: WDR1 is included in (GO:BP apical junction assembly; q_global = 0.0447) and is functionally linked to actin-filament disassembly, cortical-cytoskeleton organization, neutrophil-mediated immunity, and platelet formation. It connects CYBA with USP5 and NCKAP1, placing actin remodeling between redox-associated and lamellipodium or Rac-associated biology. HPA also highlights platelet and megakaryocyte-related cell types, which broadens the possible cellular-composition contribution.
- **Conclusion**: Established evidence supports WDR1 as an actin-remodeling component that reinforces the apical-junction interpretation and may also capture immune-cell state. Whether it participates in the same cells as CYBA and the junction genes, rather than marking mixed cell populations, remains unresolved.

#### C1QC

- **Related proteins** (co-abundance neighbors): LGALS3BP (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08115.1
- **Function (MyGene.info)**: complement C1q C chain. This gene encodes the C-chain polypeptide of serum complement subcomponent C1q, which associates with C1r and C1s to yield the first component of the serum complement system. C1q is composed of 18 polypeptide chains which include 6 A-chains, 6 B-chains, and 6 C-chains. Each chain contains an N-terminal collagen-like region and a C-terminal C1q globular domain. C1q deficiency is associated with lup…
- **Diseases (Open Targets)**: immunodeficiency due to a classical component pathway complement deficiency (0.619); C1Q deficiency (0.597); neurodegenerative disease (0.540); complement deficiency (0.462); C1Q deficiency 1 (0.462)
- **Europe PMC papers**: 4647
- **Why important**: C1QC is a secreted complement component with strong HPA association to lymphoid tissue and macrophage-lineage populations, including Kupffer cells and Hofbauer cells. It connects to LGALS3BP and is one of the two module members represented in hu.MAP complex (hu.MAP huMAP3_08115.1). Its established roles in classical complement, immune signaling, and macrophage biology provide a clear explanation for the myeloid component of the module and for the possibility that tissue-cell composition contributes to the cross-tissue pattern.
- **Conclusion**: Established evidence supports C1QC as a resident or recruited macrophage-associated complement signal and as limited complex-level support through (hu.MAP huMAP3_08115.1). Its co-abundance with junction genes is most plausibly interpreted as coordinated tissue state or cellular composition unless cell-resolved data demonstrate expression in the same cells.

## Module 7

**Tissue pair**: cervix_uterine and liver  
**Genes (19)**: AFDN, AMPD2, AP3B1, BLMH, DNAJB1, ERO1A, GYG1, GNL1, LTA4H, NDUFS1, DDOST, PDLIM2, ATIC, QNG1, IARS2, WARS1, TIMM44, TXLNA, UCHL5

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway annotation. Its network instead suggests a heterogeneous cellular-maintenance program linking protein folding and endoplasmic-reticulum quality control through DNAJB1, ERO1A and DDOST; vesicle, junction and intracellular transport through AP3B1, TXLNA and AFDN; mitochondrial function through NDUFS1, TIMM44 and IARS2; purine metabolism through ATIC and AMPD2; translation through IARS2 and WARS1; and inflammatory lipid metabolism through LTA4H. Because these functions are distributed across weakly connected branches rather than concentrated in a coherent enriched pathway, the safest interpretation is a shared co-abundance state involving general proteostasis, metabolism, organelle maintenance and cell-structural functions, not a single demonstrated biological pathway. The lack of globally significant enrichment does not invalidate the module.

**Cell composition.** The module is predominantly composed of broadly expressed or low-tissue-specificity proteins rather than plasma or secreted proteins. HPA reports low immune-cell specificity for most genes, and only a limited subset shows monocyte or neutrophil enrichment; therefore the module is not best characterized as a blood-cell module. Only ERO1A is annotated in the secretome summary, with an intracellular and membrane pattern, so the module is not predominantly secreted. Most proteins are detected in both cervix_uterine and liver, consistent with a shared cellular program, although tissue-restricted detection of some genes and cell-type-enhanced signals indicate that cellular composition could contribute. The HPA pattern is more compatible with broadly shared cellular machinery, possibly mixed with contributions from particular epithelial, stromal or immune cell populations, than with a simple plasma-protein signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides two high-confidence physical or functional relationships within the module: AMPD2 with ATIC, and IARS2 with WARS1. These support a purine-metabolism connection for AMPD2 and ATIC and a translation-related connection for the two aminoacyl-tRNA synthetases. STRING reports no functional enrichment for the module. hu.MAP identifies complex huMAP3_14442.1 (hu.MAP huMAP3_14442.1), containing LTA4H and ATIC among its module members, but most of the complex lies outside the module. Thus, the module contains a small amount of support from known molecular relationships, while most of its co-abundance edges are not represented by the supplied STRING or hu.MAP evidence. The network should therefore be treated as an expression-correlation structure rather than as a validated physical complex.

**STRING interactions (score >= 0.7)**: 2 of 171 gene pairs: AMPD2–ATIC (0.951); IARS2–WARS1 (0.846)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (LTA4H, ATIC; 2/57)

### Novelty

The conserved co-abundance pattern may be a new observation in this tissue-pair analysis, because the module combines genes from proteostasis, trafficking, mitochondrial function, translation, purine metabolism, adhesion and inflammatory lipid metabolism without a matching globally enriched GO or KEGG theme. However, the evidence is insufficient to claim a new biological mechanism. Several component functions and relationships are already established, including the AMPD2–ATIC and IARS2–WARS1 STRING relationships and the partial hu.MAP complex assignment (hu.MAP huMAP3_14442.1). The absence of broad STRING or hu.MAP coverage does not by itself establish novelty. A defensible claim is that the cross-tissue co-abundance organization is potentially novel and requires replication in independent cohorts, assessment of cell composition, and comparison with published tissue co-expression modules.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular stress and resource-allocation state shared by selected cervix_uterine and liver cell populations. In this model, proteostasis and endoplasmic-reticulum handling through DNAJB1, ERO1A and DDOST are coordinated with mitochondrial import and respiration through TIMM44 and NDUFS1, while purine supply, translation, vesicle trafficking and cell-junction organization are adjusted through ATIC, AMPD2, IARS2, WARS1, AP3B1, TXLNA and AFDN. LTA4H could connect this state to inflammatory lipid processing. This is a mechanistic hypothesis, not an established pathway assignment, because global enrichment evidence is absent and the network contains only sparse known molecular links.

### Important genes

#### GNL1

- **Related proteins** (co-abundance neighbors): ATIC (0.82), NDUFS1 (0.82), ERO1A (0.82), IARS2 (0.81), WARS1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein nucleolar 1. The GNL1 gene, identified in the human major histocompatibility complex class I region, shows a high degree of similarity with its mouse counterpart. The GNL1 gene is located less than 2 kb centromeric to HLA-E, in the same transcriptional orientation. GNL1 is telomeric to HLA-B and HLA-C. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: psoriasis (0.116); cancer (0.068); autosomal recessive osteopetrosis (0.048); Gaucher disease (0.039); acrodysostosis (0.039)
- **Europe PMC papers**: 274
- **Why important**: GNL1 has the strongest network position in the module and connects branches involving ATIC, NDUFS1, ERO1A, IARS2 and WARS1. Its annotation includes signal transduction, DNA-damage response and T-cell-mediated immunity, while its HPA profile is broadly expressed with vesicular localization. It therefore occupies a useful integrative position, although its disease and functional literature is less extensive than that of several other selected genes.
- **Conclusion**: Established evidence supports GNL1 as the principal network connector and as a broadly expressed gene with reported roles in cellular signaling and stress-related biology. It is a plausible module organizer, but a specific causal role in the shared cervix_uterine–liver state remains hypothetical.

#### DNAJB1

- **Related proteins** (co-abundance neighbors): AFDN (0.88), TXLNA (0.85), AP3B1 (0.84), UCHL5 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DnaJ heat shock protein family (Hsp40) member B1. This gene encodes a member of the DnaJ or Hsp40 (heat shock protein 40 kD) family of proteins. DNAJ family members are characterized by a highly conserved amino acid stretch called the 'J-domain' and function as one of the two major classes of molecular chaperones involved in a wide range of cellular events, such as protein folding and oligomeric protein complex assembly. The encoded protein is a …
- **Diseases (Open Targets)**: fibrolamellar hepatocellular carcinoma (0.377); hepatocellular adenoma (0.370); bile duct adenocarcinoma (0.370); hepatocellular carcinoma (0.290); hepatoblastoma (0.281)
- **Europe PMC papers**: 2924
- **Why important**: DNAJB1 is among the better-connected genes and links AFDN, TXLNA, AP3B1 and UCHL5. Its established Hsp40 chaperone function, involvement in protein folding and unfolded-protein responses, nucleoplasmic localization, disease associations with liver neoplasia, and extensive literature make it a strong candidate for the proteostasis component of the module.
- **Conclusion**: Established evidence supports DNAJB1 as a molecular chaperone involved in protein folding and stress responses. Its central network position is consistent with a proteostasis role in the module, but the data do not establish that DNAJB1 drives the cross-tissue co-abundance pattern.

#### ATIC

- **Related proteins** (co-abundance neighbors): GNL1 (0.82); STRING partners: AMPD2 (0.951)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase. This gene encodes a bifunctional protein that catalyzes the last two steps of the de novo purine biosynthetic pathway. The N-terminal domain has phosphoribosylaminoimidazolecarboxamide formyltransferase activity, and the C-terminal domain has IMP cyclohydrolase activity. A mutation in this gene results in AICA-ribosiduria. [provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: AICA-ribosiduria (0.708); cancer (0.571); Intellectual disability (0.463); lung adenocarcinoma (0.390); anaplastic large cell lymphoma (0.374)
- **Europe PMC papers**: 5200
- **Why important**: ATIC is directly connected to GNL1 and has a high-confidence STRING relationship with AMPD2. It catalyzes the final reactions of de novo purine biosynthesis, is represented in the partial hu.MAP complex (hu.MAP huMAP3_14442.1), has substantial literature, and has disease associations including AICA-ribosiduria and cancer. Its network degree is limited, but its biochemical specificity and independent interaction evidence make it an informative anchor.
- **Conclusion**: Established evidence supports ATIC as a purine-biosynthesis enzyme with a known relationship to AMPD2 and partial complex support from (hu.MAP huMAP3_14442.1). Its participation in a coordinated nucleotide-supply program within this module is plausible, whereas any broader role in tissue stress adaptation is a hypothesis.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): GNL1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 connects to GNL1 and encodes a major iron-sulfur-containing core subunit of mitochondrial respiratory complex I. It has mitochondrial localization, broad detection in both tissues, tissue enhancement in muscle-related samples, extensive literature, and strong associations with mitochondrial complex-I deficiency and neurodegenerative or metabolic disease. It provides a biologically meaningful marker for the module's energetic branch.
- **Conclusion**: Established evidence supports NDUFS1 as a core mitochondrial respiratory-chain component. Its inclusion suggests that mitochondrial energy metabolism may accompany the module, but the limited network connectivity and absence of global enrichment prevent assigning it a central causal role.

#### LTA4H

- **Related proteins** (co-abundance neighbors): IARS2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: leukotriene A4 hydrolase. The protein encoded by this gene is an enzyme that contains both hydrolase and aminopeptidase activities. The hydrolase activity is used in the final step of the biosynthesis of leukotriene B4, a proinflammatory mediator. The aminopeptidase activity has been shown to degrade proline-glycine-proline (PGP), a neutrophil chemoattractant and biomarker for chronic obstructive pulmonary disease (COPD). …
- **Diseases (Open Targets)**: hypotensive disorder (0.198); small intestine neuroendocrine neoplasm (0.150); cystic fibrosis (0.104); COVID-19 (0.096); hepatocellular carcinoma (0.086)
- **Europe PMC papers**: 1823
- **Why important**: LTA4H is connected to IARS2 and appears with ATIC in the hu.MAP complex assignment (hu.MAP huMAP3_14442.1). It has well-established leukotriene A hydrolase and aminopeptidase activities, including production of leukotriene B4 and degradation of a neutrophil chemoattractant. Its cell-type annotations include alveolar, esophageal and myeloid populations, and it has substantial literature and disease associations involving inflammatory and pulmonary conditions.
- **Conclusion**: Established evidence supports LTA4H as an inflammatory lipid-metabolism and peptide-processing enzyme. Its presence may indicate an inflammatory or myeloid-linked component, but HPA does not show that the module as a whole is blood-cell enriched; connecting LTA4H mechanistically to the full module remains hypothetical.

## Module 8

**Tissue pair**: cervix_uterine and liver  
**Genes (5)**: AIFM1, ALDH3A2, HADHB, FH, SDHA

### Function

The module is most consistent with coordinated mitochondrial energy and lipid metabolism, centered on oxidative phosphorylation, the tricarboxylic acid cycle, and long-chain fatty-acid beta-oxidation. HADHB supports mitochondrial trifunctional-protein activity and long-chain fatty-acid beta-oxidation; SDHA is a catalytic component of respiratory complex II and links succinate metabolism to electron transport; FH catalyzes a tricarboxylic-acid-cycle step; AIFM1 connects mitochondrial respiratory function with apoptotic responses; and ALDH3A2 detoxifies long-chain aldehydes generated during lipid metabolism and lipid peroxidation. The co-abundance network has a compact chain-like structure, with HADHB, SDHA, and AIFM1 occupying the more connected positions and FH and ALDH3A2 at the network periphery. No GO or KEGG term passed global correction, so these annotations support biological interpretation but do not constitute globally significant enrichment. The STRING HPO associations are supplementary and should not be interpreted as globally corrected enrichment. Overall, the evidence supports a mitochondrial metabolic and stress-response interpretation rather than a disease-specific functional annotation.

**Cell composition.** This is not a plasma-protein, secreted-protein, or blood-cell-enriched module. All genes are non-secreted, all have low immune-cell specificity, and the HPA profile shows tissue or cell-type enhancement rather than a blood signature. The profile is compatible with tissue-resident metabolic programs, particularly liver, heart muscle, skeletal muscle, hepatocytes, and selected epithelial or specialized cell types. Protein detection is broad in liver and nearly complete in cervix_uterine, although ALDH3A2 is not detected in cervix_uterine by the supplied HPA evidence. The shared module therefore is more plausibly related to conserved mitochondrial or metabolic activity in sampled tissues than to circulating proteins or an infiltrating blood-cell population. The tissue-enhanced pattern also cautions that co-abundance may reflect shared cellular composition or metabolic state rather than direct physical interaction among every member.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides two high-confidence relationships within the module: FH with SDHA and HADHB with SDHA. The FH-SDHA relationship is especially strongly supported in the supplied network, while the HADHB-SDHA relationship is also supported. These links connect the tricarboxylic acid cycle and respiratory complex II with fatty-acid oxidation, giving the network a biologically coherent mitochondrial core. AIFM1 and ALDH3A2 have no listed STRING partners within this module, so their inclusion is supported primarily by co-abundance and their individual mitochondrial, metabolic, or stress-related annotations rather than by recorded within-module STRING links. No hu.MAP complex contains multiple module members. Thus, the module is not evidence for a known multiprotein complex, and STRING associations should be regarded as functional or reported associations rather than proof that all genes form one physical assembly.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: FH–SDHA (0.999); HADHB–SDHA (0.785)
**STRING functional enrichment (supplementary, within-query FDR)**: HPO Tinnitus (FDR = 0.0122, 3 genes); HPO Abnormal fundus morphology (FDR = 0.0187, 5 genes); HPO Abnormal circulating calcium concentration (FDR = 0.0187, 3 genes); HPO Abnormal pyramidal sign (FDR = 0.0187, 4 genes); HPO Abnormal blood inorganic cation concentration (FDR = 0.0187, 3 genes); HPO Generalized muscle weakness (FDR = 0.0209, 3 genes); HPO Functional abnormality of the middle ear (FDR = 0.0472, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact conserved co-abundance module may be a potentially new observation, because the supplied resources do not identify a matching hu.MAP complex and only part of the module has known STRING relationships. However, it should not be called a newly discovered molecular pathway: the individual genes and several of their biological connections are well established, especially the mitochondrial respiratory, tricarboxylic-acid-cycle, and fatty-acid-oxidation roles. The absence of a hu.MAP complex or a STRING edge for some pairs does not establish novelty, because co-abundance can reflect shared regulation, tissue composition, metabolic demand, or incomplete database coverage. A defensible claim is therefore that the conserved tissue-pair co-abundance pattern is potentially novel, while its component biology is largely established and mechanistically plausible.

**Hypothesis.** Hypothesis: the shared module reflects coordinated mitochondrial adaptation to lipid-derived substrate use and oxidative or metabolic stress in cervix_uterine and liver. In this model, HADHB supplies long-chain fatty-acid beta-oxidation capacity, SDHA couples succinate handling to respiratory electron transfer, FH supports tricarboxylic-acid-cycle flux, ALDH3A2 limits accumulation of reactive long-chain aldehydes, and AIFM1 links mitochondrial state to cell-survival or apoptotic signaling. The observed co-abundance could therefore arise from common regulation of mitochondrial demand or from shared abundance of metabolically active cell populations, rather than from a single physical complex. This hypothesis requires validation with cell-resolved expression, protein-level co-localization, metabolic measurements, and perturbation experiments.

### Important genes

#### SDHA

- **Related proteins** (co-abundance neighbors): FH (0.85), AIFM1 (0.80); STRING partners: FH (0.999), HADHB (0.785)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: succinate dehydrogenase complex flavoprotein subunit A. This gene encodes a major catalytic subunit of succinate-ubiquinone oxidoreductase, a complex of the mitochondrial respiratory chain. The complex is composed of four nuclear-encoded subunits and is localized in the mitochondrial inner membrane. Mutations in this gene have been associated with a form of mitochondrial respiratory chain deficiency known as Leigh Syndrome. A pseudogene has been identi…
- **Diseases (Open Targets)**: mitochondrial complex II deficiency, nuclear type 1 (0.813); pheochromocytoma/paraganglioma syndrome 5 (0.790); dilated cardiomyopathy 1GG (0.768); neurodegeneration with ataxia and late-onset optic atrophy (0.761); gastrointestinal stromal tumor (0.743)
- **Europe PMC papers**: 12756
- **Why important**: SDHA is a central network connector, linked in STRING to both FH and HADHB, and is a catalytic subunit of mitochondrial respiratory complex II. Its annotations connect the module to succinate metabolism, the tricarboxylic acid cycle, and electron transport. It also has extensive literature and disease associations involving mitochondrial respiratory deficiency, cardiomyopathy, neurodegeneration, and tumor syndromes, making it the strongest integrative anchor of the module.
- **Conclusion**: Established evidence supports SDHA as the mitochondrial respiration and tricarboxylic-acid-cycle anchor. It is reasonable to hypothesize that SDHA helps organize the metabolic signal represented by the module, but the co-abundance data do not prove that SDHA directly regulates the other genes.

#### HADHB

- **Related proteins** (co-abundance neighbors): ALDH3A2 (0.84), AIFM1 (0.82); STRING partners: SDHA (0.785)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxyacyl-CoA dehydrogenase trifunctional multienzyme complex subunit beta. This gene encodes the beta subunit of the mitochondrial trifunctional protein, which catalyzes the last three steps of mitochondrial beta-oxidation of long chain fatty acids. The mitochondrial membrane-bound heterocomplex is composed of four alpha and four beta subunits, with the beta subunit catalyzing the 3-ketoacyl-CoA thiolase activity. The encoded protein can also bind RNA and decreases the s…
- **Diseases (Open Targets)**: mitochondrial trifunctional protein deficiency 2 (0.802); mitochondrial trifunctional protein deficiency (0.782); mitochondrial trifunctional protein deficiency 1 (0.700); long chain 3-hydroxyacyl-CoA dehydrogenase deficiency (0.520); hypertrophic cardiomyopathy (0.388)
- **Europe PMC papers**: 2162
- **Why important**: HADHB is one of the more connected genes in the module and is linked to SDHA in STRING while also connecting in the co-abundance graph to ALDH3A2 and AIFM1. It is the beta subunit of the mitochondrial trifunctional protein and catalyzes the thiolase step of long-chain fatty-acid beta-oxidation. Its established mitochondrial disease associations and substantial literature make it important for interpreting the module as a lipid-fueled energy program rather than a generic respiratory signature.
- **Conclusion**: Established evidence supports HADHB as the fatty-acid-oxidation component of the module. A plausible but unproven interpretation is that coordinated HADHB abundance reflects increased use or processing of long-chain fatty acids in the relevant tissue cell populations.

#### FH

- **Related proteins** (co-abundance neighbors): SDHA (0.85); STRING partners: SDHA (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fumarate hydratase. The protein encoded by this gene is an enzymatic component of the tricarboxylic acid (TCA) cycle, or Krebs cycle, and catalyzes the formation of L-malate from fumarate. It exists in both a cytosolic form and an N-terminal extended form, differing only in the translation start site used. The N-terminal extended form is targeted to the mitochondrion, where the removal of the extension generates the …
- **Diseases (Open Targets)**: hereditary leiomyomatosis and renal cell cancer (0.838); fumaric aciduria (0.820); hereditary neoplastic syndrome (0.580); Multiple cutaneous leiomyomas (0.575); neurodegenerative disease (0.482)
- **Europe PMC papers**: 42469
- **Why important**: FH is directly connected to SDHA, the strongest supplied STRING relationship, and is a mitochondrial and cytosolic fumarase involved in fumarate and malate metabolism. It provides a clear tricarboxylic-acid-cycle link and has major disease associations including hereditary leiomyomatosis and renal cell cancer and fumaric aciduria. Its very extensive literature also makes it a well-characterized metabolic marker within this otherwise small module.
- **Conclusion**: Established evidence supports FH as a core tricarboxylic-acid-cycle component and a biologically meaningful partner of SDHA. The module does not establish that FH-mediated metabolite changes cause the shared tissue co-abundance pattern, so that causal interpretation remains a hypothesis.

#### AIFM1

- **Related proteins** (co-abundance neighbors): HADHB (0.82), SDHA (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apoptosis inducing factor mitochondria associated 1. This gene encodes a flavoprotein essential for nuclear disassembly in apoptotic cells, and it is found in the mitochondrial intermembrane space in healthy cells. Induction of apoptosis results in the translocation of this protein to the nucleus where it affects chromosome condensation and fragmentation. In addition, this gene product induces mitochondria to release the apoptogenic proteins cytochr…
- **Diseases (Open Targets)**: severe X-linked mitochondrial encephalomyopathy (0.813); X-linked hereditary sensory and autonomic neuropathy with hearing loss (0.798); Charcot-Marie-Tooth disease X-linked recessive 4 (0.761); spondyloepimetaphyseal dysplasia, Bieganski type (0.747); combined oxidative phosphorylation deficiency (0.615)
- **Europe PMC papers**: 1952
- **Why important**: AIFM1 occupies a relatively connected position in the co-abundance graph through HADHB and SDHA, despite having no listed STRING partner in the module. It is a mitochondrial intermembrane-space flavoprotein involved in apoptotic nuclear changes, mitochondrial respiratory-complex assembly, and responses to ischemia or toxic stress. Its disease associations include severe mitochondrial encephalomyopathy and other X-linked mitochondrial or neurologic disorders, providing a bridge between energy metabolism and cell fate.
- **Conclusion**: Established evidence supports AIFM1 as a mitochondrial respiratory and apoptosis-related component. The hypothesis that it links metabolic stress to survival or apoptotic signaling in this shared module is biologically plausible but is not demonstrated by the co-abundance network alone.

#### ALDH3A2

- **Related proteins** (co-abundance neighbors): HADHB (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 3 family member A2. Aldehyde dehydrogenase isozymes are thought to play a major role in the detoxification of aldehydes generated by alcohol metabolism and lipid peroxidation. This gene product catalyzes the oxidation of long-chain aliphatic aldehydes to fatty acid. Mutations in the gene cause Sjogren-Larsson syndrome. Alternatively spliced transcript variants encoding different isoforms have been found for this gene…
- **Diseases (Open Targets)**: Sjogren-Larsson syndrome (0.850); hereditary disease (0.415); cerebral palsy (0.340); neurodegenerative disease (0.193); neoplasm (0.099)
- **Europe PMC papers**: 1499
- **Why important**: ALDH3A2 is a peripheral module member connected to HADHB and is tissue-enhanced in liver. It oxidizes long-chain aliphatic aldehydes produced during alcohol metabolism and lipid peroxidation, complementing the fatty-acid-oxidation role of HADHB. Its association with Sjogren-Larsson syndrome and its established aldehyde-detoxification function make it important for a potential lipid-peroxidation or membrane-stress interpretation, even though its protein is not detected in cervix_uterine in the supplied HPA summary.
- **Conclusion**: Established evidence supports ALDH3A2 as a hepatic aldehyde-detoxification and lipid-stress component. Its absence of detected protein in cervix_uterine weakens a simple shared protein-expression explanation and raises the possibility of tissue-specific regulation or cell-composition effects; this remains a hypothesis requiring validation.

## Module 9

**Tissue pair**: cervix_uterine and liver  
**Genes (5)**: AIMP1, AKR1B1, TBRG4, MAT2A, SNX2

### Function

This is a small, heterogeneous co-abundance module rather than a module with a demonstrated single pathway. TBRG4 occupies the central network position and connects AIMP1, AKR1B1, and SNX2, while AIMP1 connects to MAT2A. The gene annotations span mitochondrial biology, aminoacyl-tRNA synthetase-associated functions, cytokine and vascular signaling, aldehyde and carbohydrate reduction, endosomal transport, and S-adenosylmethionine production. Because no GO or KEGG term passed global correction, there is no globally significant pathway assignment. The most defensible interpretation is a coordinated cellular state involving protein-production or stress signaling, intracellular trafficking, redox or metabolic activity, and methyl-donor metabolism, but this composite interpretation remains inferential rather than an established pathway annotation.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: AIMP1 is the only gene annotated as secreted to blood. Most genes have low tissue specificity, although AKR1B1 is tissue enriched in adrenal gland and MAT2A is tissue enhanced in pancreas. Most genes show cell-type-enhanced expression, with recurrent HPA associations involving extravillous trophoblasts, migrating cytotrophoblasts, and Hofbauer cells. SNX2 is immune-cell enhanced and associated with memory and naive B cells, whereas the other genes generally have low immune-cell specificity. Thus, the shared cervix and liver signal could reflect a shared cellular state or shared cell composition, including trophoblast-like or other stromal or immune-related contributions, rather than a dedicated cervix-liver biochemical program. Protein detection is also tissue dependent: TBRG4 and MAT2A are detected in cervix but not liver, SNX2 is detected in liver but not cervix, and AIMP1 is detected in both.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The abundance network contains the observed co-abundance relationships, with TBRG4 linked to AIMP1, AKR1B1, and SNX2, and AIMP1 linked to MAT2A. None of the possible gene pairs has a high-confidence STRING interaction in the supplied evidence, STRING functional enrichment is absent, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance structure is not supported by previously catalogued physical interactions or a known shared complex. This does not invalidate the module: co-abundance can reflect common regulation, cell composition, compartmental state, or indirect biology rather than direct binding.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

A new biological mechanism cannot be claimed from this module alone. The pattern is potentially novel as a cross-tissue co-abundance observation because it lacks high-confidence STRING links, lacks a shared hu.MAP complex, and lacks globally significant GO or KEGG enrichment. However, absence from interaction resources does not establish novelty, and the genes themselves have established individual functions and substantial literature, especially AKR1B1 and MAT2A. The appropriate conclusion is that the cross-tissue association is a candidate observation requiring replication and experimental validation, not a demonstrated novel pathway.

**Hypothesis.** Hypothesis: a shared cellular or compositional state in cervix and liver coordinates a TBRG4-centered program that couples intracellular trafficking through SNX2 with AIMP1-associated translation, inflammatory, angiogenic, or wound-healing signaling, while AKR1B1 contributes reductive metabolic activity and MAT2A supplies methyl-donor metabolism. AIMP1 secretion could connect intracellular state to extracellular vascular or inflammatory signaling. This model predicts that the module will track specific cell populations or cellular stress states more strongly than it will represent a stable physical complex. It should be tested by cell-resolved expression, independent cohorts, protein measurements, and perturbation of the proposed bridge genes.

### Important genes

#### TBRG4

- **Related proteins** (co-abundance neighbors): AIMP1 (0.85), AKR1B1 (0.84), SNX2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: not available
- **Diseases (Open Targets)**: not available
- **Europe PMC papers**: 602
- **Why important**: TBRG4 is the central and most highly connected member of the co-abundance subgraph, linking AIMP1, AKR1B1, and SNX2. Its mitochondrial localization gives it a plausible position at the interface of cellular energy or stress state and the other module processes. HPA describes low tissue specificity, cell-type enhancement in trophoblast-related populations, and detection in cervix but not liver. Its comparatively limited literature volume makes it especially useful as a candidate driver or marker, while also making functional interpretation less certain.
- **Conclusion**: Established: TBRG4 is the network hub and is mitochondrially localized, with the stated HPA distribution. Hypothesis: TBRG4 may coordinate the otherwise diverse metabolic, trafficking, and signaling signals. The hub position alone does not demonstrate biochemical control or causality.

#### AIMP1

- **Related proteins** (co-abundance neighbors): TBRG4 (0.85), MAT2A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminoacyl tRNA synthetase complex interacting multifunctional protein 1. The protein encoded by this gene is a cytokine that is specifically induced by apoptosis, and it is involved in the control of angiogenesis, inflammation, and wound healing. The release of this cytokine renders the tumor-associated vasculature sensitive to tumor necrosis factor. The precursor protein is identical to the p43 subunit, which is associated with the multi-tRNA synthetase complex, and i…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 3 (0.790); Pelizaeus-Merzbacher-like disease (0.657); POLR-related leukodystrophy (0.657); leukodystrophy (0.372); autosomal recessive non-syndromic intellectual disability (0.371)
- **Europe PMC papers**: 663
- **Why important**: AIMP1 is the principal connector between TBRG4 and MAT2A and is also the only secreted-to-blood protein in the module. Its annotated functions include association with the multi-tRNA synthetase complex, aminoacylation-related activity, apoptosis-induced cytokine behavior, angiogenesis, inflammation, wound healing, leukocyte migration, and endothelial regulation. It is detected in both tissues and has recognized disease associations involving several leukodystrophy-related conditions.
- **Conclusion**: Established: AIMP1 has both intracellular translation-associated and extracellular cytokine-related biology and occupies a bridging network position. Hypothesis: it could provide the signaling link between a shared cellular state and vascular or inflammatory effects in the two tissues. The module does not establish that AIMP1 secretion mediates the observed co-abundance.

#### AKR1B1

- **Related proteins** (co-abundance neighbors): TBRG4 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldo-keto reductase family 1 member B. This gene encodes a member of the aldo/keto reductase superfamily, which consists of more than 40 known enzymes and proteins. This member catalyzes the reduction of a number of aldehydes, including the aldehyde form of glucose, and is thereby implicated in the development of diabetic complications by catalyzing the reduction of glucose to sorbitol. Multiple pseudogenes have been identified for thi…
- **Diseases (Open Targets)**: diabetic neuropathy (0.426); diabetes mellitus (0.406); neurodegenerative disease (0.370); diabetic cardiomyopathy (0.264); hypertensive disorder (0.179)
- **Europe PMC papers**: 2300
- **Why important**: AKR1B1 is directly connected to TBRG4 and contributes a distinct metabolic axis. It catalyzes reduction of aldehydes, including the aldehyde form of glucose, and is associated with carbohydrate, retinoid, prostaglandin, and steroid-related metabolism. HPA identifies adrenal tissue enrichment and enhancement in several trophoblast-related and Hofbauer-cell populations. Its disease associations include diabetic neuropathy, diabetes mellitus, neurodegenerative disease, and diabetic cardiomyopathy, and it has a comparatively extensive literature.
- **Conclusion**: Established: AKR1B1 is a metabolically relevant, tissue-enriched enzyme with disease links related to metabolic complications. Hypothesis: its co-abundance with TBRG4 may mark a redox or metabolic state rather than a direct interaction. The module does not show that AKR1B1 drives the cross-tissue pattern.

#### SNX2

- **Related proteins** (co-abundance neighbors): TBRG4 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endosomes; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorting nexin 2. This gene belongs to the sorting nexin family whose members contain the phosphoinositide-binding phox (PX) domain. The encoded protein is a component of the retromer complex which plays a role in protein sorting in the endocytic pathway. This protein may form oligomeric complexes with other family members. Alternate splicing results in multiple transcript variants of this gene. Pseudogenes associa…
- **Diseases (Open Targets)**: diverticular disease (0.368); anxiety (0.364); chronic obstructive pulmonary disease (0.362); malnutrition (0.315); migraine disorder (0.311)
- **Europe PMC papers**: 852
- **Why important**: SNX2 is connected to TBRG4 and represents the module's endosomal trafficking component. It is a retromer-associated sorting nexin involved in intracellular, endosomal, and retrograde endosome-to-Golgi transport. HPA places it in endosomes, identifies enhancement in B cells and trophoblast-related populations, and reports immune-cell enhancement in memory and naive B cells. Its disease associations include diverticular disease, anxiety, chronic obstructive pulmonary disease, malnutrition, and migraine disorder.
- **Conclusion**: Established: SNX2 contributes endosomal transport biology and has a cell-type pattern that could influence tissue-level co-abundance. Hypothesis: SNX2 may reflect altered receptor or cargo trafficking within the shared cellular state. There is no evidence here for a direct physical interaction between SNX2 and the other module genes.

#### MAT2A

- **Related proteins** (co-abundance neighbors): AIMP1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine adenosyltransferase 2A. The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); familial thoracic aortic aneurysm and aortic dissection (0.416); autoimmune disorder of central nervous system (0.340); prostate carcinoma (0.252); Abnormality of the cardiovascular system (0.192)
- **Europe PMC papers**: 2615
- **Why important**: MAT2A is connected to AIMP1 and supplies a chemically distinct function: production of S-adenosylmethionine, a key methyl donor. Its annotations include methionine response, protein oligomerization, and positive regulation of TORC1 signaling. HPA reports tissue enhancement in pancreas, enhancement in smooth muscle cells, and detection in cervix but not liver. It has extensive literature and disease associations spanning neurodegenerative disease, vascular disease, autoimmune disease, and prostate carcinoma.
- **Conclusion**: Established: MAT2A is a central metabolic enzyme for methyl-donor production and is the AIMP1-linked endpoint of the module. Hypothesis: its co-abundance with AIMP1 could indicate coordinated regulation of translation, growth signaling, or methylation capacity. The module does not establish altered methylation or TORC1 activity.

## Module 10

**Tissue pair**: cervix_uterine and liver  
**Genes (13)**: ALDH2, CPT2, DECR1, SORD, FAHD2A, AGL, GSTM1, GYS1, KNG1, PCK2, RIGI, TOR1AIP2, UQCRFS1

### Function

No GO or KEGG term passed global correction, so the module does not have statistically established pathway enrichment from those analyses. Its gene composition nevertheless suggests a metabolic co-abundance program centered on hepatic carbohydrate handling, glycogen turnover, mitochondrial energy metabolism, fatty-acid oxidation, redox detoxification, and related nutrient-responsive processes. GYS1 and AGL provide the clearest functional anchor because they encode glycogen synthase and glycogen debranching activities and are directly connected in the module. PCK2, CPT2, DECR1, FAHD2A, ALDH2, GSTM1, SORD, and UQCRFS1 support gluconeogenic, mitochondrial, lipid-oxidation, aldehyde-detoxification, polyol, and respiratory functions. RIGI and KNG1 may represent immune or blood-associated biology rather than the central metabolic program. This is a biologically coherent interpretation, but it remains an inference because no GO/KEGG term passed global correction and STRING enrichment was absent.

**Cell composition.** The module is predominantly composed of intracellular metabolic proteins rather than plasma or secreted proteins. HPA describes frequent liver enrichment, hepatocyte specificity, and detection in both tissues for many members, supporting a liver-like metabolic component. Most genes have low immune-cell specificity, and only KNG1 is annotated as secreted to blood; therefore this does not look primarily like a plasma-protein or blood-cell module. KNG1 is liver-enriched, blood-secreted, and not detected in immune cells, so it could reflect circulating protein contribution rather than a shared intracellular program. The HPA pattern also includes skeletal muscle and other tissue enrichments, indicating that some co-abundance may reflect shared metabolic cell states or tissue composition. The absence of PCK2 protein detection in cervix and the absence of ALDH2 detection in both tissues caution against interpreting every member as a uniformly active protein program in both organs.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The strongest established STRING relationship is the AGL-GYS1 pair. This agrees with their complementary roles in glycogen breakdown and glycogen synthesis and supports a glycogen-related core. No STRING functional enrichment was reported, and the remaining module relationships were not supported by high-confidence STRING interactions. hu.MAP provides additional complex-level support: GYS1 and AGL co-occur in several glycogen-related complexes (hu.MAP huMAP3_10227.1), (hu.MAP huMAP3_09760.1), (hu.MAP huMAP3_13075.1), (hu.MAP huMAP3_11993.1), and (hu.MAP huMAP3_12186.1); CPT2 and PCK2 co-occur in mitochondrial metabolic complexes (hu.MAP huMAP3_10835.1) and (hu.MAP huMAP3_13468.1); and KNG1 and ALDH2 co-occur in a larger complex containing many plasma, complement, coagulation, and metabolic proteins (hu.MAP huMAP3_15040.1). These hu.MAP observations show that selected pairs have known complex context, but they do not establish one physical complex containing the entire module. The sparse direct interaction evidence therefore favors a co-abundance network assembled from partially connected metabolic and tissue-composition signals rather than a single demonstrated molecular complex.

**STRING interactions (score >= 0.7)**: 1 of 78 gene pairs: AGL–GYS1 (0.944)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10835.1 (CPT2, PCK2; 2/7); huMAP3_10227.1 (GYS1, AGL; 2/14); huMAP3_09760.1 (GYS1, AGL; 2/15); huMAP3_13075.1 (GYS1, AGL; 2/15); huMAP3_11993.1 (GYS1, AGL; 2/20); huMAP3_12186.1 (GYS1, AGL; 2/23); huMAP3_15040.1 (KNG1, ALDH2; 2/64); huMAP3_13468.1 (CPT2, PCK2; 2/99)

### Novelty

This module may represent a new tissue-pair co-abundance observation, but it cannot be called a definitively new biological mechanism from the available evidence. Its glycogen, mitochondrial, lipid-oxidation, gluconeogenic, and detoxification components are established biology, and the AGL-GYS1 relationship is already known through STRING and hu.MAP. The apparent novelty is instead the particular cross-tissue co-abundance combination and its coordination between cervix_uterine and liver. Lack of STRING or hu.MAP support for many edges does not prove novelty, because those resources capture physical interactions and curated complexes rather than all expression or protein-abundance covariation. The online search retrieved a review concerning lysosomal glucose sensing and glycophagy, which is relevant metabolic context but does not validate this exact module. Independent cohorts, quantitative replication, cell-composition adjustment, and targeted validation would be required before claiming a new conserved mechanism.

**Hypothesis.** Hypothesis: the module reflects a conserved nutrient and energetic-state program in which glycogen storage and mobilization, mitochondrial substrate use, gluconeogenic handling, redox detoxification, and respiratory capacity vary together across liver and cervix samples. GYS1-AGL may form the glycogen-related anchor, while PCK2, CPT2, DECR1, FAHD2A, ALDH2, GSTM1, SORD, and UQCRFS1 report coordinated carbon flux, fatty-acid use, aldehyde and xenobiotic handling, and mitochondrial activity. KNG1 may add a liver-derived circulating component, and RIGI may reflect sample-specific innate-immune state. A further possibility is that the shared signal is partly driven by hepatocyte-like or other metabolically active cell content rather than coordinated regulation within all cervix cells. This hypothesis is not established by enrichment, because no GO/KEGG term passed global correction and the network contains few known direct interactions.

Web sources: https://www.sciencedirect.com/science/article/pii/S1043276023001522

### Important genes

#### GYS1

- **Related proteins** (co-abundance neighbors): RIGI (0.89), AGL (0.83), GSTM1 (0.82), KNG1 (0.81), FAHD2A (0.80); STRING partners: AGL (0.944)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: glycogen synthase 1. The protein encoded by this gene catalyzes the addition of glucose monomers to the growing glycogen molecule through the formation of alpha-1,4-glycoside linkages. Mutations in this gene are associated with muscle glycogen storage disease. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: glycogen storage disease due to muscle and heart glycogen synthase deficiency (0.784); disorder of glycogen metabolism (0.530); neurodegenerative disease (0.440); glycogen storage disease XV (0.382); congenital myasthenic syndrome (0.266)
- **Europe PMC papers**: 1794
- **Why important**: GYS1 has the strongest network position in the module and connects the glycogen-related anchor to RIGI, AGL, GSTM1, KNG1, and FAHD2A. It catalyzes glycogen synthesis, has direct STRING support with AGL, appears in multiple hu.MAP glycogen-related complexes (hu.MAP huMAP3_10227.1), (hu.MAP huMAP3_09760.1), (hu.MAP huMAP3_13075.1), (hu.MAP huMAP3_11993.1), and (hu.MAP huMAP3_12186.1), and has extensive literature and disease evidence for glycogen-storage disorders.
- **Conclusion**: Established evidence supports GYS1 as a central glycogen-metabolism marker and a plausible network hub. It is reasonable to treat GYS1 as important for module interpretation, but the data do not establish that GYS1 regulates the other module genes or that glycogen metabolism is globally enriched in the module.

#### AGL

- **Related proteins** (co-abundance neighbors): GYS1 (0.83); STRING partners: GYS1 (0.944)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase. This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs…
- **Diseases (Open Targets)**: glycogen storage disease III (0.831); disorder of glycogen metabolism (0.768); glycogen storage disease XV (0.608); hereditary disease (0.507); Acute rhabdomyolysis (0.463)
- **Europe PMC papers**: 4441
- **Why important**: AGL is the functional complement of GYS1, encoding the glycogen debranching enzyme. Its direct high-confidence STRING relationship with GYS1 and repeated hu.MAP membership with GYS1 (hu.MAP huMAP3_10227.1), (hu.MAP huMAP3_09760.1), (hu.MAP huMAP3_13075.1), (hu.MAP huMAP3_11993.1), and (hu.MAP huMAP3_12186.1) give it unusually strong structural support within this otherwise sparse network. It also has substantial literature and established glycogen-storage-disease associations.
- **Conclusion**: Established evidence supports AGL as the best partner to GYS1 and as a marker of glycogen turnover. The hypothesis that the pair defines the main conserved module process is plausible, but it remains provisional because global enrichment was not demonstrated.

#### GSTM1

- **Related proteins** (co-abundance neighbors): TOR1AIP2 (0.84), SORD (0.84), PCK2 (0.83), GYS1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutathione S-transferase mu 1. Cytosolic and membrane-bound forms of glutathione S-transferase are encoded by two distinct supergene families. At present, eight distinct classes of the soluble cytoplasmic mammalian glutathione S-transferases have been identified: alpha, kappa, mu, omega, pi, sigma, theta and zeta. This gene encodes a glutathione S-transferase that belongs to the mu class. The mu class of enzymes functions in th…
- **Diseases (Open Targets)**: urinary bladder carcinoma (0.406); urinary bladder cancer (0.175); restless legs syndrome (0.159); breast carcinoma (0.149); metabolic syndrome (0.144)
- **Europe PMC papers**: 9390
- **Why important**: GSTM1 has one of the strongest network positions and links SORD, PCK2, TOR1AIP2, and GYS1. HPA identifies it as liver-enhanced and detected in both tissues. Its established glutathione-transferase function connects the module to electrophile, xenobiotic, and oxidative-stress handling, and it has a large literature base and disease-association record.
- **Conclusion**: Established evidence supports GSTM1 as a liver-associated detoxification and redox marker that may connect carbohydrate metabolism with chemical-stress handling. Its position supports a coordinating role in the co-abundance pattern, but does not prove direct biochemical coupling to GYS1, PCK2, or SORD.

#### PCK2

- **Related proteins** (co-abundance neighbors): GSTM1 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_10835.1, huMAP3_13468.1
- **Function (MyGene.info)**: phosphoenolpyruvate carboxykinase 2, mitochondrial. This gene encodes a mitochondrial enzyme that catalyzes the conversion of oxaloacetate to phosphoenolpyruvate in the presence of guanosine triphosphate (GTP). A cytosolic form of this protein is encoded by a different gene and is the key enzyme of gluconeogenesis in the liver. Alternatively spliced transcript variants have been described. [provided by RefSeq, Apr 2014].
- **Diseases (Open Targets)**: phosphoenolpyruvate carboxykinase deficiency, mitochondrial (0.511); phosphoenolpyruvate carboxykinase deficiency (0.443); neuropathy (0.187); Gait disturbance (0.185); retinitis pigmentosa (0.148)
- **Europe PMC papers**: 2644
- **Why important**: PCK2 is a mitochondrial enzyme involved in conversion of oxaloacetate to phosphoenolpyruvate and is associated with gluconeogenesis, insulin response, starvation response, and mitochondrial metabolism. It connects to GSTM1 and is represented with CPT2 in hu.MAP complexes (hu.MAP huMAP3_10835.1) and (hu.MAP huMAP3_13468.1). It is liver- and hepatocyte-enriched and has substantial literature and disease evidence.
- **Conclusion**: Established evidence supports PCK2 as an important mitochondrial carbon-routing marker and a strong explanation for the liver-like component of the module. Its lack of HPA protein detection in cervix means that a shared cervix mechanism should not be assumed; the cervix signal could reflect abundance variation, cell composition, or a related metabolic state.

#### CPT2

- **Related proteins** (co-abundance neighbors): FAHD2A (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_10835.1, huMAP3_13468.1
- **Function (MyGene.info)**: carnitine palmitoyltransferase 2. The protein encoded by this gene is a nuclear protein which is transported to the mitochondrial inner membrane. Together with carnitine palmitoyltransferase I, the encoded protein oxidizes long-chain fatty acids in the mitochondria. Defects in this gene are associated with mitochondrial long-chain fatty-acid (LCFA) oxidation disorders. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: carnitine palmitoyl transferase II deficiency, myopathic form (0.830); carnitine palmitoyl transferase II deficiency, severe infantile form (0.800); carnitine palmitoyl transferase II deficiency, neonatal form (0.772); carnitine palmitoyltransferase II deficiency (0.710); hereditary disease (0.505)
- **Europe PMC papers**: 5133
- **Why important**: CPT2 is a liver-enhanced mitochondrial enzyme required for the carnitine shuttle and long-chain fatty-acid oxidation. It connects to FAHD2A and co-occurs with PCK2 in hu.MAP complexes (hu.MAP huMAP3_10835.1) and (hu.MAP huMAP3_13468.1). Its extensive literature and strong disease evidence for several forms of CPT2 deficiency make it a biologically important indicator of mitochondrial lipid utilization.
- **Conclusion**: Established evidence supports CPT2 as a marker of mitochondrial fatty-acid oxidation and gives the module a broader energetic interpretation than glycogen metabolism alone. Its role as a driver of the cross-tissue co-abundance pattern is a hypothesis, not a demonstrated causal relationship.

## Module 11

**Tissue pair**: cervix_uterine and liver  
**Genes (18)**: ATP5F1C, CNN3, TSFM, FABP5, HMOX2, EIF4E, DTYMK, LACTB2, PMM2, PSMA1, RAB10, RAB21, RAN, RPL9, MRPL11, STT3A, STX7, TPD52L2

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. The gene composition nevertheless suggests a mixed cellular homeostasis program rather than a single established pathway. The module combines mitochondrial translation and energy-related genes such as MRPL11, TSFM, and ATP5F1C; cytosolic translation and translation control through RPL9 and EIF4E; glycoprotein biosynthesis through PMM2 and STT3A; vesicle and membrane trafficking through RAB21, RAB10, and STX7; and cytoskeletal or epithelial organization through CNN3 and FABP5. These annotations support a cautious interpretation involving biosynthetic capacity, organelle function, membrane traffic, and epithelial or cellular structural maintenance. Because the co-abundance graph spans several cellular systems and lacks globally significant enrichment, it should not be labeled as a defined mitochondrial, glycosylation, or vesicle complex.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only one member is annotated as secreted, while the others are intracellular, membrane-associated, mitochondrial, cytosolic, nuclear, lysosomal, or vesicular. Most genes have low tissue specificity, and most have cell-type-enhanced rather than cell-type-enriched expression. Immune-cell specificity is generally low, with only a small subset showing immune-cell enhancement or enrichment; therefore the module does not appear to be primarily a blood-cell signature. Protein detection is broad in both cervix and liver, although several genes are absent in one tissue and some show tissue-enhanced expression. The shared signal may consequently reflect broadly active cellular machinery, common cell populations, or sample-composition effects rather than a tissue-specific secretory program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited connected core. Known high-confidence relationships involve ATP5F1C with RPL9 and TSFM, MRPL11 with RPL9 and TSFM, and RPL9 with STT3A and TSFM. These links provide prior support for relationships among mitochondrial translation, ATP synthesis, ribosomal machinery, and glycoprotein processing, but they do not establish that all module members form one physical complex. The remaining module connections are not represented by high-confidence STRING relationships. No hu.MAP complex contains multiple module members. Thus, the network is partly anchored by known interactions but is not equivalent to a previously catalogued multiprotein complex.

**STRING interactions (score >= 0.7)**: 6 of 153 gene pairs: ATP5F1C–RPL9 (0.887); ATP5F1C–TSFM (0.884); MRPL11–RPL9 (0.834); MRPL11–TSFM (0.88); RPL9–STT3A (0.806); RPL9–TSFM (0.797)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance module may represent a new tissue-shared expression association, but the fact sheet does not establish it as a new biological mechanism. Its genes have individually established functions and disease links, and several of its STRING relationships are already known. The absence of a matching hu.MAP complex and the sparse STRING connectivity argue against simple recovery of one canonical complex, but absence from those resources alone cannot prove novelty. A defensible novelty claim would require replication in independent cervix and liver datasets, assessment against cell-composition covariates, and comparison with published co-expression modules. At present, the strongest conclusion is that the shared co-abundance pattern is a candidate integrative signal linking common cellular machinery across the two tissues.

**Hypothesis.** Hypothesis: the module reflects coordinated maintenance of biosynthetic and organelle functions in a shared epithelial or parenchymal cell population. In this model, mitochondrial translation and ATP production support cellular activity; EIF4E and RPL9 support protein synthesis; PMM2 and STT3A support glycoprotein maturation; and RAB21, RAB10, STX7, and CNN3 coordinate trafficking, adhesion, and cytoskeletal organization. The observed co-abundance could therefore arise from a shared demand for protein production, energy metabolism, membrane trafficking, and structural maintenance rather than from direct physical interaction among all genes. This hypothesis should be tested by cell-type deconvolution, replication across samples, and perturbation or spatial assays.

### Important genes

#### CNN3

- **Related proteins** (co-abundance neighbors): RAB21 (0.88), RAB10 (0.87), STX7 (0.83), TPD52L2 (0.82), RPL9; RPL9P7; RPL9P8; RPL9P9 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calponin 3. This gene encodes a protein with a markedly acidic C terminus; the basic N-terminus is highly homologous to the N-terminus of a related gene, CNN1. Members of the CNN gene family all contain similar tandemly repeated motifs. This encoded protein is associated with the cytoskeleton but is not involved in contraction. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.492); pleural empyema (0.256); pneumothorax (0.256); biliary tract disorder (0.247); tooth disorder (0.196)
- **Europe PMC papers**: 1628
- **Why important**: CNN3 has the strongest network position in the module and connects to RAB21, RAB10, STX7, TPD52L2, and RPL9. Its annotated roles in actin filament organization, actomyosin structure, epithelial differentiation, and cell-cell adhesion make it a plausible bridge between structural organization and membrane trafficking. It is detected in both tissues and has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports CNN3 as a cytoskeletal and adhesion-related component with broad tissue presence. Its central position supports involvement in the module, but the data do not establish that CNN3 drives the shared tissue signal. A role linking epithelial structure to trafficking is a hypothesis.

#### PMM2

- **Related proteins** (co-abundance neighbors): HMOX2 (0.90), MRPL11 (0.85), EIF4E (0.83), ATP5F1C (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphomannomutase 2. The protein encoded by this gene catalyzes the isomerization of mannose 6-phosphate to mannose 1-phosphate, which is a precursor to GDP-mannose necessary for the synthesis of dolichol-P-oligosaccharides. Mutations in this gene have been shown to cause defects in glycoprotein biosynthesis, which manifests as carbohydrate-deficient glycoprotein syndrome type I. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: PMM2-congenital disorder of glycosylation (0.869); hereditary disease (0.544); cerebellar ataxia (0.482); isolated cerebellar hypoplasia/agenesis (0.478); congenital disorder of glycosylation (0.457)
- **Europe PMC papers**: 1516
- **Why important**: PMM2 is highly connected to HMOX2, MRPL11, EIF4E, and ATP5F1C. It catalyzes a required step in GDP-mannose production and is directly involved in glycoprotein biosynthesis and N-linked glycosylation. Its strong disease association with congenital disorders of glycosylation gives it clear functional and clinical importance.
- **Conclusion**: Established evidence identifies PMM2 as a core glycan-precursor and glycoprotein-biosynthesis enzyme. Its network position suggests coordination with translation and mitochondrial machinery, but no globally significant enrichment or physical complex supports a specific integrated pathway. The proposed coordination remains a hypothesis.

#### MRPL11

- **Related proteins** (co-abundance neighbors): TSFM (0.86), PMM2 (0.85), EIF4E (0.84), RAB10 (0.82); STRING partners: RPL9 (0.834), TSFM (0.88)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein L11. This nuclear gene encodes a 39S subunit component of the mitochondial ribosome. Alternative splicing results in multiple transcript variants. Pseudogenes for this gene are found on chromosomes 5 and 12. [provided by RefSeq, May 2014].
- **Diseases (Open Targets)**: neurodegenerative disease (0.484); type 2 diabetes mellitus (0.300); diabetes mellitus (0.264); bipolar disorder (0.023); asthma (0.019)
- **Europe PMC papers**: 355
- **Why important**: MRPL11 is among the more connected genes and links TSFM, PMM2, EIF4E, and RAB10. It is a mitochondrial ribosomal component with an established role in mitochondrial translation, and its STRING relationships with RPL9 and TSFM provide prior interaction support. Its disease associations further emphasize the biological importance of mitochondrial protein synthesis.
- **Conclusion**: Established evidence supports MRPL11 as a mitochondrial translation component and as part of a known interaction neighborhood. Its position makes it a credible anchor for the organelle-related aspect of the module, but it does not prove that mitochondrial translation explains the complete module.

#### RAB10

- **Related proteins** (co-abundance neighbors): CNN3 (0.87), MRPL11 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB10, member RAS oncogene family. RAB10 belongs to the RAS (see HRAS; MIM 190020) superfamily of small GTPases. RAB proteins localize to exocytic and endocytic compartments and regulate intracellular vesicle trafficking (Bao et al., 1998 [PubMed 9918381]).[supplied by OMIM, Mar 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.549); digestive system disorder (0.242); cervical carcinoma (0.215); lobular capilliary hemangioma (0.165); hepatocellular carcinoma (0.109)
- **Europe PMC papers**: 2856
- **Why important**: RAB10 connects CNN3 and MRPL11 and is annotated for exocytosis, Golgi-to-plasma-membrane transport, endosomal transport, and vesicle-mediated transport. It is detected in both tissues and has extensive literature and disease-association coverage, including links to cervical and liver malignancy contexts.
- **Conclusion**: Established evidence supports RAB10 as a membrane-trafficking regulator. Its connection to CNN3 supports a possible relationship between trafficking and cellular architecture, while its connection to MRPL11 is more plausibly co-abundance than a demonstrated direct mechanism. A role in coordinating biosynthetic output with membrane delivery is a hypothesis.

#### STT3A

- **Related proteins** (co-abundance neighbors): RAB21 (0.86); STRING partners: RPL9 (0.806)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: STT3 oligosaccharyltransferase complex catalytic subunit A. The protein encoded by this gene is a catalytic subunit of the N-oligosaccharyltransferase (OST) complex, which functions in the endoplasmic reticulum to transfer glycan chains to asparagine residues of target proteins. A separate complex containing a similar catalytic subunit with an overlapping function also exists. Multiple transcript variants encoding different isoforms have been found for thi…
- **Diseases (Open Targets)**: congenital disorder of glycosylation, type Iw, autosomal dominant (0.751); STT3A-congenital disorder of glycosylation (0.740); dengue disease (0.512); COVID-19 (0.370); hereditary disease (0.192)
- **Europe PMC papers**: 944
- **Why important**: STT3A is the catalytic subunit of an endoplasmic-reticulum oligosaccharyltransferase complex and performs co-translational N-linked glycosylation. It connects RAB21 in the module, while STRING independently links it to RPL9. Its established congenital glycosylation disease associations make it important for interpreting protein maturation and quality-control aspects of the module.
- **Conclusion**: Established evidence supports STT3A as a central enzyme in co-translational glycoprotein maturation. The module provides a plausible co-abundance context involving translation and trafficking, but there is no globally significant enrichment or hu.MAP support for a module-wide glycosylation complex.

#### EIF4E

- **Related proteins** (co-abundance neighbors): MRPL11 (0.84), PMM2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 4E. The protein encoded by this gene is a component of the eukaryotic translation initiation factor 4F complex, which recognizes the 7-methylguanosine cap structure at the 5' end of messenger RNAs. The encoded protein aids in translation initiation by recruiting ribosomes to the 5'-cap structure. Association of this protein with the 4F complex is the rate-limiting step in translation initiation. This …
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); dengue disease (0.379); autism (0.378); substance-related disorder (0.133); neoplasm (0.115)
- **Europe PMC papers**: 17652
- **Why important**: EIF4E is connected to MRPL11 and PMM2 and is a well-studied rate-limiting component of cap-dependent translation initiation. Its extensive literature and proto-oncogenic associations make it an informative marker of translational demand and growth-related cellular state, even though its graph degree is not among the highest.
- **Conclusion**: Established evidence supports EIF4E as a translation-initiation regulator with broad relevance to proliferation and disease. Its co-abundance with mitochondrial and glycosylation genes may indicate shared biosynthetic demand, but the module does not demonstrate direct functional coupling or oncogenic activity in either tissue.

## Module 12

**Tissue pair**: cervix_uterine and liver  
**Genes (19)**: BCLAF1, DYNC1I2, DCTN1, DIAPH1, FLNA, GTF2I, IFI16, NUP98, PDHB, PRPF31, PFAS, ADSL, RAD50, RO60, SEPTIN9, SNW1, TMOD3, XPO7, ZW10

### Function

The strongest defensible functional description is a broadly distributed intracellular supramolecular-complex module, supported by (GO:CC supramolecular complex; q_global = 0.0128), which covers genes involved in cytoskeletal organization, microtubule-based transport, nuclear transport, RNA processing, transcriptional regulation, DNA-damage responses, cell division, purine synthesis, and mitochondrial energy metabolism. The network links these themes through high-connectivity genes such as TMOD3, DCTN1, NUP98 and PFAS, but (GO:CC supramolecular complex; q_global = 0.0128) does not establish one single biochemical pathway. The module therefore appears to represent coordinated cellular architecture and transport, together with gene-expression and metabolic functions, rather than a narrowly specialized tissue pathway. No other GO or KEGG term is primary evidence; specifically, no GO or KEGG term passed global correction beyond (GO:CC supramolecular complex; q_global = 0.0128).

**Cell composition.** This is not a plasma-protein or secreted-protein module: HPA reports no secreted genes, and the proteins detected in cervix_uterine and liver are predominantly intracellular. Most genes have low tissue specificity, so the shared signal is compatible with broadly expressed cellular machinery rather than a tissue-exclusive program. HPA does show several cell-type-enhanced patterns, including neutrophils, platelets, erythrocyte progenitors, endothelial or vascular-related cells, and other cell types, but overall blood-cell specificity is low. Thus, a blood or shared-cell-type contribution cannot be excluded, especially for genes such as PFAS, DIAPH1 and IFI16, yet the evidence does not support calling this primarily a blood-cell module. The absence of secretion and the broad intracellular localization argue against a simple circulating-protein explanation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC supramolecular complex | 0.0128 | BCLAF1, DCTN1, DIAPH1, DYNC1I2, FLNA, IFI16, NUP98, PRPF31, SEPTIN9, SNW1, TMOD3, ZW10 |

### STRING and hu.MAP

STRING provides a limited set of high-confidence relationships. The strongest reported links are DCTN1 with DYNC1I2, ADSL with PFAS, BCLAF1 with SNW1, DCTN1 with ZW10, and FLNA with SEPTIN9. These relationships support real submodules involving dynein and dynactin transport, purine metabolism, nuclear RNA or transcriptional regulation, and the actin or septin cytoskeleton. STRING supplementary compartment evidence (STRING COMPARTMENTS Nuclear body; within-query FDR = 0.017) places NUP98, PRPF31, RO60, IFI16, BCLAF1 and SNW1 in a nuclear-body context, but (STRING COMPARTMENTS Nuclear body; within-query FDR = 0.017) is not globally corrected enrichment evidence. hu.MAP contributes one lower-confidence broad complex connection (hu.MAP huMAP3_11232.1), containing ZW10 and XPO7 among many other proteins. The limited overlap with hu.MAP and the small number of STRING links indicate that the co-abundance network is not simply a direct copy of one established physical complex; it combines several known cellular systems.

**STRING interactions (score >= 0.7)**: 5 of 171 gene pairs: ADSL–PFAS (0.847); BCLAF1–SNW1 (0.823); DCTN1–DYNC1I2 (0.997); DCTN1–ZW10 (0.719); FLNA–SEPTIN9 (0.707)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nuclear body (FDR = 0.017, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11232.1 (ZW10, XPO7; 2/78)

### Novelty

A new biological mechanism cannot be claimed from these data alone. The individual components and several pairwise relationships are well established, while many module pairs are absent from the supplied STRING and hu.MAP results. That absence may reflect incomplete interaction coverage, context dependence, indirect regulation, or co-abundance rather than biological novelty. The potentially novel result is the conserved co-abundance organization of these otherwise familiar intracellular systems across cervix_uterine and liver. Demonstrating novelty would require independent replication, comparison with existing tissue co-expression studies, and preferably perturbation or physical-interaction experiments. On the present evidence, this is best described as a potentially informative cross-tissue module, not a proven new complex or pathway.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-maintenance state in which cytoskeletal and microtubule systems coordinate intracellular transport and organelle positioning with nuclear pore function, RNA processing, DNA surveillance, cell-cycle control, and biosynthetic energy demands. TMOD3, FLNA, SEPTIN9 and DIAPH1 may provide cytoskeletal context; DCTN1, DYNC1I2 and ZW10 may support transport and spindle-related organization; NUP98, XPO7, PRPF31, BCLAF1 and SNW1 may connect nuclear trafficking with RNA and transcriptional regulation; and PFAS, ADSL and PDHB may reflect purine and central-carbon metabolic support. This is a mechanistic model rather than a demonstrated physical assembly. A blood-cell or shared-cell-type contribution remains an alternative explanation and should be tested by cell-composition adjustment and cell-resolved data.

### Important genes

#### TMOD3

- **Related proteins** (co-abundance neighbors): PFAS (0.89), SNW1 (0.87), NUP98 (0.85), BCLAF1 (0.84), PRPF31 (0.84), IFI16 (0.81), PDHB (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tropomodulin 3. Enables cadherin binding activity involved in cell-cell adhesion. Predicted to be involved in actin filament organization; muscle contraction; and myofibril assembly. Predicted to act upstream of or within actin cytoskeleton organization; erythrocyte development; and positive regulation of mitotic cell cycle phase transition. Located in adherens junction. [provided by Alliance of Genome Resources,…
- **Diseases (Open Targets)**: myasthenia gravis (0.278); dementia (0.192); intelligence (0.088); cancer (0.075); glioblastoma (0.065)
- **Europe PMC papers**: 675
- **Why important**: TMOD3 has the strongest network position in the module and is included in (GO:CC supramolecular complex; q_global = 0.0128). Its annotated functions in actin filament organization, cell-cell adhesion, pointed-end actin capping and muscle-related processes make it a plausible bridge between the module's supramolecular-complex signal and cytoskeletal organization. It is detected in both tissues, has broad tissue distribution with cell-type enhancement, and has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports TMOD3 as a highly connected actin-associated component of the module. It is reasonable to hypothesize that TMOD3 helps organize the cytoskeletal arm of the shared signal, but the co-abundance data do not prove that it physically coordinates the nuclear, transport or metabolic genes.

#### DCTN1

- **Related proteins** (co-abundance neighbors): GTF2I (0.87), XPO7 (0.85), NUP98 (0.84), ZW10 (0.84), RAD50 (0.82), ADSL (0.81); STRING partners: DYNC1I2 (0.997), ZW10 (0.719)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynactin subunit 1. This gene encodes the largest subunit of dynactin, a macromolecular complex consisting of 10 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein. Dynactin is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, chromosome movement, nuclear positi…
- **Diseases (Open Targets)**: Perry syndrome (0.798); amyotrophic lateral sclerosis (0.764); neuronopathy, distal hereditary motor, type 7B (0.743); cancer (0.547); neurodegenerative disease (0.530)
- **Europe PMC papers**: 1985
- **Why important**: DCTN1 is among the most connected genes and is linked in STRING to DYNC1I2 and ZW10, including a particularly strong DCTN1-DYNC1I2 relationship. It encodes the largest dynactin subunit and connects dynein-dependent microtubule transport with spindle formation, chromosome movement, nuclear positioning and organelle transport. It is detected in both tissues and has extensive literature and disease relevance.
- **Conclusion**: Established evidence identifies DCTN1 as the clearest transport-related hub and as part of known dynein or dynactin relationships. Its role as a connector from transport to the rest of the module is a supported network interpretation, whereas a tissue-specific transport mechanism remains hypothetical.

#### NUP98

- **Related proteins** (co-abundance neighbors): RAD50 (0.86), TMOD3 (0.85), DCTN1 (0.84), SEPTIN9 (0.82), DIAPH1 (0.81), PFAS (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 98 and 96 precursor. Nuclear pore complexes (NPCs) regulate the transport of macromolecules between the nucleus and cytoplasm, and are composed of many polypeptide subunits, many of which belong to the nucleoporin family. This gene belongs to the nucleoporin gene family and encodes a 186 kDa precursor protein that undergoes autoproteolytic cleavage to generate a 98 kDa nucleoporin and 96 kDa nucleoporin. The 98 kDa nu…
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.542); HIV infectious disease (0.541); viral infectious disease (0.531); acute myeloid leukemia (0.399); lung carcinoma (0.376)
- **Europe PMC papers**: 4839
- **Why important**: NUP98 has high network connectivity, belongs to (GO:CC supramolecular complex; q_global = 0.0128), and is also represented in the supplementary nuclear-body result (STRING COMPARTMENTS Nuclear body; within-query FDR = 0.017). Its established functions include nucleocytoplasmic transport, nuclear-pore organization, RNA export and nuclear-periphery organization. It connects to RAD50, TMOD3, DCTN1, SEPTIN9, DIAPH1 and PFAS in the module network, placing nuclear transport at an interface with cytoskeletal, repair and metabolic signals. It has extensive literature and disease-association evidence.
- **Conclusion**: Established evidence supports NUP98 as a central nuclear-transport and RNA-trafficking component. The hypothesis that it coordinates the module's nuclear and cytoskeletal arms is plausible from network position, but no direct physical interaction with most of those module genes is established by the supplied databases.

#### PFAS

- **Related proteins** (co-abundance neighbors): PRPF31 (0.90), TMOD3 (0.89), PDHB (0.87), XPO7 (0.81), NUP98 (0.80); STRING partners: ADSL (0.847)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoribosylformylglycinamidine synthase. Purines are necessary for many cellular processes, including DNA replication, transcription, and energy metabolism. Ten enzymatic steps are required to synthesize inosine monophosphate (IMP) in the de novo pathway of purine biosynthesis. The enzyme encoded by this gene catalyzes the fourth step of IMP biosynthesis. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: dyskeratosis congenita (0.520); Coats plus syndrome (0.455); neurodegenerative disease (0.187); hereditary disease (0.174); retinal disorder (0.118)
- **Europe PMC papers**: 3393
- **Why important**: PFAS has substantial network connectivity and links in STRING to ADSL, forming a known purine-biosynthesis relationship. Its annotated enzyme function is a step in de novo IMP and GMP biosynthesis, while HPA shows enhancement in erythrocyte progenitors and neutrophils and detection in liver. It therefore provides a metabolic interpretation that also warrants attention to possible hematopoietic or cell-composition effects. It has a substantial literature and disease-association record.
- **Conclusion**: Established evidence supports PFAS as a purine-biosynthetic enzyme and as part of a known ADSL-associated metabolic relationship. Its placement beside transport, nuclear and cytoskeletal genes may reflect shared cellular demand or co-abundance rather than a single purine complex; a blood-cell contribution is an alternative hypothesis.

#### BCLAF1

- **Related proteins** (co-abundance neighbors): FLNA (0.86), SEPTIN9 (0.85), TMOD3 (0.84), PDHB (0.81); STRING partners: SNW1 (0.823)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCL2 associated transcription factor 1. This gene encodes a transcriptional repressor that interacts with several members of the BCL2 family of proteins. Overexpression of this protein induces apoptosis, which can be suppressed by co-expression of BCL2 proteins. The protein localizes to dot-like structures throughout the nucleus, and redistributes to a zone near the nuclear envelope in cells undergoing apoptosis. Multiple transcript var…
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); Pulmonary artery atresia (0.416); acute myeloid leukemia (0.357); bronchial disorder (0.288); Vertigo (0.253)
- **Europe PMC papers**: 1702
- **Why important**: BCLAF1 is included in (GO:CC supramolecular complex; q_global = 0.0128), connects to FLNA, SEPTIN9, TMOD3 and PDHB, and has a known STRING relationship with SNW1. Its annotations encompass transcriptional regulation, mRNA stabilization, apoptosis and DNA-damage response, while HPA places it in nuclear speckles and shows detection in both tissues. Its network position links nuclear regulation to cytoskeletal and metabolic neighbors, and it has substantial literature and disease-association evidence.
- **Conclusion**: Established evidence supports BCLAF1 as a nuclear transcriptional and RNA-regulatory component with apoptosis and DNA-damage relevance. It is a plausible integrator of the nuclear and cytoskeletal portions of the module, but the module does not establish that BCLAF1 drives the shared tissue signal or directly binds all of its neighbors.

## Module 13

**Tissue pair**: cervix_uterine and liver  
**Genes (11)**: CALU, COPG2, CLINT1, ME2, OSGEP, P3H1, PSMC4, PSMC2, POLR2B, CTTN, TTLL12

### Function

The module does not have a GO or KEGG term that passed global correction. Its structure nevertheless suggests a mixed intracellular maintenance program rather than a single established pathway. The strongest direct functional signal is the proteasome regulatory ATPase pair PSMC2 and PSMC4, which is supported by their exceptionally strong STRING relationship and their membership in the same hu.MAP proteasome-related complexes (hu.MAP huMAP3_05064.1). Other genes represent distinct cellular processes: collagen maturation and protein folding through P3H1 and CALU, transcription through POLR2B, vesicle trafficking through CLINT1 and COPG2, mitochondrial metabolism through ME2, tRNA modification through OSGEP, chromatin and cell-cycle regulation through TTLL12, and epithelial cytoskeletal organization through CTTN. Thus, the most defensible interpretation is coordinated abundance of broadly used protein-processing, trafficking, transcriptional, metabolic, and structural machinery, with a proteasome component that is biologically coherent but not sufficient to define the entire module. No GO or KEGG term passed global correction; nominal or within-module results are not used as primary evidence.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only P3H1 and CALU have intracellular or membrane-associated secretome classifications, and the remaining proteins are intracellular. HPA indicates generally low tissue specificity for most genes, with only ME2 and TTLL12 showing tissue-enhanced patterns. Most genes show low immune-cell specificity, although CLINT1 is immune-cell enriched for basophils and CTTN is immune-cell enhanced for basophils and neutrophils. Several genes have cell-type-enhanced annotations in trophoblasts, epithelial cells, adipocytes, glia, and other specialized cell types, but these annotations are heterogeneous. Protein detection is broad in cervix and somewhat less complete in liver. Overall, the shared signal is more consistent with broadly expressed cellular machinery or shared cellular composition than with a blood or secreted-protein module, although minor blood-cell or cell-type contributions cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence interaction within the module, between PSMC2 and PSMC4. No other listed pair has a reported STRING interaction at the stated threshold, and STRING functional enrichment is absent. hu.MAP independently places PSMC2 and PSMC4 together in three proteasome-related complexes (hu.MAP huMAP3_05064.1), while the other module genes have no listed hu.MAP complex membership. These findings establish a known proteasome-associated core within the module, but they do not establish a single physical complex containing all module members. The sparse known interaction structure suggests that the co-abundance relationships outside the PSMC pair may reflect coordinated regulation, shared cellular state, or indirect biological coupling rather than direct binding.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: PSMC2–PSMC4 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05064.1 (PSMC2, PSMC4; 2/31); huMAP3_09656.1 (PSMC2, PSMC4; 2/64); huMAP3_13725.1 (PSMC2, PSMC4; 2/69)

### Novelty

This is not sufficient to claim a newly discovered molecular complex or pathway. The PSMC2–PSMC4 relationship and their proteasome context are already well established by STRING and hu.MAP (hu.MAP huMAP3_05064.1). The potentially novel aspect is the cross-tissue co-abundance grouping of these proteasome genes with genes involved in collagen processing, vesicle trafficking, transcription, metabolism, tRNA modification, chromatin regulation, and cytoskeletal organization. However, absence of the other relationships from STRING or hu.MAP does not prove novelty. The appropriate conclusion is that the module is a potentially interesting cross-tissue co-abundance pattern whose mechanistic novelty requires independent replication, perturbation, and comparison with existing co-expression resources.

**Hypothesis.** Hypothesis: the module reflects a shared cellular homeostasis state in which proteasome capacity, endoplasmic-reticulum protein folding, intracellular trafficking, transcription, mitochondrial metabolism, and epithelial structural maintenance vary together across cervix and liver samples. PSMC2 and PSMC4 may represent a proteostasis-related anchor, while P3H1 and CALU could connect that state to secretory or extracellular-matrix protein handling, and CLINT1, COPG2, and CTTN could reflect vesicle and membrane-cytoskeleton activity. This remains a hypothesis because the module lacks globally significant GO or KEGG enrichment and contains only one direct STRING interaction.

### Important genes

#### PSMC2

- **Related proteins** (co-abundance neighbors): OSGEP (0.83), POLR2B (0.80); STRING partners: PSMC4 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 is one of the module genes directly connected to PSMC4 by STRING and is present with PSMC4 in all three listed hu.MAP complexes (hu.MAP huMAP3_05064.1). It is a proteasome regulatory ATPase with a central role in ubiquitin-dependent protein catabolism and oxidative-stress response. Its network position is not the most connected, but its known physical relationship and coherent complex membership make it an important anchor. Its disease associations include plasma-cell myeloma, mantle-cell lymphoma, neoplasm, HIV infection, and amyloidosis, and its literature volume is substantial.
- **Conclusion**: Established evidence supports PSMC2 as a proteasome-associated component and as part of the module's best-supported physical relationship. It is plausible, but not established, that variation in proteasome capacity helps organize the broader cross-tissue co-abundance pattern.

#### PSMC4

- **Related proteins** (co-abundance neighbors): P3H1 (0.89); STRING partners: PSMC2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 4. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.603); mantle cell lymphoma (0.542); neoplasm (0.519); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1065
- **Why important**: PSMC4 has the strongest direct STRING relationship in the module through its interaction with PSMC2 and shares all three listed hu.MAP proteasome-related complexes with PSMC2 (hu.MAP huMAP3_05064.1). It is a proteasome regulatory ATPase involved in proteolysis, oxidative-stress response, and proteasome-mediated ubiquitin-dependent protein catabolism. It has the largest literature volume among the proteasome pair and disease associations including plasma-cell myeloma, mantle-cell lymphoma, neoplasm, HIV infection, and amyloidosis.
- **Conclusion**: Established evidence identifies PSMC4 as a proteasome regulatory subunit and confirms its connection to PSMC2. Its role as a functional driver of the whole module is a hypothesis rather than a demonstrated conclusion.

#### P3H1

- **Related proteins** (co-abundance neighbors): PSMC4 (0.89), CALU (0.82), CLINT1 (0.82), CTTN (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: prolyl 3-hydroxylase 1. This gene encodes an enzyme that is a member of the collagen prolyl hydroxylase family. These enzymes are localized to the endoplasmic reticulum and their activity is required for proper collagen synthesis and assembly. Mutations in this gene are associated with osteogenesis imperfecta type VIII. Three alternatively spliced transcript variants encoding different isoforms have been described. Other…
- **Diseases (Open Targets)**: osteogenesis imperfecta type 8 (0.751); osteogenesis imperfecta (0.642); osteogenesis imperfecta type 3 (0.533); osteogenesis imperfecta, recessive (0.455); osteogenesis imperfecta type 2 (0.370)
- **Europe PMC papers**: 676
- **Why important**: P3H1 has the highest network connectivity in the module and links the proteasome-associated branch through PSMC4 with CALU, CLINT1, and CTTN. It encodes an endoplasmic-reticulum collagen prolyl hydroxylase required for collagen synthesis and assembly, protein folding, protein stabilization, and regulation of protein secretion. It is associated with osteogenesis imperfecta type eight and related osteogenesis imperfecta conditions, and it has substantial literature support.
- **Conclusion**: Established evidence supports P3H1 as a collagen-processing and endoplasmic-reticulum protein-folding enzyme and as the principal network connector in this module. Its connections to proteasome, trafficking, and cytoskeletal genes suggest coordinated protein-handling biology, but do not prove direct mechanistic coupling.

#### POLR2B

- **Related proteins** (co-abundance neighbors): COPG2 (0.86), PSMC2 (0.80), CLINT1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase II subunit B. This gene encodes the second largest subunit of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase that catalyzes the transcription of DNA into precursors of mRNA, snRNA and microRNA. This subunit and the largest subunit form opposite sides of the center cleft of Pol II. Deletion of the flap loop region of this subunit results in a decrease in the rate of transcriptional elongation. Altern…
- **Diseases (Open Targets)**: HIV infectious disease (0.600); Orthomyxoviridae infectious disease (0.370); dengue disease (0.370); acrocephalosyndactyly (0.370); neurodegenerative disease (0.341)
- **Europe PMC papers**: 589
- **Why important**: POLR2B is a relatively well-connected module member linking COPG2, PSMC2, and CLINT1. It encodes the second-largest subunit of RNA polymerase II and participates in transcription initiation and elongation. Its broad tissue and cell-type profile is compatible with a general cellular-maintenance signal. It has extensive literature support and disease associations including viral infectious diseases, acrocephalosyndactyly, and neurodegenerative disease.
- **Conclusion**: Established evidence supports POLR2B as a core transcriptional enzyme and a broadly expressed cellular component. Its co-abundance with proteasome and trafficking genes may indicate shared cellular activity or regulation, but a specific transcriptional mechanism for this module is not established.

#### CALU

- **Related proteins** (co-abundance neighbors): P3H1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calumenin. The product of this gene is a calcium-binding protein localized in the endoplasmic reticulum (ER) and it is involved in such ER functions as protein folding and sorting. This protein belongs to a family of multiple EF-hand proteins (CERC) that include reticulocalbin, ERC-55, and Cab45 and the product of this gene. Alternatively spliced transcript variants encoding different isoforms have been iden…
- **Diseases (Open Targets)**: intelligence (0.490); mathematical ability (0.469); autism spectrum disorder (0.333); attention deficit-hyperactivity disorder (0.333); Alzheimer disease (0.308)
- **Europe PMC papers**: 9190
- **Why important**: CALU is directly connected to the most connected gene, P3H1, and encodes an endoplasmic-reticulum calcium-binding protein involved in protein folding and sorting. Its location and function complement the collagen-processing role of P3H1, giving this edge a biologically plausible protein-homeostasis interpretation. CALU also has a large literature base and reported associations with cognitive traits and neurological disease.
- **Conclusion**: Established evidence supports CALU as an endoplasmic-reticulum folding and sorting factor connected to P3H1 in the module. A shared endoplasmic-reticulum or secretory-protein handling state is a reasonable hypothesis, but the co-abundance data do not establish that CALU regulates P3H1.

## Module 14

**Tissue pair**: cervix_uterine and liver  
**Genes (5)**: CASP3, CLIC1, KRT19, PSMF1, S100A10

### Function

The module does not have any GO or KEGG term passing global correction. Its expression pattern is therefore best interpreted from the gene composition and network structure rather than from formal pathway enrichment. CASP3 is the most connected node and links genes associated with apoptosis, proteolytic regulation, intracellular chloride transport, epithelial structure, and membrane trafficking. KRT19 and S100A10 suggest an epithelial and vesicle-associated component, while CLIC1 and PSMF1 suggest cellular transport, redox-related activity, and regulation of proteasome-mediated protein turnover. Overall, the module is consistent with a context-dependent cellular maintenance or stress-response program involving epithelial integrity, intracellular trafficking, proteostasis, and apoptosis, but the data do not establish a single coherent biochemical pathway. The co-abundance signal may also reflect shared cell composition rather than coordinated molecular regulation.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its genes is annotated as secreted by HPA. KRT19 is an epithelial intermediate-filament gene with tissue-enhanced expression in several epithelial tissues, including esophagus, intestine, salivary gland, and urinary bladder. S100A10 also has tissue-enhanced annotation in esophagus. The remaining genes have low tissue specificity, while the single-cell annotations include epithelial, platelet, megakaryocytic, lymphoid, plasma-cell, and other immune-associated populations. KRT19 is not detected in immune cells, whereas several other module genes have platelet or blood-cell-associated annotations. Protein detection in both cervix and liver is common but not universal across the module. Thus, the shared module could reflect a mixture of epithelial and blood-associated cell contributions, including sample composition or blood content, rather than a tissue-independent mechanism. The HPA evidence does not support interpreting it as a secreted-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No within-module pair is supported by a high-confidence STRING interaction, and no hu.MAP complex contains multiple module members. Consequently, the co-abundance edges should not be treated as established physical binding or complex membership. The network nevertheless has an interpretable topology: CASP3 connects to KRT19, CLIC1, and PSMF1; KRT19 connects to S100A10; and CLIC1 connects to PSMF1. These links may represent correlated expression across samples, shared cell states, or indirect functional relationships. Established individual protein functions are compatible with apoptosis, epithelial organization, membrane trafficking, intracellular ion handling, and proteostasis, but the external interaction resources provide no direct support for a unified physical complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a dataset-specific co-abundance pattern, but it cannot be declared a new biological mechanism from the supplied evidence. The absence of high-confidence STRING interactions and multi-member hu.MAP complexes indicates that the particular combination is not corroborated there, yet absence from those resources does not prove novelty. The component genes and their broad functions are already established, and several are heavily studied. The lack of globally significant GO or KEGG enrichment further argues against presenting the module as a newly discovered canonical pathway. A stronger novelty claim would require independent replication across cohorts, cell-composition adjustment, comparison with published co-expression modules, and direct experimental testing of the inferred relationships.

**Hypothesis.** Hypothesis: the shared cervix-liver module reflects a cell-state or sample-composition program in which epithelial structural activity and vesicle trafficking co-vary with stress-linked proteostasis and apoptotic readiness. In this model, KRT19 and S100A10 mark the epithelial and membrane-trafficking component, CLIC1 and PSMF1 represent intracellular transport or protein-homeostasis components, and CASP3 occupies a central position associated with apoptotic regulation. An alternative explanation is that epithelial signals are combined with platelet or other blood-associated signals in the samples. This hypothesis is not established by the enrichment analysis, because no GO or KEGG term passed global correction, and it should be tested with cell-type deconvolution, independent replication, and perturbation experiments.

### Important genes

#### CASP3

- **Related proteins** (co-abundance neighbors): KRT19 (0.89), CLIC1 (0.83), PSMF1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caspase 3. The protein encoded by this gene is a cysteine-aspartic acid protease that plays a central role in the execution-phase of cell apoptosis. The encoded protein cleaves and inactivates poly(ADP-ribose) polymerase while it cleaves and activates sterol regulatory element binding proteins as well as caspases 6, 7, and 9. This protein itself is processed by caspases 8, 9, and 10. It is the predominant ca…
- **Diseases (Open Targets)**: neurodegenerative disease (0.537); Kawasaki disease (0.455); response to vaccine (0.422); response to water (0.315); response to stimulus (0.290)
- **Europe PMC papers**: 51611
- **Why important**: CASP3 is the most connected gene in the module and links the apoptosis-related component to KRT19, CLIC1, and PSMF1. Its established function is as a cysteine-aspartic acid protease central to execution-phase apoptosis, with additional roles in proteolytic processing and cytokine regulation. It is also the most extensively studied gene in the module and has broad disease and response associations in the supplied resources.
- **Conclusion**: Established evidence supports CASP3 as the central apoptotic regulator represented in the module. The hypothesis that its central network position marks coordinated apoptotic readiness or cellular stress is plausible, but co-abundance alone does not demonstrate CASP3 activation or causality.

#### KRT19

- **Related proteins** (co-abundance neighbors): CASP3 (0.89), S100A10 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 19. The protein encoded by this gene is a member of the keratin family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. The type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains. Unlike its related family members, this smallest known ac…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.134); neoplasm (0.119); hereditary breast ovarian cancer syndrome (0.118); breast carcinoma (0.118); thyroid gland papillary carcinoma (0.117)
- **Europe PMC papers**: 6566
- **Why important**: KRT19 connects the central CASP3 branch to S100A10 and is the clearest epithelial structural marker in the module. Its established function is as a keratin intermediate-filament protein involved in epithelial structural integrity, epithelial morphogenesis, and differentiation. HPA detects it in both relevant tissues and annotates it as tissue-enhanced in multiple epithelial sites, while it is not detected in immune cells. It also has substantial literature and disease-association coverage.
- **Conclusion**: Established evidence supports KRT19 as an epithelial identity and structural component. Its presence makes a shared epithelial or epithelial-containing cell-state explanation credible. It does not establish that KRT19 mechanistically regulates the other module genes.

#### CLIC1

- **Related proteins** (co-abundance neighbors): CASP3 (0.83), PSMF1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CLIC family member 1. Chloride channels are a diverse group of proteins that regulate fundamental cellular processes including stabilization of cell membrane potential, transepithelial transport, maintenance of intracellular pH, and regulation of cell volume. Chloride intracellular channel 1  is a member of the p64 family; the protein localizes principally to the cell nucleus and exhibits both nuclear and plasma membra…
- **Diseases (Open Targets)**: spermatogenic failure 74 (0.333); neoplasm (0.115); glioblastoma (0.114); gastric cancer (0.102); central nervous system cancer (0.099)
- **Europe PMC papers**: 4339
- **Why important**: CLIC1 is connected to CASP3 and PSMF1, placing it within the module's intracellular transport and protein-homeostasis branch. Its established annotations include chloride transport, signal transduction, platelet aggregation, and cellular oxidant detoxification. HPA places it in cytosol and identifies associations with basal and suprabasal keratinocytes, dendritic cells, megakaryocytes, and platelets. It has a substantial literature and disease-association record.
- **Conclusion**: Established evidence supports CLIC1 as a multifunctional intracellular transport and redox-associated protein with epithelial and blood-cell relevance. Its module position supports a possible link between cellular stress, transport, and apoptosis, but that link remains a hypothesis rather than a demonstrated mechanism.

#### PSMF1

- **Related proteins** (co-abundance neighbors): CLIC1 (0.82), CASP3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proteasome inhibitor subunit 1. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: complex neurodevelopmental disorder with motor features (0.399); placental abruption (0.318); methicillin-resistant staphylococcus aureus infectious disease (0.308); jaw disease (0.209); neurodegenerative disease (0.188)
- **Europe PMC papers**: 411
- **Why important**: PSMF1 is connected to both CASP3 and CLIC1 and represents the module's most direct protein-degradation or proteostasis annotation. Its established function is regulation of proteasome-mediated ubiquitin-dependent protein catabolism. HPA detects it in both relevant tissues and describes low tissue and immune specificity. Compared with the other selected genes, it has a smaller literature base, making its appearance in the module potentially informative for a less well-characterized proteostasis connection.
- **Conclusion**: Established evidence supports PSMF1 as a proteasome-regulatory component. Its co-abundance with CASP3 and CLIC1 is compatible with coordinated protein-quality control during stress, but the module does not establish that PSMF1 controls apoptosis or chloride transport.

#### S100A10

- **Related proteins** (co-abundance neighbors): KRT19 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: S100 calcium binding protein A10. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: actinic keratosis (0.208); neurodegenerative disease (0.184); diverticular disease (0.183); neoplasm (0.115); hepatocellular carcinoma (0.111)
- **Europe PMC papers**: 10215
- **Why important**: S100A10 is a terminal module node connected to KRT19 and provides a membrane-trafficking and calcium-binding-associated component. Its established annotations include membrane-raft assembly, vesicle budding, positive regulation of plasminogen activation, positive regulation of exocytosis, and regulation of GTPase activity. HPA annotates it as tissue-enhanced in esophagus and enriched in esophageal apical cells, with detection in both relevant tissues. It is also extensively studied and has disease associations including hepatocellular carcinoma.
- **Conclusion**: Established evidence supports S100A10 as a vesicle, exocytosis, and membrane-organization factor associated with epithelial biology. Its connection to KRT19 supports an epithelial trafficking interpretation of part of the module, while any functional connection to CASP3 or the proteostasis branch remains hypothetical.

## Module 15

**Tissue pair**: cervix_uterine and liver  
**Genes (5)**: CACYBP, FKBP3, GCLM, SNRPA1, VAMP8

### Function

The module does not support a statistically established GO or KEGG functional enrichment: no GO/KEGG term passed global correction. Its gene annotations nevertheless suggest a composite intracellular maintenance program involving glutathione production and oxidative-stress responses through GCLM, vesicle fusion and autophagy-related trafficking through VAMP8, ubiquitin-associated protein handling and possible beta-catenin degradation through CACYBP, protein-folding and trafficking regulation through FKBP3, and pre-mRNA splicing through SNRPA1. The network topology is sparse, with CACYBP acting as the central connector and GCLM linking to VAMP8. Thus, the most defensible interpretation is coordinated cellular proteostasis, redox maintenance, vesicle trafficking, and RNA-processing activity rather than a single demonstrated pathway.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. The HPA summary reports no secreted genes and low immune-cell specificity for every member. All members are detected at the protein level in both cervix_uterine and liver, supporting biological presence in both tissues rather than a protein-detection artifact. The composition is mixed: CACYBP, VAMP8, and SNRPA1 have low tissue specificity, whereas GCLM is liver-enhanced and FKBP3 is enhanced in skeletal muscle and tongue. Every gene has some cell-type enhancement, including trophoblast populations for several genes and specialized cell types for individual genes. These patterns may reflect shared cellular states or cell-type composition, but the available HPA evidence does not specifically support a blood-contamination explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair reaches the supplied high-confidence STRING interaction threshold, and STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. Therefore, the co-abundance relationships are not corroborated here as established physical interactions or as a known multi-member protein complex. The absence of STRING and hu.MAP support does not exclude indirect regulation, transient interactions, tissue-specific interactions, or coordinated expression without physical binding. The strongest network-level observation is instead the co-abundance topology itself, especially the central position of CACYBP and the GCLM-VAMP8 connection.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may represent a previously unreported cross-tissue co-abundance pattern, because the supplied databases do not identify a shared known interaction, complex, or enriched functional term. However, it cannot be called a definitively new biological module on that basis alone. Database absence is not proof of novelty, and the sparse network, lack of globally significant enrichment, and mixed gene functions weaken a strong claim of a novel coherent mechanism. The appropriate conclusion is that the cross-tissue co-abundance association is a candidate observation requiring replication, comparison with independent cohorts, and testing against cellular-composition and technical confounders.

**Hypothesis.** Hypothesis: in both cervix_uterine and liver, a shared cellular state may coordinate redox buffering through GCLM with membrane and autophagic vesicle trafficking through VAMP8, while CACYBP connects this state to ubiquitin-dependent protein handling and possibly beta-catenin turnover. FKBP3 and SNRPA1 may represent accompanying protein-folding, transcriptional, or RNA-processing requirements. This model predicts that the module will track oxidative or nutrient stress and altered intracellular trafficking more strongly than a tissue-specific secretory or immune program. The model is provisional because the module has no globally significant GO/KEGG enrichment, no high-confidence STRING edges, and no hu.MAP-supported complex.

### Important genes

#### CACYBP

- **Related proteins** (co-abundance neighbors): GCLM (0.85), FKBP3 (0.82), SNRPA1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcyclin binding protein. The protein encoded by this gene is a calcyclin binding protein. It may be involved in calcium-dependent ubiquitination and subsequent proteosomal degradation of target proteins. It probably serves as a molecular bridge in ubiquitin E3 complexes and participates in the ubiquitin-mediated degradation of beta-catenin. Two alternatively spliced transcript variants encoding different isoforms have bee…
- **Diseases (Open Targets)**: esophageal disorder (0.358); gastroesophageal reflux disease (0.291); Abnormality of the skeletal system (0.262); mood disorder (0.202); major depressive disorder (0.202)
- **Europe PMC papers**: 835
- **Why important**: CACYBP is the network hub, connecting GCLM, FKBP3, and SNRPA1. Its annotation supports a role as a calcyclin-binding protein and possible molecular bridge in ubiquitin E3 complexes, including beta-catenin degradation. It is broadly detected in both tissues, has low tissue specificity, and has substantial literature coverage. Its central network position makes it the best candidate for coordinating otherwise diverse intracellular processes.
- **Conclusion**: Established evidence supports CACYBP as the principal co-abundance connector and as a protein associated with ubiquitin-dependent cellular regulation. The hypothesis that it mechanistically organizes the entire module or couples redox, trafficking, and splicing processes remains untested.

#### GCLM

- **Related proteins** (co-abundance neighbors): CACYBP (0.85), VAMP8 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate-cysteine ligase modifier subunit. Glutamate-cysteine ligase, also known as gamma-glutamylcysteine synthetase, is the first rate limiting enzyme of glutathione synthesis. The enzyme consists of two subunits, a heavy catalytic subunit and a light regulatory subunit. Gamma glutamylcysteine synthetase deficiency has been implicated in some forms of hemolytic anemia. Alternative splicing results in multiple transcript variants encoding…
- **Diseases (Open Targets)**: non-autoimmune hemolytic anemia (0.370); refractive error (0.175); alcohol drinking (0.163); Abnormality of refraction (0.143); device complication (0.096)
- **Europe PMC papers**: 6416
- **Why important**: GCLM connects directly to CACYBP and VAMP8 and encodes the regulatory subunit of glutamate-cysteine ligase, the rate-limiting enzyme system for glutathione synthesis. Its liver-enhanced HPA profile is particularly relevant to the shared liver component, while protein is detected in both tissues. Its annotation links it to glutathione biosynthesis, oxidative-stress responses, nutrient responses, and xenobiotic responses. It also has extensive literature coverage and a disease association involving hemolytic anemia.
- **Conclusion**: Established evidence identifies GCLM as the clearest redox and glutathione-related component of the module. It is plausible, but not demonstrated, that GCLM-mediated redox buffering drives or stabilizes the broader co-abundance pattern.

#### VAMP8

- **Related proteins** (co-abundance neighbors): GCLM (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Plasma membrane; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vesicle associated membrane protein 8. This gene encodes an integral membrane protein that belongs to the synaptobrevin/vesicle-associated membrane protein subfamily of soluble N-ethylmaleimide-sensitive factor attachment protein receptors (SNAREs). The encoded protein is involved in the fusion of synaptic vesicles with the presynaptic membrane.[provided by RefSeq, Jun 2010].
- **Diseases (Open Targets)**: Moderate albuminuria (0.327); coronary artery disorder (0.326); prostate carcinoma (0.304); myocardial infarction (0.276); myocardial ischemia (0.204)
- **Europe PMC papers**: 2696
- **Why important**: VAMP8 forms the module's direct link to GCLM and contributes the most explicit membrane-trafficking interpretation. It is a SNARE-family vesicle-associated membrane protein annotated for vesicle fusion, vesicle-mediated transport, autophagosome membrane docking, and SNARE-complex assembly. It is detected in both tissues and has substantial literature coverage, with disease associations involving albuminuria and cardiovascular disorders.
- **Conclusion**: Established evidence supports VAMP8 as a vesicle-fusion and autophagy-trafficking component that may connect redox state to membrane dynamics. A direct functional partnership between VAMP8 and GCLM is only a hypothesis because the supplied STRING and hu.MAP evidence does not establish such an interaction.

#### FKBP3

- **Related proteins** (co-abundance neighbors): CACYBP (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FKBP prolyl isomerase 3. The protein encoded by this gene is a member of the immunophilin protein family, which play a role in immunoregulation and basic cellular processes involving protein folding and trafficking. This encoded protein is a cis-trans prolyl isomerase that binds the immunosuppressants FK506 and rapamycin, as well as histone deacetylases, the transcription factor YY1, casein kinase II, and nucleolin. It ha…
- **Diseases (Open Targets)**: chronic pancreatitis (0.178); lung adenocarcinoma (0.094); non-small cell lung carcinoma (0.075); colorectal carcinoma (0.075); diffuse large B-cell lymphoma (0.074)
- **Europe PMC papers**: 344
- **Why important**: FKBP3 is connected to the hub CACYBP and provides a protein-folding, trafficking, and signaling-regulatory dimension through its immunophilin activity and binding to rapamycin, histone deacetylases, YY1, casein kinase II, and nucleolin. Its tissue-enhanced profile in skeletal muscle and tongue shows that it is not simply a liver marker, while detection in both tissues supports the shared-module interpretation. Its literature volume is more limited than that of GCLM or VAMP8, making its role potentially informative but less firmly characterized in this context.
- **Conclusion**: Established evidence supports FKBP3 as an immunophilin involved in protein folding, trafficking, and regulatory protein interactions. Its placement beside CACYBP suggests a possible proteostasis or signaling bridge, but the module does not establish that FKBP3 controls the other members.

#### SNRPA1

- **Related proteins** (co-abundance neighbors): CACYBP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide A'. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); dengue disease (0.370); phosphorus metabolism disease (0.196); hypotensive disorder (0.196); cancer (0.087)
- **Europe PMC papers**: 520
- **Why important**: SNRPA1 is connected to CACYBP and contributes a nuclear RNA-processing component. It encodes a U two-type spliceosomal protein involved in snRNP assembly, pre-spliceosome formation, mRNA splicing, and spermatogenesis. It is detected in both tissues, has low tissue specificity, and has a substantial literature base. Its inclusion emphasizes that the module may represent a broad cellular-state program rather than a single membrane or metabolic pathway.
- **Conclusion**: Established evidence supports SNRPA1 as a spliceosomal and RNA-processing factor. Its co-abundance with CACYBP may reflect coordinated demand for gene-expression and protein-quality control, but a direct mechanistic connection is not demonstrated.

## Module 16

**Tissue pair**: cervix_uterine and liver  
**Genes (5)**: GLUL, KRT10, KRT1, KRT5, TAP1

### Function

The strongest interpretation is an epithelial intermediate-filament and keratinization module. All globally corrected GO evidence is driven by KRT1, KRT10, and KRT5: structural constituent of skin epidermis (GO:MF structural constituent of skin epidermis; q_global = 0.0019), keratin filament (GO:CC keratin filament; q_global = 0.0138), intermediate-filament organization (GO:BP intermediate filament organization; q_global = 0.0221), intermediate-filament-based process (GO:BP intermediate filament-based process; q_global = 0.0327), and intermediate-filament cytoskeleton organization (GO:BP intermediate filament cytoskeleton organization; q_global = 0.0327). The three keratins therefore define the core function. GLUL contributes a glutamine-synthetase and ammonia-detoxification function, while TAP1 contributes antigen processing and peptide transport, but neither gene appears in a globally corrected GO or KEGG term. The STRING disease and functional enrichments support the keratin interpretation but are supplementary evidence only.

**Cell composition.** This is not primarily a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, and the core genes are intracellular structural proteins. Its composition is strongly epithelial and keratinocyte-associated. KRT1, KRT5, and KRT10 are repeatedly associated with skin and suprabasal or basal keratinocytes, with additional cervix, esophagus, and vagina associations. KRT5 is detected in cervix but not liver, KRT1 is detected in cervix but not liver, and KRT10 is not detected in either tissue by the reported IHC observations. GLUL and TAP1 are detected in both tissues and are more broadly distributed. The conserved cervix-liver signal may therefore reflect shared epithelial material, epithelial contamination, or a shared epithelial cell component rather than a liver-specific keratin program. The HPA blood-cell associations are gene-specific and heterogeneous, not evidence that this is chiefly a blood-cell module.

**GO/KEGG enrichment**: 5 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF structural constituent of skin epidermis | 0.0019 | KRT1, KRT10, KRT5 |
| GO:CC keratin filament | 0.0138 | KRT1, KRT10, KRT5 |
| GO:BP intermediate filament organization | 0.0221 | KRT1, KRT10, KRT5 |
| GO:BP intermediate filament-based process | 0.0327 | KRT1, KRT10, KRT5 |
| GO:BP intermediate filament cytoskeleton organization | 0.0327 | KRT1, KRT10, KRT5 |

### STRING and hu.MAP

STRING provides high-confidence pairwise support for the keratin core: KRT1 connects with KRT10 and KRT5, and KRT10 connects with KRT5. These relationships are concordant with known heterotypic keratin filament biology and explain the central placement of KRT5 and KRT1 in the co-abundance subgraph. STRING reports no partner for GLUL or TAP1 within the listed module interactions, so their links to KRT5 should not be interpreted as established physical complexes. No hu.MAP complex contains at least two module members. Thus, the network contains a well-supported known keratin subnetwork plus weaker or potentially context-dependent associations involving GLUL and TAP1.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: KRT1–KRT10 (0.999); KRT1–KRT5 (0.923); KRT10–KRT5 (0.793)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Cell type benign neoplasm (FDR = 0.00042, 4 genes); DISEASES Acanthoma (FDR = 0.00065, 3 genes); Function Structural constituent of skin epidermis (FDR = 0.0041, 3 genes); HPO Erythema (FDR = 0.0052, 4 genes); SMART Intermediate filament protein (FDR = 0.0055, 3 genes); Keyword Intermediate filament (FDR = 0.0072, 3 genes); Keyword Keratin (FDR = 0.0072, 3 genes); Component Keratin filament (FDR = 0.0081, 3 genes); COMPARTMENTS Keratin filament (FDR = 0.0083, 3 genes); NetworkNeighborAL Formation of the cornified envelope, and Serpin, conserved site (FDR = 0.0152, 3 genes); DISEASES Epidermolytic acanthoma (FDR = 0.0155, 2 genes); DISEASES Organ system benign neoplasm (FDR = 0.0196, 3 genes); DISEASES Bullous congenital ichthyosiform erythroderma (FDR = 0.0196, 2 genes); DISEASES Basal cell carcinoma (FDR = 0.0196, 2 genes); DISEASES Epidermolytic hyperkeratosis (FDR = 0.0196, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The keratin biology itself is not a new finding: the KRT1-KRT5-KRT10 relationships, epidermal structural function, keratinocyte expression, and keratin-associated disorders are well established in the fact sheet. The potentially novel observation is the conserved co-abundance of this keratin core with GLUL and TAP1 across cervix and liver in this dataset. However, the evidence does not establish a new physical complex or a new molecular pathway: hu.MAP has no supported complex, and STRING lacks listed interactions for GLUL and TAP1. Therefore this should be described as a dataset-specific conserved co-abundance pattern built around a known keratin program, not as a demonstrated new biological complex.

**Hypothesis.** Hypothesis: the module reflects coordinated abundance of epithelial structural proteins with cellular stress, metabolic, and immune-interface programs. KRT5 may mark the epithelial basal component and provide the network link to GLUL and TAP1; KRT1 and KRT10 may represent the differentiating or suprabasal keratin program. In cervix and liver samples, shared epithelial content or epithelial injury could produce co-abundance of these keratins, while GLUL could reflect local ammonia and glutamate handling and TAP1 could reflect antigen-processing activity. This is a mechanistic model for the co-abundance pattern, not proof that GLUL or TAP1 physically interact with the keratin filaments.

### Important genes

#### KRT5

- **Related proteins** (co-abundance neighbors): KRT1 (0.89), GLUL (0.82), TAP1 (0.80); STRING partners: KRT1 (0.923), KRT10 (0.793)
- **HPA**: Group enriched; Group enriched; blood Immune cell enriched; location Intermediate filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 5. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the basal layer of the epidermis with family member KRT14. Mutations in t…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 2C, localized (0.768); epidermolysis bullosa simplex 2A, generalized severe (0.761); epidermolysis bullosa simplex 2B, generalized intermediate (0.761); epidermolysis bullosa simplex 2F, with mottled pigmentation (0.729); Dowling-Degos disease 1 (0.697)
- **Europe PMC papers**: 7044
- **Why important**: KRT5 is the most connected module gene and links the keratin core to GLUL and TAP1. It is present in every globally corrected GO term (5 globally significant GO/KEGG terms, q_global 0.0019–0.0327; see the table), is associated with basal and suprabasal keratinocytes, and has extensive disease and literature support involving epidermolysis bullosa simplex and epithelial structural biology. Its cervix detection and lack of liver detection are also important for interpreting the tissue-pair signal.
- **Conclusion**: Established evidence supports KRT5 as a central basal-epithelial intermediate-filament gene and the principal network connector. It is plausible, but not established, that KRT5 is the transcript-level bridge linking the keratin program to GLUL and TAP1 in this shared module.

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT5 (0.89), KRT10 (0.89); STRING partners: KRT10 (0.999), KRT5 (0.923)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a core member of all globally corrected GO terms (5 globally significant GO/KEGG terms, q_global 0.0019–0.0327; see the table) and connects directly to both KRT5 and KRT10. HPA associates it with skin and suprabasal keratinocytes, while the gene information links it to keratinization, intermediate-filament organization, and multiple keratin disorders. It also has extensive disease and literature support.
- **Conclusion**: Established evidence identifies KRT1 as a principal structural and differentiating keratin in the module. Its network position and annotations support a central role in epithelial cytoskeletal organization, but they do not show that KRT1 drives the cross-tissue co-abundance pattern.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT1 (0.89); STRING partners: KRT1 (0.999), KRT5 (0.793)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is part of every globally corrected GO term (5 globally significant GO/KEGG terms, q_global 0.0019–0.0327; see the table) and has a very strong STRING relationship with KRT1, as well as a reported relationship with KRT5. It is associated with suprabasal keratinocytes, keratinocyte differentiation, cornification, and epidermolytic hyperkeratosis. Its literature base is substantial, although less extensive than that of KRT1 or KRT5 in the supplied evidence.
- **Conclusion**: Established evidence supports KRT10 as the differentiating or suprabasal component of the keratin filament program. Its absence from the reported IHC detection in both tissues makes it especially important to treat the module signal as an abundance or sample-composition pattern rather than direct proof of widespread tissue protein expression.

#### GLUL

- **Related proteins** (co-abundance neighbors): KRT5 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enhanced; location Mitochondria, Cytosol; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamate-ammonia ligase. The protein encoded by this gene belongs to the glutamine synthetase family. It catalyzes the synthesis of glutamine from glutamate and ammonia in an ATP-dependent reaction. This protein plays a role in ammonia and glutamate detoxification, acid-base homeostasis, cell signaling, and cell proliferation. Glutamine is an abundant amino acid, and is important to the biosynthesis of several amino acids…
- **Diseases (Open Targets)**: congenital brain dysgenesis due to glutamine synthetase deficiency (0.791); developmental and epileptic encephalopathy 116 (0.668); neurodegenerative disease (0.525); hereditary disease (0.190); genetic developmental and epileptic encephalopathy (0.185)
- **Europe PMC papers**: 4047
- **Why important**: GLUL is the only non-keratin gene connected to KRT5 in the module graph and is detected in both cervix and liver. It encodes glutamate-ammonia ligase, supporting glutamine synthesis, ammonia and glutamate detoxification, acid-base homeostasis, and proliferation. It has disease associations involving congenital glutamine-synthetase deficiency and a substantial literature base. STRING supplementary terms connect it to the keratin-associated module context, but GLUL is absent from the globally corrected GO terms.
- **Conclusion**: Established evidence supports GLUL as a broadly relevant metabolic gene that may explain the liver-compatible portion of the module. Its connection to the keratin program is a co-abundance association rather than an established physical interaction; a shared cell state, epithelial stress response, or sample-composition effect remains a hypothesis.

#### TAP1

- **Related proteins** (co-abundance neighbors): KRT5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Centriolar satellite; IHC detected in cervix_uterine, liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transporter 1, ATP binding cassette subfamily B member. The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily ar…
- **Diseases (Open Targets)**: MHC class I deficiency (0.760); MHC class II deficiency (0.371); autoimmune disorder of central nervous system (0.357); neurodegenerative disease (0.240); hereditary disease (0.193)
- **Europe PMC papers**: 7090
- **Why important**: TAP1 is connected to KRT5 and is detected in both tissues. Its established function is ATP-dependent transport associated with cytosol-to-endoplasmic-reticulum peptide transport and antigen processing for MHC class I presentation. It has disease associations involving MHC deficiency and a substantial literature base. It has no globally corrected GO term, no listed STRING functional enrichment, and no listed STRING partner within this module.
- **Conclusion**: Established evidence supports TAP1 as an antigen-processing and peptide-transport gene that may report immune or epithelial interface activity. The link to KRT5 is currently only a module co-abundance relationship, so an immune-epithelial mechanism is plausible but not demonstrated.
