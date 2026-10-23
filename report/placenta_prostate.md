# Conserved co-abundance modules: placenta and prostate

## Module 0

**Tissue pair**: placenta and prostate  
**Genes (7)**: ACLY, ANXA1, COPB1, LMNB1, PLIN3, PSMA1, SEC23A

### Function

The module does not have a globally supported GO or KEGG functional enrichment signal: no globally significant GO/KEGG term passed global correction. Its gene-level annotations nevertheless suggest a mixed intracellular program involving ER-to-Golgi and Golgi vesicle trafficking (SEC23A and COPB1), nuclear-envelope organization (LMNB1), proteasome-mediated protein turnover and stress-related processes (PSMA1), lipid synthesis and acetyl-CoA production (ACLY), lipid-droplet and endosomal trafficking (PLIN3), and membrane-associated inflammatory regulation (ANXA1). The co-abundance pattern therefore most cautiously represents coordinated cellular maintenance, trafficking, proteostasis, and lipid-handling activity rather than a single established pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only ANXA1 is annotated as secreted to blood, while the other genes are intracellular or membrane-associated. It is also not strongly blood-cell enriched overall. HPA indicates broadly distributed expression for most genes, with selected tissue or cell-type enhancement involving bone marrow, lymphoid tissue, esophageal cells, neutrophils, pancreatic islet cells, spermatids, erythrocyte progenitors, and related progenitor populations. ANXA1 is immune-cell enhanced and associated with basophils, but the module as a whole has low immune-cell specificity. All module proteins are detected in both placenta and prostate. Thus, shared abundance may reflect broadly expressed cellular machinery, with possible contributions from shared or variable cell populations, rather than a placenta-prostate-specific secretory program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction among the module gene pairs reaches the fact-sheet interaction threshold, and there is no supplementary STRING functional enrichment. No hu.MAP complex contains multiple module members. The co-abundance edges are therefore not corroborated by the supplied high-confidence physical-interaction or complex resources. This does not invalidate the module: co-abundance can reflect shared regulation, cell composition, correlated activity, or indirect coordination. It does mean that the observed network should not be described as a known protein complex or established physical interaction network.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may be a novel co-abundance pattern, but the evidence is insufficient to claim a new biological mechanism or a newly discovered protein complex. Its lack of STRING and hu.MAP support makes it less likely to reproduce a canonical physical complex, yet absence from those resources alone does not establish novelty. The genes themselves are well characterized, several have extensive literature and disease annotation, and their individual functions are not novel. The potentially novel aspect is their coordinated abundance across placenta and prostate, which requires independent replication, control for cell composition, and comparison with published tissue co-expression modules.

**Hypothesis.** Hypothesis: the module reflects coordinated remodeling of intracellular membrane traffic and lipid-associated cellular maintenance in shared placenta and prostate cell populations. SEC23A and COPB1 could represent coupled ER-to-Golgi and retrograde trafficking capacity; PLIN3 and ACLY could link vesicle or endosomal processes with lipid-droplet handling and cytosolic acetyl-CoA supply; LMNB1 and PSMA1 could indicate concurrent nuclear-structure and proteostasis requirements; and ANXA1 could connect these processes to membrane organization or inflammatory-cell signals. This is a mechanistic model rather than an enrichment result, and it should be tested by cell-resolved analysis, perturbation of trafficking or lipid-handling genes, and assessment of whether the co-abundance pattern persists within comparable cell types.

### Important genes

#### ANXA1

- **Related proteins** (co-abundance neighbors): PSMA1 (0.82), PLIN3 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A1. This gene encodes a membrane-localized protein that binds phospholipids. This protein inhibits phospholipase A2 and has anti-inflammatory activity. Loss of function or expression of this gene has been detected in multiple tumors. [provided by RefSeq, Dec 2014].
- **Diseases (Open Targets)**: schizophrenia (0.434); myopathy (0.413); type 1 diabetes mellitus (0.346); spinal cord injury (0.335); Abnormal nasolacrimal system morphology (0.327)
- **Europe PMC papers**: 9690
- **Why important**: ANXA1 is among the more connected and strongly weighted module members and links PSMA1 with PLIN3 in the co-abundance graph. Its established functions include phospholipid binding, inhibition of phospholipase A2, anti-inflammatory activity, leukocyte migration, phagocytosis, and inflammatory regulation. HPA identifies it as tissue enhanced, esophageal-cell enriched, immune-cell enhanced, and secreted to blood. It also has particularly extensive literature and multiple disease associations, making it the best candidate for evaluating whether the module contains an immune, epithelial, or extracellular component.
- **Conclusion**: Established evidence supports ANXA1 as a membrane-associated inflammatory regulator that may also be detectable extracellularly. Its module membership could reflect shared membrane or inflammatory biology, but a cell-composition contribution is also plausible. It should not be concluded that ANXA1 physically interacts with the other module proteins because STRING provides no supporting interaction evidence.

#### SEC23A

- **Related proteins** (co-abundance neighbors): COPB1 (0.84), ACLY (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A is a central connecting member in the module, linked to COPB1 and ACLY. Its established function is COPII-dependent vesicle budding and ER-to-Golgi protein transport, with additional roles in cargo loading and intracellular trafficking. It is detected in both tissues and has disease associations involving skeletal development and other conditions. Its position provides a coherent anchor for interpreting part of the module as membrane-trafficking related.
- **Conclusion**: Established evidence supports SEC23A as a core ER export and vesicle-trafficking component. The hypothesis that its abundance coordinates with lipid metabolism and Golgi recycling in this module is biologically plausible but not demonstrated by the available enrichment, STRING, or complex evidence.

#### COPB1

- **Related proteins** (co-abundance neighbors): LMNB1 (0.89), SEC23A (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus, Vesicles, Cytosol; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coat protein complex I subunit beta 1. This gene encodes a protein subunit of the coatomer complex associated with non-clathrin coated vesicles. The coatomer complex, also known as the coat protein complex 1, forms in the cytoplasm and is recruited to the Golgi by activated guanosine triphosphatases. Once at the Golgi membrane, the coatomer complex may assist in the movement of protein and lipid components back to the endoplasmic retic…
- **Diseases (Open Targets)**: Baralle-Macken syndrome (0.598); Alzheimer disease (0.463); Parkinson disease (0.462); neurodegenerative disease (0.462); lysosomal storage disease (0.462)
- **Europe PMC papers**: 565
- **Why important**: COPB1 is a central connector between LMNB1 and SEC23A. It encodes a coatomer subunit involved in COPI-associated Golgi and ER trafficking, including retrograde and intra-Golgi transport. Its broad HPA profile and detection in both tissues make it a useful indicator of general intracellular trafficking rather than a tissue-restricted marker. Its disease associations also connect it to vesicle and neurodegenerative biology.
- **Conclusion**: Established evidence supports COPB1 as a component of coatomer-mediated intracellular transport. Its co-abundance with SEC23A supports a trafficking-related interpretation at the level of coordinated expression, but does not establish a direct physical relationship in this module.

#### ACLY

- **Related proteins** (co-abundance neighbors): SEC23A (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP citrate lyase. ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several im…
- **Diseases (Open Targets)**: familial hypercholesterolemia (0.532); Hypercholesterolemia (0.532); atherosclerosis (0.470); inherited lipid metabolism disorder (0.467); cardiovascular disorder (0.449)
- **Europe PMC papers**: 7957
- **Why important**: ACLY connects to SEC23A and provides the clearest metabolic component of the module. It produces cytosolic acetyl-CoA used for fatty-acid and cholesterol biosynthesis and is annotated for citrate and acyl-CoA metabolism. It has extensive literature and disease associations involving hypercholesterolemia, atherosclerosis, and lipid metabolism. Its cell-type enhancement in pancreatic islet cells suggests that abundance may be sensitive to cellular metabolic state.
- **Conclusion**: Established evidence supports ACLY as a cytosolic metabolic enzyme that can supply biosynthetic acetyl-CoA. The proposed link between ACLY activity and vesicle or lipid-droplet remodeling is a hypothesis consistent with the module composition, not a demonstrated pathway-level conclusion.

#### LMNB1

- **Related proteins** (co-abundance neighbors): COPB1 (0.89), PSMA1 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lamin B1. This gene encodes one of the two B-type lamin proteins and is a component of the nuclear lamina. A duplication of this gene is associated with autosomal dominant adult-onset leukodystrophy (ADLD). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: microcephaly 26, primary, autosomal dominant (0.723); autosomal dominant primary microcephaly (0.675); adult-onset autosomal dominant demyelinating leukodystrophy (0.670); hereditary disease (0.488); Syndrome with microcephaly as major feature (0.487)
- **Europe PMC papers**: 3851
- **Why important**: LMNB1 is a highly weighted connector linking COPB1 and PSMA1 and is the module's principal nuclear-envelope marker. It encodes lamin B1, a structural component of the nuclear lamina involved in nuclear-envelope organization, nuclear migration, chromatin organization, and nuclear pore localization. HPA shows tissue enhancement in bone marrow and lymphoid tissue and cell-type enhancement across several progenitor and spermatid populations. Its strong disease relevance includes adult-onset demyelinating leukodystrophy and primary microcephaly.
- **Conclusion**: Established evidence supports LMNB1 as a nuclear-architecture and genome-organization protein. Its presence suggests that the module may include general cellular structural or proliferative-state effects in addition to membrane trafficking. Any proposed functional coupling between nuclear-envelope state and the other module processes remains speculative.

## Module 1

**Tissue pair**: placenta and prostate  
**Genes (13)**: ACTN1, B2M, CALD1, COL12A1, CORO1C, CSRP1, DPYSL3, FLNA, FLNC, PDLIM7, TPM1, LTF, THBS1

### Function

The module is most consistent with an actin-cytoskeleton, cell-adhesion, and contractile-cell program. Its central genes, especially FLNA, ACTN1, PDLIM7, and FLNC, connect actin filaments with membrane or focal-adhesion structures. TPM1 and CALD1 support actin-tropomyosin regulation and smooth-muscle or nonmuscle contraction, while CSRP1, THBS1, and COL12A1 connect the program to cellular adhesion and extracellular matrix. DPYSL3 provides an additional cytoskeletal and migration-related connection. This interpretation is supported by the individual gene annotations and the network architecture, but no GO or KEGG term passed global correction. The absence of a globally enriched term does not invalidate the module.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: only a minority are annotated as secreted or extracellular-matrix proteins, including THBS1, B2M, LTF, and COL12A1. The HPA pattern instead points strongly toward smooth-muscle, stromal, vascular, myoepithelial, trophoblast, and platelet-associated cell states. Many genes are enhanced in smooth-muscle cells, with additional representation in hepatic stellate cells, decidual stromal cells, breast myoepithelial cells, and platelets. Several genes also show blood-cell associations, particularly neutrophil, eosinophil, basophil, monocyte, or platelet associations. Therefore, the shared placenta–prostate signal could reflect a conserved contractile or stromal cell program, but contribution from blood or platelet material and tissue-associated immune cells remains a plausible sample-composition explanation. Protein detection is present for several genes in placenta and for a smaller overlapping subset in prostate, so transcript or protein detection alone should not be interpreted as proof of a shared cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING relationships form a coherent but incomplete cytoskeletal structure. ACTN1 connects with FLNA, PDLIM7, and TPM1; FLNA connects with FLNC; and CALD1 connects with TPM1. These relationships are already known protein-association evidence and support an actin-filament and contractility interpretation rather than an arbitrary co-abundance pattern. The network also contains co-abundance links involving DPYSL3, B2M, CORO1C, CSRP1, THBS1, LTF, and COL12A1 that are not represented by high-confidence STRING edges in the supplied results. No hu.MAP complex contains multiple module members. Thus, the module is supported by several known pairwise relationships, but it is not established as one known multiprotein complex.

**STRING interactions (score >= 0.7)**: 5 of 78 gene pairs: ACTN1–FLNA (0.716); ACTN1–PDLIM7 (0.74); ACTN1–TPM1 (0.887); CALD1–TPM1 (0.869); FLNA–FLNC (0.907)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The genes and several of their pairwise relationships are not biologically novel: actin crosslinking, focal adhesion, smooth-muscle contraction, platelet biology, extracellular-matrix interaction, and innate immune functions are established for members of the module. The potentially novel observation is the coordinated co-abundance of this mixed cytoskeletal, contractile, stromal, extracellular, and blood-associated set across placenta and prostate. That claim should remain provisional because the module has no globally significant GO or KEGG term, no STRING functional-enrichment result, and no hu.MAP multi-member complex. Absence from the supplied interaction resources does not prove novelty, and the pattern could partly reflect shared stromal, vascular, smooth-muscle, platelet, or blood-cell composition. Independent replication and cell-composition-aware analysis would be needed before calling it a new biological module.

**Hypothesis.** Hypothesis: the conserved module represents a tissue-interface structural program in which smooth-muscle or stromal cells organize actin filaments and focal adhesions to control cell shape, contractility, migration, and extracellular-matrix attachment. FLNA, ACTN1, PDLIM7, FLNC, TPM1, and CALD1 could form the structural and contractile core, while THBS1 and COL12A1 could couple that core to matrix and vascular signaling. Platelet- and innate-immune-associated genes, including B2M and LTF, may reflect biological participation at the tissue interface or admixture from blood-derived material rather than the core mechanism. This is a mechanistic hypothesis, not a demonstrated causal model.

### Important genes

#### FLNA

- **Related proteins** (co-abundance neighbors): DPYSL3 (0.90), PDLIM7 (0.86), FLNC (0.86), ACTN1 (0.83); STRING partners: ACTN1 (0.716), FLNC (0.907)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Actin filaments, Cytosol; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: filamin A. The protein encoded by this gene is an actin-binding protein that crosslinks actin filaments and links actin filaments to membrane glycoproteins. The encoded protein is involved in remodeling the cytoskeleton to effect changes in cell shape and migration. This protein interacts with integrins, transmembrane receptor complexes, and second messengers. Defects in this gene are a cause of several synd…
- **Diseases (Open Targets)**: Melnick-Needles syndrome (0.820); heterotopia, periventricular, X-linked dominant (0.810); otopalatodigital syndrome type 2 (0.808); otopalatodigital syndrome type 1 (0.802); frontometaphyseal dysplasia 1 (0.793)
- **Europe PMC papers**: 6055
- **Why important**: FLNA is a leading network hub and links DPYSL3, PDLIM7, FLNC, and ACTN1. Its established function is to crosslink actin and connect the cytoskeleton to membrane glycoproteins, integrins, receptor complexes, and signaling pathways. HPA associates it with blood vessels, stromal and myoepithelial cell states, and megakaryocytes. Its disease associations include periventricular nodular heterotopia and several skeletal developmental syndromes, and it has an extensive literature base.
- **Conclusion**: Established evidence supports FLNA as a structural organizer and a central component of the module's actin-adhesion architecture. Hypothesis: FLNA may coordinate the shared contractile or migratory state across placenta and prostate, although its lack of prostate protein detection in the supplied HPA evidence cautions against assuming uniform cellular expression.

#### ACTN1

- **Related proteins** (co-abundance neighbors): DPYSL3 (0.90), B2M (0.84), FLNA (0.83), CORO1C (0.82); STRING partners: FLNA (0.716), PDLIM7 (0.74), TPM1 (0.887)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Actin filaments, Focal adhesion sites; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: actinin alpha 1. Alpha actinins belong to the spectrin gene superfamily which represents a diverse group of cytoskeletal proteins, including the alpha and beta spectrins and dystrophins. Alpha actinin is an actin-binding protein with multiple roles in different cell types. In nonmuscle cells, the cytoskeletal isoform is found along microfilament bundles and adherens-type junctions, where it is involved in binding …
- **Diseases (Open Targets)**: platelet-type bleeding disorder 15 (0.781); Macrothrombocytopenia (0.622); autosomal dominant macrothrombocytopenia (0.550); Thrombocytopenia (0.482); type 2 diabetes mellitus (0.410)
- **Europe PMC papers**: 3070
- **Why important**: ACTN1 is a leading network hub connecting DPYSL3, B2M, FLNA, and CORO1C, and it has a direct STRING relationship with TPM1. It binds actin at microfilament bundles and adherens-type junctions and is associated with focal adhesions, smooth muscle, neutrophils, and platelets. Its disease associations include platelet-type bleeding disorders and macrothrombocytopenia, with substantial literature support.
- **Conclusion**: Established evidence supports ACTN1 as a core actin-to-membrane and platelet or contractile-cell component, consistent with its detection in both placenta and prostate. Hypothesis: ACTN1 may be a principal structural mediator of the conserved co-abundance signal, while the B2M and CORO1C links may partly reflect cell-state or sample-composition effects.

#### PDLIM7

- **Related proteins** (co-abundance neighbors): TPM1 (0.88), FLNA (0.86), FLNC (0.83), COL12A1 (0.81); STRING partners: ACTN1 (0.74)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Actin filaments, Focal adhesion sites; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 7. The protein encoded by this gene is representative of a family of proteins composed of conserved PDZ and LIM domains. LIM domains are proposed to function in protein-protein recognition in a variety of contexts including gene transcription and development and in cytoskeletal interaction. The LIM domains of this protein bind to protein kinases, whereas the PDZ domain binds to actin filaments. The g…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); nasopharyngeal carcinoma (0.121); neoplasm (0.120); lymphoma (0.115); Hodgkins lymphoma (0.105)
- **Europe PMC papers**: 808
- **Why important**: PDLIM7 is a leading network hub connected to TPM1, FLNA, FLNC, and COL12A1. Its PDZ and LIM domains support protein recognition, kinase binding, and association with actin filaments; its annotations include actin-cytoskeleton organization and muscle-structure development. HPA places it in vascular, intestinal, skeletal-muscle, stromal, myoepithelial, megakaryocyte, and granulocyte-associated states. It has disease associations involving neurodegeneration and neoplasia and a meaningful literature base.
- **Conclusion**: Established evidence supports PDLIM7 as an adaptor linking the actin network to contractile and matrix-associated components. Hypothesis: it may organize the interface between the cytoskeletal core and COL12A1-containing extracellular structures in the shared tissue program, but this proposed bridge is not directly demonstrated by the supplied data.

#### CALD1

- **Related proteins** (co-abundance neighbors): TPM1 (0.85); STRING partners: TPM1 (0.869)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 provides a focused mechanistic link to TPM1 and is annotated as a calmodulin- and actin-binding regulator of smooth-muscle and nonmuscle contraction. It is detected by HPA in both placenta and prostate and is associated with decidual stromal, myoepithelial, extravillous trophoblast, hepatic stellate, and Leydig cell states. Its disease associations include skeletal, diaphragmatic, and ocular abnormalities, and it has substantial literature support.
- **Conclusion**: Established evidence supports CALD1 as a contractility-related component that strengthens the interpretation of the module as a structural and smooth-muscle-associated program. Hypothesis: CALD1 may tune actin-tropomyosin activity in the shared placenta–prostate state, but the module data do not establish altered contraction or direct causality.

#### THBS1

- **Related proteins** (co-abundance neighbors): CSRP1 (0.84), LTF (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Endoplasmic reticulum, Plasma membrane; IHC detected in placenta
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thrombospondin 1. The protein encoded by this gene is a subunit of a disulfide-linked homotrimeric protein. This protein is an adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. This protein can bind to fibrinogen, fibronectin, laminin, type V collagen and integrins alpha-V/beta-1. This protein has been shown to play roles in platelet aggregation, angiogenesis, and tumorigenesis. [pro…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.385); tooth disorder (0.350); autism spectrum disorder (0.336); neurodegenerative disease (0.323); metabolic syndrome (0.309)
- **Europe PMC papers**: 12762
- **Why important**: THBS1 is an extracellular and secreted bridge between CSRP1 and LTF in the module. It mediates cell-to-cell and cell-to-matrix interactions, binds fibrinogen, fibronectin, laminin, collagen, and integrins, and is linked to platelet aggregation, angiogenesis, hypoxia responses, and endothelial regulation. HPA associates it with fibroblasts, hepatic stellate cells, macrophages, monocytes, and platelets. It has the broadest literature support among the module genes and is detected in placenta.
- **Conclusion**: Established evidence supports THBS1 as an extracellular-matrix and vascular or platelet-associated component rather than a core intracellular actin organizer. Hypothesis: THBS1 could couple the cytoskeletal program to matrix remodeling or vascular signaling in placenta and prostate, while its secretion also makes it a plausible marker of tissue or blood composition.

## Module 2

**Tissue pair**: placenta and prostate  
**Genes (8)**: AHNAK, EEA1, ITIH2, PDLIM5, PLEC, S100A10, SPTBN1, SPTAN1

### Function

The module is most consistent with a conserved membrane–cytoskeleton and vesicle-trafficking program. AHNAK occupies the strongest network position and connects the spectrin-associated branch with S100A10, ITIH2, and EEA1. The SPTAN1–SPTBN1 pair, together with PLEC, supports cytoskeletal scaffolding, membrane organization, and cell-shape maintenance. EEA1 contributes an endosomal and vesicle-fusion link, while S100A10 is associated with membrane-raff assembly, vesicle budding, exocytosis, and endocytosis. The spectrin-repeat signal (STRING SMART Spectrin repeats; within-query FDR = 0.0429) is supportive but supplementary. No GO/KEGG term passed global correction, so there is no globally significant GO/KEGG enrichment to invoke. Overall, the evidence supports a structural and trafficking module rather than a narrowly defined pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only ITIH2 is annotated as secreted to blood, and it was not detected by HPA in placenta or prostate. Most members are intracellular or membrane-associated proteins, including cytoskeletal, vesicular, and scaffold proteins. HPA indicates broadly distributed expression for several genes, with additional tissue or cell-type enhancement in muscle, esophageal epithelial cells, endothelial or stromal populations, hepatocytes, Schwann cells, urothelial cells, and related cell types. Blood contamination is not the leading interpretation because most genes have low immune-cell specificity or are not detected in immune cells, although PDLIM5 is immune-cell enriched in basophils. The shared signal may therefore reflect a common epithelial, stromal, muscle-associated, or general membrane-cytoskeleton state present in both tissues rather than a placenta–prostate-specific secreted program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a connected structural core through the AHNAK–S100A10, AHNAK–PLEC, PLEC–SPTAN1, and SPTAN1–SPTBN1 relationships. The strongest-supported relationships are AHNAK–S100A10 and SPTAN1–SPTBN1, indicating that parts of the co-abundance pattern correspond to known molecular associations. The supplementary spectrin-repeat result (STRING SMART Spectrin repeats; within-query FDR = 0.0429) is consistent with the SPTAN1, SPTBN1, and PLEC branch but is not a globally corrected enrichment result. hu.MAP independently supports the same organization: (hu.MAP huMAP3_09165.1) places AHNAK, S100A10, SPTAN1, and SPTBN1 in a larger complex; (hu.MAP huMAP3_07940.1) and (hu.MAP huMAP3_05473.1) support the SPTAN1–SPTBN1 pair; and (hu.MAP huMAP3_08718.1) supports the AHNAK–S100A10 pair. Thus, the module is not merely a collection of unrelated co-abundant genes; it contains a known spectrin-associated and membrane-scaffold core, with AHNAK providing links to vesicular and extracellular-matrix-related members.

**STRING interactions (score >= 0.7)**: 4 of 28 gene pairs: AHNAK–PLEC (0.73); AHNAK–S100A10 (0.999); PLEC–SPTAN1 (0.795); SPTAN1–SPTBN1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: SMART Spectrin repeats (FDR = 0.0429, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09165.1 (S100A10, SPTBN1, AHNAK, SPTAN1; 4/39); huMAP3_07940.1 (SPTBN1, SPTAN1; 2/5); huMAP3_05473.1 (SPTBN1, SPTAN1; 2/7); huMAP3_08718.1 (S100A10, AHNAK; 2/17)

### Novelty

The molecular relationships represented here are not wholly new because several are supported by high-confidence STRING associations and multiple hu.MAP complexes. Absence of STRING or hu.MAP support for PDLIM5, PLEC, ITIH2, or EEA1 connections does not establish novelty, because database coverage and context dependence can be incomplete. The potentially novel aspect is the conserved co-abundance of this particular combination across placenta and prostate, especially the coupling of a known spectrin–AHNAK–S100A10 scaffold with EEA1, ITIH2, and PDLIM5. However, the fact sheet alone does not establish that this tissue-pair module is a new biological mechanism. It is best described as a potentially informative cross-tissue co-abundance configuration built around established structural relationships.

**Hypothesis.** Hypothesis: in both placenta and prostate, a shared population or state of epithelial, stromal, muscle-associated, or other non-immune cells uses an AHNAK–spectrin–plectin scaffold to organize the plasma membrane and cortical cytoskeleton while coordinating endosomal trafficking and membrane turnover. S100A10 may couple the scaffold to membrane budding and exocytosis, EEA1 may connect it to early-endosome handling, and ITIH2 may reflect extracellular-matrix or blood-derived coupling to the intracellular structural program. PDLIM5 may provide a tissue-state or muscle-associated scaffold link. This is a mechanistic model, not a demonstrated causal pathway; it requires validation with cell-type-resolved data, protein interaction assays, and perturbation experiments.

### Important genes

#### AHNAK

- **Related proteins** (co-abundance neighbors): S100A10 (0.93), SPTAN1 (0.84), ITIH2 (0.84), EEA1 (0.82); STRING partners: PLEC (0.73), S100A10 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in placenta, prostate
- **hu.MAP 3.0**: huMAP3_09165.1, huMAP3_08718.1
- **Function (MyGene.info)**: AHNAK nucleoprotein. The protein encoded by this gene is a large (700 kDa) structural scaffold protein consisting of a central domain with 128 aa repeats. The encoded protein may play a role in such diverse processes as blood-brain barrier formation, cell structure and migration, cardiac calcium channel regulation, and tumor metastasis. A much shorter variant encoding a 17 kDa isoform exists for this gene, and the sho…
- **Diseases (Open Targets)**: Aganglionic megacolon (0.266); neoplasm (0.108); hepatocellular carcinoma (0.093); cancer (0.085); melanoma (0.085)
- **Europe PMC papers**: 2886
- **Why important**: AHNAK has the strongest network position and connects four module branches, including S100A10, SPTAN1, ITIH2, and EEA1. It is a large structural scaffold associated with cell structure, migration, plasma-membrane repair, and blood–brain-barrier formation. It is detected in both placenta and prostate, has low tissue specificity, and has extensive literature coverage. Its STRING link to S100A10 and hu.MAP membership in (hu.MAP huMAP3_09165.1) and (hu.MAP huMAP3_08718.1) make it the clearest candidate connector in the module. Its disease associations include neoplasm, hepatocellular carcinoma, melanoma, and aganglionic megacolon.
- **Conclusion**: Established evidence supports AHNAK as a central structural and membrane-associated scaffold in this module. Its role as the causal coordinator of the other module branches is a hypothesis, although its network position and independent interaction evidence make that hypothesis plausible.

#### SPTAN1

- **Related proteins** (co-abundance neighbors): SPTBN1 (0.88), PDLIM5 (0.85), AHNAK (0.84); STRING partners: PLEC (0.795), SPTBN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Microtubules; IHC detected in placenta, prostate
- **hu.MAP 3.0**: huMAP3_09165.1, huMAP3_07940.1, huMAP3_05473.1
- **Function (MyGene.info)**: spectrin alpha, non-erythrocytic 1. Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encod…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 5 (0.749); developmental delay with or without epilepsy (0.681); spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia (0.681); infantile spasms (0.651); genetic developmental and epileptic encephalopathy (0.651)
- **Europe PMC papers**: 1422
- **Why important**: SPTAN1 is a central member of the spectrin branch, connects to SPTBN1, PLEC, and AHNAK, and participates in (hu.MAP huMAP3_09165.1), (hu.MAP huMAP3_07940.1), and (hu.MAP huMAP3_05473.1). Its established function is to stabilize plasma membranes, organize intracellular organelles, and support the actin cytoskeleton. It is detected in both tissues and has substantial literature coverage. Its disease associations include developmental and epileptic encephalopathy, developmental delay, and spastic paraplegia.
- **Conclusion**: Established evidence supports SPTAN1 as a core cytoskeletal scaffold and as an important structural anchor of the module. Whether its co-abundance reflects altered cytoskeletal organization, cell composition, or both remains unresolved.

#### SPTBN1

- **Related proteins** (co-abundance neighbors): SPTAN1 (0.88), PLEC (0.84); STRING partners: SPTAN1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, prostate
- **hu.MAP 3.0**: huMAP3_09165.1, huMAP3_07940.1, huMAP3_05473.1
- **Function (MyGene.info)**: spectrin beta, non-erythrocytic 1. Spectrin is an actin crosslinking and molecular scaffold protein that links the plasma membrane to the actin cytoskeleton, and functions in the determination of cell shape, arrangement of transmembrane proteins, and organization of organelles. It is composed of two antiparallel dimers of alpha- and beta- subunits. This gene is one member of a family of beta-spectrin genes. The encoded protein cont…
- **Diseases (Open Targets)**: developmental delay, impaired speech, and behavioral abnormalities (0.802); cancer (0.597); hereditary disease (0.516); hearing loss disorder (0.459); neurodevelopmental disorder (0.453)
- **Europe PMC papers**: 1635
- **Why important**: SPTBN1 forms the strongly supported SPTAN1–SPTBN1 spectrin pair, has links to PLEC, and appears in (hu.MAP huMAP3_09165.1), (hu.MAP huMAP3_07940.1), and (hu.MAP huMAP3_05473.1). Spectrin beta supports membrane shape, actin linkage, transmembrane-protein organization, organelle organization, cytokinesis, and vesicle-mediated transport. It is detected in placenta and prostate, has broad tissue distribution, and has substantial literature coverage. Its disease associations include developmental delay, neurodevelopmental disease, hearing loss, and cancer.
- **Conclusion**: Established evidence supports SPTBN1 as the beta-spectrin partner that reinforces the module's membrane–actin scaffold. A role in coordinating vesicle trafficking within this specific cross-tissue module is a reasonable hypothesis but is not directly demonstrated by the fact sheet.

#### PLEC

- **Related proteins** (co-abundance neighbors): SPTBN1 (0.84); STRING partners: AHNAK (0.73), SPTAN1 (0.795)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments, Cytosol; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plectin. Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 5B, with muscular dystrophy (0.796); epidermolysis bullosa simplex 5A, Ogna type (0.775); autosomal recessive limb-girdle muscular dystrophy type 2Q (0.768); epidermolysis bullosa simplex 5C, with pyloric atresia (0.755); epidermolysis bullosa simplex with nail dystrophy (0.695)
- **Europe PMC papers**: 2578
- **Why important**: PLEC links the spectrin-associated branch through STRING relationships with AHNAK and SPTAN1. It is a major cytolinker that interconnects cytoskeletal systems, maintains tissue integrity, and supports cell shape and dynamic cytoarchitecture. It is tissue enhanced in skeletal muscle, cell-type enhanced in urothelial cells, detected in both tissues, and has substantial literature coverage. Its disease associations include epidermolysis bullosa simplex and muscular dystrophy syndromes.
- **Conclusion**: Established evidence supports PLEC as a plausible mechanical integrator between spectrin structures and other cytoskeletal elements. Its specific contribution to the placenta–prostate co-abundance pattern, and whether it reflects shared cell composition or coordinated regulation, remains a hypothesis.

#### S100A10

- **Related proteins** (co-abundance neighbors): AHNAK (0.93); STRING partners: AHNAK (0.999)
- **HPA**: Tissue enhanced; Cell type enriched; blood Low immune cell specificity; location Mitochondria; IHC detected in placenta, prostate
- **hu.MAP 3.0**: huMAP3_09165.1, huMAP3_08718.1
- **Function (MyGene.info)**: S100 calcium binding protein A10. The protein encoded by this gene is a member of the S100 family of proteins containing 2 EF-hand calcium-binding motifs. S100 proteins are localized in the cytoplasm and/or nucleus of a wide range of cells, and involved in the regulation of a number of cellular processes such as cell cycle progression and differentiation. S100 genes include at least 13 members which are located as a cluster on chr…
- **Diseases (Open Targets)**: actinic keratosis (0.208); neurodegenerative disease (0.184); diverticular disease (0.183); neoplasm (0.115); hepatocellular carcinoma (0.111)
- **Europe PMC papers**: 10215
- **Why important**: S100A10 has a very strong STRING relationship with AHNAK and occurs with AHNAK in (hu.MAP huMAP3_09165.1) and (hu.MAP huMAP3_08718.1). Its annotated functions include membrane-raft assembly, vesicle budding, exocytosis, endocytosis, and positive regulation of plasminogen activation. It is tissue enhanced in esophagus and cell-type enriched in esophageal apical cells, while still being detected in placenta and prostate. It has especially extensive literature coverage and disease associations including neoplasm and hepatocellular carcinoma.
- **Conclusion**: Established evidence supports S100A10 as the principal membrane-trafficking and vesicle-associated component connected to AHNAK. Its participation in a shared membrane-repair or secretory mechanism in placenta and prostate is a hypothesis rather than a demonstrated tissue-specific function.

#### EEA1

- **Related proteins** (co-abundance neighbors): AHNAK (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Not detected in immune cells; location Vesicles; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: early endosome antigen 1. Enables 1-phosphatidylinositol binding activity; GTP-dependent protein binding activity; and protein homodimerization activity. Involved in endocytosis; vesicle fusion; and viral RNA genome replication. Located in cytosol and early endosome. Is extrinsic component of plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.370); liver disorder (0.298); external ear disorder (0.273); benign digestive system neoplasm (0.256); Alzheimer disease (0.163)
- **Europe PMC papers**: 7344
- **Why important**: EEA1 is directly connected to AHNAK in the co-abundance network and is annotated as an early-endosome protein involved in endocytosis, vesicle fusion, and early-to-late endosome transport. It is detected in both placenta and prostate, has low tissue and cell-type specificity, and has extensive literature coverage. Its disease associations include central nervous system autoimmunity, liver disorders, external-ear disorders, benign digestive-system neoplasms, and Alzheimer disease.
- **Conclusion**: Established evidence supports EEA1 as the module member that most clearly supplies an early-endosomal interpretation. Its connection to AHNAK may indicate coordinated membrane trafficking, but direct physical association or causal cooperation between these proteins in this module is not established.

## Module 3

**Tissue pair**: placenta and prostate  
**Genes (11)**: LAP3, HSPA5, CLTC, CTNNA1, FASN, HNRNPK, HYOU1, IMPDH2, PDIA4, NARS1, CCT8

### Function

No GO or KEGG term passed global multiple-testing correction, so the module does not support a formally significant pathway assignment. Its gene-level evidence instead points to cellular protein homeostasis, especially endoplasmic-reticulum folding and stress handling through HSPA5, HYOU1, and PDIA4; cytosolic protein folding and assembly through CCT8; protein synthesis through NARS1; RNA processing through HNRNPK; intracellular trafficking through CLTC; proteolysis through LAP3; guanine-nucleotide production through IMPDH2; lipid synthesis through FASN; and adhesion or mechanosensing through CTNNA1. The network therefore appears functionally mixed, with a coherent proteostasis core embedded in broadly expressed cellular machinery rather than a narrowly defined pathway.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only a minority are annotated as secreted, and most have low tissue specificity. Blood-cell confounding is not strongly supported because the genes generally have low immune-cell specificity or are not detected in immune cells. Several genes are cell-type enhanced in plasma cells, trophoblasts, epididymal cells, lactating breast cells, or germ-cell-related populations, so shared cellular composition or stress state remains a plausible contributor in placenta and prostate. Most module proteins are detected in both tissues, while FASN is tissue enhanced in adipose tissue, breast, and liver and is not detected in the sampled placenta or prostate protein data. Overall, the pattern is more consistent with broadly expressed housekeeping and proteostasis machinery, with possible contributions from shared epithelial, trophoblast, secretory, or reproductive cell states, than with a blood-derived module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact, high-confidence endoplasmic-reticulum interaction core: HSPA5 connects strongly with HYOU1 and PDIA4, and HYOU1 connects strongly with PDIA4. CCT8 also has a weaker supported link with HSPA5. STRING reports no functional-enrichment result for the module. hu.MAP independently places HSPA5 with HYOU1 in (hu.MAP huMAP3_07455.1), and places PDIA4 with HYOU1 in (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). These complexes contain many proteins not present in the module, so they validate specific physical or complex-level relationships rather than the entire module as one complete complex. The remaining module links, including the central network connections involving NARS1, LAP3, CTNNA1, and HNRNPK, are not represented by recorded high-confidence STRING partners or hu.MAP complexes in the fact sheet. Thus, the network combines a known ER proteostasis subnetwork with co-abundance relationships that may reflect shared regulation, cell composition, or indirect biology.

**STRING interactions (score >= 0.7)**: 4 of 55 gene pairs: CCT8–HSPA5 (0.701); HSPA5–HYOU1 (0.999); HSPA5–PDIA4 (0.99); HYOU1–PDIA4 (0.997)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07455.1 (HSPA5, HYOU1; 2/4); huMAP3_06775.1 (PDIA4, HYOU1; 2/60); huMAP3_09327.1 (PDIA4, HYOU1; 2/93)

### Novelty

This cannot be called a wholly new molecular mechanism because the HSPA5-HYOU1-PDIA4 relationships are already supported by STRING and hu.MAP, and the functions of the individual proteins are established. The potentially new observation is the conservation of this particular co-abundance grouping across placenta and prostate, including its links to translation, RNA handling, trafficking, metabolism, adhesion, and proteolysis. However, absence of some module pairs from STRING or hu.MAP does not establish novelty, because those resources emphasize curated or experimentally supported relationships and may not capture tissue-specific co-abundance. The appropriate conclusion is that the cross-tissue module is a hypothesis-generating systems-level observation whose specific conservation and biological meaning require independent replication and perturbation.

**Hypothesis.** Hypothesis: a shared secretory or epithelial cellular state in placenta and prostate increases ER folding demand and adaptive stress handling, producing coordinated abundance of HSPA5, HYOU1, and PDIA4. This state may be coupled to cytosolic protein assembly, translation, RNA processing, vesicle trafficking, adhesion, and biosynthetic metabolism through CCT8, NARS1, HNRNPK, CLTC, CTNNA1, IMPDH2, and FASN, with LAP3 contributing protein turnover. The hypothesis predicts that the ER-proteostasis genes should covary most strongly within comparable cell populations and should respond together to secretory load or ER stress. It remains a hypothesis because global GO or KEGG enrichment was absent and the co-abundance network does not by itself demonstrate physical interaction, causal regulation, or a common cellular origin.

### Important genes

#### HYOU1

- **Related proteins** (co-abundance neighbors): NARS1 (0.90), CTNNA1 (0.87), LAP3 (0.83), HNRNPK (0.82), CCT8 (0.81); STRING partners: HSPA5 (0.999), PDIA4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_07455.1, huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 is one of the strongest network hubs and connects to NARS1, CTNNA1, LAP3, HNRNPK, and CCT8. It has direct high-confidence STRING relationships with HSPA5 and PDIA4 and appears in all listed hu.MAP complexes (hu.MAP huMAP3_07455.1), (hu.MAP huMAP3_06775.1), and (hu.MAP huMAP3_09327.1). Its annotation supports ER folding, ER-stress response, hypoxia response, vesicle transport, and protection from apoptosis. Its cell-type-enhanced pattern includes plasma cells and reproductive or brain-related populations, and it has substantial literature support.
- **Conclusion**: Established evidence supports HYOU1 as a central ER stress and protein-folding component with strong network and complex support. Its role as the organizing bridge for the entire cross-tissue module is a hypothesis, not an established conclusion.

#### HSPA5

- **Related proteins** (co-abundance neighbors): LAP3 (0.86); STRING partners: CCT8 (0.701), HYOU1 (0.999), PDIA4 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in placenta, prostate
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is the best-supported ER chaperone in the module. It has strong STRING links to HYOU1 and PDIA4, an additional link to CCT8, and membership in hu.MAP complex (hu.MAP huMAP3_07455.1). Its annotation identifies it as an ER HSP seventy-family chaperone and master regulator of ER homeostasis, unfolded-protein response, and protein targeting to membranes. It is detected in both tissues and is cell-type enhanced in trophoblast, epididymal, and plasma-cell populations.
- **Conclusion**: Established evidence supports HSPA5 as a core proteostasis marker and plausible driver of the module's ER-related signal. Whether its abundance causally coordinates the other module genes in placenta and prostate remains untested.

#### PDIA4

- **Related proteins** (co-abundance neighbors): LAP3 (0.83); STRING partners: HSPA5 (0.99), HYOU1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta, prostate
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 has direct high-confidence STRING relationships with HSPA5 and HYOU1 and occurs with HYOU1 in hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). Its ER location and thiol-disulfide isomerase activity provide a mechanistic complement to HSPA5 and HYOU1, while its annotation includes protein folding, secretion, and ER-stress response. It is detected in both tissues and is enhanced in epididymal, trophoblast, hepatocyte, and plasma-cell populations.
- **Conclusion**: Established evidence supports PDIA4 as a key ER folding and disulfide-processing component of the module. Its participation in a conserved placenta-prostate stress program is plausible but remains a network-based inference.

#### NARS1

- **Related proteins** (co-abundance neighbors): HYOU1 (0.90), CLTC (0.86), CTNNA1 (0.86), CCT8 (0.85), LAP3 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: asparaginyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids.  Asparaginyl-tRNA synthetase is localized to the cytoplasm and belongs to the class II family of tRNA synthetases.  The N-terminal domain represents the signature sequence for the eukaryotic asparaginyl-tRNA synthetases. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, impaired language, and gait abnormalities (0.762); neurodevelopmental disorder with microcephaly, impaired language, epilepsy, and gait abnormalities (0.679); neurodevelopmental disorder (0.567); complex neurodevelopmental disorder (0.462); developmental disability (0.340)
- **Europe PMC papers**: 216
- **Why important**: NARS1 has high network connectivity and links the ER-associated portion of the module to CLTC, CTNNA1, CCT8, and LAP3. Its established function is cytoplasmic asparaginyl-tRNA aminoacylation, directly connecting the module to protein translation. It is broadly expressed, detected in both tissues, has no recorded STRING partners or hu.MAP complexes here, and has disease associations involving neurodevelopment.
- **Conclusion**: Established evidence supports NARS1 as a translation-supporting and broadly expressed network bridge. Its connection to ER stress in this module is best interpreted as coordinated cellular demand for protein synthesis rather than proof of a direct NARS1 interaction with the ER machinery.

#### CTNNA1

- **Related proteins** (co-abundance neighbors): HYOU1 (0.87), NARS1 (0.86), HNRNPK (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin alpha 1. This gene encodes a member of the catenin family of proteins that play an important role in cell adhesion process by connecting cadherins located on the plasma membrane to the actin filaments inside the cell. The encoded mechanosensing protein contains three vinculin homology domains and undergoes conformational changes in response to cytoskeletal tension, resulting in the reconfiguration of cadhe…
- **Diseases (Open Targets)**: Butterfly-shaped pigment dystrophy (0.750); hereditary neoplastic syndrome (0.557); hereditary diffuse gastric adenocarcinoma (0.555); colorectal cancer (0.506); exudative vitreoretinopathy (0.390)
- **Europe PMC papers**: 2688
- **Why important**: CTNNA1 connects the module's proteostasis-related hub HYOU1 with NARS1 and HNRNPK and is localized at plasma-membrane junctions. Its established function is coupling cadherin-based adhesion to actin and sensing cytoskeletal tension, with annotations involving adhesion, migration, gap-junction assembly, and male gonad development. It is detected in both tissues and has substantial literature and disease relevance, including hereditary neoplastic and adhesion-related disorders.
- **Conclusion**: Established evidence supports CTNNA1 as an adhesion and mechanotransduction component that may link cellular architecture to the module. Its role as a tissue-context signal connecting adhesion to ER proteostasis is a plausible hypothesis, not demonstrated causality.

#### FASN

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid synthase. The enzyme encoded by this gene is a multifunctional protein. Its main function is to catalyze the synthesis of palmitate from acetyl-CoA and malonyl-CoA, in the presence of NADPH, into long-chain saturated fatty acids. In some cancer cell lines, this protein has been found to be fused with estrogen receptor-alpha (ER-alpha), in which the N-terminus of FAS is fused in-frame with the C-terminus of …
- **Diseases (Open Targets)**: dengue disease (0.469); autism spectrum disorder (0.333); Parkinson disease (0.295); Epileptic encephalopathy (0.211); neurodegenerative disease (0.205)
- **Europe PMC papers**: 21528
- **Why important**: FASN provides the module's clearest metabolic specialization and connects to IMPDH2. Its established function is de novo long-chain fatty-acid synthesis, and it has extensive literature and disease relevance. HPA shows tissue enhancement in adipose tissue, breast, and liver and no protein detection in the sampled placenta or prostate, making it potentially informative about cell composition, metabolic state, or transcript-protein discordance rather than a stable protein component of both tissues.
- **Conclusion**: Established evidence supports FASN as a lipid-biosynthetic marker with possible relevance to proliferative or secretory cellular states. Its inclusion in this conserved module should be treated cautiously because the tissue protein evidence does not support uniform presence in both tissues.

## Module 4

**Tissue pair**: placenta and prostate  
**Genes (5)**: ATP5F1B, TUFM, PRDX3, PRDX4, VDAC2

### Function

The strongest functional interpretation is a mitochondrial oxidative-energy and proteostasis module. The primary evidence is (GO:CC mitochondrial matrix; q_global = 0.0244), the globally corrected enrichment for mitochondrial matrix, represented by ATP5F1B, PRDX3, TUFM, and VDAC2. This is coherently supported by the supplementary STRING annotations (STRING Keyword Mitochondrion; within-query FDR = 0.0109), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.011), and (STRING Component Mitochondrial matrix; within-query FDR = 0.0121). ATP5F1B is part of the catalytic F1 sector of mitochondrial ATP synthase and supports oxidative phosphorylation; TUFM supports mitochondrial translation; PRDX3 provides mitochondrial peroxide reduction; and VDAC2 forms a major metabolite-permeable channel in the mitochondrial outer membrane and is linked to mitochondrial apoptosis. PRDX4 adds an endoplasmic-reticulum antioxidant component, suggesting that the module may connect mitochondrial energy production with cellular redox control rather than represent a narrowly localized single complex. The mitochondrial nucleoid-related STRING terms (STRING COMPARTMENTS Mitochondrial nucleoid; within-query FDR = 0.0211) and (STRING Component Mitochondrial nucleoid; within-query FDR = 0.0402) are supplementary and should not be treated as globally corrected enrichment. No additional GO or KEGG term passed global correction.

**Cell composition.** This does not look like a plasma-protein, secreted-protein, or blood-cell module. HPA reports low immune-cell specificity for every gene, no enriched blood-cell category, and only PRDX4 as having intracellular-and-membrane secretome annotation. All module proteins were detected in both placenta and prostate. Most genes have low tissue specificity, while ATP5F1B and PRDX4 show tissue-enhanced or tissue-enriched patterns and all genes show cell-type enhancement. The recurring cytotrophoblast and late-spermatid associations, together with other epithelial and secretory cell associations, indicate that shared cellular composition may contribute to the cross-tissue signal. The module therefore most plausibly reflects a broadly relevant mitochondrial and redox program that is especially detectable in particular cell populations, rather than contamination by circulating blood proteins.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial matrix | 0.0244 | ATP5F1B, PRDX3, TUFM, VDAC2 |

### STRING and hu.MAP

The module contains established STRING-supported relationships between ATP5F1B and TUFM, ATP5F1B and VDAC2, and PRDX3 and VDAC2. These links support a connection between ATP synthesis, mitochondrial translation, metabolite transport, and redox regulation, but the remaining module relationships are not represented by high-confidence STRING edges in the supplied evidence. hu.MAP provides a complementary partial complex observation: (hu.MAP huMAP3_12666.1) places PRDX3 and PRDX4 in a peroxiredoxin-containing complex that also includes PRDX1, PRDX2, and KRTAP13-2. Thus, the module combines some previously recognized mitochondrial relationships with a peroxiredoxin complex connection, while not constituting a fully validated single physical complex. The co-abundance network may therefore capture coordinated pathway activity or cell-state regulation in addition to direct binding.

**STRING interactions (score >= 0.7)**: 3 of 10 gene pairs: ATP5F1B–TUFM (0.84); ATP5F1B–VDAC2 (0.758); PRDX3–VDAC2 (0.709)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Mitochondrion (FDR = 0.0109, 4 genes); COMPARTMENTS Mitochondrial matrix (FDR = 0.011, 4 genes); Component Mitochondrial matrix (FDR = 0.0121, 4 genes); COMPARTMENTS Mitochondrial nucleoid (FDR = 0.0211, 3 genes); Component Mitochondrial nucleoid (FDR = 0.0402, 3 genes); Keyword Transit peptide (FDR = 0.0427, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12666.1 (PRDX3, PRDX4; 2/5)

### Novelty

The tissue-pair co-abundance observation may be a useful new observation, but the module should not be described as a newly discovered molecular complex or as definitively novel biology. Its central functions are already established: mitochondrial ATP synthesis, mitochondrial translation, peroxide detoxification, and outer-membrane metabolite transport are well characterized. The STRING and hu.MAP evidence also shows that several component relationships or related complexes are already known. Conversely, the limited coverage of direct high-confidence STRING links and the partial rather than complete hu.MAP overlap leave open the possibility that this particular conserved placenta-prostate co-abundance configuration is under-described. Establishing novelty would require comparison with published tissue co-abundance modules, independent cohorts, perturbation data, and direct physical-interaction experiments; absence from STRING or hu.MAP alone is insufficient.

**Hypothesis.** Hypothesis: in shared placenta and prostate cell populations, coordinated mitochondrial energy production, mitochondrial protein synthesis, and peroxide handling form a cell-state program that preserves respiratory function under oxidative or biosynthetic demand. ATP5F1B and TUFM could represent energy production and mitochondrial translation, PRDX3 and PRDX4 could buffer oxidant load across mitochondrial and endoplasmic-reticulum compartments, and VDAC2 could couple metabolite exchange with mitochondrial stress or apoptotic signaling. This model is consistent with the globally corrected mitochondrial-matrix signal (GO:CC mitochondrial matrix; q_global = 0.0244), the supplementary mitochondrial annotations (STRING Keyword Mitochondrion; within-query FDR = 0.0109) through (STRING Keyword Transit peptide; within-query FDR = 0.0427), the observed network connections, and the cell-type-enhanced HPA pattern, but it remains a mechanistic hypothesis rather than a demonstrated causal pathway.

### Important genes

#### PRDX3

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.91), VDAC2 (0.81), PRDX4 (0.81), TUFM (0.80); STRING partners: VDAC2 (0.709)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Mitochondria; IHC detected in placenta, prostate
- **hu.MAP 3.0**: huMAP3_12666.1
- **Function (MyGene.info)**: peroxiredoxin 3. This gene encodes a mitochondrial protein with antioxidant function. The protein is similar to the C22 subunit of Salmonella typhimurium alkylhydroperoxide reductase, and it can rescue bacterial resistance to alkylhydroperoxide in E. coli that lack the C22 subunit. The human and mouse genes are highly conserved, and they map to the regions syntenic between mouse and human chromosomes. Sequence com…
- **Diseases (Open Targets)**: spinocerebellar ataxia, autosomal recessive 32 (0.653); corneal dystrophy, punctiform and polychromatic pre-descemet (0.571); autosomal recessive cerebellar ataxia (0.268); neurodegenerative disease (0.257); hereditary disease (0.191)
- **Europe PMC papers**: 2613
- **Why important**: PRDX3 is the most connected and strongest node in the supplied module network, linking ATP5F1B, VDAC2, PRDX4, and TUFM. It is one of the four genes supporting the primary mitochondrial-matrix term (GO:CC mitochondrial matrix; q_global = 0.0244) and the supplementary mitochondrial annotations (STRING Keyword Mitochondrion; within-query FDR = 0.0109), (STRING COMPARTMENTS Mitochondrial matrix; within-query FDR = 0.011), (STRING Component Mitochondrial matrix; within-query FDR = 0.0121), and (STRING Keyword Transit peptide; within-query FDR = 0.0427). Its established antioxidant role makes it a plausible bridge between respiratory activity and protection from mitochondrial oxidative stress. It also has extensive literature and disease associations, while its hu.MAP membership with PRDX4 in (hu.MAP huMAP3_12666.1) connects mitochondrial redox biology to the peroxiredoxin complex.
- **Conclusion**: Established evidence supports PRDX3 as a central mitochondrial antioxidant and network hub in this module. A role as the principal redox coordinator of the shared placenta-prostate program is a plausible hypothesis, but causality and direction of regulation are not established by co-abundance alone.

#### ATP5F1B

- **Related proteins** (co-abundance neighbors): PRDX3 (0.91), VDAC2 (0.82), TUFM (0.82); STRING partners: TUFM (0.84), VDAC2 (0.758)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP synthase F1 subunit beta. This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalyti…
- **Diseases (Open Targets)**: hypermetabolism due to uncoupled mitochondrial oxidative phosphorylation 2 (0.499); hypertrophic cardiomyopathy (0.212); Alzheimer disease (0.177); hypertensive disorder (0.117); response to xenobiotic stimulus (0.117)
- **Europe PMC papers**: 735
- **Why important**: ATP5F1B is a highly connected module node and participates in the primary mitochondrial-matrix enrichment (GO:CC mitochondrial matrix; q_global = 0.0244) and all supplied STRING functional annotations (STRING Keyword Mitochondrion; within-query FDR = 0.0109) through (STRING Keyword Transit peptide; within-query FDR = 0.0427). Its established function as the beta subunit of mitochondrial ATP synthase gives the module a direct oxidative-phosphorylation anchor. It has tissue-enhanced protein expression in skeletal muscle and tongue, is detected in both tissues, and has disease associations involving mitochondrial energy dysregulation and cardiometabolic phenotypes.
- **Conclusion**: Established evidence identifies ATP5F1B as the module's strongest energy-production representative and as a supported interaction partner of TUFM and VDAC2. Its prominence suggests coordinated respiratory demand, but the data do not show that ATP5F1B initiates or controls the module.

#### TUFM

- **Related proteins** (co-abundance neighbors): PRDX4 (0.83), ATP5F1B (0.82), PRDX3 (0.80); STRING partners: ATP5F1B (0.84)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Tu translation elongation factor, mitochondrial. This gene encodes a protein which participates in protein translation in mitochondria. Mutations in this gene have been associated with combined oxidative phosphorylation deficiency resulting in lactic acidosis and fatal encephalopathy. A pseudogene has been identified on chromosome 17. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: combined oxidative phosphorylation defect type 4 (0.769); neurodegenerative disease (0.502); COVID-19 (0.471); combined oxidative phosphorylation deficiency (0.370); ulcerative colitis (0.303)
- **Europe PMC papers**: 1391
- **Why important**: TUFM is a connected node associated with PRDX3, PRDX4, and ATP5F1B, and it contributes to (GO:CC mitochondrial matrix; q_global = 0.0244) and every supplied STRING functional annotation (STRING Keyword Mitochondrion; within-query FDR = 0.0109) through (STRING Keyword Transit peptide; within-query FDR = 0.0427). Its established role in mitochondrial translation and its disease association with combined oxidative-phosphorylation deficiency make it important for linking mitochondrial protein synthesis to respiratory capacity. Its cell-type-enhanced pattern includes late spermatids and esophageal basal cells, and it is detected in both tissues.
- **Conclusion**: Established evidence supports TUFM as the mitochondrial translation component of the module and as a known STRING partner of ATP5F1B. A coordinated translation-to-respiration response is a reasonable hypothesis, but the module does not establish that TUFM activity is altered or rate limiting.

#### VDAC2

- **Related proteins** (co-abundance neighbors): ATP5F1B (0.82), PRDX3 (0.81); STRING partners: ATP5F1B (0.758), PRDX3 (0.709)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in placenta, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: voltage dependent anion channel 2. This gene encodes a member of the voltage-dependent anion channel pore-forming family of proteins that are considered the main pathway for metabolite diffusion across the mitochondrial outer membrane. The encoded protein is also thought to be involved in the mitochondrial apoptotic pathway via regulation of BCL2-antagonist/killer 1 protein activity. Pseudogenes have been identified on chromosomes …
- **Diseases (Open Targets)**: neurodegenerative disease (0.345); alcohol drinking (0.204); atrial fibrillation (0.175); major depressive disorder (0.143); severe combined immunodeficiency (0.118)
- **Europe PMC papers**: 2914
- **Why important**: VDAC2 is one of the genes contributing to (GO:CC mitochondrial matrix; q_global = 0.0244) and to the supplementary mitochondrial and nucleoid-related STRING annotations (STRING Keyword Mitochondrion; within-query FDR = 0.0109) through (STRING Component Mitochondrial nucleoid; within-query FDR = 0.0402). It connects to ATP5F1B and PRDX3 in the module and is a mitochondrial outer-membrane channel involved in metabolite diffusion, with an additional established relationship to mitochondrial apoptotic signaling. Its extensive literature and disease associations make it an important interface between metabolism, membrane transport, and stress response.
- **Conclusion**: Established evidence supports VDAC2 as the module's mitochondrial outer-membrane and transport-related component, with known STRING links to ATP5F1B and PRDX3. Its proposed role in coupling respiratory metabolism to apoptotic sensitivity is mechanistically plausible but not demonstrated by this network.

#### PRDX4

- **Related proteins** (co-abundance neighbors): TUFM (0.83), PRDX3 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in placenta, prostate
- **hu.MAP 3.0**: huMAP3_12666.1
- **Function (MyGene.info)**: peroxiredoxin 4. The protein encoded by this gene is an antioxidant enzyme and belongs to the peroxiredoxin family. The protein is localized to the cytoplasm. Peroxidases of the peroxiredoxin family reduce hydrogen peroxide and alkyl hydroperoxides to water and alcohol with the use of reducing equivalents derived from thiol-containing donor molecules. This protein has been found to play a regulatory role in the ac…
- **Diseases (Open Targets)**: Neurodevelopmental delay (0.118); neoplasm (0.113); cancer (0.097); lung adenocarcinoma (0.096); gastric cancer (0.095)
- **Europe PMC papers**: 1836
- **Why important**: PRDX4 is the less connected node but is important because it extends the module beyond the mitochondrial matrix into the endoplasmic reticulum and belongs with PRDX3 in the hu.MAP complex (hu.MAP huMAP3_12666.1). Its established peroxiredoxin activity includes peroxide reduction, redox homeostasis, and cellular oxidant detoxification. Its tissue-enriched pancreatic pattern and cell-type associations with trophoblasts, epididymal principal cells, hepatocytes, late spermatids, and pancreatic acinar cells suggest that it may mark specialized secretory or metabolically active cell states. It also has substantial literature and cancer-related disease associations.
- **Conclusion**: Established evidence supports PRDX4 as an endoplasmic-reticulum and broader cellular redox component that is physically or compositionally related to PRDX3 through (hu.MAP huMAP3_12666.1). Its inclusion in a conserved mitochondrial-associated co-abundance module suggests cross-organelle redox coordination, but that connection remains a hypothesis.
