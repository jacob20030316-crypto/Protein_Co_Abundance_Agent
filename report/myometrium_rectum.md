# Conserved co-abundance modules: myometrium and rectum

## Module 0

**Tissue pair**: myometrium and rectum  
**Genes (13)**: CALD1, CNN1, CFL2, CRIP2, CSRP1, DSTN, HSPB1, MYL9, PDLIM3, PDLIM7, SMTN, SORBS1, TAGLN

### Function

The module is most consistent with a smooth-muscle contractile and actin-cytoskeletal program. The primary evidence is unusually coherent: cytoskeletal protein binding (GO:MF cytoskeletal protein binding; q_global = 0.000114), actin binding (GO:MF actin binding; q_global = 0.000515), myofibril and contractile muscle fiber (GO:CC myofibril; q_global = 0.000871) (GO:CC contractile muscle fiber; q_global = 0.000962), actin cytoskeleton (GO:CC actin cytoskeleton; q_global = 0.00116), Z disc and I band (GO:CC Z disc; q_global = 0.00174) (GO:CC I band; q_global = 0.00201), actin-cytoskeleton organization (GO:BP actin cytoskeleton organization; q_global = 0.00272), actin-filament processes (GO:BP actin filament-based process; q_global = 0.00433), sarcomere (GO:CC sarcomere; q_global = 0.00562), muscle structure development (GO:BP muscle structure development; q_global = 0.0113), stress fibers and contractile actin bundles (GO:CC stress fiber; q_global = 0.0182) (GO:CC contractile actin filament bundle; q_global = 0.0182), actomyosin (GO:CC actomyosin; q_global = 0.0234), actin-filament bundles (GO:CC actin filament bundle; q_global = 0.0265), and cytoskeleton organization (GO:BP cytoskeleton organization; q_global = 0.0303) all passed global correction. The genes collectively cover contractile apparatus components, actin-binding and actin-remodeling proteins, cytoskeletal adaptors, focal-adhesion-associated proteins, and stress-response machinery. The agreement between the co-abundance structure, the globally corrected GO terms, and the supplementary STRING enrichments supports a biological program rather than an interpretation based on one annotation alone. The module should nevertheless be interpreted as a coordinated expression state, not as proof that every encoded protein physically interacts or that the module is restricted to one muscle subtype.

**Cell composition.** The HPA evidence argues strongly against a plasma-protein or secreted-protein explanation: no module gene is annotated as secreted. Most genes show tissue or cell-type enrichment, especially in blood vessels, intestine, smooth muscle cells, or vascular smooth muscle cells. The module is therefore more consistent with shared smooth-muscle, vascular-muscle, myoepithelial, stromal, or related contractile cell populations present in both tissues than with broadly expressed housekeeping genes. Several genes have low immune-cell specificity or are not detected in immune cells, although some show enrichment in selected blood-cell populations. This leaves a possible contribution from vascular or stromal components, but the overall HPA pattern does not primarily support a blood-cell contamination explanation. Protein detection is broader in myometrium than in rectum, while several core genes are detected in both tissues; this supports a conserved cellular program with possible tissue-specific protein-level differences.

**GO/KEGG enrichment**: 16 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF cytoskeletal protein binding | 0.000114 | CALD1, CFL2, CNN1, CSRP1, DSTN, MYL9, PDLIM3, PDLIM7, SMTN, SORBS1, TAGLN |
| GO:MF actin binding | 0.000515 | CALD1, CFL2, CNN1, DSTN, PDLIM3, PDLIM7, SMTN, SORBS1, TAGLN |
| GO:CC myofibril | 0.000871 | CALD1, CFL2, CSRP1, HSPB1, MYL9, PDLIM3, PDLIM7 |
| GO:CC contractile muscle fiber | 0.000962 | CALD1, CFL2, CSRP1, HSPB1, MYL9, PDLIM3, PDLIM7 |
| GO:CC actin cytoskeleton | 0.00116 | CALD1, CFL2, CNN1, DSTN, MYL9, PDLIM3, PDLIM7, SMTN, SORBS1 |
| GO:CC Z disc | 0.00174 | CFL2, CSRP1, HSPB1, MYL9, PDLIM3, PDLIM7 |
| GO:CC I band | 0.00201 | CFL2, CSRP1, HSPB1, MYL9, PDLIM3, PDLIM7 |
| GO:BP actin cytoskeleton organization | 0.00272 | CALD1, CFL2, CNN1, CSRP1, DSTN, MYL9, PDLIM3, PDLIM7, SORBS1 |
| GO:BP actin filament-based process | 0.00433 | CALD1, CFL2, CNN1, CSRP1, DSTN, MYL9, PDLIM3, PDLIM7, SORBS1 |
| GO:CC sarcomere | 0.00562 | CFL2, CSRP1, HSPB1, MYL9, PDLIM3, PDLIM7 |
| GO:BP muscle structure development | 0.0113 | CFL2, CSRP1, MYL9, PDLIM3, PDLIM7, SMTN, TAGLN |
| GO:CC stress fiber | 0.0182 | CALD1, MYL9, PDLIM3, PDLIM7, SORBS1 |
| GO:CC contractile actin filament bundle | 0.0182 | CALD1, MYL9, PDLIM3, PDLIM7, SORBS1 |
| GO:CC actomyosin | 0.0234 | CALD1, MYL9, PDLIM3, PDLIM7, SORBS1 |
| GO:CC actin filament bundle | 0.0265 | CALD1, MYL9, PDLIM3, PDLIM7, SORBS1 |

### STRING and hu.MAP

STRING provides known high-confidence relationships among CALD1, CNN1, MYL9, TAGLN, and SMTN, forming a contractile smooth-muscle-centered interaction group. It also supports the actin-remodeling relationship between CFL2 and DSTN. These relationships are concordant with the module's actin-binding, contractile-fiber, and muscle annotations, so part of the module recapitulates established molecular biology. The STRING functional results independently reinforce cytoskeletal protein binding, actin organization, myofibril, Z-disc, muscle, and smooth-muscle themes, but they remain supplementary evidence rather than globally corrected enrichment. hu.MAP identifies three complexes containing the DSTN-CFL2 pair, with additional actin-regulatory or actin-associated proteins in the corresponding complexes. The limited hu.MAP overlap means that the module is not itself a single established hu.MAP complex; rather, it appears to combine a known actin-dynamics subcomplex with a broader co-abundance program. Lack of hu.MAP assignments for the other genes does not imply lack of biological association.

**STRING interactions (score >= 0.7)**: 9 of 78 gene pairs: CALD1–CNN1 (0.867); CALD1–MYL9 (0.844); CALD1–TAGLN (0.794); CFL2–DSTN (0.921); CNN1–MYL9 (0.771); CNN1–SMTN (0.799); CNN1–TAGLN (0.781); MYL9–TAGLN (0.929); SMTN–TAGLN (0.798)
**STRING functional enrichment (supplementary, within-query FDR)**: NetworkNeighborAL Mixed, incl. Contractile fiber, and Microfilament motor activity (FDR = 1.25e-05, 7 genes); Function Cytoskeletal protein binding (FDR = 3.14e-05, 11 genes); Process Actin cytoskeleton organization (FDR = 6.08e-05, 10 genes); Function Actin binding (FDR = 9.19e-05, 9 genes); Component Cytoskeleton (FDR = 0.0003, 11 genes); Component Myofibril (FDR = 0.0003, 7 genes); Component Z disc (FDR = 0.0003, 6 genes); Component Actin cytoskeleton (FDR = 0.00051, 8 genes); Component Intracellular non-membrane-bounded organelle (FDR = 0.0009, 12 genes); Component Supramolecular fiber (FDR = 0.0011, 8 genes); PMID (2023) Integrated bioinformatics and wet-lab analysis revealed cell adhesion prominent genes CDC42, TAGLN and GSN as prognostic biomarkers in colonic-polyp lesions. (FDR = 0.0012, 8 genes); TISSUES Smooth muscle (FDR = 0.0034, 4 genes); TISSUES Vertebrate muscular system (FDR = 0.0034, 8 genes); Process Muscle structure development (FDR = 0.0038, 7 genes); NetworkNeighborAL Muscle protein, and Myosin light chain kinase activity (FDR = 0.0057, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03395.1 (DSTN, CFL2; 2/6); huMAP3_09579.1 (DSTN, CFL2; 2/9); huMAP3_11076.1 (DSTN, CFL2; 2/10)

### Novelty

This is unlikely to be a wholly new molecular function: the contractile smooth-muscle and actin-cytoskeletal interpretation is strongly established by globally corrected GO evidence, known STRING relationships, HPA cell-type enrichment, and gene literature. The potentially novel aspect is the conserved co-abundance configuration shared by myometrium and rectum, especially the coordinated inclusion of contractile proteins, cytoskeletal adaptors, and actin-remodeling genes across these tissues. The fact that several module relationships are absent from STRING or hu.MAP is compatible with an expression-level association, tissue-context effect, or incomplete database coverage, but it cannot establish novelty by itself. A defensible claim is therefore that the shared cross-tissue module may represent a newly observed tissue-pair-specific organization of a largely known smooth-muscle program, pending comparison with published co-expression modules and independent cohorts.

**Hypothesis.** Hypothesis: the module reflects a conserved contractile-cell state shared by myometrium and rectum in which actomyosin force generation is coupled to actin-filament turnover, stress-fiber or focal-adhesion organization, and mechanical-stress adaptation. In this model, MYL9, CNN1, CALD1, TAGLN, and SMTN support contractile filament regulation; PDLIM3, PDLIM7, CSRP1, and SORBS1 organize or anchor cytoskeletal structures; and CFL2 with DSTN tunes actin-filament remodeling. HSPB1 may contribute to proteostatic or stress adaptation within the same cellular state. This is a mechanistic model inferred from co-abundance and annotations, not evidence of direct physical interaction among all module members or of a demonstrated causal pathway.

### Important genes

#### MYL9

- **Related proteins** (co-abundance neighbors): CSRP1 (0.89), CNN1 (0.87), PDLIM3 (0.84), TAGLN (0.83), SORBS1 (0.83), DSTN (0.83); STRING partners: CALD1 (0.844), CNN1 (0.771), TAGLN (0.929)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin light chain 9. Myosin, a structural component of muscle, consists of two heavy chains and four light chains. The protein encoded by this gene is a myosin light chain that may regulate muscle contraction by modulating the ATPase activity of myosin heads. The encoded protein binds calcium and is activated by myosin light chain kinase. Two transcript variants encoding different isoforms have been found for this gen…
- **Diseases (Open Targets)**: megacystis-microcolon-intestinal hypoperistalsis syndrome 4 (0.566); diabetic ketoacidosis (0.319); familial visceral myopathy (0.289); visceral myopathy 1 (0.288); Abnormality of the skeletal system (0.168)
- **Europe PMC papers**: 3103
- **Why important**: MYL9 is a highly connected module member and is detected in both myometrium and rectum. It appears in nearly all of the core contractile and cytoskeletal global terms, including myofibril, sarcomere, actomyosin, stress-fiber, and actin-bundle terms (11 globally significant GO/KEGG terms, q_global 0.000114–0.0303; see the table). Its known function as a myosin light chain regulating muscle contraction provides a direct bridge between the module's expression pattern and force generation. STRING supports relationships with CALD1, CNN1, and TAGLN, while the literature and disease associations include visceral myopathy and nemaline-related intestinal or muscle phenotypes.
- **Conclusion**: Established: MYL9 is a central contractile effector and a strong anchor for the module's smooth-muscle interpretation. Hypothesis: coordinated MYL9 abundance may tune contractile force or mechanical tone in both tissues, but the fact sheet does not establish altered phosphorylation, enzymatic activity, or causality.

#### CNN1

- **Related proteins** (co-abundance neighbors): TAGLN (0.94), PDLIM3 (0.88), CSRP1 (0.88), MYL9 (0.87), DSTN (0.84), CALD1 (0.83); STRING partners: CALD1 (0.867), MYL9 (0.771), SMTN (0.799), TAGLN (0.781)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Actin filaments; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calponin 1. Predicted to enable actin binding activity. Involved in negative regulation of vascular associated smooth muscle cell proliferation. Located in cytoskeleton. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.356); self-injurious ideation (0.114); breast cancer (0.096); neoplasm (0.093); breast carcinoma (0.086)
- **Europe PMC papers**: 3024
- **Why important**: CNN1 has a highly central network position, is localized to actin filaments, and is tissue-enhanced in blood vessel, intestine, and smooth muscle. It contributes to the globally corrected actin-binding and cytoskeletal terms (6 globally significant GO/KEGG terms, q_global 0.000114–0.0303; see the table) and has extensive literature. Its annotated roles include smooth-muscle contraction, actomyosin organization, and negative regulation of vascular smooth-muscle proliferation. STRING links it to CALD1, MYL9, SMTN, and TAGLN, connecting it to the best-supported contractile component of the network.
- **Conclusion**: Established: CNN1 is a well-supported actin-associated smooth-muscle marker and likely structural regulator in this module. Hypothesis: its abundance may couple contractile differentiation with restraint of vascular-like smooth-muscle proliferation, although that coupling is not demonstrated in these tissues by the fact sheet.

#### CALD1

- **Related proteins** (co-abundance neighbors): PDLIM7 (0.86), SORBS1 (0.84), CNN1 (0.83), CSRP1 (0.83); STRING partners: CNN1 (0.867), MYL9 (0.844), TAGLN (0.794)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Actin filaments; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: caldesmon 1. This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating…
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.499); diaphragmatic hernia (0.447); glaucoma (0.405); diverticular disease (0.393); open-angle glaucoma (0.390)
- **Europe PMC papers**: 3386
- **Why important**: CALD1 participates in many globally corrected terms spanning cytoskeletal binding, actin binding, contractile fibers, stress fibers, actomyosin, and actin-bundle organization (12 globally significant GO/KEGG terms, q_global 0.000114–0.0303; see the table). Its annotated protein functions directly include binding to actin, calmodulin, tropomyosin, myosin, and phospholipids, and regulating smooth-muscle contraction. Its network links to CNN1 and MYL9 are supported by STRING, while its tissue and cellular annotations are compatible with contractile stromal or muscle cells.
- **Conclusion**: Established: CALD1 is a plausible molecular integrator of actin filaments and contractile regulation. Hypothesis: it may help translate calcium-sensitive signaling into coordinated actomyosin behavior in the shared module, but the co-abundance data do not demonstrate calcium dependence or direct regulation.

#### TAGLN

- **Related proteins** (co-abundance neighbors): CNN1 (0.94), CSRP1 (0.91), PDLIM3 (0.88), MYL9 (0.83); STRING partners: CALD1 (0.794), CNN1 (0.781), MYL9 (0.929), SMTN (0.798)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Mitochondria, Cytosol; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: transgelin. This gene encodes a shape change and transformation sensitive actin-binding protein which belongs to the calponin family. It is ubiquitously expressed in vascular and visceral smooth muscle, and is an early marker of smooth muscle differentiation. The encoded protein is thought to be involved in calcium-independent smooth muscle contraction. It acts as a tumor suppressor, and the loss of its expre…
- **Diseases (Open Targets)**: hypertensive disorder (0.242); diverticular disease (0.216); refractive error (0.209); essential hypertension (0.201); hypothyroidism (0.161)
- **Europe PMC papers**: 6125
- **Why important**: TAGLN is a canonical smooth-muscle-associated actin-binding protein with the largest literature representation among the module genes. It is detected in both tissues, enriched in blood vessel and intestine, and connected in STRING to CALD1, CNN1, MYL9, and SMTN. It contributes to globally corrected cytoskeletal protein-binding, actin-binding, and muscle-development terms (GO:MF cytoskeletal protein binding; q_global = 0.000114) (GO:MF actin binding; q_global = 0.000515) (GO:BP muscle structure development; q_global = 0.0113). Its annotation as an early smooth-muscle differentiation marker and its reported association with calcium-independent smooth-muscle contraction make it an important identity and state marker.
- **Conclusion**: Established: TAGLN strongly supports a differentiated contractile-cell interpretation and connects several core network members. Hypothesis: TAGLN may help stabilize a contractile phenotype in both tissues, but its abundance alone cannot establish preserved contractile function or tumor-suppressive activity.

#### PDLIM3

- **Related proteins** (co-abundance neighbors): CNN1 (0.88), TAGLN (0.88), SORBS1 (0.87), MYL9 (0.84), CSRP1 (0.83), CRIP2 (0.83); STRING partners: none
- **HPA**: Group enriched; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in myometrium
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PDZ and LIM domain 3. The protein encoded by this gene contains a PDZ domain and a LIM domain, indicating that it may be involved in cytoskeletal assembly. In support of this, the encoded protein has been shown to bind the spectrin-like repeats of alpha-actinin-2 and to colocalize with alpha-actinin-2 at the Z lines of skeletal muscle. Alternatively spliced transcript variants encoding multiple isoforms have been obser…
- **Diseases (Open Targets)**: glomerulonephritis (0.338); viral pneumonia (0.289); nephrotic syndrome (0.271); hypertrophic cardiomyopathy (0.217); dilated cardiomyopathy (0.208)
- **Europe PMC papers**: 942
- **Why important**: PDLIM3 has a highly central network position and is the only selected gene represented in every globally corrected GO term listed for the module (16 globally significant GO/KEGG terms, q_global 0.000114–0.0303; see the table). Its PDZ and LIM domains are annotated as mediators of cytoskeletal assembly, and its reported localization with alpha-actinin at muscle Z lines fits the module's Z-disc, I-band, sarcomere, and contractile-fiber evidence. It is enriched in smooth-muscle cells and myonuclei-related populations, and its disease associations include cardiomyopathies. Although it lacks STRING partners and hu.MAP assignments in the fact sheet, its network centrality and annotation breadth make it a key organizational candidate.
- **Conclusion**: Established: PDLIM3 is a strong cytoskeletal-organizing marker that links the module to muscle structural assemblies. Hypothesis: PDLIM3 may act as an organizing scaffold that coordinates contractile proteins with Z-line-like or adhesion-associated structures in the shared tissues; direct interactions in this module remain unconfirmed.

## Module 1

**Tissue pair**: myometrium and rectum  
**Genes (6)**: COPB1, HSD17B4, GARS1, SEC24D, DARS1, UGGT1

### Function

No GO/KEGG term passed global correction, so the module does not support a formally significant pathway assignment from enrichment analysis. Its gene-level biology is nevertheless coherent at the level of intracellular protein handling, but heterogeneous in detail. SEC24D and COPB1 support COPII and COPI-related endoplasmic-reticulum–Golgi vesicle trafficking, while UGGT1 supports endoplasmic-reticulum glycoprotein quality control. GARS1 and DARS1 support aminoacyl-tRNA charging and protein translation. HSD17B4 contributes peroxisomal fatty-acid beta-oxidation and steroid-related metabolism. The co-abundance structure therefore appears to combine protein production and trafficking machinery with organellar lipid metabolism rather than representing a single established biochemical pathway. The lack of significant GO/KEGG enrichment does not invalidate the module; it indicates that the shared expression pattern is not sufficiently specific for the tested term set.

**Cell composition.** The HPA profile argues against a module dominated by plasma proteins, secreted proteins, or strongly immune-restricted genes. The individual annotations describe predominantly intracellular locations, including vesicles, cytosol, Golgi apparatus, and peroxisomes, although the module-level HPA summary identifies some secreted genes. Most genes have low tissue specificity, and most have low immune-cell specificity. One gene is liver enhanced, and several show cell-type-enhanced patterns involving endocrine, alveolar, erythroid, hepatocyte, plasma-cell, or basophil populations. Protein detection is broadly present in both myometrium and rectum, with DARS1 being the notable exception in myometrium. Thus, a shared broadly expressed cellular program is more plausible than a blood-contamination explanation, although contributions from shared or variable cell populations cannot be excluded.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides one high-confidence relationship within the module, between DARS1 and GARS1. This supports a known connection between the two aminoacyl-tRNA synthetase genes and strengthens the interpretation of a translation-related substructure. The remaining co-abundance links are not supported by the supplied high-confidence STRING interaction list, so they should be treated as expression relationships rather than established physical interactions. No hu.MAP complex contains multiple module members, providing no independent complex-level support. SEC24D and COPB1 have complementary vesicle-trafficking annotations, and SEC24D is connected in the co-abundance graph to both COPB1 and UGGT1, but the supplied resources do not establish a shared physical complex for these module members.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: DARS1–GARS1 (0.772)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be called a new molecular complex or a newly discovered pathway. Its component functions are established, and the DARS1–GARS1 relationship is already represented in STRING. The module may still be a potentially novel tissue-pair co-abundance observation because the supplied evidence does not show a previously catalogued hu.MAP complex or a broad STRING interaction pattern spanning all members. However, absence from hu.MAP or STRING alone does not demonstrate novelty. A defensible claim is therefore that the shared myometrium–rectum co-abundance pattern is insufficiently characterized by the supplied interaction databases, rather than proven to be biologically new.

**Hypothesis.** Hypothesis: the module reflects a shared demand for proteostasis and intracellular biosynthetic capacity in cells present in both tissues. Endoplasmic-reticulum quality control through UGGT1, cargo selection and vesicle export through SEC24D, and Golgi-to-endoplasmic-reticulum retrieval through COPB1 could coordinate the handling of newly synthesized proteins. GARS1 and DARS1 may mark the translational supply that produces those proteins, while HSD17B4 may couple the state of this cellular program to peroxisomal lipid and steroid metabolism. This is a mechanistic interpretation of the co-abundance pattern, not an established physical interaction model; it should be tested with protein-level interaction, cell-type-resolved expression, and perturbation data.

### Important genes

#### SEC24D

- **Related proteins** (co-abundance neighbors): COPB1 (0.85), UGGT1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC24 homolog D, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. This gene product is implicated in the shaping of the vesicle, and also in cargo selection and concentration. Mut…
- **Diseases (Open Targets)**: Cole-Carpenter syndrome (0.753); hereditary disease (0.380); osteogenesis imperfecta type 1 (0.370); Seizure (0.259); Intellectual disability (0.259)
- **Europe PMC papers**: 780
- **Why important**: SEC24D is a highly connected node in the module and links the vesicle-trafficking branch to both COPB1 and UGGT1. Its established function in COPII vesicle budding, cargo selection, and endoplasmic-reticulum–Golgi transport gives the module a plausible protein-trafficking anchor. It is detected in both tissues, has low tissue specificity, and has substantial literature coverage. Its disease associations include Cole-Carpenter syndrome and osteogenesis imperfecta type one.
- **Conclusion**: Established: SEC24D is a broadly expressed COPII component with a central network position and documented links to inherited skeletal disease. Hypothesis: its co-abundance with UGGT1 and COPB1 may indicate coordinated protein export and membrane trafficking in shared tissue-resident cells.

#### UGGT1

- **Related proteins** (co-abundance neighbors): HSD17B4 (0.84), SEC24D (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: UDP-glucose glycoprotein glucosyltransferase 1. UDP-glucose:glycoprotein glucosyltransferase (UGT) is a soluble protein of the endoplasmic reticulum (ER) that selectively reglucosylates unfolded glycoproteins, thus providing quality control for protein transport out of the ER.[supplied by OMIM, Oct 2009].
- **Diseases (Open Targets)**: congenital disorder of glycosylation (0.416); hypercholesterolemia, familial, 1 (0.333); connective tissue disorder (0.234); ovarian dysfunction (0.216); chronic laryngitis (0.147)
- **Europe PMC papers**: 507
- **Why important**: UGGT1 is a highly connected node joining SEC24D with HSD17B4. Its established role as an endoplasmic-reticulum quality-control glucosyltransferase connects the trafficking branch to glycoprotein folding and secretion competence. It is detected in both tissues, has low tissue specificity, and has documented associations with congenital disorders of glycosylation and other disease categories.
- **Conclusion**: Established: UGGT1 supports recognition and reglucosylation of incompletely folded glycoproteins in the endoplasmic reticulum. Hypothesis: its module-level association with trafficking and metabolic genes may reflect coordinated proteostasis rather than a direct physical complex.

#### HSD17B4

- **Related proteins** (co-abundance neighbors): UGGT1 (0.84), GARS1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Peroxisomes; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hydroxysteroid 17-beta dehydrogenase 4. The protein encoded by this gene is a bifunctional enzyme that is involved in the peroxisomal beta-oxidation pathway for fatty acids. It also acts as a catalyst for the formation of 3-ketoacyl-CoA intermediates from both straight-chain and 2-methyl-branched-chain fatty acids. Defects in this gene that affect the peroxisomal fatty acid beta-oxidation activity are a cause of D-bifunctional protein d…
- **Diseases (Open Targets)**: d-bifunctional protein deficiency (0.830); Perrault syndrome 1 (0.761); Perrault syndrome (0.736); hereditary disease (0.488); hearing loss disorder (0.370)
- **Europe PMC papers**: 1624
- **Why important**: HSD17B4 is a highly connected bridge between UGGT1 and GARS1 and has the strongest tissue-specific signal in the module, with liver enhancement and cell-type enhancement in alveolar cells and hepatocytes. Its established peroxisomal role in fatty-acid beta-oxidation, together with steroid and fatty-acid metabolic annotations, adds a metabolic dimension that is not explained by vesicle trafficking alone. It has the largest literature volume among the module genes and strong disease associations involving D-bifunctional protein deficiency and Perrault syndrome.
- **Conclusion**: Established: HSD17B4 is a peroxisomal metabolic enzyme with important inherited-disease relevance. Hypothesis: its position between the endoplasmic-reticulum quality-control branch and the translation branch may indicate that cellular proteostasis is co-regulated with lipid or steroid metabolism.

#### GARS1

- **Related proteins** (co-abundance neighbors): DARS1 (0.82), HSD17B4 (0.80); STRING partners: DARS1 (0.772)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycyl-tRNA synthetase 1. This gene encodes glycyl-tRNA synthetase, one of the aminoacyl-tRNA synthetases that charge tRNAs with their cognate amino acids. The encoded enzyme is an (alpha)2 dimer which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Two transcript variants encoding different isoforms ha…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease type 2D (0.790); neuronopathy, distal hereditary motor, type 5A (0.729); neuronopathy, distal hereditary motor, type 5 (0.698); spinal muscular atrophy, infantile, James type (0.649); Charcot-Marie-Tooth disease type 2 (0.565)
- **Europe PMC papers**: 302
- **Why important**: GARS1 occupies a central position in the co-abundance topology and is the partner of DARS1 in the only high-confidence STRING relationship supplied for the module. Its established function in glycyl-tRNA aminoacylation provides direct support for a protein-translation substructure. It is detected in both tissues, has low tissue and immune specificity, and is associated with Charcot-Marie-Tooth disease and related motor neuron disorders.
- **Conclusion**: Established: GARS1 is a cytosolic and mitochondrial glycyl-tRNA synthetase with a known relationship to DARS1 in the supplied STRING evidence. Hypothesis: GARS1 may represent the translational-demand component that links biosynthetic activity to the trafficking and quality-control genes.

#### DARS1

- **Related proteins** (co-abundance neighbors): GARS1 (0.82); STRING partners: GARS1 (0.772)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aspartyl-tRNA synthetase 1. This gene encodes a member of a multienzyme complex that functions in mediating the attachment of amino acids to their cognate tRNAs. The encoded protein ligates L-aspartate to tRNA(Asp). Mutations in this gene have been found in patients showing hypomyelination with brainstem and spinal cord involvement and leg spasticity. Alternative splicing results in multiple transcript variants. [provided by…
- **Diseases (Open Targets)**: hypomyelination with brain stem and spinal cord involvement and leg spasticity (0.773); atrial fibrillation (0.268); Abnormal brain morphology (0.266); tooth hard tissue disease (0.226); Pancreatic pseudocyst (0.225)
- **Europe PMC papers**: 238
- **Why important**: DARS1 is important because it forms the only supplied high-confidence STRING pair within the module, together with GARS1, and because its annotation includes translation, aspartyl-tRNA aminoacylation, and protein-containing complex assembly. It is detected in rectum but not myometrium, making it a useful marker of tissue-specific representation within an otherwise broadly detected module. Its disease associations include hypomyelination with brainstem and spinal cord involvement and leg spasticity, while its literature volume is more limited than that of the major trafficking and metabolic genes.
- **Conclusion**: Established: DARS1 is an aspartyl-tRNA synthetase with a supported relationship to GARS1 and established neurological disease associations. Hypothesis: the absence of myometrial protein detection may reflect cell composition, regulation at the protein level, or measurement sensitivity rather than absence of its transcript-level co-abundance signal.

## Module 2

**Tissue pair**: myometrium and rectum  
**Genes (10)**: DPYSL2, DPYSL3, EHD2, FERMT2, ILK, CKB, PARVA, TGFB1I1, TPM1, TPM2

### Function

The module is best interpreted as a smooth-muscle contractile and cytoskeletal adhesion program. The primary enrichment evidence is strong and internally coherent: cytoskeleton organization (GO:BP cytoskeleton organization; q_global = 0.0194), sarcomere (GO:CC sarcomere; q_global = 0.02), supramolecular polymers and fibers (GO:CC supramolecular polymer; q_global = 0.0265) (GO:CC supramolecular fiber; q_global = 0.0265), myofibril (GO:CC myofibril; q_global = 0.0363), heart morphogenesis (GO:BP heart morphogenesis; q_global = 0.0379), and contractile muscle fiber (GO:CC contractile muscle fiber; q_global = 0.0391). ILK, FERMT2, PARVA, TPM1, and TPM2 define an integrin-linked focal-adhesion and actin–sarcomere axis, while DPYSL2, DPYSL3, and EHD2 extend the module toward cytoskeletal remodeling, membrane organization, and cell projection biology. The heart-morphogenesis annotation should be interpreted as a developmental association rather than evidence that the module is cardiac-specific. The pattern is also consistent with the smooth-muscle and connective-tissue context of the two sampled tissues. STRING supplementary annotations independently point toward connective tissue, sarcomere, cytoskeleton, lamellipodia, leading edge, actin filaments, and supramolecular fibers (11 supplementary STRING terms; within-query FDR 0.0081–0.0459), but these are supportive rather than globally corrected GO/KEGG evidence.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. It is also not predominantly a blood-cell module. HPA indicates cell-type enhancement for every module gene, with smooth-muscle cells the most frequent enriched cell type and additional enrichment in peritubular myoid, vascular smooth-muscle, stromal, and related contractile or mesenchymal populations. Several genes have immune-cell annotations, including DPYSL2, TPM1, TPM2, TGFB1I1, PARVA, and CKB, but the overall pattern is more compatible with a shared smooth-muscle, stromal, or contractile cell component than with a blood contaminant. Five genes are tissue-enhanced and the remainder have low tissue specificity, so the module combines contractile-cell markers with broadly distributed cytoskeletal functions. Protein detection in both myometrium and rectum for most genes supports biological detectability in both tissues. EHD2, DPYSL3, and DPYSL2 show tissue-specific detection differences, so some components may reflect differing cell composition or protein abundance between the tissues.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP cytoskeleton organization | 0.0194 | DPYSL2, DPYSL3, EHD2, FERMT2, ILK, PARVA, TPM1, TPM2 |
| GO:CC sarcomere | 0.02 | FERMT2, ILK, PARVA, TPM1, TPM2 |
| GO:CC supramolecular polymer | 0.0265 | DPYSL2, DPYSL3, FERMT2, ILK, PARVA, TPM1, TPM2 |
| GO:CC supramolecular fiber | 0.0265 | DPYSL2, DPYSL3, FERMT2, ILK, PARVA, TPM1, TPM2 |
| GO:CC myofibril | 0.0363 | FERMT2, ILK, PARVA, TPM1, TPM2 |
| GO:BP heart morphogenesis | 0.0379 | ILK, PARVA, TPM1 |
| GO:CC contractile muscle fiber | 0.0391 | FERMT2, ILK, PARVA, TPM1, TPM2 |

### STRING and hu.MAP

STRING contains a connected set of known or strongly supported relationships: DPYSL2–DPYSL3, FERMT2–ILK, FERMT2–PARVA, ILK–PARVA, ILK–TGFB1I1, PARVA–TGFB1I1, and TPM1–TPM2. The strongest relational anchors are the ILK–PARVA–FERMT2 focal-adhesion group, the TPM1–TPM2 tropomyosin pair, and the DPYSL2–DPYSL3 collapsin-response-mediator pair. hu.MAP independently places DPYSL2 with DPYSL3 in several complexes (hu.MAP huMAP3_00051.1) (hu.MAP huMAP3_11599.1) (hu.MAP huMAP3_11626.1), TPM1 with TPM2 in a tropomyosin complex (hu.MAP huMAP3_06153.1), and ILK with PARVA in integrin-associated complexes (hu.MAP huMAP3_09385.1) (hu.MAP huMAP3_11194.1). These complexes also contain proteins not present in the module, including other tropomyosins, LIM-domain and adhesion proteins, and additional neuronal or cytoskeletal proteins. Thus, the module contains recognizable molecular subassemblies rather than an entirely unconnected gene list. At the same time, the absence of STRING or hu.MAP links for several co-abundance edges means that the abundance network may capture tissue-level co-regulation, shared cell origin, or indirect coordination rather than direct physical binding.

**STRING interactions (score >= 0.7)**: 7 of 45 gene pairs: DPYSL2–DPYSL3 (0.976); FERMT2–ILK (0.997); FERMT2–PARVA (0.893); ILK–PARVA (0.999); ILK–TGFB1I1 (0.745); PARVA–TGFB1I1 (0.724); TPM1–TPM2 (0.993)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Connective tissue (FDR = 0.0081, 8 genes); Component Sarcomere (FDR = 0.0122, 5 genes); Component Cytoskeleton (FDR = 0.0216, 8 genes); Component Muscle thin filament tropomyosin (FDR = 0.0301, 2 genes); Component Lamellipodium (FDR = 0.0301, 4 genes); Component Cell leading edge (FDR = 0.0301, 5 genes); Component Intracellular non-membrane-bounded organelle (FDR = 0.0301, 9 genes); Component Supramolecular fiber (FDR = 0.0301, 6 genes); Component Plasma membrane bounded cell projection (FDR = 0.0301, 7 genes); Component Actin cytoskeleton (FDR = 0.0455, 5 genes); Component Actin filament (FDR = 0.0459, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_00051.1 (DPYSL3, DPYSL2; 2/6); huMAP3_06153.1 (TPM2, TPM1; 2/6); huMAP3_11599.1 (DPYSL3, DPYSL2; 2/8); huMAP3_09385.1 (ILK, PARVA; 2/8); huMAP3_11194.1 (ILK, PARVA; 2/10); huMAP3_11626.1 (DPYSL3, DPYSL2; 2/42)

### Novelty

The module should not be called a wholly new molecular pathway. Its principal components and several pairwise relationships are already established through STRING and hu.MAP, and the annotations of integrin-linked adhesion, actin organization, tropomyosin-based contractility, and collapsin-response-mediator cytoskeletal biology are established. The potentially novel aspect is the conserved co-abundance of these components across myometrium and rectum, particularly the joint association of smooth-muscle contractile machinery, focal-adhesion signaling, membrane organization, and DPYSL proteins in this tissue pair. However, absence from STRING or hu.MAP alone cannot establish novelty, and the supplied evidence does not demonstrate prior literature-wide absence of this cross-tissue module. The defensible conclusion is that this is a potentially novel tissue-pair co-abundance configuration built from largely known molecular functions and interactions.

**Hypothesis.** Hypothesis: a shared smooth-muscle or contractile stromal cell population in myometrium and rectum coordinates integrin–extracellular-matrix adhesion with actin and sarcomeric contractility. In this model, FERMT2, ILK, and PARVA organize integrin-linked focal adhesions; TPM1 and TPM2 stabilize actin filaments and support contractile force transmission; TGFB1I1 may connect adhesion and transforming-growth-factor-responsive transcriptional programs; EHD2 may couple plasma-membrane organization to the actin cytoskeleton; and DPYSL2 with DPYSL3 may contribute cytoskeletal remodeling or cell-projection behavior. The shared abundance pattern could therefore reflect a conserved mechanical or contractile state across the two tissues. This is a hypothesis from the integrated network and annotation pattern, not a demonstrated causal mechanism.

### Important genes

#### ILK

- **Related proteins** (co-abundance neighbors): TGFB1I1 (0.87), FERMT2 (0.87), EHD2 (0.87), PARVA (0.85), DPYSL3 (0.82), DPYSL2 (0.81); STRING partners: FERMT2 (0.997), PARVA (0.999), TGFB1I1 (0.745)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK is the highest-connectivity hub in the supplied module and connects the focal-adhesion group to TGFB1I1, EHD2, DPYSL3, and DPYSL2. It appears in every primary GO/KEGG term (7 globally significant GO/KEGG terms, q_global 0.0194–0.0391; see the table), is present in multiple supplementary STRING terms (6 supplementary STRING terms; within-query FDR 0.0122–0.0301), and participates in the ILK–PARVA hu.MAP complexes (hu.MAP huMAP3_09385.1) (hu.MAP huMAP3_11194.1). Its HPA localization at focal-adhesion sites, detection in both tissues, smooth-muscle cell enhancement, integrin-linked signaling annotation, and substantial literature support make it a central mechanistic organizer. Its disease associations include cardiovascular and neoplastic categories.
- **Conclusion**: Established evidence supports ILK as a central integrin-linked cytoskeletal and adhesion component of the module. It is a strong candidate for coordinating contractile-cell adhesion with cytoskeletal state. Whether its abundance is causally responsible for conservation between the tissues remains untested.

#### PARVA

- **Related proteins** (co-abundance neighbors): ILK (0.85); STRING partners: FERMT2 (0.893), ILK (0.999), TGFB1I1 (0.724)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Actin filaments, Focal adhesion sites; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: huMAP3_09385.1, huMAP3_11194.1
- **Function (MyGene.info)**: parvin alpha. This gene encodes a member of the parvin family of actin-binding proteins. Parvins are associated with focal contacts and contain calponin homology domains that bind to actin filaments. The encoded protein is part of the integrin-linked kinase signaling complex and plays a role in cell adhesion, motility and survival. [provided by RefSeq, Dec 2010].
- **Diseases (Open Targets)**: neurodegenerative disease (0.487); osteoarthritis, hip (0.339); total hip arthroplasty (0.339); open-angle glaucoma (0.337); Pancreatic pseudocyst (0.331)
- **Europe PMC papers**: 3949
- **Why important**: PARVA is a focal-adhesion and actin-filament protein with a near-hub role in the focal-adhesion subnetwork. It is linked in STRING to ILK, FERMT2, and TGFB1I1 and occurs with ILK in hu.MAP complexes (hu.MAP huMAP3_09385.1) (hu.MAP huMAP3_11194.1). It is present in all primary enrichment terms (7 globally significant GO/KEGG terms, q_global 0.0194–0.0391; see the table) and many supportive STRING annotations, including sarcomere, lamellipodium, leading edge, actin cytoskeleton, and supramolecular fiber (9 supplementary STRING terms; within-query FDR 0.0081–0.0455). HPA identifies smooth-muscle cell enhancement and focal-adhesion or actin-filament localization. Its function in adhesion, polarity, motility, survival, and actin organization directly matches the inferred module function.
- **Conclusion**: Established evidence supports PARVA as an adhesion-to-actin integrator within the module. It plausibly helps transmit extracellular-matrix or integrin signals into contractile-cell architecture, but that tissue-pair-specific role is a hypothesis.

#### TPM1

- **Related proteins** (co-abundance neighbors): TPM2 (0.96), TGFB1I1 (0.81), EHD2 (0.80); STRING partners: TPM2 (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: huMAP3_06153.1
- **Function (MyGene.info)**: tropomyosin 1. This gene is a member of the tropomyosin family of highly conserved, widely distributed actin-binding proteins involved in the contractile system of striated and smooth muscles and the cytoskeleton of non-muscle cells. Tropomyosin is composed of two alpha-helical chains arranged as a coiled-coil. It is polymerized end to end along the two grooves of actin filaments and provides stability to the fi…
- **Diseases (Open Targets)**: hypertrophic cardiomyopathy (0.798); left ventricular noncompaction (0.760); left ventricular noncompaction 9 (0.664); familial isolated dilated cardiomyopathy (0.639); hypertrophic cardiomyopathy 3 (0.596)
- **Europe PMC papers**: 6278
- **Why important**: TPM1 is one member of the tightly connected TPM1–TPM2 pair and has a prominent network position relative to the smaller module. It appears in every primary term (7 globally significant GO/KEGG terms, q_global 0.0194–0.0391; see the table) and in numerous STRING annotations, including sarcomere, muscle thin filament, actin filament, and connective tissue (10 supplementary STRING terms; within-query FDR 0.0081–0.0459). HPA reports heart- and skeletal-muscle tissue enhancement, actin-filament localization, smooth-muscle-associated cell-type enhancement, and protein detection in both tissues. Its established function is stabilization of actin filaments and regulation of muscle contraction. Its disease associations include cardiomyopathies and other cardiac structural disorders.
- **Conclusion**: Established evidence supports TPM1 as a core structural effector of the contractile arm of the module. Its co-abundance with TPM2 is consistent with shared thin-filament biology; the specific role of this pair in coordinating myometrium and rectum is still inferential.

#### TPM2

- **Related proteins** (co-abundance neighbors): TPM1 (0.96), CKB (0.87), TGFB1I1 (0.84); STRING partners: TPM1 (0.993)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: huMAP3_06153.1
- **Function (MyGene.info)**: tropomyosin 2. This gene encodes beta-tropomyosin, a member of the actin filament binding protein family, and mainly expressed in slow, type 1 muscle fibers. Mutations in this gene can alter the expression of other sarcomeric tropomyosin proteins, and cause cap disease, nemaline myopathy and distal arthrogryposis syndromes. Alternatively spliced transcript variants encoding different isoforms have been found for…
- **Diseases (Open Targets)**: congenital myopathy 23 (0.809); digitotalar dysmorphism (0.739); cap myopathy (0.710); nemaline myopathy (0.681); Sheldon-hall syndrome (0.620)
- **Europe PMC papers**: 3621
- **Why important**: TPM2 forms the strongest direct STRING pair in the module with TPM1 and belongs to the same hu.MAP tropomyosin complex (hu.MAP huMAP3_06153.1). It contributes to the primary cytoskeleton, sarcomere, supramolecular fiber, myofibril, and contractile-fiber terms (6 globally significant GO/KEGG terms, q_global 0.0194–0.0391; see the table), as well as supportive connective-tissue, sarcomere, thin-filament, and actin annotations (9 supplementary STRING terms; within-query FDR 0.0081–0.0459). HPA reports skeletal-muscle and smooth-muscle-associated enrichment and detection in both tissues. Its established function is beta-tropomyosin-mediated actin regulation and muscle contraction. Its disease associations include congenital and distal myopathies.
- **Conclusion**: Established evidence supports TPM2 as a core thin-filament component that reinforces the contractile interpretation. The module supports a coordinated TPM1–TPM2 program, but it does not by itself establish altered contractile force or a disease mechanism in either tissue.

#### FERMT2

- **Related proteins** (co-abundance neighbors): ILK (0.87); STRING partners: ILK (0.997), PARVA (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Focal adhesion sites; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FERM domain containing kindlin 2. Enables several functions, including actin binding activity; phosphatidylinositol-3,4,5-trisphosphate binding activity; and type I transforming growth factor beta receptor binding activity. Involved in several processes, including cell surface receptor signaling pathway; positive regulation of cell differentiation; and positive regulation of cellular component biogenesis. Acts upstream of or withi…
- **Diseases (Open Targets)**: open-angle glaucoma (0.501); prostate carcinoma (0.488); glaucoma (0.488); neurodegenerative disease (0.473); primary angle-closure glaucoma (0.407)
- **Europe PMC papers**: 1336
- **Why important**: FERMT2 is directly linked to ILK in STRING and is also connected to PARVA, creating the principal kindlin–ILK–parvin adhesion axis. It participates in the primary cytoskeleton, sarcomere, supramolecular polymer and fiber, myofibril, and contractile-fiber terms (6 globally significant GO/KEGG terms, q_global 0.0194–0.0391; see the table), and in many supportive STRING categories (9 supplementary STRING terms; within-query FDR 0.0081–0.0455). HPA places it at focal adhesions, detects it in both tissues, and reports smooth-muscle cell enhancement. Its annotations support integrin-mediated signaling, cell-matrix adhesion, actin binding, and transforming-growth-factor receptor interaction. Its literature volume is more moderate than that of ILK or the tropomyosins, which makes its placement in this conserved module especially informative.
- **Conclusion**: Established evidence supports FERMT2 as an adhesion-side structural and signaling component of the contractile module. It is a plausible mediator of force transmission between matrix-linked integrins and the actin apparatus, although that mechanistic link in these tissues remains a hypothesis.

#### DPYSL2

- **Related proteins** (co-abundance neighbors): ILK (0.81); STRING partners: DPYSL3 (0.976)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Microtubules, Cytosol; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_00051.1, huMAP3_11599.1, huMAP3_11626.1
- **Function (MyGene.info)**: dihydropyrimidinase like 2. This gene encodes a member of the collapsin response mediator protein family. Collapsin response mediator proteins form homo- and hetero-tetramers and facilitate neuron guidance, growth and polarity. The encoded protein promotes microtubule assembly and is required for Sema3A-mediated growth cone collapse, and also plays a role in synaptic signaling through interactions with calcium channels. This…
- **Diseases (Open Targets)**: hypertensive disorder (0.431); autosomal dominant non-syndromic intellectual disability (0.370); cardiovascular disorder (0.297); ovarian neoplasm (0.292); glomerulonephritis (0.269)
- **Europe PMC papers**: 1328
- **Why important**: DPYSL2 forms a high-confidence STRING pair with DPYSL3 and appears with DPYSL3 in multiple hu.MAP complexes (hu.MAP huMAP3_00051.1) (hu.MAP huMAP3_11599.1) (hu.MAP huMAP3_11626.1). It contributes to cytoskeleton organization and supramolecular polymer or fiber annotations (GO:BP cytoskeleton organization; q_global = 0.0194) (GO:CC supramolecular polymer; q_global = 0.0265) (GO:CC supramolecular fiber; q_global = 0.0265), with supportive STRING evidence for cytoskeleton, cell projection, and actin-related compartments (4 supplementary STRING terms; within-query FDR 0.0081–0.0301). HPA reports brain tissue enhancement, multiple neuronal cell-type annotations, and several myeloid annotations, while protein detection is reported in rectum. Its established CRMP-family functions include microtubule assembly, neuron guidance, polarity, endocytosis, and cytoskeletal signaling. Its literature and disease associations are substantial but more neurobiology-centered than the contractile genes.
- **Conclusion**: Established evidence supports DPYSL2 as a cytoskeletal-remodeling component and as part of a known DPYSL2–DPYSL3 complex. In this module, its association with ILK and contractile genes may indicate broader cytoskeletal coordination or shared cell composition, but a direct smooth-muscle contractile function is only a hypothesis.

## Module 3

**Tissue pair**: myometrium and rectum  
**Genes (7)**: ERO1A, PSMC2, PSMD13, RARS1, CCT3, CCT7, CCT8

### Function

The strongest interpretation is a conserved cellular proteostasis module centered on the chaperonin-containing TCP-1 complex. The central evidence is the enrichment of intracellular protein-containing complex and chaperonin-containing T-complex terms (GO:CC intracellular protein-containing complex; q_global = 0.00143) (GO:CC chaperonin-containing T-complex; q_global = 0.00179), together with the CCT-related localization and protein-folding terms (GO:BP protein localization to nuclear body; q_global = 0.00179) through (GO:BP protein localization to nucleoplasm; q_global = 0.00179), (GO:CC protein folding chaperone complex; q_global = 0.02), and (GO:MF ATP-dependent protein folding chaperone; q_global = 0.0338). CCT3, CCT7, and CCT8 form the coherent functional core. Their established role is ATP-dependent folding of newly synthesized proteins, including actin and tubulin, and the STRING annotations independently support CCT/TriC structure, conserved chaperonin domains, and folding of actin and tubulin (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 0.00084) through (STRING InterPro GroEL-like equatorial domain superfamily; within-query FDR = 0.0042), (STRING NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis; within-query FDR = 0.0073) through (STRING RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding; within-query FDR = 0.0105). RARS1 connects the module to aminoacylation and translation, while PSMC2 and PSMD13 connect it to ubiquitin-dependent proteasomal protein turnover. The telomere, Cajal-body, sperm-recognition, and fertilization terms (GO:BP regulation of telomerase RNA localization to Cajal body; q_global = 0.00179) through (GO:BP positive regulation of telomere maintenance; q_global = 0.02) and (GO:BP single fertilization; q_global = 0.0338) are statistically supported annotations, but they are driven mainly by the shared CCT trio and should not be interpreted as evidence that this myometrium-rectum module specifically performs reproductive or telomere functions. Overall, the module most plausibly represents coordinated synthesis, folding, quality control, and disposal of proteins.

**Cell composition.** This is not primarily a plasma-protein, secreted-protein, or blood-cell module. The HPA summary identifies only one secreted annotation, while all genes have low immune-cell specificity and no enriched blood-cell population is reported. Most genes have low tissue specificity, which is consistent with broadly expressed housekeeping or core cellular machinery rather than a specialized myometrium or rectum program. The HPA protein observations support presence in both tissues for CCT3, CCT7, and PSMC2, with additional detection in rectum for CCT8, RARS1, and PSMD13. ERO1A is tissue enhanced in esophagus and cell-type enriched in esophageal apical cells, is not detected by IHC in either target tissue, and is therefore less persuasive as a defining tissue-shared component. The cell-type annotations for CCT8, CCT7, PSMC2, and PSMD13 include oocytes, spermatogenic cells, or syncytiotrophoblasts, but the low immune specificity and lack of a blood-cell enrichment argue against a simple blood contamination explanation.

**GO/KEGG enrichment**: 33 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC intracellular protein-containing complex | 0.00143 | CCT3, CCT7, CCT8, PSMC2, PSMD13, RARS1 |
| GO:CC chaperonin-containing T-complex | 0.00179 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 0.00179 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 0.00179 | CCT3, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 0.00179 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 0.00179 | CCT3, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 0.00179 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 0.00179 | CCT3, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 0.00179 | CCT3, CCT7, CCT8 |
| GO:BP binding of sperm to zona pellucida | 0.00372 | CCT3, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.00372 | CCT3, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 0.00372 | CCT3, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 0.00372 | CCT3, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 0.00372 | CCT3, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 0.00372 | CCT3, CCT7, CCT8 |

### STRING and hu.MAP

STRING provides very strong, expected physical or functional support for the CCT core: CCT3, CCT7, and CCT8 are mutually connected with near-maximal confidence, and CCT8 connects to PSMC2. PSMC2 and PSMD13 are also linked with very strong confidence, matching their shared proteasome assignment. The STRING enrichment results (STRING Pfam TCP-1/cpn60 chaperonin family; within-query FDR = 0.00084) through (STRING InterPro GroEL-like equatorial domain superfamily; within-query FDR = 0.0042) and (STRING NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis; within-query FDR = 0.0073) through (STRING RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding; within-query FDR = 0.0105) reinforce the CCT chaperonin and folding interpretation, but they are supplementary rather than globally corrected module-level evidence. hu.MAP independently places CCT3, CCT7, and CCT8 together in several complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1), while PSMC2 and PSMD13 occur together in proteasome complexes (hu.MAP huMAP3_05064.1) through (hu.MAP huMAP3_13725.1). Thus, the dense CCT relationships and the proteasome pair are already known molecular relationships. The remaining co-abundance links, especially those involving RARS1 and ERO1A, are not supported by recorded STRING partners or hu.MAP complexes in this fact sheet and should be treated as expression-level associations rather than demonstrated physical interactions.

**STRING interactions (score >= 0.7)**: 5 of 21 gene pairs: CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT7–CCT8 (0.999); CCT8–PSMC2 (0.733); PSMC2–PSMD13 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: Pfam TCP-1/cpn60 chaperonin family (FDR = 0.00084, 3 genes); Component Chaperonin-containing T-complex (FDR = 0.0032, 3 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 0.0033, 3 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 0.0042, 3 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 0.0042, 3 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 0.0042, 3 genes); InterPro GroEL-like apical domain superfamily (FDR = 0.0042, 3 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 0.0042, 3 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 0.0042, 3 genes); TISSUES Lymphoblast (FDR = 0.0046, 5 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 0.0073, 3 genes); RCTM Folding of actin by CCT/TriC (FDR = 0.0081, 3 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 0.0081, 3 genes); RCTM Formation of tubulin folding intermediates by CCT/TriC (FDR = 0.0105, 3 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 0.0105, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT3, CCT8, CCT7; 3/23); huMAP3_06559.1 (CCT3, CCT8, CCT7; 3/25); huMAP3_09191.1 (CCT3, CCT8, CCT7; 3/32); huMAP3_10656.1 (CCT3, CCT8, CCT7; 3/36); huMAP3_14584.1 (CCT3, CCT8, CCT7; 3/61); huMAP3_01951.1 (CCT3, CCT7; 2/8); huMAP3_05064.1 (PSMC2, PSMD13; 2/31); huMAP3_09656.1 (PSMC2, PSMD13; 2/64); huMAP3_13725.1 (PSMC2, PSMD13; 2/69)

### Novelty

The module should not be claimed as a newly discovered molecular complex. Its core consists of well-established CCT subunits, and its proteasome pair belongs to well-characterized proteasome machinery, with extensive STRING and hu.MAP support. What may be novel is the conserved co-abundance pattern across myometrium and rectum, particularly the way the CCT core is coordinated with RARS1, ERO1A, PSMC2, and PSMD13 in these tissue groups. That is a tissue-comparison or systems-level observation, not evidence of a new biochemical interaction. The absence of some module pairs from STRING or hu.MAP cannot establish novelty, because those resources emphasize curated or experimentally supported relationships and do not test every tissue-specific co-abundance association. Independent replication, comparison with other tissue pairs, and validation at the protein or perturbation level would be required to establish a genuinely new tissue-shared mechanism.

**Hypothesis.** Hypothesis: the shared module reflects a general proteostasis program operating in cells present in both myometrium and rectum. CCT3, CCT7, and CCT8 may provide the folding capacity for newly synthesized structural and regulatory proteins; RARS1 may mark the coupled translation supply; and PSMC2 with PSMD13 may provide downstream removal of damaged or surplus proteins. ERO1A could indicate an endoplasmic-reticulum or redox-related folding contribution, but its tissue and cell-type annotations make that connection uncertain in these samples. Under this model, the co-abundance pattern represents coordinated protein production, folding, and quality control rather than a specialized reproductive, telomere, or blood-cell program. This remains a hypothesis because co-abundance does not demonstrate physical binding, causal regulation, or cell-specific activity.

### Important genes

#### CCT8

- **Related proteins** (co-abundance neighbors): RARS1 (0.87), CCT3 (0.82), PSMD13 (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), PSMC2 (0.733)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Connecting piece, End piece; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 8. This gene encodes the theta subunit of the CCT chaperonin, which is abundant in the eukaryotic cytosol and may be involved in the transport and assembly of newly synthesized proteins. Alternative splicing results in multiple transcript variants of this gene. A pseudogene related to this gene is located on chromosome 1. [provided by RefSeq, Sep 2013].
- **Diseases (Open Targets)**: colorectal carcinoma (0.094); neoplasm (0.093); hepatocellular carcinoma (0.090); lung adenocarcinoma (0.087); cancer (0.083)
- **Europe PMC papers**: 1127
- **Why important**: CCT8 is the most connected module gene and links the CCT core to RARS1 and the proteasome-associated PSMC2 branch. It participates in every globally enriched term (GO:CC intracellular protein-containing complex; q_global = 0.00143) through (GO:CC zona pellucida receptor complex; q_global = 0.0462), is present in several hu.MAP CCT-related complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_14584.1), and has strong STRING links to CCT3, CCT7, and PSMC2. Its extensive literature and disease-association record make it a well-supported marker of the module's central chaperonin biology.
- **Conclusion**: Established: CCT8 is a core CCT chaperonin subunit involved in ATP-dependent protein folding and protein stabilization. Established: its network position supports a bridging role between chaperonin activity and proteostasis-associated expression. Hypothesis: CCT8 may be a useful sentinel of the shared tissue proteostasis state, but the data do not show that it drives the module.

#### CCT3

- **Related proteins** (co-abundance neighbors): CCT7 (0.86), CCT8 (0.82); STRING partners: CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a core member of the CCT chaperonin complex, has strong links to CCT7 and CCT8, and participates in all globally enriched terms reported for the module. It is detected in both myometrium and rectum and appears in multiple hu.MAP complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1). Its substantial literature volume and annotations for folding actin and tubulin support the interpretation that the module contains a genuine chaperone core rather than a coincidental gene grouping.
- **Conclusion**: Established: CCT3 is a broadly expressed molecular chaperone subunit with direct support for protein-folding function. Established: its bilateral tissue detection and core network placement are consistent with a conserved cellular machinery signal. Hypothesis: variation in CCT3 abundance could reflect changes in folding demand, although causality is not established.

#### CCT7

- **Related proteins** (co-abundance neighbors): CCT3 (0.86), ERO1A (0.82); STRING partners: CCT3 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 7. This gene encodes a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including act…
- **Diseases (Open Targets)**: myocardial infarction (0.334); preeclampsia (0.177); neurodegenerative disease (0.117); intelligence (0.083); hepatocellular carcinoma (0.083)
- **Europe PMC papers**: 907
- **Why important**: CCT7 is part of the densely connected CCT trio, is linked to CCT3 and CCT8 in STRING, and occurs in numerous hu.MAP complexes (hu.MAP huMAP3_07938.1) through (hu.MAP huMAP3_01951.1). It contributes to the globally enriched CCT, protein-folding, localization, telomere-related, and chromosome-organization annotations (GO:CC intracellular protein-containing complex; q_global = 0.00143) through (GO:BP regulation of chromosome organization; q_global = 0.0421). Its detection in both target tissues and substantial literature support make it an important representative of the shared core.
- **Conclusion**: Established: CCT7 is a CCT/TRiC chaperone subunit that supports folding of proteins such as actin and tubulin. Established: it is consistently represented in the module's independent network and complex evidence. Hypothesis: CCT7 abundance may report the demand for cytoskeletal and general protein maturation in shared cells of the two tissues.

#### PSMC2

- **Related proteins** (co-abundance neighbors): RARS1 (0.82); STRING partners: CCT8 (0.733), PSMD13 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Cytoplasmic bodies; IHC detected in myometrium, rectum
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, ATPase 2. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.604); mantle cell lymphoma (0.542); neoplasm (0.531); HIV infectious disease (0.476); amyloidosis (0.472)
- **Europe PMC papers**: 1007
- **Why important**: PSMC2 provides the clearest proteasome-side component of the module. It connects to CCT8 in STRING and to PSMD13 with strong confidence, while hu.MAP places it with PSMD13 in multiple proteasome complexes (hu.MAP huMAP3_05064.1) through (hu.MAP huMAP3_13725.1). Its annotations support ATP-dependent proteasomal protein catabolism and oxidative-stress responses, giving the module a quality-control and degradation arm beyond protein folding.
- **Conclusion**: Established: PSMC2 is a proteasome regulatory ATPase involved in ubiquitin-dependent protein degradation. Established: its relationship with PSMD13 is supported by both STRING and hu.MAP, whereas its link to CCT8 is supported by STRING and co-abundance. Hypothesis: PSMC2 may connect folding demand with selective removal of proteins that fail maturation, but direct coordination with CCT has not been demonstrated here.

#### PSMD13

- **Related proteins** (co-abundance neighbors): CCT8 (0.82); STRING partners: PSMC2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear speckles; IHC detected in rectum
- **hu.MAP 3.0**: huMAP3_05064.1, huMAP3_09656.1, huMAP3_13725.1
- **Function (MyGene.info)**: proteasome 26S subunit, non-ATPase 13. The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, …
- **Diseases (Open Targets)**: plasma cell myeloma (0.605); mantle cell lymphoma (0.542); neurodegenerative disease (0.521); neoplasm (0.521); HIV infectious disease (0.476)
- **Europe PMC papers**: 647
- **Why important**: PSMD13 complements PSMC2 as the proteasome-associated non-ATPase component. It has a strong STRING relationship with PSMC2, shares several hu.MAP proteasome complexes (hu.MAP huMAP3_05064.1) through (hu.MAP huMAP3_13725.1), and contributes to the intracellular protein-containing-complex term (GO:CC intracellular protein-containing complex; q_global = 0.00143). Its nuclear-speckle localization and annotations for proteasomal and oxidative-stress responses make it relevant to the module's protein-quality-control interpretation.
- **Conclusion**: Established: PSMD13 is part of the proteasome regulatory machinery and participates in ubiquitin-dependent protein catabolism. Established: its strongest known relationship in this module is with PSMC2. Hypothesis: PSMD13 may represent the degradation and nuclear quality-control side of the shared proteostasis state, but the co-abundance data do not establish a tissue-specific function.
