# Conserved co-abundance modules: autonomic_nervous_system and cell line

## Module 0

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (32)**: YWHAH, AP1S1, APOA1, ASH2L, BYSL, CHORDC1, DIAPH3, ERLIN2, FLNB, GCSH, GNAS, GNAS, IQGAP3, NAMPT, NDUFA6, NDUFS2, NOP2, NQO1, NUP88, NUSAP1, PLK1, PZP, RASSF9, RHOG, SLK, SMC2, SPR, AARS1, KARS1, THOC1, TPD52L2, VTN

### Function

This is a heterogeneous co-abundance module rather than a cleanly defined pathway. Its central network organization is dominated by RASSF9, which connects genes associated with endosomal or secretory trafficking, lipid and plasma proteins, mitochondrial respiration, cytoskeletal regulation, nuclear transport, RNA processing, translation, and cell division. The module therefore most plausibly reflects coordinated cellular state, protein trafficking, and biosynthetic or proliferative activity rather than one specific biological process. The functional annotations support several component processes: RASSF9 is associated with protein targeting and endosomal transport; NDUFS2 and NDUFA6 with mitochondrial complex I activity; NUP88 with nucleocytoplasmic transport; AARS1 and KARS1 with translation; NOP2 and BYSL with ribosome biogenesis; and PLK1, NUSAP1, and SMC2 with mitosis and chromosome organization. These are established component functions, not evidence for one unified pathway. No GO/KEGG term passed global correction, so no GO/KEGG enrichment can be treated as primary module-level evidence. The lack of a globally enriched term does not invalidate the co-abundance module.

**Cell composition.** The module has a mixed composition. APOA1, PZP, and VTN are liver-enriched or liver-associated secreted proteins, and NAMPT is also annotated as secreted to blood. Thus, part of the signal could reflect circulating protein abundance, liver or plasma contamination, or shared extracellular material rather than intracellular biology in autonomic nervous system or cell-line cells. HPA annotations do not support a module composed predominantly of immune cells: most genes have low immune-cell specificity, although selected genes show immune or hematopoietic associations. Several genes are broadly expressed or have low tissue specificity, including RASSF9, GNAS, ERLIN2, THOC1, and AARS1. Other components show tissue or cell-type enhancement in bone marrow, lymphoid tissue, brain, testis, hepatocytes, trophoblasts, or epithelial populations. Overall, the composition is mixed and should be interpreted cautiously as potentially reflecting shared cell states, sample composition, or extracellular carryover rather than a tissue-specific autonomic nervous system program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a limited set of high-confidence relationships. Established pairings include AARS1 with KARS1, APOA1 with VTN, BYSL with NOP2, DIAPH3 with RHOG, NDUFS2 with NDUFA6, and PLK1 with NUSAP1, SLK, and SMC2. These links support real submodules involving aminoacyl-tRNA synthesis, extracellular or plasma-associated proteins, ribosome biogenesis, actin regulation, mitochondrial complex I, and mitotic control. STRING functional enrichment is absent, so these interactions should not be interpreted as global pathway enrichment. hu.MAP supports several complexes: NDUFS2 and NDUFA6 recur together in multiple complex I assemblies; NUP88 and NUSAP1 recur in nuclear-pore or mitotic-associated complexes; and AARS1 and CHORDC1 occur together in a broader complex. Because each hu.MAP complex contains only a small subset of its members in this module, the evidence supports component-level membership rather than a single complete complex. The observed network therefore combines known molecular relationships with abundance correlations that are not necessarily direct physical interactions.

**STRING interactions (score >= 0.7)**: 8 of 496 gene pairs: AARS1–KARS1 (0.992); APOA1–VTN (0.755); BYSL–NOP2 (0.915); DIAPH3–RHOG (0.722); NDUFA6–NDUFS2 (0.999); NUSAP1–PLK1 (0.811); PLK1–SLK (0.909); PLK1–SMC2 (0.743)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10000.1 (NUP88, NUSAP1; 2/44); huMAP3_14018.1 (NDUFS2, NDUFA6; 2/48); huMAP3_06397.1 (NDUFS2, NDUFA6; 2/49); huMAP3_09982.1 (NDUFS2, NDUFA6; 2/49); huMAP3_09567.1 (NDUFS2, NDUFA6; 2/52); huMAP3_14878.1 (NDUFS2, NDUFA6; 2/53); huMAP3_14442.1 (AARS1, CHORDC1; 2/57); huMAP3_12581.1 (NUP88, NUSAP1; 2/58)

### Novelty

This module should not be called a newly discovered molecular complex or pathway. Several of its relationships are already established by STRING and hu.MAP, including the complex I pair, the AARS1–KARS1 pair, the APOA1–VTN pair, the BYSL–NOP2 pair, and the PLK1-centered mitotic relationships. The apparent novelty is more limited and lies in the cross-tissue co-abundance configuration, especially the association of a high-connectivity RASSF9-centered pattern with secreted plasma proteins, mitochondrial components, nuclear transport factors, and cell-cycle genes. That configuration may be a new observation in these tissue groups, but the fact sheet does not establish replication, tissue-specific specificity, causal regulation, or independence from sample composition. Absence of a relationship from STRING or hu.MAP would not by itself prove novelty.

**Hypothesis.** Hypothesis: the shared module may represent a coordinated cellular-state signal in which RASSF9-associated endosomal or secretory trafficking is coupled to extracellular protein abundance, mitochondrial respiratory capacity, and biosynthetic or proliferative activity. In cell lines, this could reflect variation in growth state, mitotic fraction, metabolic demand, or secretion. In autonomic nervous system samples, it could additionally reflect mixtures of neural, vascular, epithelial, hematopoietic, or circulating material. A testable model is that samples with stronger module abundance will show concordant changes in RASSF9-linked trafficking, complex I activity, secreted APOA1/PZP/VTN abundance, and proliferation-associated PLK1/NUSAP1 activity. This is a hypothesis derived from the combined network and annotations, not an established mechanism.

### Important genes

#### RASSF9

- **Related proteins** (co-abundance neighbors): ERLIN2 (0.95), DIAPH3 (0.94), GCSH (0.91), NQO1 (0.91), SLK (0.90), NUP88 (0.90), VTN (0.89), YWHAH (0.89), SPR (0.88), THOC1 (0.88), NOP2 (0.87), GNAS (0.87), GNAS (0.87), NDUFS2 (0.87), TPD52L2 (0.85), CHORDC1 (0.85), NUSAP1 (0.85), KARS1 (0.85), PLK1 (0.85), NDUFA6 (0.84), IQGAP3 (0.83), ASH2L (0.81), AARS1 (0.81), FLNB (0.81), BYSL (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Ras association domain family member 9. The protein encoded by this gene localizes to perinuclear endosomes. This protein associates with peptidylglycine alpha-amidating monooxygenase, and may be involved with the trafficking of this enzyme through secretory or endosomal pathways. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: hair color (0.423); autoimmune thyroid disease (0.183); osteoarthritis, knee (0.151); Cough (0.120); response to angiotensin-converting enzyme inhibitor (0.120)
- **Europe PMC papers**: 204
- **Why important**: RASSF9 is the dominant network hub in the supplied module, connecting many otherwise weakly connected components. Its established association with perinuclear endosomes, protein targeting, and endosomal or secretory trafficking makes it a plausible organizer of the module's trafficking-related signal. It has substantial literature support relative to most of the less connected genes, although it has no STRING partner or hu.MAP assignment in the supplied evidence.
- **Conclusion**: Established: RASSF9 is highly connected within this co-abundance network and is annotated for endosomal trafficking and protein targeting. Hypothesis: it may mark or help coordinate the shared trafficking and cellular-state signal. The network does not demonstrate that RASSF9 causally regulates the other genes.

#### APOA1

- **Related proteins** (co-abundance neighbors): PZP (0.98), GNAS (0.90), GNAS (0.90), VTN (0.87), AP1S1 (0.86), NQO1 (0.85), NAMPT (0.83), TPD52L2 (0.83), NDUFS2 (0.83), ERLIN2 (0.82), YWHAH (0.81); STRING partners: VTN (0.755)
- **HPA**: Tissue enriched; Group enriched; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein A1. This gene encodes apolipoprotein A-I, which is the major protein component of high density lipoprotein (HDL) in plasma. The encoded preproprotein is proteolytically processed to generate the mature protein, which promotes cholesterol efflux from tissues to the liver for excretion, and is a cofactor for lecithin cholesterolacyltransferase (LCAT), an enzyme responsible for the formation of most plas…
- **Diseases (Open Targets)**: hypoalphalipoproteinemia, primary, 2 (0.762); familial visceral amyloidosis (0.720); hypoalphalipoproteinemia, primary, 2, intermediate (0.618); apolipoprotein A-I deficiency (0.612); dengue disease (0.581)
- **Europe PMC papers**: 20230
- **Why important**: APOA1 is a highly studied, liver-enriched protein secreted to blood and the major protein component of HDL. It has a strong module position relative to many peripheral genes and a known STRING relationship with VTN. Its abundance provides an important warning that the module may partly reflect circulating or liver-derived material rather than a cell-intrinsic autonomic nervous system program. Its disease and literature associations are extensive, but that literature volume does not establish a specific role in this module.
- **Conclusion**: Established: APOA1 participates in lipid transport and cholesterol efflux and is secreted to blood; its relationship with VTN is supported by STRING. Hypothesis: APOA1 may be an extracellular or sample-composition indicator that helps connect the module to plasma-associated biology, rather than a driver of the intracellular network.

#### NDUFS2

- **Related proteins** (co-abundance neighbors): RASSF9 (0.87), APOA1 (0.83); STRING partners: NDUFA6 (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_06397.1, huMAP3_09982.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S2. The protein encoded by this gene is a core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (complex I). Mammalian mitochondrial complex I is composed of at least 43 different subunits, 7 of which are encoded by the mitochondrial genome, and the rest are the products of nuclear genes. The iron-sulfur protein fraction of complex I is made up of 7 subunits, including this g…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.758); mitochondrial complex I deficiency, nuclear type 6 (0.665); type 2 diabetes mellitus (0.608); mitochondrial disease (0.596); Parkinson disease (0.588)
- **Europe PMC papers**: 1723
- **Why important**: NDUFS2 is a core subunit of mitochondrial respiratory complex I and is paired with NDUFA6 by STRING and several hu.MAP complex assemblies. Its annotation directly supports mitochondrial electron transport, complex I assembly, and ATP-linked respiration. It adds a coherent mitochondrial component to an otherwise heterogeneous module and has disease associations involving complex I deficiency and mitochondrial disease.
- **Conclusion**: Established: NDUFS2 is a complex I component, and its relationship with NDUFA6 is supported by both STRING and hu.MAP. Hypothesis: the module may track variation in mitochondrial respiratory capacity or energetic demand. The available evidence does not show that the entire module is a mitochondrial pathway.

#### PLK1

- **Related proteins** (co-abundance neighbors): RASSF9 (0.85); STRING partners: NUSAP1 (0.811), SLK (0.909), SMC2 (0.743)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: polo like kinase 1. The Ser/Thr protein kinase encoded by this gene belongs to the CDC5/Polo subfamily. It is highly expressed during mitosis and elevated levels are found in many different types of cancer. Depletion of this protein in cancer cells dramatically inhibited cell proliferation and induced apoptosis; hence, it is a target for cancer therapy. [provided by RefSeq, Sep 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); Alzheimer disease (0.543); Parkinson disease (0.528); lysosomal storage disease (0.526); microcephaly (0.371)
- **Europe PMC papers**: 16075
- **Why important**: PLK1 is a canonical mitotic serine/threonine kinase with extensive literature and disease relevance. Its STRING relationships with NUSAP1, SLK, and SMC2 connect the module to spindle organization, cytokinesis, and chromosome control. Its HPA pattern is enhanced in proliferative or hematopoietic contexts, making it particularly informative for assessing cell-cycle composition or growth state in cell-line samples.
- **Conclusion**: Established: PLK1 regulates mitotic progression and is connected to several mitosis-related module members by STRING. Hypothesis: PLK1 may report a proliferative substate that contributes to cross-sample co-abundance, especially in cell lines. It is not evidence that the autonomic nervous system component is undergoing pathological proliferation.

#### NUP88

- **Related proteins** (co-abundance neighbors): RASSF9 (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_10000.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 88. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins, a family of 50 to 100 proteins, are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene belongs to the nucleoporin family and is associated with th…
- **Diseases (Open Targets)**: fetal akinesia deformation sequence 1 (0.656); Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.527); fetal akinesia deformation sequence (0.378)
- **Europe PMC papers**: 1030
- **Why important**: NUP88 is a nucleoporin involved in nucleocytoplasmic transport and ribosomal and messenger RNA export. It occurs with NUSAP1 in hu.MAP complexes, linking nuclear transport to a module that also contains mitotic and RNA-processing components. Its disease and cancer associations provide biological context, while its network connection to the RASSF9 hub gives it importance despite limited direct STRING support.
- **Conclusion**: Established: NUP88 is a nuclear-pore component involved in macromolecule transport and shares hu.MAP complex membership with NUSAP1. Hypothesis: it may reflect coordinated nuclear transport and proliferative or biosynthetic state. The module does not establish a direct RASSF9–NUP88 mechanism.

## Module 1

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (24)**: BZW2, ABCD3, ACSL3, BOP1, CAPN2, CHD1, DIS3L2, DYNC1H1, FLII, EIF4G1, KNTC1, LSS, MCM5, NCKAP1, NUP188, DIS3, SEC24A, HM13, SRP68, SRP72, CARS1, EPRS1, XAB2, SNRNP200

### Function

The module does not define a single statistically supported biological function: no GO or KEGG term passed global correction, and STRING functional enrichment was absent. Its structure is heterogeneous, with subnetworks involving cytoplasmic transport and cytoskeletal movement centered on DYNC1H1, RNA processing and spliceosomal function involving SNRNP200 and XAB2, lipid and peroxisomal metabolism involving ACSL3 and ABCD3, endoplasmic-reticulum processing involving HM13 and the SRP components, and cell-cycle or RNA-quality-control functions involving KNTC1, MCM5, DIS3, and DIS3L2. These annotations support a composite cellular-maintenance signature rather than a confidently assigned pathway. The co-abundance structure may therefore reflect coordinated general cellular state, proteostasis, biosynthetic demand, or shared cellular composition rather than one specialized autonomic-nervous-system process.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. HPA reports no secreted genes and generally low immune-cell specificity, with one gene not detected in immune cells. Most genes have low tissue specificity, while the tissue-enhanced genes are distributed across brain, skeletal muscle, bone marrow, heart muscle, tongue, parathyroid gland, and liver rather than pointing to one tissue. Many genes are cell-type enhanced, including genes associated with epithelial, trophoblast, germ-cell, plasma-cell, and progenitor populations, but this is not evidence that the module is a blood-cell module. The shared signal could instead reflect broadly conserved cellular programs or variation in the mixture of cell types across samples. Protein-level HPA assessment is unavailable for both named tissue groups.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a limited set of specific relationships within the module: ABCD3 with ACSL3, CARS1 with EPRS1, KNTC1 with MCM5, SNRNP200 with XAB2, and SRP68 with SRP72. The very strong SNRNP200–XAB2 and SRP68–SRP72 relationships are consistent with established spliceosomal and signal-recognition-particle associations, while the other STRING links support smaller functional connections. hu.MAP independently places ACSL3 with HM13 in membrane and lipid-related complexes (hu.MAP huMAP3_08167.1) and repeatedly places SNRNP200 with XAB2 in spliceosome-related complexes (hu.MAP huMAP3_06726.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1). KNTC1 with BZW2 occurs in broad complexes linked to nuclear transport, translation, and cellular organization (hu.MAP huMAP3_10202.1), (hu.MAP huMAP3_10287.1), (hu.MAP huMAP3_11232.1), while ACSL3 with HM13 also occurs in a larger membrane and organelle-associated complex (hu.MAP huMAP3_09592.1). Because each complex contains only a small subset of module genes and several complexes are broad, these resources support real local relationships but not one unified molecular complex.

**STRING interactions (score >= 0.7)**: 5 of 276 gene pairs: ABCD3–ACSL3 (0.748); CARS1–EPRS1 (0.849); KNTC1–MCM5 (0.728); SNRNP200–XAB2 (0.997); SRP68–SRP72 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08167.1 (ACSL3, HM13; 2/24); huMAP3_06726.1 (SNRNP200, XAB2; 2/37); huMAP3_08501.1 (SNRNP200, XAB2; 2/47); huMAP3_09504.1 (SNRNP200, XAB2; 2/51); huMAP3_10202.1 (KNTC1, BZW2; 2/52); huMAP3_10287.1 (KNTC1, BZW2; 2/53); huMAP3_09945.1 (SNRNP200, XAB2; 2/61); huMAP3_11232.1 (KNTC1, BZW2; 2/78); huMAP3_09592.1 (ACSL3, HM13; 2/95)

### Novelty

This module should not be called a new biological pathway or a newly discovered complex. Several of its strongest local relationships are already represented in STRING or hu.MAP, especially the SNRNP200–XAB2 spliceosomal pair, the SRP68–SRP72 pair, the ACSL3–HM13 complex membership, and the KNTC1–BZW2 complex memberships. At the same time, the particular cross-tissue co-abundance pattern and the way these otherwise distinct subnetworks are connected may be a novel observation. Absence of a complete module-level match in STRING or hu.MAP would not establish novelty, because those databases describe physical or curated relationships rather than tissue-pair co-abundance patterns. Demonstrating novelty would require comparison with published co-abundance modules, independent cohorts, and replication in additional autonomic-nervous-system and cell-line datasets.

**Hypothesis.** Hypothesis: the module represents a conserved cellular-state program that couples intracellular transport and cytoskeletal activity with RNA processing, translation, endoplasmic-reticulum targeting, lipid handling, and cell-cycle-associated maintenance. DYNC1H1 may provide a transport-related structural hub, while the SNRNP200–XAB2 and SRP68–SRP72 relationships mark coordinated RNA maturation and membrane-protein targeting. ACSL3, ABCD3, and HM13 may connect lipid or organelle handling to ER-associated protein processing. This model predicts that the module will track biosynthetic and proteostatic demand or shared cellular composition more reliably than a specialized autonomic-neural function. It remains a hypothesis because global enrichment was not significant and the network contains several weakly connected functional neighborhoods.

### Important genes

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): KNTC1 (0.89), MCM5 (0.85), CARS1 (0.83), SRP72 (0.82), CAPN2 (0.81), FLII (0.81), NCKAP1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 is the principal network hub by weighted connectivity and links otherwise distinct module neighborhoods, including KNTC1, MCM5, CARS1, SRP72, CAPN2, FLII, and NCKAP1. Its established function in cytoplasmic dynein-mediated intracellular transport, organelle movement, spindle dynamics, and retrograde axonal transport is particularly relevant to the autonomic-nervous-system context. HPA reports brain and retinal-ganglion-cell enrichment, and the gene has substantial disease and literature support involving motor-neuron, neuropathy, and neurodevelopmental phenotypes.
- **Conclusion**: Established evidence supports DYNC1H1 as the strongest structural and transport-related integrator in the module, with relevance to neuronal trafficking. The hypothesis that its co-abundance links transport to the other module neighborhoods is plausible from network position but is not demonstrated as a direct molecular interaction by the supplied STRING or hu.MAP evidence.

#### SNRNP200

- **Related proteins** (co-abundance neighbors): NUP188 (0.86), SEC24A (0.83), HM13 (0.82), ACSL3 (0.81); STRING partners: XAB2 (0.997)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein U5 subunit 200. Pre-mRNA splicing is catalyzed by the spliceosome, a complex of specialized RNA and protein subunits that removes introns from a transcribed pre-mRNA segment. The spliceosome consists of small nuclear RNA proteins (snRNPs) U1, U2, U4, U5 and U6, together with approximately 80 conserved proteins. U5 snRNP contains nine specific proteins. This gene encodes one of the U5 snRNP-specific proteins. This…
- **Diseases (Open Targets)**: retinitis pigmentosa (0.820); inherited retinal dystrophy (0.632); autosomal dominant retinitis pigmentosa (0.510); neurodegenerative disease (0.397); eye disorder (0.370)
- **Europe PMC papers**: 889
- **Why important**: SNRNP200 is a central RNA-processing member with connections to NUP188, SEC24A, HM13, and ACSL3. It is a core U5 small nuclear ribonucleoprotein helicase involved in spliceosome assembly and conformational change. Its relationship with XAB2 is strongly supported by STRING and repeatedly represented in hu.MAP spliceosome complexes (hu.MAP huMAP3_06726.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1). It also has established disease associations with retinitis pigmentosa and inherited retinal dystrophy and a substantial literature base.
- **Conclusion**: Established evidence identifies SNRNP200 as a bona fide spliceosomal component and one of the best-supported molecular anchors of the module. Its connection to lipid, ER, and transport genes is a co-abundance observation rather than evidence that those processes form one physical complex.

#### ACSL3

- **Related proteins** (co-abundance neighbors): ABCD3 (0.84), SNRNP200 (0.81), EPRS1 (0.80); STRING partners: ABCD3 (0.748)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli, Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08167.1, huMAP3_09592.1
- **Function (MyGene.info)**: acyl-CoA synthetase long chain family member 3. The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme is highly expressed…
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.370); acute myeloid leukemia (0.313); neurodegenerative disease (0.300); ovarian dysfunction (0.253); Abnormality of the skeletal system (0.215)
- **Europe PMC papers**: 2930
- **Why important**: ACSL3 connects ABCD3, SNRNP200, and EPRS1 and is supported by STRING with ABCD3. It activates long-chain fatty acids for lipid biosynthesis and degradation, has brain expression, and is linked in hu.MAP to HM13 in membrane and organelle-associated complexes (hu.MAP huMAP3_08167.1), (hu.MAP huMAP3_09592.1). Its disease and cancer associations and substantial literature make it a biologically informative marker of lipid and membrane handling within an otherwise heterogeneous module.
- **Conclusion**: Established evidence supports ACSL3 as the main lipid-metabolic representative and as a plausible bridge between the ABCD3 lipid/peroxisomal neighborhood and the broader module. It is not established that ACSL3 drives the shared co-abundance pattern or that the module is primarily a fatty-acid program.

#### XAB2

- **Related proteins** (co-abundance neighbors): CHD1 (0.82); STRING partners: SNRNP200 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: XPA binding protein 2. Involved in mRNA splicing, via spliceosome; transcription, DNA-templated; and transcription-coupled nucleotide-excision repair. Located in nucleoplasm. Part of U2-type catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); neoplasm (0.081); colorectal carcinoma (0.074); neuropathic pain (0.055); gastric cancer (0.043)
- **Europe PMC papers**: 587
- **Why important**: XAB2 is connected to CHD1 and forms the strongest supplied STRING relationship with SNRNP200. It is part of the catalytic spliceosome and also participates in transcription-coupled nucleotide-excision repair, providing a link between RNA processing and genome maintenance. Its repeated hu.MAP membership with SNRNP200 across spliceosome-related complexes (hu.MAP huMAP3_06726.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1), (hu.MAP huMAP3_09945.1) gives independent support, while its disease and developmental associations add biological relevance.
- **Conclusion**: Established evidence supports XAB2 as a spliceosome and transcription-coupled repair component that validates one coherent subnetwork. Any proposed role as a coordinator of the entire module remains hypothetical because the remaining connections are co-abundance edges or indirect database associations.

#### HM13

- **Related proteins** (co-abundance neighbors): SNRNP200 (0.82), BOP1 (0.81), CHD1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: huMAP3_08167.1, huMAP3_09592.1
- **Function (MyGene.info)**: histocompatibility minor 13. The protein encoded by this gene, which localizes to the endoplasmic reticulum, catalyzes intramembrane proteolysis of some signal peptides after they have been cleaved from a preprotein. This activity is required to generate signal sequence-derived human lymphocyte antigen-E epitopes that are recognized by the immune system, and to process hepatitis C virus core protein. The encoded protein is an…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.097); neoplasm (0.094); breast cancer (0.078); breast carcinoma (0.077); eye disorder (0.077)
- **Europe PMC papers**: 460
- **Why important**: HM13 links SNRNP200, BOP1, and CHD1 in the co-abundance graph and is independently paired with ACSL3 in hu.MAP (hu.MAP huMAP3_08167.1), (hu.MAP huMAP3_09592.1). It is an ER intramembrane protease involved in signal-peptide processing, retrograde ER-to-cytosol transport, membrane-protein proteolysis, and antigen-epitope generation. Its localization and function provide a mechanistic connection between ER protein handling and the module's SRP, lipid, and RNA-processing components.
- **Conclusion**: Established evidence supports HM13 as an ER proteolysis and membrane-processing component and as part of the ACSL3-associated complexes. The idea that HM13 couples ER quality control to the spliceosomal and cytoskeletal portions of the module is a testable hypothesis, not an established molecular mechanism.

## Module 2

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (5)**: ACO2, PPM1A, PTS, SCOC, VASP

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway annotation for this module. The co-abundance pattern is therefore best interpreted as a mixed cellular program rather than a demonstrated biological pathway. The genes span Golgi-associated protein-complex regulation and macroautophagy, tetrahydrobiopterin biosynthesis, mitochondrial citrate metabolism, stress-responsive protein dephosphorylation, and actin organization. SCOC is the network center, linking all other module genes, but the absence of STRING functional enrichment means that the shared abundance pattern should not be equated with a validated physical or biochemical pathway. The annotations are compatible with coordinated regulation of cellular maintenance, metabolism, stress signaling, and cytoskeletal organization, but this remains an interpretation rather than an established module function.

**Cell composition.** The module is not composed of plasma or secreted proteins: all listed genes have no secretome annotation. It also does not show a blood-cell-enriched composition according to the HPA summary, which assigns every gene low immune-cell specificity. Several genes nevertheless have cell-type-enhanced expression in platelets, neutrophils, spermatids, or epithelial populations, and PPM1A has tissue enhancement in bone marrow. ACO2 is tissue-enhanced in heart muscle, skeletal muscle, and tongue. Thus, the module does not resemble a simple plasma-protein or blood-cell signature, but shared cellular composition, particularly muscle-associated, epithelial, platelet-related, or progenitor-like cells, could contribute to the cross-tissue co-abundance. HPA protein-detection evidence is unavailable for both queried sample groups, so protein-level tissue localization cannot be confirmed.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and there was no STRING functional enrichment. No hu.MAP complex contained at least two module members. The only observed network structure is the co-abundance graph, in which SCOC connects to PTS, ACO2, PPM1A, and VASP, while the other genes are peripheral. Consequently, the co-abundance links are not supported here by previously catalogued high-confidence physical interactions or shared hu.MAP complexes. This favors an indirect explanation such as shared regulation, common cell composition, coordinated abundance control, or correlated cellular state rather than a proven multiprotein complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module can be considered a potentially novel co-abundance association, but not a newly established molecular complex or pathway. Its novelty is supported by the lack of high-confidence STRING interactions, lack of hu.MAP complexes, and lack of STRING functional enrichment, together with the absence of a globally significant GO or KEGG term. Those absences do not by themselves prove biological novelty: the pattern may reflect indirect regulation, tissue or cell-type composition, technical covariance, or limited database coverage. The most defensible claim is that this particular cross-tissue co-abundance configuration is not explained by the supplied interaction and enrichment resources.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-state program in which SCOC-associated regulation of protein-complex stability or autophagy is co-regulated with mitochondrial energy metabolism through ACO2, tetrahydrobiopterin-dependent metabolic capacity through PTS, stress-responsive phosphatase activity through PPM1A, and actin or adhesion remodeling through VASP. In autonomic nervous system and cell-line samples, this could arise from a common balance between metabolic demand, proteostatic stress, signaling restraint, and cytoskeletal organization. The HPA cell-type annotations suggest that shared cellular composition may be an important alternative explanation. This hypothesis requires validation using independent cohorts, cell-composition adjustment, perturbation experiments, and protein-level measurements.

### Important genes

#### SCOC

- **Related proteins** (co-abundance neighbors): PTS (0.90), ACO2 (0.85), PPM1A (0.84), VASP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: short coiled-coil protein. This gene encodes a short coiled-coiled domain-containing protein that localizes to the Golgi apparatus. The encoded protein interacts with ADP-ribosylation factor-like proteins. Pseudogenes of this gene are found on chromosomes 1 and 14. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2009].
- **Diseases (Open Targets)**: neurodegenerative disease (0.358); Hypercholesterolemia (0.185); exostosis (0.173); gastritis (0.166); glomerulonephritis (0.146)
- **Europe PMC papers**: 430
- **Why important**: SCOC is the network center and is connected to every other module member in the supplied co-abundance graph. Its annotation links it to the Golgi apparatus, ADP-ribosylation-factor-like proteins, macroautophagy, and protein-complex stability, making it the most plausible organizing candidate for the otherwise heterogeneous module. It also has substantial literature coverage and an Open Targets association with neurodegenerative disease.
- **Conclusion**: Established evidence: SCOC is the central co-abundance node and has Golgi, autophagy, and protein-complex annotations. Hypothesis: SCOC may coordinate the module indirectly through proteostasis or intracellular trafficking. The co-abundance data do not establish that SCOC physically regulates the other genes.

#### ACO2

- **Related proteins** (co-abundance neighbors): SCOC (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aconitase 2. The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine proteas…
- **Diseases (Open Targets)**: infantile cerebellar-retinal degeneration (0.814); optic atrophy 9 (0.693); autosomal dominant optic atrophy, classic form (0.619); optic atrophy (0.601); mitochondrial disease (0.505)
- **Europe PMC papers**: 3559
- **Why important**: ACO2 represents mitochondrial intermediary metabolism and catalyzes a step in the tricarboxylic acid cycle. It is tissue-enhanced in heart muscle, skeletal muscle, and tongue, which may explain part of the cross-sample covariance and makes it relevant to cellular energetic state. Its mitochondrial localization and disease associations with optic atrophy and mitochondrial disease provide biological significance despite its peripheral network position.
- **Conclusion**: Established evidence: ACO2 is a mitochondrial citrate-cycle enzyme with muscle-associated HPA tissue enhancement and disease links involving mitochondrial dysfunction and optic atrophy. Hypothesis: ACO2 abundance may mark energetic or oxidative-state variation that covaries with the other module genes, rather than participating in a shared physical complex.

#### PTS

- **Related proteins** (co-abundance neighbors): SCOC (0.90); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 6-pyruvoyltetrahydropterin synthase. The enzyme encoded by this gene catalyzes the elimination of inorganic triphosphate from dihydroneopterin triphosphate, which is the second and irreversible step in the biosynthesis of tetrahydrobiopterin from GTP. Tetrahydrobiopterin, also known as BH(4), is an essential cofactor and regulator of various enzyme activities, including enzymes involved in serotonin biosynthesis and NO synthase activ…
- **Diseases (Open Targets)**: BH4-deficient hyperphenylalaninemia A (0.857); hyperphenylalaninemia due to tetrahydrobiopterin deficiency (0.838); Intellectual disability (0.462); dystonic disorder (0.425); GTP cyclohydrolase I deficiency with hyperphenylalaninemia (0.420)
- **Europe PMC papers**: 27104
- **Why important**: PTS encodes an enzyme in tetrahydrobiopterin biosynthesis, a pathway relevant to neurotransmitter production and nitric oxide synthase activity. It has extensive literature coverage and strong disease associations with tetrahydrobiopterin-deficient hyperphenylalaninemia and related neurological disorders. Although it is peripheral in the module, its biochemical specificity makes it an important functional anchor.
- **Conclusion**: Established evidence: PTS has a defined role in tetrahydrobiopterin biosynthesis and is associated with inherited hyperphenylalaninemia and neurological disease. Hypothesis: PTS may connect the module to neurotransmitter or nitric-oxide-related metabolic state in autonomic nervous system samples. The module does not demonstrate such a connection directly.

#### PPM1A

- **Related proteins** (co-abundance neighbors): SCOC (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase, Mg2+/Mn2+ dependent 1A. The protein encoded by this gene is a member of the PP2C family of Ser/Thr protein phosphatases. PP2C family members are known to be negative regulators of cell stress response pathways. This phosphatase dephosphorylates, and negatively regulates the activities of, MAP kinases and MAP kinase kinases. It has been shown to inhibit the activation of p38 and JNK kinase cascades induced by environmenta…
- **Diseases (Open Targets)**: neurodegenerative disease (0.446); Hypoxemia (0.241); asphyxia (0.241); hair color (0.225); nephrotic syndrome (0.196)
- **Europe PMC papers**: 1198
- **Why important**: PPM1A is a stress-responsive serine/threonine phosphatase that negatively regulates MAP kinase and MAP kinase-kinase activities and can affect stress, transforming-growth-factor, and NF-kappaB signaling. Its bone-marrow tissue enhancement and cell-type enhancement in spermatids, neutrophils, and platelets provide a possible cellular-composition explanation for its covariance. It has disease associations involving neurodegeneration and hypoxemia-related traits.
- **Conclusion**: Established evidence: PPM1A is a phosphatase with reported roles in stress-response and signaling regulation, and it has bone-marrow and several blood-associated cell-type annotations. Hypothesis: PPM1A may reflect coordinated signaling or stress adaptation in the shared module, but the low immune-cell specificity and absence of interaction evidence argue against labeling the module as an immune signature.

#### VASP

- **Related proteins** (co-abundance neighbors): SCOC (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions, Focal adhesion sites; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vasodilator stimulated phosphoprotein. Vasodilator-stimulated phosphoprotein (VASP) is a member of the Ena-VASP protein family. Ena-VASP family members contain an EHV1 N-terminal domain that binds proteins containing E/DFPPPPXD/E motifs and targets Ena-VASP proteins to focal adhesions. In the mid-region of the protein, family members have a proline-rich domain that binds SH3 and WW domain-containing proteins. Their C-terminal EVH2 doma…
- **Diseases (Open Targets)**: neurodegenerative disease (0.215); Hypercholesterolemia (0.133); breast cancer (0.110); breast carcinoma (0.105); hepatocellular carcinoma (0.102)
- **Europe PMC papers**: 5374
- **Why important**: VASP represents actin polymerization, focal-adhesion, cell-junction, and membrane-associated biology. Its cell-type-enhanced annotations include megakaryocytes, platelets, neutrophils, and trophoblasts, while its literature and disease-association coverage are substantial. It is a peripheral module member, but it provides a mechanistically distinct cytoskeletal component that could reflect shared adhesion or cellular-state regulation.
- **Conclusion**: Established evidence: VASP is an Ena-VASP family actin-regulatory protein associated with focal adhesions, cell junctions, and actin filament organization. Hypothesis: VASP may covary with the module because cellular adhesion or cytoskeletal remodeling is coordinated with metabolism and stress signaling. The evidence does not establish a direct VASP interaction with the other module members.

## Module 3

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (14)**: AGK, ARL6, DNM2, HMGN1, LIMA1, NHERF1, NOL9, MT-ND2, PEG10, RFC3, SNX5, CTTN, SYMPK, ZWILCH

### Function

No GO or KEGG term passed global correction, so the module does not support a formally globally enriched pathway assignment. Its most coherent supplementary signal is a membrane ruffle and actin-remodelling theme, supported by the STRING (STRING Component Ruffle; within-query FDR = 0.0099) and (STRING COMPARTMENTS Ruffle; within-query FDR = 0.0438) terms involving SNX5, CTTN, LIMA1 and DNM2. The genes also span mitochondrial respiration, intracellular trafficking, cytoskeletal organization, membrane scaffolding, chromatin regulation, DNA replication, kinetochore function, ribosome biogenesis and placental or reproductive biology. Thus, the module is best interpreted as a heterogeneous co-abundance program with a plausible cellular-interface component rather than as a single established biochemical pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, while a smaller group is tissue enhanced in diverse tissues including brain, heart muscle, retina, esophagus, adrenal gland, testis and placenta. Most genes show cell-type enhancement, but the highlighted cell types are diverse and include epithelial, reproductive, neural, stromal and immune-associated populations. Most genes have low immune-cell specificity, although some are immune-cell enhanced or enriched and CTTN is associated with basophils and neutrophils. The composition therefore does not strongly indicate a plasma-protein or blood-cell module, but shared cell composition, broad cellular stress, or technical abundance effects remain possible. HPA protein-detection evidence is unavailable for both tissue groups.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING pair within the module is CTTN--DNM2, indicating a known relationship between cortactin and dynamin two. STRING supplementary enrichment points to ruffle biology through (STRING Component Ruffle; within-query FDR = 0.0099) and (STRING COMPARTMENTS Ruffle; within-query FDR = 0.0438), with SNX5, CTTN, LIMA1 and DNM2 contributing to that signal. These are useful mechanistic clues but are not globally corrected module-level enrichment evidence. No hu.MAP complex contains at least two module members. The co-abundance network itself is therefore much broader than the currently catalogued physical interaction network, with MT-ND2 acting as the central abundance-connected hub while most other genes are peripheral. This pattern supports coordinated regulation or shared cellular context more strongly than it supports one experimentally established multiprotein complex.

**STRING interactions (score >= 0.7)**: 1 of 91 gene pairs: CTTN–DNM2 (0.993)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Ruffle (FDR = 0.0099, 5 genes); COMPARTMENTS Ruffle (FDR = 0.0438, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a novel co-abundance association, because its member relationships are largely absent from the supplied STRING and hu.MAP evidence and no shared hu.MAP complex was identified. However, absence from those resources does not establish biological novelty: co-abundance can arise from cell composition, mitochondrial content, tissue mixture, or technical effects, and many individual genes have well-established functions. The known CTTN--DNM2 relationship and the supplementary ruffle signal show that at least part of the module recapitulates existing biology. A claim of a new module would require independent replication, preservation across datasets, and tests against cell-type composition and mitochondrial abundance.

**Hypothesis.** Hypothesis: the shared module reflects coordinated variation in cellular interface and trafficking machinery, coupled to mitochondrial state. In this model, CTTN, DNM2, LIMA1, SNX5 and NHERF1 participate in actin-rich membrane ruffles, endocytosis, vesicle movement and membrane scaffolding, while MT-ND2 and AGK reflect mitochondrial respiratory and lipid metabolic state. The remaining genes may be co-varying because of cell-state or proliferative context rather than because they form one physical pathway. This hypothesis predicts that module activity should track ruffling or endocytic phenotypes and mitochondrial measures, while adjustment for cell-type composition may weaken some associations.

### Important genes

#### MT-ND2

- **Related proteins** (co-abundance neighbors): SNX5 (0.88), ARL6 (0.88), AGK (0.87), SYMPK (0.85), HMGN1 (0.85), NHERF1 (0.84), DNM2 (0.84), LIMA1 (0.83), CTTN (0.82), RFC3 (0.82), ZWILCH (0.82), NOL9 (0.81), PEG10 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH dehydrogenase subunit 2. Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone and mitochondrial respiratory chain complex I assembly. Part of mitochondrial respiratory chain complex I. Implicated in Leber hereditary optic neuropathy; multiple sclerosis; myocardial infarction; neurodegenerative disease (multiple); and urinary bladder cancer. [provided by Allianc…
- **Diseases (Open Targets)**: Leber hereditary optic neuropathy (0.688); mitochondrial disease (0.671); Leigh syndrome (0.667); mitochondrial complex I deficiency (0.648); type 2 diabetes mellitus (0.612)
- **Europe PMC papers**: 3526
- **Why important**: MT-ND2 is the weighted-degree hub of the module and connects to every other member in the supplied co-abundance graph. Its established function is as a mitochondrial complex I subunit involved in NADH-linked electron transport, aerobic respiration and mitochondrial ATP production. It has extensive literature and disease links including Leber hereditary optic neuropathy, mitochondrial disease and other neurodegenerative or metabolic conditions. Its hub position makes it important for interpreting the module, but also raises the possibility that mitochondrial abundance or RNA-composition effects organize the network.
- **Conclusion**: Established evidence supports MT-ND2 as a mitochondrial respiratory gene and the central co-abundance correlate. It is not established that MT-ND2 mechanistically regulates the other module genes. Its role as the driver of the module is therefore a hypothesis requiring mitochondrial-content and expression-quality controls.

#### CTTN

- **Related proteins** (co-abundance neighbors): MT-ND2 (0.82); STRING partners: DNM2 (0.993)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles, Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cortactin. This gene is overexpressed in breast cancer and squamous cell carcinomas of the head and neck. The encoded protein is localized in the cytoplasm and in areas of the cell-substratum contacts. This gene has two roles: (1) regulating the interactions between components of adherens-type junctions and (2) organizing the cytoskeleton and cell adhesion structures of epithelia and carcinoma cells. During …
- **Diseases (Open Targets)**: drug allergy (0.349); placenta praevia (0.265); response to antihypertensive drug (0.260); gallbladder disorder (0.258); non-autoimmune hemolytic anemia (0.240)
- **Europe PMC papers**: 2395
- **Why important**: CTTN is one of the clearest functional anchors because it participates in actin cytoskeleton organization, receptor-mediated endocytosis, cell adhesion structures and axon extension. It is included in both supplementary STRING ruffle terms, (STRING Component Ruffle; within-query FDR = 0.0099) and (STRING COMPARTMENTS Ruffle; within-query FDR = 0.0438), and has a high-confidence STRING relationship with DNM2. HPA associates it with neural cell types and with basophils and neutrophils. It also has substantial literature and cancer-related annotation.
- **Conclusion**: Established evidence supports CTTN as an actin, adhesion and endocytic regulator and supports its physical relationship with DNM2. It is plausible, but not demonstrated, that CTTN helps generate the shared module's co-abundance pattern across the two tissue groups.

#### DNM2

- **Related proteins** (co-abundance neighbors): MT-ND2 (0.84); STRING partners: CTTN (0.993)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 is the partner of CTTN in the only high-confidence STRING interaction supplied for the module. Its established functions include GTPase-dependent membrane remodelling, endocytosis, vesicle transport, autophagy and cell motility. It has strong disease relevance for centronuclear myopathy and Charcot-Marie-Tooth disease, and it is associated by HPA with neutrophils. Its network position links the module's central hub to the most clearly documented membrane-remodelling relationship.
- **Conclusion**: Established evidence supports DNM2 as a membrane-remodelling and endocytic protein with a known CTTN interaction. A role for DNM2 in coordinating the entire module, or in connecting mitochondrial state to ruffle biology, remains hypothetical.

#### LIMA1

- **Related proteins** (co-abundance neighbors): MT-ND2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LIM domain and actin binding 1. This gene encodes a cytoskeleton-associated protein that inhibits actin filament depolymerization and cross-links filaments in bundles. It is downregulated in some cancer cell lines. Alternatively spliced transcript variants encoding different isoforms have been described for this gene, and expression of some of the variants maybe independently regulated. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.327); hypertensive disorder (0.276); malunion fracture (0.189); nephrotic syndrome (0.169); Abnormality of the skeletal system (0.157)
- **Europe PMC papers**: 1156
- **Why important**: LIMA1 is included in both supplementary ruffle terms, (STRING Component Ruffle; within-query FDR = 0.0099) and (STRING COMPARTMENTS Ruffle; within-query FDR = 0.0438). It binds and bundles actin, inhibits actin filament depolymerization, and is annotated for ruffle organization and cell migration. HPA places it at the plasma membrane and actin filaments and identifies enhancement in several differentiated cell types. It therefore provides a direct cytoskeletal explanation for the module's supplementary functional signal.
- **Conclusion**: Established evidence supports LIMA1 as an actin-bundling and membrane-associated cytoskeletal regulator. Its participation in the shared co-abundance program is consistent with the data, but the data do not show that LIMA1 controls the other module members.

#### NHERF1

- **Related proteins** (co-abundance neighbors): MT-ND2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Centriolar satellite; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NHERF family PDZ scaffold protein 1. This gene encodes a sodium/hydrogen exchanger regulatory cofactor. The protein interacts with and regulates various proteins including the cystic fibrosis transmembrane conductance regulator and G-protein coupled receptors such as the beta2-adrenergic receptor and the parathyroid hormone 1 receptor. The protein also interacts with proteins that function as linkers between integral membrane and cyt…
- **Diseases (Open Targets)**: hypophosphatemic nephrolithiasis/osteoporosis 2 (0.643); nephrolithiasis (0.262); hypophosphatemia (0.261); hereditary disease (0.194); chronic kidney disease (0.119)
- **Europe PMC papers**: 1155
- **Why important**: NHERF1 is a membrane and cytoskeletal scaffold that regulates sodium-hydrogen exchange-related functions, CFTR, G-protein-coupled receptors and other membrane proteins. It localizes to actin-rich structures and is annotated for plasma-membrane organization, epithelial morphogenesis and cell-shape regulation. HPA shows tissue enhancement in esophagus and cell-type enhancement in enterocytes and esophageal epithelial populations. Its strong connection to epithelial membrane architecture complements the ruffle and trafficking interpretation even though it is not in the supplementary STRING ruffle gene set.
- **Conclusion**: Established evidence supports NHERF1 as a membrane-cytoskeletal scaffold with epithelial and receptor-regulatory functions. Its contribution to this module is a biologically plausible interpretation, not a demonstrated physical interaction with the other module members.

#### ARL6

- **Related proteins** (co-abundance neighbors): MT-ND2 (0.88); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Primary cilium; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ARF like GTPase 6. The protein encoded by this gene belongs to the ARF-like (ADP ribosylation factor-like) sub-family of the ARF family of GTP-binding proteins which are involved in regulation of intracellular traffic. Mutations in this gene are associated with Bardet-Biedl syndrome (BBS). A vision-specific transcript, encoding long isoform BBS3L, has been described (PMID: 20333246). [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: Bardet-Biedl syndrome (0.831); retinitis pigmentosa (0.781); Bardet-Biedl syndrome 1 (0.705); inherited retinal dystrophy (0.606); polydactyly (0.462)
- **Europe PMC papers**: 837
- **Why important**: ARL6 connects to the central MT-ND2 hub and is associated with intracellular traffic, protein targeting to membranes, vesicle-mediated transport, cilia and melanosome transport. HPA shows enhancement in retina and in photoreceptor and ciliated cell types. Its Bardet-Biedl syndrome and retinal-dystrophy associations make it relevant to the neural, sensory and ciliary aspects represented among the module's tissue annotations.
- **Conclusion**: Established evidence supports ARL6 as a trafficking and ciliary GTPase associated with Bardet-Biedl syndrome and retinal disease. Its inclusion supports a broad intracellular-trafficking interpretation, but no direct ARL6 interaction with the other module genes is established by the supplied STRING or hu.MAP results.

## Module 4

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (11)**: AP3D1, FAM120A, GBE1, GNA11, HELLS, MEN1, POR, OPA1, PITRM1, SLC29A1, SCG3

### Function

The strongest integrated interpretation is a heterogeneous secretory, trafficking, metabolic, mitochondrial, and signaling module rather than a narrowly defined pathway. The only globally corrected GO/KEGG result is (GO:BP alpha-beta T cell differentiation; q_global = 0.0392), alpha-beta T cell differentiation, supported by AP3D1, MEN1, and OPA1. This result should be treated cautiously because the three contributing genes have distinct established functions: AP3D1 in vesicle and lysosomal trafficking, MEN1 in chromatin regulation and DNA damage responses, and OPA1 in mitochondrial organization. The module hub SCG3 points toward neuroendocrine secretory-granule biology, while the remaining genes represent mitochondrial protein processing, G-protein signaling, steroid and xenobiotic metabolism, nucleoside transport, glycogen metabolism, RNA regulation, and chromatin biology. Thus, the data support a co-abundance program associated with secretory-cell state and cellular maintenance, with an immune or T-cell differentiation association that is statistically supported by (GO:BP alpha-beta T cell differentiation; q_global = 0.0392) but mechanistically not established for the module as a whole.

**Cell composition.** This is not predominantly a plasma-protein or broadly secreted-protein module. SCG3 is the only gene annotated as secreted, specifically in brain, and it is the highly connected hub; the other genes are intracellular, membrane-associated, or organelle-associated. Most genes have low tissue specificity, whereas several show cell-type enhancement across neural, endocrine, hepatic, muscle, intestinal, reproductive, and blood-related cell types. The HPA summary shows mostly low immune-cell specificity, with selected immune associations involving GNA11, SLC29A1, and other genes, including neutrophil or eosinophil signals. This does not resemble a coherent blood-cell module, although variation in shared cell types or sample composition could contribute to the cross-tissue co-abundance. The lack of matching HPA protein-detection data for the two sampled tissue labels limits protein-level interpretation.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP alpha-beta T cell differentiation | 0.0392 | AP3D1, MEN1, OPA1 |

### STRING and hu.MAP

No gene pair in the module meets the supplied stringent STRING interaction threshold, and STRING reports no supplementary functional-enrichment result. No hu.MAP complex contains at least two module members. Therefore, the co-abundance structure is not recapitulated by the tested catalogue of known physical or functional interactions and does not identify a known shared complex. The star-like topology centered on SCG3, with the other genes connected only to that hub, indicates coordinated abundance without evidence that the proteins form a direct molecular complex. This could reflect shared cellular state, co-regulation, compartmental composition, or indirect biological coupling.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is potentially novel as a cross-tissue co-abundance association because it has no detected high-confidence STRING relationships, no supported hu.MAP multi-member complex, and combines genes from several otherwise distinct functional systems around SCG3. However, these observations do not prove discovery of a new molecular pathway. The module may instead capture shared cell states, sample composition, or coordinated expression of genes that are already individually well characterized. The globally supported (GO:BP alpha-beta T cell differentiation; q_global = 0.0392) association provides a biological clue, but the discordance between that term and the heterogeneous gene functions means that independent replication, expression control analyses, cell-composition adjustment, and experimental validation would be needed before claiming a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular-state program in which neuroendocrine secretory-granule biology, represented by the SCG3 hub, covaries with vesicle trafficking, mitochondrial quality and energy handling, receptor-linked signaling, and tissue-specific metabolic functions. In cell populations with immune or endocrine features, this state could coincide with alpha-beta T-cell differentiation-related transcriptional programs, consistent with (GO:BP alpha-beta T cell differentiation; q_global = 0.0392), without implying that all module proteins directly participate in T-cell differentiation. A plausible alternative is that SCG3 marks a shared secretory or neural-like cellular component and the peripheral genes are indirect abundance correlates rather than members of a single biochemical pathway.

### Important genes

#### SCG3

- **Related proteins** (co-abundance neighbors): AP3D1 (0.91), FAM120A (0.87), HELLS (0.85), OPA1 (0.84), MEN1 (0.84), PITRM1 (0.84), GNA11 (0.84), POR (0.83), SLC29A1 (0.81), GBE1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: secretogranin III. The protein encoded by this gene is a member of the chromogranin/secretogranin family of neuroendocrine secretory proteins. Granins may serve as precursors for biologically active peptides. Some granins have been shown to function as helper proteins in sorting and proteolytic processing of prohormones; however, the function of this protein is unknown. Two transcript variants encoding different iso…
- **Diseases (Open Targets)**: osteoarthritis, knee (0.403); intelligence (0.341); osteoarthritis, hip (0.317); placental abruption (0.253); total knee arthroplasty (0.212)
- **Europe PMC papers**: 797
- **Why important**: SCG3 is the network hub, connected to every other module member with strong co-abundance weights. HPA links it to brain, pituitary, retina, neural and neuroendocrine cell types, and identifies brain secretion and secretory-vesicle localization. Its annotation places it in the chromogranin and secretogranin family and in protein localization to secretory granules. It therefore provides the clearest anchor for interpreting the module as a secretory or neuroendocrine state. Its disease and literature associations are less definitive for mechanism than those of several other genes, and its annotated function remains partly unknown.
- **Conclusion**: Established: SCG3 is the central co-abundance hub and is associated with secretory-granule biology and neural or neuroendocrine cell types. Hypothesis: SCG3 may organize or mark the shared cellular state that brings otherwise unrelated genes into the module. Direct physical interaction with the other members is not established by STRING or hu.MAP.

#### AP3D1

- **Related proteins** (co-abundance neighbors): SCG3 (0.91); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit delta 1. The protein encoded by this gene is a subunit of the AP3 adaptor-like complex, which is not clathrin-associated, but is associated with the golgi region, as well as more peripheral structures. The AP-3 complex facilitates the budding of vesicles from the golgi membrane, and may be directly involved in trafficking to lysosomes. This subunit is implicated in intracellular biogenesis and trafficking …
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 10 (0.584); Hermansky-Pudlak syndrome 2 (0.455); Hermansky-Pudlak syndrome (0.432); Alzheimer disease (0.421); lysosomal storage disease (0.417)
- **Europe PMC papers**: 637
- **Why important**: AP3D1 is one of the genes contributing to the globally significant (GO:BP alpha-beta T cell differentiation; q_global = 0.0392) term and is the only direct neighbor of SCG3 among the genes with the most direct trafficking relevance. Its established role in the AP-3 adaptor complex connects the module to Golgi-derived vesicle budding, lysosomal transport, anterograde axonal transport, pigment granules, platelet dense granules, and neurotransmitter vesicles. Its disease associations include Hermansky-Pudlak syndromes and lysosomal storage disease, giving it strong mechanistic relevance to vesicle biology.
- **Conclusion**: Established: AP3D1 supports an intracellular vesicle-trafficking interpretation and contributes to (GO:BP alpha-beta T cell differentiation; q_global = 0.0392). Hypothesis: the SCG3–AP3D1 relationship may reflect coordinated secretory-vesicle handling, but the absence of catalogue-supported protein interaction evidence prevents treating it as a confirmed complex.

#### OPA1

- **Related proteins** (co-abundance neighbors): SCG3 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: OPA1 mitochondrial dynamin like GTPase. The protein encoded by this gene is a nuclear-encoded mitochondrial protein with similarity to dynamin-related GTPases. The encoded protein localizes to the inner mitochondrial membrane and helps regulate mitochondrial stability and energy output. This protein also sequesters cytochrome c. Mutations in this gene have been associated with optic atrophy type 1, which is a dominantly inherited optic …
- **Diseases (Open Targets)**: autosomal dominant optic atrophy, classic form (0.846); Behr syndrome (0.812); optic atrophy with or without deafness, ophthalmoplegia, myopathy, ataxia, and neuropathy (0.766); mitochondrial DNA depletion syndrome 14B (cardioencephalomyopathic type) (0.745); optic atrophy (0.653)
- **Europe PMC papers**: 12169
- **Why important**: OPA1 contributes to (GO:BP alpha-beta T cell differentiation; q_global = 0.0392), is connected directly to the SCG3 hub, and has a well-established role in mitochondrial inner-membrane organization, fusion, stability, and energy output. Its association with dominant optic atrophy and other mitochondrial or neuropathic disorders makes it especially relevant to a module containing neural and secretory-cell signals. OPA1 also has extensive literature support compared with most module members.
- **Conclusion**: Established: OPA1 represents mitochondrial organization and is part of the globally supported (GO:BP alpha-beta T cell differentiation; q_global = 0.0392) gene overlap. Hypothesis: mitochondrial fitness may support the secretory-cell state marked by SCG3, but a direct causal connection between OPA1 and the module’s immune association is unproven.

#### GNA11

- **Related proteins** (co-abundance neighbors): SCG3 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: G protein subunit alpha 11. The protein encoded by this gene belongs to the family of guanine nucleotide-binding proteins (G proteins), which function as modulators or transducers in various transmembrane signaling systems. G proteins are composed of 3 units: alpha, beta and gamma. This gene encodes one of the alpha subunits (subunit alpha-11). Mutations in this gene have been associated with hypocalciuric hypercalcemia type…
- **Diseases (Open Targets)**: familial hypoparathyroidism (0.754); familial hypocalciuric hypercalcemia 2 (0.736); autosomal dominant hypocalcemia (0.611); congenital hemangioma (0.494); uveal melanoma (0.469)
- **Europe PMC papers**: 4418
- **Why important**: GNA11 is directly connected to SCG3 and supplies a signaling interpretation through heterotrimeric G-protein, G-protein-coupled receptor, phospholipase C, adenylate cyclase, and acetylcholine-receptor pathways. HPA shows enhancement in intestinal cell types and immune enhancement in neutrophils. Its established associations with familial hypocalciuric hypercalcemia, hypoparathyroidism, and dominant hypocalcemia connect the module to endocrine and calcium-signaling biology.
- **Conclusion**: Established: GNA11 is a signaling component with endocrine, intestinal, and selected immune-cell relevance. Hypothesis: it may couple extracellular receptor inputs to the secretory state represented by SCG3, but the module does not establish a specific receptor, pathway direction, or causal role.

#### POR

- **Related proteins** (co-abundance neighbors): SCG3 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cytochrome p450 oxidoreductase. This gene encodes an endoplasmic reticulum membrane oxidoreductase that is essential for multiple metabolic processes, including reactions catalyzed by cytochrome P450 proteins for metabolism of steroid hormones, drugs and xenobiotics. The encoded protein has a flavin adenine dinucleotide (FAD)-binding domain and a flavodoxin-like domain which bind two cofactors, FAD and FMN, that allow it to dona…
- **Diseases (Open Targets)**: congenital adrenal hyperplasia due to cytochrome P450 oxidoreductase deficiency (0.834); Antley-Bixler syndrome with genital anomalies and disordered steroidogenesis (0.810); congenital adrenal hyperplasia (0.534); coffee consumption (0.446); Antley-Bixler syndrome without genital anomalies or disordered steroidogenesis (0.444)
- **Europe PMC papers**: 28661
- **Why important**: POR is directly connected to SCG3 and represents a major metabolic dimension of the module. It transfers electrons from NADPH to microsomal cytochrome P450 enzymes and is involved in steroid-hormone, drug, xenobiotic, fatty-acid, and nitric-oxide-related metabolism. HPA shows enhancement in liver and in hepatic, intestinal, and neutrophil cell types. Its strong disease associations with POR-deficiency syndromes and disordered steroidogenesis make it an informative marker of metabolic and endocrine cellular state.
- **Conclusion**: Established: POR supports an endoplasmic-reticulum and steroid or xenobiotic metabolic interpretation. Hypothesis: POR may indicate the metabolic capacity needed by secretory or endocrine-like cells in this shared module. Its presence does not demonstrate a direct biochemical relationship with SCG3 or the other module members.

## Module 5

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (11)**: ANAPC7, CNDP2, DCAF1, MSH3, NAA50, NAP1L5, OSBPL9, RCN3, ARHGAP17, SRI, TLN1

### Function

The module does not support a single statistically established GO or KEGG function: no GO or KEGG term passed global correction. Its structure is a hub-and-spoke co-abundance pattern centered on NAP1L5, with the other genes connected primarily through that hub rather than through a densely interconnected network. The constituent genes span chromatin and protein regulation, cell-cycle control, DNA mismatch repair, intracellular calcium handling, sterol and membrane organization, cytoskeletal signaling, and endoplasmic-reticulum protein handling. The most coherent biological interpretation is therefore a possible cross-tissue cellular-state or proteostasis-related module rather than a well-defined pathway. The annotations suggest links among nuclear regulation, protein turnover, membrane and cytoskeletal organization, and calcium-dependent cellular function, but these links remain interpretive because enrichment and external network support are absent.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only RCN3 has a secretome annotation, and that annotation describes intracellular and membrane localization. The genes are also not strongly blood-cell enriched. Most have low immune-cell specificity, with RCN3 the only gene marked as immune-cell enhanced. The HPA profile is heterogeneous, including brain, skeletal muscle, blood vessel, intestine, and testis tissue associations, alongside cell-type associations spanning neurons, myonuclei, enterocytes, stromal cells, glial cells, megakaryocytes, and spermatids. This diversity argues against a simple blood-contamination explanation, although shared cell states, tissue composition, or broad cellular stress and growth programs could contribute. Several genes have low tissue specificity and broad intracellular functions, so a housekeeping-like or general cellular-state component is plausible. Protein-level interpretation in the two queried tissue groups is limited because the supplied HPA protein-detection fields provide no matching tissue evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and STRING functional enrichment was absent. No hu.MAP complex contained multiple module members. Thus, the co-abundance relationships are not corroborated as established physical interactions or shared complexes by these resources. The annotations nevertheless identify established functions for individual genes: NAP1L5 is related to nucleosome assembly, ANAPC7 to APC/C-mediated cell-cycle control, NAA50 to NatE-dependent protein acetylation, TLN1 to integrin and actin-cytoskeletal signaling, OSBPL9 to sterol and phospholipid transfer, SRI to calcium handling, CNDP2 to dipeptide and glutathione metabolism, RCN3 to endoplasmic-reticulum calcium binding and protein secretion, MSH3 to mismatch repair, ARHGAP17 to small-GTPase regulation, and DCAF1 to Cul4-associated ubiquitin regulation. These are established gene-level functions, not evidence that the genes form one physical complex.

**STRING interactions (score >= 0.7)**: 0 of 55 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The shared co-abundance pattern may be a new observation, but it cannot be claimed as a newly discovered biological module from the supplied evidence alone. Its novelty is supported only in the limited sense that the module has no matching high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO or KEGG signature. Those absences do not prove novelty: the pattern could reflect correlated expression, tissue composition, cell-state effects, technical structure, or an incompletely annotated relationship. The star-like topology, heterogeneous tissue annotations, and lack of pathway enrichment make a specific mechanistic discovery less likely than a potentially reproducible co-abundance signature requiring replication in independent data and testing after adjustment for tissue and cell-type composition.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular state in which NAP1L5-associated chromatin or nucleosome-related regulation covaries with protein acetylation, ubiquitin-dependent regulation, DNA repair, intracellular calcium handling, lipid and membrane organization, and cytoskeletal signaling. One possible explanation is that a shared transcriptional or proteostatic state across autonomic-nervous-system samples and cell-line samples produces the observed correlations without requiring direct physical interaction among the proteins. A second possibility is that NAP1L5 is a central abundance marker linked to several otherwise independent cellular programs. This hypothesis predicts that the module should be sensitive to adjustment for cell composition and proliferation, and that its reproducibility should be tested in independent cohorts and with protein-level measurements.

### Important genes

#### NAP1L5

- **Related proteins** (co-abundance neighbors): ANAPC7 (0.86), NAA50 (0.84), TLN1 (0.83), OSBPL9 (0.82), SRI (0.82), CNDP2 (0.82), RCN3 (0.82), MSH3 (0.81), ARHGAP17 (0.81), DCAF1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleosome assembly protein 1 like 5. This gene encodes a protein that shares sequence similarity to nucleosome assembly factors, but may be localized to the cytoplasm rather than the nucleus. Expression of this gene is downregulated in hepatocellular carcinomas. This gene is located within a differentially methylated region (DMR) and is imprinted and paternally expressed. There is a related pseudogene on chromosome 4. [provided by Re…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.279); neurodegenerative disease (0.225); type 2 diabetes mellitus (0.216); thrombophilia (0.210); osteoarthritis, knee (0.209)
- **Europe PMC papers**: 471
- **Why important**: NAP1L5 is the topological hub: every other module member is connected to it in the supplied subgraph. Its annotation links it to nucleosome assembly, with brain enrichment and cell-type associations including autonomic-relevant neural populations. It also has substantial literature and disease-linked associations involving neurodegenerative, skeletal, metabolic, and thrombotic phenotypes. Because the module is centered on this gene, NAP1L5 is the most important candidate for distinguishing a real regulatory signal from a hub-driven correlation pattern.
- **Conclusion**: Established evidence: NAP1L5 is a nucleosome-assembly-related gene and the network hub, with brain-associated HPA evidence. Hypothesis: its abundance may mark a chromatin or cellular-state program that links the otherwise diverse genes. This remains unproven because neither STRING nor hu.MAP supports the proposed module as a physical interaction network.

#### SRI

- **Related proteins** (co-abundance neighbors): NAP1L5 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorcin. This gene encodes a calcium-binding protein with multiple E-F hand domains that relocates from the cytoplasm to the sarcoplasmic reticulum in response to elevated calcium levels. In addition to regulating intracellular calcium homeostasis it also modulates excitation-contraction coupling in the heart. Alternative splicing results in multiple transcript variants encoding distinct proteins. Multiple…
- **Diseases (Open Targets)**: hereditary disease (0.340); benign neoplasm of pituitary gland (0.261); neoplasm (0.101); hepatocellular carcinoma (0.099); Abnormality of the skeletal system (0.087)
- **Europe PMC papers**: 25217
- **Why important**: SRI is connected directly to the hub and has a well-established role in calcium binding, sarcoplasmic-reticulum calcium regulation, and excitation-contraction coupling. Its tissue annotation is intestine-enhanced, while its cell-type associations include enterocytes and other epithelial populations. SRI also has a very substantial literature base and broad disease relevance, making it a biologically informative test of whether the module captures calcium and membrane physiology rather than only nuclear processes.
- **Conclusion**: Established evidence: SRI regulates intracellular calcium handling and is associated with the module through NAP1L5. Hypothesis: calcium-dependent signaling could be one downstream cellular state represented by the module. The cross-tissue interpretation is uncertain because the HPA tissue associations are not specific to autonomic nervous system or cell line.

#### TLN1

- **Related proteins** (co-abundance neighbors): NAP1L5 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Low immune cell specificity; location Focal adhesion sites, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: talin 1. This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cel…
- **Diseases (Open Targets)**: cancer (0.612); Noonan syndrome (0.526); hypertrophic cardiomyopathy (0.510); Costello syndrome (0.503); cardiofaciocutaneous syndrome (0.370)
- **Europe PMC papers**: 2276
- **Why important**: TLN1 represents the cytoskeletal and adhesion arm of the module. It is annotated for integrin activation, cell adhesion, actin organization, and cell-cell junction biology, and its HPA profile is enhanced in blood vessels with group enrichment in megakaryocytes and platelets. It has a large literature base and multiple cardiovascular and developmental disease associations. Its inclusion helps test whether the module reflects changes in cell shape, adhesion, or cellular composition.
- **Conclusion**: Established evidence: TLN1 is a focal-adhesion and integrin-associated cytoskeletal protein with vascular and platelet-related HPA associations. Hypothesis: the module may partly reflect a shared adhesion or cytoskeletal state. There is no evidence here that TLN1 physically interacts with the other module members.

#### MSH3

- **Related proteins** (co-abundance neighbors): NAP1L5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 3. The protein encoded by this gene forms a heterodimer with MSH2 to form MutS beta, part of the post-replicative DNA mismatch repair system. MutS beta initiates mismatch repair by binding to a mismatch and then forming a complex with MutL alpha heterodimer. This gene contains a polymorphic 9 bp tandem repeat sequence in the first exon. The repeat is present 6 times in the reference genome sequence a…
- **Diseases (Open Targets)**: familial adenomatous polyposis 4 (0.743); endometrial carcinoma (0.651); hereditary neoplastic syndrome (0.576); endometrial cancer (0.374); endometrial neoplasm (0.370)
- **Europe PMC papers**: 4720
- **Why important**: MSH3 represents genome maintenance rather than membrane or cytoskeletal biology. It forms MutS beta with MSH2 and participates in DNA mismatch repair, repeat-element maintenance, and recombination-related processes. It has a large literature base and strong disease associations involving familial adenomatous polyposis and endometrial cancer. Its presence makes cell-cycle, replication, or DNA-damage state a plausible alternative explanation for the co-abundance pattern.
- **Conclusion**: Established evidence: MSH3 is a mismatch-repair factor with important inherited and cancer-related disease associations. Hypothesis: the module may include a genome-maintenance or proliferative-state component. The module data do not establish that DNA repair is its dominant function, particularly because no GO or KEGG term passed global correction.

#### ARHGAP17

- **Related proteins** (co-abundance neighbors): NAP1L5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho GTPase activating protein 17. RICH1 is a GTPase-activating protein (GAP). GAPs stimulate the intrinsic GTP hydrolysis of small G proteins, such as RHOA (MIM 165390), RAC1 (MIM 602048), and CDC42 (MIM 116952).[supplied by OMIM, Apr 2004].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.559); neurodegenerative disease (0.496); atrial fibrillation (0.367); gout (0.321); diabetic neuropathy (0.277)
- **Europe PMC papers**: 527
- **Why important**: ARHGAP17 provides a mechanistic bridge to cell polarity, membrane signaling, and actin regulation through its control of RHOA, RAC1, and CDC42 activity. It is associated with neuronal and glial cell types in HPA and has disease links involving skeletal abnormalities, neurodegeneration, atrial fibrillation, and diabetic neuropathy. Its direct connection to the hub places it in the module's signaling and morphology-related branch.
- **Conclusion**: Established evidence: ARHGAP17 is a Rho-family GTPase-activating protein involved in actin-cytoskeleton and signal-transduction regulation. Hypothesis: it may connect the module to neuronal morphology, cell polarity, or adaptive membrane signaling. This interpretation is provisional because the network contains no independently supported STRING or hu.MAP relationship.

## Module 6

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (13)**: ASNS, ATAD2, CIT, MCFD2, MDN1, POGLUT1, PLEC, SACS, SKIC3, PPAN, TAF5, VANGL2, VAV2

### Function

The module does not support a single statistically established GO or KEGG function because no GO/KEGG term passed global multiple-testing correction. Its gene annotations instead suggest a mixed cellular program involving planar-cell-polarity and developmental signaling, cytoskeletal organization, neuronal development, RNA processing and ribosome maturation, chromatin and transcriptional regulation, protein folding, ER protein glycosylation and trafficking, and cellular proliferation. The co-abundance topology is dominated by VANGL2, which connects to most of the other genes, while the remaining genes form mostly peripheral links. This structure is more consistent with a coordinated expression state or shared cellular context than with a demonstrated physical protein complex or a narrowly defined pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins and does not show a strong blood-cell signature. Most genes have low immune-cell specificity or are not detected in immune cells, with only VAV2 showing immune-cell enhancement in memory B cells. Two genes have intracellular or membrane-associated secretome annotations, but the module is not a secreted-protein module. The HPA profile is heterogeneous: several genes are broadly expressed, whereas many show cell-type enhancement in neural and glial populations, and individual genes are enhanced in bone marrow, lymphoid tissue, pancreas, brain, skeletal muscle, or testis. The shared signal could therefore reflect a mixture of broadly expressed cellular programs and tissue or cell-type composition, rather than a uniform autonomic-nervous-system-specific mechanism. Protein-level interpretation in the two queried sample groups is limited because the HPA summary reports no matching tissue protein detections for either group.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No gene pair in the module reaches the specified high-confidence STRING interaction threshold, and STRING functional enrichment is absent. No hu.MAP complex contains multiple module members. Thus, the co-abundance relationships are not corroborated here by high-confidence known protein interactions or a shared hu.MAP complex. The network may represent coordinated regulation, correlated abundance caused by cell composition, indirect biological relationships, or interactions that are context-dependent and not captured by these resources. The absence of STRING and hu.MAP support argues against calling this module a validated physical complex.

**STRING interactions (score >= 0.7)**: 0 of 78 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module may represent a previously unreported co-abundance pattern, but it cannot be declared a new biological mechanism from the available evidence. Its apparent novelty is supported only in the limited sense that the module has no high-confidence STRING pair, no STRING enrichment, and no multi-member hu.MAP complex. Those database absences do not establish novelty because the genes have substantial prior annotation and literature, and co-abundance modules can capture transcriptional, cellular-composition, developmental, or indirect relationships rather than physical complexes. A stronger novelty claim would require replication in independent cohorts, preservation across datasets, adjustment for cell-type composition, and experimental testing of the proposed relationships.

**Hypothesis.** Hypothesis: the module reflects a coordinated cellular state in which VANGL2-linked developmental and polarity signaling is coupled indirectly to cytoskeletal organization, neuronal or glial identity, biosynthetic capacity, RNA and ribosome processing, chromatin regulation, and ER protein handling. POGLUT1 could connect developmental Notch-related glycosylation to this state, while PLEC and VAV2 could represent cytoskeletal and signaling outputs, and ASNS, ATAD2, PPAN, MDN1, and SKIC3 could reflect biosynthetic, proliferative, or RNA-maintenance demands. This is a hypothesis rather than an established pathway: the lack of globally significant GO or KEGG enrichment and the absence of high-confidence STRING and hu.MAP support require that it be tested through replication, cell-type deconvolution, perturbation, and measurements of protein or functional phenotypes.

### Important genes

#### VANGL2

- **Related proteins** (co-abundance neighbors): SKIC3 (0.86), PPAN (0.85), MDN1 (0.85), CIT (0.84), POGLUT1 (0.82), TAF5 (0.81), VAV2 (0.81), ATAD2 (0.80), MCFD2 (0.80), PLEC (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VANGL planar cell polarity protein 2. The protein encoded by this gene is a membrane protein involved in the regulation of planar cell polarity, especially in the stereociliary bundles of the cochlea. The encoded protein transmits directional signals to individual cells or groups of cells in epithelial sheets. This protein is also involved in the development of the neural plate. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: spina bifida (0.603); placental abruption (0.239); hereditary disease (0.192); Graves disease (0.123); breast cancer (0.106)
- **Europe PMC papers**: 2097
- **Why important**: VANGL2 is the clear network hub, connecting broadly across the module. Its established functions include planar cell polarity, neural tube closure, cell migration in development, and dopaminergic and serotonergic axon guidance. It has neural and astrocyte-related HPA cell-type annotations and a substantial literature, making it the strongest candidate for organizing the module's developmental and polarity interpretation.
- **Conclusion**: Established evidence supports VANGL2 as a biologically important polarity and neural-development protein and as the central co-abundance node. It is plausible, but not established, that VANGL2-related signaling helps organize the shared module.

#### CIT

- **Related proteins** (co-abundance neighbors): VANGL2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citron rho-interacting serine/threonine kinase. This gene encodes a serine/threonine-protein kinase that functions in cell division. Together with the kinesin KIF14, this protein localizes to the central spindle and midbody, and functions to promote efficient cytokinesis. This protein is involved in central nervous system development. Polymorphisms in this gene are associated with bipolar disorder and risk for schizophrenia. Alternative splicin…
- **Diseases (Open Targets)**: autosomal recessive primary microcephaly (0.773); neurodegenerative disease (0.554); hereditary disease (0.472); Primary microcephaly (0.464); atrial fibrillation (0.286)
- **Europe PMC papers**: 16815
- **Why important**: CIT is directly connected to VANGL2 and has a well-established role in cytokinesis, the central spindle, the midbody, actin organization, and nervous-system development. Its brain and neural cell-type enhancement and strong disease literature, including microcephaly and neurodevelopmental associations, make it important for linking the module to cellular division and neural development.
- **Conclusion**: Established evidence supports CIT as a cytokinesis and neurodevelopment gene with strong disease relevance. Its co-abundance with VANGL2 may indicate a shared developmental or proliferative cell state, but a direct functional partnership is not demonstrated.

#### SACS

- **Related proteins** (co-abundance neighbors): SKIC3 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sacsin molecular chaperone. This gene encodes the sacsin protein, which includes a UbL domain at the N-terminus, a DnaJ domain, and a HEPN domain at the C-terminus. The gene is highly expressed in the central nervous system, also found in skin, skeletal muscles and at low levels in the pancreas. This gene includes a very large exon spanning more than 12.8 kb. Mutations in this gene result in autosomal recessive spastic ataxi…
- **Diseases (Open Targets)**: Charlevoix-Saguenay spastic ataxia (0.851); autosomal recessive limb-girdle muscular dystrophy type 2C (0.583); Spastic paraplegia (0.573); hereditary spastic paraplegia (0.545); autosomal recessive limb-girdle muscular dystrophy (0.543)
- **Europe PMC papers**: 14737
- **Why important**: SACS is connected to SKIC3 and encodes a large molecular chaperone involved in protein folding and suppression of inclusion-body assembly. It is highly associated with the nervous system in the provided annotation, is enhanced in inhibitory neurons and muscle-related cell types, and has a strong connection to hereditary neurodegenerative disease.
- **Conclusion**: Established evidence supports SACS as a neuronal protein-homeostasis factor and a disease gene for hereditary spastic ataxia. Its presence may indicate proteostasis requirements in the shared cellular state, but the module does not establish a new SACS mechanism.

#### POGLUT1

- **Related proteins** (co-abundance neighbors): VANGL2 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein O-glucosyltransferase 1. This gene encodes a protein with both O-glucosyltransferase and O-xylosyltransferase activity which localizes to the lumen of the endoplasmic reticulum. This protein has a carboxy-terminal KTEL motif which is predicted to function as an endoplasmic reticulum retention signal. This gene is an essential regulator of Notch signalling and likely plays a role in cell fate and tissue formation during de…
- **Diseases (Open Targets)**: Dowling-Degos disease (0.706); autosomal recessive limb-girdle muscular dystrophy type 2U (0.696); neurodegenerative disease (0.522); autosomal recessive limb-girdle muscular dystrophy (0.370); hereditary disease (0.192)
- **Europe PMC papers**: 492
- **Why important**: POGLUT1 is linked directly to VANGL2 and encodes an ER-resident O-glycosyltransferase that regulates Notch signaling and tissue formation. Its functions provide a plausible molecular bridge between ER processing, developmental signaling, cell fate, and the neural or muscle-related context represented by other module genes. It also has established disease associations involving skin and muscle.
- **Conclusion**: Established evidence supports POGLUT1 as an ER glycosylation and Notch-regulatory protein with developmental importance. A role for POGLUT1 in coupling ER processing to the module's polarity signal is a reasonable hypothesis, not a demonstrated interaction.

#### ASNS

- **Related proteins** (co-abundance neighbors): ATAD2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: asparagine synthetase (glutamine-hydrolyzing). The protein encoded by this gene is involved in the synthesis of asparagine. This gene complements a mutation in the temperature-sensitive hamster mutant ts11, which blocks progression through the G1 phase of the cell cycle at nonpermissive temperature. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, May 2010].
- **Diseases (Open Targets)**: congenital microcephaly - severe encephalopathy - progressive cerebral atrophy syndrome (0.815); hereditary disease (0.468); Neurodevelopmental delay (0.425); Abnormal cerebral morphology (0.352); Neurodevelopmental abnormality (0.286)
- **Europe PMC papers**: 3627
- **Why important**: ASNS is connected to ATAD2 and encodes the enzyme responsible for asparagine synthesis. Its annotations include responses to glucose starvation, apoptosis regulation, and cell-cycle regulation, while HPA indicates pancreas and multiple neural or glial cell-type enhancement. Its disease associations include severe neurodevelopmental syndromes, giving it relevance to both metabolic support and neural vulnerability.
- **Conclusion**: Established evidence supports ASNS as a metabolic and stress-response enzyme with neurodevelopmental disease relevance. Its co-abundance may reflect biosynthetic demand or metabolic state in the shared cell populations, but the module does not prove that asparagine metabolism drives the network.

#### VAV2

- **Related proteins** (co-abundance neighbors): VANGL2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vav guanine nucleotide exchange factor 2. VAV2 is the second member of the VAV guanine nucleotide exchange factor family of oncogenes. Unlike VAV1, which is expressed exclusively in hematopoietic cells, VAV2 transcripts were found in most tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008].
- **Diseases (Open Targets)**: cutaneous leishmaniasis (0.503); open-angle glaucoma (0.448); glaucoma (0.373); type 2 diabetes mellitus (0.306); diabetes mellitus (0.301)
- **Europe PMC papers**: 2236
- **Why important**: VAV2 is a signaling and guanine-nucleotide-exchange factor connected to VANGL2. Its known functions include small-GTPase signaling, cell migration, immune-receptor signaling, and platelet activation. It is broadly expressed but shows enhancement in memory B cells, making it useful for evaluating whether a limited immune or cell-composition component contributes to the module.
- **Conclusion**: Established evidence supports VAV2 as a broadly expressed signaling regulator with immune-cell relevance. Its presence does not establish that the module is blood-derived; it instead raises a testable possibility that signaling or cell-composition effects contribute to the shared co-abundance pattern.

## Module 7

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (9)**: ATP13A1, CHD4, DDX10, NEFH, POLR1B, PDCD11, DARS2, RARS1, UGGT1

### Function

No GO or KEGG term passed global multiple-testing correction, and STRING reported no supplementary functional enrichment. The module therefore does not support a single statistically validated pathway. Its annotated genes span mitochondrial and cytosolic translation, endoplasmic-reticulum protein quality control, nucleolar ribosomal RNA transcription and processing, chromatin remodeling, and neuronal cytoskeletal structure. The strongest internal network structure is a nucleolar ribosome-biogenesis unit involving DDX10, PDCD11, and POLR1B, alongside a more connected DARS2-centered set linking mitochondrial translation with ATP13A1, UGGT1, RARS1, POLR1B, and CHD4. NEFH contributes a neuronal structural and axonal interpretation. Overall, the module is best viewed as a mixed cellular maintenance and biosynthetic state rather than evidence for one narrowly defined biological process.

**Cell composition.** The HPA profile does not indicate a plasma or broadly secreted module: only one gene is annotated as secreted, while the remainder are not secreted. Most genes have low tissue specificity and low immune-cell specificity, arguing against a module dominated by blood proteins or a general blood-cell signature. One gene is immune-cell enhanced in non-classical monocytes, but this isolated observation does not establish blood contamination. Cell-type-enhanced annotations are distributed across adipocytes, cardiomyocytes, glial populations, erythrocyte progenitors, germ-cell populations, and photoreceptors, with no common cell type dominating. NEFH has group-enriched expression in brain and prostate, but the target tissues have no matching HPA protein-detection data, so tissue-level protein expression in this comparison cannot be confirmed from the supplied evidence.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact set of known relationships rather than a uniformly connected module. DDX10, PDCD11, and POLR1B form the most strongly supported interaction cluster and are all linked to nucleolar RNA metabolism, with DDX10 and PDCD11 associated with ribosomal RNA processing and POLR1B with RNA polymerase I transcription. DARS2 and RARS1 have a supported interaction, consistent with aminoacyl-tRNA synthetase biology. The remaining co-abundance links, including those involving ATP13A1, UGGT1, CHD4, and NEFH, do not have corresponding high-confidence STRING partners in the supplied results. No hu.MAP complex contains multiple module members. Thus, the network combines a known nucleolar interaction core with additional co-abundance relationships that may reflect shared cellular state, indirect regulation, or tissue-composition effects rather than physical complex membership.

**STRING interactions (score >= 0.7)**: 4 of 36 gene pairs: DARS2–RARS1 (0.728); DDX10–PDCD11 (0.973); DDX10–POLR1B (0.858); PDCD11–POLR1B (0.977)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported cross-tissue co-abundance pattern, but the supplied evidence is insufficient to call it a new biological mechanism. The absence of a hu.MAP complex and the limited STRING connectivity do not prove novelty. Several component functions and relationships are already established, especially nucleolar ribosome biogenesis, aminoacyl-tRNA charging, chromatin remodeling, and neurofilament biology. What could be novel is the particular combination and co-abundance behavior of these genes across autonomic nervous system and cell-line samples. Establishing novelty would require comparison with published co-expression modules, independent cohorts, replication across datasets, and tests that distinguish cell composition from coordinated regulation.

**Hypothesis.** Hypothesis: the module reflects a shared cellular maintenance state coupling biosynthetic capacity with proteostasis, RNA production, and neuronal structural programs. In this model, DARS2 and RARS1 represent translation-related demand, UGGT1 and ATP13A1 represent protein-quality and membrane-protein homeostasis, while DDX10, PDCD11, and POLR1B represent increased nucleolar RNA processing and ribosome production. CHD4 could connect this state to transcriptional and chromatin regulation, and NEFH could indicate neuronal structural context or neuronal material in the samples. This hypothesis is not established by enrichment because no GO or KEGG term achieved global significance, and it should be tested by replication, cell-composition adjustment, and direct measurements of translation, nucleolar activity, proteostasis, and neuronal content.

### Important genes

#### DARS2

- **Related proteins** (co-abundance neighbors): UGGT1 (0.86), ATP13A1 (0.85), POLR1B (0.82), RARS1 (0.81), CHD4 (0.80); STRING partners: RARS1 (0.728)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 2, mitochondrial. The protein encoded by this gene belongs to the class-II aminoacyl-tRNA synthetase family. It is a mitochondrial enzyme that specifically aminoacylates aspartyl-tRNA. Mutations in this gene are associated with leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation (LBSL). [provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: leukoencephalopathy with brain stem and spinal cord involvement-high lactate syndrome (0.843); neurodegenerative disease (0.527); hereditary disease (0.518); hypertensive disorder (0.425); Cerebral cortical atrophy (0.425)
- **Europe PMC papers**: 796
- **Why important**: DARS2 is the most connected and strongest network hub in the module. It encodes a mitochondrial aspartyl-tRNA synthetase involved in mitochondrial translation, and its disease associations include leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation. It connects the aminoacyl-tRNA synthetase pair DARS2–RARS1 with genes involved in protein quality control, chromatin regulation, and nucleolar transcription. Its substantial literature base also makes it a comparatively well-characterized anchor for interpretation.
- **Conclusion**: Established: DARS2 supports mitochondrial aminoacyl-tRNA charging and has a documented neurological disease association. Its hub position supports a coordinating or state-marker role in this module. Hypothesis: variation in mitochondrial translational demand may help explain the module's cross-tissue co-abundance, but the network does not demonstrate that DARS2 regulates the other genes.

#### NEFH

- **Related proteins** (co-abundance neighbors): ATP13A1 (0.84), DDX10 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Immune cell enhanced; location Nuclear bodies, Centrosome, Basal body; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: neurofilament heavy chain. Neurofilaments are type IV intermediate filament heteropolymers composed of light, medium, and heavy chains. Neurofilaments comprise the axoskeleton and functionally maintain neuronal caliber. They may also play a role in intracellular transport to axons and dendrites. This gene encodes the heavy neurofilament protein. This protein is commonly used as a biomarker of neuronal damage and susceptibil…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2CC (0.660); Charcot-Marie-Tooth disease type 2 (0.555); amyotrophic lateral sclerosis (0.490); hereditary disease (0.342); Abnormality of the skeletal system (0.313)
- **Europe PMC papers**: 2092
- **Why important**: NEFH provides the clearest neuronal structural interpretation. It encodes the heavy neurofilament subunit, contributes to axonal caliber and transport, and is used as a marker of neuronal damage, with associations including amyotrophic lateral sclerosis and Charcot-Marie-Tooth disease. Its tissue-enriched brain annotation and connection to ATP13A1 and DDX10 make it important for assessing whether the module includes neuronal material or a neuronal maintenance component.
- **Conclusion**: Established: NEFH is a neuronal intermediate-filament protein and a disease-relevant marker of axonal pathology. Hypothesis: its presence may indicate neuronal structural content or axonal stress within the autonomic nervous system samples, but co-abundance alone cannot distinguish true regulation from differences in neuronal representation.

#### CHD4

- **Related proteins** (co-abundance neighbors): PDCD11 (0.81), DARS2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chromodomain helicase DNA binding protein 4. The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing result…
- **Diseases (Open Targets)**: Sifrim-Hitz-Weiss syndrome (0.810); neurodegenerative disease (0.551); hereditary disease (0.505); endometrial cancer (0.470); uterine carcinosarcoma (0.439)
- **Europe PMC papers**: 3617
- **Why important**: CHD4 is a highly connected module member and the principal chromatin-regulatory gene in the set. It is a core component of the nucleosome remodeling and deacetylase complex and is implicated in transcriptional repression, chromatin remodeling, DNA repair, cell-fate regulation, and disease including Sifrim-Hitz-Weiss syndrome and endometrial cancer. Its links to DARS2 and PDCD11 potentially connect cellular state regulation with nucleolar RNA metabolism.
- **Conclusion**: Established: CHD4 participates in chromatin remodeling and transcriptional repression and has recognized genetic and cancer associations. Hypothesis: CHD4 may help coordinate transcriptional adaptation to biosynthetic or proteostatic demand in this module, but the data do not establish a direct regulatory link to the nucleolar genes.

#### POLR1B

- **Related proteins** (co-abundance neighbors): DARS2 (0.82); STRING partners: DDX10 (0.858), PDCD11 (0.977)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli fibrillar center; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA polymerase I subunit B. Eukaryotic RNA polymerase I (pol I) is responsible for the transcription of ribosomal RNA (rRNA) genes and production of rRNA, the primary component of ribosomes. Pol I is a multisubunit enzyme composed of 6 to 14 polypeptides, depending on the species. Most of the mass of the pol I complex derives from the 2 largest subunits, Rpa1 and Rpa2 in yeast. POLR1B is homologous to Rpa2 (Seither and Grumm…
- **Diseases (Open Targets)**: Treacher Collins syndrome 4 (0.751); Treacher-Collins syndrome (0.383); arthropathy (0.212); Chronic Obstructive Asthma (0.188); lower respiratory tract disorder (0.124)
- **Europe PMC papers**: 521
- **Why important**: POLR1B is part of the known STRING-supported nucleolar interaction cluster with DDX10 and PDCD11. It encodes a subunit of RNA polymerase I, which transcribes ribosomal RNA, and is associated with Treacher Collins syndrome. Its position links the module to ribosome production and provides a mechanistic bridge between transcriptional output and the translation-related genes.
- **Conclusion**: Established: POLR1B is a core RNA polymerase I component required for ribosomal RNA transcription, and its relationships with DDX10 and PDCD11 are supported by STRING. Hypothesis: coordinated abundance of this nucleolar unit may indicate altered ribosome biogenesis, but there is no globally significant enrichment or direct activity measurement proving that interpretation in these samples.

#### PDCD11

- **Related proteins** (co-abundance neighbors): CHD4 (0.81); STRING partners: DDX10 (0.973), POLR1B (0.977)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: programmed cell death 11. PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008].
- **Diseases (Open Targets)**: Back pain (0.277); insomnia (0.216); systemic lupus erythematosus (0.170); neoplasm (0.095); colorectal carcinoma (0.093)
- **Europe PMC papers**: 334
- **Why important**: PDCD11 is a member of the strongest known interaction cluster in the module, connecting tightly with DDX10 and POLR1B. It is a nucleolar factor involved in precursor ribosomal RNA processing and generation of mature ribosomal RNA. Although it is less broadly studied than CHD4 or NEFH, its functional specificity and network placement make it a useful indicator of the nucleolar component.
- **Conclusion**: Established: PDCD11 participates in nucleolar ribosomal RNA maturation and has supported STRING relationships with DDX10 and POLR1B. Hypothesis: PDCD11 may report coordinated ribosome-biogenesis activity in the module, but its co-abundance with the other genes does not establish a causal role or a disease-specific mechanism.

## Module 8

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (12)**: BCL2, CD2AP, DPCD, GOLT1B, HSP90AB2P, MOGS, PNP, RTCA, RUVBL2, MPST, TWF1, VKORC1L1

### Function

No GO or KEGG term passed global correction, and STRING supplied no functional-enrichment result. The module is therefore best interpreted from its gene functions and network structure rather than as a statistically established pathway. Its central feature is BCL2-linked co-abundance with genes spanning apoptosis and mitochondrial biology, vesicle and endoplasmic-reticulum trafficking, actin and membrane organization, purine metabolism, sulfur metabolism, RNA processing, vitamin K metabolism, ciliary biology, and chromatin or DNA-repair machinery. The star-like structure indicates a coordinated expression pattern centered on BCL2, not a densely interconnected biochemical pathway. DPCD and RUVBL2 provide the clearest known molecular connection through STRING and hu.MAP, while the remaining edges should be treated primarily as co-abundance associations.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. Most annotated genes have low tissue specificity and low immune-cell specificity, arguing against a simple blood-cell or plasma-protein signature. Several genes show enhanced expression in specialized epithelial, reproductive, ciliated, adipocyte, or digestive cell populations, with DPCD and RUVBL2 particularly associated with ciliated and spermatogenic cell types. This heterogeneity suggests that the shared module may reflect broadly distributed cellular programs, sample composition, or shared cell states rather than a specific autonomic-nervous-system identity. The HPA protein-detection fields for both queried sample groups provide no usable tissue match.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports one high-confidence pair, DPCD–RUVBL2, whereas the other module edges lack listed STRING partners. hu.MAP independently places DPCD and RUVBL2 together in complexes (hu.MAP huMAP3_06881.1) through (hu.MAP huMAP3_14306.1), alongside RUVBL1 and components associated with chromatin remodeling, transcriptional regulation, DNA replication, DNA repair, and related nuclear assemblies. These repeated complexes make the DPCD–RUVBL2 relationship biologically credible and suggest that part of the module may track a nuclear or cilia-associated cellular program. However, only two module members occur in each listed complex, so hu.MAP does not establish that the whole module is one physical complex.

**STRING interactions (score >= 0.7)**: 1 of 66 gene pairs: DPCD–RUVBL2 (0.896)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06881.1 (DPCD, RUVBL2; 2/4); huMAP3_02648.1 (DPCD, RUVBL2; 2/7); huMAP3_07843.1 (DPCD, RUVBL2; 2/23); huMAP3_09291.1 (DPCD, RUVBL2; 2/27); huMAP3_14133.1 (DPCD, RUVBL2; 2/28); huMAP3_10481.1 (DPCD, RUVBL2; 2/40); huMAP3_14306.1 (DPCD, RUVBL2; 2/55)

### Novelty

The overall cross-tissue co-abundance module may represent a new observation, but the available evidence is insufficient to call it a new biological mechanism. The strongest internal relationship, DPCD–RUVBL2, is already supported by STRING and multiple hu.MAP complexes, so that component is not novel as a molecular association. Conversely, the BCL2-centered co-abundance pattern linking these genes is not supported by a corresponding STRING network or shared enriched GO or KEGG term in the fact sheet. Absence from those resources cannot prove novelty; it may reflect context-specific co-expression, incomplete database coverage, or a mixture of cell states. The defensible conclusion is that the module-level association is potentially novel and requires replication, while its individual molecular components are partly established.

**Hypothesis.** Hypothesis: the module represents a shared cell-state program coupling survival and stress buffering, centered on BCL2, with context-dependent contributions from membrane trafficking and actin remodeling, proteostasis and glycosylation, metabolic detoxification, RNA processing, and ciliary or chromatin-related functions. DPCD and RUVBL2 may mark a ciliated or reproductive-cell-associated nuclear program that becomes co-abundant with BCL2 in both sample groups. This model is provisional: the absence of globally significant GO or KEGG enrichment and the sparse network mean that coordinated expression, rather than a demonstrated common pathway, is the primary evidence.

### Important genes

#### BCL2

- **Related proteins** (co-abundance neighbors): GOLT1B (0.96), TWF1 (0.92), MOGS (0.91), MPST (0.90), DPCD (0.88), PNP (0.86), CD2AP (0.84), HSP90AB2P (0.84), RUVBL2 (0.84), VKORC1L1 (0.83), RTCA (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BCL2 apoptosis regulator. This gene encodes an integral outer mitochondrial membrane protein that blocks the apoptotic death of some cells such as lymphocytes. Constitutive expression of BCL2, such as in the case of translocation of BCL2 to Ig heavy chain locus, is thought to be the cause of follicular lymphoma. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016].
- **Diseases (Open Targets)**: B-cell chronic lymphocytic leukemia (0.740); neoplasm (0.605); diffuse large B-cell lymphoma (0.554); neurodegenerative disease (0.541); prostate carcinoma (0.533)
- **Europe PMC papers**: 83347
- **Why important**: BCL2 is the dominant network hub, connected to every other module member with the strongest overall weighted connectivity. Its established function is inhibition of apoptosis through an integral mitochondrial outer-membrane protein, and its annotations include cytochrome-c release, apoptosis, and DNA-damage response. It also has extensive literature and disease associations including lymphoid malignancy and neurodegenerative disease, making it the most influential candidate for interpreting the module.
- **Conclusion**: Established evidence supports BCL2 as the network's central survival-associated gene and as a plausible marker of cellular stress or survival state. It is not established that BCL2 mechanistically drives the co-abundance of the other genes; that causal interpretation remains a hypothesis.

#### DPCD

- **Related proteins** (co-abundance neighbors): BCL2 (0.88); STRING partners: RUVBL2 (0.896)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm, Vesicles; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06881.1, huMAP3_02648.1, huMAP3_07843.1, huMAP3_09291.1, huMAP3_14133.1, huMAP3_10481.1, huMAP3_14306.1
- **Function (MyGene.info)**: deleted in primary ciliary dyskinesia homolog (mouse). This gene in mouse encodes a protein that may be involved in the generation and maintenance of ciliated cells. In mouse, expression of this gene increases during ciliated cell differentiation, and disruption of this gene has been linked to primary ciliary dyskinesia. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.309); atrial fibrillation (0.248); ulcerative colitis (0.169); uterine corpus leiomyoma (0.149); Kartagener Syndrome (0.050)
- **Europe PMC papers**: 267
- **Why important**: DPCD is connected to the BCL2 hub and is the only module gene paired with RUVBL2 by a high-confidence STRING interaction. It occurs with RUVBL2 in every listed hu.MAP complex, and its annotations connect it to generation and maintenance of ciliated cells and primary ciliary dyskinesia. HPA evidence links it to choroid plexus, testis, spermatogenic cells, and several ciliated-cell populations, giving it a distinctive cellular-context signal despite its modest network degree.
- **Conclusion**: Established evidence supports DPCD as the module's clearest cilia-associated and complex-supported marker. Its co-abundance with BCL2 may indicate a shared ciliated-cell or differentiation state, but the fact sheet does not establish a direct DPCD–BCL2 mechanism.

#### RUVBL2

- **Related proteins** (co-abundance neighbors): BCL2 (0.84); STRING partners: DPCD (0.896)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06881.1, huMAP3_02648.1, huMAP3_07843.1, huMAP3_09291.1, huMAP3_14133.1, huMAP3_10481.1, huMAP3_14306.1
- **Function (MyGene.info)**: RuvB like AAA ATPase 2. This gene encodes the second human homologue of the bacterial RuvB gene. Bacterial RuvB protein is a DNA helicase essential for homologous recombination and DNA double-strand break repair. Functional analysis showed that this gene product has both ATPase and DNA helicase activities. This gene is physically linked to the CGB/LHB gene cluster on chromosome 19q13.3, and is very close (55 nt) to the L…
- **Diseases (Open Targets)**: hypogonadotropic hypogonadism 23 with or without anosmia (0.500); neurodegenerative disease (0.273); hypogonadotropic hypogonadism (0.118); hepatocellular carcinoma (0.102); neoplasm (0.093)
- **Europe PMC papers**: 1413
- **Why important**: RUVBL2 is connected to BCL2 and forms the module's strongest externally supported pair with DPCD. Its participation in multiple hu.MAP complexes places it in assemblies related to chromatin remodeling, DNA replication, DNA repair, telomere maintenance, and RNA-complex assembly. HPA evidence associates it with testis, spermatogenic cells, and ciliated cell types, providing a plausible cellular bridge to DPCD.
- **Conclusion**: Established evidence supports RUVBL2 as a multifunctional nuclear ATPase and as a credible partner of DPCD. Its role as a mediator of the entire BCL2-centered module is not established and should be tested with independent interaction or perturbation data.

#### CD2AP

- **Related proteins** (co-abundance neighbors): BCL2 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD2 associated protein. This gene encodes a scaffolding molecule that regulates the actin cytoskeleton. The protein directly interacts with filamentous actin and a variety of cell membrane proteins through multiple actin binding sites, SH3 domains, and a proline-rich region containing binding sites for SH3 domains. The cytoplasmic protein localizes to membrane ruffles, lipid rafts, and the leading edges of cells. It is i…
- **Diseases (Open Targets)**: familial idiopathic steroid-resistant nephrotic syndrome (0.701); focal segmental glomerulosclerosis (0.585); Alzheimer disease (0.493); dementia (0.395); Abnormality of the skeletal system (0.314)
- **Europe PMC papers**: 3461
- **Why important**: CD2AP is a BCL2-linked peripheral member with a well-described scaffolding role in actin organization, membrane trafficking, receptor endocytosis, migration, secretion, and synapse organization. Its disease associations include kidney disease and neurodegenerative disease, which are relevant to cellular barrier and neuronal contexts. HPA places it in enterocytes and plasmacytoid dendritic cells, while its membrane localization gives the module a plausible interface between intracellular survival and cell-surface organization.
- **Conclusion**: Established evidence supports CD2AP as an actin and membrane-trafficking scaffold that could report cell architecture or cellular composition. A direct functional connection to BCL2 or to the DPCD–RUVBL2 complexes is not established.

#### MPST

- **Related proteins** (co-abundance neighbors): BCL2 (0.90); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mercaptopyruvate sulfurtransferase. This protein encoded by this gene catalyzes the transfer of a sulfur ion from 3-mercaptopyruvate to cyanide or other thiol compounds. It may be involved in cysteine degradation and cyanide detoxification. There is confusion in literature between this protein (mercaptopyruvate sulfurtransferase, MPST), which appears to be cytoplasmic, and thiosulfate sulfurtransferase (rhodanese, TST, GeneID:7263),…
- **Diseases (Open Targets)**: neurodegenerative disease (0.261); COVID-19 (0.164); severe acute respiratory syndrome (0.163); colitis (0.080); non-alcoholic fatty liver (0.078)
- **Europe PMC papers**: 1532
- **Why important**: MPST is a BCL2-linked mitochondrial enzyme involved in sulfur-amino-acid catabolism, cyanide detoxification, and responses to toxic substances. Its HPA profile is tissue enhanced in liver and cell-type enhanced across enteric and epithelial populations, while its disease associations include neurodegenerative and metabolic-inflammatory conditions. It therefore offers a biologically distinct readout of redox, sulfur, and detoxification state within the otherwise mixed module.
- **Conclusion**: Established evidence supports MPST as a metabolic and stress-response component. Its presence may indicate a redox or detoxification dimension of the co-abundance pattern, but no direct mechanistic link to BCL2, DPCD, or RUVBL2 is demonstrated.

## Module 9

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (14)**: CDC73, COPB1, DDX46, DDX6, DIAPH1, POLA1, HSPBP1, MTCL3, POLR1A, POLR2A, SLC25A13, SEC24C, SUPT5H, THOP1

### Function

The module most strongly suggests a transcription and RNA-processing program centered on nuclear RNA polymerase machinery. This interpretation is supported by the direct STRING relationships among POLR2A, CDC73, and SUPT5H, the supplementary STRING nuclear DNA-directed RNA polymerase complex terms (STRING COMPARTMENTS Nuclear DNA-directed RNA polymerase complex; within-query FDR = 0.0278) and (STRING Component Nuclear DNA-directed RNA polymerase complex; within-query FDR = 0.0381), and the repeated hu.MAP associations linking these genes to RNA polymerase and transcription-elongation complexes (hu.MAP huMAP3_11092.1) through (hu.MAP huMAP3_14318.1). POLR2A represents the catalytic core of messenger-RNA transcription, POLR1A represents ribosomal-RNA transcription, SUPT5H supports RNA polymerase II elongation, and CDC73 connects transcription with post-transcriptional control. DDX6 adds an RNA surveillance and decay component, while DDX46 contributes a splicing-related connection. The GO and KEGG analysis provides no globally significant term: no GO or KEGG term passed global correction. The functional interpretation therefore rests on convergent gene functions, network structure, STRING evidence, and hu.MAP complexes rather than on a globally significant enrichment term.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the secreted-gene count is zero, and the proteins are predominantly nuclear, cytoplasmic, mitochondrial, Golgi, vesicular, or membrane associated. The HPA profile is mainly low tissue specificity, with some tissue-enhanced or tissue-enriched signals in brain, lymphoid tissue, and liver. Several genes show cell-type-enhanced patterns involving oligodendrocytes, choroid plexus epithelial cells, neutrophils, neutrophil progenitors, platelets, erythrocyte progenitors, and gastrointestinal or ciliated epithelial cells. However, the module has low immune-cell specificity overall, with some genes not detected in immune cells, and no frequent enriched blood-cell category was reported. Thus, the shared signal is more consistent with a broadly distributed cellular machinery program, with possible contributions from particular cell types, than with a simple plasma, blood-cell, or secreted-protein signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a known transcriptional core: CDC73 is very strongly connected to POLR2A and SUPT5H, POLR2A is strongly connected to DDX6, and POLR1A has a moderate connection to HSPBP1. The COPB1–SEC24C relationship supports a separate vesicle-trafficking pair. The supplementary STRING compartment and component terms (STRING COMPARTMENTS Nuclear DNA-directed RNA polymerase complex; within-query FDR = 0.0278) and (STRING Component Nuclear DNA-directed RNA polymerase complex; within-query FDR = 0.0381) identify POLR1A, CDC73, POLA1, and POLR2A in a nuclear DNA-directed RNA polymerase complex, but these are not globally corrected enrichment results. hu.MAP independently recovers repeated complexes containing SUPT5H, CDC73, and POLR2A, together with broader polymerase and transcription-elongation machinery (hu.MAP huMAP3_11092.1) through (hu.MAP huMAP3_07749.1), and complexes containing POLR1A and POLR2A (hu.MAP huMAP3_08487.1) through (hu.MAP huMAP3_14318.1). These relationships indicate that a substantial part of the module corresponds to established physical or complex-level biology. The remaining edges, especially those involving MTCL3, DDX46, DIAPH1, POLA1, HSPBP1, SLC25A13, THOP1, SEC24C, and COPB1, are less directly supported by STRING or hu.MAP and may reflect co-abundance, indirect regulation, shared cellular state, or tissue composition rather than direct physical interaction.

**STRING interactions (score >= 0.7)**: 6 of 91 gene pairs: CDC73–POLR2A (0.999); CDC73–SUPT5H (0.999); COPB1–SEC24C (0.714); DDX6–POLR2A (0.963); HSPBP1–POLR1A (0.741); POLR2A–SUPT5H (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Nuclear DNA-directed RNA polymerase complex (FDR = 0.0278, 4 genes); Component Nuclear DNA-directed RNA polymerase complex (FDR = 0.0381, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11092.1 (SUPT5H, POLR1A, POLR2A, CDC73; 4/65); huMAP3_09843.1 (SUPT5H, POLR2A, CDC73; 3/29); huMAP3_07948.1 (SUPT5H, CDC73; 2/9); huMAP3_11018.1 (SUPT5H, CDC73; 2/15); huMAP3_12111.1 (SUPT5H, CDC73; 2/16); huMAP3_07454.1 (SUPT5H, CDC73; 2/27); huMAP3_07749.1 (SUPT5H, CDC73; 2/28); huMAP3_08487.1 (POLR1A, POLR2A; 2/37); huMAP3_06426.1 (POLR1A, POLR2A; 2/38); huMAP3_14318.1 (POLR1A, POLR2A; 2/58)

### Novelty

The module should not be described as a wholly new molecular complex. Its central POLR2A–CDC73–SUPT5H structure and its polymerase-associated organization are already represented in STRING and hu.MAP, so the core biology is established. A potentially novel aspect is the specific co-abundance combination across autonomic nervous system and cell-line samples, particularly the linkage of the established transcriptional core with vesicle-trafficking genes, RNA decay or splicing factors, mitochondrial transport, cytoskeletal regulation, and MTCL3. However, absence of some module relationships from STRING or hu.MAP does not prove novelty. Establishing a new finding would require replication in independent datasets, control for cell composition and expression breadth, and experimental or orthogonal evidence for the less-established connections.

**Hypothesis.** Hypothesis: the conserved module reflects a shared cellular state in which transcriptional output and RNA handling are coordinated with protein trafficking, organelle function, and cytoskeletal or stress responses. In this model, the POLR2A–SUPT5H–CDC73 axis represents active transcription and elongation, DDX6 and DDX46 regulate downstream RNA fate, POLA1 marks replication or repair competence, SEC24C and COPB1 support secretory-pathway trafficking, SLC25A13 supports mitochondrial metabolite exchange, and MTCL3 may act as a tissue- or cell-state-linked scaffold connecting otherwise distinct processes. The cross-tissue conservation could arise from a broadly shared housekeeping or proliferative state, with additional modulation by neural, epithelial, or hematopoietic cell composition. This is a mechanistic hypothesis, not a demonstrated physical pathway.

### Important genes

#### POLR2A

- **Related proteins** (co-abundance neighbors): DDX6 (0.86), POLR1A (0.83), SEC24C (0.82), COPB1 (0.81), MTCL3 (0.81); STRING partners: CDC73 (0.999), DDX6 (0.963), SUPT5H (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11092.1, huMAP3_09843.1, huMAP3_08487.1, huMAP3_06426.1, huMAP3_14318.1
- **Function (MyGene.info)**: RNA polymerase II subunit A. This gene encodes the largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a carboxy terminal domain composed of heptapeptide repeats that are essential for polymerase activity. These repeats contain serine and threonine residues that are phosphorylated in actively transcribing RNA polymerase. In addition, …
- **Diseases (Open Targets)**: neurodevelopmental disorder with hypotonia and variable intellectual and behavioral abnormalities (0.738); HIV infectious disease (0.600); hereditary disease (0.479); syndromic intellectual disability (0.462); Orthomyxoviridae infectious disease (0.374)
- **Europe PMC papers**: 4546
- **Why important**: POLR2A is a central network gene and the catalytic subunit of RNA polymerase II, which synthesizes messenger RNA. It connects directly to DDX6 and is part of the strongest established transcriptional relationships with CDC73 and SUPT5H in STRING. It also appears in multiple hu.MAP polymerase and transcription complexes (hu.MAP huMAP3_11092.1), (hu.MAP huMAP3_09843.1), and (hu.MAP huMAP3_08487.1) through (hu.MAP huMAP3_14318.1). Its disease associations include neurodevelopmental and intellectual-disability phenotypes, and its literature volume is substantial, making it the strongest anchor for the module's transcriptional interpretation.
- **Conclusion**: Established evidence supports POLR2A as a core transcriptional component and a principal organizing gene of the module. The module data do not establish that POLR2A directly drives the cross-tissue co-abundance pattern; that causal role remains a hypothesis.

#### CDC73

- **Related proteins** (co-abundance neighbors): MTCL3 (0.85); STRING partners: POLR2A (0.999), SUPT5H (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11092.1, huMAP3_09843.1, huMAP3_07948.1, huMAP3_11018.1, huMAP3_12111.1, huMAP3_07454.1, huMAP3_07749.1
- **Function (MyGene.info)**: cell division cycle 73. This gene encodes a tumor suppressor that is involved in transcriptional and post-transcriptional control pathways. The protein is a component of the the PAF protein complex, which associates with the RNA polymerase II subunit POLR2A and with a histone methyltransferase complex. This protein appears to facilitate the association of 3' mRNA processing factors with actively-transcribed chromatin. Mu…
- **Diseases (Open Targets)**: hyperparathyroidism 2 with jaw tumors (0.810); parathyroid gland carcinoma (0.802); familial isolated hyperparathyroidism (0.738); hyperparathyroidism (0.599); hereditary neoplastic syndrome (0.555)
- **Europe PMC papers**: 2210
- **Why important**: CDC73 has highly supported STRING relationships with POLR2A and SUPT5H and occurs repeatedly in hu.MAP complexes (hu.MAP huMAP3_11092.1) through (hu.MAP huMAP3_07749.1). It links RNA polymerase II to transcriptional and post-transcriptional control through the PAF-associated machinery. Its tumor-suppressor function and associations with hyperparathyroidism and parathyroid neoplasia give it clear disease relevance, while its literature volume is substantial.
- **Conclusion**: Established evidence supports CDC73 as a bridge between transcription elongation and RNA processing within the module. The data support a regulatory interpretation, but they do not show that CDC73 mutations or activity explain the observed co-abundance in these tissue groups.

#### SUPT5H

- **Related proteins** (co-abundance neighbors): DDX6 (0.81); STRING partners: CDC73 (0.999), POLR2A (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11092.1, huMAP3_09843.1, huMAP3_07948.1, huMAP3_11018.1, huMAP3_12111.1, huMAP3_07454.1, huMAP3_07749.1
- **Function (MyGene.info)**: SPT5 homolog, DSIF elongation factor subunit. Enables enzyme binding activity and protein heterodimerization activity. Involved in positive regulation of macroautophagy; regulation of RNA metabolic process; and transcription elongation from RNA polymerase II promoter. Located in nucleoplasm. Part of DSIF complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: HIV infectious disease (0.593); neoplasm (0.084); malignant colon neoplasm (0.081); colonic neoplasm (0.081); autosomal recessive spondylocostal dysostosis (0.075)
- **Europe PMC papers**: 707
- **Why important**: SUPT5H is a transcription-elongation factor and a recurring member of the hu.MAP complexes (hu.MAP huMAP3_11092.1) through (hu.MAP huMAP3_07749.1). Its very strong STRING relationships with CDC73 and POLR2A provide direct support for the central elongation machinery. Its annotation links it to RNA polymerase II elongation and RNA metabolic regulation, and its disease and neoplasm associations provide additional biological context.
- **Conclusion**: Established evidence supports SUPT5H as a core elongation component of the conserved module. It is plausible that coordinated SUPT5H abundance reflects transcriptional state, but the module does not demonstrate a specific target-gene program or a direct tissue-specific mechanism.

#### DDX6

- **Related proteins** (co-abundance neighbors): POLR2A (0.86), SEC24C (0.83), THOP1 (0.82), SUPT5H (0.81); STRING partners: POLR2A (0.963)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytoplasmic bodies; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DEAD-box helicase 6. This gene encodes a member of the DEAD box protein family. The protein is an RNA helicase found in P-bodies and stress granules, and functions in translation suppression and mRNA degradation. It is required for microRNA-induced gene silencing. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Mar 2012].
- **Diseases (Open Targets)**: intellectual developmental disorder with impaired language and dysmorphic facies (0.650); Intellectual disability (0.555); neurodegenerative disease (0.459); lung carcinoma (0.371); Global developmental delay (0.371)
- **Europe PMC papers**: 3002
- **Why important**: DDX6 occupies a relatively central position in the module and connects POLR2A, SEC24C, THOP1, and SUPT5H. It is an RNA helicase involved in P-body function, translation suppression, messenger-RNA decapping, deadenylation-dependent decay, and microRNA-mediated silencing. Its extensive literature and associations with intellectual disability, neurodevelopmental disease, and neurodegeneration make it important for interpreting the module as coordinated transcription and RNA fate rather than transcription alone.
- **Conclusion**: Established evidence supports DDX6 as an RNA surveillance and post-transcriptional regulator linked to the transcriptional core through the module network and a STRING relationship with POLR2A. The data do not establish direct binding between DDX6 and every module component or prove that RNA decay is the primary driver.

#### SEC24C

- **Related proteins** (co-abundance neighbors): DDX6 (0.83), POLR2A (0.82), COPB1 (0.82); STRING partners: COPB1 (0.714)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC24 homolog C, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The product of this gene may play a role in shaping the vesicle, as well as in cargo selection and concentration.…
- **Diseases (Open Targets)**: 22q11.2 deletion syndrome (0.370); neurodegenerative disease (0.369); Alzheimer disease (0.281); lysosomal storage disease (0.274); Parkinson disease (0.274)
- **Europe PMC papers**: 693
- **Why important**: SEC24C connects the transcription-associated POLR2A neighborhood to COPB1 and DDX6 in the co-abundance network. It is a COPII component involved in cargo selection and endoplasmic-reticulum-to-Golgi transport, and its relationship with COPB1 is supported by STRING. Its disease associations include chromosomal deletion syndromes and neurodegenerative conditions, while its moderate literature volume supports a well-established trafficking role.
- **Conclusion**: Established evidence supports SEC24C as a vesicle-trafficking component and COPB1 partner within the module. Its connection to the nuclear transcriptional core is not established as a physical interaction and may represent coordinated cellular state, indirect regulation, or sample-composition effects.

## Module 10

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (5)**: LLPH, RAB39A, IARS2, UQCRFS1, WDR12

### Function

The module is most consistent with a heterogeneous intracellular maintenance program centered on RAB39A-linked vesicle and lysosome biology, with accompanying mitochondrial translation, respiratory-chain, neuronal-structural, and ribosome-biogenesis functions. RAB39A is the sole network hub, connected to every other module member, while the remaining genes are peripheral and are not connected to one another. The gene annotations support roles in autophagosome–lysosome fusion, phagosome maturation and acidification, mitochondrial protein synthesis, respiratory electron transport, dendritic development, and rRNA processing. However, no GO or KEGG term passed global correction, and there was no supplementary STRING functional-enrichment result. Thus, the functional interpretation is hypothesis-generating rather than evidence of a single statistically established pathway. The external RAB39A literature supports a role for RAB39A in HOPS-dependent autophagosome–lysosome fusion and in phagosome maturation, including antigen presentation, but those findings do not establish direct physical association with the other module genes.

**Cell composition.** The module does not have the profile of a plasma-protein or secreted-protein module: none of the genes is annotated as secreted. Most members have low tissue specificity, and most have low immune-cell specificity, arguing against a simple blood-cell or broadly shared immune signature. Nevertheless, HPA annotations are heterogeneous: RAB39A is tissue-enhanced in brain and lymphoid tissue and is immune-cell enhanced in intermediate monocytes; UQCRFS1 is tissue-enhanced in skeletal muscle and tongue; and several genes show cell-type-enhanced expression in distinct cell populations. The appearance of adrenal medulla cells among the RAB39A-associated cell types is compatible with relevance to autonomic tissues, but the mixed HPA pattern also cautions that the shared module may reflect cellular composition or general intracellular state rather than a tissue-specific autonomic mechanism. The absence of matching HPA protein data for the two tissues limits protein-level interpretation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied confidence threshold, and no STRING functional-enrichment result was reported. No hu.MAP complex contained multiple module members. Therefore, the co-abundance edges should not be presented as known protein–protein interactions or as a recognized multiprotein complex. Known biology exists for individual members: RAB39A participates in lysosomal and phagosomal trafficking, UQCRFS1 is a component of mitochondrial respiratory complex III and is also associated with complex IV in the supplied annotation, IARS2 supports mitochondrial translation, LLPH has annotations related to dendrite extension and dendritic-spine development, and WDR12 participates in ribosome biogenesis. The lack of STRING and hu.MAP support means that the observed co-abundance pattern is not explained by an already catalogued physical complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is a potentially novel co-abundance association, but it is not sufficient to claim discovery of a new biochemical pathway. The module has no globally significant GO or KEGG enrichment, no supplementary STRING enrichment, no high-confidence STRING pair, and no multi-member hu.MAP complex. Its novelty therefore lies mainly in the cross-tissue co-abundance configuration and in the unusual combination of RAB39A with mitochondrial, nucleolar, neuronal, and ribosome-related genes. Absence from interaction databases alone does not prove novelty: the pattern could reflect coordinated cell composition, shared stress or organelle state, indirect regulation, or limited database coverage. Independent replication, tissue-cell deconvolution, and perturbation experiments would be needed before treating it as a new mechanism.

**Hypothesis.** Hypothesis: in autonomic nervous system and cell-line samples, variation in a RAB39A-dependent endolysosomal or phagosomal trafficking state may covary with cellular demands for mitochondrial translation and respiration, ribosome production, and neuronal structural maintenance. RAB39A could act as the most prominent state marker, while IARS2, UQCRFS1, LLPH, and WDR12 report different downstream aspects of organelle and biosynthetic demand. This is a coordinated-state hypothesis, not evidence that the five proteins form a physical complex. A testable prediction is that perturbing RAB39A trafficking or lysosome function will alter the abundance or activity of the mitochondrial, ribosome-biogenesis, and neuronal-maintenance programs, while controlling for cell-type composition.

Web sources: https://www.nature.com/articles/s41467-023-42003-0; https://www.uniprot.org/uniprotkb/Q14964/entry; https://link.springer.com/article/10.15252/embj.2019102020; https://pmc.ncbi.nlm.nih.gov/articles/PMC6480249/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3862771/

### Important genes

#### RAB39A

- **Related proteins** (co-abundance neighbors): IARS2 (0.88), UQCRFS1 (0.83), LLPH (0.81), WDR12 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB39A, member RAS oncogene family. Predicted to enable GTPase activity. Involved in phagosome acidification and phagosome-lysosome fusion. Located in phagocytic vesicle. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: anemia (phenotype) (0.194); cancer (0.080); placental abruption (0.040); breast carcinoma (0.029); neoplasm (0.024)
- **Europe PMC papers**: 421
- **Why important**: RAB39A is the network hub and has the strongest central position in the module. Its curated functions include vesicle-mediated transport, phagosome acidification, phagosome–lysosome fusion, and autophagosome–lysosome fusion. It is also the member with brain, lymphoid-tissue, adrenal-medulla, dendritic-cell, and monocyte-related HPA signals. The literature volume is substantial, and external studies support roles in HOPS-mediated lysosomal tethering and phagosome maturation.
- **Conclusion**: Established evidence: RAB39A is the principal network marker and has a well-supported role in endolysosomal and phagosomal trafficking. Hypothesis: its centrality reflects a biological organizing process for the module rather than merely a statistical hub. The module data do not establish that RAB39A directly regulates the other four genes.

#### UQCRFS1

- **Related proteins** (co-abundance neighbors): RAB39A (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquinol-cytochrome c reductase, Rieske iron-sulfur polypeptide 1. Predicted to enable oxidoreductase activity. Involved in mitochondrial respiratory chain complex III assembly and respiratory electron transport chain. Located in mitochondrion. Part of mitochondrial respiratory chain complex III and mitochondrial respiratory chain complex IV. Implicated in mitochondrial complex III deficiency. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: mitochondrial complex III deficiency, nuclear type 10 (0.745); neurodegenerative disease (0.484); cardiomyopathy (0.427); lactic acidosis (0.426); propionic acidemia (0.425)
- **Europe PMC papers**: 1748
- **Why important**: UQCRFS1 is the strongest mitochondrial respiratory candidate in the module. It is annotated as a Rieske iron-sulfur component of respiratory complex III, involved in respiratory electron transport and complex III assembly, and associated with mitochondrial complex III deficiency. It has the largest literature volume among the module genes and is tissue-enhanced in skeletal muscle and tongue, with cell-type enhancement in several metabolically active cell populations.
- **Conclusion**: Established evidence: UQCRFS1 is a core mitochondrial respiratory-chain component with disease relevance. Hypothesis: its co-abundance with RAB39A may indicate coupling between endolysosomal trafficking and cellular energy demand. The module does not prove such coupling or a direct interaction.

#### IARS2

- **Related proteins** (co-abundance neighbors): RAB39A (0.88); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: isoleucyl-tRNA synthetase 2, mitochondrial. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAS, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Two forms of isoleucine-tRNA synthetase exist, a cytoplasmic form and a mitochondrial form. This gene encodes th…
- **Diseases (Open Targets)**: cataract-growth hormone deficiency-sensory neuropathy-sensorineural hearing loss-skeletal dysplasia syndrome (0.724); Leigh syndrome (0.563); hereditary disease (0.416); neurodegenerative disease (0.411); mitochondrial disease (0.374)
- **Europe PMC papers**: 411
- **Why important**: IARS2 encodes the mitochondrial isoleucine-tRNA synthetase and is annotated for mitochondrial translation, tRNA aminoacylation, and translational fidelity. It is broadly expressed according to HPA and has disease associations involving mitochondrial and neurodevelopmental phenotypes. Although peripheral in the graph, its mitochondrial location gives it a coherent functional link to UQCRFS1 at the level of organelle maintenance, even though those genes are not directly connected in the module.
- **Conclusion**: Established evidence: IARS2 supports accurate mitochondrial protein synthesis and is associated with mitochondrial disease biology. Hypothesis: IARS2 may mark the mitochondrial translation component of a broader cellular state represented alongside RAB39A. The co-abundance data do not establish that RAB39A trafficking controls IARS2.

#### LLPH

- **Related proteins** (co-abundance neighbors): RAB39A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: LLP homolog, long-term synaptic facilitation factor. Enables RNA binding activity. Predicted to be involved in dendrite extension and positive regulation of dendritic spine development. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dementia (0.287); hemorrhoid (0.223); aortic stenosis (0.190); insomnia (0.167); medical procedure (0.165)
- **Europe PMC papers**: 140
- **Why important**: LLPH contributes a neuronal and RNA-related dimension. It is annotated for RNA binding, dendrite extension, and positive regulation of dendritic-spine development, and HPA identifies cell-type enhancement in late primary spermatocytes rather than a uniform tissue pattern. Its literature volume is more limited than that of the major mitochondrial and trafficking genes, which makes it potentially informative as a less-characterized module component.
- **Conclusion**: Established evidence: LLPH has curated links to dendritic development and RNA-related biology. Hypothesis: LLPH may connect the module to neuronal structural maintenance or a broader differentiation state. This interpretation is tentative because it lacks enrichment support and direct network or complex evidence.

#### WDR12

- **Related proteins** (co-abundance neighbors): RAB39A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: WD repeat domain 12. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); poisoning (0.233); non-autoimmune hemolytic anemia (0.214); coronary artery disorder (0.210); myocardial infarction (0.168)
- **Europe PMC papers**: 602
- **Why important**: WDR12 is annotated for rRNA processing, ribosome biogenesis, large-subunit maturation, and cell-cycle regulation. Its WD-repeat architecture is compatible with participation in multiprotein assemblies, but no hu.MAP complex containing another module member was identified. It has disease associations spanning neurodegenerative and cardiovascular phenotypes and provides a biosynthetic and nucleolar perspective distinct from the trafficking and mitochondrial genes.
- **Conclusion**: Established evidence: WDR12 is a ribosome-biogenesis factor with broad cellular relevance. Hypothesis: its co-abundance may report variation in biosynthetic capacity that accompanies the RAB39A-associated state. The module does not show that WDR12 is part of a RAB39A complex or that the two proteins directly regulate each other.

## Module 11

**Tissue pair**: autonomic_nervous_system and cell line  
**Genes (5)**: PHIP, PI4KA, PRKDC, RSL1D1, SUPV3L1

### Function

No GO or KEGG term passed global correction, so the module does not support a formally established pathway-level annotation. Its genes nevertheless suggest a heterogeneous intracellular program involving DNA double-strand-break repair and innate immune signaling through PRKDC, phosphoinositide biosynthesis and signaling through PI4KA, RNA and ribosome-associated regulation through RSL1D1, mitochondrial RNA surveillance through SUPV3L1, and signal-transduction, chromatin, and growth regulation through PHIP. The co-abundance structure is sparse and should therefore be interpreted as a candidate coordinated state rather than proof of a single biochemical pathway. The supplementary STRING result (STRING SMART Phosphoinositide 3-kinase, catalytic domain; within-query FDR = 0.0325) linking PRKDC and PI4KA through a phosphoinositide-kinase catalytic-domain annotation is compatible with a kinase-centered interpretation, but it is not globally corrected enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: all genes are annotated as non-secreted intracellular proteins. It is also not broadly characterized as blood-cell specific, because every gene has low immune-cell specificity in HPA. Most genes have low tissue specificity, with PI4KA being tissue enhanced in brain and cell-type enhancement reported for PI4KA in pDCs and for PRKDC in erythrocyte progenitors and neutrophils. These isolated cell-type signals do not establish a blood-derived module, although shared cell composition or cellular-state effects remain possible. HPA provides no matching protein-detection evidence for either target tissue group, so protein-level expression in autonomic nervous system and cell line samples cannot be confirmed from this summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only supplied STRING functional signal is (STRING SMART Phosphoinositide 3-kinase, catalytic domain; within-query FDR = 0.0325), involving PRKDC and PI4KA and a phosphoinositide-kinase catalytic-domain annotation. The high-confidence STRING network contains no reported pairwise interactions among the module genes, and hu.MAP reports no complex containing multiple module members. Thus, the PRKDC–PI4KA relationship is the only explicitly supported connection from the interaction resources, and even that relationship is supplementary rather than globally corrected evidence. The abundance edges may therefore reflect coordinated regulation, shared cellular state, indirect biology, or dataset-specific covariance rather than a known physical complex. The remaining annotations point to distinct nuclear, nucleolar, mitochondrial, and signaling functions.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Phosphoinositide 3-kinase, catalytic domain (FDR = 0.0325, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This is best described as a potentially novel co-abundance association, not as a newly established molecular complex or pathway. The combination is notable because the module is shared between autonomic nervous system and cell line, yet it lacks a multi-member hu.MAP complex and lacks high-confidence STRING pairwise support. That pattern favors novelty at the level of cross-tissue co-abundance rather than novelty of the individual genes or their canonical functions. The absence of STRING or hu.MAP support alone does not prove novelty; independent replication, preservation in additional cohorts, control for cell composition, and experimental testing would be required.

**Hypothesis.** Hypothesis: the module may mark a coordinated intracellular stress or growth state in which PI4KA-dependent phosphoinositide signaling covaries with PRKDC-mediated genome surveillance, while PHIP links signaling to chromatin and transcriptional regulation and RSL1D1 and SUPV3L1 reflect coupled RNA-processing and quality-control demands. A possible explanation for sharing between autonomic nervous system and cell line is a conserved proliferative, DNA-damage, or metabolic state rather than a tissue-specific autonomic function. This hypothesis is provisional because there is no globally significant GO or KEGG term, no known multi-member complex, and no dense physical interaction network.

### Important genes

#### PRKDC

- **Related proteins** (co-abundance neighbors): PHIP (0.87), RSL1D1 (0.85), PI4KA (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC is the strongest network-connected gene and links PHIP, RSL1D1, and PI4KA in the co-abundance graph. It encodes the catalytic subunit of DNA-dependent protein kinase, with established roles in DNA double-strand-break repair, recombination, telomere maintenance, and innate immune activation. It also supplies one side of the supplementary STRING signal (STRING SMART Phosphoinositide 3-kinase, catalytic domain; within-query FDR = 0.0325) with PI4KA and has extensive literature and disease evidence, including DNA-PKcs-deficiency immunodeficiency and neurodegenerative disease associations.
- **Conclusion**: Established evidence supports PRKDC as the central network candidate and as a genome-surveillance kinase. It is plausible, but not established, that PRKDC coordinates the other module genes in this shared co-abundance state.

#### PI4KA

- **Related proteins** (co-abundance neighbors): PRKDC (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol 4-kinase alpha. This gene encodes a phosphatidylinositol (PI) 4-kinase which catalyzes the first committed step in the biosynthesis of phosphatidylinositol 4,5-bisphosphate. The mammalian PI 4-kinases have been classified into two types, II and III, based on their molecular mass, and modulation by detergent and adenosine. The protein encoded by this gene is a type III enzyme that is not inhibited by adenosine. Al…
- **Diseases (Open Targets)**: polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis (0.749); spastic paraplegia 84, autosomal recessive (0.691); multiple intestinal atresia (0.595); PI4KA-related disorder (0.494); neurodegenerative disease (0.492)
- **Europe PMC papers**: 803
- **Why important**: PI4KA is the other member of (STRING SMART Phosphoinositide 3-kinase, catalytic domain; within-query FDR = 0.0325) and catalyzes a committed step in phosphatidylinositol and phosphoinositide biosynthesis. Its annotation includes signal transduction and peripheral-nervous-system myelination, and HPA identifies brain tissue enhancement and pDC cell-type enhancement. Its disease associations include neurodevelopmental, neurological, and intestinal disorders, making it especially relevant to the autonomic nervous system context.
- **Conclusion**: Established evidence supports PI4KA as a biologically meaningful signaling and membrane-lipid regulator with neurological relevance. Its apparent connection to PRKDC is a candidate association from the supplied data, not evidence that it forms a functional complex with PRKDC in these samples.

#### PHIP

- **Related proteins** (co-abundance neighbors): PRKDC (0.87); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PHIP subunit of CUL4-Ring ligase complex. This gene encodes a protein that binds to the insulin receptor substrate 1 protein and regulates glucose transporter translocation in skeletal muscle cells. The encoded protein may also regulate growth and survival of pancreatic beta cells. Elevated copy number of this gene may be associated with melanoma severity and the encoded protein may promote melanoma metastasis in human patients. [provided…
- **Diseases (Open Targets)**: PHIP-related behavioral problems-intellectual disability-obesity-dysmorphic features syndrome (0.805); Intellectual disability (0.544); hereditary disease (0.543); obesity due to melanocortin 4 receptor deficiency (0.383); obesity disorder (0.383)
- **Europe PMC papers**: 2064
- **Why important**: PHIP is directly connected to PRKDC and has functions spanning insulin-receptor signaling, chromatin organization, transcriptional regulation, protein phosphorylation, and cell-population proliferation. It is associated with a syndromic neurodevelopmental and obesity phenotype and has a substantial literature base. Its position may make it a bridge between signaling and nuclear growth or transcriptional programs.
- **Conclusion**: Established evidence supports PHIP as a multifunctional signaling and chromatin regulator with developmental and metabolic disease relevance. Its role as a bridge within this module is a hypothesis based on co-abundance topology rather than a demonstrated molecular interaction.

#### RSL1D1

- **Related proteins** (co-abundance neighbors): PRKDC (0.85), SUPV3L1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosomal L1 domain containing 1. Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Involved in regulation of apoptotic process and regulation of cellular senescence. Acts upstream of or within regulation of protein localization. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.219); hepatocellular carcinoma (0.099); neoplasm (0.099); colorectal carcinoma (0.096); insomnia (0.078)
- **Europe PMC papers**: 381
- **Why important**: RSL1D1 connects PRKDC to SUPV3L1 and is localized to the nucleolus and mitotic chromosome. Its annotations include regulation of apoptosis, cellular senescence, protein localization, and osteoblast differentiation, while its literature and disease-association evidence are more limited than those of PRKDC or PHIP. It may therefore represent a regulatory or nucleolar-state component of the module.
- **Conclusion**: Established evidence supports RSL1D1 as a nucleolar and chromosome-associated regulator with links to apoptosis and senescence. Its participation in a DNA-repair or cellular-stress program here remains provisional and is not supported by a globally significant enrichment term.

#### SUPV3L1

- **Related proteins** (co-abundance neighbors): RSL1D1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Suv3 like RNA helicase. Enables helicase activity; nucleic acid binding activity; and protein homodimerization activity. Involved in several processes, including mitochondrial RNA metabolic process; mitochondrion morphogenesis; and positive regulation of mitochondrial RNA catabolic process. Located in mitochondrial nucleoid and nucleus. Part of mitochondrial degradosome. [provided by Alliance of Genome Resources, Apr 202…
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); response to vaccine (0.276); neoplasm (0.041); gestational diabetes (0.036); seasonal allergic rhinitis (0.025)
- **Europe PMC papers**: 275
- **Why important**: SUPV3L1 is connected to RSL1D1 and encodes a helicase involved in mitochondrial RNA metabolism, RNA degradation, RNA processing, and mitochondrial morphogenesis. It is a component of the mitochondrial degradosome and has disease associations including neurodegenerative disease. Its inclusion broadens the module from nuclear signaling to mitochondrial RNA quality control.
- **Conclusion**: Established evidence supports SUPV3L1 as a mitochondrial RNA-surveillance and processing factor. Its co-abundance with the nuclear and signaling genes may indicate a shared cellular quality-control state, but a direct mechanistic link is not established.
