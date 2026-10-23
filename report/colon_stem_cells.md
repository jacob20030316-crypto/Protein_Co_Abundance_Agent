# Conserved co-abundance modules: colon and stem_cells

## Module 0

**Tissue pair**: colon and stem_cells  
**Genes (29)**: PRKAB1, AFG2A, ASAP1, ARFGEF3, CNOT4, DESI2, EVL, FKBP7, FMNL3, H2BC26, F8A1, ISG15, MTARC1, MEN1, IGF2R, NCK1, NHEJ1, PANK4, MRPL10, MRPL30, GFM2, STK11IP, SCAF11, SPART, TSPAN6, EFTUD2, UFD1, ZC3H7A, SLC30A1

### Function

The module does not have a statistically supported GO or KEGG functional label: no GO/KEGG term passed global correction. Its structure is sparse and organized around two co-abundance neighborhoods, with DESI2 and FMNL3 acting as the principal network hubs. The annotations point to several connected cellular themes rather than one established pathway: protein deubiquitination and RNA regulation around DESI2, cytoskeletal organization and vesicle-associated signaling around FMNL3, and mitochondrial translation around GFM2, MRPL10, and MRPL30. Additional genes support chromatin regulation, DNA repair, membrane trafficking, nutrient sensing, zinc transport, and interferon-related biology. These annotations support a cautious interpretation as a cellular maintenance or state-associated module involving proteostasis, trafficking, and mitochondrial capacity, but they do not establish a single pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only a small minority of genes are secreted, and ISG15 is the clear example of a protein secreted to blood. Most genes have low tissue specificity, consistent with broadly expressed cellular machinery rather than a tissue-restricted program. HPA evidence does show a mixed cell-type signal, including neutrophils, eosinophils, plasmacytoid dendritic cells, basophils, colon epithelial populations, and several neuronal or reproductive cell types. Therefore, shared co-abundance could partly reflect common cell populations or sample composition, including an immune contribution, but the evidence does not support calling this primarily a blood module. Protein detection is reported for most annotated genes in colon, whereas there is no matching HPA tissue for the stem-cell group.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no supplementary functional enrichment. Its high-confidence physical-interaction evidence is concentrated in the mitochondrial translation neighborhood: GFM2 interacts with MRPL10 and MRPL30, and MRPL10 interacts strongly with MRPL30. hu.MAP independently places these same genes in a shared complex, (hu.MAP huMAP3_06589.1), while MRPL10 and MRPL30 recur together across the additional hu.MAP complexes (hu.MAP huMAP3_03763.1) through (hu.MAP huMAP3_09483.1). This convergence means that the mitochondrial submodule contains relationships already supported by external interaction and complex resources. In contrast, the DESI2 and FMNL3 hub connections, and most cross-functional edges in the co-abundance graph, are not represented by STRING or hu.MAP in the supplied evidence. Thus, the network combines a known mitochondrial complex fragment with largely unvalidated co-abundance relationships.

**STRING interactions (score >= 0.7)**: 3 of 406 gene pairs: GFM2–MRPL10 (0.814); GFM2–MRPL30 (0.818); MRPL10–MRPL30 (0.977)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06589.1 (MRPL10, MRPL30, GFM2; 3/79); huMAP3_03763.1 (MRPL10, MRPL30; 2/26); huMAP3_01856.1 (MRPL10, MRPL30; 2/31); huMAP3_06439.1 (MRPL10, MRPL30; 2/57); huMAP3_06550.1 (MRPL10, MRPL30; 2/62); huMAP3_07939.1 (MRPL10, MRPL30; 2/68); huMAP3_08458.1 (MRPL10, MRPL30; 2/70); huMAP3_09113.1 (MRPL10, MRPL30; 2/72); huMAP3_09483.1 (MRPL10, MRPL30; 2/74)

### Novelty

The module should not be described as a wholly new molecular complex or as a newly discovered pathway. The GFM2, MRPL10, and MRPL30 relationships are already supported by STRING and hu.MAP, and the functions of many individual genes are well established. A potentially novel aspect is the reproducible co-abundance organization shared by colon and stem_cells, especially the placement of DESI2 and FMNL3 as central connectors to genes involved in different cellular systems. However, database absence for most edges is not proof of novelty. Establishing a new finding would require replication across cohorts, control for cell composition, and experimental or orthogonal confirmation of the non-database-supported relationships.

**Hypothesis.** Hypothesis: this shared module reflects a cellular state in which epithelial or progenitor-associated cells coordinate proteostasis and RNA handling with cytoskeletal or vesicle remodeling, while maintaining mitochondrial protein-synthesis capacity. DESI2 may mark the proteostasis and post-translational-regulation arm, FMNL3 may mark the actin and trafficking arm, and the GFM2–MRPL10–MRPL30 group may represent a mitochondrial translation arm. Immune-associated genes and the ISG15 signal could indicate a contribution from inflammatory or mixed-cell states rather than a core function of every cell. This is a mechanistic proposal, not an enriched-pathway conclusion; it should be tested by cell-resolved expression, mitochondrial translation measurements, perturbation of DESI2 or FMNL3, and replication in independent colon and stem-cell datasets.

### Important genes

#### DESI2

- **Related proteins** (co-abundance neighbors): AFG2A (0.87), ZC3H7A (0.87), UFD1 (0.86), CNOT4 (0.86), SCAF11 (0.85), GFM2 (0.85), STK11IP (0.84), IGF2R (0.83), EFTUD2 (0.80), ISG15 (0.80), SLC30A1 (0.80), MRPL10 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: desumoylating isopeptidase 2. Enables Lys48-specific deubiquitinase activity; Lys63-specific deubiquitinase activity; and thiol-dependent deubiquitinase. Predicted to be involved in protein deubiquitination. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: brain disorder (0.199); digestive system disorder (0.192); response to antihypertensive drug (0.167); cancer (0.077); complex regional pain syndrome (0.061)
- **Europe PMC papers**: 135
- **Why important**: DESI2 is the most connected node in the supplied module graph and links genes involved in ubiquitin-dependent proteostasis, RNA processing, mitochondrial translation, signaling, and trafficking. Its annotated deubiquitinase activities and predicted role in macromolecule depalmitoylation provide a plausible regulatory bridge across these otherwise diverse processes. It has substantial literature support and disease associations spanning brain and digestive-system disorders, although it has no STRING or hu.MAP relationship in this module.
- **Conclusion**: Established evidence supports DESI2 as a proteostasis-related enzyme and as the central statistical connector of the module. It is plausible, but unproven, that DESI2 coordinates the other module neighborhoods; the co-abundance graph alone does not demonstrate physical interaction or causal control.

#### FMNL3

- **Related proteins** (co-abundance neighbors): NHEJ1 (0.88), ARFGEF3 (0.86), EVL (0.84), PANK4 (0.83), MRPL30 (0.83), ZC3H7A (0.83), NCK1 (0.83), PRKAB1 (0.81), F8A1; F8A2; F8A3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Golgi apparatus, Vesicles, Plasma membrane; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: formin like 3. The protein encoded by this gene contains a formin homology 2 domain and has high sequence identity to the mouse Wbp3 protein. Two alternative transcripts encoding different isoforms have been described. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: alcohol drinking (0.233); colorectal carcinoma (0.086); nicotine dependence (0.084); nasopharyngeal carcinoma (0.079); pancreatic adenocarcinoma (0.074)
- **Europe PMC papers**: 457
- **Why important**: FMNL3 is the second prominent network hub and connects the module to NHEJ1, ARFGEF3, EVL, PANK4, MRPL30, ZC3H7A, NCK1, and PRKAB1. Its established annotations involve actin organization, cell migration, morphogenesis, and filopodium assembly, which are relevant to epithelial architecture and progenitor-cell behavior. HPA detects it in colon and associates it with microglia and plasmacytoid dendritic cells; its literature and colorectal-carcinoma association further increase its biological relevance.
- **Conclusion**: Established evidence supports FMNL3 as an actin and cell-migration regulator with colon relevance. Its position suggests a possible role in the module's structural or trafficking arm, but the link to mitochondrial and RNA-related genes remains a hypothesis because neither STRING nor hu.MAP supports those specific module edges.

#### GFM2

- **Related proteins** (co-abundance neighbors): DESI2 (0.85); STRING partners: MRPL10 (0.814), MRPL30 (0.818)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_06589.1
- **Function (MyGene.info)**: GTP dependent ribosome recycling factor mitochondrial 2. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: combined oxidative phosphorylation deficiency (0.727); mitochondrial disease (0.456); Leigh syndrome (0.216); hereditary disease (0.193); Alzheimer disease (0.191)
- **Europe PMC papers**: 185
- **Why important**: GFM2 is the mitochondrial translation factor in the module and is part of the externally supported mitochondrial interaction cluster with MRPL10 and MRPL30. STRING supports its relationships with both partners, and hu.MAP places all three in (hu.MAP huMAP3_06589.1). Its established function in mitochondrial ribosome recycling, elongation, and termination, together with disease associations involving oxidative-phosphorylation deficiency and mitochondrial disease, gives this small submodule clear mechanistic significance.
- **Conclusion**: Established evidence supports GFM2 as a component of mitochondrial protein synthesis and validates its relationships with MRPL10 and MRPL30. Its role as a driver of the whole co-abundance module is not established; it may instead report mitochondrial capacity within a broader cellular state.

#### MRPL10

- **Related proteins** (co-abundance neighbors): DESI2 (0.80); STRING partners: GFM2 (0.814), MRPL30 (0.977)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_06589.1, huMAP3_03763.1, huMAP3_01856.1, huMAP3_06439.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L10. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.532); Alzheimer disease (0.270); Parkinson disease (0.268); lysosomal storage disease (0.268); atrial fibrillation (0.079)
- **Europe PMC papers**: 327
- **Why important**: MRPL10 is one of the two mitochondrial large-subunit proteins in the strongly supported mitochondrial cluster. It is connected to GFM2 and MRPL30 in STRING and recurs with MRPL30 across the hu.MAP complexes (hu.MAP huMAP3_06589.1) through (hu.MAP huMAP3_09483.1). Its annotated role in mitochondrial translation and its disease links to neurodegenerative and lysosomal disorders make it a useful marker of mitochondrial protein-synthesis demand, despite its limited direct connectivity in the co-abundance graph.
- **Conclusion**: Established evidence supports MRPL10 as a mitochondrial ribosomal protein embedded in known complexes. Its module association is therefore biologically credible for the mitochondrial arm, but it does not by itself establish a colon- or stem-cell-specific mechanism.

#### MRPL30

- **Related proteins** (co-abundance neighbors): FMNL3 (0.83); STRING partners: GFM2 (0.818), MRPL10 (0.977)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06589.1, huMAP3_03763.1, huMAP3_01856.1, huMAP3_06439.1, huMAP3_06550.1, huMAP3_07939.1, huMAP3_08458.1, huMAP3_09113.1, huMAP3_09483.1
- **Function (MyGene.info)**: mitochondrial ribosomal protein L30. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); liver disorder (0.300); device complication (0.171); male reproductive organ cancer (0.036); corneal ulcer (0.025)
- **Europe PMC papers**: 211
- **Why important**: MRPL30 has the strongest supplied STRING relationship, with MRPL10, and participates with MRPL10 in every listed hu.MAP complex containing module members. Its established role in mitochondrial translation gives independent support to the mitochondrial interpretation. Its co-abundance connection to FMNL3 is especially notable because it may link mitochondrial protein synthesis with cytoskeletal or epithelial-state biology, although that cross-system relationship is not externally validated here.
- **Conclusion**: Established evidence supports MRPL30 as part of a known mitochondrial ribosomal complex. The FMNL3–MRPL30 association is a hypothesis-generating co-abundance observation rather than a demonstrated molecular interaction.

#### MEN1

- **Related proteins** (co-abundance neighbors): H2BC26 (0.85), SPART (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: menin 1. This gene encodes menin, a tumor suppressor associated with a syndrome known as multiple endocrine neoplasia type 1. Menin is a scaffold protein that functions in histone modification and epigenetic gene regulation. It is thought to regulate several pathways and processes by altering chromatin structure through the modification of histones. [provided by RefSeq, May 2019].
- **Diseases (Open Targets)**: multiple endocrine neoplasia type 1 (0.866); parathyroid gland adenoma (0.675); endocrine gland neoplasm (0.663); multiple endocrine neoplasia (0.661); Angiofibroma (0.642)
- **Europe PMC papers**: 7686
- **Why important**: MEN1 is a well-studied chromatin and transcriptional regulator with the strongest literature volume among the selected genes and a well-established tumor-suppressor association with multiple endocrine neoplasia. It connects in the module to H2BC26 and SPART, thereby occupying a branch that combines chromatin biology with mitochondrial and trafficking signals. Its annotations include histone modification, epigenetic regulation, DNA repair, and transcriptional control, all relevant to proliferating or stem-like cellular states.
- **Conclusion**: Established evidence supports MEN1 as an epigenetic scaffold and tumor suppressor. Its presence may indicate a proliferation or chromatin-regulatory component, but the module does not provide enough evidence to assign MEN1 a causal role or to infer a MEN1-specific disease mechanism in colon or stem_cells.

## Module 1

**Tissue pair**: colon and stem_cells  
**Genes (20)**: CCN1, CENPK, CENPV, DNMT3A, FHIP1A, FKBP9, GMEB1, GTPBP3, MARK3, NECTIN2, NUDT16, OSGEPL1, PCLAF, PEX26, RNF185, POLR2E, RYBP, WDR89, ZNF280C, ZNF143

### Function

The module does not support a single statistically established GO or KEGG function: no GO/KEGG term passed global correction, and STRING functional enrichment was absent. Its gene content instead suggests a mixed cellular program involving mitochondrial RNA modification and metabolism, transcriptional and epigenetic regulation, chromosome segregation and cell-cycle control, intracellular protein handling, and extracellular adhesion or signaling. The network is centered on OSGEPL1, with links to genes involved in mitochondrial tRNA modification, transcriptional regulation, chromatin regulation, peroxisomal import, cell division, and extracellular-matrix signaling. This interpretation is functional and hypothesis-generating rather than pathway enrichment evidence.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only a small subset is secreted or extracellular, including CCN1, while most members are intracellular proteins. Most genes have low tissue specificity, and many have broad or enhanced cell-type patterns rather than a coherent tissue-restricted signature. HPA shows protein detection for most genes in colon, whereas there is no matching HPA tissue for stem_cells. Several members show enrichment or enhancement in blood-related cells, including eosinophils, neutrophils, monocytes, dendritic cells, memory B cells, and T-reg cells, while others are associated with bone marrow and lymphoid tissue. Therefore, the shared module could partly reflect common epithelial, proliferative, stromal, or immune-cell contributions in the samples rather than a colon-and-stem-cell-specific biochemical complex. The limited secreted component argues against a predominantly circulating plasma-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module met the stated high-confidence STRING interaction threshold, and no STRING functional enrichment was reported. No hu.MAP complex contained multiple module members. The co-abundance links therefore represent coordinated abundance patterns that are not corroborated here by curated high-confidence physical interactions or known protein complexes. This does not invalidate the module: co-abundance can arise from shared cell composition, shared regulation, parallel stress or differentiation states, or indirect biological coupling. It does mean that a direct physical complex interpretation is unsupported.

**STRING interactions (score >= 0.7)**: 0 of 190 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a new co-abundance observation, but novelty is not established solely by the absence of STRING interactions or hu.MAP complexes. The evidence for novelty is that the particular cross-tissue co-abundance grouping is not represented as a known high-confidence interaction network or multi-member hu.MAP complex in the supplied data. Against a strong novelty claim, many component genes have established functions and substantial literature, and the module contains broadly expressed and cell-type-associated genes that could be brought together by sample composition or common regulation. The appropriate conclusion is that the coordinated abundance pattern is potentially novel, while its biological mechanism requires independent replication and validation.

**Hypothesis.** Hypothesis: the module reflects a shared proliferative or differentiation state in colon and stem-cell samples, coupled to cellular stress and proteostasis. In this model, OSGEPL1 links mitochondrial RNA-modification biology to a broader transcriptional and cellular-maintenance program; DNMT3A and transcriptional regulators influence cell-state programs; CENPK, CENPV, and PCLAF mark chromosome, centrosome, and replication-associated activity; and CCN1 contributes an extracellular adhesion or vascular-stromal signal. The blood-cell and developmental cell-type patterns in HPA raise an alternative explanation that the module partly reflects changing proportions of immune, stromal, or progenitor-like cells. This hypothesis should be tested with cell-resolved expression, independent cohorts, perturbation of candidate regulators, and assays distinguishing direct molecular coupling from compositional correlation.

### Important genes

#### OSGEPL1

- **Related proteins** (co-abundance neighbors): ZNF280C (0.91), WDR89 (0.87), GMEB1 (0.87), CCN1 (0.86), GTPBP3 (0.84), RYBP (0.84), POLR2E (0.83), PEX26 (0.82), FKBP9 (0.81), NECTIN2 (0.81), CENPK (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: O-sialoglycoprotein endopeptidase like 1. Predicted to enable N(6)-L-threonylcarbamoyladenine synthase activity and metal ion binding activity. Predicted to be involved in tRNA threonylcarbamoyladenosine modification. Located in mitochondrion. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.333); hepatocellular carcinoma (0.074); glomerulonephritis (0.048); metabolic disease (0.047); osteoarthritis, hip (0.035)
- **Europe PMC papers**: 192
- **Why important**: OSGEPL1 is the principal network hub by weighted degree and connects genes spanning mitochondrial biology, transcriptional regulation, protein handling, and cell-state control. HPA places it in mitochondria with low tissue specificity and enhanced signal in several cell types. Its predicted role in mitochondrial tRNA threonylcarbamoyladenosine modification provides a plausible link to mitochondrial translation and cellular energy state. It also has a substantial literature and disease associations involving neurodegenerative, metabolic, hepatic, renal, and skeletal conditions.
- **Conclusion**: Established evidence supports OSGEPL1 as the network center and as a mitochondrial tRNA-modification gene. It is a strong marker of the module's coordinated state, but the data do not establish that it physically interacts with its module neighbors or causally drives the module. Its role as a mechanistic organizer remains a hypothesis.

#### CCN1

- **Related proteins** (co-abundance neighbors): FHIP1A (0.90), NUDT16 (0.89), DNMT3A (0.88), OSGEPL1 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cellular communication network factor 1. The secreted protein encoded by this gene is growth factor-inducible and promotes the adhesion of endothelial cells. The encoded protein interacts with several integrins and with heparan sulfate proteoglycan. This protein also plays a role in cell proliferation, differentiation, angiogenesis, apoptosis, and extracellular matrix formation. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.575); vein disorder (0.338); lymphatic system disorder (0.338); myalgic encephalomeyelitis/chronic fatigue syndrome (0.260); glomerulonephritis (0.253)
- **Europe PMC papers**: 14168
- **Why important**: CCN1 is the clearest extracellular and signaling component. It has the second strongest network position among the highlighted genes, is tissue-enhanced in blood vessel, is secreted to the extracellular matrix, and is detected in colon. Its established functions include endothelial adhesion, integrin-mediated signaling, migration, angiogenesis, proliferation, differentiation, apoptosis, and extracellular-matrix formation. It also has a very large literature and associations with skeletal, venous, lymphatic, renal, and inflammatory-related disorders.
- **Conclusion**: Established evidence supports CCN1 as an extracellular-matrix and cell-communication factor that could connect tissue architecture to the intracellular state represented by the module. The co-abundance data do not show that CCN1 directly regulates the other members. Its participation may reflect stromal or vascular composition rather than a shared molecular pathway.

#### DNMT3A

- **Related proteins** (co-abundance neighbors): CCN1 (0.88), ZNF143 (0.83), NUDT16 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA methyltransferase 3 alpha. CpG methylation is an epigenetic modification that is important for embryonic development, imprinting, and X-chromosome inactivation. Studies in mice have demonstrated that DNA methylation is required for mammalian development. This gene encodes a DNA methyltransferase that is thought to function in de novo methylation, rather than maintenance methylation. The protein localizes to the cytoplasm an…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.858); Tatton-Brown-Rahman overgrowth syndrome (0.844); Heyn-Sproul-Jackson syndrome (0.763); myelodysplastic syndrome (0.741); myeloid leukemia (0.682)
- **Europe PMC papers**: 31456
- **Why important**: DNMT3A occupies a connector position between CCN1, ZNF143, and NUDT16. It encodes a de novo DNA methyltransferase involved in developmental methylation and transcriptional repression, and it is associated with acute myeloid leukemia, myelodysplastic disease, and developmental overgrowth syndromes. Its large literature makes it one of the best-established regulatory genes in the module. HPA shows broad tissue distribution with cell-type enhancement in several differentiated or specialized populations.
- **Conclusion**: Established evidence supports DNMT3A as an epigenetic regulator with major roles in development and hematologic disease. In this module it may indicate shared cell-state or differentiation regulation, but the data do not demonstrate that DNMT3A epigenetically controls the other module genes. A causal regulatory role is therefore a hypothesis.

#### CENPK

- **Related proteins** (co-abundance neighbors): PCLAF (0.82), OSGEPL1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: centromere protein K. CENPK is a subunit of a CENPH (MIM 605607)-CENPI (MIM 300065)-associated centromeric complex that targets CENPA (MIM 117139) to centromeres and is required for proper kinetochore function and mitotic progression (Okada et al., 2006 [PubMed 16622420]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); diverticular disease (0.294); Abnormality of the skeletal system (0.247); Incisional hernia (0.231); glomerulonephritis (0.195)
- **Europe PMC papers**: 645
- **Why important**: CENPK connects OSGEPL1-associated structure to PCLAF and is enhanced in bone marrow and lymphoid tissue. It is a subunit of a centromeric complex required for CENPA targeting, kinetochore function, and mitotic progression. Its single-cell associations include differentiating germ-cell populations, erythrocyte progenitors, and extravillous trophoblasts, consistent with proliferative or developmental states. It has established disease associations and a substantial literature.
- **Conclusion**: Established evidence supports CENPK as a chromosome-segregation and kinetochore factor. Its presence may mark proliferating progenitor-like cells shared between the sampled tissues. The module does not establish a direct relationship between CENPK and OSGEPL1 or show that CENPK drives the co-abundance pattern.

#### GTPBP3

- **Related proteins** (co-abundance neighbors): OSGEPL1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: GTP binding protein 3, mitochondrial. This locus encodes a GTP-binding protein. The encoded protein is localized to the mitochondria and may play a role in mitochondrial tRNA modification. Polymorphisms at this locus may be associated with severity of aminoglycoside-induced deafness, a disease associated with a mutation in the 12S rRNA. Alternatively spliced transcript variants encoding different isoforms have been described. [provide…
- **Diseases (Open Targets)**: Combined oxidative phosphorylation defect type 23 (0.788); neurodegenerative disease (0.494); hereditary disease (0.415); mitochondrial disease (0.374); Leigh syndrome (0.185)
- **Europe PMC papers**: 403
- **Why important**: GTPBP3 is directly connected to the central OSGEPL1 node and provides an independent mitochondrial interpretation. It is localized to mitochondria and is involved in mitochondrial tRNA wobble-uridine modification. Its disease associations include combined oxidative-phosphorylation defects, mitochondrial disease, hereditary disease, and Leigh syndrome. Although its network position is peripheral, its functional concordance with OSGEPL1 makes it informative for interpreting the hub-centered portion of the module.
- **Conclusion**: Established evidence supports GTPBP3 as a mitochondrial tRNA-modification factor and makes mitochondrial RNA biology a credible component of the module. The paired occurrence with OSGEPL1 is consistent with coordinated mitochondrial function, but direct interaction and causal cooperation are not demonstrated by the supplied STRING or hu.MAP results.

## Module 2

**Tissue pair**: colon and stem_cells  
**Genes (5)**: CPS1, N4BP3, RAB8B, SLC25A29, VMA12

### Function

The module does not have a GO or KEGG term that passes global multiple-testing correction, so no pathway-level function can be assigned from enrichment evidence. The gene annotations instead point to a heterogeneous combination of intracellular vesicle trafficking and membrane recycling through RAB8B, vacuolar ATPase assembly and lysosomal acidification through VMA12, mitochondrial nitrogen disposal through CPS1, and mitochondrial amino-acid or carnitine transport through SLC25A29. N4BP3 is a relatively poorly characterized nucleoplasmic protein associated with cytoplasmic vesicles and nervous-system development. The co-abundance structure may therefore reflect coordinated expression of several cellular maintenance processes rather than a single well-established biochemical pathway. The lack of globally significant enrichment does not by itself invalidate the module.

**Cell composition.** The module is not dominated by secreted or plasma proteins, since none of the genes is annotated as secreted. It is also not uniformly blood-cell enriched: most genes have low immune-cell specificity or are not detected in immune cells, while N4BP3 has group-enriched blood-cell patterns. Tissue expression is heterogeneous, with individual genes associated with bone marrow, esophagus, liver, and thyroid gland, and with diverse cell types including cDCs, hepatocytes, esophageal cells, and several epithelial or neural-related populations. CPS1 is liver and hepatocyte enriched and is not detected in immune cells, whereas N4BP3 is detected by colon immunohistochemistry and has esophageal and selected blood-cell associations. This pattern does not support a simple plasma contamination explanation, but a shared cell type, tissue-composition effect, or cross-tissue expression program remains possible.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING interaction is reported among the module genes, and no supplementary STRING functional enrichment is available. No hu.MAP complex contains multiple module members. Thus, the observed co-abundance links are not corroborated by the supplied physical-interaction or curated-complex resources. The gene functions nevertheless provide biologically plausible connections involving organelle trafficking, membrane systems, mitochondrial metabolism, and cellular transport. The database-negative result means that the module is not supported as a known protein complex; it does not demonstrate that the co-abundance relationships are biologically meaningless.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a new biological discovery solely because it is absent from STRING and hu.MAP. Its lack of overlap with known high-confidence interactions and curated complexes makes the particular co-abundance combination comparatively unexplained, but the individual genes and their functions are established to very different extents. CPS1, RAB8B, VMA12, and SLC25A29 have recognized cellular or disease-related annotations, whereas N4BP3 is less characterized. The appropriate conclusion is that the cross-tissue co-abundance pattern is a candidate novel observation requiring independent replication, cell-composition control, and experimental testing rather than a proven novel mechanism.

**Hypothesis.** Hypothesis: the shared colon and stem-cell module may represent a context-dependent organelle homeostasis program in which vesicle trafficking and recycling through RAB8B are coordinated with vacuolar-system maintenance through VMA12 and mitochondrial metabolic or transport demands through CPS1 and SLC25A29, with N4BP3 acting as a regulatory or compartment-associated connector. An alternative explanation is that the module reflects mixed cellular composition across the two sample groups, especially because the HPA profiles are tissue and cell-type heterogeneous. This hypothesis predicts that the co-abundance pattern should track organelle-stress, trafficking, and metabolic-state measurements within purified relevant cell populations, but those predictions are not established by the supplied data.

### Important genes

#### CPS1

- **Related proteins** (co-abundance neighbors): N4BP3 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbamoyl-phosphate synthase 1. The mitochondrial enzyme encoded by this gene catalyzes synthesis of carbamoyl phosphate from ammonia and bicarbonate. This reaction is the first committed step of the urea cycle, which is important in the removal of excess urea from cells. The encoded protein may also represent a core mitochondrial nucleoid protein. Three transcript variants encoding different isoforms have been found for this ge…
- **Diseases (Open Targets)**: carbamoyl phosphate synthetase I deficiency disease (0.866); Abnormality of the skeletal system (0.584); venous thromboembolism (0.524); Hyperammonemia (0.522); kidney failure (0.503)
- **Europe PMC papers**: 4139
- **Why important**: CPS1 is the most functionally established metabolic member of the module. It catalyzes the first committed step of the urea cycle, is liver and hepatocyte enriched, and has well-established links to CPS1 deficiency, hyperammonemia, and related metabolic disease. Its module connection to N4BP3 is not supported by STRING or hu.MAP, making it especially useful for testing whether the module reflects metabolic state or cellular composition. Its extensive literature supports strong biological interpretability, while the liver specificity cautions against assigning the whole module a colon or stem-cell-specific function.
- **Conclusion**: Established evidence supports CPS1 as a mitochondrial nitrogen-disposal and urea-cycle marker with strong liver-associated biology. It is a plausible anchor for a metabolic interpretation, but its participation in a shared colon and stem-cell mechanism remains a hypothesis and could instead reflect cell-type composition.

#### RAB8B

- **Related proteins** (co-abundance neighbors): VMA12 (0.85), SLC25A29 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB8B, member RAS oncogene family. RAB proteins, like RAB8B, are low molecular mass monomeric GTPases that localize on the cytoplasmic surfaces of distinct membrane-bound organelles. RAB proteins function in intracellular vesicle transport by aiding in the docking and/or fusion of vesicles with their target membranes (summary by Chen et al., 1997 [PubMed 9030196]).[supplied by OMIM, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.287); placenta praevia (0.192); tooth disorder (0.126); osteoarthritis, hip (0.095); infection (0.072)
- **Europe PMC papers**: 871
- **Why important**: RAB8B is a central connector in the supplied co-abundance graph, linking both VMA12 and SLC25A29. Its established function as a small Ras-family GTPase in vesicle docking, fusion, exocytosis, and endocytic recycling gives the module a plausible trafficking axis. It also has annotations involving antigen presentation and cell-projection organization, and it has a substantial literature and disease-association record. Despite this functional plausibility, no corresponding STRING partner or hu.MAP complex is reported for the module.
- **Conclusion**: Established evidence supports RAB8B as an intracellular membrane-trafficking regulator and as the network connector linking the trafficking-related part of the module. Its role as a coordinator of the entire module is a hypothesis, not a demonstrated physical interaction.

#### VMA12

- **Related proteins** (co-abundance neighbors): RAB8B (0.85), N4BP3 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vacuolar ATPase assembly factor VMA12. The protein encoded by this gene has been observed to localize to the endoplasmic reticulum (ER)-Golgi intermediate compartment (ERGIC) and coat protein complex I (COPI) in some human cells. The encoded protein shares some homology with the yeast protein Vma12. Defects in this gene are a cause of congenital disorder of glycosylation, type IIp. [provided by RefSeq, Mar 2016].
- **Diseases (Open Targets)**: TMEM199-CDG (0.706); congenital disorder of glycosylation type II (0.648); congenital disorder of glycosylation (0.372); hereditary disease (0.190); cancer (0.073)
- **Europe PMC papers**: 80
- **Why important**: VMA12 connects RAB8B and N4BP3 and has a coherent organelle-maintenance annotation. It contributes to vacuolar ATPase assembly, lysosomal lumen acidification, and lysosomal protein catabolism, and defects are associated with congenital disorders of glycosylation. Its cell-type profile is broad and includes glial and Hofbauer-cell annotations, while its tissue specificity is low. The gene therefore offers a mechanistic bridge between vesicle trafficking and degradative or acidic organelle function, although the module contains no curated complex evidence for that bridge.
- **Conclusion**: Established evidence supports VMA12 as an organelle-acidification and V-type ATPase assembly factor with disease relevance. Its proposed coordination with RAB8B and N4BP3 within this module is a testable hypothesis rather than an established molecular complex.

#### SLC25A29

- **Related proteins** (co-abundance neighbors): RAB8B (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 25 member 29. This gene encodes a nuclear-encoded mitochondrial protein that is a member of the large family of solute carrier family 25 (SLC25) mitochondrial transporters. The members of this superfamily are involved in numerous metabolic pathways and cell functions. This gene product was previously reported to be a mitochondrial carnitine-acylcarnitine-like (CACL) translocase (PMID:128829710) or an ornithine …
- **Diseases (Open Targets)**: neurodegenerative disease (0.370); protozoa infectious disease (0.285); Alzheimer disease (0.227); type 2 diabetes mellitus (0.054); diabetes mellitus (0.053)
- **Europe PMC papers**: 316
- **Why important**: SLC25A29 is directly connected to RAB8B in the module and encodes a mitochondrial solute-carrier family protein. Its annotations include amino-acid, ornithine, carnitine, histidine, and O-acyl-carnitine transport, placing it at the interface of mitochondrial metabolism and transport. Its thyroid-associated tissue pattern and diverse epithelial cell-type associations suggest that it is not a simple immune or secreted marker. Its disease associations and literature provide useful support for biological relevance, but the precise transport role has had differing descriptions.
- **Conclusion**: Established evidence supports SLC25A29 as a mitochondrial transport protein involved in metabolite handling. Its connection to RAB8B may indicate coordinated trafficking and mitochondrial physiology, but that interpretation is hypothetical because interaction databases provide no supporting relationship.

#### N4BP3

- **Related proteins** (co-abundance neighbors): CPS1 (0.81), VMA12 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Group enriched; location Nucleoplasm; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NEDD4 binding protein 3. Predicted to be involved in nervous system development. Predicted to be located in axon and dendrite. Predicted to be active in cytoplasmic vesicle. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.380); alcohol drinking (0.272); stroke disorder (0.230); neoplasm (0.080); hepatocellular carcinoma (0.076)
- **Europe PMC papers**: 174
- **Why important**: N4BP3 occupies the bridge position between VMA12 and CPS1 and is detected in colon by immunohistochemistry. It is annotated as a NEDD4-binding protein with predicted roles in nervous-system development and predicted localization to axons, dendrites, and cytoplasmic vesicles. Its tissue and cell-type patterns include esophageal populations, trophoblasts, and selected blood-cell groups, indicating substantial context dependence. Compared with CPS1 and RAB8B, it has a smaller literature and less firmly established molecular function, which makes it important as a potentially informative but uncertain connector.
- **Conclusion**: Established evidence is limited to the reported NEDD4-binding annotation, predicted developmental and vesicle-related roles, and its colon detection. Its apparent bridging position could make it a regulatory linker in the proposed module, but this is a hypothesis that requires direct interaction, perturbation, and cell-specific validation.

## Module 3

**Tissue pair**: colon and stem_cells  
**Genes (10)**: FERMT2, FHL1, GSTM3, HSPA2, PRKCA, LIMS1, LIMS2, MEX3A, NOTCH2, SLMAP

### Function

The strongest interpretation is a cell-adhesion and cell-junction module centered on focal-adhesion and integrin-associated biology. (GO:BP positive regulation of substrate adhesion-dependent cell spreading; q_global = 0.0159) links LIMS2, LIMS1, and FERMT2 to positive regulation of substrate adhesion-dependent cell spreading. (GO:BP cell-cell junction organization; q_global = 0.0202) extends this signal to cell-cell junction organization through FERMT2, LIMS1, LIMS2, and PRKCA. (GO:BP regulation of substrate adhesion-dependent cell spreading; q_global = 0.0371) independently supports regulation of adhesion-dependent cell spreading through FERMT2, LIMS1, and LIMS2. Together, these terms support coordinated regulation of cell shape, adhesion, spreading, junction organization, and signaling at cell-cell or cell-matrix interfaces. (GO:BP cholangiocyte proliferation; q_global = 0.0303) associates LIMS2 and NOTCH2 with cholangiocyte proliferation; this is compatible with a broader role in epithelial or progenitor-cell regulation, but it should not be interpreted as evidence that the module is specific to cholangiocytes. The network topology is consistent with this interpretation because LIMS2 is the central connector and links the focal-adhesion proteins to PRKCA, SLMAP, FHL1, and GSTM3, while NOTCH2 connects to PRKCA and MEX3A connects to LIMS1 and FHL1. No GO or KEGG term passed within-module correction, whereas the terms tagged globally significant GO/KEGG passed the required global correction and are therefore the primary enrichment evidence.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It is also not uniformly blood-cell enriched. Instead, the genes show a mixed cellular composition, with frequent enhancement in smooth muscle cells, hepatic stellate cells, adipocytes, podocytes, and several neural or reproductive cell types. Several genes have immune-cell enhancement, including LIMS2 in naive B cells, FHL1 in NK cells, GSTM3 in naive CD4 T cells, and HSPA2 in T-reg cells, while other genes are absent from or have low specificity in immune cells. This pattern argues against interpreting the shared module simply as a circulating blood signature, although shared stromal, epithelial, smooth-muscle, or other contaminating cell populations could contribute. The module is mixed rather than a broadly expressed housekeeping set. HPA detects protein for several genes in colon, including LIMS1, PRKCA, SLMAP, NOTCH2, and FERMT2, while the stem-cell group has no matching HPA tissue entry, so direct protein-level confirmation in stem cells is unavailable from this fact sheet.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP positive regulation of substrate adhesion-dependent cell spreading | 0.0159 | FERMT2, LIMS1, LIMS2 |
| GO:BP cell-cell junction organization | 0.0202 | FERMT2, LIMS1, LIMS2, PRKCA |
| GO:BP cholangiocyte proliferation | 0.0303 | LIMS2, NOTCH2 |
| GO:BP regulation of substrate adhesion-dependent cell spreading | 0.0371 | FERMT2, LIMS1, LIMS2 |

### STRING and hu.MAP

STRING provides one high-confidence pairwise relationship within the module: FERMT2-LIMS1. This known interaction directly supports the adhesion interpretation but covers only a small part of the observed co-abundance structure. STRING functional annotations are supplementary: (STRING RCTM Cell-extracellular matrix interactions; within-query FDR = 0.0129) connects LIMS2, LIMS1, and FERMT2 with cell-extracellular-matrix interactions, while (STRING SMART Zinc-binding domain present in Lin-11, Isl-1, Mec-3.; within-query FDR = 0.025) and (STRING Keyword LIM domain; within-query FDR = 0.0297) identify a shared LIM-domain or LIM-related zinc-binding signal involving LIMS2, LIMS1, and FHL1. These supplementary findings are concordant with the primary GO interpretation but are not global enrichment evidence. hu.MAP identifies three complexes containing both LIMS1 and LIMS2, tagged (hu.MAP huMAP3_04827.1), (hu.MAP huMAP3_09385.1), and (hu.MAP huMAP3_11194.1). Their additional members include PXN, ILK, PARVG, PARVB, PARVA, RSU1, and, in one complex, other proteins. This repeated LIMS1-LIMS2 complex membership provides independent support for an integrin-linked focal-adhesion or cytoskeletal context. However, the hu.MAP results do not establish that every module gene belongs to one physical complex, and the sparse STRING pairwise connectivity indicates that co-abundance is broader than the currently catalogued direct interactions.

**STRING interactions (score >= 0.7)**: 1 of 45 gene pairs: FERMT2–LIMS1 (0.856)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Cell-extracellular matrix interactions (FDR = 0.0129, 3 genes); SMART Zinc-binding domain present in Lin-11, Isl-1, Mec-3. (FDR = 0.025, 3 genes); Keyword LIM domain (FDR = 0.0297, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_04827.1 (LIMS1, LIMS2; 2/7); huMAP3_09385.1 (LIMS1, LIMS2; 2/8); huMAP3_11194.1 (LIMS1, LIMS2; 2/10)

### Novelty

The module should not be called a completely new molecular mechanism. Its central biology is grounded in established adhesion proteins, LIM-domain proteins, integrin-associated signaling, cell junctions, and Notch biology. Known support includes the STRING FERMT2-LIMS1 interaction, the repeated hu.MAP co-membership of LIMS1 and LIMS2, and the established functional descriptions of LIMS1, LIMS2, and FERMT2. At the same time, the specific conserved co-abundance pattern across colon and stem_cells is not shown in the fact sheet to be an established complex or previously defined module. The limited catalogued interaction coverage means absence from STRING or hu.MAP cannot prove novelty, but it does leave open the possibility that the cross-tissue co-abundance organization is a new systems-level observation. The appropriate conclusion is therefore conditional novelty: potentially novel as a conserved tissue-pair co-abundance module, but not novel in its individual molecular functions.

**Hypothesis.** Hypothesis: in both colon and stem-cell-related contexts, a shared population of adhesion-competent cells coordinates integrin-linked focal adhesions, cell-cell junction remodeling, and signaling that influences cell spreading and fate. LIMS1 and LIMS2 may organize LIM-domain protein assemblies around integrin-linked kinase and other adhesion machinery; FERMT2 may couple these assemblies to integrin-mediated adhesion and actin organization; PRKCA may provide regulated phosphorylation and junctional signaling; and NOTCH2 may connect the adhesion state to cell-fate or proliferative programs. SLMAP, FHL1, and the remaining genes may reflect cytoskeletal, membrane-signaling, stress-response, or cell-state components of the same correlated cellular state. This is a mechanistic model suggested by the co-abundance structure and annotations, not a demonstrated causal pathway. It should be tested by cell-type-resolved expression, perturbation of LIMS1, LIMS2, or FERMT2, and measurement of adhesion, junction integrity, spreading, and Notch-related responses.

### Important genes

#### LIMS2

- **Related proteins** (co-abundance neighbors): FHL1 (0.90), GSTM3 (0.87), SLMAP (0.84), PRKCA (0.84), FERMT2 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: huMAP3_04827.1, huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: LIM zinc finger domain containing 2. This gene encodes a member of a small family of focal adhesion proteins which interacts with ILK (integrin-linked kinase), a protein which effects protein-protein interactions with the extraceullar matrix. The encoded protein has five LIM domains, each domain forming two zinc fingers, which permit interactions which regulate cell shape and migration. A pseudogene of this gene is located on chromos…
- **Diseases (Open Targets)**: autosomal recessive limb-girdle muscular dystrophy type 2W (0.548); renal cell carcinoma (0.296); clear cell renal carcinoma (0.123); neutropenia (0.111); lymphopenia (0.111)
- **Europe PMC papers**: 448
- **Why important**: LIMS2 is the central network connector and participates in every primary globally corrected term, (GO:BP positive regulation of substrate adhesion-dependent cell spreading; q_global = 0.0159) through (GO:BP regulation of substrate adhesion-dependent cell spreading; q_global = 0.0371). It is a focal-adhesion protein with LIM domains, interacts with integrin-linked kinase according to the gene annotation, and is present with LIMS1 in all three hu.MAP complexes, (hu.MAP huMAP3_04827.1) through (hu.MAP huMAP3_11194.1). It also participates in all supplementary STRING terms, (STRING RCTM Cell-extracellular matrix interactions; within-query FDR = 0.0129) through (STRING Keyword LIM domain; within-query FDR = 0.0297), and has disease associations including limb-girdle muscular dystrophy and renal cell carcinoma. Its large literature base supports substantial prior biological characterization.
- **Conclusion**: Established conclusion: LIMS2 is the best network and annotation-level anchor for an adhesion and junction module. Hypothesis: its central position may make it an organizational regulator that couples focal-adhesion architecture to cell-state or proliferative signaling in the shared module.

#### LIMS1

- **Related proteins** (co-abundance neighbors): MEX3A (0.82); STRING partners: FERMT2 (0.856)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: huMAP3_04827.1, huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: LIM zinc finger domain containing 1. The protein encoded by this gene is an adaptor protein which contains five LIM domains, or double zinc fingers. The protein is likely involved in integrin signaling through its LIM domain-mediated interaction with integrin-linked kinase, found in focal adhesion plaques. It is also thought to act as a bridge linking integrin-linked kinase to NCK adaptor protein 2, which is involved in growth factor…
- **Diseases (Open Targets)**: placental abruption (0.297); poisoning (0.245); stroke disorder (0.211); alcohol drinking (0.211); Hirsutism (0.181)
- **Europe PMC papers**: 739
- **Why important**: LIMS1 is a LIM-domain adaptor involved in integrin signaling, cell-matrix adhesion, and cell-cell junction organization. It occurs in (GO:BP positive regulation of substrate adhesion-dependent cell spreading; q_global = 0.0159), (GO:BP cell-cell junction organization; q_global = 0.0202), and (GO:BP regulation of substrate adhesion-dependent cell spreading; q_global = 0.0371), forms the only high-confidence STRING pair with FERMT2, and repeatedly co-occurs with LIMS2 in hu.MAP complexes (hu.MAP huMAP3_04827.1), (hu.MAP huMAP3_09385.1), and (hu.MAP huMAP3_11194.1). Its colon protein detection and enhancement in megakaryocytes, monocytes, and platelets make it relevant both to epithelial adhesion and to possible stromal or blood-associated cellular contributions. Its disease and literature annotations provide established support for biological importance.
- **Conclusion**: Established conclusion: LIMS1 is a strong molecular bridge between the module's adhesion enrichment and its known interaction or complex evidence. Hypothesis: coordinated LIMS1-LIMS2 abundance may mark assembly or stabilization of an adhesion-signaling scaffold rather than merely parallel expression.

#### FERMT2

- **Related proteins** (co-abundance neighbors): LIMS2 (0.81); STRING partners: LIMS1 (0.856)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: FERMT2, also known as kindlin two, appears in (GO:BP positive regulation of substrate adhesion-dependent cell spreading; q_global = 0.0159), (GO:BP cell-cell junction organization; q_global = 0.0202), and (GO:BP regulation of substrate adhesion-dependent cell spreading; q_global = 0.0371), is located at focal adhesions, and is annotated for integrin-mediated signaling, cell-matrix adhesion, cell junctions, and actin-related functions. Its direct high-confidence STRING relationship with LIMS1 gives the module one particularly clear known physical connection. HPA detects the protein in colon and shows enhancement in adipocytes, podocytes, and smooth muscle cells, supporting a possible stromal or contractile-cell contribution. Its disease associations include glaucoma and prostate carcinoma.
- **Conclusion**: Established conclusion: FERMT2 is a plausible effector of the adhesion and spreading signal represented by the primary enrichment. Hypothesis: FERMT2 may translate the LIMS scaffold into altered integrin activation, actin organization, and cell spreading in the shared tissue state.

#### PRKCA

- **Related proteins** (co-abundance neighbors): LIMS2 (0.84), NOTCH2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C alpha. Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and the second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC family members also serve as major receptors for phorbol esters, a class of tumor promoters. Each mem…
- **Diseases (Open Targets)**: acute myeloid leukemia (0.554); hypertrophic cardiomyopathy (0.506); mast cell leukemia (0.475); systemic mastocytosis (0.471); heart failure (0.462)
- **Europe PMC papers**: 5462
- **Why important**: PRKCA is the only gene besides the adhesion scaffold genes that contributes directly to (GO:BP cell-cell junction organization; q_global = 0.0202), linking the module to cell-cell junction organization. It encodes a calcium- and diacylglycerol-responsive serine/threonine kinase with broad signaling capacity, and it connects in the module to LIMS2 and NOTCH2. HPA detects PRKCA in colon and shows enhancement in brain-associated cell types, while its disease associations include hematologic malignancy and cardiac disorders. Its large literature base makes its signaling biology well established.
- **Conclusion**: Established conclusion: PRKCA is a credible signaling component of the junction-related portion of the module. Hypothesis: PRKCA may regulate the phosphorylation state of adhesion or junction-associated proteins and thereby connect focal-adhesion organization with Notch-linked cell-state signaling.

#### NOTCH2

- **Related proteins** (co-abundance neighbors): PRKCA (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in colon
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: notch receptor 2. This gene encodes a member of the Notch family. Members of this Type 1 transmembrane protein family share structural characteristics including an extracellular domain consisting of multiple epidermal growth factor-like (EGF) repeats, and an intracellular domain consisting of multiple, different domain types. Notch family members play a role in a variety of developmental processes by controlling ce…
- **Diseases (Open Targets)**: acroosteolysis dominant type (0.826); Alagille syndrome due to a NOTCH2 point mutation (0.761); Alagille syndrome (0.701); diffuse large B-cell lymphoma (0.550); diabetes mellitus (0.467)
- **Europe PMC papers**: 15072
- **Why important**: NOTCH2 contributes to (GO:BP cholangiocyte proliferation; q_global = 0.0303), which links it with LIMS2 in the globally corrected cholangiocyte-proliferation term, and it is the module's principal annotated cell-fate receptor. It is a transmembrane Notch receptor involved in developmental cell-fate decisions and transcriptional regulation, and it connects in the module to PRKCA. HPA detects NOTCH2 in colon and reports enhancement in monocytes and neutrophils. Its extensive literature and disease associations, including Alagille syndrome and lymphoma, support its importance even though it is not part of the primary adhesion terms.
- **Conclusion**: Established conclusion: NOTCH2 supplies a biologically plausible cell-fate and proliferation axis that complements the adhesion-centered evidence. Hypothesis: the module may reflect coupling between adhesion state and Notch-dependent fate regulation, but the co-abundance data alone do not establish directionality or direct signaling between NOTCH2 and the adhesion proteins.
