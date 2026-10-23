# Conserved co-abundance modules: bone_marrow and myometrium

## Module 0

**Tissue pair**: bone_marrow and myometrium  
**Genes (15)**: PGD, CNDP2, COPB1, DDX5, TUFM, EIF3L, HSPH1, MAT2A, PCNA, PSMC2, SEC24C, AARS1, DARS1, USO1, XPO1

### Function

This is best interpreted as a mixed cellular maintenance module rather than a narrowly specialized pathway. Its genes cover translation and aminoacyl-tRNA charging (AARS1, DARS1, EIF3L), mitochondrial translation (TUFM), proteostasis and degradation (HSPH1, PSMC2), RNA processing and nuclear transport (DDX5, XPO1), DNA replication and repair (PCNA), methyl-donor production (MAT2A), oxidative pentose-phosphate metabolism (PGD), and intracellular membrane trafficking (COPB1, USO1, SEC24C). No GO/KEGG term passed global correction, so there is no globally significant pathway annotation to claim. The supplementary STRING results support protein metabolism (STRING RCTM Metabolism of proteins; within-query FDR = 0.0453) and a lymphoblast-associated expression pattern (STRING TISSUES Lymphoblast; within-query FDR = 0.0441), but these are supportive rather than globally corrected enrichment evidence.

**Cell composition.** The module contains no secreted genes and is not dominated by plasma proteins. Most genes have low tissue specificity and low immune-cell specificity, consistent with broadly expressed housekeeping or cellular-maintenance functions. HPA detects all module proteins in bone marrow, whereas detection is more limited in myometrium, which may reflect differences in abundance or detectability rather than absence of the biology. There is nevertheless a blood-related component: PGD is group-enriched in bone marrow and in several myeloid cell types, including neutrophils and their progenitors, and the module includes a supplementary lymphoblast signal (STRING TISSUES Lymphoblast; within-query FDR = 0.0441). The shared module may therefore partly reflect common broadly expressed cellular programs, with a possible contribution from hematopoietic or other shared cell populations, rather than a myometrium-specific mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING network is sparse. Established high-confidence relationships include AARS1-DARS1, linking two aminoacyl-tRNA synthetases, and a trafficking cluster consisting of COPB1, USO1, and SEC24C. The latter relationships are coherent with COPI, COPII, ER-to-Golgi, and Golgi transport functions. Additional STRING-supported membership in protein-metabolism and lymphoblast tissue annotations is supplementary (STRING TISSUES Lymphoblast; within-query FDR = 0.0441) (STRING RCTM Metabolism of proteins; within-query FDR = 0.0453). hu.MAP provides two partial complex connections: AARS1 and PGD occur together in C1, while USO1 and SEC24C occur together in C2. Because each hu.MAP complex contributes only a small subset of its members to this module, these findings support local mechanistic links but do not establish one unified multiprotein complex. Overall, the evidence favors a co-abundance module assembled from several connected maintenance processes, with the strongest physical-network coherence in the trafficking submodule.

**STRING interactions (score >= 0.7)**: 4 of 105 gene pairs: AARS1–DARS1 (0.743); COPB1–SEC24C (0.714); COPB1–USO1 (0.869); SEC24C–USO1 (0.761)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Lymphoblast (FDR = 0.0441, 6 genes); RCTM Metabolism of proteins (FDR = 0.0453, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (AARS1, PGD; 2/57); huMAP3_12394.1 (USO1, SEC24C; 2/98)

### Novelty

This may be a new tissue-pair co-abundance observation, but it should not be described as a newly discovered molecular complex or pathway. Several component functions and relationships are already established by STRING and hu.MAP, especially aminoacyl-tRNA synthetase association and intracellular vesicle trafficking (hu.MAP huMAP3_14442.1) (hu.MAP huMAP3_12394.1). The absence of a globally significant GO/KEGG term and the sparse physical network make the biological interpretation less specific. Thus, the potentially novel aspect is the coordinated abundance pattern shared by bone marrow and myometrium, not the individual gene functions or their known interactions. Replication in independent cohorts, control for cell composition, and perturbation or directed interaction experiments would be needed to establish novelty beyond a reproducible association.

**Hypothesis.** Hypothesis: the module reflects a shared cellular-stress and biosynthetic-support program that couples protein production, folding, degradation, nuclear and mitochondrial information flow, and secretory-pathway trafficking. In bone marrow, PGD and the hematopoietic expression signals suggest that this program may be especially visible in metabolically active or developing blood cells. In myometrium, the same program may arise from broadly expressed maintenance requirements or shared stromal and smooth-muscle cell states. The co-abundance pattern could therefore represent coordinated demand for translation, proteostasis, energy and redox support, and intracellular cargo handling, rather than a single dedicated tissue function. This is a hypothesis; the fact sheet does not demonstrate causal regulation or a direct physical assembly of all module proteins.

### Important genes

#### AARS1

- **Related proteins** (co-abundance neighbors): MAT2A (0.86), PGD (0.84), PCNA (0.83), USO1 (0.82); STRING partners: DARS1 (0.743)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is among the most connected genes in the module and links MAT2A, PGD, PCNA, and USO1. It has direct STRING support with DARS1 and is also present in hu.MAP complex C1 (hu.MAP huMAP3_14442.1). Its established function in alanyl-tRNA aminoacylation provides a strong translation-related anchor, while its broad HPA pattern is compatible with a general cellular maintenance role. Its disease associations include Charcot-Marie-Tooth disease and developmental epileptic encephalopathy, and it has a substantial literature.
- **Conclusion**: Established: AARS1 is a broadly expressed translation enzyme with a central network position and known association with DARS1 and C1. Hypothesis: it may help connect translational demand to the metabolic and trafficking components of this shared module.

#### USO1

- **Related proteins** (co-abundance neighbors): COPB1 (0.85), AARS1 (0.82), HSPH1 (0.82); STRING partners: COPB1 (0.869), SEC24C (0.761)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: USO1 vesicle transport factor. The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during buddin…
- **Diseases (Open Targets)**: psoriatic arthritis (0.184); bipolar disorder (0.150); retinitis pigmentosa (0.085); cone dystrophy (0.076); cone-rod dystrophy (0.076)
- **Europe PMC papers**: 546
- **Why important**: USO1 is a key bridge between the trafficking cluster and the rest of the module, connecting COPB1, SEC24C, AARS1, and HSPH1. It has strong STRING relationships with COPB1 and SEC24C and occurs with SEC24C in hu.MAP complex C2 (hu.MAP huMAP3_12394.1). Its established ER-to-Golgi and Golgi vesicle-transport function gives the module a concrete intracellular logistics component. It is tissue-enhanced in skeletal muscle and cell-type-enhanced in myonuclei, while remaining detected in bone marrow.
- **Conclusion**: Established: USO1 is a Golgi-associated vesicle-transport factor supported by both STRING and hu.MAP evidence. Hypothesis: USO1 may be the principal organizing feature of a shared secretory-pathway maintenance arm, although the module does not show evidence for secretion of its proteins.

#### PGD

- **Related proteins** (co-abundance neighbors): AARS1 (0.84); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in bone_marrow
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: phosphogluconate dehydrogenase. 6-phosphogluconate dehydrogenase is the second dehydrogenase in the pentose phosphate shunt. Deficiency of this enzyme is generally asymptomatic, and the inheritance of this disorder is autosomal dominant. Hemolysis results from combined deficiency of 6-phosphogluconate dehydrogenase and 6-phosphogluconolactonase suggesting a synergism of the two enzymopathies. Several transcript variants encoding…
- **Diseases (Open Targets)**: neurodegenerative disease (0.420); Abnormality of the skeletal system (0.329); autoimmune disorder of central nervous system (0.246); smoking behavior (0.245); essential hypertension (0.199)
- **Europe PMC papers**: 8652
- **Why important**: PGD is important because it is the clearest composition-sensitive marker in the module. HPA places it in a bone-marrow-enriched pattern and associates it with neutrophils, neutrophil progenitors, basophils, monocytes, and eosinophils. Its established role in the oxidative pentose-phosphate pathway and NADPH regeneration links the module to redox balance and biosynthetic metabolism. It is also a member of hu.MAP complex C1 with AARS1 (hu.MAP huMAP3_14442.1), and it has extensive disease and literature associations.
- **Conclusion**: Established: PGD is a metabolic enzyme with a strong hematopoietic expression signature and a plausible link to redox support. Hypothesis: PGD may indicate that part of the shared module reflects blood-cell composition or the metabolic demands of hematopoietic cells, rather than a universal myometrial program.

#### PCNA

- **Related proteins** (co-abundance neighbors): AARS1 (0.83), TUFM (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: proliferating cell nuclear antigen. The protein encoded by this gene is found in the nucleus and is a cofactor of DNA polymerase delta. The encoded protein acts as a homotrimer and helps increase the processivity of leading strand synthesis during DNA replication. In response to DNA damage, this protein is ubiquitinated and is involved in the RAD6-dependent DNA repair pathway. Two transcript variants encoding the same protein have b…
- **Diseases (Open Targets)**: ataxia-telangiectasia-like disorder (0.497); neurodegenerative disease (0.188); neoplasm (0.118); diabetes mellitus (0.116); hepatocellular carcinoma (0.113)
- **Europe PMC papers**: 61820
- **Why important**: PCNA has a direct connection to AARS1 and TUFM and is tissue-enhanced in bone marrow, with cell-type enhancement in erythrocyte progenitors and other proliferative cell populations. Its established function as a DNA-replication processivity factor and participant in mismatch repair makes it a marker of proliferative and genome-maintenance capacity. It has the largest literature volume among the highlighted genes and disease associations including ataxia-telangiectasia-like disorder and neoplasia.
- **Conclusion**: Established: PCNA supports a genome-replication and repair interpretation and is compatible with proliferative bone-marrow cell states. Hypothesis: PCNA may explain part of the shared abundance pattern through cell-cycle demand, but the fact sheet does not establish that proliferation drives the entire module.

#### MAT2A

- **Related proteins** (co-abundance neighbors): AARS1 (0.86), DARS1 (0.85), DDX5 (0.84), PSMC2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionine adenosyltransferase 2A. The protein encoded by this gene catalyzes the production of S-adenosylmethionine (AdoMet) from methionine and ATP. AdoMet is the key methyl donor in cellular processes. [provided by RefSeq, Jun 2011].
- **Diseases (Open Targets)**: neurodegenerative disease (0.545); familial thoracic aortic aneurysm and aortic dissection (0.416); autoimmune disorder of central nervous system (0.340); prostate carcinoma (0.252); Abnormality of the cardiovascular system (0.192)
- **Europe PMC papers**: 2615
- **Why important**: MAT2A has the highest network connectivity in the module and links AARS1, DARS1, DDX5, and PSMC2. Its established production of S-adenosylmethionine provides methyl-donor capacity for cellular processes, and its annotations include methionine response and positive regulation of TORC1 signaling. It is tissue-enhanced in pancreas and cell-type-enhanced in smooth-muscle cells, which is relevant to the myometrium comparison. Its disease associations span neurodegenerative, cardiovascular, autoimmune, and malignant conditions, with substantial literature support.
- **Conclusion**: Established: MAT2A is a highly connected metabolic regulator with a plausible role in methylation and growth-related cellular maintenance. Hypothesis: MAT2A may integrate nutrient state with the translation, proteostasis, and cell-cycle signals represented by neighboring genes, but this regulatory role is not demonstrated by the co-abundance data alone.

## Module 1

**Tissue pair**: bone_marrow and myometrium  
**Genes (7)**: GOT2, CS, CLTC, FH, NNT, DDOST, STT3A

### Function

The strongest primary functional signal is an endoplasmic-reticulum protein N-linked glycosylation process, supported by the globally corrected oligosaccharyltransferase-complex terms (GO:CC oligosaccharyltransferase complex; q_global = 0.0442) and (GO:CC oligosaccharyltransferase complex A; q_global = 0.0442). DDOST and STT3A provide the direct molecular basis for this interpretation. The remaining genes form a coherent mitochondrial oxidative-metabolism group: CS, GOT2, FH and NNT participate in the tricarboxylic-acid cycle, amino-acid metabolism, proton-linked redox chemistry or NADPH regeneration. CLTC contributes intracellular vesicle trafficking and receptor-mediated endocytosis. Thus, the most defensible interpretation is a module linking mitochondrial energy and redox metabolism with protein maturation and intracellular trafficking, rather than a narrowly defined single pathway. The heart-tissue STRING signals (STRING TISSUES Atrium; within-query FDR = 0.0138), (STRING TISSUES Left ventricle; within-query FDR = 0.015) and (STRING TISSUES Right atrium; within-query FDR = 0.0421) are supplementary and support the metabolic component, but are not primary globally corrected enrichment evidence.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. It also does not show a blood-cell enrichment pattern, because every gene has low immune-cell specificity and no enriched blood-cell category is reported. The composition is instead dominated by broadly functional intracellular metabolic proteins, with several genes showing tissue enhancement in skeletal muscle, tongue, liver or related metabolically active tissues. HPA detects protein for most genes in bone marrow and for a subset in myometrium, while GOT2, DDOST and CLTC have absent myometrium detection in the supplied IHC summary. The shared co-abundance may therefore reflect conserved cellular energy, biosynthetic or trafficking programs, and could also be influenced by shared metabolically active cell populations, rather than blood contamination.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC oligosaccharyltransferase complex | 0.0442 | DDOST, STT3A |
| GO:CC oligosaccharyltransferase complex A | 0.0442 | DDOST, STT3A |

### STRING and hu.MAP

STRING provides strong known support for a metabolic subnetwork involving CS with FH and GOT2, and for the DDOST-STT3A oligosaccharyltransferase relationship. These established relationships support biological coherence, but STRING does not cover every co-abundance edge: NNT and CLTC have no listed STRING partners in the supplied thresholded results, and the listed STRING evidence does not establish the full module as one physical complex. The tissue enrichments (STRING TISSUES Atrium; within-query FDR = 0.0138), (STRING TISSUES Left ventricle; within-query FDR = 0.015) and (STRING TISSUES Right atrium; within-query FDR = 0.0421) are consistent with the mitochondrial metabolic component. No hu.MAP complex contains multiple members of this module, so there is no supplied complex-level evidence for a single assembled multiprotein machine.

**STRING interactions (score >= 0.7)**: 4 of 21 gene pairs: CS–FH (0.993); CS–GOT2 (0.952); DDOST–STT3A (0.999); FH–GOT2 (0.979)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Atrium (FDR = 0.0138, 4 genes); TISSUES Left ventricle (FDR = 0.015, 4 genes); TISSUES Right atrium (FDR = 0.0421, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a wholly new molecular pathway. Its principal relationships and functions are already established: CS, GOT2 and FH are known metabolic proteins, and DDOST with STT3A are known oligosaccharyltransferase components. The absence of a multi-member hu.MAP complex and the incomplete STRING coverage do not by themselves demonstrate novelty. The potentially novel aspect is the tissue-pair-specific co-abundance configuration that brings mitochondrial metabolism, oligosaccharyltransferase activity and trafficking into one conserved module across bone marrow and myometrium. That systems-level association is a hypothesis generated by this analysis and requires independent validation.

**Hypothesis.** Hypothesis: this conserved module reflects a coordinated cellular state in which mitochondrial carbon metabolism and redox buffering support endoplasmic-reticulum protein maturation and membrane trafficking. CS, GOT2 and FH could provide metabolic flux, while NNT could maintain NADPH-dependent redox capacity; DDOST and STT3A could mediate co-translational glycosylation, with CLTC supporting subsequent intracellular transport. This model is mechanistically plausible from the supplied annotations and network structure, but the co-abundance data do not establish directionality, physical interaction among all members, or causal regulation.

### Important genes

#### CS

- **Related proteins** (co-abundance neighbors): GOT2 (0.86), NNT (0.84), FH (0.84), DDOST (0.82); STRING partners: FH (0.993), GOT2 (0.952)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: citrate synthase. The protein encoded by this gene is a Krebs tricarboxylic acid cycle enzyme that catalyzes the synthesis of citrate from oxaloacetate and acetyl coenzyme A. The enzyme is found in nearly all cells capable of oxidative metablism. This protein is nuclear encoded and transported into the mitochondrial matrix, where the mature form is found. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.385); autoimmune disorder of central nervous system (0.251); psoriasis (0.176); deafness (0.107); hearing loss, autosomal recessive (0.107)
- **Europe PMC papers**: 189739
- **Why important**: CS has the strongest network centrality in the supplied module and connects the mitochondrial metabolic group to NNT, FH, GOT2 and DDOST. Its established function is citrate synthesis in the mitochondrial tricarboxylic-acid cycle, and it has tissue enhancement in skeletal muscle and tongue. Its extensive literature and disease associations make it the clearest metabolic anchor.
- **Conclusion**: Established evidence supports CS as a central mitochondrial metabolic component of the module. Its proposed role as a bridge to protein glycosylation is a hypothesis based on the co-abundance network, not a demonstrated direct mechanism.

#### FH

- **Related proteins** (co-abundance neighbors): CS (0.84); STRING partners: CS (0.993), GOT2 (0.979)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fumarate hydratase. The protein encoded by this gene is an enzymatic component of the tricarboxylic acid (TCA) cycle, or Krebs cycle, and catalyzes the formation of L-malate from fumarate. It exists in both a cytosolic form and an N-terminal extended form, differing only in the translation start site used. The N-terminal extended form is targeted to the mitochondrion, where the removal of the extension generates the …
- **Diseases (Open Targets)**: hereditary leiomyomatosis and renal cell cancer (0.838); fumaric aciduria (0.820); hereditary neoplastic syndrome (0.580); Multiple cutaneous leiomyomas (0.575); neurodegenerative disease (0.482)
- **Europe PMC papers**: 42469
- **Why important**: FH is connected to CS and GOT2 by strong known STRING relationships and catalyzes a core tricarboxylic-acid-cycle reaction. It has liver tissue enhancement, mitochondrial detection in the supplied tissues, extensive literature, and disease associations including hereditary leiomyomatosis and renal cell cancer and fumaric aciduria.
- **Conclusion**: Established evidence identifies FH as a well-supported metabolic member that reinforces the mitochondrial subnetwork. Its participation in a coordinated redox-to-glycosylation program remains a module-level hypothesis.

#### NNT

- **Related proteins** (co-abundance neighbors): CS (0.84), STT3A (0.83), CLTC (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nicotinamide nucleotide transhydrogenase. This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free …
- **Diseases (Open Targets)**: familial glucocorticoid deficiency (0.638); neurodegenerative disease (0.497); hereditary disease (0.453); atypical hemolytic-uremic syndrome with DGKE deficiency (0.416); Abnormality of the skeletal system (0.396)
- **Europe PMC papers**: 6111
- **Why important**: NNT has a high network position and links CS with STT3A and CLTC in the co-abundance graph. It is an inner-mitochondrial- membrane enzyme that generates NADPH and contributes to reactive-oxygen-species metabolism. HPA reports enrichment in metabolically specialized tissues and cell types, and the gene has disease associations involving glucocorticoid deficiency and redox-relevant hereditary disease.
- **Conclusion**: Established evidence supports NNT as a plausible redox regulator within the metabolic portion of the module. Its possible support of endoplasmic-reticulum glycosylation through redox control is a hypothesis rather than a direct demonstrated interaction.

#### STT3A

- **Related proteins** (co-abundance neighbors): NNT (0.83); STRING partners: DDOST (0.999)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: STT3 oligosaccharyltransferase complex catalytic subunit A. The protein encoded by this gene is a catalytic subunit of the N-oligosaccharyltransferase (OST) complex, which functions in the endoplasmic reticulum to transfer glycan chains to asparagine residues of target proteins. A separate complex containing a similar catalytic subunit with an overlapping function also exists. Multiple transcript variants encoding different isoforms have been found for thi…
- **Diseases (Open Targets)**: congenital disorder of glycosylation, type Iw, autosomal dominant (0.751); STT3A-congenital disorder of glycosylation (0.740); dengue disease (0.512); COVID-19 (0.370); hereditary disease (0.192)
- **Europe PMC papers**: 944
- **Why important**: STT3A is one of the two genes responsible for the primary globally corrected oligosaccharyltransferase enrichment (GO:CC oligosaccharyltransferase complex; q_global = 0.0442) and (GO:CC oligosaccharyltransferase complex A; q_global = 0.0442). It is the catalytic subunit of an endoplasmic-reticulum N-linked glycosylation complex and has a disease association with STT3A-related congenital disorder of glycosylation. Its relationship with DDOST is also strongly supported by STRING.
- **Conclusion**: Established evidence supports STT3A as the principal protein-glycosylation anchor of the module. Its connection to mitochondrial metabolic genes is supported by co-abundance but is not established as a direct biochemical interaction.

#### DDOST

- **Related proteins** (co-abundance neighbors): CS (0.82); STRING partners: STT3A (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dolichyl-diphosphooligosaccharide--protein glycosyltransferase non-catalytic subunit. This gene encodes a component of the oligosaccharyltransferase complex which catalyzes the transfer of high-mannose oligosaccharides to asparagine residues on nascent polypeptides in the lumen of the rough endoplasmic reticulum. The protein complex co-purifies with ribosomes. The product of this gene is also implicated in the processing of advanced glycation endproducts (AGEs), which form from non…
- **Diseases (Open Targets)**: DDOST-congenital disorder of glycosylation (0.734); young-onset Parkinson disease (0.561); neurodegenerative disease (0.539); dengue disease (0.505); congenital disorder of glycosylation (0.373)
- **Europe PMC papers**: 685
- **Why important**: DDOST is the other member of both globally corrected oligosaccharyltransferase terms (GO:CC oligosaccharyltransferase complex; q_global = 0.0442) and (GO:CC oligosaccharyltransferase complex A; q_global = 0.0442). It is a non-catalytic oligosaccharyltransferase component located in the endoplasmic reticulum, and its known STRING relationship with STT3A supports the glycosylation module. Its reported associations with congenital glycosylation disorders and neurodegenerative disease add disease relevance.
- **Conclusion**: Established evidence supports DDOST as a structural oligosaccharyltransferase component and as a partner of STT3A. Its apparent network connection with mitochondrial metabolism should be treated as a co-abundance observation until experimentally validated.

## Module 2

**Tissue pair**: bone_marrow and myometrium  
**Genes (16)**: ACO2, ANXA6, CANX, CAPN1, FERMT2, GARS1, GBE1, HSP90AA1, HSPA8, NIBAN2, PDIA4, CTPS1, RRBP1, SEPTIN9, TARS1, VPS35

### Function

The strongest interpretation is an endoplasmic-reticulum protein quality-control and secretory-protein processing module. (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00575) identifies protein processing in the endoplasmic reticulum and includes PDIA4, CANX, RRBP1, HSP90AA1, HSPA8 and CAPN1. PDIA4 provides disulfide-isomerase activity and is linked to protein folding, secretion and the endoplasmic-reticulum stress response; CANX is an endoplasmic-reticulum chaperone for newly synthesized glycoproteins; RRBP1 links endoplasmic-reticulum membranes to ribosomes and secretory pathways; and HSPA8 and HSP90AA1 provide chaperone functions. (GO:CC melanosome; q_global = 0.0357) and (GO:CC pigment granule; q_global = 0.0357) associate the module with melanosome and pigment-granule cellular components, but these terms share several general chaperone and endoplasmic-reticulum genes with (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00575). They should therefore be treated as cellular-localization evidence rather than evidence that this bone-marrow–myometrium module performs a dedicated pigment function. The remaining genes add translation, nucleotide synthesis, energy metabolism, cytoskeletal, membrane, adhesion and trafficking functions, consistent with a broader cellular proteostasis and biosynthetic program.

**Cell composition.** This does not appear to be a plasma-protein or predominantly secreted-protein module: the HPA summary identifies only a small secreted subset, while PDIA4 is intracellular and membrane-associated and most members are nonsecreted. The module is also not strongly blood-cell specific. HPA reports low immune-cell specificity for most genes, with only limited immune-cell-enhanced or immune-cell-enriched annotations. Most genes have low tissue specificity, and protein detection is broadly present in both bone marrow and myometrium. Some members show enhancement in smooth muscle, muscle, adipocyte, trophoblast, epithelial, pancreatic or other specialized cell types. Thus, shared abundance could reflect a broadly expressed housekeeping or proteostasis program, with contributions from shared or recurring cell populations, rather than a bone-marrow-specific immune process or a myometrium-specific contractile process.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human) | 0.00575 | CANX, CAPN1, HSP90AA1, HSPA8, PDIA4, RRBP1 |
| GO:CC melanosome | 0.0357 | ANXA6, CANX, HSP90AA1, HSPA8, PDIA4 |
| GO:CC pigment granule | 0.0357 | ANXA6, CANX, HSP90AA1, HSPA8, PDIA4 |

### STRING and hu.MAP

STRING independently supports the endoplasmic-reticulum processing interpretation through (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.002) and supports the melanosome-related localization through (STRING Component Melanosome; within-query FDR = 0.0353), but these are supplementary enrichments rather than globally corrected evidence. The high-confidence pairings are CANX with PDIA4, CANX with HSP90AA1, HSP90AA1 with HSPA8, and GARS1 with TARS1. These links reinforce a chaperone and protein-folding core together with a separate aminoacyl-tRNA-synthetase relationship. The co-abundance graph contains additional links that are not represented by high-confidence STRING pairings, so co-abundance should not be equated with direct physical interaction. No hu.MAP complex contains multiple module members. This argues against assigning the whole module to one established physical complex and instead favors a coordinated cellular state or pathway-level program.

**STRING interactions (score >= 0.7)**: 4 of 120 gene pairs: CANX–HSP90AA1 (0.848); CANX–PDIA4 (0.931); GARS1–TARS1 (0.909); HSP90AA1–HSPA8 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Protein processing in endoplasmic reticulum (FDR = 0.002, 6 genes); Component Melanosome (FDR = 0.0353, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module is a plausible tissue-pair co-abundance finding, but the fact sheet does not establish that its biological function is a previously unknown molecular pathway. The core endoplasmic-reticulum chaperone and folding relationships are already represented in STRING, and the functions of PDIA4, CANX, RRBP1, HSPA8 and HSP90AA1 are established. The lack of a multi-member hu.MAP complex and the limited overlap between module edges and STRING interactions leave open the possibility that the particular cross-tissue co-abundance organization is novel. However, absence from hu.MAP or STRING alone cannot prove novelty, because co-abundance captures coordinated abundance rather than only direct binding and database coverage is incomplete. The defensible conclusion is that the module may represent a new tissue-pair pattern built from largely known proteostasis components, rather than a demonstrably new molecular mechanism.

**Hypothesis.** Hypothesis: a shared endoplasmic-reticulum proteostasis state in bone marrow and myometrium coordinates folding, disulfide-bond formation, ribosome-associated secretory processing and stress-buffering with the biosynthetic and metabolic demands of the resident cells. PDIA4, CANX, RRBP1, HSPA8 and HSP90AA1 could form the functional core, while CTPS1, the aminoacyl-tRNA synthetases, ACO2, GBE1, ANXA6, FERMT2, SEPTIN9 and VPS35 could reflect linked demands for nucleotide supply, translation, energy, membrane organization, adhesion and trafficking. The pigment-granule annotations may indicate shared vesicular or membrane-associated machinery rather than pigment production. This hypothesis requires validation with cell-resolved data, perturbation of the endoplasmic-reticulum quality-control components, and comparison of module abundance with secretory load and cellular composition.

### Important genes

#### PDIA4

- **Related proteins** (co-abundance neighbors): CANX (0.92), TARS1 (0.89), RRBP1 (0.86), NIBAN2 (0.84), ACO2 (0.83), CTPS1 (0.83), ANXA6 (0.80); STRING partners: CANX (0.931)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 has the strongest central network position in the module and connects the endoplasmic-reticulum-related core to TARS1, RRBP1 and several additional module genes. It is present in all primary enrichment terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00575), (GO:CC melanosome; q_global = 0.0357) and (GO:CC pigment granule; q_global = 0.0357) and both supplementary STRING terms (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.002) and (STRING Component Melanosome; within-query FDR = 0.0353). Its established function is catalysis of protein folding and thiol-disulfide interchange in the endoplasmic reticulum, with links to immunoglobulin assembly, secretion and endoplasmic-reticulum stress. Its disease associations include neurodegenerative disease, neoplasm and liver-related disorders, and the literature support is substantial.
- **Conclusion**: Established evidence supports PDIA4 as a central endoplasmic-reticulum folding and secretory-quality-control component. It is the strongest candidate for an upstream or organizing role in this module. It remains a hypothesis that PDIA4 drives the shared tissue-pair abundance pattern rather than simply marking the same cellular state.

#### CANX

- **Related proteins** (co-abundance neighbors): PDIA4 (0.92), TARS1 (0.91), CTPS1 (0.82), ANXA6 (0.82), HSP90AA1 (0.81); STRING partners: HSP90AA1 (0.848), PDIA4 (0.931)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is highly connected within the module and links PDIA4, HSP90AA1, TARS1, CTPS1 and ANXA6. It appears in all primary enrichment terms (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00575), (GO:CC melanosome; q_global = 0.0357) and (GO:CC pigment granule; q_global = 0.0357) and both STRING terms (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.002) and (STRING Component Melanosome; within-query FDR = 0.0353). Its established function as an endoplasmic-reticulum calcium-binding chaperone places it directly at the interface of glycoprotein folding, assembly and retention of improperly folded proteins. It has extensive literature support and disease associations spanning neurodegenerative and infectious disease contexts.
- **Conclusion**: Established evidence supports CANX as a central molecular chaperone and a plausible bridge between endoplasmic-reticulum quality control and the broader module. Its position makes it a strong marker of coordinated proteostasis. A specific role in coupling this program to pigment-granule-like vesicular machinery remains hypothetical.

#### HSP90AA1

- **Related proteins** (co-abundance neighbors): HSPA8 (0.81), CANX (0.81); STRING partners: CANX (0.848), HSPA8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein 90 alpha family class A member 1. The protein encoded by this gene is an inducible molecular chaperone that functions as a homodimer. The encoded protein aids in the proper folding of specific target proteins by use of an ATPase activity that is modulated by co-chaperones. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012].
- **Diseases (Open Targets)**: cancer (0.643); plasma cell myeloma (0.404); non-small cell lung carcinoma (0.394); dengue disease (0.375); Orthomyxoviridae infectious disease (0.375)
- **Europe PMC papers**: 8215
- **Why important**: HSP90AA1 belongs to the enriched gene set in (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00575), (GO:CC melanosome; q_global = 0.0357) and (GO:CC pigment granule; q_global = 0.0357) and is supported by (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.002) and (STRING Component Melanosome; within-query FDR = 0.0353). It has a high-confidence STRING relationship with HSPA8 and a further relationship with CANX, forming a recognizable chaperone neighborhood. Its established function is ATP-dependent folding of specific client proteins and regulation of stress and defense-related processes. It has very extensive literature support and broad disease associations, including cancer and infectious disease.
- **Conclusion**: Established evidence supports HSP90AA1 as a general proteostasis and stress-buffering component that strengthens the interpretation of the module as a coordinated chaperone state. Its broad expression and extensive disease literature make it informative but not specific to either tissue. Any tissue-specific client proteins or causal contribution to the shared module remain hypotheses.

#### RRBP1

- **Related proteins** (co-abundance neighbors): PDIA4 (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribosome binding protein 1. This gene encodes a ribosome-binding protein of the endoplasmic reticulum (ER) membrane. Studies suggest that this gene plays a role in ER proliferation, secretory pathways and secretory cell differentiation, and mediation of ER-microtubule interactions. Alternative splicing has been observed and protein isoforms are characterized by regions of N-terminal decapeptide and C-terminal heptad repeats.…
- **Diseases (Open Targets)**: cancer (0.476); dengue disease (0.462); neurodegenerative disease (0.324); coronary artery disorder (0.292); placental abruption (0.279)
- **Europe PMC papers**: 1654
- **Why important**: RRBP1 is connected to PDIA4 and is included in the primary endoplasmic-reticulum term (KEGG Protein processing in endoplasmic reticulum - Homo sapiens (human); q_global = 0.00575) and the supplementary STRING term (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.002). It is an endoplasmic-reticulum membrane ribosome-binding protein with established roles in endoplasmic-reticulum proliferation, secretory pathways, secretory-cell differentiation and endoplasmic-reticulum–microtubule interactions. Its pancreas and acinar-cell enrichment is compatible with a role in secretory-cell biology, while its detection in both tissues supports relevance to the shared module. It has substantial literature support and disease associations that include cancer and neurodegenerative disease.
- **Conclusion**: Established evidence supports RRBP1 as the module member most directly connecting endoplasmic-reticulum architecture, ribosome association and secretory capacity. It strengthens the interpretation that the module reflects biosynthetic and secretory load rather than a dedicated immune signature. Whether RRBP1 is functionally regulating the shared state or merely responding to it is unresolved.

#### CTPS1

- **Related proteins** (co-abundance neighbors): TARS1 (0.88), CAPN1 (0.88), PDIA4 (0.83), CANX (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CTP synthase 1. This gene encodes an enzyme responsible for the catalytic conversion of UTP (uridine triphosphate) to CTP (cytidine triphospate). This reaction is an important step in the biosynthesis of phospholipids and nucleic acids. Activity of this proten is important in the immune system, and loss of function of this gene has been associated with immunodeficiency. Alternative splicing results in multiple tr…
- **Diseases (Open Targets)**: combined immunodeficiency due to CTPS1 deficiency (0.712); androgenetic alopecia (0.204); hyperpituitarism (0.195); urolithiasis (0.097); alcohol drinking (0.097)
- **Europe PMC papers**: 641
- **Why important**: CTPS1 occupies a connecting position between TARS1, CAPN1, PDIA4 and CANX, linking the proteostasis core to nucleotide metabolism. It is not part of the primary enrichment terms, so its importance comes from network placement and established biology rather than direct enrichment annotation. CTPS1 catalyzes CTP production needed for nucleotide and phospholipid biosynthesis, and its activity is important in immune function; loss of function is associated with combined immunodeficiency. It has substantial literature support and a particularly direct disease association with CTPS1 deficiency.
- **Conclusion**: Established evidence supports CTPS1 as a biosynthetic support component that could supply nucleotide and membrane-building demands accompanying protein processing. Its low immune-cell specificity in HPA argues against interpreting the module as simply a blood-cell signature. The proposed coupling between CTPS1 activity and endoplasmic-reticulum proteostasis in these tissues is a hypothesis requiring direct metabolic and perturbation studies.

## Module 3

**Tissue pair**: bone_marrow and myometrium  
**Genes (15)**: ALDH1A2, CORO1C, DPYSL2, EHD2, ILK, CKB, LDHB, MDH1, PARVA, PLS3, SELENBP1, SERPINB6, TGFB1I1, TPM1, TPM2

### Function

The strongest functional interpretation is a contractile, actin–focal-adhesion and cell-matrix morphogenesis module. The primary evidence is the globally corrected heart morphogenesis term (GO:BP heart morphogenesis; q_global = 0.00484), supported by ALDH1A2, ILK, PARVA and TPM1. This signal is biologically coherent with ILK and PARVA roles in integrin-linked adhesion, TPM1 and TPM2 roles in actin-based contraction, and the supplementary sarcomere and heart-morphogenesis terms (STRING Component Sarcomere; within-query FDR = 0.025) and (STRING Process Heart morphogenesis; within-query FDR = 0.0352). Additional module genes connect cytoskeletal organization, endocytosis, cellular energy metabolism and redox or metabolic processes, but these are secondary interpretations because they are not represented by globally corrected GO or KEGG terms. The module therefore most plausibly reflects organization and signaling of contractile or stromal cells rather than a narrowly defined biochemical pathway.

**Cell composition.** The module is not composed of secreted or plasma proteins: the HPA summary reports no secreted genes. It is also not uniformly a blood-cell module. Most genes have cell-type-enhanced rather than cell-type-enriched expression, with recurring associations to smooth muscle cells, vascular smooth muscle cells and decidual stromal cells. Several genes also have immune-cell annotations, including plasmacytoid dendritic cells, myeloid dendritic cells, monocytes, basophils, neutrophils and platelets, so blood or shared hematopoietic cells may contribute to the bone-marrow signal. However, the repeated smooth-muscle, stromal and focal-adhesion pattern, together with detection of most proteins in both tissues, supports a shared contractile or stromal cellular component as a plausible source. Some broadly distributed cytoskeletal and metabolic proteins may be housekeeping-like contributors rather than tissue-specific drivers. The HPA pattern also shows tissue-enhanced expression in heart muscle, endometrium, intestine, brain and related tissues, indicating that the module is not specific to either sampled tissue.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP heart morphogenesis | 0.00484 | ALDH1A2, ILK, PARVA, TPM1 |

### STRING and hu.MAP

STRING identifies a compact set of high-confidence relationships rather than a fully connected network. The established relationships include CORO1C with PLS3, ILK with PARVA, ILK with TGFB1I1, PARVA with TGFB1I1, and TPM1 with TPM2. These links support two recognizable substructures: an ILK–PARVA–TGFB1I1 focal-adhesion signaling group and a TPM1–TPM2 actin or contractile group, with CORO1C–PLS3 supporting actin remodeling. STRING supplementary enrichment for sarcomere and cytoplasmic components (STRING Component Sarcomere; within-query FDR = 0.025) and (STRING Keyword Cytoplasm; within-query FDR = 0.032), and for heart morphogenesis (STRING Process Heart morphogenesis; within-query FDR = 0.0352), is consistent with this interpretation but is not global enrichment evidence. hu.MAP independently places TPM1 and TPM2 together in (hu.MAP huMAP3_06153.1), and ILK and PARVA together in (hu.MAP huMAP3_09385.1) and (hu.MAP huMAP3_11194.1). The agreement between the co-abundance network, STRING interactions and hu.MAP complexes supports a biologically structured module, while the absence of hu.MAP assignments for many other genes indicates that the module also contains genes linked by co-abundance or indirect cellular context rather than one established complex.

**STRING interactions (score >= 0.7)**: 5 of 105 gene pairs: CORO1C–PLS3 (0.818); ILK–PARVA (0.999); ILK–TGFB1I1 (0.745); PARVA–TGFB1I1 (0.724); TPM1–TPM2 (0.993)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Sarcomere (FDR = 0.025, 5 genes); Keyword Cytoplasm (FDR = 0.032, 13 genes); Process Heart morphogenesis (FDR = 0.0352, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06153.1 (TPM2, TPM1; 2/6); huMAP3_09385.1 (ILK, PARVA; 2/8); huMAP3_11194.1 (ILK, PARVA; 2/10)

### Novelty

This is not best described as a wholly new molecular pathway, because its central relationships and functions are already established by STRING, hu.MAP, gene annotations and disease literature. The potentially novel result is the coordinated co-abundance of this contractile, focal-adhesion, stromal and metabolic gene set across bone marrow and myometrium. That cross-tissue association is suggestive but cannot by itself establish a new mechanism. Absence of some module genes from STRING or hu.MAP does not prove novelty, because such databases preferentially capture experimentally studied interactions and curated complexes. A stronger novelty claim would require independent replication, cell-composition adjustment, comparison with existing tissue co-expression modules and perturbation or localization experiments.

**Hypothesis.** Hypothesis: the shared module marks a conserved contractile-stromal state in which integrin-linked adhesion signaling through ILK and PARVA, modulation by TGFB1I1, and actin filament regulation by TPM1, TPM2, CORO1C and PLS3 coordinate cell shape, matrix attachment and mechanical responsiveness. ALDH1A2 may contribute local retinoic-acid signaling that influences morphogenesis or stromal differentiation. In bone marrow, the same pattern could arise from stromal, vascular, megakaryocytic or platelet-associated cells, with additional immune-cell contributions; in myometrium, it could reflect smooth-muscle or stromal cells. This is a hypothesis, not proof that the same cell type or causal pathway produces the module in both tissues.

### Important genes

#### ILK

- **Related proteins** (co-abundance neighbors): TGFB1I1 (0.87), PARVA (0.85); STRING partners: PARVA (0.999), TGFB1I1 (0.745)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK is a central focal-adhesion gene with direct links to PARVA and TGFB1I1 in STRING and membership in two hu.MAP complexes (hu.MAP huMAP3_09385.1) and (hu.MAP huMAP3_11194.1). It is one of the genes in the globally corrected heart morphogenesis term (GO:BP heart morphogenesis; q_global = 0.00484) and is annotated for integrin-mediated signaling, cell-matrix adhesion and morphogenesis. HPA links it to smooth muscle cells, megakaryocytes and platelets, and its literature volume is substantial.
- **Conclusion**: Established evidence supports ILK as a core adhesion and morphogenesis component of the module. Its network and complex memberships make it a strong candidate driver or anchor of the shared module, but the co-abundance data do not establish that ILK is causally regulating the other genes in either tissue.

#### PARVA

- **Related proteins** (co-abundance neighbors): ILK (0.85); STRING partners: ILK (0.999), TGFB1I1 (0.724)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments, Focal adhesion sites; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: parvin alpha. This gene encodes a member of the parvin family of actin-binding proteins. Parvins are associated with focal contacts and contain calponin homology domains that bind to actin filaments. The encoded protein is part of the integrin-linked kinase signaling complex and plays a role in cell adhesion, motility and survival. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.487); osteoarthritis, hip (0.339); total hip arthroplasty (0.339); open-angle glaucoma (0.337); Pancreatic pseudocyst (0.331)
- **Europe PMC papers**: 3949
- **Why important**: PARVA is directly connected to ILK and TGFB1I1 in STRING and occurs with ILK in hu.MAP complexes (hu.MAP huMAP3_09385.1) and (hu.MAP huMAP3_11194.1). It is included in the globally corrected heart morphogenesis term (GO:BP heart morphogenesis; q_global = 0.00484) and is annotated for focal contacts, actin binding, cell adhesion, polarity and actin-cytoskeleton organization. HPA associates it with smooth muscle cells and focal-adhesion or actin locations, making it especially relevant to the proposed contractile-stromal interpretation.
- **Conclusion**: Established evidence supports PARVA as an actin-linked integrin-complex component that helps explain the module's adhesion and morphogenesis signal. Its co-abundance with ILK is consistent with shared focal-adhesion activity, while a causal role in the cross-tissue module remains hypothetical.

#### TPM1

- **Related proteins** (co-abundance neighbors): TGFB1I1 (0.83), CORO1C (0.81); STRING partners: TPM2 (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in myometrium
- **hu.MAP 3.0**: huMAP3_06153.1
- **Function (MyGene.info)**: tropomyosin 1. This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the fi…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.798); left ventricular noncompaction (0.760); left ventricular noncompaction 9 (0.664); familial isolated dilated cardiomyopathy (0.639); hypertrophic cardiomyopathy 3 (0.596)
- **Europe PMC papers**: 6278
- **Why important**: TPM1 is one of the genes in (GO:BP heart morphogenesis; q_global = 0.00484), participates in the supplementary sarcomere and heart-morphogenesis terms (STRING Component Sarcomere; within-query FDR = 0.025) and (STRING Process Heart morphogenesis; within-query FDR = 0.0352), and has a high-confidence STRING relationship with TPM2. It belongs to a hu.MAP tropomyosin complex with TPM2 (hu.MAP huMAP3_06153.1). Its actin-filament location, smooth and striated muscle functions, heart and skeletal-muscle tissue enhancement, and strong cardiomyopathy associations make it a particularly informative marker of contractile biology.
- **Conclusion**: Established evidence supports TPM1 as a contractile actin-filament component and a major explanation for the morphogenesis and sarcomere signals. The module does not show that TPM1 activity causes the shared pattern, but its presence makes a contractile-cell contribution more plausible than a purely generic housekeeping interpretation.

#### ALDH1A2

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 1 family member A2. This protein belongs to the aldehyde dehydrogenase family of proteins. The product of this gene is an enzyme that catalyzes the synthesis of retinoic acid (RA) from retinaldehyde. Retinoic acid, the active derivative of vitamin A (retinol), is a hormonal signaling molecule that functions in developing and adult tissues. The studies of a similar mouse gene suggest that this enzyme and the cytochrom…
- **Diseases (Open Targets)**: diaphragmatic hernia 4, with cardiovascular defects (0.704); osteoarthritis, hand (0.464); osteoarthritis, knee (0.462); Knee pain (0.366); alcohol drinking (0.352)
- **Europe PMC papers**: 3482
- **Why important**: ALDH1A2 is included in the globally corrected heart morphogenesis term (GO:BP heart morphogenesis; q_global = 0.00484) and in the supplementary heart-morphogenesis term (STRING Process Heart morphogenesis; within-query FDR = 0.0352). It encodes the enzyme that synthesizes retinoic acid and is annotated for retinoic-acid biosynthesis, vitamin A metabolism and developmental processes. HPA links it to endometrium, fallopian tube, decidual stromal cells, endometrial stromal cells and epicardial cells, while its disease associations include cardiovascular developmental defects and osteoarthritis. Its network position is peripheral, but its biochemical specificity gives it interpretive importance.
- **Conclusion**: Established evidence supports ALDH1A2 as a plausible developmental and stromal signaling component that complements the mechanical adhesion genes. Its peripheral network position argues against calling it a central structural hub; its role in the shared module may instead reflect local retinoic-acid state or cell identity. A direct mechanistic connection to ILK or the contractile genes is a hypothesis.

#### TGFB1I1

- **Related proteins** (co-abundance neighbors): CORO1C (0.92), CKB (0.91), ILK (0.87), DPYSL2 (0.87), LDHB (0.86), TPM2 (0.84), TPM1 (0.83); STRING partners: ILK (0.745), PARVA (0.724)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Focal adhesion sites; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transforming growth factor beta 1 induced transcript 1. This gene encodes a coactivator of the androgen receptor, a transcription factor which is activated by androgen and has a key role in male sexual differentiation. The encoded protein is thought to regulate androgen receptor activity and may have a role to play in the treatment of prostate cancer. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by R…
- **Diseases (Open Targets)**: neurodegenerative disease (0.318); Glycosuria (0.226); mucous membrane pemphigoid (0.074); triple-A syndrome (0.074); esophageal squamous cell carcinoma (0.058)
- **Europe PMC papers**: 874
- **Why important**: TGFB1I1 has the strongest network connectivity in the module and links focal-adhesion genes with cytoskeletal and metabolic neighbors, including ILK, PARVA, TPM1 and TPM2. STRING supports its relationships with ILK and PARVA. HPA places it at focal-adhesion sites and associates it with decidual stromal, hepatic stellate, ovarian stromal and myoepithelial cells. Its annotations include cell adhesion, transforming-growth-factor receptor signaling and epithelial-to-mesenchymal transition, making it a strong integrator of matrix and differentiation signals.
- **Conclusion**: Established evidence supports TGFB1I1 as a network-level integrator of adhesion, matrix signaling and stromal-state biology. Its central position makes it important for interpreting the module, although centrality in a co-abundance graph does not prove biochemical control or directionality.

## Module 4

**Tissue pair**: bone_marrow and myometrium  
**Genes (5)**: CAVIN3, KCTD12, PDLIM4, PDXK, PGM1

### Function

The module does not have a demonstrated pathway-level function. No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Its most coherent interpretation is a mixed cellular-state module linking cytoskeletal and membrane organization with intermediary metabolism. PDLIM4 is associated with actin filaments and muscle structure development, CAVIN3 with the plasma membrane and caveolae biology, KCTD12 with receptor and G protein-coupled receptor signaling, PDXK with vitamin B6 cofactor metabolism, and PGM1 with glucose and glycogen metabolism. These annotations support biological plausibility but do not establish a single shared pathway. The co-abundance pattern may instead reflect coordinated expression in particular stromal, smooth-muscle, vascular, myeloid, or related cell states.

**Cell composition.** The module is not composed of plasma or secreted proteins: the HPA summary reports no secreted genes. It is also not uniformly blood-cell enriched. CAVIN3 is enriched in classical monocytes and myeloid dendritic cells, and KCTD12 is immune-cell enhanced in those contexts, whereas PDLIM4 is not detected in immune cells, PDXK has low immune-cell specificity, and PGM1 has low immune-cell specificity. HPA tissue and single-cell annotations are heterogeneous, including blood vessel, brain, skeletal muscle, tongue, decidual stromal cells, smooth-muscle-related contexts, fibroblasts, endothelial cells, and myeloid cells. This heterogeneity argues against interpreting the module as a dedicated bone-marrow or myometrium pathway. A shared cell-type composition effect, particularly involving stromal, vascular, smooth-muscle, or myeloid populations, remains a plausible explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was detected among the module genes, and no hu.MAP complex contained multiple module members. Thus, the co-abundance edges are not supported here as established physical protein interactions or as membership in a known multiprotein complex. The absence of STRING and hu.MAP support weakens a direct-complex interpretation, but it does not exclude indirect regulation, condition-dependent interactions, shared cell-type expression, or correlations driven by common cellular states.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The cross-tissue co-abundance pattern appears potentially under-described because it lacks high-confidence STRING links, shared hu.MAP complex membership, and globally significant GO or KEGG enrichment. However, those absences do not prove that the module is a new biological discovery. The strongest defensible conclusion is that this particular tissue-pair association is a candidate novel observation requiring replication, cell-composition adjustment, independent expression data, and ideally protein-level or perturbational validation. Its novelty is therefore provisional rather than established.

**Hypothesis.** Hypothesis: the module reflects a shared structural and metabolic state present in a subset of cells contributing to bone marrow and myometrium. PDLIM4 and CAVIN3 may mark coordinated cytoskeletal and membrane organization, while KCTD12 may represent receptor-signaling or cell-state regulation. PDXK and PGM1 may support the metabolic and cofactor requirements of that state. The pattern could arise from coordinated stromal, vascular, smooth-muscle, or myeloid-cell abundance rather than direct physical interaction among the proteins. This hypothesis should be tested by controlling for cell composition and by examining whether the genes co-vary within purified cell populations.

### Important genes

#### PDLIM4

- **Related proteins** (co-abundance neighbors): CAVIN3 (0.90), KCTD12 (0.85), PDXK (0.81), PGM1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Actin filaments; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 4. This gene encodes a protein which may be involved in bone development. Mutations in this gene are associated with susceptibility to osteoporosis. [provided by RefSeq, Nov 2009]
- **Diseases (Open Targets)**: neurodegenerative disease (0.446); dermatitis (0.353); inflammatory bowel disease (0.226); atopic eczema (0.196); chalazion (0.155)
- **Europe PMC papers**: 687
- **Why important**: PDLIM4 is the central network hub, linking every other module member in the supplied co-abundance structure. Its actin-filament location and annotations involving actin organization, muscle structure development, and bone development make it the strongest candidate for a structural anchor. Its reported association with osteoporosis susceptibility adds disease relevance, while its literature base is substantial.
- **Conclusion**: Established evidence supports PDLIM4 as the network-centered cytoskeletal candidate and as a gene relevant to bone-related biology. It is not established that PDLIM4 mechanistically drives the shared module or connects directly to the other proteins; that interpretation remains a hypothesis.

#### CAVIN3

- **Related proteins** (co-abundance neighbors): PDLIM4 (0.90), KCTD12 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caveolae associated protein 3. The protein encoded by this gene was identified as a binding protein of the protein kinase C, delta (PRKCD). The expression of this gene in cultured cell lines is strongly induced by serum starvation. The expression of this protein was found to be down-regulated in various cancer cell lines, suggesting the possible tumor suppressor function of this protein. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: restless legs syndrome (0.315); insomnia (0.275); sickle cell disease and related diseases (0.226); non-autoimmune hemolytic anemia (0.193); thalassemia (0.136)
- **Europe PMC papers**: 221
- **Why important**: CAVIN3 occupies an intermediate network position and connects PDLIM4 with KCTD12. It is tissue enhanced in blood vessel and localized to the plasma membrane, while its single-cell annotations include stromal, fibroblast, stellate, and germ-cell contexts and its blood-cell annotations include classical monocytes and myeloid dendritic cells. Its reported caveolae and protein-kinase-C-related biology makes it a plausible membrane-state marker, although its literature volume is more limited than that of the metabolic genes.
- **Conclusion**: Established evidence supports CAVIN3 as a membrane-associated, cell-context-sensitive component of the module. The idea that it coordinates membrane structure with PDLIM4 or immune and stromal states is a hypothesis, not a demonstrated interaction.

#### KCTD12

- **Related proteins** (co-abundance neighbors): CAVIN3 (0.85), PDLIM4 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: potassium channel tetramerization domain containing 12. Enables identical protein binding activity. Predicted to be involved in protein homooligomerization. Predicted to act upstream of or within regulation of G protein-coupled receptor signaling pathway. Predicted to be located in cell projection. Predicted to be part of receptor complex. Predicted to be active in postsynaptic membrane and presynaptic membrane. [provided by Alliance of Genome Resource…
- **Diseases (Open Targets)**: adolescent idiopathic scoliosis (0.315); alcohol drinking (0.313); stroke disorder (0.296); sialolithiasis (0.251); Tietze syndrome (0.239)
- **Europe PMC papers**: 741
- **Why important**: KCTD12 is centrally placed within the smaller membrane-associated portion of the network, connecting to both PDLIM4 and CAVIN3. Its annotations involve protein homooligomerization, receptor complexes, G protein-coupled receptor signaling, and neuronal or cell-projection biology. HPA places it in monocyte progenitor, macrophage, Kupffer-cell, and related contexts, making it relevant to a possible myeloid or shared-cell-state explanation. Its literature base is substantial.
- **Conclusion**: Established evidence supports KCTD12 as a signaling- and cell-state-associated gene with immune-cell relevance. A role in coupling receptor signaling to the structural part of this module is plausible but remains unproven because neither STRING nor hu.MAP supports a known complex here.

#### PDXK

- **Related proteins** (co-abundance neighbors): PDLIM4 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in bone_marrow
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pyridoxal kinase. The protein encoded by this gene phosphorylates vitamin B6, a step required for the conversion of vitamin B6 to pyridoxal-5-phosphate, an important cofactor in intermediary metabolism. The encoded protein is cytoplasmic and probably acts as a homodimer. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. [provided by RefSeq, Jul 200…
- **Diseases (Open Targets)**: neuropathy, hereditary motor and sensory, type VIc, with optic atrophy (0.581); neurodegenerative disease (0.429); autoimmune disorder of central nervous system (0.370); hypertensive disorder (0.188); ovarian neoplasm (0.169)
- **Europe PMC papers**: 859
- **Why important**: PDXK is connected to the module hub and provides a distinct biochemical dimension. It catalyzes a step in vitamin B six salvage that generates an important metabolic cofactor, is tissue enhanced in brain, and has strong disease relevance through hereditary neuropathy and neurodegenerative associations. Its literature base is substantial, but its direct relationship to the structural and membrane-associated genes is not established.
- **Conclusion**: Established evidence supports PDXK as a vitamin B six metabolic enzyme and a plausible indicator of cellular metabolic demand. Its inclusion in a shared bone-marrow–myometrium module may reflect cell composition or metabolic state; a direct mechanistic link to PDLIM4 is only a hypothesis.

#### PGM1

- **Related proteins** (co-abundance neighbors): PDLIM4 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in bone_marrow, myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphoglucomutase 1. The protein encoded by this gene is an isozyme of phosphoglucomutase (PGM) and belongs to the phosphohexose mutase family. There are several PGM isozymes, which are encoded by different genes and catalyze the transfer of phosphate between the 1 and 6 positions of glucose. In most cell types, this PGM isozyme is predominant, representing about 90% of total PGM activity. In red cells, PGM2 is a majo…
- **Diseases (Open Targets)**: PGM1-congenital disorder of glycosylation (0.843); MPDU1-congenital disorder of glycosylation (0.551); developmental and epileptic encephalopathy, 36 (0.551); RFT1-congenital disorder of glycosylation (0.551); disorder of glycogen metabolism (0.506)
- **Europe PMC papers**: 3203
- **Why important**: PGM1 is connected to the hub and is the most broadly supported metabolic candidate in the module. It is the predominant phosphoglucomutase isozyme in most cell types, participates in glucose, glycogen, glycolytic, and related carbohydrate metabolism, and has group-enriched expression in skeletal muscle and tongue. Its disease associations include PGM1-related congenital glycosylation and glycogen-metabolism disorders, and it has the largest literature base among the listed genes.
- **Conclusion**: Established evidence supports PGM1 as a central carbohydrate-metabolism enzyme with relevance to muscle and inherited metabolic disease. Its co-abundance with structural and membrane genes may indicate shared energetic requirements or cell-type composition, but it does not establish a direct pathway or physical interaction.
