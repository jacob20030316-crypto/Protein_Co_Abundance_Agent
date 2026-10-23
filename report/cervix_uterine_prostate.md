# Conserved co-abundance modules: cervix_uterine and prostate

## Module 0

**Tissue pair**: cervix_uterine and prostate  
**Genes (49)**: PPP2R5D, ACADVL, ADK, ADPGK, AIMP1, ANXA1, ASPH, ATP1A1, ATXN10, CANX, CDC73, CS, CPSF3, COPS3, DFFA, ERO1A, FLII, GAPVD1, GNL1, HEXA, IDH3A, METAP1, METAP2, MAT2B, MBOAT7, MSH2, MYOF, NDUFS4, NCSTN, NSDHL, NUP155, DDOST, PDCD6IP, PLOD2, PFAS, CAD, RAB3GAP2, SUPT5H, STK39, STXBP1, ACAT2, THOC3, THUMPD1, TSG101, TSPO, UBA3, UGDH, UMPS, VPS45

### Function

No GO/KEGG term passed global correction, and STRING functional enrichment was absent. Therefore, the module does not support a single statistically established pathway-level annotation. Its genes instead suggest a heterogeneous cellular maintenance program spanning RNA processing and export, nuclear transport, protein maturation and endoplasmic-reticulum quality control, vesicle trafficking, central carbon and nucleotide metabolism, lipid and sterol metabolism, mitochondrial energy metabolism, and membrane or cytoskeletal organization. The co-abundance structure may therefore reflect coordinated general cellular activity rather than one specialized biochemical pathway. The strongest biological themes are supported by individual gene functions and by coherent subnetworks, not by enriched GO/KEGG terms.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a minority of secreted genes, while most genes have low tissue specificity and low immune-cell specificity. The module is consequently more consistent with broadly expressed intracellular and membrane-associated proteins than with a blood-contamination signature. Nevertheless, HPA single-cell annotations show repeated associations with esophageal apical cells, spermatids, trophoblasts and neutrophils, with additional epithelial, stromal, muscle and monocyte signals. These patterns indicate that shared cellular composition or common epithelial, germline, secretory, or stress-related states could contribute to the cervix-and-prostate co-abundance relationship. Protein detection is broadly supported in both tissues, although selected genes are not detected in one or both tissues by IHC, so RNA co-abundance should not be interpreted as uniform protein expression.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING network provides a limited but informative set of established relationships. Known metabolic links include ACAT2 with CS, CS with IDH3A, CAD with UMPS, and MAT2B or NSDHL with UGDH. Known processing and quality-control links include CANX with DDOST, ERO1A and NCSTN. METAP1 is linked to METAP2. The strongest organizational anchors are TSG101 with PDCD6IP and CDC73 with SUPT5H. hu.MAP independently places PDCD6IP and TSG101 together across multiple ESCRT or endosomal-complex models, places CDC73 and SUPT5H together across transcription-elongation and RNA-polymerase-associated models, and places UGDH with UMPS in a metabolic complex model. Additional hu.MAP support connects STXBP1 with VPS45 and MBOAT7 with MYOF. These overlaps show that parts of the module recapitulate known molecular systems. However, most co-abundance edges are not represented by STRING or hu.MAP, so the module is a tissue-level expression relationship rather than evidence that all module genes form one physical complex.

**STRING interactions (score >= 0.7)**: 12 of 1176 gene pairs: ACAT2–CS (0.966); CAD–UMPS (0.946); CANX–DDOST (0.886); CANX–ERO1A (0.726); CANX–NCSTN (0.754); CANX–TSG101 (0.845); CDC73–SUPT5H (0.999); CS–IDH3A (0.925); MAT2B–UGDH (0.74); METAP1–METAP2 (0.991); NSDHL–UGDH (0.712); PDCD6IP–TSG101 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_01514.1 (PDCD6IP, TSG101; 2/5); huMAP3_06010.1 (PDCD6IP, TSG101; 2/7); huMAP3_07951.1 (PDCD6IP, TSG101; 2/8); huMAP3_07948.1 (SUPT5H, CDC73; 2/9); huMAP3_12841.1 (UGDH, UMPS; 2/10); huMAP3_09572.1 (PDCD6IP, TSG101; 2/11); huMAP3_08679.1 (PDCD6IP, TSG101; 2/12); huMAP3_12917.1 (PDCD6IP, TSG101; 2/13); huMAP3_10053.1 (PDCD6IP, TSG101; 2/14); huMAP3_11018.1 (SUPT5H, CDC73; 2/15); huMAP3_12111.1 (SUPT5H, CDC73; 2/16); huMAP3_09042.1 (UMPS, ATXN10; 2/26); huMAP3_07454.1 (SUPT5H, CDC73; 2/27); huMAP3_07749.1 (SUPT5H, CDC73; 2/28); huMAP3_09843.1 (SUPT5H, CDC73; 2/29); huMAP3_13805.1 (PDCD6IP, TSG101; 2/30); huMAP3_13160.1 (STXBP1, VPS45; 2/49); huMAP3_10725.1 (MBOAT7, MYOF; 2/59); huMAP3_11092.1 (SUPT5H, CDC73; 2/65)

### Novelty

The module should not be claimed as a wholly new molecular complex or as a newly discovered pathway. Several of its internal relationships and subnetworks are already established by STRING and hu.MAP, especially ESCRT-related trafficking, transcription elongation, pyrimidine metabolism, and selected metabolic or endoplasmic-reticulum relationships. A potentially novel aspect is the cross-tissue co-abundance configuration linking these otherwise distinct systems in cervix_uterine and prostate. That configuration may be a new observation, but novelty requires replication, comparison with published tissue co-expression resources, and testing against cell-composition and technical covariates. The absence of a relationship from STRING or hu.MAP would not by itself establish novelty.

**Hypothesis.** Hypothesis: the shared module reflects a conserved epithelial or reproductive-tissue cellular state in which biosynthetic demand and membrane traffic are coordinated with RNA maturation, protein folding, vesicle sorting, lipid remodeling, and energy metabolism. In this model, transcription and RNA-processing components support increased biosynthetic activity; CANX, DDOST and ERO1A support folding and secretory quality control; TSG101 and PDCD6IP support endosomal sorting and membrane remodeling; and UGDH, UMPS, CS, IDH3A, ACAT2 and related enzymes supply nucleotide, glycan, lipid and mitochondrial metabolic capacity. The HPA cell-type pattern also permits an alternative explanation in which shared epithelial, germline, or low-level immune-cell composition generates much of the signal. This hypothesis should be tested with cell-resolved data, matched tissue histology, independent cohorts, and perturbation of the proposed trafficking or biosynthetic anchors.

### Important genes

#### NUP155

- **Related proteins** (co-abundance neighbors): RAB3GAP2 (0.90), CPSF3 (0.89), NSDHL (0.88), ATXN10 (0.86), DDOST (0.85), ERO1A (0.85), UMPS (0.85), PLOD2 (0.84), MSH2 (0.83), PFAS (0.83), CDC73 (0.81), VPS45 (0.81), GNL1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 155. Nucleoporins are proteins that play an important role in the assembly and functioning of the nuclear pore complex (NPC) which regulates the movement of macromolecules across the nuclear envelope (NE). The protein encoded by this gene plays a role in the fusion of NE vesicles and formation of the double membrane NE. The protein may also be involved in cardiac physiology and may be associated with t…
- **Diseases (Open Targets)**: HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.526); atrial fibrillation (0.470); familial atrial fibrillation (0.390)
- **Europe PMC papers**: 944
- **Why important**: NUP155 is the highest-positioned network gene in the supplied ranking and connects nuclear-envelope organization with multiple module neighborhoods, including RNA-processing, metabolism and endoplasmic-reticulum-associated genes. Its annotation supports nuclear pore function, RNA export, nucleocytoplasmic transport and nuclear-envelope organization. It has substantial literature and disease associations including familial atrial fibrillation, making it a strong structural integrator even though it has no STRING partner or hu.MAP complex listed here.
- **Conclusion**: Established evidence supports NUP155 as a nuclear-pore and nuclear-envelope gene with a central co-abundance position. It is reasonable to regard it as a module organizer, but it is not established that NUP155 mechanistically coordinates the other module systems; that interpretation remains a hypothesis.

#### TSG101

- **Related proteins** (co-abundance neighbors): CAD (0.83), CPSF3 (0.82), ANXA1 (0.81), NSDHL (0.81), ADPGK (0.81); STRING partners: CANX (0.845), PDCD6IP (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_01514.1, huMAP3_06010.1, huMAP3_07951.1, huMAP3_09572.1, huMAP3_08679.1, huMAP3_12917.1, huMAP3_10053.1, huMAP3_13805.1
- **Function (MyGene.info)**: tumor susceptibility 101. The protein encoded by this gene belongs to a group of apparently inactive homologs of ubiquitin-conjugating enzymes. The gene product contains a coiled-coil domain that interacts with stathmin, a cytosolic phosphoprotein implicated in tumorigenesis. The protein may play a role in cell growth and differentiation and act as a negative growth regulator. In vitro steady-state expression of this tumor…
- **Diseases (Open Targets)**: HIV infectious disease (0.528); viral infectious disease (0.467); dengue disease (0.370); neurodegenerative disease (0.337); Alkalosis (0.144)
- **Europe PMC papers**: 14220
- **Why important**: TSG101 is a central module member with a well-supported physical relationship to PDCD6IP in STRING and repeated membership with PDCD6IP in hu.MAP endosomal and ESCRT-related complex models (hu.MAP huMAP3_01514.1), (hu.MAP huMAP3_06010.1), (hu.MAP huMAP3_07951.1), (hu.MAP huMAP3_09572.1), (hu.MAP huMAP3_08679.1), (hu.MAP huMAP3_12917.1), (hu.MAP huMAP3_10053.1) and (hu.MAP huMAP3_13805.1). Its annotation supports vesicle-mediated transport, extracellular transport and macroautophagy. It also connects in the module to genes involved in RNA processing, lipid metabolism and glycolysis, and it has a particularly large literature base.
- **Conclusion**: Established evidence identifies TSG101 as the clearest endosomal-trafficking anchor of the module. Its co-abundance with metabolic and RNA-processing genes may indicate coordinated cellular demand or cell-state regulation, but a direct functional bridge among all of those processes is not established.

#### CPSF3

- **Related proteins** (co-abundance neighbors): NUP155 (0.89), UMPS (0.85), ATXN10 (0.85), METAP1 (0.84), AIMP1 (0.83), TSG101 (0.82), FLII (0.81), MAT2B (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cleavage and polyadenylation specific factor 3. This gene encodes a member of the metallo-beta-lactamase family. The encoded protein is a 73kDa subunit of the cleavage and polyadenylation specificity factor and functions as an endonuclease that recognizes the pre-mRNA 3'-cleavage site AAUAAA prior to polyadenylation. It also cleaves after the pre-mRNA sequence ACCCA during histone 3'-end pre-mRNA processing. [provided by RefSeq, Oct 2012].
- **Diseases (Open Targets)**: neurodevelopmental disorder with microcephaly, hypotonia, nystagmus, and seizures (0.601); neurodegenerative disease (0.527); neurodevelopmental disorder with hypotonia, microcephaly, and seizures (0.416); complex neurodevelopmental disorder (0.370); dengue disease (0.370)
- **Europe PMC papers**: 548
- **Why important**: CPSF3 has a relatively strong network position and links NUP155 with UMPS, ATXN10, METAP1, AIMP1, TSG101 and other module genes. It is the catalytic endonuclease component of the cleavage and polyadenylation specificity factor and participates in messenger-RNA three-prime-end processing and histone messenger-RNA processing. Its presence in both cervix and prostate by IHC supports tissue relevance, while its disease and developmental literature provides substantial external context.
- **Conclusion**: Established evidence supports CPSF3 as an RNA-maturation anchor that could explain co-abundance with nuclear transport and biosynthetic genes. The data do not establish altered polyadenylation or a specific transcriptional program in either tissue, so that extension is a hypothesis.

#### UGDH

- **Related proteins** (co-abundance neighbors): PLOD2 (0.86), DDOST (0.85), ACAT2 (0.83), PFAS (0.80); STRING partners: MAT2B (0.74), NSDHL (0.712)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_12841.1
- **Function (MyGene.info)**: UDP-glucose 6-dehydrogenase. The protein encoded by this gene converts UDP-glucose to UDP-glucuronate and thereby participates in the biosynthesis of glycosaminoglycans such as hyaluronan, chondroitin sulfate, and heparan sulfate. These glycosylated compounds are common components of the extracellular matrix and likely play roles in signal transduction, cell migration, and cancer growth and metastasis. The expression of this …
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 84 (0.784); Epileptic encephalopathy (0.491); hereditary disease (0.413); neurodegenerative disease (0.344); hemorrhoid (0.288)
- **Europe PMC papers**: 1718
- **Why important**: UGDH connects the module’s metabolic and extracellular-matrix-related signals. It converts UDP-glucose to UDP-glucuronate and supports glycosaminoglycan, hyaluronan, chondroitin-sulfate and heparan-sulfate biosynthesis. It has STRING relationships with MAT2B and NSDHL and is represented with UMPS in a hu.MAP complex model (hu.MAP huMAP3_12841.1). Its tissue-enhanced liver annotation and cell-type associations with epithelial and absorptive cells are compatible with a biosynthetic or matrix-related state, although they do not define the cervix or prostate mechanism.
- **Conclusion**: Established evidence supports UGDH as a glycan-precursor and extracellular-matrix metabolism anchor. It may connect intracellular biosynthetic demand to tissue remodeling, but a specific matrix-remodeling role in this shared module requires direct tissue and functional validation.

#### CDC73

- **Related proteins** (co-abundance neighbors): NUP155 (0.81), SUPT5H (0.80); STRING partners: SUPT5H (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_07948.1, huMAP3_11018.1, huMAP3_12111.1, huMAP3_07454.1, huMAP3_07749.1, huMAP3_09843.1, huMAP3_11092.1
- **Function (MyGene.info)**: cell division cycle 73. This gene encodes a tumor suppressor that is involved in transcriptional and post-transcriptional control pathways. The protein is a component of the the PAF protein complex, which associates with the RNA polymerase II subunit POLR2A and with a histone methyltransferase complex. This protein appears to facilitate the association of 3' mRNA processing factors with actively-transcribed chromatin. Mu…
- **Diseases (Open Targets)**: hyperparathyroidism 2 with jaw tumors (0.810); parathyroid gland carcinoma (0.802); familial isolated hyperparathyroidism (0.738); hyperparathyroidism (0.599); hereditary neoplastic syndrome (0.555)
- **Europe PMC papers**: 2210
- **Why important**: CDC73 forms one of the clearest known interaction pairs in the module through its STRING relationship with SUPT5H and its repeated hu.MAP placement with SUPT5H in transcription-elongation, PAF and RNA-polymerase-associated complexes (hu.MAP huMAP3_07948.1), (hu.MAP huMAP3_11018.1), (hu.MAP huMAP3_12111.1), (hu.MAP huMAP3_07454.1), (hu.MAP huMAP3_07749.1), (hu.MAP huMAP3_09843.1) and (hu.MAP huMAP3_11092.1). Its annotation supports transcriptional and post-transcriptional control, RNA-polymerase-II elongation and tumor suppression. Its established associations with hyperparathyroidism and jaw-tumor syndrome provide important disease relevance, despite lower tissue-specific protein detection in prostate.
- **Conclusion**: Established evidence supports CDC73 as a transcriptional-control and RNA-polymerase-associated anchor. Its co-abundance with NUP155 and CPSF3 is consistent with coordinated gene-expression regulation, but the module does not demonstrate that CDC73 drives the shared cervix-and-prostate state.

## Module 1

**Tissue pair**: cervix_uterine and prostate  
**Genes (36)**: PPP2R2A, ACSL1, FDXR, BPNT1, CDK5RAP3, CNDP2, CPNE3, CPT2, DHRS1, DHRS7, ENDOD1, GFUS, SHMT1, GCA, H1-10, IMPA1, LYPLAL1, MYO6, NDUFA9, NT5DC1, DBT, PPL, PGM2, PKP3, RAD50, RRBP1, RTCA, SEPTIN8, SPTBN2, SUCLG2, TOM1, TRIM56, SLC25A1, UACA, UTRN, WDR11

### Function

The module does not have a single statistically established GO or KEGG function: no GO or KEGG term passed global correction. Its structure instead suggests a mixed cellular program centered on epithelial junction and cytoskeletal organization, intracellular trafficking, and metabolic support. PKP3 and PPL support desmosomal and epithelial structural biology; SPTBN2 and UTRN support membrane–cytoskeleton organization; MYO6 and TOM1 support vesicle and endosomal trafficking; and several module genes support mitochondrial energy, lipid, amino-acid, and nucleotide metabolism. The co-abundance pattern therefore appears more consistent with a shared cellular-state or tissue-composition signal than with a narrowly defined pathway. The interpretation remains inferential because there are no globally significant GO or KEGG terms and no supplementary STRING enrichment.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins: the HPA summary identifies only a single secreted gene, while most genes are intracellular or membrane-associated. It is also not broadly dominated by immune-cell markers, since most genes have low immune-cell specificity. Nevertheless, there are localized composition signals. GCA is associated with neutrophils and eosinophils and is not detected by immunohistochemistry in either tissue; ACSL1 is associated with neutrophils; and several genes show immune-cell-enhanced or immune-cell-group-enriched profiles. A stronger recurring signal is epithelial and barrier-associated biology, especially esophageal apical-cell and related epithelial profiles, together with liver, skeletal-muscle, skin, and reproductive-cell annotations. Protein detection in both tissues is widespread for the module, but this does not establish that every gene is expressed by the same cell type. The shared module could therefore partly reflect common epithelial or stromal cell states, with a possible minor blood-cell contribution rather than a plasma-protein signature.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING evidence is sparse but includes DBT with SUCLG2, MYO6 with TOM1, and PKP3 with PPL. These relationships are biologically coherent with mitochondrial or metabolic organization, endosomal trafficking, and epithelial junction structure, respectively, but they do not cover most module edges. hu.MAP provides additional support for recurring protein-complex relationships. BPNT1, FDXR, and CPT2 occur together in C1, SLC25A1 and SUCLG2 occur together in C2, PKP3 and PPL recur across several epithelial or junction-related complexes, and SPTBN2 with TOM1 recurs in cytoskeletal or membrane-associated complexes. These observations indicate that parts of the module overlap known molecular machinery, while the overall co-abundance network is broader and more heterogeneous than the experimentally supported interaction or complex relationships. Co-abundance edges without STRING or hu.MAP support should not be treated as physical interactions.

**STRING interactions (score >= 0.7)**: 3 of 630 gene pairs: DBT–SUCLG2 (0.89); MYO6–TOM1 (0.981); PKP3–PPL (0.797)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (BPNT1, FDXR, CPT2; 3/99); huMAP3_11101.1 (SLC25A1, SUCLG2; 2/3); huMAP3_06046.1 (PPL, PKP3; 2/5); huMAP3_07940.1 (SPTBN2, TOM1; 2/5); huMAP3_07972.1 (PPL, PKP3; 2/7); huMAP3_09165.1 (SPTBN2, TOM1; 2/39); huMAP3_09125.1 (PPL, PKP3; 2/53); huMAP3_09929.1 (PPL, PKP3; 2/75)

### Novelty

The module should not be claimed as a wholly new molecular complex or pathway. Several of its relationships and functional components are already represented by STRING or hu.MAP, particularly the PKP3–PPL, MYO6–TOM1, and DBT–SUCLG2 relationships and the complexes containing PKP3, PPL, SPTBN2, TOM1, BPNT1, FDXR, CPT2, SLC25A1, and SUCLG2. The potentially novel aspect is the tissue-pair-specific co-abundance organization linking epithelial junction, membrane trafficking, mitochondrial metabolism, and cell-state markers across cervix uterine and prostate. However, the fact sheet does not establish that this cross-tissue module has never been reported, and absence from interaction resources would not prove novelty. The appropriate conclusion is that the module may represent a novel integrative co-abundance pattern, but this requires independent replication and comparison with prior tissue-network studies.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial tissue state in cervix uterine and prostate in which junctional and membrane-cytoskeletal organization is coordinated with vesicle trafficking and energetic or lipid metabolism. PKP3 and PPL may mark the epithelial adhesion scaffold, SPTBN2 and UTRN may connect that scaffold to the membrane cytoskeleton, MYO6 and TOM1 may support cargo movement and endosomal handling, and CPT2 together with related metabolic genes may provide energy and lipid oxidation capacity. The blood-cell-associated signal around GCA and ACSL1 could represent admixture or inflammatory context rather than the core mechanism. This hypothesis predicts that the module will be strongest in epithelial or glandular cellular fractions and will vary with epithelial integrity, trafficking demand, metabolic state, or local inflammation.

### Important genes

#### PKP3

- **Related proteins** (co-abundance neighbors): MYO6 (0.92), GCA (0.92), WDR11 (0.82); STRING partners: PPL (0.797)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_06046.1, huMAP3_07972.1, huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: plakophilin 3. This gene encodes a member of the arm-repeat (armadillo) and plakophilin gene families. Plakophilin proteins contain numerous armadillo repeats, localize to cell desmosomes and nuclei, and participate in linking cadherins to intermediate filaments in the cytoskeleton. This protein may act in cellular desmosome-dependent adhesion and signaling pathways. Two transcript variants encoding different is…
- **Diseases (Open Targets)**: anorectal malformation (0.295); neurodegenerative disease (0.292); lymphopenia (0.111); neutropenia (0.111); hypertensive disorder (0.106)
- **Europe PMC papers**: 747
- **Why important**: PKP3 is a prominent epithelial-junction candidate with a strong position in the module’s epithelial substructure. HPA places it in cell junctions and links it to cervix, esophageal, colon, and enterocyte profiles, while its annotations support desmosome assembly, desmosome organization, epithelial structure maintenance, and cytokine-related regulation. It also participates in several hu.MAP complexes and has a high-confidence STRING relationship with PPL. Its literature base is substantial, and its disease associations include prostate carcinoma and epithelial or inflammatory phenotypes.
- **Conclusion**: Established evidence supports PKP3 as an epithelial desmosomal and structural marker that anchors a meaningful part of this module. The hypothesis that PKP3 coordinates the broader metabolic and trafficking components is not established by the available interaction evidence and should be tested rather than assumed.

#### PPL

- **Related proteins** (co-abundance neighbors): UACA (0.89), SEPTIN8 (0.82), GFUS (0.81); STRING partners: PKP3 (0.797)
- **HPA**: Tissue enhanced; Cell type enriched; blood Not detected in immune cells; location Plasma membrane, Basal body, Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_06046.1, huMAP3_07972.1, huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: periplakin. The protein encoded by this gene is a component of desmosomes and of the epidermal cornified envelope in keratinocytes. The N-terminal domain of this protein interacts with the plasma membrane and its C-terminus interacts with intermediate filaments. Through its rod domain, this protein forms complexes with envoplakin. This protein may serve as a link between the cornified envelope and desmosomes …
- **Diseases (Open Targets)**: hypertensive disorder (0.495); prostate carcinoma (0.406); seborrheic keratosis (0.367); obesity disorder (0.334); brain cancer (0.332)
- **Europe PMC papers**: 9177
- **Why important**: PPL is a central epithelial structural candidate linked to PKP3 and recurring across multiple hu.MAP complexes. It is tissue enhanced in cervix, esophagus, and vagina, is localized to the plasma membrane and cytosol, and is annotated for intermediate-filament organization, wound healing, and response to mechanical stimulus. Its network position connects the epithelial junction signal to UACA, SEPTIN8, and GFUS, and it has a substantial literature record compared with most genes in the module.
- **Conclusion**: Established evidence supports PPL as a periplakin-based intermediate-filament and desmosomal component that could explain the epithelial and mechanical-stress aspect of the module. Its role as a mechanistic bridge to mitochondrial metabolism remains a hypothesis because direct support for that bridge is not present in STRING or hu.MAP.

#### MYO6

- **Related proteins** (co-abundance neighbors): PKP3 (0.92), LYPLAL1 (0.87), CPT2 (0.87), WDR11 (0.81); STRING partners: TOM1 (0.981)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin VI. This gene encodes a reverse-direction motor protein that moves toward the minus end of actin filaments and plays a role in intracellular vesicle and organelle transport. The protein consists of a motor domain containing an ATP- and an actin-binding site and a globular tail which interacts with other proteins. This protein maintains the structural integrity of inner ear hair cells and mutations in …
- **Diseases (Open Targets)**: progressive sensorineural hearing loss-hypertrophic cardiomyopathy syndrome (0.760); autosomal dominant nonsyndromic hearing loss (0.721); hearing loss, autosomal recessive (0.702); nonsyndromic genetic hearing loss (0.660); hearing loss disorder (0.653)
- **Europe PMC papers**: 2084
- **Why important**: MYO6 links epithelial and membrane biology to intracellular transport. It encodes a reverse-direction actin motor involved in vesicle and organelle transport, endocytosis, actin organization, and intracellular localization. It is connected in the module to PKP3, WDR11, LYPLAL1, and CPT2, and its relationship with TOM1 is strongly supported by STRING. HPA detects it in both tissues and associates it with endometrial glandular and esophageal apical cells, while its literature and disease evidence are well developed.
- **Conclusion**: Established evidence supports MYO6 as a plausible trafficking and actin-motor component of the module, with a known relationship to TOM1. It is reasonable to hypothesize that MYO6 couples epithelial junctional state to endosomal transport, but the cross-tissue co-abundance relationship itself does not demonstrate such causality.

#### SPTBN2

- **Related proteins** (co-abundance neighbors): UTRN (0.89), RRBP1 (0.87), SUCLG2 (0.87), CPT2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_07940.1, huMAP3_09165.1
- **Function (MyGene.info)**: spectrin beta, non-erythrocytic 2. Spectrins are principle components of a cell's membrane-cytoskeleton and are composed of two alpha and two beta spectrin subunits. The protein encoded by this gene (SPTBN2), is called spectrin beta non-erythrocytic 2 or beta-III spectrin. It is related to, but distinct from, the beta-II spectrin gene which is also known as spectrin beta non-erythrocytic 1 (SPTBN1). SPTBN2 regulates the glutamate s…
- **Diseases (Open Targets)**: spinocerebellar ataxia type 5 (0.799); autosomal recessive spinocerebellar ataxia 14 (0.766); hereditary disease (0.506); cerebellar ataxia (0.438); spinocerebellar ataxia type 14 (0.388)
- **Europe PMC papers**: 767
- **Why important**: SPTBN2 provides a membrane-cytoskeleton connection and is linked in the module to UTRN, RRBP1, SUCLG2, and CPT2. Its annotations support spectrin-based membrane structure, vesicle-mediated transport, actin-cytoskeleton organization, and membrane signaling. It is detected in both tissues, is associated with epithelial and reproductive cell types, and occurs with TOM1 in hu.MAP complexes. Its disease associations also provide a well-established functional context for spectrin biology.
- **Conclusion**: Established evidence supports SPTBN2 as a structural organizer that may connect membrane architecture with transport and metabolic components. Its participation in the specific cervix–prostate module is a network-level observation, while any direct regulatory role in the other module genes remains hypothetical.

#### CPT2

- **Related proteins** (co-abundance neighbors): MYO6 (0.87), SPTBN2 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: carnitine palmitoyltransferase 2. The protein encoded by this gene is a nuclear protein which is transported to the mitochondrial inner membrane. Together with carnitine palmitoyltransferase I, the encoded protein oxidizes long-chain fatty acids in the mitochondria. Defects in this gene are associated with mitochondrial long-chain fatty-acid (LCFA) oxidation disorders. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: carnitine palmitoyl transferase II deficiency, myopathic form (0.830); carnitine palmitoyl transferase II deficiency, severe infantile form (0.800); carnitine palmitoyl transferase II deficiency, neonatal form (0.772); carnitine palmitoyltransferase II deficiency (0.710); hereditary disease (0.505)
- **Europe PMC papers**: 5133
- **Why important**: CPT2 represents the mitochondrial lipid-oxidation arm of the module. It is annotated for the carnitine shuttle, long-chain fatty-acid transport, and fatty-acid beta-oxidation, is detected in both tissues, and is associated with hepatocytes and reproductive cell types. It occurs in hu.MAP complex C1 with BPNT1 and FDXR and connects in the co-abundance network to MYO6 and SPTBN2. Its disease associations and literature record provide strong evidence for its established metabolic function.
- **Conclusion**: Established evidence supports CPT2 as a mitochondrial fatty-acid oxidation enzyme and as evidence that the module includes metabolic support in addition to epithelial structure. The proposed coordination between CPT2-dependent metabolism and junctional or trafficking state is a testable hypothesis, not an established interaction.

## Module 2

**Tissue pair**: cervix_uterine and prostate  
**Genes (7)**: NT5E, C3, COL6A1, GSN, H1-0, HEBP2, LTF

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway-level annotation. Its strongest biological interpretation is a mixed extracellular, secreted, immune-associated, and stromal module. COL6A1 points to extracellular-matrix and tissue-structural biology; NT5E points to extracellular nucleotide metabolism and cell-surface signaling; GSN links actin regulation with secreted blood-associated biology; LTF and C3 support mucosal innate defense, antimicrobial activity, iron handling, and complement-related inflammation. The STRING supplementary terms involving secretomes, signal-related proteins, and NETosis (4 supplementary STRING terms; within-query FDR 0.0024–0.0354) are consistent with this interpretation but are not globally corrected evidence. HEBP2 and H1-0 add possible oxidative-stress or cell-death and chromatin-related components, respectively, making this a heterogeneous co-abundance module rather than a clearly defined molecular complex.

**Cell composition.** The module is strongly influenced by secreted or extracellular proteins: COL6A1 is secreted to the extracellular matrix, while GSN, LTF, and C3 are secreted to blood. HPA therefore supports a substantial circulating, extracellular, or stromal contribution rather than a uniformly tissue-resident intracellular program. LTF and C3 show bone-marrow, neutrophil, or monocyte associations, and several genes show fibroblast or stromal-cell enhancement. NT5E is tissue-enhanced in cervix and detected in both tissues, whereas LTF is detected in prostate but not cervix and GSN is detected in cervix but not prostate. The mixed tissue and cell-type pattern means that shared blood-derived material, stromal cells, immune cells, or common extracellular signals could contribute to the module. HEBP2 and H1-0 are intracellular or nuclear proteins, so the module is not composed exclusively of plasma proteins.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship within the module is the C3–LTF connection. This is biologically compatible with complement, innate defense, and secreted inflammatory biology, but it does not establish the entire module as a direct interaction complex. The supplementary STRING associations (4 supplementary STRING terms; within-query FDR 0.0024–0.0354) repeatedly involve LTF, C3, GSN, COL6A1, NT5E, and, for the NETosis-related result, H1-0. These results support shared biological context but are not global enrichment evidence. No hu.MAP complex contains multiple module members. Thus, known interaction and complex evidence is sparse and concentrated around C3 and LTF, while the remaining relationships are primarily co-abundance associations rather than demonstrated physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 21 gene pairs: C3–LTF (0.711)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2023) Towards standardization of human adipose-derived stromal cells secretomes. (FDR = 0.0024, 5 genes); Keyword Signal (FDR = 0.0103, 5 genes); Keyword Secreted (FDR = 0.0332, 4 genes); PMID (2020) Cellular Mechanisms of NETosis. (FDR = 0.0354, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module should not be called a newly discovered molecular complex. Its lack of a hu.MAP complex, the sparse STRING interaction structure, and the absence of globally significant GO or KEGG enrichment argue against an already established coherent complex. At the same time, absence from STRING or hu.MAP does not prove novelty, and the individual functions of the genes are well established. The defensible conclusion is that the shared cervix–prostate co-abundance pattern may be a new tissue-pair-level observation, but its novelty as a biological mechanism remains unconfirmed without independent replication, comparison with published tissue co-expression studies, and validation of the underlying cell and protein sources.

**Hypothesis.** Hypothesis: the module reflects a shared extracellular and immune–stromal state present in both tissues, rather than a single intracellular pathway. Stromal extracellular-matrix production involving COL6A1 may co-vary with NT5E-mediated extracellular nucleotide handling and with secreted defense proteins such as LTF and C3. GSN may connect extracellular or circulating material with cytoskeletal and actin-related remodeling, while HEBP2 and H1-0 may mark accompanying oxidative-stress, cell-death, or chromatin-state variation. A contribution from blood-derived neutrophil or monocyte material, or from fibroblast-like stromal cells, is plausible from HPA, but this remains a hypothesis because the co-abundance edges do not establish causality or physical binding.

### Important genes

#### COL6A1

- **Related proteins** (co-abundance neighbors): LTF (0.89), GSN (0.88), NT5E (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen type VI alpha 1 chain. The collagens are a superfamily of proteins that play a role in maintaining the integrity of various tissues. Collagens are extracellular matrix proteins and have a triple-helical domain as their common structural element. Collagen VI is a major structural component of microfibrils. The basic structural unit of collagen VI is a heterotrimer of the alpha1(VI), alpha2(VI), and alpha3(VI) chains. The…
- **Diseases (Open Targets)**: Bethlem myopathy 1A (0.820); Ullrich congenital muscular dystrophy 1A (0.787); Bethlem myopathy (0.759); Ullrich congenital muscular dystrophy (0.750); collagen 6-related myopathy (0.624)
- **Europe PMC papers**: 5811
- **Why important**: COL6A1 is a central network member connected with LTF, GSN, and NT5E, and it is the clearest structural anchor of the module. It encodes a collagen-six extracellular-matrix component involved in tissue integrity and microfibrils, with fibroblast and stromal-cell associations in HPA. Its established links to Bethlem and Ullrich congenital muscular dystrophy and its extensive literature make it biologically informative even though it has no direct STRING partner in this module.
- **Conclusion**: Established evidence supports COL6A1 as an extracellular-matrix and stromal marker with a prominent position in the co-abundance network. It is plausible, but unproven, that COL6A1-related matrix remodeling helps organize the shared tissue signal.

#### NT5E

- **Related proteins** (co-abundance neighbors): COL6A1 (0.85), HEBP2 (0.84), LTF (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5'-nucleotidase ecto. The protein encoded by this gene is a plasma membrane protein that catalyzes the conversion of extracellular nucleotides to membrane-permeable nucleosides. The encoded protein is used as a determinant of lymphocyte differentiation. Defects in this gene can lead to the calcification of joints and arteries. Two transcript variants encoding different isoforms have been found for this gene.[provided b…
- **Diseases (Open Targets)**: hereditary arterial and articular multiple calcification syndrome (0.721); autosomal recessive spinocerebellar ataxia 20 (0.556); Spinocerebellar atrophy (0.340); non-small cell lung carcinoma (0.329); placental abruption (0.289)
- **Europe PMC papers**: 4404
- **Why important**: NT5E is another central network member, connected with COL6A1, HEBP2, and LTF. Its established function is cell-surface conversion of extracellular nucleotides into nucleosides, and its annotations include responses to ATP and ADP, leukocyte adhesion, and tissue mineralization. HPA detects it in both tissues and shows cervix enhancement as well as associations with lymphoid and endothelial-related cell types. Its disease associations include arterial and articular calcification and other disorders, with substantial literature support.
- **Conclusion**: Established evidence supports NT5E as a membrane-associated regulator of extracellular nucleotide signaling and a plausible interface between stromal, vascular, and immune biology. Its role as a driver of this module, rather than a correlated marker, is a hypothesis.

#### LTF

- **Related proteins** (co-abundance neighbors): COL6A1 (0.89), NT5E (0.82); STRING partners: C3 (0.711)
- **HPA**: Group enriched; Cell type enhanced; blood Group enriched; location None; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: lactotransferrin. This gene is a member of the transferrin family of genes and its protein product is found in the secondary granules of neutrophils. The protein is a major iron-binding protein in milk and body secretions with an antimicrobial activity, making it an important component of the non-specific immune system. The protein demonstrates a broad spectrum of properties, including regulation of iron homeostasi…
- **Diseases (Open Targets)**: tuberculosis (0.517); AL amyloidosis (0.467); Abnormality of the skeletal system (0.435); schizophrenia (0.235); inflammatory bowel disease (0.218)
- **Europe PMC papers**: 7000
- **Why important**: LTF connects directly in the module to COL6A1 and NT5E and is the most prominent secreted innate-defense candidate. It is a neutrophil-granule and body-fluid protein with iron-binding, antimicrobial, mucosal immune, and cytokine-regulatory functions. HPA associates it with bone marrow, neutrophils, non-classical monocytes, and glandular cell types; it is detected in prostate. LTF recurs across all supplementary STRING terms (4 supplementary STRING terms; within-query FDR 0.0024–0.0354) and has extensive literature, strengthening its interpretive value.
- **Conclusion**: Established evidence supports LTF as a secreted innate-defense and blood- or gland-associated component. Its co-abundance may indicate immune or secretory material in the samples, but the data do not show that LTF mechanistically controls the stromal or nucleotide-related genes.

#### C3

- **Related proteins** (co-abundance neighbors): GSN (0.85); STRING partners: LTF (0.711)
- **HPA**: Tissue enriched; Cell type enhanced; blood Immune cell enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: complement C3. Complement component C3 plays a central role in the activation of complement system. Its activation is required for both classical and alternative complement activation pathways. The encoded preproprotein is proteolytically processed to generate alpha and beta subunits that form the mature protein, which is then further processed to generate numerous peptide products. The C3a peptide, also known a…
- **Diseases (Open Targets)**: atypical hemolytic-uremic syndrome with C3 anomaly (0.798); complement component 3 deficiency (0.771); age-related macular degeneration (0.740); complement 3 glomerulopathy (0.596); atypical hemolytic-uremic syndrome (0.594)
- **Europe PMC papers**: 153947
- **Why important**: C3 is the canonical complement component in the module and is the partner of GSN in the co-abundance graph as well as the only member with a high-confidence STRING link to LTF. It is liver-enriched, secreted to blood, associated with non-classical monocytes, and has established roles in complement activation, inflammatory signaling, and antimicrobial activity. Its extensive disease literature includes complement deficiency, complement-mediated kidney disease, and macular degeneration.
- **Conclusion**: Established evidence supports C3 as an extracellular complement and inflammatory marker. The C3–LTF relationship provides the strongest known interaction context in the module, but it remains unproven that complement activation explains the complete cervix–prostate co-abundance pattern.

#### GSN

- **Related proteins** (co-abundance neighbors): COL6A1 (0.88), C3 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: gelsolin. The protein encoded by this gene binds to the 'plus' ends of actin monomers and filaments to prevent monomer exchange. The encoded calcium-regulated protein functions in both assembly and disassembly of actin filaments. Defects in this gene are a cause of familial amyloidosis Finnish type (FAF). Multiple transcript variants encoding several different isoforms have been found for this gene. [provid…
- **Diseases (Open Targets)**: Finnish type amyloidosis (0.805); AL amyloidosis (0.463); neuropathy (0.418); cardiomyopathy (0.418); cutis laxa (0.417)
- **Europe PMC papers**: 5062
- **Why important**: GSN occupies an intermediate network position between COL6A1 and C3 and is repeatedly represented in the supplementary secretome and NETosis-related STRING results (4 supplementary STRING terms; within-query FDR 0.0024–0.0354). Its established function is calcium-regulated control of actin filament assembly and disassembly, and HPA associates it with fibroblasts, endothelial and epithelial cell types, eosinophils, heart muscle, and secretion to blood. Its disease associations include Finnish-type amyloidosis and cardiomyopathy, supported by extensive literature.
- **Conclusion**: Established evidence supports GSN as an actin-remodeling protein that can also appear in extracellular or blood-associated contexts. It may link cytoskeletal or stromal remodeling to secreted inflammatory material, but that integrative role is a hypothesis rather than a demonstrated mechanism.

## Module 3

**Tissue pair**: cervix_uterine and prostate  
**Genes (28)**: ACO2, AGPS, ADGRE5, AMPD2, AP2B1, ARPC1B, CPD, DCTN1, DNM1L, DNM2, EZR, FKBP10, LTA4H, NCKAP1, NUP214, ERC1, SEC23A, SEC23B, SEPTIN7, SEPTIN9, SNX2, IARS2, TXNDC5, USP5, UNC45A, USO1, WDR44, XPO7

### Function

No GO or KEGG term passed global correction, so the module does not have a statistically established pathway-level annotation from that analysis. Its gene composition nevertheless points to a broad intracellular logistics and cell-architecture program. SEC23A, SEC23B and USO1 support COPII-dependent ER-to-Golgi trafficking and vesicle fusion; AP2B1, DNM2, WDR44 and SNX2 support coated-vesicle formation, endocytosis, endosomal recycling and retrograde transport; SEPTIN7, SEPTIN9, ARPC1B, NCKAP1 and EZR support actin organization, membrane shape and cell movement. Additional genes connect the module to nuclear transport, mitochondrial dynamics, protein folding, lipid metabolism and inflammatory lipid mediator production. The most defensible interpretation is therefore a coordinated cellular trafficking, membrane-remodelling and proteostasis state rather than a narrowly defined biological pathway. The absence of globally significant GO or KEGG enrichment does not invalidate the module; it limits the strength and specificity of pathway-level claims.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a small minority of genes as secreted, and most proteins are intracellular or membrane-associated. Most genes have low tissue specificity, and protein detection is broadly compatible with both cervix_uterine and prostate. This supports a shared cellular program rather than a tissue-exclusive secretory program. The module also contains a meaningful immune and myeloid signal. HPA highlights neutrophils, monocytes, neutrophil progenitors and other blood-associated cell types for several genes, including ADGRE5, CPD, LTA4H, AMPD2, DNM2 and SEC23B. However, most genes have low immune-cell specificity, so the module is not adequately described as a blood-cell module alone. A shared infiltrating myeloid or other immune-cell contribution remains plausible, as does a shared epithelial, stromal or general housekeeping contribution. The HPA evidence argues for testing cell composition and tissue histology before assigning the co-abundance pattern to a specialised cervix or prostate function.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The STRING network provides a limited but coherent set of established relationships. SEC23A is linked to SEC23B and USO1, SEPTIN7 is strongly linked to SEPTIN9, AP2B1 is linked to DNM2, and ARPC1B is linked to NCKAP1. These links support real molecular submodules involving COPII trafficking, septin cytoskeletal organisation, clathrin-associated endocytosis and Arp two slash three actin nucleation. The hu.MAP evidence independently reinforces these interpretations. (hu.MAP huMAP3_12394.1) places USO1, AP2B1, SEC23A and SEC23B in a large trafficking and coated-vesicle complex. (hu.MAP huMAP3_00065.1) through (hu.MAP huMAP3_13535.1) repeatedly recover SEC23A with SEC23B in COPII-related complexes. (hu.MAP huMAP3_02362.1) recovers SEPTIN7 with SEPTIN9, while (hu.MAP huMAP3_11232.1) places DNM2 with XPO7 in a larger complex. Many other module edges are not represented by high-confidence STRING interactions or hu.MAP complexes. Thus the module contains several known molecular assemblies, but its full co-abundance structure is not equivalent to one experimentally established physical complex.

**STRING interactions (score >= 0.7)**: 5 of 378 gene pairs: AP2B1–DNM2 (0.759); ARPC1B–NCKAP1 (0.714); SEC23A–SEC23B (0.949); SEC23A–USO1 (0.704); SEPTIN7–SEPTIN9 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (USO1, AP2B1, SEC23A, SEC23B; 4/98); huMAP3_00065.1 (SEC23A, SEC23B; 2/4); huMAP3_00707.1 (SEC23A, SEC23B; 2/4); huMAP3_07775.1 (SEC23A, SEC23B; 2/5); huMAP3_06453.1 (SEC23A, SEC23B; 2/6); huMAP3_09282.1 (SEC23A, SEC23B; 2/6); huMAP3_11128.1 (SEC23A, SEC23B; 2/8); huMAP3_11237.1 (SEC23A, SEC23B; 2/12); huMAP3_13535.1 (SEC23A, SEC23B; 2/14); huMAP3_02362.1 (SEPTIN7, SEPTIN9; 2/14); huMAP3_11232.1 (DNM2, XPO7; 2/78)

### Novelty

The module should not be presented as a newly discovered molecular mechanism. Its strongest components and relationships are already biologically established, including COPII trafficking, endocytosis, septin organisation, actin remodelling, mitochondrial dynamics and nuclear transport. What may be novel is the coordinated co-abundance of these genes across cervix_uterine and prostate, especially the particular combination of trafficking, cytoskeletal, metabolic and immune-associated genes. That claim remains provisional because the module has no globally significant GO or KEGG term, no STRING functional-enrichment result, and several genes may reflect shared cell composition or general cellular activity. Absence from STRING or hu.MAP does not demonstrate novelty; it may reflect incomplete interaction coverage, context dependence or co-regulation without direct physical binding. Replication in independent cohorts, adjustment for cell composition and comparison with published tissue co-expression modules would be needed to establish a genuinely new finding.

**Hypothesis.** Hypothesis: the shared module reflects a conserved cellular state in which high membrane and protein-trafficking demand couples ER-to-Golgi export and endocytic recycling to cytoskeletal remodelling, mitochondrial maintenance and proteostasis. SEC23A, SEC23B and USO1 could support secretory trafficking; AP2B1 and DNM2 could support receptor internalisation; SEPTIN7, SEPTIN9, ARPC1B, NCKAP1 and EZR could organise membrane-associated actin and cell shape; DNM1L, IARS2, ACO2, FKBP10 and TXNDC5 could reflect linked metabolic, folding and organelle-maintenance demands. An alternative hypothesis is that part of this signal arises from shared immune or myeloid-cell content, particularly the genes with neutrophil or monocyte enrichment. These hypotheses require validation using cell-resolved expression, protein localisation, perturbation and independent tissue cohorts.

### Important genes

#### SEC23A

- **Related proteins** (co-abundance neighbors): USO1 (0.89), XPO7 (0.87), DNM1L (0.83), IARS2 (0.83), AP2B1 (0.83), NUP214 (0.81); STRING partners: SEC23B (0.949), USO1 (0.704)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_12394.1, huMAP3_00065.1, huMAP3_00707.1, huMAP3_07775.1, huMAP3_06453.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_11237.1, huMAP3_13535.1
- **Function (MyGene.info)**: SEC23 homolog A, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family. It is part of a protein complex and found in the ribosome-free transitional face of the endoplasmic reticulum (ER) and associated vesicles. This protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The encoded protein is…
- **Diseases (Open Targets)**: craniolenticulosutural dysplasia (0.627); vitamin D deficiency (0.283); alcohol drinking (0.221); male reproductive organ cancer (0.193); metabolic syndrome X (0.156)
- **Europe PMC papers**: 1139
- **Why important**: SEC23A has the strongest network position in the module and connects to USO1, XPO7, DNM1L, IARS2, AP2B1 and NUP214. It is a COPII component involved in ER-to-Golgi transport, vesicle budding and cargo loading. It is also supported by the SEC23A–SEC23B STRING relationship and by the repeated hu.MAP complexes (hu.MAP huMAP3_12394.1) through (hu.MAP huMAP3_13535.1). Its disease associations include craniolenticulosutural dysplasia and male reproductive organ cancer, and the fact sheet indicates substantial literature coverage.
- **Conclusion**: Established evidence supports SEC23A as a central trafficking anchor and the best marker of the module's secretory-transport component. It is plausible, but not established, that coordinated SEC23A abundance is a driver of the shared module rather than a consequence of general cellular demand.

#### SEC23B

- **Related proteins** (co-abundance neighbors): USO1 (0.84); STRING partners: SEC23A (0.949)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Vesicles, Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_12394.1, huMAP3_00065.1, huMAP3_00707.1, huMAP3_07775.1, huMAP3_06453.1, huMAP3_09282.1, huMAP3_11128.1, huMAP3_11237.1, huMAP3_13535.1
- **Function (MyGene.info)**: SEC23 homolog B, COPII component. The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The function of this gene product has been implicated in cargo selection and concentration. Multiple alternativel…
- **Diseases (Open Targets)**: congenital dyserythropoietic anemia type 2 (0.834); Cowden syndrome 7 (0.730); congenital dyserythropoietic anemia (0.438); hereditary disease (0.194); hereditary ataxia (0.118)
- **Europe PMC papers**: 847
- **Why important**: SEC23B is the paralogous COPII component paired with SEC23A in STRING and in several hu.MAP complexes, including (hu.MAP huMAP3_12394.1) through (hu.MAP huMAP3_13535.1). It contributes to ER-to-Golgi vesicle budding and cargo selection and is detected in both tissues. Its disease associations include congenital dyserythropoietic anemia and Cowden syndrome.
- **Conclusion**: Established evidence supports SEC23B as a genuine member of the COPII-related core rather than an incidental co-abundance gene. The paired presence of SEC23A and SEC23B strengthens the trafficking interpretation, but does not prove that the two proteins form the dominant functional driver in these tissues.

#### DNM2

- **Related proteins** (co-abundance neighbors): SEPTIN9 (0.92), NUP214 (0.83); STRING partners: AP2B1 (0.759)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_11232.1
- **Function (MyGene.info)**: dynamin 2. Dynamins represent one of the subfamilies of GTP-binding proteins. These proteins share considerable sequence similarity over the N-terminal portion of the molecule, which contains the GTPase domain. Dynamins are associated with microtubules. They have been implicated in cell processes such as endocytosis and cell motility, and in alterations of the membrane that accompany certain activities such …
- **Diseases (Open Targets)**: autosomal dominant centronuclear myopathy (0.844); Charcot-Marie-Tooth disease dominant intermediate B (0.830); fetal akinesia-cerebral and retinal hemorrhage syndrome (0.739); autosomal dominant Charcot-Marie-Tooth disease type 2M (0.715); centronuclear myopathy (0.692)
- **Europe PMC papers**: 2412
- **Why important**: DNM2 links the module to membrane scission, endocytosis and post-Golgi vesicle transport. It connects in the module to SEPTIN9 and NUP214, has a STRING relationship with AP2B1, and occurs in hu.MAP complex (hu.MAP huMAP3_11232.1). It has a well-developed disease literature involving centronuclear myopathy and Charcot-Marie-Tooth disease.
- **Conclusion**: Established evidence supports DNM2 as a bridge between vesicle trafficking and cytoskeletal membrane remodelling. Its neutrophil-associated HPA signal also makes it relevant to the alternative cell-composition explanation. A specific role for DNM2 in the shared cervix–prostate state remains a hypothesis.

#### AP2B1

- **Related proteins** (co-abundance neighbors): TXNDC5 (0.87), SEPTIN9 (0.83), AGPS (0.83), SEC23A (0.83); STRING partners: DNM2 (0.759)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_12394.1
- **Function (MyGene.info)**: adaptor related protein complex 2 subunit beta 1. The protein encoded by this gene is one of two large chain components of the assembly protein complex 2, which serves to link clathrin to receptors in coated vesicles. The encoded protein is found on the cytoplasmic face of coated vesicles in the plasma membrane. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: HIV infectious disease (0.551); dengue disease (0.375); peroxisome biogenesis disorder (0.186); peroxisome biogenesis disorder 3A (Zellweger) (0.186); mathematical ability (0.180)
- **Europe PMC papers**: 866
- **Why important**: AP2B1 is a clathrin adaptor subunit involved in receptor-linked endocytosis and vesicle-mediated transport. It connects SEC23A, TXNDC5, SEPTIN9 and AGPS, has a STRING relationship with DNM2, and is part of hu.MAP complex (hu.MAP huMAP3_12394.1). Its literature includes vesicle transport, infection-related associations and peroxisome-related disease associations.
- **Conclusion**: Established evidence supports AP2B1 as an endocytic and coated-vesicle component that complements the COPII signal. Its absence of protein detection in prostate in the HPA summary cautions against treating it as a uniformly expressed tissue-intrinsic driver, and a contribution from cellular composition remains possible.

#### SEPTIN9

- **Related proteins** (co-abundance neighbors): DNM2 (0.92), AP2B1 (0.83), ADGRE5 (0.80); STRING partners: SEPTIN7 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_02362.1
- **Function (MyGene.info)**: septin 9. This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic l…
- **Diseases (Open Targets)**: neuralgic amyotrophy (0.564); hypertensive disorder (0.496); cataract (0.437); essential hypertension (0.426); alcohol drinking (0.420)
- **Europe PMC papers**: 748
- **Why important**: SEPTIN9 connects DNM2, AP2B1 and ADGRE5 and is paired with SEPTIN7 by a high-confidence STRING relationship and hu.MAP complex (hu.MAP huMAP3_02362.1). Septin biology supports cytoskeletal organisation, intracellular localisation, cytokinesis and cilium-related processes. Its disease associations include hereditary neuralgic amyotrophy and vascular or blood-pressure-related traits.
- **Conclusion**: Established evidence supports SEPTIN9 as a cytoskeletal and membrane-organisation component that may connect endocytosis to cell shape. Its urothelial-cell annotation and immune-adjacent network neighbours make cell identity an important confounder. A direct role in the conserved tissue-pair module is therefore plausible but unproven.

## Module 4

**Tissue pair**: cervix_uterine and prostate  
**Genes (11)**: ADAM10, ALDH3A2, DSP, SORD, HADHB, ERLIN2, FLOT1, AGL, GYS1, NFKB1, JUP

### Function

The module does not have any GO or KEGG term passing global multiple-testing correction, so no pathway-level enrichment can be claimed from the primary analysis. Its biology is heterogeneous but coherent at the level of cellular structure and metabolism. The strongest directly supported themes are desmosomal and cell-junction biology through DSP and JUP, glycogen synthesis and degradation through GYS1 and AGL, lipid and aldehyde metabolism through ALDH3A2 and HADHB, ER lipid-raft and ER-associated degradation biology through ERLIN2, membrane trafficking through FLOT1 and ADAM10, and inflammatory transcriptional regulation through NFKB1. The network appears to contain several connected substructures rather than one uniformly annotated pathway. SORD is a high-connectivity bridge between the junctional genes and metabolic or ER-associated genes. These interpretations are functional annotations and network-based hypotheses, not evidence of significant GO or KEGG enrichment.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: only a minority of genes have secretome annotation, and the proteins are mainly intracellular, membrane-associated, mitochondrial, cytosolic, nuclear, or junctional. The HPA profile argues against a simple blood-contamination explanation. Most genes have low immune-cell specificity, although some show enrichment or enhancement in neutrophil, monocyte, B-cell, eosinophil, or related populations. The recurring tissue and cell-type signals instead point toward epithelial and barrier-associated states, with additional skeletal-muscle, tongue, liver, esophageal, and skin associations. Because many genes are broadly detectable and several are enriched in cell types that can occur across tissues, the shared cervix and prostate signal could reflect common epithelial or junctional biology, metabolic state, or shared cellular composition. HPA protein detection in both tissues supports presence for much of the module, but the lack of DSP and ALDH3A2 detection in the two queried tissues cautions against assuming that every transcript-level co-abundance relationship represents abundant protein in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides strong, specific support for the DSP-JUP relationship and for the AGL-GYS1 relationship. These are biologically concordant pairs: DSP and JUP are established desmosomal or junctional components, while AGL and GYS1 participate in glycogen metabolism. No STRING functional-enrichment result was returned, so the network should not be assigned a STRING-derived pathway label. hu.MAP independently places AGL and GYS1 together in several glycogen-related complexes, with additional glycogen, phosphatase-regulatory, nutrient-response, and autophagy-associated proteins in the surrounding complexes. hu.MAP also repeatedly places DSP and JUP in epithelial or keratinization-associated complexes containing desmosomal, junctional, and barrier proteins. Thus, the module contains two externally supported molecular pairings, while its remaining cross-subgraph links are less established by the supplied resources. The known complexes support biological plausibility, but the partial overlap of each complex with the module does not establish that the complete module is one physical complex.

**STRING interactions (score >= 0.7)**: 2 of 55 gene pairs: AGL–GYS1 (0.944); DSP–JUP (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10227.1 (GYS1, AGL; 2/14); huMAP3_09760.1 (GYS1, AGL; 2/15); huMAP3_13075.1 (GYS1, AGL; 2/15); huMAP3_11993.1 (GYS1, AGL; 2/20); huMAP3_12186.1 (GYS1, AGL; 2/23); huMAP3_05845.1 (JUP, DSP; 2/24); huMAP3_08595.1 (JUP, DSP; 2/25); huMAP3_09125.1 (JUP, DSP; 2/53); huMAP3_09929.1 (JUP, DSP; 2/75)

### Novelty

The module-level finding may be novel as a conserved co-abundance pattern shared by cervix and prostate, but the available evidence is insufficient to call it a new biological mechanism. The DSP-JUP and AGL-GYS1 relationships are already well established by STRING and hu.MAP, and the individual functions of the genes are extensively characterized. What could be new is their recurrent co-abundance across these two tissue groups and the apparent connection between junctional, metabolic, ER, membrane-trafficking, and inflammatory components. That possibility requires validation in independent cohorts, control for epithelial and immune composition, and comparison with published tissue co-expression modules. Lack of a STRING interaction or hu.MAP complex for several gene pairs is not evidence of novelty. The absence of globally significant GO or KEGG enrichment also does not invalidate the module; it instead indicates that its signal is mixed, modest, or not captured by the tested annotations.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial-cell state in cervix and prostate in which junctional integrity is coupled to metabolic adaptation and membrane or ER remodeling. In this model, the DSP-JUP axis represents desmosomal structural organization, the AGL-GYS1 axis represents glycogen storage and mobilization, ALDH3A2 and HADHB support handling of lipid-derived aldehydes and fatty-acid oxidation, ERLIN2 and FLOT1 support ER or membrane-domain processes, and ADAM10 may connect membrane trafficking with regulated ectodomain cleavage. SORD and NFKB1 could link metabolic or redox-related state to inflammatory transcriptional responses. This is a mechanistic model generated from annotations and network structure; the co-abundance data do not demonstrate physical interaction, directionality, or causality.

### Important genes

#### DSP

- **Related proteins** (co-abundance neighbors): JUP (0.91), AGL (0.88), SORD (0.85); STRING partners: JUP (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: huMAP3_05845.1, huMAP3_08595.1, huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: desmoplakin. This gene encodes a protein that anchors intermediate filaments to desmosomal plaques and forms an obligate component of functional desmosomes. Mutations in this gene are the cause of several cardiomyopathies and keratodermas, including skin fragility-woolly hair syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: arrhythmogenic cardiomyopathy with wooly hair and keratoderma (0.841); arrhythmogenic right ventricular dysplasia 8 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.760); lethal acantholytic epidermolysis bullosa (0.745); cardiomyopathy, dilated, with wooly hair, keratoderma, and tooth agenesis (0.741)
- **Europe PMC papers**: 17350
- **Why important**: DSP is among the more highly connected genes in the module and is directly linked to JUP by a very strong STRING relationship. It is a core desmosomal plaque component, has junctional localization, is represented with JUP in several hu.MAP epithelial or barrier complexes, and has extensive disease and literature support involving cardiomyopathy, keratoderma, and epidermal fragility.
- **Conclusion**: Established evidence supports DSP as a structural epithelial-junction anchor and as one of the best-supported components of the module. Its co-abundance here is consistent with shared junctional or epithelial state. It does not by itself establish that desmosome dysfunction drives the cervix-prostate association.

#### JUP

- **Related proteins** (co-abundance neighbors): DSP (0.91), SORD (0.82), ADAM10 (0.81); STRING partners: DSP (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_05845.1, huMAP3_08595.1, huMAP3_09125.1, huMAP3_09929.1
- **Function (MyGene.info)**: junction plakoglobin. This gene encodes a major cytoplasmic protein which is the only known constituent common to submembranous plaques of both desmosomes and intermediate junctions. This protein forms distinct complexes with cadherins and desmosomal cadherins and is a member of the catenin family since it contains a distinct repeating amino acid motif called the armadillo repeat. Mutation in this gene has been associa…
- **Diseases (Open Targets)**: Naxos disease (0.784); arrhythmogenic right ventricular dysplasia 12 (0.755); arrhythmogenic right ventricular cardiomyopathy (0.597); lethal acantholytic epidermolysis bullosa (0.383); familial isolated arrhythmogenic ventricular dysplasia, biventricular form (0.370)
- **Europe PMC papers**: 3429
- **Why important**: JUP is a highly connected junctional gene, directly paired with DSP in STRING, detected at the protein level in both queried tissues, and present with DSP in multiple hu.MAP complexes. It is a catenin-family component of desmosomes and intermediate junctions and has established associations with Naxos disease and arrhythmogenic cardiomyopathy.
- **Conclusion**: Established evidence supports JUP as a central cell-adhesion and junctional marker in this module. Its position connecting the DSP branch to SORD and ADAM10 makes it a plausible integrator of structural and membrane-associated signals, but that integrator role remains a hypothesis.

#### AGL

- **Related proteins** (co-abundance neighbors): DSP (0.88), GYS1 (0.81); STRING partners: GYS1 (0.944)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase. This gene encodes the glycogen debrancher enzyme which is involved in glycogen degradation. This enzyme has two independent catalytic activities which occur at different sites on the protein: a 4-alpha-glucotransferase activity and a amylo-1,6-glucosidase activity. Mutations in this gene are associated with glycogen storage disease although a wide range of enzymatic and clinical variability occurs…
- **Diseases (Open Targets)**: glycogen storage disease III (0.831); disorder of glycogen metabolism (0.768); glycogen storage disease XV (0.608); hereditary disease (0.507); Acute rhabdomyolysis (0.463)
- **Europe PMC papers**: 4441
- **Why important**: AGL is connected to DSP and GYS1 and is repeatedly represented with GYS1 in hu.MAP complexes. It encodes the glycogen-debranching enzyme and has established links to glycogen storage disease. Its tissue profile emphasizes skeletal muscle and tongue, suggesting that metabolic-state or cell-composition effects may contribute to the shared signal.
- **Conclusion**: Established evidence supports AGL as a glycogen-degradation component and as the metabolic partner of GYS1. The module supports a possible glycogen-related subprogram, but the lack of globally significant GO or KEGG enrichment means this cannot be presented as a statistically enriched pathway.

#### GYS1

- **Related proteins** (co-abundance neighbors): AGL (0.81); STRING partners: AGL (0.944)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Microtubules, Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_10227.1, huMAP3_09760.1, huMAP3_13075.1, huMAP3_11993.1, huMAP3_12186.1
- **Function (MyGene.info)**: glycogen synthase 1. The protein encoded by this gene catalyzes the addition of glucose monomers to the growing glycogen molecule through the formation of alpha-1,4-glycoside linkages. Mutations in this gene are associated with muscle glycogen storage disease. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Sep 2009].
- **Diseases (Open Targets)**: glycogen storage disease due to muscle and heart glycogen synthase deficiency (0.784); disorder of glycogen metabolism (0.530); neurodegenerative disease (0.440); glycogen storage disease XV (0.382); congenital myasthenic syndrome (0.266)
- **Europe PMC papers**: 1794
- **Why important**: GYS1 forms the other directly supported STRING pair with AGL and recurs with AGL across several hu.MAP complexes. It catalyzes glycogen synthesis and is associated with muscle and heart glycogen-storage disorders. Its network position is modest, but its relationship with AGL is mechanistically complementary and therefore informative.
- **Conclusion**: Established evidence supports GYS1 as a glycogen-synthesis component that gives the module a plausible carbohydrate-storage axis. Its joint abundance with AGL may indicate coordinated glycogen turnover or shared cellular composition; it does not prove that glycogen flux is altered.

#### SORD

- **Related proteins** (co-abundance neighbors): DSP (0.85), NFKB1 (0.83), ERLIN2 (0.82), JUP (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sorbitol dehydrogenase. Sorbitol dehydrogenase (SORD; EC 1.1.1.14) catalyzes the interconversion of polyols and their corresponding ketoses, and together with aldose reductase (ALDR1; MIM 103880), makes up the sorbitol pathway that is believed to play an important role in the development of diabetic complications (summarized by Carr and Markham, 1995 [PubMed 8535074]). The first reaction of the pathway (also called the p…
- **Diseases (Open Targets)**: neuronopathy, distal hereditary motor, autosomal recessive 8 (0.781); hereditary disease (0.486); Charcot-Marie-Tooth disease (0.377); juvenile amyotrophic lateral sclerosis (0.370); neuromuscular disease (0.340)
- **Europe PMC papers**: 1060
- **Why important**: SORD has the strongest network connectivity in the supplied subgraph and bridges DSP, JUP, NFKB1, and ERLIN2. It encodes sorbitol dehydrogenase, participates in polyol and carbohydrate metabolism, is detected in both queried tissues, and has substantial disease and literature support involving inherited neuropathy and related metabolic consequences.
- **Conclusion**: Established evidence supports SORD as a metabolic enzyme and as a network bridge in this module. Its position makes it a useful candidate for linking metabolic state with junctional and ER-associated biology, but the bridge interpretation is network-based and does not demonstrate biochemical regulation between these genes.

#### ERLIN2

- **Related proteins** (co-abundance neighbors): ALDH3A2 (0.87), HADHB (0.83), SORD (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ER lipid raft associated 2. This gene encodes a member of the SPFH domain-containing family of lipid raft-associated proteins. The encoded protein is localized to lipid rafts of the endoplasmic reticulum and plays a critical role in inositol 1,4,5-trisphosphate (IP3) signaling by mediating ER-associated degradation of activated IP3 receptors. Mutations in this gene are a cause of spastic paraplegia-18 (SPG18). Alternatively …
- **Diseases (Open Targets)**: hereditary spastic paraplegia 18 (0.757); spastic paraplegia 18b, autosomal recessive (0.659); hereditary spastic paraplegia (0.631); cancer (0.587); autosomal dominant complex spastic paraplegia (0.570)
- **Europe PMC papers**: 595
- **Why important**: ERLIN2 connects ALDH3A2, HADHB, and SORD and is localized to the endoplasmic reticulum. Its known functions include ER-associated degradation of activated IP3 receptors and regulation of lipid-biosynthetic signaling. It also has established associations with hereditary spastic paraplegia, giving the module an ER and lipid-homeostasis anchor.
- **Conclusion**: Established evidence supports ERLIN2 as an ER lipid-raft and ERAD-related protein. Its connectivity to metabolic genes supports a possible ER-metabolic interface in the module, but the absence of direct STRING or hu.MAP support for these module links means that this interface remains a hypothesis.

## Module 5

**Tissue pair**: cervix_uterine and prostate  
**Genes (13)**: AHNAK, SERPINC1, ANXA4, ANXA5, ANXA6, APOE, AHSG, GLIPR2, ITIH2, LHPP, RSU1, SOD2, GC

### Function

The strongest interpretation is a blood-associated extracellular and secretory module linked to coagulation regulation and membrane-associated vesicles. The primary evidence is the enrichment of blood microparticles (GO:CC blood microparticle; q_global = 0.000216), regulation of coagulation (GO:BP regulation of coagulation; q_global = 0.00881), zymogen granule membrane (GO:CC zymogen granule membrane; q_global = 0.0236), and zymogen granule (GO:CC zymogen granule; q_global = 0.0404). Annexins ANXA4, ANXA5, and ANXA6 support a calcium-dependent membrane and vesicle component, while SERPINC1 provides a direct anticoagulation function. The extracellular-matrix and extracellular-vesicle signals in (STRING Component Collagen-containing extracellular matrix; within-query FDR = 2.17e-05) and (5 supplementary STRING terms; within-query FDR 0.00071–0.007) are supplementary and consistent with this interpretation. The sparse network suggests a composite module rather than a single tightly connected intracellular pathway.

**Cell composition.** The module is strongly influenced by plasma and secreted proteins, including AHSG, APOE, GC, ITIH2, and SERPINC1. HPA evidence links several of these genes to liver and hepatocytes, and identifies secretion to blood for APOE and ITIH2. This composition makes circulating protein carryover, vascular material, or shared blood-derived material a plausible explanation for the conservation between cervix_uterine and prostate. The module is not broadly immune-cell enriched: most genes have low immune-cell specificity or are not detected in immune cells, although SOD2 has an immune-cell association with neutrophils and several genes show cell-type enhancement in monocytes or platelet-related populations. The eight detected proteins in each tissue do not establish local production, especially because several central plasma proteins are not detected by HPA in either tissue.

**GO/KEGG enrichment**: 4 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC blood microparticle | 0.000216 | AHSG, ANXA5, APOE, GC, ITIH2, SERPINC1 |
| GO:BP regulation of coagulation | 0.00881 | ANXA4, ANXA5, APOE, SERPINC1 |
| GO:CC zymogen granule membrane | 0.0236 | ANXA4, ANXA5, ANXA6 |
| GO:CC zymogen granule | 0.0404 | ANXA4, ANXA5, ANXA6 |

### STRING and hu.MAP

The directly supported STRING relationships are AHSG with GC, ITIH2, and SERPINC1, plus GC with SERPINC1. These form a coherent plasma-protein and coagulation-associated interaction core. The remaining co-abundance edges are not supported by high-confidence STRING relationships in the supplied evidence, so co-abundance should not be treated as direct physical interaction. hu.MAP provides additional context: AHSG, GC, ITIH2, and SERPINC1 co-occur in the broad plasma-protein complex (hu.MAP huMAP3_15040.1), while AHSG, GC, and ITIH2 recur in (hu.MAP huMAP3_10678.1), and AHSG with ITIH2 recur in (hu.MAP huMAP3_07265.1) and (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1). ANXA6 and GLIPR2 share (hu.MAP huMAP3_12658.1), and AHSG with GC share (hu.MAP huMAP3_09434.1). These complexes reinforce a known extracellular and plasma-protein framework, but their broad membership means they do not prove that every module gene participates in one physical complex.

**STRING interactions (score >= 0.7)**: 4 of 78 gene pairs: AHSG–GC (0.959); AHSG–ITIH2 (0.922); AHSG–SERPINC1 (0.838); GC–SERPINC1 (0.84)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Collagen-containing extracellular matrix (FDR = 2.17e-05, 7 genes); Component Blood microparticle (FDR = 3.14e-05, 6 genes); COMPARTMENTS Blood microparticle (FDR = 0.00013, 6 genes); COMPARTMENTS Extracellular space (FDR = 0.00071, 9 genes); COMPARTMENTS Vesicle (FDR = 0.0029, 11 genes); COMPARTMENTS Extracellular membrane-bounded organelle (FDR = 0.0029, 8 genes); COMPARTMENTS Extracellular vesicle (FDR = 0.0029, 8 genes); Component Extracellular exosome (FDR = 0.007, 12 genes); NetworkNeighborAL Complement and coagulation cascades, and Protein-lipid complex (FDR = 0.0111, 4 genes); PMID (2023) Cerebrospinal Fluid Proteomic Profiles in Patients with Postherpetic Neuralgia. (FDR = 0.0178, 5 genes); NetworkNeighborAL Hemostasis, and Dissolution of Fibrin Clot (FDR = 0.0213, 3 genes); SMART Annexin repeats (FDR = 0.0229, 3 genes); PMID (2020) Revelation of Proteomic Indicators for Colorectal Cancer in Initial Stages of Development. (FDR = 0.0332, 5 genes); RCTM Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) (FDR = 0.0438, 4 genes); RCTM Post-translational protein phosphorylation (FDR = 0.0438, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (SERPINC1, AHSG, GC, ITIH2; 4/64); huMAP3_10678.1 (AHSG, GC, ITIH2; 3/71); huMAP3_07265.1 (AHSG, ITIH2; 2/20); huMAP3_12658.1 (ANXA6, GLIPR2; 2/32); huMAP3_09434.1 (AHSG, GC; 2/33); huMAP3_08395.1 (AHSG, ITIH2; 2/43); huMAP3_09531.1 (AHSG, ITIH2; 2/47); huMAP3_10101.1 (AHSG, ITIH2; 2/49)

### Novelty

The molecular interpretation is not a new coagulation or plasma-protein mechanism: the STRING links and hu.MAP complexes show that important parts of the module are already known. The potentially novel aspect is the co-abundance of this mixed plasma, membrane, vesicle, and tissue-associated set across cervix_uterine and prostate. The supplied evidence does not include a prior module catalogue or an independent study demonstrating this exact tissue-pair module, so novelty at the module level remains plausible but unproven. Absence of STRING or hu.MAP support for some edges cannot establish novelty, because those resources capture physical interactions and curated complexes rather than every tissue-level co-abundance relationship. Independent cohorts, matched plasma controls, and cell-resolved measurements would be needed to distinguish a genuine shared tissue program from circulating-protein or sample-composition effects.

**Hypothesis.** Hypothesis: a shared vascular or extracellular-vesicle environment in cervix_uterine and prostate produces coordinated abundance of circulating liver-derived proteins with local calcium-dependent membrane proteins. In this model, AHSG, GC, ITIH2, APOE, and SERPINC1 represent a circulating plasma-protein scaffold related to lipid transport, extracellular-matrix stabilization, and coagulation control, while ANXA4, ANXA5, and ANXA6 represent membrane or vesicle responses. SOD2 could reflect oxidative or mitochondrial stress, and GLIPR2, RSU1, LHPP, and AHNAK could connect the extracellular signal to epithelial, adhesion, or membrane-repair states. This is a mechanistic hypothesis rather than a demonstrated causal pathway; the strongest alternative is shared blood or extracellular material in the tissue samples.

### Important genes

#### SERPINC1

- **Related proteins** (co-abundance neighbors): SOD2 (0.89), ANXA4 (0.83); STRING partners: AHSG (0.838), GC (0.84)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: serpin family C member 1. The protein encoded by this gene, antithrombin III, is a plasma protease inhibitor and a member of the serpin superfamily. This protein inhibits thrombin as well as other activated serine proteases of the coagulation system, and it regulates the blood coagulation cascade. The protein includes two functional domains: the heparin binding-domain at the N-terminus of the mature protein, and the reacti…
- **Diseases (Open Targets)**: hereditary antithrombin deficiency (0.851); venous thromboembolism (0.706); Venous thrombosis (0.683); deep vein thrombosis (0.656); blood coagulation disease (0.654)
- **Europe PMC papers**: 3200
- **Why important**: SERPINC1 is a central functional anchor because it is present in the primary blood-microparticle and coagulation terms (GO:CC blood microparticle; q_global = 0.000216) and (GO:BP regulation of coagulation; q_global = 0.00881). It encodes antithrombin, a plasma serine-protease inhibitor that regulates coagulation, has established associations with hereditary antithrombin deficiency and venous thromboembolic disease, and is linked by STRING to AHSG and GC. Its network position connects the coagulation interpretation to the known plasma-protein core in (hu.MAP huMAP3_15040.1).
- **Conclusion**: Established evidence supports SERPINC1 as a circulating anticoagulation component and a strong indicator of plasma-associated module biology. It does not by itself show that cervix_uterine or prostate cells express or regulate the module locally; local involvement remains a hypothesis.

#### AHSG

- **Related proteins** (co-abundance neighbors): GLIPR2 (0.94), ITIH2 (0.86); STRING partners: GC (0.959), ITIH2 (0.922), SERPINC1 (0.838)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_07265.1, huMAP3_09434.1, huMAP3_08395.1, huMAP3_09531.1, huMAP3_10101.1
- **Function (MyGene.info)**: alpha 2-HS glycoprotein. The protein encoded by this gene is a negatively-charged serum glycoprotein that is synthesized by hepatocytes. The encoded protein consists of two polypeptide chains, which are both cleaved from a proprotein encoded from a single mRNA. It is involved in several processes, including endocytosis, brain development, and the formation of bone tissue. Defects in this gene are a cause of susceptibility…
- **Diseases (Open Targets)**: alopecia - intellectual disability syndrome (0.476); otosclerosis (0.465); nephrolithiasis, calcium oxalate (0.417); calcium oxalate urolithiasis (0.416); neurodegenerative disease (0.204)
- **Europe PMC papers**: 2310
- **Why important**: AHSG is a liver- and hepatocyte-enriched secreted protein with links to acute-phase response, mineralization, endocytosis, and insulin-receptor signaling. It is present in (GO:CC blood microparticle; q_global = 0.000216) and appears in many STRING supplementary extracellular and coagulation-related categories. Its STRING links to GC, ITIH2, and SERPINC1, together with repeated membership in hu.MAP complexes (hu.MAP huMAP3_15040.1) (hu.MAP huMAP3_10678.1) (hu.MAP huMAP3_07265.1) and (hu.MAP huMAP3_09434.1) (hu.MAP huMAP3_08395.1) (hu.MAP huMAP3_09531.1) (hu.MAP huMAP3_10101.1), make it a prominent bridge between the plasma and complex evidence. Its literature volume is substantial and its disease associations include metabolic and mineralization-related conditions.
- **Conclusion**: Established evidence supports AHSG as a liver-derived extracellular scaffold and a marker of circulating plasma material. A local structural or signaling role in both tissues is not established by this module.

#### GC

- **Related proteins** (co-abundance neighbors): RSU1 (0.97), ANXA5 (0.84), SOD2 (0.82); STRING partners: AHSG (0.959), SERPINC1 (0.84)
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_15040.1, huMAP3_10678.1, huMAP3_09434.1
- **Function (MyGene.info)**: GC vitamin D binding protein. The protein encoded by this gene belongs to the albumin gene family. It is a multifunctional protein found in plasma, ascitic fluid, cerebrospinal fluid and on the surface of many cell types. It binds to vitamin D and its plasma metabolites and transports them to target tissues. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq,…
- **Diseases (Open Targets)**: vitamin D deficiency (0.574); vitamin deficiency (0.552); chronic obstructive pulmonary disease (0.499); squamous cell carcinoma (0.339); central nervous system cancer (0.334)
- **Europe PMC papers**: 363974
- **Why important**: GC is a liver-enriched secreted vitamin-D-binding protein with functions in vitamin-D and nutrient transport. It is present in (GO:CC blood microparticle; q_global = 0.000216), connects to RSU1, ANXA5, and SOD2 in the co-abundance graph, and has STRING links to AHSG and SERPINC1. It recurs in hu.MAP complexes (hu.MAP huMAP3_15040.1), (hu.MAP huMAP3_10678.1), and (hu.MAP huMAP3_09434.1), while its very large literature base and disease associations involving vitamin deficiency and cancer make it an informative marker of systemic rather than tissue-restricted biology.
- **Conclusion**: Established evidence supports GC as a circulating transport protein that helps define the plasma-associated character of the module. The co-abundance link to membrane and stress-related genes should be treated as contextual association, not proof of direct GC action in either tissue.

#### APOE

- **Related proteins** (co-abundance neighbors): ANXA4 (0.95), ITIH2 (0.86), ANXA6 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: apolipoprotein E. The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hype…
- **Diseases (Open Targets)**: hyperlipoproteinemia type 3 (0.803); coronary artery disorder (0.782); lipoprotein glomerulopathy (0.759); Alzheimer disease (0.696); familial hypercholesterolemia (0.651)
- **Europe PMC papers**: 74272
- **Why important**: APOE has the strongest network connectivity among the lipid-associated genes and links ANXA4, ITIH2, and ANXA6. It is secreted to blood, enriched in liver and brain-related contexts, and has annotations for lipid transport, triglyceride metabolism, receptor-mediated endocytosis, and reactive-oxygen responses. It appears in the primary terms (GO:CC blood microparticle; q_global = 0.000216) and (GO:BP regulation of coagulation; q_global = 0.00881) and across many supplementary extracellular, vesicle, and protein-lipid categories. Its extensive literature and associations with dyslipidemia, coronary disease, lipoprotein disorders, and Alzheimer disease make it a biologically informative hub.
- **Conclusion**: Established evidence supports APOE as a lipid-transport and extracellular-vesicle component that may connect plasma composition with membrane biology. Its presence does not establish a tissue-specific disease mechanism in cervix_uterine or prostate.

#### ANXA5

- **Related proteins** (co-abundance neighbors): GC (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A5. The Annexin 5 gene spans 29 kb containing 13 exons, and encodes a single transcript of approximately 1.6 kb and a protein product with a molecular weight of about 35 kDa.The protein encoded by this gene belongs to the annexin family of calcium-dependent phospholipid binding proteins some of which have been implicated in membrane-related events along exocytotic and endocytotic pathways. Annexin 5 i…
- **Diseases (Open Targets)**: habitual spontaneous abortion (0.370); complication (0.124); herpes zoster (0.124); nervous system disorder (0.124); neoplasm (0.118)
- **Europe PMC papers**: 3276
- **Why important**: ANXA5 is the clearest annexin representative because it occurs in all primary enrichment terms (4 globally significant GO/KEGG terms, q_global 0.000216–0.0404; see the table). It is detected in both tissues by HPA, has annotations for calcium-dependent membrane events, inhibition of coagulation, and apoptosis-related processes, and is linked to GC in the module graph. Its membership in the blood-microparticle, coagulation, zymogen-granule, and extracellular-vesicle evidence provides a plausible interface between circulating material and local membrane biology. Its literature volume and disease associations are substantial.
- **Conclusion**: Established evidence supports ANXA5 as a calcium-dependent membrane and anticoagulation-associated protein consistent with the module function. A role in generating or responding to vesicles in both tissues is plausible but remains a hypothesis from co-abundance data.

#### ANXA4

- **Related proteins** (co-abundance neighbors): APOE (0.95), LHPP (0.92), GLIPR2 (0.84), SERPINC1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A4. Annexin IV (ANX4) belongs to the annexin family of calcium-dependent phospholipid binding proteins. Although their functions are still not clearly defined, several members of the annexin family have been implicated in membrane-related events along exocytotic and endocytotic pathways. ANX4 has 45 to 59% identity with other members of its family and shares a similar size and exon-intron organization…
- **Diseases (Open Targets)**: atrial fibrillation (0.445); Abnormality of the skeletal system (0.385); dentures (0.301); neurodegenerative disease (0.268); placental abruption (0.235)
- **Europe PMC papers**: 1395
- **Why important**: ANXA4 has the highest network connectivity in the supplied graph and links APOE, LHPP, GLIPR2, and SERPINC1. It occurs in the coagulation and both zymogen-granule terms (GO:BP regulation of coagulation; q_global = 0.00881) (GO:CC zymogen granule membrane; q_global = 0.0236) (GO:CC zymogen granule; q_global = 0.0404), is detected in both tissues, and is enriched in epithelial or duct-associated cell contexts including cholangiocytes and pancreatic duct cells. Its annexin-family function supports membrane trafficking and calcium-dependent phospholipid binding, while its substantial literature and disease associations provide broader biological context.
- **Conclusion**: Established evidence supports ANXA4 as a local membrane-associated component that may connect epithelial or secretory biology with the plasma-associated core. The proposed bridge to coagulation or extracellular vesicles is supported by enrichment context but not demonstrated as a direct mechanism.

## Module 6

**Tissue pair**: cervix_uterine and prostate  
**Genes (6)**: ALB, APOH, QDPR, HBA1, ALAD, MYLK

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established shared pathway annotation. Its biological pattern is more consistent with a mixed plasma, erythrocyte, heme-related, and tissue-structural signal than with a single coherent intracellular pathway. ALB and APOH represent circulating plasma proteins involved in transport, lipoprotein biology, coagulation, and hemostasis. HBA1 represents erythrocytes and oxygen transport, while ALAD represents heme biosynthesis. MYLK provides a smooth-muscle and contractility connection. The strongest direct network relationship is ALB-APOH, and the supplementary STRING result (STRING PMID (2016) Supernatant protein biomarkers of red blood cell storage hemolysis as determined through an absolute quantification proteomics technology.; within-query FDR = 0.0442) links APOH, ALB, HBA1, and ALAD to a red-blood-cell-storage hemolysis biomarker context. This supports a blood or hemolysis-related interpretation, but does not establish a formally enriched pathway.

**Cell composition.** The module is strongly compatible with a circulating or blood-derived component rather than being specific to cervix or prostate tissue. HPA identifies liver enrichment for several genes and hepatocyte enrichment for several genes, with APOH and ALB annotated as secreted to blood. HBA1 is associated with erythrocytes, bone marrow, lymphoid tissue, and several blood-cell contexts. Some genes also show neutrophil, eosinophil, basophil, or plasmacytoid dendritic-cell associations. Protein detection is absent for all module genes in cervix and present for only one gene in prostate, with ALAD being detected in prostate. Therefore, the shared co-abundance signal may reflect plasma carryover, red-cell or hemolysis-related material, or shared vascular and stromal components. MYLK and ALAD leave open a possible local smooth-muscle or heme-related contribution, but the HPA evidence does not support broad local protein production by the module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains one high-confidence pair within the module, ALB-APOH, indicating that this relationship is already known rather than newly inferred here. The supplementary STRING term (STRING PMID (2016) Supernatant protein biomarkers of red blood cell storage hemolysis as determined through an absolute quantification proteomics technology.; within-query FDR = 0.0442) connects APOH, ALB, HBA1, and ALAD with red-blood-cell-storage hemolysis biomarkers; it is supportive context only and is not global enrichment evidence. hu.MAP complex (hu.MAP huMAP3_15040.1) contains APOH, ALB, and HBA1, but the complex is broad and includes many plasma, complement, coagulation, lipoprotein, and hemoglobin-related proteins. Thus, the complex supports a shared plasma or blood-associated molecular context, while the sparse STRING connectivity argues against a densely established physical complex involving the entire module. MYLK, QDPR, and ALAD have no listed STRING partners or hu.MAP complex membership within the supplied evidence.

**STRING interactions (score >= 0.7)**: 1 of 15 gene pairs: ALB–APOH (0.933)
**STRING functional enrichment (supplementary, within-query FDR)**: PMID (2016) Supernatant protein biomarkers of red blood cell storage hemolysis as determined through an absolute quantification proteomics technology. (FDR = 0.0442, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_15040.1 (APOH, ALB, HBA1; 3/64)

### Novelty

This module should not be described as a new biological pathway or a newly discovered protein complex. Its central ALB-APOH relationship is already represented in STRING, and APOH, ALB, and HBA1 occur together in hu.MAP complex (hu.MAP huMAP3_15040.1). The absence of additional STRING or hu.MAP relationships is not proof of novelty. A more defensible claim is that this particular co-abundance configuration may be data-specific or tissue-pair specific, especially because it combines plasma, erythrocyte, heme, metabolic, and smooth-muscle signals. That possibility requires independent replication, control for blood contamination and cellular composition, and comparison with matched tissue cohorts before it can be considered a novel biological finding.

**Hypothesis.** Hypothesis: the shared cervix-prostate module primarily records variation in circulating plasma and erythrocyte-derived material, potentially including low-grade hemolysis or vascular leakage, with a secondary contribution from local smooth-muscle or stromal biology. In this model, ALB and APOH form the plasma-associated anchor, HBA1 reports erythrocyte material, and ALAD reports heme-related cellular content or oxidative stress. MYLK could reflect contractile stromal or smooth-muscle context, while QDPR could reflect a broader metabolic or hepatocyte-like signal. This is a mechanistic interpretation to test, not an established causal pathway.

### Important genes

#### ALB

- **Related proteins** (co-abundance neighbors): MYLK (0.86), HBA1; HBA2 (0.83), APOH (0.81); STRING partners: APOH (0.933)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: albumin. This gene encodes the most abundant protein in human blood. This protein functions in the regulation of blood plasma colloid osmotic pressure and acts as a carrier protein for a wide range of endogenous molecules including hormones, fatty acids, and metabolites, as well as exogenous drugs. Additionally, this protein exhibits an esterase-like activity with broad substrate specificity. The encoded p…
- **Diseases (Open Targets)**: congenital analbuminemia (0.678); hyperthyroxinemia (0.649); hyperthyroxinemia, familial dysalbuminemic (0.554); hyperthyroidism (0.429); chronic kidney disease (0.409)
- **Europe PMC papers**: 29730
- **Why important**: ALB is a high-connectivity module gene and is directly linked to APOH by a high-confidence STRING relationship. It is the most abundant blood protein, functions as a broad plasma carrier, is secreted to blood, and is liver and hepatocyte enriched by HPA. It has the largest literature volume in the module and extensive disease annotation. Its absence from cervix and prostate protein detection makes it especially important for evaluating plasma contribution or sample contamination.
- **Conclusion**: Established: ALB is a circulating liver-derived carrier protein and a central anchor of the known plasma-associated part of the module. Hypothesis: its co-abundance here mainly reflects variable plasma content rather than a cervix-prostate-specific ALB program.

#### APOH

- **Related proteins** (co-abundance neighbors): ALAD (0.86), QDPR (0.84), ALB (0.81); STRING partners: ALB (0.933)
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location Golgi apparatus; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: apolipoprotein H. Apolipoprotein H, also known as beta-2-glycoprotein I, is a component of circulating plasma lipoproteins. It has been implicated in a variety of physiologic pathways including lipoprotein metabolism, coagulation, hemostasis, and the production of antiphospholipid autoantibodies. APOH may be a required cofactor for anionic phospholipid binding by the antiphospholipid autoantibodies found in sera of…
- **Diseases (Open Targets)**: atrial fibrillation (0.549); metabolic syndrome (0.502); Hypercholesterolemia (0.501); aortic stenosis (0.473); familial lipoprotein lipase deficiency (0.460)
- **Europe PMC papers**: 3121
- **Why important**: APOH has high module connectivity and is connected to ALB by the only high-confidence STRING pair. It is secreted to blood, liver and hepatocyte enriched, and implicated in lipoprotein metabolism, coagulation, hemostasis, and antiphospholipid autoantibody biology. It is also present in the supplementary hemolysis-related STRING term (STRING PMID (2016) Supernatant protein biomarkers of red blood cell storage hemolysis as determined through an absolute quantification proteomics technology.; within-query FDR = 0.0442) and has substantial literature and disease associations.
- **Conclusion**: Established: APOH is a plasma-associated hemostatic and lipoprotein-related protein with a known relationship to ALB. Hypothesis: APOH helps define the circulating or vascular component of this module and may track blood-derived material in both tissues.

#### HBA1

- **Related proteins** (co-abundance neighbors): none; STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: huMAP3_15040.1
- **Function (MyGene.info)**: hemoglobin subunit alpha 1. The human alpha globin gene cluster located on chromosome 16 spans about 30 kb and includes seven loci: 5'- zeta - pseudozeta - mu - pseudoalpha-1 - alpha-2 - alpha-1 - theta - 3'. The alpha-2 (HBA2) and alpha-1 (HBA1) coding sequences are identical. These genes differ slightly over the 5' untranslated regions and the introns, but they differ significantly over the 3' untranslated regions. Two alp…
- **Diseases (Open Targets)**: alpha thalassemia spectrum (0.758); hemoglobin H disease (0.755); hemoglobin M disease (0.735); Heinz body anemia (0.698); primary familial polycythemia due to EPO receptor mutation (0.689)
- **Europe PMC papers**: 4551
- **Why important**: HBA1 is the clearest erythrocyte marker in the module. HPA associates it with erythrocytes, bone marrow, lymphoid tissue, and multiple blood-cell contexts, while its annotation supports oxygen, carbon-dioxide, nitric-oxide, and oxidative-stress biology. It participates in hu.MAP complex (hu.MAP huMAP3_15040.1) with ALB and APOH and appears in the supplementary hemolysis-related term (STRING PMID (2016) Supernatant protein biomarkers of red blood cell storage hemolysis as determined through an absolute quantification proteomics technology.; within-query FDR = 0.0442), despite having no listed direct STRING partner in the module.
- **Conclusion**: Established: HBA1 is an erythrocyte-associated hemoglobin gene and supports a blood-derived interpretation. Hypothesis: its presence indicates red-cell carryover or hemolysis more likely than a locally produced cervix or prostate signal.

#### MYLK

- **Related proteins** (co-abundance neighbors): HBA1; HBA2 (0.87), ALB (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Actin filaments; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: myosin light chain kinase. This gene, a muscle member of the immunoglobulin gene superfamily, encodes myosin light chain kinase which is a calcium/calmodulin dependent enzyme. This kinase phosphorylates myosin regulatory light chains to facilitate myosin interaction with actin filaments to produce contractile activity. This gene encodes both smooth muscle and nonmuscle isoforms. In addition, using a separate promoter in an …
- **Diseases (Open Targets)**: aortic aneurysm, familial thoracic 7 (0.767); familial thoracic aortic aneurysm and aortic dissection (0.710); megacystis-microcolon-intestinal hypoperistalsis syndrome 1 (0.617); megacystis-microcolon-intestinal hypoperistalsis syndrome (0.597); Rare genetic vascular disease (0.483)
- **Europe PMC papers**: 10503
- **Why important**: MYLK connects the module to calcium-dependent myosin regulation, actin interaction, smooth-muscle contraction, and cell migration. It has the highest connectivity tier after ALB and APOH, is tissue enhanced in seminal vesicle and smooth muscle, and shows associations with peritubular myoid cells, platelets, and myoepithelial or hepatic stromal cell types. It has a substantial literature and disease association profile, although it has no listed STRING or hu.MAP relationship here.
- **Conclusion**: Established: MYLK is a contractility and cytoskeletal regulator with relevant smooth-muscle and stromal annotations. Hypothesis: it may represent a local structural or vascular component layered onto an otherwise blood-associated module, but the current network evidence is insufficient to make that interpretation definitive.

#### ALAD

- **Related proteins** (co-abundance neighbors): APOH (0.86); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aminolevulinate dehydratase. The ALAD enzyme is composed of 8 identical subunits and catalyzes the condensation of 2 molecules of delta-aminolevulinate to form porphobilinogen (a precursor of heme, cytochromes and other hemoproteins). ALAD catalyzes the second step in the porphyrin and heme biosynthetic pathway; zinc is essential for enzymatic activity. ALAD enzymatic activity is inhibited by lead and a defect in the ALAD str…
- **Diseases (Open Targets)**: porphyria due to ALA dehydratase deficiency (0.751); Acute hepatic porphyria (0.716); neurodegenerative disease (0.237); hereditary disease (0.191); renal cell carcinoma (0.081)
- **Europe PMC papers**: 1931
- **Why important**: ALAD is the module's heme-biosynthetic enzyme and is the only gene reported as detected by HPA immunohistochemistry in prostate. It is liver enhanced, associated with erythrocyte progenitors, and appears in the supplementary hemolysis-related term (STRING PMID (2016) Supernatant protein biomarkers of red blood cell storage hemolysis as determined through an absolute quantification proteomics technology.; within-query FDR = 0.0442). Its direct network link to APOH and its established role in porphyrin and heme production connect the blood-associated signal to a plausible heme or oxidative-stress process. Its disease literature includes acute hepatic porphyria and ALAD deficiency.
- **Conclusion**: Established: ALAD catalyzes an early step in heme biosynthesis and has a prostate protein-detection signal in the supplied HPA evidence. Hypothesis: ALAD may indicate heme-related cellular material or oxidative stress and could provide a limited local component, but this does not establish a prostate specific mechanism.

## Module 7

**Tissue pair**: cervix_uterine and prostate  
**Genes (15)**: BCLAF1, CLTC, DDX21, DHX9, ADAR, EDC4, HNRNPL, HNRNPR, MYBBP1A, PRPF4, RECQL, SEC16A, U2SURP, DARS1, UBTF

### Function

The strongest interpretation is a conserved nuclear RNA and nucleic-acid regulation module. The primary evidence is the broad enrichment for nucleic acid metabolic processes (GO:BP nucleic acid metabolic process; q_global = 0.0112), nucleic acid binding (GO:MF nucleic acid binding; q_global = 0.0123), RNA binding (GO:MF RNA binding; q_global = 0.0157), RNA metabolic processes (GO:BP RNA metabolic process; q_global = 0.0232), and RNA processing (GO:BP RNA processing; q_global = 0.0274). The double-stranded RNA-binding term (GO:MF double-stranded RNA binding; q_global = 0.0431) further supports coordinated handling of structured RNA, particularly through ADAR and the RNA helicases DHX9 and DDX21. The module also contains spliceosome-associated and RNA-binding proteins, including HNRNPL, HNRNPR, PRPF4, U2SURP, and BCLAF1, together with nucleolar and ribosomal-transcription regulators such as MYBBP1A and UBTF. The osteoblast-differentiation term (GO:BP osteoblast differentiation; q_global = 0.0228) is globally significant, but it is represented by a smaller subset and overlaps with genes that also have broader RNA, nucleolar, transcriptional, or trafficking functions. It should therefore be treated as a possible context-dependent association rather than the primary module function. The overall pattern is most consistent with coordinated RNA processing, RNA surveillance or remodeling, nucleolar activity, and gene-expression control.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and the proteins are intracellular, with locations including nucleoplasm, nucleoli, nuclear speckles, cytosol, endosomes, lysosomes, Golgi, and cytoplasmic bodies. HPA reports low tissue specificity for nearly all genes, low immune-cell specificity for the module, and no enriched blood-cell category. Protein detection is broad in both cervix and prostate, with only RECQL lacking detection in prostate. Some genes show cell-type-enhanced expression, including keratinocyte-associated DDX21, glial-associated HNRNPL and EDC4, and neutrophil-associated ADAR and CLTC, but the module as a whole does not look like a blood-cell contamination signature. Its broad tissue distribution and concentration on core RNA-processing machinery indicate that shared housekeeping or broadly deployed epithelial and nucleoplasmic biology is a plausible explanation for its conservation across these tissues.

**GO/KEGG enrichment**: 7 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP nucleic acid metabolic process | 0.0112 | ADAR, BCLAF1, DARS1, DDX21, DHX9, EDC4, HNRNPL, HNRNPR, MYBBP1A, PRPF4, RECQL, U2SURP, UBTF |
| GO:MF nucleic acid binding | 0.0123 | ADAR, BCLAF1, CLTC, DARS1, DDX21, DHX9, HNRNPL, HNRNPR, MYBBP1A, PRPF4, RECQL, U2SURP, UBTF |
| GO:MF RNA binding | 0.0157 | ADAR, BCLAF1, CLTC, DARS1, DDX21, DHX9, HNRNPL, HNRNPR, MYBBP1A, PRPF4, U2SURP, UBTF |
| GO:BP osteoblast differentiation | 0.0228 | ADAR, CLTC, DDX21, DHX9, MYBBP1A |
| GO:BP RNA metabolic process | 0.0232 | ADAR, BCLAF1, DARS1, DDX21, DHX9, EDC4, HNRNPL, HNRNPR, MYBBP1A, PRPF4, U2SURP, UBTF |
| GO:BP RNA processing | 0.0274 | ADAR, BCLAF1, DDX21, DHX9, HNRNPL, HNRNPR, PRPF4, U2SURP |
| GO:MF double-stranded RNA binding | 0.0431 | ADAR, CLTC, DDX21, DHX9 |

### STRING and hu.MAP

STRING independently supports the RNA-centered interpretation through supplementary enrichment for RNA metabolism, nucleic-acid binding, RNA binding, RNA processing, and related gene-expression categories (STRING Process RNA metabolic process; within-query FDR = 0.0022) through (STRING Process Gene expression; within-query FDR = 0.0478). The strongest known relationships include ADAR with DHX9, DDX21 with DHX9 and MYBBP1A, DHX9 with HNRNPL and HNRNPR, and HNRNPL with HNRNPR. These links provide external support for a real interaction-rich RNA-regulatory core, although STRING enrichment is supplementary here and its reported FDR is not a global correction across module-term tests. The module also contains known hu.MAP associations. HNRNPL, HNRNPR, and ADAR co-occur in a high-confidence heterogeneous nuclear ribonucleoprotein complex (hu.MAP huMAP3_10625.1). HNRNPL and HNRNPR recur across several additional RNA-protein complex models (hu.MAP huMAP3_07225.1), (hu.MAP huMAP3_06093.1), (hu.MAP huMAP3_09654.1), (hu.MAP huMAP3_07581.1), and (hu.MAP huMAP3_10659.1). SEC16A and CLTC recur in trafficking and clathrin-related complexes (hu.MAP huMAP3_07405.1), (hu.MAP huMAP3_08744.1), (hu.MAP huMAP3_10762.1), (hu.MAP huMAP3_12918.1), and (hu.MAP huMAP3_12394.1). These complexes generally contain only a subset of the module, so they support established substructures rather than proving that the entire co-abundance module is one physical complex. The module therefore appears to combine a well-supported RNA-processing core with a smaller vesicle-trafficking and endomembrane-associated component.

**STRING interactions (score >= 0.7)**: 9 of 105 gene pairs: ADAR–DHX9 (0.922); BCLAF1–U2SURP (0.797); DDX21–DHX9 (0.908); DDX21–HNRNPR (0.73); DDX21–MYBBP1A (0.963); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); HNRNPL–HNRNPR (0.961); MYBBP1A–UBTF (0.768)
**STRING functional enrichment (supplementary, within-query FDR)**: Process RNA metabolic process (FDR = 0.0022, 11 genes); Process Nucleic acid metabolic process (FDR = 0.0022, 12 genes); Function Nucleic acid binding (FDR = 0.0098, 13 genes); Function RNA binding (FDR = 0.0098, 12 genes); Process Osteoblast differentiation (FDR = 0.0148, 5 genes); Process RNA processing (FDR = 0.0173, 8 genes); Function Double-stranded RNA binding (FDR = 0.0227, 4 genes); Function DNA binding (FDR = 0.0252, 7 genes); RCTM Metabolism of RNA (FDR = 0.0273, 8 genes); COMPARTMENTS Chromosome (FDR = 0.034, 7 genes); Process mRNA metabolic process (FDR = 0.0378, 7 genes); Process Gene expression (FDR = 0.0478, 10 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPR, HNRNPL, ADAR; 3/57); huMAP3_07405.1 (SEC16A, CLTC; 2/3); huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_08744.1 (SEC16A, CLTC; 2/20); huMAP3_07581.1 (HNRNPR, HNRNPL; 2/21); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_10762.1 (SEC16A, CLTC; 2/62); huMAP3_12918.1 (SEC16A, CLTC; 2/62); huMAP3_12394.1 (SEC16A, CLTC; 2/98)

### Novelty

The biological theme is not, by itself, a new discovery. RNA binding, RNA processing, spliceosomal activity, nucleolar regulation, and clathrin-associated trafficking are established functions, and several module relationships are already represented in STRING or hu.MAP. Conversely, the specific conserved co-abundance pattern across cervix and prostate may be a new systems-level observation, because co-abundance across tissues is not equivalent to a previously catalogued physical interaction or complex. The available evidence does not establish that the module is novel at the gene-function level, nor does absence of some module pairs from STRING or hu.MAP prove novelty. A defensible conclusion is that this is a potentially novel tissue-pair co-abundance configuration built largely from known RNA-regulatory biology. Its novelty would require validation in independent cohorts, replication across platforms, and comparison with existing tissue co-expression or proteomic networks.

**Hypothesis.** Hypothesis: the module reflects a conserved intracellular RNA-homeostasis program shared by cervix and prostate cells. In this model, DHX9 and DDX21 remodel structured RNA and coordinate with ADAR-mediated RNA editing; HNRNPL and HNRNPR organize RNA-protein assemblies and influence transcript processing; PRPF4 and U2SURP support spliceosomal processing; BCLAF1 and MYBBP1A connect RNA handling with transcriptional or nucleolar stress responses; and UBTF supports ribosomal RNA transcription. EDC4 may connect RNA turnover with cytoplasmic decapping bodies, while SEC16A and CLTC may represent a linked trafficking or compartmental component rather than the central mechanism. The osteoblast-differentiation association may indicate that this RNA program is reused during differentiation or tissue remodeling, but the module data alone do not demonstrate an osteoblast-specific mechanism. This hypothesis should be tested by perturbing the RNA-core genes and measuring splicing, RNA editing, nucleolar activity, and cell-state or differentiation responses in relevant cervical and prostate models.

### Important genes

#### DHX9

- **Related proteins** (co-abundance neighbors): SEC16A (0.89), DDX21 (0.87), ADAR (0.86), EDC4 (0.86), HNRNPR (0.81), BCLAF1 (0.80); STRING partners: ADAR (0.922), DDX21 (0.908), HNRNPL (0.901), HNRNPR (0.909)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is the leading network hub in the module and connects directly to ADAR, DDX21, HNRNPL, HNRNPR, EDC4, and SEC16A. It appears in every primary enrichment term (GO:BP nucleic acid metabolic process; q_global = 0.0112) through (GO:MF double-stranded RNA binding; q_global = 0.0431) and every supplementary STRING term (STRING Process RNA metabolic process; within-query FDR = 0.0022) through (STRING Process Gene expression; within-query FDR = 0.0478). Its established function as an ATP-dependent RNA and DNA-RNA helicase, together with roles in RNA processing, transcriptional regulation, and interferon-related biology, makes it a strong mechanistic anchor. It has substantial literature support and disease associations involving intellectual disability and neurodegenerative or infectious disease contexts.
- **Conclusion**: Established: DHX9 is a central RNA-remodeling factor and a highly connected member of the conserved module. Hypothesis: its hub position may allow it to coordinate the module's RNA-processing and structured-RNA activities across both tissues.

#### ADAR

- **Related proteins** (co-abundance neighbors): HNRNPL (0.88), UBTF (0.87), DHX9 (0.86); STRING partners: DHX9 (0.922)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR is present in all primary enrichment terms (GO:BP nucleic acid metabolic process; q_global = 0.0112) through (GO:MF double-stranded RNA binding; q_global = 0.0431), including double-stranded RNA binding (GO:MF double-stranded RNA binding; q_global = 0.0431), and is linked in STRING to DHX9 and in hu.MAP to an hnRNP-containing complex (hu.MAP huMAP3_10625.1). Its established enzymatic activity converts adenosine to inosine in RNA and can destabilize double-stranded RNA. It is detected in both tissues and has strong disease associations with Aicardi-Goutieres syndrome, dyschromatosis, and ADAR-related interferonopathy, as well as a substantial literature base.
- **Conclusion**: Established: ADAR provides a specific RNA-editing and double-stranded-RNA interpretation for the module. Hypothesis: coordinated ADAR and helicase activity may tune RNA structure, editing, and innate-RNA sensing in cervical and prostate cells.

#### DDX21

- **Related proteins** (co-abundance neighbors): MYBBP1A (0.92), DHX9 (0.87), HNRNPL (0.84), PRPF4 (0.84), U2SURP (0.83); STRING partners: DHX9 (0.908), HNRNPR (0.73), MYBBP1A (0.963)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli rim, Mitotic chromosome; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExD-box helicase 21. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to b…
- **Diseases (Open Targets)**: neurodegenerative disease (0.396); colorectal carcinoma (0.112); cancer (0.099); gastric cancer (0.098); hepatocellular carcinoma (0.095)
- **Europe PMC papers**: 1867
- **Why important**: DDX21 is a highly connected module member linking MYBBP1A, DHX9, HNRNPL, PRPF4, and U2SURP. It occurs in all primary enrichment terms (GO:BP nucleic acid metabolic process; q_global = 0.0112) through (GO:MF double-stranded RNA binding; q_global = 0.0431) and has strong STRING support with DHX9 and MYBBP1A. Its established DEAD-box helicase function is compatible with RNA structure remodeling, ribosome and spliceosome assembly, cellular growth, and gene regulation. HPA shows enhanced expression in basal and suprabasal keratinocytes, which is relevant to the epithelial context, and it has substantial literature and cancer-related disease associations.
- **Conclusion**: Established: DDX21 is a nucleolar and RNA-helicase component that connects the module's RNA-processing and transcriptional features. Hypothesis: its epithelial cell-state association may help explain why this module is conserved in tissues with epithelial compartments.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): ADAR (0.88), DDX21 (0.84), MYBBP1A (0.82), BCLAF1 (0.82), HNRNPR (0.80); STRING partners: DHX9 (0.901), HNRNPR (0.961)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_07581.1, huMAP3_10659.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a highly connected RNA-binding node linked to ADAR, DDX21, MYBBP1A, BCLAF1, and HNRNPR. It participates in the primary RNA and nucleic-acid terms (GO:BP nucleic acid metabolic process; q_global = 0.0112), (GO:MF nucleic acid binding; q_global = 0.0123), (GO:MF RNA binding; q_global = 0.0157), (GO:BP RNA metabolic process; q_global = 0.0232), and (GO:BP RNA processing; q_global = 0.0274), and it is repeatedly represented in hu.MAP hnRNP complexes (hu.MAP huMAP3_10625.1), (hu.MAP huMAP3_07225.1), (hu.MAP huMAP3_06093.1), (hu.MAP huMAP3_09654.1), (hu.MAP huMAP3_07581.1), and (hu.MAP huMAP3_10659.1). Its established role in hnRNP assembly, mRNA processing, and alternative splicing gives direct functional meaning to the module. It is detected in both tissues, has broad expression, and has a substantial literature and disease-association record.
- **Conclusion**: Established: HNRNPL is a core RNA-protein assembly and transcript-processing component. Hypothesis: its repeated complex membership may make it a structural bridge between the ADAR-helicase submodule and spliceosomal regulation.

#### PRPF4

- **Related proteins** (co-abundance neighbors): DDX21 (0.84), EDC4 (0.83), CLTC (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: pre-mRNA splicing tri-snRNP complex factor PRPF4. The protein encoded by this gene is part of a heteromeric complex that binds U4, U5, and U6 small nuclear RNAs and is involved in pre-mRNA splicing. The encoded protein also is a mitotic checkpoint protein and a regulator of chemoresistance in human ovarian cancer. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: retinitis pigmentosa (0.634); retinitis pigmentosa 70 (0.578); inherited retinal dystrophy (0.377); neurodegenerative disease (0.203); refractive error (0.083)
- **Europe PMC papers**: 461
- **Why important**: PRPF4 connects DDX21, EDC4, and CLTC in the module and appears in the primary RNA-processing terms (GO:BP nucleic acid metabolic process; q_global = 0.0112), (GO:MF nucleic acid binding; q_global = 0.0123), (GO:MF RNA binding; q_global = 0.0157), (GO:BP RNA metabolic process; q_global = 0.0232), and (GO:BP RNA processing; q_global = 0.0274). Its established role in U4, U5, and U6 small nuclear RNA-associated spliceosomal complexes provides a direct mechanistic link to pre-mRNA splicing. It is detected in both tissues and has disease associations with retinitis pigmentosa and inherited retinal dystrophy, together with literature supporting its spliceosomal and mitotic functions.
- **Conclusion**: Established: PRPF4 supports the interpretation that the module includes spliceosomal assembly and pre-mRNA processing. Hypothesis: its co-abundance with helicases and hnRNP proteins may reflect coordinated control of spliceosome-dependent transcript maturation.

## Module 8

**Tissue pair**: cervix_uterine and prostate  
**Genes (7)**: CYFIP1, EHD4, RAP1GDS1, CAST, PLEC, SERPINB5, SPTAN1

### Function

No GO/KEGG term passed global correction, so the module does not support a statistically confirmed pathway assignment from enrichment analysis. Its gene-level biology nevertheless points to a cytoskeletal and epithelial-cell organization program. SPTAN1 and PLEC are structural scaffolding proteins that connect membrane-associated and intermediate-filament systems, while CAST regulates calpain activity. EHD4 supports endocytic recycling and membrane trafficking, RAP1GDS1 regulates small-GTPase signaling, and CYFIP1 participates in WAVE-complex-dependent actin remodeling. SERPINB5 adds an epithelial, protease-regulatory and cell-proliferation-related component. The co-abundance pattern is therefore most consistent with coordinated maintenance of cell architecture, adhesion, membrane trafficking, and epithelial cell state rather than a narrowly defined biochemical pathway. This interpretation is functional and hypothesis-generating, not an enrichment claim. The shared detection of most module proteins in cervix and prostate supports biological relevance in both tissues.

**Cell composition.**  This is not predominantly a plasma-protein or secreted-protein module: only SERPINB5 has a secretome annotation, and it is described as intracellular and membrane-associated. Most genes have low tissue specificity, while PLEC and SERPINB5 show tissue-enhanced expression in skeletal muscle, esophagus, or skin. Several genes are enhanced in epithelial cell populations, especially urothelial, esophageal, ocular, or keratinocyte populations. CYFIP1 is enriched in microglia and several monocyte or myeloid dendritic-cell populations, but the remainder generally show low immune-cell specificity and SERPINB5 is not detected in immune cells. Thus, the module does not look primarily like a blood-cell module. It may instead reflect shared epithelial or structural cell content, with possible contribution from common cell-state or sample-composition effects. EHD4 is not detected by IHC in either tissue and RAP1GDS1 is not detected in prostate, so transcript-level co-abundance should not automatically be interpreted as uniform protein abundance across both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

 STRING supports a small structural interaction core involving CAST with SPTAN1 and PLEC with SPTAN1. These are already known relationships and provide independent support for a spectrin-associated cytoskeletal component. The other module relationships are not represented by the reported high-confidence STRING interactions, so the co-abundance edges should not all be read as direct physical binding. No hu.MAP complex contains multiple module members, providing no complex-level support from that resource. Overall, the databases support a limited known interaction core embedded in a broader expression-correlation structure.

**STRING interactions (score >= 0.7)**: 2 of 21 gene pairs: CAST–SPTAN1 (0.79); PLEC–SPTAN1 (0.795)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The exact conserved co-abundance module in cervix and prostate may be a new tissue-pair observation, but the underlying biology is not wholly new. SPTAN1, PLEC, CAST, CYFIP1, EHD4, RAP1GDS1, and SERPINB5 each have established cellular or disease-related annotations, and STRING already recognizes part of the structural connection. Conversely, the lack of a hu.MAP multi-member complex and the sparse STRING representation mean that the specific cross-tissue co-abundance arrangement is not strongly documented by those resources. This supports cautious novelty as a systems-level association, not a claim that the genes or their individual functions are newly discovered. Absence from STRING or hu.MAP alone cannot establish novelty.

**Hypothesis.** Hypothesis: a shared epithelial or epithelial-like cell state in cervix and prostate increases coordinated expression of cytoskeletal scaffolds, protease regulation, membrane recycling, and small-GTPase-controlled actin remodeling. In this model, SPTAN1 and PLEC form a structural backbone, CAST modulates calpain-dependent remodeling, EHD4 supports recycling of membrane components, RAP1GDS1 tunes signaling connected to cytoskeletal organization, CYFIP1 links signaling to actin polymerization, and SERPINB5 stabilizes an epithelial differentiation or proliferation state through protease control. The hypothesis predicts that the module will track epithelial architecture, adhesion, or tissue integrity more closely than circulating immune-cell abundance. It requires validation with cell-resolved expression, protein measurements, and perturbation experiments.

### Important genes

#### SPTAN1

- **Related proteins** (co-abundance neighbors): PLEC (0.84), CAST (0.82); STRING partners: CAST (0.79), PLEC (0.795)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Microtubules; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: spectrin alpha, non-erythrocytic 1. Spectrins are a family of filamentous cytoskeletal proteins that function as essential scaffold proteins that stabilize the plasma membrane and organize intracellular organelles. Spectrins are composed of alpha and beta dimers that associate to form tetramers linked in a head-to-head arrangement. This gene encodes an alpha spectrin that is specifically expressed in nonerythrocytic cells. The encod…
- **Diseases (Open Targets)**: developmental and epileptic encephalopathy, 5 (0.749); developmental delay with or without epilepsy (0.681); spastic paraplegia 91, autosomal dominant, with or without cerebellar ataxia (0.681); infantile spasms (0.651); genetic developmental and epileptic encephalopathy (0.651)
- **Europe PMC papers**: 1422
- **Why important**: SPTAN1 is a central connector in the module and links both PLEC and CAST. Its established role as a non-erythrocytic spectrin scaffold fits the proposed membrane and cytoskeletal organization function. It is detected in both tissues, has extensive literature, and has well-established developmental and neurological disease associations. The direct STRING relationships reinforce its importance as the best-supported structural hub.
- **Conclusion**: Established evidence supports SPTAN1 as a broadly expressed cytoskeletal scaffold and as part of the known interaction core. It is plausible, but not proven, that SPTAN1 organizes the shared tissue module in these samples.

#### PLEC

- **Related proteins** (co-abundance neighbors): SPTAN1 (0.84), SERPINB5 (0.80); STRING partners: SPTAN1 (0.795)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Intermediate filaments, Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: plectin. Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture…
- **Diseases (Open Targets)**: epidermolysis bullosa simplex 5B, with muscular dystrophy (0.796); epidermolysis bullosa simplex 5A, Ogna type (0.775); autosomal recessive limb-girdle muscular dystrophy type 2Q (0.768); epidermolysis bullosa simplex 5C, with pyloric atresia (0.755); epidermolysis bullosa simplex with nail dystrophy (0.695)
- **Europe PMC papers**: 2578
- **Why important**: PLEC is a central connector with links to SPTAN1 and SERPINB5. Its plakin architecture interlinks cytoskeletal systems and supports tissue integrity, cell shape, and organelle positioning. HPA evidence places it in a tissue-enhanced skeletal-muscle context and in urothelial cells, while its disease associations include epidermolysis bullosa and muscular-dystrophy phenotypes. Its extensive literature and direct relationship with SPTAN1 make it a strong candidate for the structural arm of the module.
- **Conclusion**: Established evidence identifies PLEC as a major cytolinker relevant to epithelial and tissue integrity. Its role as the module's structural bridge is a supported interpretation, whereas a specific cervix-prostate mechanism remains hypothetical.

#### SERPINB5

- **Related proteins** (co-abundance neighbors): PLEC (0.80), RAP1GDS1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Vesicles; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serpin family B member 5. Predicted to enable serine-type endopeptidase inhibitor activity. Predicted to be involved in negative regulation of endopeptidase activity. Predicted to act upstream of or within several processes, including extracellular matrix organization; prostate gland morphogenesis; and regulation of epithelial cell proliferation. Located in cytoplasm. Biomarker of hepatocellular carcinoma. [provided by All…
- **Diseases (Open Targets)**: Umbilical hernia (0.167); breast carcinoma (0.122); neoplasm (0.119); breast cancer (0.111); lung adenocarcinoma (0.109)
- **Europe PMC papers**: 2277
- **Why important**: SERPINB5 connects PLEC with RAP1GDS1 and is detected in both tissues. It is tissue-enhanced in esophagus and skin and is enriched across several epithelial cell populations, matching the strongest composition signal in the module. Its annotated serine-protease inhibitor activity, links to extracellular-matrix organization and epithelial proliferation, disease associations with cancer and hernia, and substantial literature make it an important candidate for coupling epithelial state to structural remodeling.
- **Conclusion**: Established evidence supports SERPINB5 as an epithelial and protease-regulatory marker that may explain part of the shared tissue signal. Its proposed role in coordinating the module with cytoskeletal remodeling is a hypothesis rather than a demonstrated interaction.

#### EHD4

- **Related proteins** (co-abundance neighbors): CYFIP1 (0.82), RAP1GDS1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EH domain containing 4. Enables cadherin binding activity. Involved in endocytic recycling and protein homooligomerization. Located in endoplasmic reticulum and recycling endosome membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.400); hypertensive disorder (0.296); Increased blood pressure (0.183); hepatocellular carcinoma (0.075); male infertility with azoospermia or oligozoospermia due to single gene mutation (0.062)
- **Europe PMC papers**: 716
- **Why important**: EHD4 occupies a connector position between CYFIP1 and RAP1GDS1 and is annotated for endocytosis and endocytic recycling. Its enhancement in esophageal apical and urothelial cells is compatible with epithelial membrane turnover. It has comparatively less literature and no reported STRING or hu.MAP support within this module, which makes it valuable as a potentially under-characterized trafficking component rather than as an established hub.
- **Conclusion**: Established evidence supports EHD4 in membrane recycling and endocytosis. Its inclusion in a shared cervix-prostate epithelial program is plausible from cell-type evidence, but the module does not establish a direct physical or regulatory link to the other genes.

#### RAP1GDS1

- **Related proteins** (co-abundance neighbors): EHD4 (0.82), SERPINB5 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rap1 GTPase-GDP dissociation stimulator 1. The smg GDP dissociation stimulator (smgGDS) protein is a stimulatory GDP/GTP exchange protein with GTPase activity (Riess et al., 1993 [PubMed 8262526]).[supplied by OMIM, Feb 2010].
- **Diseases (Open Targets)**: Alfadhel syndrome (0.430); carcinoma of liver and intrahepatic biliary tract (0.370); uterine carcinosarcoma (0.370); ovarian endometrioid adenocarcinoma with squamous differentiation (0.370); HER2 positive breast carcinoma (0.370)
- **Europe PMC papers**: 561
- **Why important**: RAP1GDS1 is a connector between EHD4 and SERPINB5 and provides a signaling bridge to processes involving mitochondrial organization, calcium regulation, smooth-muscle contraction, and myosin-filament assembly. Its enrichment in cone and rod photoreceptor cells indicates cell-type-selective expression, while its disease associations include Alfadhel syndrome and several carcinomas. Its smaller literature base makes it a useful candidate for testing rather than a firmly established module driver.
- **Conclusion**: Established evidence supports RAP1GDS1 as a signaling and localization regulator. Its role in connecting epithelial trafficking to cytoskeletal remodeling in these tissues is a hypothesis, especially because protein detection is not uniform across the paired tissues.

#### CAST

- **Related proteins** (co-abundance neighbors): SPTAN1 (0.82); STRING partners: SPTAN1 (0.79)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum, Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calpastatin
- **Diseases (Open Targets)**: peeling skin-leukonuchia-acral punctate keratoses-cheilitis-knuckle pads syndrome (0.688); Alzheimer disease (0.387); Bart-Pumphrey syndrome (0.378); cheilitis (0.373); punctate palmoplantar keratoderma (0.370)
- **Europe PMC papers**: 46701
- **Why important**: CAST is directly connected to SPTAN1 in STRING and encodes calpastatin, the endogenous inhibitor of calpain proteases. This gives the structural SPTAN1-centered core a plausible proteolytic-remodeling component. CAST is detected in both tissues, shows epithelial cell enhancement in esophageal apical and ocular epithelial cells, and has a very extensive literature base together with skin and neurodegenerative disease associations.
- **Conclusion**: Established evidence supports CAST as a calpain-regulatory protein with a known connection to SPTAN1. Its possible role in controlling tissue-specific cytoskeletal remodeling within this module is mechanistically reasonable but not demonstrated by the co-abundance data alone.

## Module 9

**Tissue pair**: cervix_uterine and prostate  
**Genes (5)**: EPS15L1, CLINT1, EPS15, ARHGAP17, USP15

### Function

The strongest functional interpretation is clathrin-mediated vesicle formation and endocytic trafficking. The primary evidence is the globally corrected GO cellular-component term (GO:CC clathrin coat; q_global = 0.0154), which contains CLINT1, EPS15, and EPS15L1 and identifies the clathrin coat. This is reinforced by the supplementary STRING terms for clathrin coat, Eps15 homology domains, ubiquitin-interacting motifs, and endocytosis (8 supplementary STRING terms; within-query FDR 0.0073–0.0464). EPS15 is annotated for receptor-mediated endocytosis, receptor recycling, Golgi-to-endosome transport, and vesicle organization. CLINT1 is annotated for clathrin-coat assembly and trafficking between the trans-Golgi network and endosomes. EPS15L1 is annotated for endocytosis and endosomal transport. ARHGAP17 contributes a possible interface with Rho-family GTPase regulation and the actin cytoskeleton, whereas USP15 contributes a possible regulatory layer through deubiquitination and transforming growth factor beta signaling. The clathrin and endocytic interpretation is established; the links to actin regulation and transforming growth factor beta signaling are plausible extensions rather than demonstrated module-level functions. No KEGG term is reported as globally significant, and the absence of additional enriched terms does not invalidate the module.

**Cell composition.** This is not a plasma or secreted-protein module: the HPA summary reports no secreted genes. The genes are generally detected in both cervix_uterine and prostate, and most have low tissue specificity, consistent with broadly distributed intracellular vesicle or signaling machinery rather than a tissue-exclusive program. At the same time, all module genes have cell-type-enhanced annotations, with several associated with neutrophils or neutrophil progenitors. USP15 is tissue enhanced in bone marrow and immune-cell enhanced in neutrophils, while CLINT1 is immune-cell enriched in basophils. These findings raise the possibility that the shared tissue signal partly reflects common immune-cell or blood-cell content, especially because the module is not composed solely of tissue-parenchymal markers. The HPA protein evidence supports presence in the sampled tissues, but does not establish that every module gene is produced by the same cell type in cervix_uterine and prostate.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC clathrin coat | 0.0154 | CLINT1, EPS15, EPS15L1 |

### STRING and hu.MAP

STRING provides high-confidence support for the EPS15–CLINT1 relationship and the EPS15–EPS15L1 relationship. The supplementary STRING results independently point to clathrin coat assembly, Eps15 homology domains, and endocytosis (8 supplementary STRING terms; within-query FDR 0.0073–0.0464). Thus, the central triplet of EPS15, EPS15L1, and CLINT1 is consistent with known endocytic machinery rather than being an unexplained statistical association. hu.MAP repeatedly places this same triplet in complexes containing AP2 components, clathrin-associated adaptors, FCHO proteins, intersectins, STON proteins, NECAP proteins, and other endocytic factors (hu.MAP huMAP3_05120.1) (hu.MAP huMAP3_05849.1) (hu.MAP huMAP3_08320.1) (hu.MAP huMAP3_09403.1) (hu.MAP huMAP3_10876.1) (hu.MAP huMAP3_10762.1) (hu.MAP huMAP3_12918.1) (hu.MAP huMAP3_12394.1) (hu.MAP huMAP3_06283.1) (hu.MAP huMAP3_08540.1) (hu.MAP huMAP3_09107.1). The complexes differ in breadth and confidence, but their recurring inclusion of the triplet supports a shared molecular context. ARHGAP17 and USP15 do not have listed STRING or hu.MAP relationships in this module, so their co-abundance connections should not be interpreted as established physical interactions.

**STRING interactions (score >= 0.7)**: 2 of 10 gene pairs: CLINT1–EPS15 (0.871); EPS15–EPS15L1 (0.99)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Clathrin coat (FDR = 0.0073, 3 genes); NetworkNeighborAL Clathrin coat, and Eps15 homology domain (FDR = 0.0077, 3 genes); Component Clathrin coat (FDR = 0.0092, 3 genes); SMART Ubiquitin-interacting motif. (FDR = 0.0158, 2 genes); SMART Eps15 homology domain (FDR = 0.0197, 2 genes); Keyword Endocytosis (FDR = 0.0278, 3 genes); NetworkNeighborAL Eps15 homology domain, and Epsin N-terminal homology (ENTH) domain (FDR = 0.029, 2 genes); COMPARTMENTS Clathrin coat of coated pit (FDR = 0.0464, 2 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05120.1 (EPS15, CLINT1, EPS15L1; 3/14); huMAP3_05849.1 (EPS15, CLINT1, EPS15L1; 3/21); huMAP3_08320.1 (EPS15, CLINT1, EPS15L1; 3/24); huMAP3_09403.1 (EPS15, CLINT1, EPS15L1; 3/26); huMAP3_10876.1 (EPS15, CLINT1, EPS15L1; 3/40); huMAP3_10762.1 (EPS15, CLINT1, EPS15L1; 3/62); huMAP3_12918.1 (EPS15, CLINT1, EPS15L1; 3/62); huMAP3_12394.1 (EPS15, CLINT1, EPS15L1; 3/98); huMAP3_06283.1 (EPS15, EPS15L1; 2/19); huMAP3_08540.1 (EPS15, EPS15L1; 2/19); huMAP3_09107.1 (EPS15, EPS15L1; 2/23)

### Novelty

The molecular function itself is not a new discovery: the roles of EPS15, EPS15L1, and CLINT1 in clathrin-associated endocytosis are already supported by GO, STRING, hu.MAP, and gene-level annotations. The potentially novel aspect is the observation that this combination of endocytic machinery, together with ARHGAP17 and USP15, forms a conserved co-abundance module across cervix_uterine and prostate. The fact sheet does not establish whether this tissue-pair pattern has been reported previously, whether it is driven by the same cell population in both tissues, or whether it is reproducible in independent cohorts. Therefore, the module can be described as a potentially useful tissue-pair co-abundance observation, not as a newly discovered molecular complex or a proven tissue-specific mechanism. Lack of listed STRING or hu.MAP relationships for ARHGAP17 and USP15 alone does not demonstrate novelty.

**Hypothesis.** Hypothesis: the shared module reflects coordinated regulation of clathrin-dependent endocytosis in a common cellular component present in cervix_uterine and prostate, potentially including infiltrating or resident neutrophil-lineage cells. EPS15, EPS15L1, and CLINT1 may organize or stabilize clathrin-coated endocytic structures; ARHGAP17 may couple this trafficking state to Rho-family GTPase and actin-cytoskeleton regulation; and USP15 may tune receptor or signaling-protein stability through deubiquitination. A testable prediction is that the module will be strongest in the same endocytic and immune-related cell populations in both tissues and will track coordinated abundance of clathrin-adaptor machinery rather than secretion of a tissue-specific product. This remains a hypothesis because the fact sheet provides co-abundance and annotation evidence, not cell-resolved causality or perturbation data.

### Important genes

#### EPS15

- **Related proteins** (co-abundance neighbors): EPS15L1 (0.84), CLINT1 (0.84), ARHGAP17 (0.82); STRING partners: CLINT1 (0.871), EPS15L1 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles, Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_05120.1, huMAP3_05849.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1, huMAP3_06283.1, huMAP3_08540.1, huMAP3_09107.1
- **Function (MyGene.info)**: epidermal growth factor receptor pathway substrate 15. This gene encodes a protein that is part of the EGFR pathway. The protein is present at clatherin-coated pits and is involved in receptor-mediated endocytosis of EGF. Notably, this gene is rearranged with the HRX/ALL/MLL gene in acute myelogeneous leukemias. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, May 2009].
- **Diseases (Open Targets)**: atrial fibrillation (0.399); Abnormality of the skeletal system (0.383); bile duct carcinoma (0.370); esophageal adenocarcinoma (0.370); B-cell acute lymphoblastic leukemia (0.370)
- **Europe PMC papers**: 2810
- **Why important**: EPS15 has a central network position, connecting to EPS15L1, CLINT1, and ARHGAP17, and it participates in every listed hu.MAP complex containing the module's core triplet. It is the most extensively studied gene in the module, with established roles at clathrin-coated pits, receptor-mediated endocytosis, receptor recycling, and endosomal transport. Its disease associations include acute lymphoblastic leukemia, bile duct carcinoma, esophageal adenocarcinoma, skeletal abnormalities, and atrial fibrillation in the provided Open Targets evidence.
- **Conclusion**: Established conclusion: EPS15 is a core endocytic scaffold and is the strongest anchor for interpreting the module as clathrin-associated trafficking. Hypothesis: its central position may help coordinate the co-abundance of the other module genes, but the network does not prove that EPS15 regulates their abundance.

#### EPS15L1

- **Related proteins** (co-abundance neighbors): ARHGAP17 (0.85), EPS15 (0.84), USP15 (0.83); STRING partners: EPS15 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_05120.1, huMAP3_05849.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1, huMAP3_06283.1, huMAP3_08540.1, huMAP3_09107.1
- **Function (MyGene.info)**: epidermal growth factor receptor pathway substrate 15 like 1. Enables cadherin binding activity. Predicted to be involved in endocytosis and endosomal transport. Located in membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: split hand-foot malformation (0.370); lysosomal storage disease (0.310); neurodegenerative disease (0.310); Alzheimer disease (0.310); Parkinson disease (0.310)
- **Europe PMC papers**: 426
- **Why important**: EPS15L1 has a central network position and connects to EPS15, ARHGAP17, and USP15. It is present in every listed hu.MAP complex containing the core triplet and appears in all supplementary STRING enrichment categories. Its annotations support endocytosis, endosomal transport, synaptic vesicle endocytosis, membrane localization, and cadherin binding. The provided disease associations include split hand-foot malformation, lysosomal storage disease, neurodegenerative disease, Alzheimer disease, and Parkinson disease.
- **Conclusion**: Established conclusion: EPS15L1 is a core member of the clathrin-associated endocytic signal and forms a particularly strong known STRING relationship with EPS15. Hypothesis: its connections to ARHGAP17 and USP15 may reflect coordination between endocytic trafficking, cytoskeletal regulation, and protein deubiquitination, but those links are not established physical interactions in the supplied resources.

#### CLINT1

- **Related proteins** (co-abundance neighbors): EPS15 (0.84); STRING partners: EPS15 (0.871)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Vesicles; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: huMAP3_05120.1, huMAP3_05849.1, huMAP3_08320.1, huMAP3_09403.1, huMAP3_10876.1, huMAP3_10762.1, huMAP3_12918.1, huMAP3_12394.1
- **Function (MyGene.info)**: clathrin interactor 1. This gene encodes a protein with similarity to the epsin family of endocytic adapter proteins. The encoded protein interacts with clathrin, the adapter protein AP-1 and phosphoinositides. This protein may be involved in the formation of clathrin coated vesicles and trafficking between the trans-Golgi network and endosomes. Mutations in this gene are associated with a susceptibility to schizophreni…
- **Diseases (Open Targets)**: smoking initiation (0.482); dengue disease (0.388); benign prostatic hyperplasia (0.347); psoriasis (0.339); Alzheimer disease (0.318)
- **Europe PMC papers**: 354
- **Why important**: CLINT1 is directly connected to EPS15 in STRING and participates with EPS15 and EPS15L1 across the listed hu.MAP complexes. Its annotations specifically describe clathrin-coat assembly, interaction with clathrin, AP1, and phosphoinositides, and trafficking between the trans-Golgi network and endosomes. It also has an immune-cell-enriched HPA annotation for basophils and an Open Targets association with benign prostatic hyperplasia, as well as associations with smoking initiation, dengue disease, psoriasis, and Alzheimer disease.
- **Conclusion**: Established conclusion: CLINT1 provides direct molecular support for clathrin-coat assembly and connects the module to endosome and trans-Golgi trafficking. Hypothesis: its presence may make the module relevant to receptor and membrane cargo sorting in both tissues, but a tissue-specific role is not demonstrated.

#### ARHGAP17

- **Related proteins** (co-abundance neighbors): EPS15L1 (0.85), EPS15 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho GTPase activating protein 17. RICH1 is a GTPase-activating protein (GAP). GAPs stimulate the intrinsic GTP hydrolysis of small G proteins, such as RHOA (MIM 165390), RAC1 (MIM 602048), and CDC42 (MIM 116952).[supplied by OMIM, Apr 2004].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.559); neurodegenerative disease (0.496); atrial fibrillation (0.367); gout (0.321); diabetic neuropathy (0.277)
- **Europe PMC papers**: 527
- **Why important**: ARHGAP17 connects to both EPS15 and EPS15L1 in the co-abundance network and has annotations for Rho-family GTPase regulation, actin-cytoskeleton organization, and signal transduction. It is detected in cervix_uterine but not prostate by the supplied HPA immunohistochemistry summary, and it has cell-type-enhanced annotations in several neural, epithelial, and immune-related cell types. Its listed disease associations include skeletal abnormalities, neurodegenerative disease, atrial fibrillation, gout, and diabetic neuropathy.
- **Conclusion**: Established conclusion: ARHGAP17 is a Rho-family GTPase regulator that may relate endocytic machinery to actin organization. Hypothesis: its co-abundance with EPS15 and EPS15L1 may indicate coupling between coated-vesicle dynamics and cortical cytoskeletal remodeling. This interpretation is less firmly established than the clathrin interpretation because ARHGAP17 has no listed GO, STRING, or hu.MAP support within the supplied module evidence.

#### USP15

- **Related proteins** (co-abundance neighbors): EPS15L1 (0.83); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in cervix_uterine, prostate
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ubiquitin specific peptidase 15. This gene encodes a member of the ubiquitin specific protease (USP) family of deubiquitinating enzymes. USP enzymes play critical roles in ubiquitin-dependent processes through polyubiquitin chain disassembly and hydrolysis of ubiquitin-substrate bonds. The encoded protein associates with the COP9 signalosome, and also plays a role in transforming growth factor beta signalling through deubiquitina…
- **Diseases (Open Targets)**: neurodegenerative disease (0.548); alcohol drinking (0.294); post term pregnancy (0.272); smoking initiation (0.217); injury (0.162)
- **Europe PMC papers**: 1872
- **Why important**: USP15 connects to EPS15L1 in the module and is the only gene with tissue-enhanced HPA expression, namely in bone marrow, together with immune-cell enhancement in neutrophils and neutrophil progenitors. It encodes a deubiquitinating enzyme involved in protein deubiquitination, protein stability, transforming growth factor beta receptor signaling, and BMP signaling. It has substantial literature support and listed associations with neurodegenerative disease, alcohol drinking, post-term pregnancy, smoking initiation, and injury.
- **Conclusion**: Established conclusion: USP15 is a deubiquitination and signaling regulator with a notable neutrophil-lineage expression pattern in the supplied HPA evidence. Hypothesis: its association with EPS15L1 may indicate regulation of the stability or signaling state of endocytic proteins or cargo, but no direct physical or causal relationship is established here.
