# Conserved co-abundance modules: autonomic_nervous_system and cervix_uterine

## Module 0

**Tissue pair**: autonomic_nervous_system and cervix_uterine  
**Genes (40)**: YWHAH, ARPC5L, CBR1, CCS, CLTB, CPT2, CZIB, ECHS1, FKBP2, FTH1, GGCT, GMFB, GNPNAT1, H1-10, H2AC21, HPRT1, HYPK, EIF6, PPA2, JPT2, MESD, NAA50, NDUFV2, NQO1, PYCR1, PHB1, PSME3IP1, PIR, PPIL1, PRDX4, RAB21, RHOG, SRSF5, STT3A, TAGLN2, TMA16, TPD52L2, SLC25A1, UCK2, WDR11

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway annotation. Its structure instead suggests a mixed cellular maintenance program: redox and mitochondrial energy handling through NQO1, NDUFV2, CCS, PPA2, CPT2 and ECHS1; protein folding, processing and quality control through MESD, FKBP2, PRDX4, HYPK, NAA50 and PSME3IP1; RNA processing and translation support through SRSF5, EIF6 and TMA16; and cytoskeletal, trafficking and signaling functions through ARPC5L, RHOG, RAB21, GMFB, TAGLN2 and YWHAH. These are functional hypotheses based on the individual gene annotations and network structure, not globally significant enrichment claims. The strongest coherent interpretation is a broadly expressed cellular homeostasis module with links among metabolism, proteostasis, RNA or ribosome biology, vesicle trafficking and cytoskeletal regulation.

**Cell composition.** The module is not dominated by secreted or plasma proteins: only a minority are annotated as secreted, and most proteins are intracellular or membrane-associated. It is also not strongly blood-cell specific. HPA reports low immune-cell specificity for most genes, with only a few immune-cell-enhanced genes and one gene not detected in immune cells. Many genes have low tissue specificity, while others show enhancement in liver, brain, bone marrow, pancreas or blood vessel. Single-cell annotations are heterogeneous, with recurring enrichment in epithelial, trophoblast, hepatic, neural and reproductive cell types rather than one uniform lineage. Cervix protein detection is present for most genes with available evidence, whereas matching autonomic-nervous-system HPA protein data are unavailable. Thus, the shared signal is more consistent with a conserved intracellular program or shared cellular composition than with a plasma-protein or broad blood-contamination module, although tissue or cell-type composition cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides no supplementary functional-enrichment result. Only a small set of high-confidence pairwise relationships is already represented: EIF6 with TMA16, FKBP2 with FTH1, HYPK with NAA50 and PPIL1 with PSME3IP1. These links support selected local relationships involving ribosome or nucleolar biology, protein folding or iron handling, N-terminal acetylation and RNA or protein processing, but they do not establish one unified complex for the whole module. hu.MAP provides additional evidence for GMFB with JPT2 in (hu.MAP huMAP3_12409.1), NAA50 with HYPK across several NatE- or NAA-related complexes in (hu.MAP huMAP3_06055.1), (hu.MAP huMAP3_01027.1), (hu.MAP huMAP3_10987.1) and (hu.MAP huMAP3_13394.1), and CPT2 with PPA2 in a broad mitochondrial metabolic complex in (hu.MAP huMAP3_13468.1). The repeated NAA50-HYPK pairing is the clearest complex-level anchor, while the remaining complexes contain many members outside the module. Overall, the network combines a few known molecular relationships with substantial co-abundance structure that is not explained by one established physical complex.

**STRING interactions (score >= 0.7)**: 4 of 780 gene pairs: EIF6–TMA16 (0.814); FKBP2–FTH1 (0.784); HYPK–NAA50 (0.998); PPIL1–PSME3IP1 (0.804)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12409.1 (GMFB, JPT2; 2/3); huMAP3_06055.1 (NAA50, HYPK; 2/5); huMAP3_01027.1 (NAA50, HYPK; 2/6); huMAP3_10987.1 (NAA50, HYPK; 2/8); huMAP3_13394.1 (NAA50, HYPK; 2/9); huMAP3_13468.1 (CPT2, PPA2; 2/99)

### Novelty

This is plausibly a new tissue-shared co-abundance observation, but it cannot be called a newly discovered molecular complex or pathway. The module has no globally significant GO or KEGG term, no STRING enrichment result, and only a limited subset of its relationships are represented by high-confidence STRING edges or hu.MAP complexes. At the same time, absence from these resources does not prove novelty: co-abundance can reflect coordinated regulation, cell composition, tissue state or indirect functional coupling rather than direct physical interaction. The most defensible conclusion is that the shared autonomic-nervous-system and cervix-uterine co-abundance pattern is under-characterized, with established biology concentrated in selected substructures rather than across the module as a whole.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular resilience and remodeling state shared by cells present in both tissues. Coordinated mitochondrial metabolism and redox control may support energy production and protection from oxidative stress, while endoplasmic-reticulum chaperoning, protein acetylation, RNA processing and ribosome-related functions maintain proteome quality. In parallel, Rho-family signaling, actin regulation and membrane trafficking may adapt cell shape, adhesion and intracellular transport. This could produce a coherent co-abundance signature without requiring direct physical interaction among most module members. The hypothesis should be tested by cell-resolved expression or proteomics, perturbation of redox or mitochondrial function, and examination of whether the module tracks a particular epithelial, neural, stromal or vascular cell population.

### Important genes

#### NQO1

- **Related proteins** (co-abundance neighbors): TPD52L2 (0.89), PPA2 (0.86), PIR (0.82), TMA16 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NAD(P)H quinone dehydrogenase 1. This gene is a member of the NAD(P)H dehydrogenase (quinone) family and encodes a cytoplasmic 2-electron reductase. This FAD-binding protein forms homodimers and reduces quinones to hydroquinones. This protein's enzymatic activity prevents the one electron reduction of quinones that results in the production of radical species. Mutations in this gene have been associated with tardive dyskinesia (T…
- **Diseases (Open Targets)**: neurodegenerative disease (0.543); gastric cancer (0.354); Friedreich ataxia (0.325); mitochondrial disease (0.312); immunodeficiency disease (0.194)
- **Europe PMC papers**: 20515
- **Why important**: NQO1 is a highly connected module member and links the network to quinone reduction, protection from radical species, xenobiotic handling and oxidative-stress responses. It is tissue enhanced in stomach and is detected in cervix-uterine tissue. It also has substantial literature support and disease associations involving neurodegeneration, gastric cancer and mitochondrial disease.
- **Conclusion**: Established evidence supports NQO1 as a redox and detoxification enzyme that could anchor the module's stress-response interpretation. Its network co-abundance with TPD52L2, PPA2, PIR and TMA16 supports a local module role, but it does not prove that NQO1 drives the shared tissue pattern.

#### NDUFV2

- **Related proteins** (co-abundance neighbors): CCS (0.93), ARPC5L (0.93), CBR1 (0.86), SRSF5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit V2. The NADH-ubiquinone oxidoreductase complex (complex I) of the mitochondrial respiratory chain catalyzes the transfer of electrons from NADH to ubiquinone, and consists of at least 43 subunits. The complex is located in the inner mitochondrial membrane. This gene encodes the 24 kDa subunit of complex I, and is involved in electron transfer. Mutations in this gene are implicated in Parkinson's disea…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 7 (0.717); mitochondrial complex I deficiency (0.623); type 2 diabetes mellitus (0.608); Parkinson disease (0.606); diabetes mellitus (0.579)
- **Europe PMC papers**: 1539
- **Why important**: NDUFV2 is a mitochondrial complex I subunit with a relatively central position in the network and connects to CCS, ARPC5L, CBR1 and SRSF5. Its established function in electron transfer and aerobic respiration provides a direct link to mitochondrial energy metabolism. It has extensive literature and disease associations involving complex I deficiency, Parkinson disease and diabetes.
- **Conclusion**: Established evidence supports NDUFV2 as a mitochondrial-energy component and makes it a strong candidate marker of the metabolic arm of the module. The co-abundance pattern suggests coordinated mitochondrial and cellular-maintenance biology, but does not establish altered respiratory-chain activity in either tissue.

#### CBR1

- **Related proteins** (co-abundance neighbors): ARPC5L (0.95), MESD (0.88), NDUFV2 (0.86), CZIB (0.85), UCK2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: carbonyl reductase 1. The protein encoded by this gene belongs to the short-chain dehydrogenases/reductases (SDR) family, which function as NADPH-dependent oxidoreductases having wide specificity for carbonyl compounds, such as quinones, prostaglandins, and various xenobiotics. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Nov 2013].
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); musculoskeletal system disorder (0.303); osteoporosis (0.276); Burkitt lymphoma (0.265); alcohol drinking (0.263)
- **Europe PMC papers**: 1837
- **Why important**: CBR1 has a central network position and connects metabolic, mitochondrial and structural neighborhoods through ARPC5L, MESD, NDUFV2, CZIB and UCK2. It is an NADPH-dependent oxidoreductase with broad carbonyl, quinone, prostanoid and xenobiotic activities. HPA shows tissue enhancement in choroid plexus and intestine and cell-type enhancement in epithelial and hepatic populations; the gene has substantial literature and disease associations.
- **Conclusion**: Established evidence supports CBR1 as a metabolic and redox interface, particularly relevant to epithelial or metabolically active cells. Its placement in the module is compatible with a detoxification or oxidative-stress hypothesis, but the specific substrate or tissue process responsible for the co-abundance signal remains unresolved.

#### NAA50

- **Related proteins** (co-abundance neighbors): HPRT1 (0.81), JPT2 (0.81), GGCT (0.80); STRING partners: HYPK (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06055.1, huMAP3_01027.1, huMAP3_10987.1, huMAP3_13394.1
- **Function (MyGene.info)**: N-alpha-acetyltransferase 50, NatE catalytic subunit. Enables H4 histone acetyltransferase activity; peptide alpha-N-acetyltransferase activity; and peptidyl-lysine acetyltransferase activity. Involved in N-terminal protein amino acid acetylation; establishment of mitotic sister chromatid cohesion; and mitotic sister chromatid cohesion, centromeric. Located in cytosol and nucleus. Part of NatA complex. [provided by Alliance of Genome Resources, Apr 2…
- **Diseases (Open Targets)**: musculoskeletal system disorder (0.174); Abnormality of the skeletal system (0.147); upper respiratory tract disorder (0.066); neuroblastoma (0.059); alcohol drinking (0.035)
- **Europe PMC papers**: 308
- **Why important**: NAA50 is connected to multiple module neighbors and is the most prominent complex-level anchor because it pairs with HYPK in several hu.MAP complexes (hu.MAP huMAP3_06055.1), (hu.MAP huMAP3_01027.1), (hu.MAP huMAP3_10987.1) and (hu.MAP huMAP3_13394.1). It is the catalytic subunit of NatE and participates in N-terminal protein acetylation and chromosome-cohesion biology. It is detected in cervix-uterine tissue and has documented disease and cancer-related associations.
- **Conclusion**: Established evidence supports NAA50 as a protein-processing and nuclear-machinery component, with particularly strong support for a physical relationship with HYPK from STRING and hu.MAP. It may help explain the module's proteostasis and biosynthetic arm, but the module does not demonstrate that NatE activity is globally enriched.

#### RHOG

- **Related proteins** (co-abundance neighbors): YWHAH (0.89), UCK2 (0.88), PRDX4 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ras homolog family member G. This gene encodes a member of the Rho family of small GTPases, which cycle between inactive GDP-bound and active GTP-bound states and function as molecular switches in signal transduction cascades. Rho proteins promote reorganization of the actin cytoskeleton and regulate cell shape, attachment, and motility. The encoded protein facilitates translocation of a functional guanine nucleotide exchange…
- **Diseases (Open Targets)**: atrial fibrillation (0.428); cancer (0.373); kidney transplant (0.296); eosinophilic esophagitis (0.239); cardiac arrhythmia (0.128)
- **Europe PMC papers**: 1929
- **Why important**: RHOG connects UCK2, YWHAH and PRDX4 and provides a signaling and cytoskeletal bridge within an otherwise metabolically and proteostatically mixed module. Its established role as a Rho-family molecular switch includes regulation of cell shape, polarity, actin organization and motility. HPA shows tissue enhancement in bone marrow and cell-type enhancement in several myeloid and epithelial-related populations, while the gene has broad literature and disease associations including arrhythmia and cancer.
- **Conclusion**: Established evidence supports RHOG as a plausible regulator of trafficking, adhesion and cytoskeletal adaptation. Its co-abundance with redox and nucleotide-metabolism genes is consistent with coordinated cellular remodeling, but a direct mechanistic connection in autonomic nervous system or cervix tissue is only a hypothesis.

## Module 1

**Tissue pair**: autonomic_nervous_system and cervix_uterine  
**Genes (45)**: PPP2R1B, NUDT1, ABHD14B, AIMP1, ARPC4, BID, CAMSAP2, CDK5, CARHSP1, CNN3, COMMD3, CORO1C, CROCC, DDX56, FXR1, GMPS, H1-2, HMGB3, HPCAL1, ITGB1, DTYMK, LYRM7, MMS19, EMG1, NTPCR, NUDT5, YOD1, PAFAH1B3, PDLIM2, PFDN4, PHF6, PML, PYM1, RAB18, RPS27L, SNRPA1, SNRPB2, SLC27A4, SNAP23, SSR1, STOM, SUCLG1, TOE1, TXNDC17, UCHL3

### Function

No GO/KEGG term passed global correction, so there is no globally significant pathway assignment for this module. The gene-level and network evidence instead supports a heterogeneous intracellular program with prominent RNA processing and post-transcriptional regulation, together with cytoskeletal organization, protein quality control, nucleotide metabolism, and stress or apoptosis-related functions. The strongest coherent anchor is RNA biology: SNRPA1 and SNRPB2 are U2 spliceosomal components, TOE1 performs snRNA three-prime-end processing, DDX56 is an RNA helicase associated with ribosome and spliceosome assembly, and EMG1 supports small-subunit ribosome biogenesis. Other branches include actin organization through CNN3, ARPC4, PDLIM2, and CORO1C; ubiquitin and proteostasis control through YOD1 and UCHL3; and genome or oxidative-stress protection through NUDT1, NUDT5, PML, and RPS27L. These functions should be viewed as an evidence-weighted interpretation of a mixed module, not as a formally enriched pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only AIMP1 is annotated as secreted to blood. It is also not broadly characterized as an immune-cell module, because most genes have low immune-cell specificity, although isolated signals occur in eosinophils, granulocytes, lymphocytes, platelets, and megakaryocytes. Most genes have low tissue specificity but substantial cell-type enhancement, with recurring annotations in germ-cell, esophageal, trophoblast, epithelial, neural, and platelet-related cell types. This pattern is more consistent with a mixture of broadly reusable intracellular programs and cell-state or cell-composition effects than with a simple blood-contamination signature. The cervix protein data support expression for many members, whereas the autonomic-nervous-system comparison has no matching HPA tissue protein data; therefore, the shared status should not be interpreted as equally validated at the protein level in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a small number of direct, high-confidence relationships: DDX56 with GMPS, EMG1 with RPS27L, NUDT1 with NUDT5, and SNRPA1 with SNRPB2. The SNRPA1-SNRPB2 relationship is especially informative because both proteins are U2 spliceosomal components and the pair is also represented in hu.MAP complexes. hu.MAP independently supports a spliceosome-related assembly containing SNRPB2, SNRPA1, and TOE1 in C1 and C2, with TOE1 and SNRPB2 also occurring together in C5. C3 links HMGB3 and CNN3, C4 links FXR1 and PYM1, and C6 links GMPS and BID. Thus, the module contains several biologically plausible islands, especially spliceosomal and RNA-processing structure, but most co-abundance edges are not established physical interactions. The absence of STRING functional enrichment means that these observations support local molecular relationships rather than a globally established pathway for the entire module.

**STRING interactions (score >= 0.7)**: 4 of 990 gene pairs: DDX56–GMPS (0.734); EMG1–RPS27L (0.864); NUDT1–NUDT5 (0.767); SNRPA1–SNRPB2 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06511.1 (SNRPB2, SNRPA1, TOE1; 3/79); huMAP3_08980.1 (SNRPB2, SNRPA1, TOE1; 3/97); huMAP3_11653.1 (HMGB3, CNN3; 2/17); huMAP3_10789.1 (FXR1, PYM1; 2/37); huMAP3_04549.1 (SNRPB2, TOE1; 2/52); huMAP3_14442.1 (GMPS, BID; 2/57)

### Novelty

The exact shared co-abundance module is plausibly a new observation, but the fact sheet does not establish novelty as a proven claim. The reason for considering it potentially novel is that the module combines several partially connected programs across autonomic nervous system and cervix tissue, while STRING shows only sparse direct interaction support and hu.MAP explains only selected subsets. The spliceosomal relationships and the individual functions of many genes are established, so the novelty is unlikely to be discovery of those molecular functions themselves. A stronger novelty claim would require comparison with published cross-tissue co-abundance modules, tissue deconvolution, independent cohorts, and replication of the module-preserving structure. Absence from STRING or hu.MAP alone is not evidence that the co-abundance pattern is novel.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular state in which RNA maturation and translation-related quality control are coordinated with cytoskeletal remodeling, membrane trafficking, and stress adaptation. In this model, the SNRPA1-SNRPB2-TOE1 axis supports regulated processing of nuclear RNAs, while DDX56 and EMG1 support ribosome or RNA-processing capacity; CNN3, ARPC4, PDLIM2, and CORO1C connect that state to actin and cell-adhesion architecture; and YOD1, NUDT1, NUDT5, BID, and PML provide proteostatic, oxidative-stress, and cell-survival control. The same program could arise from a shared epithelial, neural, trophoblast, germ-cell, or stromal state, or from coordinated cell-composition differences, rather than from a tissue-specific autonomic-cervical pathway. This hypothesis requires testing with single-cell localization, protein-level measurements in both tissues, perturbation of the spliceosomal and cytoskeletal branches, and replication in independent samples.

### Important genes

#### SNRPA1

- **Related proteins** (co-abundance neighbors): DTYMK (0.83), CROCC (0.81), SNRPB2 (0.81); STRING partners: SNRPB2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide A'. Enables RNA binding activity. Involved in mRNA splicing, via spliceosome and spermatogenesis. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome and U2-type precatalytic spliceosome. Implicated in connective tissue disease. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.538); dengue disease (0.370); phosphorus metabolism disease (0.196); hypotensive disorder (0.196); cancer (0.087)
- **Europe PMC papers**: 520
- **Why important**: SNRPA1 is a central representative of the RNA-processing interpretation. It has a relatively connected position in the module, forms a direct STRING relationship with SNRPB2, and occurs with SNRPB2 in hu.MAP complexes C1 and C2. Its established functions include RNA binding, U2 prespliceosome assembly, mRNA splicing, and spermatogenesis. The gene has a substantial literature base and disease associations including connective tissue disease and several neurological disease categories.
- **Conclusion**: Established evidence supports SNRPA1 as a spliceosomal component and as one of the best-supported molecular anchors of the module. It is plausible, but not demonstrated, that variation in SNRPA1 abundance helps couple the shared tissue state to altered RNA processing.

#### SNRPB2

- **Related proteins** (co-abundance neighbors): LYRM7 (0.83), SNRPA1 (0.81), TXNDC17 (0.81), HPCAL1 (0.81); STRING partners: SNRPA1 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1, huMAP3_04549.1
- **Function (MyGene.info)**: small nuclear ribonucleoprotein polypeptide B2. The protein encoded by this gene associates with stem loop IV of U2 small nuclear ribonucleoprotein (U2 snRNP) in the presence of snRNP-A'. The encoded protein may play a role in pre-mRNA splicing. Autoantibodies from patients with systemic lupus erythematosus frequently recognize epitopes on the encoded protein. Two transcript variants encoding the same protein have been found for this gene. [pro…
- **Diseases (Open Targets)**: neurodegenerative disease (0.372); dengue disease (0.370); sleep apnea syndrome (0.233); preeclampsia (0.111); gestational diabetes (0.111)
- **Europe PMC papers**: 336
- **Why important**: SNRPB2 is directly connected to SNRPA1 in STRING and is present with SNRPA1 and TOE1 in hu.MAP complexes C1 and C2, with TOE1 also represented in C5. Its annotation directly supports U2 snRNP assembly, prespliceosome assembly, and pre-mRNA splicing. Its position connects the spliceosomal branch to TXNDC17, HPCAL1, and LYRM7, linking RNA processing to redox, neuronal, and mitochondrial-associated signals.
- **Conclusion**: Established evidence identifies SNRPB2 as a strong structural anchor for the module's RNA-splicing interpretation. A coordinated SNRPA1-SNRPB2 signal is more informative than either gene alone, but whether it reflects altered splicing activity or merely shared abundance remains unresolved.

#### TOE1

- **Related proteins** (co-abundance neighbors): PPP2R1B (0.87), PHF6 (0.86), FXR1 (0.85), AIMP1 (0.83), DDX56 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06511.1, huMAP3_08980.1, huMAP3_04549.1
- **Function (MyGene.info)**: target of EGR1, exonuclease. Enables poly(A)-specific ribonuclease activity and snRNA binding activity. Involved in RNA phosphodiester bond hydrolysis, exonucleolytic and snRNA 3'-end processing. Located in Cajal body and cytoplasm. Implicated in pontocerebellar hypoplasia type 7. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 7 (0.823); neurodegenerative disease (0.541); classic familial adenomatous polyposis (0.539); mutyh-associated polyposis (0.539); hereditary neoplastic syndrome (0.479)
- **Europe PMC papers**: 736
- **Why important**: TOE1 has a relatively connected position and is the only module member shared across several hu.MAP complexes centered on spliceosomal machinery, specifically C1, C2, and C5. It has established poly-A-specific ribonuclease activity, snRNA binding, and snRNA three-prime-end processing functions, and is implicated in pontocerebellar hypoplasia type seven. Its links to FXR1, PHF6, AIMP1, DDX56, and PPP2R1B make it a bridge between RNA maturation and broader regulatory processes.
- **Conclusion**: Established evidence supports TOE1 as a mechanistically meaningful RNA-processing component. Its repeated complex membership makes it a stronger candidate than a generic housekeeping marker, although the module does not prove that TOE1 activity is altered in either tissue.

#### CNN3

- **Related proteins** (co-abundance neighbors): CDK5 (0.97), SSR1 (0.91), ARPC4 (0.90), TXNDC17 (0.89), SUCLG1 (0.82), H1-2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_11653.1
- **Function (MyGene.info)**: calponin 3. This gene encodes a protein with a markedly acidic C terminus; the basic N-terminus is highly homologous to the N-terminus of a related gene, CNN1. Members of the CNN gene family all contain similar tandemly repeated motifs. This encoded protein is associated with the cytoskeleton but is not involved in contraction. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.492); pleural empyema (0.256); pneumothorax (0.256); biliary tract disorder (0.247); tooth disorder (0.196)
- **Europe PMC papers**: 1628
- **Why important**: CNN3 has the strongest network position in the supplied subgraph and connects actin-associated partners with CDK5, SSR1, TXNDC17, SUCLG1, and H1-2. Its established functions include actin filament organization, actomyosin structure organization, epithelial differentiation, and cell-cell adhesion. HPA places its protein at actin filaments and detects it in cervix, while its cell-type annotations include Schwann and epithelial-related cells. It also has a comparatively large literature base.
- **Conclusion**: Established evidence supports CNN3 as the main cytoskeletal and adhesion anchor of the module. Its strong connectivity suggests that it may help connect RNA-processing abundance to cellular architecture, but that cross-domain coupling is a hypothesis rather than a demonstrated physical mechanism.

#### YOD1

- **Related proteins** (co-abundance neighbors): PAFAH1B3 (0.88), BID (0.87), COMMD3 (0.87), STOM (0.85), SNAP23 (0.84), SLC27A4 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: YOD1 deubiquitinase. Protein ubiquitination controls many intracellular processes, including cell cycle progression, transcriptional activation, and signal transduction. This dynamic process, involving ubiquitin conjugating enzymes and deubiquitinating enzymes, adds and removes ubiquitin. Deubiquitinating enzymes are cysteine proteases that specifically cleave ubiquitin from ubiquitin-conjugated protein substrates. Th…
- **Diseases (Open Targets)**: smoking initiation (0.406); atrial fibrillation (0.348); neoplasm (0.103); Alzheimer disease (0.082); pancreatic neoplasm (0.080)
- **Europe PMC papers**: 727
- **Why important**: YOD1 has a relatively connected position and links PAFAH1B3, BID, COMMD3, STOM, SNAP23, and SLC27A4. It is an OTU-family deubiquitinase with established roles in ER-associated degradation, the unfolded-protein response, macroautophagy, and multiple ubiquitin-linkage processes. HPA reports tissue enhancement in bone marrow and cell-type annotations spanning epithelial, erythrocyte, and germ-cell populations. Its disease associations include atrial fibrillation, neurodegenerative disease, and neoplastic conditions.
- **Conclusion**: Established evidence supports YOD1 as a proteostasis and stress-response component that could complement the RNA-processing branch. Its presence does not establish ER stress in the module, but it makes protein-quality control a biologically credible secondary interpretation.

#### CDK5

- **Related proteins** (co-abundance neighbors): CNN3 (0.97), NUDT1 (0.82), GMPS (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclin dependent kinase 5. This gene encodes a proline-directed serine/threonine kinase that is a member of the cyclin-dependent kinase family of proteins. Unlike other members of the family, the protein encoded by this gene does not directly control cell cycle regulation. Instead the protein, which is predominantly expressed at high levels in mammalian postmitotic central nervous system neurons, functions in diverse proces…
- **Diseases (Open Targets)**: Alzheimer disease (0.680); lissencephaly 7 with cerebellar hypoplasia (0.680); neurodegenerative disease (0.480); Parkinson disease (0.379); autoimmune disorder of central nervous system (0.366)
- **Europe PMC papers**: 12790
- **Why important**: CDK5 connects CNN3 with NUDT1 and GMPS and provides a functional bridge between cytoskeletal organization, neuronal biology, and nucleotide or oxidative-stress-associated genes. Its established functions include neuronal migration, axonogenesis, synapse assembly, synaptic vesicle exocytosis, and microtubule organization. It has a large literature base and well-established associations with Alzheimer disease, Parkinson disease, lissencephaly, and other neurological conditions. HPA reports tissue enhancement in brain and protein detection in cervix.
- **Conclusion**: Established evidence supports CDK5 as a neuronal and cytoskeletal regulator that is relevant to the autonomic-nervous-system side of the tissue pair. Its presence in a shared module does not prove a neuron-specific module, because HPA also reports cervix detection and the module contains many broadly or variably expressed genes.

## Module 2

**Tissue pair**: autonomic_nervous_system and cervix_uterine  
**Genes (12)**: NT5E, PGD, ABLIM1, ALB, PAM, APOH, ARPC5, CDK5RAP3, AHSG, MYO1B, NDUFS4, LTF

### Function

The module does not have any GO or KEGG term that passes global multiple-testing correction, so no pathway-level function can be assigned from primary enrichment evidence. Its strongest biological interpretation comes from the gene identities and network structure: a circulating plasma-protein and secretory-protein axis centered on ALB, AHSG, APOH, and LTF, with additional links to extracellular nucleotide metabolism, neuroendocrine peptide maturation, cytoskeletal organization, pentose-phosphate metabolism, and mitochondrial respiration. The STRING supplementary terms support signal, secretion, disulfide-bonded proteins, and glycoproteins (STRING Keyword Signal; within-query FDR = 0.0141) (STRING Keyword Secreted; within-query FDR = 0.0141) (STRING Keyword Disulfide bond; within-query FDR = 0.0141) (STRING Keyword Glycoprotein; within-query FDR = 0.0159), but these are supplementary rather than globally corrected enrichment evidence. The module therefore most plausibly reflects a shared extracellular or blood-associated protein environment, with smaller tissue-cellular components rather than one coherent intracellular pathway.

**Cell composition.** The composition strongly suggests a plasma or secreted-protein component. ALB, AHSG, APOH, and LTF are secreted to blood or otherwise secreted proteins, and PAM is secreted in other tissues; the STRING supplementary annotations also identify secretion and signal-related features (STRING Keyword Signal; within-query FDR = 0.0141) (STRING Keyword Secreted; within-query FDR = 0.0141). HPA places ALB, AHSG, and APOH as liver- or hepatocyte-enriched, while LTF is associated with bone marrow, salivary gland, neutrophil progenitors, and neutrophils. Several genes show immune-cell or blood-cell enhancement, especially PGD, LTF, NT5E, and ARPC5, while other genes are broadly expressed or associated with housekeeping-like cellular functions. The cervix protein data detect several module proteins, but the absence of matched autonomic-nervous-system protein data prevents tissue-specific comparison. Thus, the shared module may partly reflect plasma carryover, vascular or stromal exposure, secretory material, or shared cell types in the samples rather than a specialized autonomic-cervical biological program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a compact known interaction core involving AHSG, ALB, APOH, and LTF. The strongest reported relationships are AHSG with ALB, AHSG with APOH, ALB with APOH, and ALB with LTF; AHSG with LTF is also supported. These relationships are consistent with known extracellular plasma-protein associations and do not establish a novel physical complex. hu.MAP independently places APOH, AHSG, and ALB together in one complex and repeatedly places AHSG with ALB in several broader serum-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08700.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). The ABLIM1 and MYO1B pair occurs in a separate actin-associated hu.MAP complex (hu.MAP huMAP3_09542.1). Most module edges lack STRING partners or hu.MAP support, so the complete co-abundance network is not equivalent to one established molecular complex. The evidence instead indicates a known plasma-protein subnetwork embedded within a broader, partly tissue- or sample-context-dependent co-abundance pattern.

**STRING interactions (score >= 0.7)**: 5 of 66 gene pairs: AHSG–ALB (0.999); AHSG–APOH (0.957); AHSG–LTF (0.744); ALB–APOH (0.933); ALB–LTF (0.996)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Signal (FDR = 0.0141, 6 genes); Keyword Secreted (FDR = 0.0141, 5 genes); Keyword Disulfide bond (FDR = 0.0141, 6 genes); Keyword Glycoprotein (FDR = 0.0159, 6 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (APOH, AHSG, ALB; 3/64); huMAP3_08700.1 (AHSG, ALB; 2/11); huMAP3_07432.1 (AHSG, ALB; 2/18); huMAP3_07265.1 (AHSG, ALB; 2/20); huMAP3_09434.1 (AHSG, ALB; 2/33); huMAP3_09542.1 (ABLIM1, MYO1B; 2/38); huMAP3_08395.1 (AHSG, ALB; 2/43); huMAP3_09531.1 (AHSG, ALB; 2/47); huMAP3_10101.1 (AHSG, ALB; 2/49); huMAP3_10678.1 (AHSG, ALB; 2/71)

### Novelty

This module should not be described as a newly discovered molecular pathway. Its central plasma-protein relationships are already represented in STRING and hu.MAP, and the liver and blood-associated expression pattern provides a conventional explanation for their co-abundance. A potentially novel aspect could be the reproducible sharing of this composite module between autonomic nervous system and cervix uterine samples, particularly the connection of the established plasma-protein core with PAM, PGD, ABLIM1, MYO1B, NDUFS4, CDK5RAP3, ARPC5, and NT5E. However, database absence for individual edges does not prove novelty, and no global GO or KEGG enrichment supports a newly defined pathway. Novelty therefore remains a testable observation about cross-tissue co-abundance, not an established mechanistic discovery.

**Hypothesis.** Hypothesis: the conserved module reflects a shared extracellular and vascular milieu in the two tissue groups, in which liver-derived plasma proteins and secreted innate-defense proteins co-vary with local epithelial, endothelial, immune, or stromal-cell signals. ALB, AHSG, and APOH may form the circulating carrier and glycoprotein core; LTF may report secretory or neutrophil-associated innate defense; NT5E may connect the extracellular protein environment to local purinergic signaling; and PAM may indicate neuroendocrine secretory activity. PGD, ABLIM1, ARPC5, and MYO1B could represent cellular metabolic or cytoskeletal contributions from the sampled tissue or accompanying cells. This hypothesis predicts that the module will correlate with plasma contamination or vascular exposure, hepatocyte-derived protein abundance, immune or secretory-cell content, and local extracellular nucleotide signaling. It requires validation with deconvolution, matched plasma measurements, cell-resolved data, and independent tissue cohorts.

### Important genes

#### ALB

- **Related proteins** (co-abundance neighbors): NDUFS4 (0.86), APOH (0.81); STRING partners: AHSG (0.999), APOH (0.933), LTF (0.996)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08700.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is a central member of the known extracellular core: it connects to APOH, AHSG, and LTF in STRING and appears with AHSG across many hu.MAP serum-protein complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08700.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). HPA identifies it as liver- and hepatocyte-enriched and secreted to blood. Its function as the major circulating carrier protein makes it a strong marker of plasma-derived composition. It also has substantial literature and disease annotation, including disorders involving albumin or circulating transport.
- **Conclusion**: Established evidence: ALB is a highly connected, liver-derived, blood-secreted carrier protein and a major anchor of the known plasma-protein subnetwork. Conclusion: ALB most likely reports the extracellular plasma component of the module rather than a tissue-specific autonomic or cervical mechanism.

#### AHSG

- **Related proteins** (co-abundance neighbors): ARPC5 (0.81); STRING partners: ALB (0.999), APOH (0.957), LTF (0.744)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_08700.1, huMAP3_07432.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1, huMAP3_10678.1
- **Function (MyGene.info)**: alpha 2-HS glycoprotein. The protein encoded by this gene is a negatively-charged serum glycoprotein that is synthesized by hepatocytes. The encoded protein consists of two polypeptide chains, which are both cleaved from a proprotein encoded from a single mRNA. It is involved in several processes, including endocytosis, brain development, and the formation of bone tissue. Defects in this gene are a cause of susceptibility…
- **Diseases (Open Targets)**: alopecia - intellectual disability syndrome (0.476); otosclerosis (0.465); nephrolithiasis, calcium oxalate (0.417); calcium oxalate urolithiasis (0.416); neurodegenerative disease (0.204)
- **Europe PMC papers**: 2310
- **Why important**: AHSG is connected to ALB, APOH, and LTF in STRING and participates with ALB in multiple hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_08700.1) (hu.MAP huMAP3_07432.1) (hu.MAP huMAP3_07265.1) (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1) (hu.MAP huMAP3_10678.1). HPA identifies it as liver- and hepatocyte-enriched and secreted to blood. Its annotated roles in acute-phase response, endocytosis, and regulation of bone mineralization provide plausible links between circulating proteins and extracellular tissue biology. It has a substantial literature base and disease associations involving mineralization, kidney stones, and neurodegenerative disease.
- **Conclusion**: Established evidence: AHSG is a liver-derived circulating glycoprotein embedded in a well-supported serum-protein interaction network. Conclusion: AHSG is an important indicator of the module's systemic extracellular origin, while any local signaling role in the two tissues remains hypothetical.

#### APOH

- **Related proteins** (co-abundance neighbors): NT5E (0.85), ARPC5 (0.83), ALB (0.81); STRING partners: AHSG (0.957), ALB (0.933)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: apolipoprotein H. Apolipoprotein H, also known as beta-2-glycoprotein I, is a component of circulating plasma lipoproteins. It has been implicated in a variety of physiologic pathways including lipoprotein metabolism, coagulation, hemostasis, and the production of antiphospholipid autoantibodies. APOH may be a required cofactor for anionic phospholipid binding by the antiphospholipid autoantibodies found in sera of…
- **Diseases (Open Targets)**: atrial fibrillation (0.549); metabolic syndrome (0.502); Hypercholesterolemia (0.501); aortic stenosis (0.473); familial lipoprotein lipase deficiency (0.460)
- **Europe PMC papers**: 3121
- **Why important**: APOH has high network connectivity through NT5E, ARPC5, and ALB and is linked to AHSG and ALB in STRING; it also occurs with AHSG and ALB in hu.MAP (hu.MAP huMAP3_15040.1). HPA identifies it as liver- and hepatocyte-enriched and secreted to blood. Its annotated roles in lipoprotein metabolism, coagulation, hemostasis, endothelial regulation, and antiphospholipid autoantibodies make it biologically relevant to vascular and immune interpretations. It has disease associations involving atrial fibrillation, metabolic syndrome, hypercholesterolemia, and aortic stenosis, with substantial literature support.
- **Conclusion**: Established evidence: APOH is a circulating liver-derived protein connecting the plasma core to NT5E and ARPC5. Conclusion: APOH may be the most informative bridge between the module's extracellular plasma signal and local vascular, immune, or nucleotide-related biology, but that bridge is a hypothesis rather than demonstrated tissue mechanism.

#### LTF

- **Related proteins** (co-abundance neighbors): PAM (0.92), NDUFS4 (0.86); STRING partners: AHSG (0.744), ALB (0.996)
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactotransferrin. This gene is a member of the transferrin family of genes and its protein product is found in the secondary granules of neutrophils. The protein is a major iron-binding protein in milk and body secretions with an antimicrobial activity, making it an important component of the non-specific immune system. The protein demonstrates a broad spectrum of properties, including regulation of iron homeostasi…
- **Diseases (Open Targets)**: tuberculosis (0.517); AL amyloidosis (0.467); Abnormality of the skeletal system (0.435); schizophrenia (0.235); inflammatory bowel disease (0.218)
- **Europe PMC papers**: 7000
- **Why important**: LTF connects to PAM and NDUFS4 in the co-abundance graph and to ALB and AHSG in STRING. It contributes to the supplementary signal, secreted, disulfide-bond, and glycoprotein annotations (STRING Keyword Signal; within-query FDR = 0.0141) (STRING Keyword Secreted; within-query FDR = 0.0141) (STRING Keyword Disulfide bond; within-query FDR = 0.0141) (STRING Keyword Glycoprotein; within-query FDR = 0.0159). HPA associates it with bone marrow, salivary gland, neutrophil progenitors, neutrophils, and non-classical monocytes, and identifies it as secreted to blood. Its established functions include iron binding, mucosal innate defense, antimicrobial activity, cytokine regulation, and humoral immunity. It has a large literature base and disease associations involving infection, amyloidosis, skeletal abnormalities, and inflammatory bowel disease.
- **Conclusion**: Established evidence: LTF is a secreted innate-defense and iron-binding protein with strong links to neutrophil and glandular biology. Conclusion: LTF may indicate immune or secretory-cell contribution to the shared module, but its co-abundance with mitochondrial and neuroendocrine genes does not prove a unified intracellular pathway.

#### PAM

- **Related proteins** (co-abundance neighbors): LTF (0.92), PGD (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: peptidylglycine alpha-amidating monooxygenase. This gene encodes a multifunctional protein. The encoded preproprotein is proteolytically processed to generate the mature enzyme. This enzyme includes two domains with distinct catalytic activities, a peptidylglycine alpha-hydroxylating monooxygenase (PHM) domain and a peptidyl-alpha-hydroxyglycine alpha-amidating lyase (PAL) domain. These catalytic domains work sequentially to catalyze the conve…
- **Diseases (Open Targets)**: type 2 diabetes mellitus (0.593); diabetes mellitus (0.538); Abnormality of the skeletal system (0.517); intelligence (0.492); diabetic eye disease (0.451)
- **Europe PMC papers**: 50367
- **Why important**: PAM links LTF and PGD in the module and contributes to all supplementary STRING keyword terms (STRING Keyword Signal; within-query FDR = 0.0141) (STRING Keyword Secreted; within-query FDR = 0.0141) (STRING Keyword Disulfide bond; within-query FDR = 0.0141) (STRING Keyword Glycoprotein; within-query FDR = 0.0159). HPA shows tissue enhancement in epididymis and heart muscle and cell-type enhancement in cardiomyocytes, myonuclei, neuroendocrine cells, and pituicytes or FSCs; it is found in the Golgi apparatus and cytosol and is secreted in other tissues. Its established enzymatic role is the sequential processing required to produce active alpha-amidated neuroendocrine peptides. It has very substantial literature and disease associations involving diabetes and skeletal abnormalities.
- **Conclusion**: Established evidence: PAM is a Golgi-associated peptide-maturation enzyme with secretory and neuroendocrine relevance. Conclusion: PAM provides a plausible local secretory or neuroendocrine component linking the plasma-protein signal to autonomic or cervical biology, but the module alone cannot establish that this process drives the shared pattern.

## Module 3

**Tissue pair**: autonomic_nervous_system and cervix_uterine  
**Genes (37)**: PRKAG1, ANXA5, ATM, ATP5F1C, AURKA, CDK1, CLIC1, CMBL, COX20, COXFA4, CACYBP, GNPDA1, HMOX2, HSPA8, HSPB1, EIF4E, PKM, MACROD1, MANF, RNGTT, APOO, NAA20, NEK7, CBFB, PPCS, PRDX3, PSMA1, PSMB8, PSMF1, PTS, RAN, RAB22A, RPL3, MRPS15, SEC22B, TXN, THYN1

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway label from primary enrichment evidence. The gene composition and network instead suggest a composite cellular maintenance module involving proteasome-associated protein quality control, translation and ribosome-related activity, mitochondrial energy and redox homeostasis, stress responses, and cell-cycle regulation. The strongest mechanistic anchors are the proteasome group formed by PSMA1, PSMB8, and PSMF1, the redox relationship between TXN and PRDX3, mitochondrial genes such as COXFA4 and ATP5F1C, and the cell-cycle relationships involving CDK1, AURKA, ATM, and NEK7. These interpretations are functional hypotheses from gene annotations and network structure, not globally significant enrichment results.

**Cell composition.** This does not look like a plasma-protein or broadly secreted module. Only a small secreted component is reported, while most genes have low tissue specificity and low immune-cell specificity. HPA evidence identifies a few tissue-enhanced patterns, including esophageal, muscle, heart, tongue, and lymphoid-associated signals, but no coherent blood-cell signature: only a small minority of genes are immune-cell enhanced, and some are not detected in immune cells. The module is therefore unlikely to be explained primarily by blood contamination or a generic leukocyte population. Its broad cellular distribution and the presence of translation, proteasome, mitochondrial, chaperone, and metabolic genes are consistent with a shared housekeeping or stress-associated cellular program. Cervix protein detection is available for many module genes, whereas there is no matching HPA tissue for the autonomic nervous system, so protein-level comparability between the two tissues remains limited.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports selected established relationships rather than a densely connected interaction network. Known examples include PSMA1 with PSMB8 and PSMF1, PSMB8 with PSMF1, AURKA with CDK1, ATM with CDK1, HSPA8 with HSPB1, PRDX3 with TXN, and mitochondrial or ribosomal links involving ATP5F1C, COXFA4, RPL3, and MRPS15. hu.MAP independently places PSMA1, PSMB8, and PSMF1 together in multiple proteasome-related complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). Thus, the proteasome submodule is supported by known physical or functional complex membership, while many other module edges lack corresponding STRING or hu.MAP support. The overall module is consequently a mixture of a validated proteasome core and more weakly supported co-abundance associations.

**STRING interactions (score >= 0.7)**: 10 of 666 gene pairs: ATM–CDK1 (0.733); ATP5F1C–COXFA4 (0.802); ATP5F1C–RPL3 (0.741); AURKA–CDK1 (0.951); HSPA8–HSPB1 (0.988); MRPS15–RPL3 (0.828); PRDX3–TXN (0.846); PSMA1–PSMB8 (0.999); PSMA1–PSMF1 (0.985); PSMB8–PSMF1 (0.84)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00356.1 (PSMA1, PSMB8, PSMF1; 3/33); huMAP3_09656.1 (PSMA1, PSMB8, PSMF1; 3/64); huMAP3_13725.1 (PSMA1, PSMF1; 2/69)

### Novelty

The module-level finding may be novel as a conserved co-abundance pattern shared by autonomic_nervous_system and cervix_uterine, because the supplied databases mainly validate individual interactions and the proteasome complex rather than this exact cross-tissue grouping. However, it should not be described as a newly discovered molecular complex or pathway. Several components and relationships are already well established, especially the proteasome, cell-cycle kinase, chaperone, redox, mitochondrial, and translation functions. The absence of an interaction from STRING or hu.MAP is not evidence of novelty. A defensible claim is therefore that the cross-tissue co-abundance configuration is potentially novel, while its constituent biology is largely known and heterogeneous.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular resilience state rather than a tissue-specific pathway. In cells present in both tissue contexts, proteasome activity may coordinate removal of damaged or misfolded proteins with translation control, while mitochondrial respiration and TXN–PRDX3 redox buffering manage metabolic and oxidative stress. CDK1, AURKA, ATM, and NEK7 may connect this maintenance state to proliferation, checkpoint control, or cell-cycle-related variation. The co-abundance pattern could therefore arise when differences in cellular stress, protein turnover, metabolic demand, and proliferative state are coordinated across samples. This hypothesis requires validation with cell-composition adjustment, independent cohorts, perturbation experiments, and direct measurement of proteasome, mitochondrial, and redox activity.

### Important genes

#### PSMA1

- **Related proteins** (co-abundance neighbors): APOO (0.89), MANF (0.88), CMBL (0.81), HMOX2 (0.80); STRING partners: PSMB8 (0.999), PSMF1 (0.985)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 20S subunit alpha 1. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.535); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1417
- **Why important**: PSMA1 is a highly connected module gene and occupies the centre of the proteasome-associated submodule. It is supported by STRING relationships with PSMB8 and PSMF1 and by membership in all three reported hu.MAP proteasome complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). Its annotation supports proteasomal protein catabolism, DNA damage response, and apoptotic processes. It also has substantial literature and disease associations involving plasma-cell myeloma, lymphoma, neoplasm, HIV infection, and amyloidosis.
- **Conclusion**: Established evidence supports PSMA1 as a structural and functional marker of the proteasome component of the module. Its co-abundance with the other module genes may indicate coordinated protein-quality control, but the data do not establish that PSMA1 regulates the entire module or that the module is driven by proteasome activity.

#### PSMB8

- **Related proteins** (co-abundance neighbors): CBFB (0.95), PSMF1 (0.86), EIF4E (0.85), ATP5F1C (0.82); STRING partners: PSMA1 (0.999), PSMF1 (0.84)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1
- **Function (MyGene.info)**: proteasome 20S subunit beta 8. The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent proc…
- **Diseases (Open Targets)**: proteosome-associated autoinflammatory syndrome (0.829); plasma cell myeloma (0.618); mantle cell lymphoma (0.542); neoplasm (0.536); amyloidosis (0.472)
- **Europe PMC papers**: 3589
- **Why important**: PSMB8 is highly connected within the module and is directly linked to PSMA1 and PSMF1 by STRING. It occurs with those genes in the hu.MAP proteasome complexes (hu.MAP huMAP3_00356.1) and (hu.MAP huMAP3_09656.1). Its annotation includes proteasomal protein catabolism and immunoproteasome-related immune functions, while HPA indicates broad tissue distribution and low immune-cell specificity. It has established associations with proteasome-associated autoinflammatory syndrome, plasma-cell myeloma, lymphoma, neoplasm, and amyloidosis.
- **Conclusion**: Established evidence identifies PSMB8 as a proteasome and immunoproteasome-related component, not as proof of immune-cell contamination. A plausible interpretation is that it contributes to regulated protein turnover or stress adaptation in the shared cellular context, but the absence of globally significant enrichment prevents a stronger pathway claim.

#### PSMF1

- **Related proteins** (co-abundance neighbors): EIF4E (0.89), PSMB8 (0.86), CLIC1 (0.83); STRING partners: PSMA1 (0.985), PSMB8 (0.84)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_00356.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome inhibitor subunit 1. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: complex neurodevelopmental disorder with motor features (0.399); placental abruption (0.318); methicillin-resistant staphylococcus aureus infectious disease (0.308); jaw disease (0.209); neurodegenerative disease (0.188)
- **Europe PMC papers**: 411
- **Why important**: PSMF1 connects the proteasome genes with EIF4E and CLIC1 in the co-abundance network and is present in all reported hu.MAP proteasome complexes (hu.MAP huMAP3_00356.1), (hu.MAP huMAP3_09656.1), and (hu.MAP huMAP3_13725.1). Its annotation describes inhibition or regulation of proteasomal protein catabolism. It has fewer literature reports than the major proteasome subunits but has disease associations involving neurodevelopmental disorder, placental abruption, infection, jaw disease, and neurodegeneration.
- **Conclusion**: Established evidence supports PSMF1 as a regulatory proteasome-associated gene and a useful bridge between the validated proteasome core and the broader module. Its centrality supports coordinated proteostasis as a hypothesis, but co-abundance alone cannot determine whether PSMF1 is an active regulator or simply tracks proteasome abundance.

#### CDK1

- **Related proteins** (co-abundance neighbors): NEK7 (0.87), PRKAG1 (0.80), PTS (0.80); STRING partners: ATM (0.733), AURKA (0.951)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclin dependent kinase 1. The protein encoded by this gene is a member of the Ser/Thr protein kinase family. This protein is a catalytic subunit of the highly conserved protein kinase complex known as M-phase promoting factor (MPF), which is essential for G2/M phase transitions of eukaryotic cell cycle. Mitotic cyclins stably associate with this protein and function as regulatory subunits. The kinase activity of this prote…
- **Diseases (Open Targets)**: neurodegenerative disease (0.535); Alzheimer disease (0.526); Parkinson disease (0.523); lysosomal storage disease (0.512); prostatitis (0.404)
- **Europe PMC papers**: 33995
- **Why important**: CDK1 links the module to mitotic control and connects to NEK7 and PRKAG1 in the module network. STRING supports relationships with AURKA and ATM. Its established function as the catalytic component of the M-phase-promoting complex and its annotations for G1/S and G2/M transitions, DNA replication, DNA repair, and chromatin remodeling make it the clearest cell-cycle representative. It has extensive literature and disease associations including neurodegenerative disease, Alzheimer disease, Parkinson disease, lysosomal storage disease, and prostatitis.
- **Conclusion**: Established evidence supports CDK1 as a cell-cycle and checkpoint-related component. Its presence may indicate proliferative or repair-state variation in the sampled cells, particularly given HPA cell-type enhancement in progenitor and trophoblast-related populations. It does not demonstrate that the entire module is a proliferation module.

#### TXN

- **Related proteins** (co-abundance neighbors): PTS (0.83), COXFA4 (0.81), COX20 (0.81), RPL3 (0.80); STRING partners: PRDX3 (0.846)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thioredoxin. The protein encoded by this gene acts as a homodimer and is involved in many redox reactions. The encoded protein is active in the reversible S-nitrosylation of cysteines in certain proteins, which is part of the response to intracellular nitric oxide. This protein is found in the cytoplasm. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct…
- **Diseases (Open Targets)**: neurodegenerative disease (0.530); smoking initiation (0.288); ovarian neoplasm (0.171); cancer (0.122); neoplasm (0.114)
- **Europe PMC papers**: 4080
- **Why important**: TXN is connected to PRDX3, COXFA4, COX20, RPL3, and PTS, thereby linking redox control with mitochondrial, translational, and metabolic parts of the module. Its annotation supports cellular redox homeostasis, hydrogen-peroxide detoxification, and reversible protein S-nitrosylation. HPA shows tissue enhancement in esophagus and cell-type enhancement across epithelial and progenitor-like populations. It has substantial literature and disease associations involving neurodegeneration, smoking initiation, ovarian neoplasm, and cancer.
- **Conclusion**: Established evidence supports TXN as a redox-homeostasis component that could connect mitochondrial and stress-related signals. The network is compatible with a redox-buffering role in the shared module, but the data do not show that oxidative stress is the initiating cause of the co-abundance pattern.

#### HMOX2

- **Related proteins** (co-abundance neighbors): ATP5F1C (0.82), EIF4E (0.82), APOO (0.80), PSMA1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heme oxygenase 2. Heme oxygenase, an essential enzyme in heme catabolism, cleaves heme to form biliverdin, which is subsequently converted to bilirubin by biliverdin reductase, and carbon monoxide, a putative neurotransmitter. Heme oxygenase activity is induced by its substrate heme and by various nonheme substances. Heme oxygenase occurs as 2 isozymes, an inducible heme oxygenase-1 and a constitutive heme oxygenas…
- **Diseases (Open Targets)**: autoimmune disorder of central nervous system (0.229); migraine disorder (0.154); schizophrenia (0.140); skin cancer (0.134); cancer (0.085)
- **Europe PMC papers**: 2039
- **Why important**: HMOX2 has strong network connections to ATP5F1C, EIF4E, APOO, and PSMA1, linking heme metabolism with mitochondrial, translation-related, lipid-associated, and proteasome-associated signals. Its established functions include heme oxidation, heme catabolism, responses to hypoxia, and responses to oxidative stress. It has substantial literature and disease associations involving central nervous system autoimmunity, migraine, schizophrenia, skin cancer, and cancer.
- **Conclusion**: Established evidence supports HMOX2 as a constitutive heme-catabolism and stress-response component. Its position suggests a possible bridge between oxygen or redox handling and proteostasis, but this bridge is a mechanistic hypothesis rather than a demonstrated causal relationship.

## Module 4

**Tissue pair**: autonomic_nervous_system and cervix_uterine  
**Genes (42)**: ABCB6, AMPD2, ASCC3, RNF40, MTHFD1L, TRIP10, CPSF6, CSTF2, DHX36, FAF1, TBRG4, GLS, GSR, HNRNPLL, KPNA2, INTS3, ISY1, LANCL1, IGF2R, MSH6, MYO1C, NAA15, NCKAP1, NDRG3, NELFE, NLN, NUP160, OAT, PDXDC1, PSPC1, PUM1, ERC1, RBBP7, RAB3GAP2, RBM12, RFC3, SEC63, SMS, GTF3C1, TLN1, TMEM109, ATP6V1A

### Function

No GO or KEGG term passed global correction, so the module has no globally significant pathway annotation. The gene and network evidence instead suggests a broad intracellular maintenance program combining RNA processing and post-transcriptional regulation, nucleocytoplasmic transport, protein targeting and quality control, intermediary metabolism, vesicle trafficking, and cytoskeletal organization. RBM12 is the strongest network hub and is linked to RNA splicing; NUP160 and KPNA2 connect the module to nuclear transport; CPSF6 and CSTF2 provide a more specific RNA three-prime-end processing connection; SEC63 supports endoplasmic-reticulum protein translocation; and GLS, OAT, AMPD2, GSR, and MTHFD1L represent metabolic and redox functions. These are functional inferences from the gene identities and network architecture, not evidence of a significantly enriched pathway.

**Cell composition.** This is not a plasma or secreted-protein module: only one gene is classified as secreted, while most are intracellular proteins located in the nucleus, cytosol, mitochondria, endoplasmic reticulum, Golgi, or vesicles. Most genes have low tissue specificity and low immune-cell specificity, arguing for a broadly expressed housekeeping or cellular-maintenance component rather than a tissue-exclusive program. Nevertheless, the HPA data show cell-type-enhanced genes in neural, glial, reproductive, epithelial, vascular, renal, and myeloid populations, with a subset enhanced in monocytes or neutrophils. The shared signal could therefore reflect conserved intracellular biology across the two tissues, shared cell types, or sample-composition effects; the available evidence does not establish a blood-derived module. Protein detection in cervix uterine is widespread among the genes, whereas there is no matching HPA tissue for autonomic nervous system, limiting tissue-level comparison.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small amount of high-confidence support: CPSF6 is connected to CSTF2, and CPSF6 is also connected to PSPC1. These relationships support a localized RNA-processing and nuclear-RNA organization subnetwork, but they do not support the whole module as one established physical complex. hu.MAP provides several partial complex overlaps. NUP160, INTS3, and TBRG4 occur together in (hu.MAP huMAP3_11232.1); KPNA2 and NUP160 recur in nuclear-pore or nuclear-transport complexes (hu.MAP huMAP3_09825.1) and (hu.MAP huMAP3_12581.1); RBM12 and TLN1 overlap in (hu.MAP huMAP3_14982.1); NUP160 and INTS3 recur in (hu.MAP huMAP3_10202.1); and GLS with MTHFD1L overlap in a mitochondrial metabolic complex (hu.MAP huMAP3_13468.1). Because each overlap contains only a small subset of the corresponding complex, the module appears to combine several known cellular subsystems rather than represent one canonical complex. The sparse STRING support and partial hu.MAP overlaps also indicate that most co-abundance relationships are not established physical interactions.

**STRING interactions (score >= 0.7)**: 2 of 861 gene pairs: CPSF6–CSTF2 (0.992); CPSF6–PSPC1 (0.748)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11232.1 (NUP160, INTS3, TBRG4; 3/78); huMAP3_09825.1 (KPNA2, NUP160; 2/27); huMAP3_14982.1 (RBM12, TLN1; 2/28); huMAP3_10202.1 (NUP160, INTS3; 2/52); huMAP3_12581.1 (KPNA2, NUP160; 2/58); huMAP3_13468.1 (GLS, MTHFD1L; 2/99)

### Novelty

The module should not be called a newly discovered molecular complex or a newly established pathway. Its component functions are individually well known, and the STRING and hu.MAP results recover recognizable parts of RNA-processing, nuclear-transport, and mitochondrial systems. However, the particular cross-tissue co-abundance organization is not directly explained by the known interaction resources: most module edges lack high-confidence STRING support, and no single hu.MAP complex accounts for the module. Thus the potentially novel observation is the coordinated abundance pattern across autonomic nervous system and cervix uterine, not the discovery of new gene functions or physical interactions. Because there is no globally significant GO or KEGG term and because broad cellular programs can arise from shared cell composition or technical factors, novelty remains provisional and requires replication, cell-composition adjustment, and independent tissue cohorts.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular stress-adaptation and biosynthetic-maintenance state in which RNA maturation and export, nuclear transport, endoplasmic-reticulum protein handling, mitochondrial and amino-acid metabolism, vesicle trafficking, and redox buffering are coordinated. RBM12, CPSF6, and CSTF2 may organize the RNA-processing side; NUP160 and KPNA2 may regulate exchange across the nuclear envelope; SEC63 may support protein entry into the endoplasmic reticulum; and GLS, OAT, AMPD2, GSR, and MTHFD1L may supply metabolic and redox capacity. In autonomic nervous system this could be compatible with neuronal or glial biosynthetic and vesicle demands, while in cervix uterine it could reflect epithelial, stromal, vascular, or reproductive-cell maintenance. This is a mechanistic model, not a demonstrated causal pathway.

### Important genes

#### RBM12

- **Related proteins** (co-abundance neighbors): PUM1 (0.92), ASCC3 (0.91), AMPD2 (0.86), NLN (0.86), CSTF2 (0.84), RAB3GAP2 (0.83), RNF40 (0.83), PDXDC1 (0.82), HNRNPLL (0.82), SEC63 (0.82), DHX36 (0.81), NAA15 (0.81), ABCB6 (0.80), ATP6V1A (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Not detected; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_14982.1
- **Function (MyGene.info)**: RNA binding motif protein 12. This gene encodes a protein that contains several RNA-binding motifs, potential transmembrane domains, and proline-rich regions. This gene and the gene for copine I overlap at map location 20q11.21. Alternative splicing in the 5' UTR results in four transcript variants. All variants encode the same protein. [provided by RefSeq, Nov 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.518); schizophrenia (0.462); schizophrenia 19 (0.437); lysosomal storage disease (0.221); Neurodevelopmental delay (0.119)
- **Europe PMC papers**: 272
- **Why important**: RBM12 is the most connected module gene and links multiple RNA-associated and metabolic neighbors, including PUM1, ASCC3, CSTF2, and NAA15. Its annotation supports regulation of RNA splicing and cAMP or PKA signaling, while its broad tissue profile and substantial literature support make it a plausible organizing hub rather than a tissue-specific marker. Its disease associations include neurodegenerative and neurodevelopmental conditions.
- **Conclusion**: Established evidence supports RBM12 as a broadly expressed RNA-associated protein with a central position in this co-abundance network. It is reasonable to hypothesize that RBM12 helps coordinate RNA processing in the module, but the co-abundance data do not demonstrate that it drives the other genes or explains the tissue sharing.

#### NUP160

- **Related proteins** (co-abundance neighbors): RNF40 (0.96), RAB3GAP2 (0.91), AMPD2 (0.85), MTHFD1L (0.84), INTS3 (0.84), OAT (0.83), ERC1 (0.82), SEC63 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_11232.1, huMAP3_09825.1, huMAP3_10202.1, huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 160. NUP160 is 1 of up to 60 proteins that make up the 120-MD nuclear pore complex, which mediates nucleoplasmic transport.[supplied by OMIM, Apr 2004]
- **Diseases (Open Targets)**: Orthomyxoviridae infectious disease (0.541); HIV infectious disease (0.541); viral infectious disease (0.527); neurodegenerative disease (0.469); Alzheimer disease (0.429)
- **Europe PMC papers**: 812
- **Why important**: NUP160 is a highly connected module member and the principal bridge to several hu.MAP overlaps, including (hu.MAP huMAP3_11232.1), (hu.MAP huMAP3_09825.1), (hu.MAP huMAP3_10202.1), and (hu.MAP huMAP3_12581.1). Its established function in the nuclear pore complex and nucleocytoplasmic transport provides a plausible structural link between the RNA-processing genes and the rest of the module. HPA cell-type enhancement in neuronal and glial populations is compatible with relevance to the autonomic nervous system, although its tissue specificity is low.
- **Conclusion**: Established evidence supports NUP160 as a nuclear-pore component and as the module's clearest connection to known transport complexes. Its role as a cross-tissue coordinator of RNA export or nuclear transport is a plausible hypothesis, not a demonstrated property of this module.

#### GLS

- **Related proteins** (co-abundance neighbors): ATP6V1A (0.93), SEC63 (0.91), OAT (0.89), AMPD2 (0.83), IGF2R (0.82), RAB3GAP2 (0.81), RNF40 (0.81), GSR (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: glutaminase. This gene encodes the K-type mitochondrial glutaminase. The encoded protein is an phosphate-activated amidohydrolase that catalyzes the hydrolysis of glutamine to glutamate and ammonia. This protein is primarily expressed in the brain and kidney plays an essential role in generating energy for metabolism, synthesizing the brain neurotransmitter glutamate and maintaining acid-base balance in the ki…
- **Diseases (Open Targets)**: global developmental delay, progressive ataxia, and elevated glutamine (0.662); genetic developmental and epileptic encephalopathy (0.626); infantile cataract, skin abnormalities, glutamate excess, and impaired intellectual development (0.591); neurodegenerative disease (0.372); glutaminase deficiency (0.371)
- **Europe PMC papers**: 15605
- **Why important**: GLS is a connected metabolic hub linking SEC63, ATP6V1A, OAT, AMPD2, IGF2R, and GSR. It converts glutamine to glutamate and is associated with brain and kidney metabolism, neurotransmitter production, and acid-base balance. Its overlap with MTHFD1L in (hu.MAP huMAP3_13468.1) supports a mitochondrial metabolic component, while its disease associations include developmental and neurological disorders.
- **Conclusion**: Established evidence supports GLS as a mitochondrial glutamine-metabolism enzyme with particular relevance to neural and renal physiology. Its coordination with RNA, transport, and protein-handling genes in this module is an inferred systems-level relationship; the data do not establish that glutamine metabolism is the primary function of the shared module.

#### IGF2R

- **Related proteins** (co-abundance neighbors): NAA15 (0.92), PDXDC1 (0.91), RNF40 (0.87), AMPD2 (0.85), SEC63 (0.83), GLS (0.82), RBBP7 (0.82), ASCC3 (0.81), CSTF2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Golgi apparatus; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2 receptor. This gene encodes a receptor for both insulin-like growth factor 2 and mannose 6-phosphate. The binding sites for each ligand are located on different segments of the protein. This receptor has various functions, including in the intracellular trafficking of lysosomal enzymes, the activation of transforming growth factor beta, and the degradation of insulin-like growth factor 2. Mutation or loss o…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.498); coronary artery disorder (0.477); Hypercholesterolemia (0.369); myocardial ischemia (0.359); coronary atherosclerosis (0.349)
- **Europe PMC papers**: 12245
- **Why important**: IGF2R is among the more connected genes and links several central module members, including NAA15, PDXDC1, RNF40, AMPD2, SEC63, and GLS. It participates in lysosomal-enzyme trafficking, insulin-like growth factor handling, and transforming-growth-factor-beta activation. HPA places it in a neutrophil-enriched context while also showing cervix uterine protein detection, making it relevant to the possibility of cell-composition contributions.
- **Conclusion**: Established evidence supports IGF2R as a trafficking and signaling receptor with lysosomal functions and disease associations including liver and cardiovascular disorders. Its network position suggests a possible interface between trafficking, metabolism, and protein quality control, but it should not be interpreted as evidence that neutrophils or IGF signaling define the entire module.

#### CPSF6

- **Related proteins** (co-abundance neighbors): RFC3 (0.81), NAA15 (0.80); STRING partners: CSTF2 (0.992), PSPC1 (0.748)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 6. The protein encoded by this gene is one subunit of a cleavage factor required for 3' RNA cleavage and polyadenylation processing. The interaction of the protein with the RNA is one of the earliest steps in the assembly of the 3' end processing complex and facilitates the recruitment of other processing factors. The cleavage factor complex is composed of four polypeptides. This gene encodes the 68k…
- **Diseases (Open Targets)**: cancer (0.579); neurodegenerative disease (0.463); Abnormality of the skeletal system (0.451); smoking initiation (0.424); leukemia (0.376)
- **Europe PMC papers**: 1665
- **Why important**: CPSF6 connects the module's RNA-processing genes to RFC3 and NAA15 and has direct high-confidence STRING relationships with CSTF2 and PSPC1. Its established role in mRNA cleavage, polyadenylation, nuclear export, and alternative polyadenylation gives the module a concrete post-transcriptional mechanism. Its nucleoplasmic and nuclear-speckle localization is consistent with the RNA-processing interpretation.
- **Conclusion**: Established evidence supports CPSF6 as a core mRNA three-prime-end processing factor and identifies a known interaction neighborhood within the module. It is a strong marker of the RNA-processing subnetwork, but the evidence does not show that altered alternative polyadenylation causes the cross-tissue co-abundance pattern.

## Module 5

**Tissue pair**: autonomic_nervous_system and cervix_uterine  
**Genes (5)**: ABCF3, APOB, GARS1, TP53RK, SRPK1

### Function

The module does not support a single confidently enriched biological process: no GO or KEGG term passed global correction, and there was no STRING functional enrichment. Its gene content instead suggests a mixed intracellular gene-expression module. GARS1 represents aminoacyl-tRNA charging and translational fidelity; TP53RK represents protein phosphorylation, p53-related signaling, translational fidelity, and the EKC/KEOPS complex; SRPK1 represents phosphorylation-dependent control of RNA splicing; APOB represents lipid transport and lipoprotein biology; and ABCF3 is an ABC-family protein with reported antiviral activity. The most defensible interpretation is therefore coordinated abundance of broadly expressed intracellular regulatory and translation-related proteins, with APOB contributing a lipid-transport or tissue-composition signal. These annotations are gene-level evidence, not evidence that the module as a whole is functionally enriched.

**Cell composition.** The module is not dominated by plasma or secreted proteins, although the HPA summary reports two secreted genes and APOB is explicitly annotated as secreted to blood. Four genes have low tissue specificity, while APOB is enriched in intestine and liver and in enterocytes and hepatocytes. Several genes show enhanced expression in reproductive or trophoblast-related cell types, and SRPK1 is enhanced in basophils, but most genes have low immune-cell specificity or are not detected in immune cells. Thus the module looks mainly like a broadly expressed intracellular program with a possible contribution from tissue or cell-type composition, rather than a clear blood-cell module. The absence of a matching autonomic-nervous-system HPA tissue prevents strong tissue-level protein-expression interpretation there; in cervix, most module proteins are detected.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No high-confidence STRING relationship was detected among the module genes, no STRING functional enrichment was reported, and no hu.MAP complex contained multiple module members. The co-abundance edges therefore are not explained by a previously catalogued dense physical interaction network or a shared hu.MAP complex. The known biology remains informative at the gene level: TP53RK is a component of the EKC/KEOPS complex, SRPK1 is a splicing-factor kinase, GARS1 is a glycyl-tRNA synthetase, and APOB is a major lipoprotein component, but the fact sheet does not establish direct physical links among these proteins. The network should consequently be treated as a statistical co-abundance relationship rather than a demonstrated molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This appears novel as a cross-tissue co-abundance module in the supplied analysis, because its members have no reported high-confidence STRING links or shared hu.MAP complex and no functional enrichment survived global correction. However, absence from those resources does not prove biological novelty: the module may reflect shared regulation, cell composition, protein abundance effects, indirect biology, or technical covariance. Its novelty is therefore strongest at the level of the specific autonomic-nervous-system and cervix-uterine co-abundance pattern, not as a claim that the individual genes or their functions are previously unknown.

**Hypothesis.** Hypothesis: the module may combine a broadly expressed intracellular maintenance and RNA/protein-processing program with an APOB-linked lipid or sample-composition signal. One possible mechanism is that variation in cellular state or tissue admixture coordinately affects translation and translational fidelity through GARS1 and TP53RK, RNA-splicing regulation through SRPK1, and lipid-particle abundance through APOB, with ABCF3 marking an additional cytosolic stress or antiviral-related component. This is a hypothesis only. It requires validation by replication, adjustment for cell composition and circulating lipoproteins, and targeted protein or transcript measurements in both tissues.

### Important genes

#### SRPK1

- **Related proteins** (co-abundance neighbors): APOB (0.86), TP53RK (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SRSF protein kinase 1. This gene encodes a serine/arginine protein kinase specific for the SR (serine/arginine-rich domain) family of splicing factors. The protein localizes to the nucleus and the cytoplasm. It is thought to play a role in regulation of both constitutive and alternative splicing by regulating intracellular localization of splicing factors. Alternative splicing of this gene results in multiple transcript…
- **Diseases (Open Targets)**: neurodegenerative disease (0.460); COVID-19 (0.372); celiac disease (0.190); ulcerative colitis (0.132); type 1 diabetes mellitus (0.123)
- **Europe PMC papers**: 1777
- **Why important**: SRPK1 is central within the module's topology, linking APOB and TP53RK. Its established function as an SR-protein kinase connects the module to RNA splicing, spliceosomal assembly, and signal-regulatory phosphorylation. It has the largest literature volume among the intracellular regulatory candidates in the fact sheet and has reported disease associations spanning neurodegenerative and inflammatory disorders. Its cell-type annotations include reproductive, urothelial, neutrophil-related, and basophil-associated signals, so it may also be sensitive to tissue composition.
- **Conclusion**: Established: SRPK1 is a plausible regulatory hub linking splicing biology to the other module members and is broadly relevant to disease biology. Hypothesis: its co-abundance with APOB and TP53RK may mark a shared state involving RNA-processing regulation and tissue or cellular composition, but the module data do not establish a direct SRPK1 mechanism.

#### GARS1

- **Related proteins** (co-abundance neighbors): TP53RK (0.88), ABCF3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycyl-tRNA synthetase 1. This gene encodes glycyl-tRNA synthetase, one of the aminoacyl-tRNA synthetases that charge tRNAs with their cognate amino acids. The encoded enzyme is an (alpha)2 dimer which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Two transcript variants encoding different isoforms ha…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease type 2D (0.790); neuronopathy, distal hereditary motor, type 5A (0.729); neuronopathy, distal hereditary motor, type 5 (0.698); spinal muscular atrophy, infantile, James type (0.649); Charcot-Marie-Tooth disease type 2 (0.565)
- **Europe PMC papers**: 302
- **Why important**: GARS1 is one of the two highest-connectivity nodes and links TP53RK with ABCF3. It encodes glycyl-tRNA synthetase, an enzyme required for glycyl-tRNA aminoacylation and protein translation, with additional mitochondrial translation-related annotation. It has substantial literature and strong disease associations with inherited peripheral neuropathy and motor neuron disorders, making it especially relevant to an autonomic-nervous-system context.
- **Conclusion**: Established: GARS1 provides a credible translation and proteostasis-related anchor and has clinically established neurological relevance. Hypothesis: its co-abundance may indicate altered translational demand or fidelity in the shared module, but no enrichment result or physical interaction evidence demonstrates that mechanism here.

#### TP53RK

- **Related proteins** (co-abundance neighbors): GARS1 (0.88), SRPK1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TP53 regulating kinase. Enables p53 binding activity and protein serine/threonine kinase activity. Involved in protein phosphorylation. Located in cytoplasm and nucleus. Part of EKC/KEOPS complex. Implicated in Galloway-Mowat syndrome 4. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Galloway-Mowat syndrome (0.762); neurodegenerative disease (0.429); Global developmental delay (0.324); Seizure (0.323); microcephaly (0.112)
- **Europe PMC papers**: 361
- **Why important**: TP53RK is a high-connectivity bridge between GARS1 and SRPK1. It has annotations for protein phosphorylation, p53-class signaling, translational fidelity, and membership in the EKC/KEOPS complex. Its association with Galloway-Mowat syndrome and other developmental or neurological phenotypes gives it biological importance beyond its modest literature volume.
- **Conclusion**: Established: TP53RK is a plausible connector between phosphorylation, translational fidelity, and RNA or cellular regulatory processes, and its disease association supports functional importance. Hypothesis: TP53RK could coordinate the intracellular portion of the module, but the available network evidence does not show a physical bridge to SRPK1 or GARS1.

#### APOB

- **Related proteins** (co-abundance neighbors): SRPK1 (0.86); STRING partners: none
- **HPA**: Group enriched; Group enriched; blood Not detected in immune cells; location Vesicles, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein B. This gene product is the main apolipoprotein of chylomicrons and low density lipoproteins (LDL), and is the ligand for the LDL receptor. It occurs in plasma as two main isoforms, apoB-48 and apoB-100: the former is synthesized exclusively in the gut and the latter in the liver. The intestinal and the hepatic forms of apoB are encoded by a single gene from a single, very long mRNA. The two isoforms…
- **Diseases (Open Targets)**: hypercholesterolemia, autosomal dominant, type B (0.814); Hypercholesterolemia (0.812); familial hypobetalipoproteinemia 1 (0.803); familial hypercholesterolemia (0.780); metabolic disease (0.729)
- **Europe PMC papers**: 28452
- **Why important**: APOB is the module's distinctive tissue-enriched and secreted component. It is enriched in intestine and liver and in enterocytes and hepatocytes, is secreted to blood, and is central to chylomicron and LDL biology, lipid transport, and cholesterol metabolism. It has by far the largest literature volume and strong associations with hypercholesterolemia and related metabolic disease. Its peripheral network position, connected only to SRPK1, argues against treating it as a core intracellular complex member.
- **Conclusion**: Established: APOB is a major lipid-transport protein and a likely contributor to tissue or circulating-protein composition. Hypothesis: its association with the intracellular genes may reflect shared sample composition, lipid-related state, or indirect regulation rather than a direct APOB-SRPK1 pathway.

## Module 6

**Tissue pair**: autonomic_nervous_system and cervix_uterine  
**Genes (47)**: ACIN1, ANP32E, NUDT2, ASNS, ATR, CDK7, CISD1, CSK, EIF2AK2, EGFR, GSK3B, MASTL, HMGN1, ILK, IMPDH1, IMPDH2, CAMK2G, KDM3B, PRKCI, RPS6KA3, ME2, NSF, OLA1, REXO2, PIP4K2C, PIK3CA, PKN1, PRP4K, PSMC6, PSMC2, PSMD9, GART, PUS1, RFC2, RFC5, SLC12A2, SAP30BP, SAMHD1, SEPTIN8, SLK, SRPK2, SUCLA2, AARS1, KARS1, CCT3, TOM1, TTLL12

### Function

The strongest interpretation is a broadly conserved intracellular nucleotide-utilization and phosphorylation module, rather than a narrowly tissue-specific pathway. Globally corrected evidence supports nucleotide and ATP binding, protein kinase and serine/threonine kinase activity, phosphate-containing compound metabolism, and protein phosphorylation (21 globally significant GO/KEGG terms, q_global 9.15e-08–0.000127; see the table), (GO:BP phosphorylation; q_global = 0.000385) (GO:MF ion binding; q_global = 0.000638), (GO:MF small molecule binding; q_global = 0.00184), (GO:MF catalytic activity; q_global = 0.00281), (GO:MF transferase activity; q_global = 0.0128). The module also contains a globally supported neurotrophin-signaling subset involving CAMK2G, GSK3B, PIK3CA, and RPS6KA3 (KEGG Neurotrophin signaling pathway - Homo sapiens (human); q_global = 0.00667). The annotations suggest coordinated control of signal transduction, energy and nucleotide availability, cell-cycle or DNA-damage responses, chromatin regulation, and cytoskeletal or adhesion processes. The large overlap of nucleotide-binding annotations should not be interpreted as evidence for one specific biochemical pathway: it partly reflects the many ATP- or nucleotide-dependent proteins in the module. The convergent kinase evidence is more functionally informative, while the neurotrophin term provides a tissue-relevant signaling link. Overall, this appears to be a conserved cellular state module integrating kinase signaling with genome maintenance, RNA or protein processing, proteostasis, and metabolism.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only a small minority are secreted, and most proteins are intracellular. HPA indicates generally low tissue specificity for many genes, with a smaller group showing tissue enhancement and one brain-enriched gene, SEPTIN8. Cell-type enhancement is common, especially for neutrophils and epithelial or reproductive cell types, but blood-cell specificity is generally low and only a limited subset shows immune-cell enhancement. Therefore, the shared module is unlikely to be explained simply by a plasma-protein or blood-cell signature. It more plausibly reflects a broadly expressed intracellular program that can occur in several cell types, although sample cellular composition could still contribute because some module genes are enhanced in neutrophils, monocytes, trophoblasts, or epithelial populations. Cervical protein detection is widespread among the tested genes, whereas the autonomic-nervous-system tissue lacks a matching HPA tissue category; this limits direct protein-level comparison between the two tissues. The brain enhancement of SEPTIN8 and the neuronal functions of CAMK2G, RPS6KA3, and NSF are compatible with relevance to autonomic tissue, but they do not establish neuronal origin.

**GO/KEGG enrichment**: 54 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF nucleotide binding | 9.15e-08 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, IMPDH1, IMPDH2, KARS1, MASTL, ME2, NSF, NUDT2, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SAMHD1, SEPTIN8, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF heterocyclic compound binding | 1.19e-07 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CISD1, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, IMPDH1, IMPDH2, KARS1, MASTL, ME2, NSF, NUDT2, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SAMHD1, SEPTIN8, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF protein kinase activity | 1.19e-07 | ATR, CAMK2G, CDK7, CSK, EGFR, EIF2AK2, GSK3B, ILK, MASTL, PIK3CA, PKN1, PRKCI, PRP4K, RPS6KA3, SLK, SRPK2 |
| GO:MF purine ribonucleoside triphosphate binding | 1.43e-07 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, KARS1, MASTL, NSF, NUDT2, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SAMHD1, SEPTIN8, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF nucleoside phosphate binding | 1.48e-07 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, IMPDH1, IMPDH2, KARS1, MASTL, ME2, NSF, NUDT2, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SAMHD1, SEPTIN8, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF purine ribonucleotide binding | 1.57e-07 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, KARS1, MASTL, NSF, NUDT2, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SAMHD1, SEPTIN8, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF ribonucleotide binding | 2.08e-07 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, KARS1, MASTL, NSF, NUDT2, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SAMHD1, SEPTIN8, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF purine nucleotide binding | 2.67e-07 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, KARS1, MASTL, ME2, NSF, NUDT2, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SAMHD1, SEPTIN8, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF ATP binding | 3.79e-07 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, KARS1, MASTL, NSF, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF adenyl ribonucleotide binding | 4.15e-07 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, KARS1, MASTL, NSF, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF phosphotransferase activity, alcohol group as acceptor | 4.39e-07 | ATR, CAMK2G, CDK7, CSK, EGFR, EIF2AK2, GSK3B, ILK, MASTL, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, RPS6KA3, SLK, SRPK2 |
| GO:MF adenyl nucleotide binding | 8.26e-07 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, KARS1, MASTL, ME2, NSF, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF carbohydrate derivative binding | 9.52e-07 | AARS1, ASNS, ATR, CAMK2G, CCT3, CDK7, CSK, EGFR, EIF2AK2, GART, GSK3B, ILK, KARS1, MASTL, NSF, NUDT2, OLA1, PIK3CA, PIP4K2C, PKN1, PRKCI, PRP4K, PSMC2, PSMC6, RFC2, RFC5, RPS6KA3, SAMHD1, SEPTIN8, SLK, SRPK2, SUCLA2, TTLL12 |
| GO:MF protein serine kinase activity | 1.25e-06 | ATR, CAMK2G, CDK7, EIF2AK2, GSK3B, MASTL, PIK3CA, PKN1, PRKCI, PRP4K, RPS6KA3, SLK, SRPK2 |
| GO:MF protein serine/threonine kinase activity | 1.28e-06 | ATR, CAMK2G, CDK7, EGFR, EIF2AK2, GSK3B, MASTL, PIK3CA, PKN1, PRKCI, PRP4K, RPS6KA3, SLK, SRPK2 |

### STRING and hu.MAP

STRING supports a set of coherent known relationships rather than a uniformly connected network. Established edges include the AARS1-KARS1 aminoacyl-tRNA synthetase relationship; EGFR-CSK, EGFR-PIK3CA, PIK3CA-ILK, PIK3CA-PIP4K2C, and PIK3CA-PRKCI signaling relationships; GSK3B-ILK; the IMPDH1-IMPDH2 and GART-IMPDH relationships in nucleotide metabolism; ATR-RFC2/RFC5 and RFC2-RFC5 in replication or checkpoint biology; and PSMC2-PSMC6-PSMD9 in the proteasome. These known links support real molecular substructures within the co-abundance module, especially signaling, nucleotide synthesis, DNA replication or damage response, and proteostasis. hu.MAP independently supports spliceosome or RNA-processing assemblies containing SRPK2, PRP4K, and ACIN1 (hu.MAP huMAP3_09621.1), proteasome assemblies containing PSMC2, PSMC6, and PSMD9 (hu.MAP huMAP3_13725.1), IMPDH-containing assemblies (hu.MAP huMAP3_07594.1), RFC-containing replication complexes (hu.MAP huMAP3_09476.1) (hu.MAP huMAP3_03241.1) (hu.MAP huMAP3_07313.1) (hu.MAP huMAP3_02854.1) (hu.MAP huMAP3_08854.1) (hu.MAP huMAP3_14232.1) (hu.MAP huMAP3_08879.1) (hu.MAP huMAP3_12839.1), and smaller complexes involving SAMHD1, SUCLA2, AARS1, OLA1, ME2, and related proteins (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_07082.1), (hu.MAP huMAP3_15342.1), (hu.MAP huMAP3_12629.1), (hu.MAP huMAP3_10665.1). Thus, the module combines several known complexes and interaction neighborhoods. At the same time, many co-abundance edges have no corresponding high-confidence STRING or hu.MAP relationship, so co-abundance should not be equated with direct physical interaction. The STRING enrichment for ATP, nucleotide binding, and kinase functions (15 supplementary STRING terms; within-query FDR 1.19e-08–5.78e-07) is supportive but remains supplementary and is not global enrichment evidence.

**STRING interactions (score >= 0.7)**: 18 of 1081 gene pairs: AARS1–ASNS (0.84); AARS1–KARS1 (0.992); ACIN1–SRPK2 (0.83); ATR–RFC2 (0.85); ATR–RFC5 (0.775); CSK–EGFR (0.929); EGFR–PIK3CA (0.999); GART–IMPDH1 (0.773); GART–IMPDH2 (0.811); GSK3B–ILK (0.895); ILK–PIK3CA (0.923); IMPDH1–IMPDH2 (0.984); PIK3CA–PIP4K2C (0.923); PIK3CA–PRKCI (0.952); PSMC2–PSMC6 (0.999); PSMC2–PSMD9 (0.97); PSMC6–PSMD9 (0.999); RFC2–RFC5 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword ATP-binding (FDR = 1.19e-08, 30 genes); Keyword Nucleotide-binding (FDR = 1.19e-08, 33 genes); Function Nucleotide binding (FDR = 2.82e-08, 36 genes); Function ATP binding (FDR = 2.82e-08, 30 genes); Function Purine ribonucleotide binding (FDR = 2.82e-08, 33 genes); Function Purine ribonucleoside triphosphate binding (FDR = 2.82e-08, 33 genes); Function Protein kinase activity (FDR = 3.3e-08, 16 genes); Function Protein serine/threonine kinase activity (FDR = 4.62e-08, 15 genes); InterPro Protein kinase-like domain superfamily (FDR = 5.19e-08, 16 genes); Function Phosphotransferase activity, alcohol group as acceptor (FDR = 5.35e-08, 17 genes); Keyword Kinase (FDR = 7.65e-08, 17 genes); Keyword Serine/threonine-protein kinase (FDR = 7.65e-08, 14 genes); Function Protein serine kinase activity (FDR = 1.9e-07, 13 genes); InterPro Protein kinase domain (FDR = 3.27e-07, 14 genes); Function Kinase activity (FDR = 5.78e-07, 17 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09621.1 (SRPK2, PRP4K, ACIN1; 3/56); huMAP3_14442.1 (ME2, AARS1, OLA1; 3/57); huMAP3_13725.1 (PSMD9, PSMC2, PSMC6; 3/69); huMAP3_07594.1 (IMPDH2, IMPDH1; 2/3); huMAP3_07082.1 (SUCLA2, SAMHD1; 2/4); huMAP3_09476.1 (RFC2, RFC5; 2/5); huMAP3_03241.1 (RFC2, RFC5; 2/9); huMAP3_07313.1 (RFC2, RFC5; 2/9); huMAP3_02854.1 (RFC2, RFC5; 2/10); huMAP3_08854.1 (RFC2, RFC5; 2/10); huMAP3_14232.1 (RFC2, RFC5; 2/10); huMAP3_08879.1 (RFC2, RFC5; 2/11); huMAP3_12839.1 (RFC2, RFC5; 2/11); huMAP3_07248.1 (PRP4K, ACIN1; 2/12); huMAP3_08365.1 (PRP4K, ACIN1; 2/12); huMAP3_00703.1 (RFC2, RFC5; 2/12); huMAP3_10568.1 (RFC2, RFC5; 2/13); huMAP3_15342.1 (IMPDH2, IMPDH1; 2/15); huMAP3_09637.1 (PRP4K, ACIN1; 2/21); huMAP3_08467.1 (SRPK2, PRP4K; 2/22); huMAP3_12629.1 (IMPDH2, IMPDH1; 2/23); huMAP3_05064.1 (PSMC2, PSMC6; 2/31); huMAP3_12727.1 (RFC2, RFC5; 2/32); huMAP3_10665.1 (SUCLA2, SAMHD1; 2/42); huMAP3_09656.1 (PSMC2, PSMC6; 2/64); huMAP3_11073.1 (PRP4K, ACIN1; 2/67); huMAP3_09943.1 (PRP4K, ACIN1; 2/78); huMAP3_05807.1 (SRPK2, PRP4K; 2/81)

### Novelty

The module is unlikely to represent a previously established single molecular complex or a canonical pathway, because it combines several recognizable subnetworks: receptor and phosphoinositide signaling, DNA replication or checkpoint machinery, purine metabolism, proteasome components, spliceosome-associated kinases, mitochondrial metabolism, and translation-related enzymes. The known STRING and hu.MAP relationships show that important parts are established biology, but they do not by themselves explain the cross-tissue co-abundance architecture. The potentially novel finding is therefore the reproducible conservation of this composite intracellular program across autonomic nervous system and cervix uterine samples, not the discovery of each individual interaction. Missing STRING or hu.MAP edges cannot prove novelty, since database coverage, context dependence, transient interactions, and co-regulation all limit those resources. A stronger novelty claim would require independent replication, comparison with published tissue co-abundance modules, and testing whether the module persists after adjustment for cell type, proliferation, tissue composition, and technical covariates.

**Hypothesis.** Hypothesis: the module represents a conserved stress-responsive growth and maintenance program in which EGFR-PIK3CA and related phosphoinositide signaling converge with CAMK2G, GSK3B, and RPS6KA3 to regulate cell state, adhesion, cytoskeletal organization, and transcription. This signaling activity may be coupled to ATR-RFC checkpoint machinery, EIF2AK2-mediated translational control, purine and amino-acid metabolism, proteasomal turnover, and mitochondrial support so that cells can maintain genome integrity and protein homeostasis during tissue-specific stimulation or stress. SRPK2-PRP4K-ACIN1 could provide an RNA-splicing arm, while NUDT2 and the aminoacyl-tRNA synthetases could reflect nucleotide and translation capacity. This is a mechanistic model, not a demonstrated causal pathway; the co-abundance data do not establish directionality, direct binding, or activation state.

### Important genes

#### EGFR

- **Related proteins** (co-abundance neighbors): ATR (0.87), IMPDH1 (0.84), OLA1 (0.84), SRPK2 (0.81), IMPDH2 (0.80); STRING partners: CSK (0.929), PIK3CA (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is a prominent signaling hub in the module and is connected in STRING to CSK and PIK3CA. It is a cell-surface receptor tyrosine kinase with established roles in receptor-driven phosphorylation and signal transduction, and it is detected in cervix uterine tissue. Its disease literature is extensive, especially in cancer, making it a strong anchor for interpreting the signaling component of the module.
- **Conclusion**: Established evidence supports EGFR as a receptor-level entry point into the module and as a plausible regulator of the PIK3CA-linked signaling neighborhood (GO:MF protein kinase activity; q_global = 1.19e-07), (7 globally significant GO/KEGG terms, q_global 1.28e-06–0.000127; see the table), (KEGG Neurotrophin signaling pathway - Homo sapiens (human); q_global = 0.00667). It is a hypothesis that EGFR activity drives the entire conserved module; co-abundance alone does not show receptor activation or causality.

#### PIK3CA

- **Related proteins** (co-abundance neighbors): ILK (0.82); STRING partners: EGFR (0.999), ILK (0.923), PIP4K2C (0.923), PRKCI (0.952)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Primary cilium, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha. Phosphatidylinositol 3-kinase is composed of an 85 kDa regulatory subunit and a 110 kDa catalytic subunit. The protein encoded by this gene represents the catalytic subunit, which uses ATP to phosphorylate PtdIns, PtdIns4P and PtdIns(4,5)P2. This gene has been found to be oncogenic and has been implicated in cervical cancers. A pseudogene of this gene has been defined on chromosome 22. [provided b…
- **Diseases (Open Targets)**: megalencephaly-capillary malformation-polymicrogyria syndrome (0.849); CLOVES syndrome (0.795); PIK3CA-related overgrowth spectrum (0.770); breast cancer (0.754); Cowden syndrome 5 (0.754)
- **Europe PMC papers**: 45816
- **Why important**: PIK3CA links EGFR to ILK, PIP4K2C, and PRKCI in STRING and is part of the globally supported neurotrophin-signaling subset (KEGG Neurotrophin signaling pathway - Homo sapiens (human); q_global = 0.00667). It encodes the catalytic phosphoinositide kinase subunit and is annotated for EGFR and insulin-receptor signaling, lamellipodium assembly, and vasculature development. Its established involvement in cervical cancer and extensive disease literature makes it especially relevant to a module shared with cervix uterine tissue.
- **Conclusion**: Established evidence identifies PIK3CA as a central phosphoinositide-signaling component with a biologically credible connection to EGFR and cytoskeletal or adhesion regulation. A module-specific role in coordinating autonomic and cervical tissue states remains a hypothesis requiring perturbation or longitudinal evidence.

#### CAMK2G

- **Related proteins** (co-abundance neighbors): PIP4K2C (0.92), IMPDH2 (0.91), CSK (0.85), ASNS (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Primary cilium tip, Primary cilium transition zone, Principal piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent protein kinase II gamma. The product of this gene is one of the four subunits of an enzyme which belongs to the serine/threonine protein kinase family, and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. Calcium signaling is crucial for several aspects of plasticity at glutamatergic synapses. In mammalian cells the enzyme is composed of four different chains: alpha, beta, gamma, and delta. The product of this…
- **Diseases (Open Targets)**: intellectual developmental disorder 59 (0.643); psoriasis (0.454); Severe intellectual disability (0.399); dengue disease (0.370); psoriasis vulgaris (0.345)
- **Europe PMC papers**: 1587
- **Why important**: CAMK2G is a calcium/calmodulin-dependent serine/threonine kinase, has high module connectivity relative to many genes, and participates with GSK3B, PIK3CA, and RPS6KA3 in the globally supported neurotrophin pathway (KEGG Neurotrophin signaling pathway - Homo sapiens (human); q_global = 0.00667). Its annotations include neuronal projection development, synaptic plasticity, calcium transport, and skeletal-muscle adaptation. HPA also reports enhancement in several neural and epithelial cell types, including cytotrophoblasts, although its protein was not detected in the tested cervix sample.
- **Conclusion**: Established evidence supports CAMK2G as a plausible calcium-sensitive signaling bridge linking the module to neuronal or excitable-cell biology and to broader phosphorylation control. Its involvement in the shared tissue module is a hypothesis because the co-abundance result does not establish neuronal composition or kinase activation.

#### ATR

- **Related proteins** (co-abundance neighbors): OLA1 (0.91), GART (0.88), EIF2AK2 (0.87), EGFR (0.87), RPS6KA3 (0.84), IMPDH2 (0.83), ILK (0.82); STRING partners: RFC2 (0.85), RFC5 (0.775)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATR checkpoint kinase. The protein encoded by this gene is a serine/threonine kinase and DNA damage sensor, activating cell cycle checkpoint signaling upon DNA stress. The encoded protein can phosphorylate and activate several proteins involved in the inhibition of DNA replication and mitosis, and can promote DNA repair, recombination, and apoptosis. This protein is also important for fragile site stability and centroso…
- **Diseases (Open Targets)**: Seckel syndrome 1 (0.744); familial cutaneous telangiectasia and oropharyngeal predisposition cancer syndrome (0.669); Seckel syndrome (0.666); microcephalic primordial dwarfism (0.513); hereditary disease (0.474)
- **Europe PMC papers**: 41041
- **Why important**: ATR is one of the most connected genes in the module and connects in STRING to RFC2 and RFC5, providing a direct link to the replication-factor-C complexes represented in hu.MAP (hu.MAP huMAP3_09476.1) (hu.MAP huMAP3_03241.1) (hu.MAP huMAP3_07313.1) (hu.MAP huMAP3_02854.1) (hu.MAP huMAP3_08854.1) (hu.MAP huMAP3_14232.1) (hu.MAP huMAP3_08879.1) (hu.MAP huMAP3_12839.1). It is a DNA-damage-sensing serine/threonine kinase involved in replication, repair, checkpoint signaling, telomere maintenance, and apoptosis. Its disease associations include Seckel syndrome and cancer-predisposition conditions, and its literature is extensive.
- **Conclusion**: Established evidence supports ATR as the genome-maintenance arm of the module, linking kinase activity with DNA replication and damage surveillance (GO:MF protein kinase activity; q_global = 1.19e-07), (GO:BP protein phosphorylation; q_global = 0.000127), (23 globally significant GO/KEGG terms, q_global 0.00112–0.00112; see the table). It is a hypothesis that the shared co-abundance pattern reflects active DNA stress or checkpoint signaling rather than constitutive expression of a general maintenance program.

#### SRPK2

- **Related proteins** (co-abundance neighbors): ACIN1 (0.88), PIP4K2C (0.88), PRP4K (0.87), EGFR (0.81); STRING partners: ACIN1 (0.83)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_09621.1, huMAP3_08467.1, huMAP3_05807.1
- **Function (MyGene.info)**: SRSF protein kinase 2. Enables ATP binding activity; magnesium ion binding activity; and protein serine/threonine kinase activity. Involved in several processes, including nucleic acid metabolic process; peptidyl-serine phosphorylation; and regulation of viral genome replication. Located in chromatin; cytosol; and nuclear lumen. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: COVID-19 (0.404); neurodegenerative disease (0.371); schizophrenia (0.303); skin aging (0.272); smoking cessation (0.268)
- **Europe PMC papers**: 1379
- **Why important**: SRPK2 is a strongly annotated kinase and is connected to ACIN1, PRP4K, PIP4K2C, and EGFR in the module. hu.MAP places SRPK2 with PRP4K and ACIN1 in spliceosome or RNA-processing assemblies (hu.MAP huMAP3_09621.1), (hu.MAP huMAP3_08467.1), (hu.MAP huMAP3_05807.1), while its functional annotations include RNA splicing, spliceosomal assembly, gene-expression regulation, and phosphorylation. This makes it a useful bridge between signaling and post-transcriptional control.
- **Conclusion**: Established evidence supports SRPK2 as a kinase associated with RNA-processing machinery and as a connector between the signaling and splicing portions of the module (GO:MF protein kinase activity; q_global = 1.19e-07), (5 globally significant GO/KEGG terms, q_global 1.25e-06–1.05e-05; see the table), (GO:MF histone modifying activity; q_global = 0.00204). A coordinated signaling-to-splicing mechanism in these two tissues is a hypothesis, not a conclusion from the co-abundance network alone.

#### NUDT2

- **Related proteins** (co-abundance neighbors): TTLL12 (0.91), CCT3 (0.91), SAP30BP (0.90), AARS1 (0.88), KARS1 (0.87), PSMD9 (0.86), ANP32E (0.85), SLK (0.84), SUCLA2 (0.84), CISD1 (0.82), PUS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nudix hydrolase 2. This gene encodes a member of the MutT family of nucleotide pyrophosphatases, a subset of the larger NUDIX hydrolase family. The gene product possesses a modification of the MutT sequence motif found in certain nucleotide pyrophosphatases. The enzyme asymmetrically hydrolyzes Ap4A to yield AMP and ATP and is responsible for maintaining the intracellular level of the dinucleotide Ap4A, the function…
- **Diseases (Open Targets)**: intellectual developmental disorder with or without peripheral neuropathy (0.665); Intellectual disability (0.456); polyneuropathy (0.372); Global developmental delay (0.371); developmental disability (0.370)
- **Europe PMC papers**: 328
- **Why important**: NUDT2 has the strongest network prominence in the supplied ranking and connects nucleotide-handling, translation-related, proteasome-associated, and cytoskeletal neighborhoods. Its known biochemical function is hydrolysis of Ap4A, linking it to intracellular dinucleotide and ATP balance, and it is annotated for nucleotide metabolism, AMP and ATP biosynthesis, apoptosis, and oxidative-stress response. It is broadly expressed and detected in cervix uterine tissue, making it a plausible state marker rather than a tissue-specific marker.
- **Conclusion**: Established evidence supports NUDT2 as a nucleotide-homeostasis and stress-response component that may help explain the module's broad nucleotide-binding enrichment (GO:MF nucleotide binding; q_global = 9.15e-08), (5 globally significant GO/KEGG terms, q_global 1.43e-07–2.67e-07; see the table), (GO:BP phosphorus metabolic process; q_global = 3.99e-05) (GO:BP phosphate-containing compound metabolic process; q_global = 3.99e-05). The hypothesis that NUDT2 coordinates the signaling and metabolic arms of the module is plausible but unproven, particularly because it lacks a reported STRING partner or hu.MAP complex in this module.

## Module 7

**Tissue pair**: autonomic_nervous_system and cervix_uterine  
**Genes (37)**: ACO2, ACTN1, BAIAP2, BOLA2, BRIX1, CGN, CORO7, DHCR24, SORD, DPYSL2, EFL1, ERBIN, ERLIN1, SHMT1, KRT9, KRT2, KRT1, MCM7, NUCB1, P4HA1, PTGR1, RAD50, RRP12, SEC16A, SEC23B, SCP2, PHGDH, SPTAN1, SRP68, SYNE2, SARS1, F2, TNPO3, TRIM56, TXNDC5, VPS4B, XPO4

### Function

The strongest functional interpretation is an epithelial structural and intermediate-filament module. The primary evidence is the globally corrected enrichment for intermediate filament-based process (GO:BP intermediate filament-based process; q_global = 0.0473) and intermediate filament cytoskeleton organization (GO:BP intermediate filament cytoskeleton organization; q_global = 0.0473), driven by ERBIN, KRT1, KRT2, and KRT9. This is consistent with the presence of cingulin, spectrin, alpha-actinin, and other cytoskeletal or junction-associated proteins. Additional genes indicate supporting processes involving ER-to-Golgi trafficking, membrane organization, cholesterol and lipid handling, mitochondrial metabolism, DNA maintenance, translation, and nuclear transport, but these are functional context rather than globally corrected GO/KEGG conclusions. The sparse high-confidence STRING network suggests that the module is not one dense canonical protein complex; instead, it contains a structural epithelial core together with several biochemical and trafficking subsystems.

**Cell composition.** The module is not predominantly composed of secreted or plasma proteins: only NUCB1 and F2 are explicitly identified as secreted to blood, while TXNDC5 is classified as intracellular and membrane-associated and P4HA1 as intracellular and membrane-associated. The HPA profile instead supports a mixed cellular composition. Many genes have low tissue specificity, while others are enriched in skin, liver, skeletal muscle, intestine, bone marrow, brain, adrenal gland, or cervix. Several genes are enhanced in epithelial populations, including suprabasal keratinocytes, esophageal apical cells, enterocytes, and glandular or myoepithelial populations. There is also a recurrent myeloid and granulocyte signal, including neutrophils and related progenitors, as well as some monocyte and dendritic-cell annotations. Thus, the shared module may reflect epithelial or epithelial-like structural biology in both tissues, with possible contribution from shared stromal or immune cell types. The HPA evidence does not justify treating it as a purely autonomic-neural module, nor does it establish that it is simply a blood-contamination signature.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP intermediate filament-based process | 0.0473 | ERBIN, KRT1, KRT2, KRT9 |
| GO:BP intermediate filament cytoskeleton organization | 0.0473 | ERBIN, KRT1, KRT2, KRT9 |

### STRING and hu.MAP

The known STRING relationships are limited but biologically coherent in several local pairs: KRT1-KRT2 supports the keratin filament interpretation; SEC16A-SEC23B supports ER export and COPII vesicle formation; PHGDH-SHMT1 links serine and one-carbon metabolism; and BRIX1-RRP12 links ribosomal biogenesis. The absence of STRING functional enrichment means that no additional STRING-derived pathway conclusion should be treated as established. hu.MAP provides repeated support for an XPO4-TNPO3 nuclear transport association across several complexes (hu.MAP huMAP3_05832.1) through (hu.MAP huMAP3_09114.1) and (hu.MAP huMAP3_10202.1) through (hu.MAP huMAP3_11232.1), although each complex contains many proteins not present in this module, so this is evidence of shared complex membership rather than proof of a complete module complex. ACTN1-SPTAN1 recur together in a cytoskeletal complex (hu.MAP huMAP3_09165.1), and SEC16A-SEC23B recur in a trafficking complex (hu.MAP huMAP3_12394.1). Overall, the databases support several known local relationships embedded within a broader co-abundance pattern, rather than a single established multiprotein machine.

**STRING interactions (score >= 0.7)**: 4 of 666 gene pairs: BRIX1–RRP12 (0.871); KRT1–KRT2 (0.956); PHGDH–SHMT1 (0.881); SEC16A–SEC23B (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05832.1 (XPO4, TNPO3; 2/14); huMAP3_06077.1 (XPO4, TNPO3; 2/15); huMAP3_08298.1 (XPO4, TNPO3; 2/24); huMAP3_09053.1 (XPO4, TNPO3; 2/25); huMAP3_09114.1 (XPO4, TNPO3; 2/30); huMAP3_09165.1 (ACTN1, SPTAN1; 2/39); huMAP3_10202.1 (XPO4, TNPO3; 2/52); huMAP3_10287.1 (XPO4, TNPO3; 2/53); huMAP3_11232.1 (XPO4, TNPO3; 2/78); huMAP3_12394.1 (SEC16A, SEC23B; 2/98)

### Novelty

This module should not be described as a wholly new molecular pathway. Its central biology is already well established through keratin filament functions, epithelial junction organization, cytoskeletal scaffolding, ER export, nuclear transport, and the documented STRING and hu.MAP relationships. The potentially novel aspect is the cross-tissue co-abundance configuration shared by autonomic_nervous_system and cervix_uterine, particularly the linking of an epithelial intermediate-filament signal with trafficking, lipid, metabolic, nuclear-transport, and neural or cytoskeletal genes. That configuration requires validation in independent cohorts, cell-type-resolved data, and preferably protein-level measurements. Absence of a complete matching STRING or hu.MAP complex is not evidence of novelty, because co-abundance can arise from shared cell composition, coordinated regulation, or context-dependent interactions.

**Hypothesis.** Hypothesis: the module reflects a conserved epithelial structural-maintenance program that couples intermediate-filament and junctional organization to membrane trafficking, lipid homeostasis, and cellular stress adaptation. In cervix_uterine, this could represent epithelial differentiation and barrier architecture. In autonomic_nervous_system, it may reflect epithelial-like support cells, vascular or stromal components, or shared cytoskeletal programs rather than neurons themselves. ERBIN, CGN, SPTAN1, and the keratin pair could provide structural organization, while SEC16A and SEC23B support delivery of membrane and junctional cargo. DHCR24, SCP2, and ERLIN1 could connect membrane structure to sterol handling, and the myeloid annotations raise the alternative possibility that part of the signal reflects shared immune-cell composition. This remains a testable hypothesis, not a demonstrated causal mechanism.

### Important genes

#### KRT1

- **Related proteins** (co-abundance neighbors): XPO4 (0.89), SORD (0.89), CGN (0.87), SEC16A (0.81); STRING partners: KRT2 (0.956)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is one of the four genes driving both primary globally corrected intermediate-filament terms (GO:BP intermediate filament-based process; q_global = 0.0473) and (GO:BP intermediate filament cytoskeleton organization; q_global = 0.0473). It is connected in the module to KRT2, CGN, SORD, and XPO4, is enriched in skin and suprabasal keratinocytes, and is detected in cervix_uterine. Its extensive literature and established keratin disease associations make it a strong anchor for epithelial differentiation and structural interpretation.
- **Conclusion**: Established evidence supports KRT1 as a core epithelial intermediate-filament component of the module and as a major contributor to its significant functional annotation. The cross-tissue co-abundance pattern may indicate shared epithelial differentiation or a related structural program, but it does not establish that KRT1 drives the module.

#### KRT2

- **Related proteins** (co-abundance neighbors): CGN (0.83), SORD (0.81); STRING partners: KRT1 (0.956)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location Intermediate filaments, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 2. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is expressed largely in the upper spinous layer of epidermal keratinocytes and mutations in this gene …
- **Diseases (Open Targets)**: superficial epidermolytic ichthyosis (0.815); exfoliative ichthyosis (0.358); Palmoplantar hyperkeratosis (0.267); hereditary disease (0.193); Vertigo (0.145)
- **Europe PMC papers**: 7459
- **Why important**: KRT2 is the known high-confidence STRING partner of KRT1 and independently contributes to both primary terms (GO:BP intermediate filament-based process; q_global = 0.0473) and (GO:BP intermediate filament cytoskeleton organization; q_global = 0.0473). HPA assigns it to skin and suprabasal keratinocytes, and the gene has extensive literature and established associations with epidermolytic and other keratinization disorders. Its module connections to CGN and SORD place it at the interface of structural and metabolic signals.
- **Conclusion**: Established evidence supports KRT2 as part of a keratin filament differentiation program that is central to the module. Whether its co-abundance in both tissues reflects local epithelial cells, shared contaminating cell populations, or a broader barrier program remains unresolved.

#### KRT9

- **Related proteins** (co-abundance neighbors): DPYSL2 (0.91), P4HA1 (0.90), DHCR24 (0.89), NUCB1 (0.83), SEC23B (0.81), SPTAN1 (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 9. This gene encodes the type I keratin 9, an intermediate filament chain expressed only in the terminally differentiated epidermis of palms and soles. Mutations in this gene cause epidermolytic palmoplantar keratoderma. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: epidermolytic palmoplantar keratoderma, 1 (0.828); palmoplantar keratoderma, epidermolytic (0.682); Localized epidermolytic hyperkeratosis (0.511); Palmoplantar hyperkeratosis (0.456); Palmoplantar keratoderma (0.438)
- **Europe PMC papers**: 773
- **Why important**: KRT9 is another direct contributor to both primary terms (GO:BP intermediate filament-based process; q_global = 0.0473) and (GO:BP intermediate filament cytoskeleton organization; q_global = 0.0473). It has a comparatively strong module position, connects to DPYSL2, P4HA1, DHCR24, NUCB1, SEC23B, and SPTAN1, and has established expression in terminally differentiated epidermis and disease associations involving palmoplantar keratoderma. Its HPA profile also shows epithelial and myoepithelial cell-type enhancement.
- **Conclusion**: Established evidence supports KRT9 as a structural marker that strengthens the interpretation of an intermediate-filament and epithelial differentiation module. Its presence does not by itself prove that the autonomic nervous system signal comes from keratinizing epithelium; cell-type composition must be tested directly.

#### SPTAN1

- **Related proteins** (co-abundance neighbors): MCM7 (0.92), SYNE2 (0.89), SEC23B (0.84), SEC16A (0.84), DHCR24 (0.83), SRP68 (0.81), RAD50 (0.81), ERBIN (0.81), NUCB1 (0.81), KRT9 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Microtubules; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_09165.1
- **Function (MyGene.info)**: spectrin alpha, non-erythrocytic 1. Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encod…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 5 (0.749); developmental delay with or without epilepsy (0.681); spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia (0.681); infantile spasms (0.651); genetic developmental and epileptic encephalopathy (0.651)
- **Europe PMC papers**: 1422
- **Why important**: SPTAN1 has the strongest network position in the supplied module and connects structural, trafficking, metabolic, DNA-maintenance, and ER-associated genes. Spectrin biology provides a plausible scaffold linking the plasma membrane, intracellular organelles, and cytoskeleton. It is detected in cervix_uterine and has extensive literature and well-established associations with developmental epileptic encephalopathy and related neurological disorders.
- **Conclusion**: Established evidence supports SPTAN1 as a broad cytoskeletal scaffold and a network-level connector. It may help explain how the module links epithelial intermediate filaments with neural or muscle-associated cytoskeletal programs, but that bridging role is a hypothesis rather than a demonstrated physical mechanism here.

#### CGN

- **Related proteins** (co-abundance neighbors): SCP2 (0.88), KRT1 (0.87), PTGR1 (0.86), VPS4B (0.85), KRT2 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cingulin. Enables cadherin binding activity. Predicted to act upstream of or within bicellular tight junction assembly; epithelial cell morphogenesis; and microtubule cytoskeleton organization. Located in bicellular tight junction and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.359); nonsyndromic deafness (0.118); skin disorder (0.094); colorectal carcinoma (0.086); ovarian carcinoma (0.065)
- **Europe PMC papers**: 3593
- **Why important**: CGN is connected to KRT1, KRT2, SCP2, PTGR1, and VPS4B and is localized to the plasma membrane and cell junctions. Its annotated roles in cadherin binding, tight-junction assembly, epithelial morphogenesis, and microtubule organization directly complement the keratin-centered primary enrichment. It is enhanced in intestinal and epithelial cell types, detected in cervix_uterine, and has substantial literature.
- **Conclusion**: Established evidence supports CGN as a junctional and epithelial-architecture component that may connect intermediate filaments to barrier organization. A role in coordinating the entire shared module is plausible from the network, but causal coordination has not been shown.

#### SEC16A

- **Related proteins** (co-abundance neighbors): P4HA1 (0.89), NUCB1 (0.88), ACO2 (0.85), SPTAN1 (0.84), KRT1 (0.81); STRING partners: SEC23B (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Golgi apparatus; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: SEC16 homolog A, endoplasmic reticulum export factor. This gene encodes a protein that forms part of the Sec16 complex. This protein has a role in protein transport from the endoplasmic reticulum (ER) to the Golgi and mediates COPII vesicle formation at the transitional ER. Alternative splicing results in multiple transcript variants that encode different protein isoforms. [provided by RefSeq, Feb 2013].
- **Diseases (Open Targets)**: squamous cell carcinoma (0.288); Crohn disease (0.277); bladder calculus (0.241); nephrolithiasis (0.235); actinic keratosis (0.215)
- **Europe PMC papers**: 595
- **Why important**: SEC16A occupies a relatively central position among the module genes and connects to P4HA1, NUCB1, ACO2, SPTAN1, and KRT1. It has a very strong known STRING relationship with SEC23B and shares a hu.MAP trafficking complex with SEC23B (hu.MAP huMAP3_12394.1). Its established function in ER-to-Golgi transport and COPII vesicle formation provides a mechanistic route for supplying membrane and junctional proteins to epithelial cells.
- **Conclusion**: Established evidence supports SEC16A as a trafficking component that complements the structural keratin and junctional signal. Its participation suggests coordinated protein export may accompany the structural program, but the co-abundance data do not establish cargo specificity or direction of regulation.

## Module 8

**Tissue pair**: autonomic_nervous_system and cervix_uterine  
**Genes (8)**: ARHGEF2, DNAAF5, FKBP10, SLC2A1, IGF2BP1, PEX19, RNH1, USO1

### Function

The module does not support a single statistically established GO or KEGG function because no term passed global correction. Its gene content instead suggests a composite cellular program involving glucose transport and metabolic stress adaptation through SLC2A1, RNA binding and post-transcriptional regulation through IGF2BP1 and RNH1, protein folding and organelle trafficking through FKBP10, PEX19, and USO1, and possible ciliary or cytoskeletal biology through DNAAF5 and ARHGEF2. The sparse co-abundance structure and absence of independent functional enrichment mean these annotations should be interpreted as convergent biological clues, not as proof of a unified pathway.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: only one member is annotated in the secretome, and most proteins are intracellular or membrane-associated. The module is also not blood-cell enriched. Most genes have low immune-cell specificity or are not detected in immune cells, with no recurrent enriched blood-cell category. The HPA profile is heterogeneous, with several broadly distributed genes and cell-type-enhanced signals involving stromal, trophoblast, glial, epithelial, hepatic stellate, ciliated, and muscle-related cell types. This pattern is compatible with a shared cellular state or mixture of cell-type-associated signals across autonomic nervous system and cervix samples, rather than a simple blood contamination explanation. The limited cervix protein detection further argues against treating the module as a uniformly abundant tissue protein program.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module gene pair meets the supplied high-confidence STRING interaction criterion, and no hu.MAP complex contains multiple module members. Therefore, the co-abundance edges are not corroborated here by established physical or functional interaction databases. The absence of STRING and hu.MAP support does not invalidate the co-abundance module, but it indicates that the observed relationships may reflect coordinated expression, indirect regulation, shared cell-state composition, or context-specific biology rather than a known stable protein complex. The strongest internal hubs are IGF2BP1 and DNAAF5, while SLC2A1 connects to several central members; these network positions are data-derived and should not be confused with validated molecular interactions.

**STRING interactions (score >= 0.7)**: 0 of 28 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a context-specific co-abundance pattern because it lacks a recognizable enriched ontology signal, STRING interaction support, or hu.MAP complex support, while combining genes from RNA regulation, glucose transport, ciliary assembly, protein folding, peroxisome biology, and vesicle trafficking. However, it cannot be called a new biological discovery solely because it is absent from STRING or hu.MAP. The individual genes and their disease associations are established, and the module could arise from shared cell composition, tissue-state variation, or coordinated regulation that is not represented in current interaction resources. Its novelty is therefore best stated as a potentially novel cross-tissue co-abundance relationship requiring independent replication and experimental validation.

**Hypothesis.** Hypothesis: the module reflects a shared stress-adaptive and biosynthetic state in selected cells present in both tissues. In this model, SLC2A1 supports glucose uptake during altered energetic or oxygen conditions; IGF2BP1 and RNH1 regulate transcript stability, translation, and stress-linked RNA handling; FKBP10, PEX19, and USO1 maintain protein folding, peroxisome membrane biology, and secretory trafficking; and DNAAF5 with ARHGEF2 may capture ciliary or cytoskeletal remodeling in a subset of cells. The apparent coordination could be driven by a particular stromal, epithelial, neural-support, or ciliated cell population rather than by direct protein complex formation. This hypothesis should be tested with cell-resolved expression, independent cohorts, perturbation of SLC2A1 or IGF2BP1, and direct assays of ciliary, organelle, and trafficking phenotypes.

### Important genes

#### IGF2BP1

- **Related proteins** (co-abundance neighbors): SLC2A1 (0.87), DNAAF5 (0.82), RNH1 (0.82), USO1 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2 mRNA binding protein 1. This gene encodes a member of the insulin-like growth factor 2 mRNA-binding protein family. The protein encoded by this gene contains four K homology domains and two RNA recognition motifs. It functions by binding to the mRNAs of certain genes, including insulin-like growth factor 2, beta-actin and beta-transducin repeat-containing protein, and regulating their translation. Two transcript variants…
- **Diseases (Open Targets)**: neurodegenerative disease (0.568); coronary artery disorder (0.407); type 2 diabetes mellitus (0.403); diabetes mellitus (0.401); hypertensive disorder (0.390)
- **Europe PMC papers**: 6279
- **Why important**: IGF2BP1 is the most connected member of the module and links several otherwise distinct genes. Its established role as an RNA-binding protein regulating transcripts including IGF2 and beta-actin makes it a plausible coordinator of post-transcriptional state. Its annotations include cytokine regulation, RNA localization, stress-related mRNA stability, translation control, and stress-granule biology. It also has substantial literature and disease links spanning neurodegenerative, metabolic, cardiovascular, and hypertensive disorders.
- **Conclusion**: Established evidence supports IGF2BP1 as a central RNA-regulatory protein with broad disease relevance and a leading network position. It is a strong candidate module anchor, but the module does not establish that IGF2BP1 directly regulates the other members. The proposed role in coordinating this cross-tissue program remains a hypothesis.

#### SLC2A1

- **Related proteins** (co-abundance neighbors): IGF2BP1 (0.87), DNAAF5 (0.86), FKBP10 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 2 member 1. This gene encodes a major glucose transporter in the mammalian blood-brain barrier. The encoded protein is found primarily in the cell membrane and on the cell surface, where it can also function as a receptor for human T-cell leukemia virus (HTLV) I and II. Mutations in this gene have been found in a family with paroxysmal exertion-induced dyskinesia. [provided by RefSeq, Apr 2013].
- **Diseases (Open Targets)**: encephalopathy due to GLUT1 deficiency (0.852); childhood onset GLUT1 deficiency syndrome 2 (0.833); dystonia 9 (0.804); hereditary cryohydrocytosis with reduced stomatin (0.778); idiopathic generalized epilepsy (0.757)
- **Europe PMC papers**: 14405
- **Why important**: SLC2A1 is highly connected within the module and encodes a major glucose transporter with relevance to the blood-brain barrier, hypoxia response, nervous-system development, and pregnancy. Its HPA profile is tissue-enhanced in placenta and cell-type-enhanced in trophoblasts and Müller glia, which fits the module's mixed neural and reproductive-tissue context. Its disease associations include GLUT1 deficiency, dystonia, epilepsy, and related neurological phenotypes, and it has extensive literature.
- **Conclusion**: Established evidence identifies SLC2A1 as a central metabolic and membrane component with strong neurological and placental relevance. It supports an energetic or hypoxia-adaptive interpretation of the module. Whether altered glucose transport drives the co-abundance pattern, rather than merely marking a particular cell population, is unresolved.

#### DNAAF5

- **Related proteins** (co-abundance neighbors): SLC2A1 (0.86), IGF2BP1 (0.82), FKBP10 (0.81), ARHGEF2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein axonemal assembly factor 5. The protein encoded by this gene is essential for the preassembly or stability of axonemal dynein arms, and is found only in organisms with motile cilia and flagella. Mutations in this gene are associated with primary ciliary dyskinesia-18, a disorder characterized by abnormalities of motile cilia. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Feb 20…
- **Diseases (Open Targets)**: Kartagener Syndrome (0.789); tongue cancer (0.239); ovarian neoplasm (0.173); congenital heart disease (0.152); congenital anomaly of kidney and urinary tract (0.118)
- **Europe PMC papers**: 270
- **Why important**: DNAAF5 is among the most connected genes and is the clearest specialized marker of axonemal dynein assembly and motile-cilium biology. Its association with primary ciliary dyskinesia and Kartagener syndrome gives it strong mechanistic and disease relevance. Its HPA cell-type enhancement in endometrial ciliated cells is especially informative for interpreting the cervix-associated component.
- **Conclusion**: Established evidence supports DNAAF5 as a ciliary dynein-assembly factor and a plausible marker of ciliated-cell representation. Its presence may indicate a ciliary cell-state contribution rather than a direct interaction with the other module proteins. A role in a shared ciliary or epithelial program remains a hypothesis.

#### FKBP10

- **Related proteins** (co-abundance neighbors): SLC2A1 (0.82), DNAAF5 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FKBP prolyl isomerase 10. The protein encoded by this gene belongs to the FKBP-type peptidyl-prolyl cis/trans isomerase (PPIase) family. This protein localizes to the endoplasmic reticulum and acts as a molecular chaperone. Alternatively spliced variants encoding different isoforms have been reported, but their biological validity has not been determined.[provided by RefSeq, Nov 2009].
- **Diseases (Open Targets)**: Bruck syndrome (0.796); osteogenesis imperfecta (0.699); arthrogryposis-like syndrome (0.596); osteogenesis imperfecta type 3 (0.579); osteogenesis imperfecta type 4 (0.499)
- **Europe PMC papers**: 1158
- **Why important**: FKBP10 connects the metabolic and ciliary portions of the network and encodes an endoplasmic-reticulum molecular chaperone with protein-folding activity. Its cell-type enhancement in decidual and endometrial stromal cells, fibroblasts, granulosa cells, and hepatic stellate cells supports a stromal or matrix-producing cellular context. Its established disease associations include Bruck syndrome and osteogenesis imperfecta, indicating importance for connective-tissue biology.
- **Conclusion**: Established evidence supports FKBP10 as a protein-folding factor with connective-tissue disease relevance and cell-type patterns compatible with stromal biology. It may report secretory or extracellular-matrix stress within the module's source cells. Direct coordination with SLC2A1 or DNAAF5 is not established by the supplied interaction evidence.

#### RNH1

- **Related proteins** (co-abundance neighbors): IGF2BP1 (0.82), PEX19 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ribonuclease/angiogenin inhibitor 1. Placental ribonuclease inhibitor (PRI) is a member of a family of proteinaceous cytoplasmic RNase inhibitors that occur in many tissues and bind to both intracellular and extracellular RNases (summarized by Lee et al., 1988 [PubMed 3219362]). In addition to control of intracellular RNases, the inhibitor may have a role in the regulation of angiogenin (MIM 105850). Ribonuclease inhibitor, of 50,000…
- **Diseases (Open Targets)**: encephalitis, acute, infection-induced, susceptibility to, 12 (0.327); hypothyroidism (0.250); Encephalopathy (0.185); psoriasis (0.129); cancer (0.082)
- **Europe PMC papers**: 994
- **Why important**: RNH1 links the central IGF2BP1 portion of the network to PEX19 and is detected by immunohistochemistry in cervix tissue. It encodes a cytoplasmic inhibitor of ribonucleases and has annotations involving mRNA catabolism, tRNA stabilization, actin nucleation, cell migration, and angiogenesis. Its cell-type enhancement in decidual stromal and esophageal apical cells is consistent with a regulated epithelial or stromal state.
- **Conclusion**: Established evidence supports RNH1 as a regulator of intracellular ribonuclease activity and RNA stability with possible links to migration and angiogenesis. It is a plausible bridge between RNA homeostasis and tissue remodeling in this module. Its specific contribution to the shared autonomic nervous system and cervix pattern remains hypothetical.
