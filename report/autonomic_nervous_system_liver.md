# Conserved co-abundance modules: autonomic_nervous_system and liver

## Module 0

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (6)**: HIBADH, ACADM, CCDC93, COQ9, DECR1, SCP2

### Function

The module is most consistent with organelle-based lipid and energy metabolism, especially mitochondrial fatty-acid oxidation, peroxisomal lipid handling, branched-chain amino-acid catabolism, and coenzyme Q biosynthesis. This interpretation is supported by the annotated functions of ACADM, DECR1, SCP2, HIBADH, and COQ9, together with the co-abundance connections linking these metabolic genes. The network is not a complete pathway: CCDC93 is annotated for vesicle transport and endocytic recycling, so it may represent a regulatory or trafficking component rather than a core metabolic enzyme. No GO/KEGG term passed global correction; therefore, the pathway interpretation is based on convergent gene annotations and network structure rather than significant enrichment.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or blood-cell-enriched genes. The HPA evidence reports no secreted genes and low immune-cell specificity for every module gene. Protein detection is present for all module genes in liver, and several genes are liver-enhanced or enriched in metabolically relevant tissues and cell types, including hepatocytes. This supports a tissue or parenchymal metabolic signal rather than a blood contamination explanation. The tissue and single-cell specificity patterns also show that the module is not uniformly ubiquitous: several genes are enhanced in liver, skeletal muscle, or tongue, while others have low tissue specificity. The shared signal between autonomic nervous system and liver could therefore reflect conserved cellular energy and lipid metabolism, but the available HPA data do not establish which autonomic cell type contributes the signal.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides high-confidence support for the ACADM-DECR1 and ACADM-SCP2 relationships. These links are biologically coherent with fatty-acid oxidation and lipid metabolism and strengthen the interpretation that part of the co-abundance module reflects known metabolic relationships. COQ9, HIBADH, and CCDC93 have no reported STRING partners within this module, so their module connections are co-abundance relationships rather than independently supported STRING interactions. No hu.MAP complex contains multiple module members. Overall, the network combines a small known interaction core with additional correlations that may reflect shared tissue regulation, pathway proximity, or coordinated organelle activity rather than a single established protein complex.

**STRING interactions (score >= 0.7)**: 2 of 15 gene pairs: ACADM–DECR1 (0.755); ACADM–SCP2 (0.745)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be claimed as a wholly new biochemical pathway. Several component functions and the ACADM relationships with DECR1 and SCP2 are already established or represented in STRING, while the genes have substantial prior literature and disease annotation. At the same time, the specific conserved co-abundance pattern across autonomic nervous system and liver, including the joint behavior of COQ9, DECR1, ACADM, SCP2, HIBADH, and CCDC93, is not directly established by the supplied STRING or hu.MAP evidence. It is therefore best described as a potentially novel cross-tissue co-abundance module built from mostly known biology, requiring replication and independent functional testing before being considered a new mechanism.

**Hypothesis.** Hypothesis: the module represents coordinated regulation of mitochondrial and peroxisomal substrate metabolism in liver and autonomic nervous system tissues. In this model, ACADM and DECR1 support mitochondrial fatty-acid oxidation, SCP2 links lipid and sterol handling with peroxisomal metabolism, HIBADH contributes branched-chain amino-acid catabolism, and COQ9 supports coenzyme Q production needed for mitochondrial respiratory function. CCDC93 may couple this metabolic state to vesicular or endocytic trafficking. A shared physiological program involving energy demand, lipid flux, or organelle maintenance could produce the observed cross-tissue co-abundance, but this regulatory explanation is a hypothesis rather than an established causal result.

### Important genes

#### COQ9

- **Related proteins** (co-abundance neighbors): SCP2 (0.87), DECR1 (0.84), CCDC93 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coenzyme Q9. This locus represents a mitochondrial ubiquinone biosynthesis gene. The encoded protein is likely necessary for biosynthesis of coenzyme Q10, as mutations at this locus have been associated with autosomal-recessive neonatal-onset primary coenzyme Q10 deficiency.[provided by RefSeq, Sep 2010].
- **Diseases (Open Targets)**: encephalopathy-hypertrophic cardiomyopathy-renal tubular disease syndrome (0.766); coenzyme Q10 deficiency (0.635); hereditary disease (0.415); mitochondrial disease (0.372); coenzyme Q10 deficiency, primary, 1 (0.370)
- **Europe PMC papers**: 958
- **Why important**: COQ9 is the most connected gene in the module and links to SCP2, DECR1, and CCDC93 in the co-abundance graph. Its established function in mitochondrial ubiquinone biosynthesis provides a plausible connection between the module and mitochondrial respiratory capacity. It is liver-detected and tissue-enhanced in skeletal muscle and tongue, and it has a strong disease connection to primary coenzyme Q deficiency and related mitochondrial disease.
- **Conclusion**: Established evidence supports COQ9 as a mitochondrial ubiquinone-biosynthesis gene and as a central network organizer. It is plausible, but not proven, that COQ9 coordinates respiratory support for the lipid and amino-acid catabolic activities in this module.

#### ACADM

- **Related proteins** (co-abundance neighbors): HIBADH (0.83), DECR1 (0.82); STRING partners: DECR1 (0.755), SCP2 (0.745)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acyl-CoA dehydrogenase medium chain. This gene encodes the medium-chain specific (C4 to C12 straight chain) acyl-Coenzyme A dehydrogenase. The homotetramer enzyme catalyzes the initial step of the mitochondrial fatty acid beta-oxidation pathway. Defects in this gene cause medium-chain acyl-CoA dehydrogenase deficiency, a disease characterized by hepatic dysfunction, fasting hypoglycemia, and encephalopathy, which can result in infant…
- **Diseases (Open Targets)**: medium chain acyl-CoA dehydrogenase deficiency (0.854); hereditary disease (0.516); rhabdomyolysis (0.370); short chain acyl-CoA dehydrogenase deficiency (0.349); Epileptic spasm (0.333)
- **Europe PMC papers**: 4795
- **Why important**: ACADM is a central metabolic node with connections to DECR1 and HIBADH, and it also has the module's STRING-supported relationships with DECR1 and SCP2. Its established enzyme activity initiates mitochondrial medium-chain fatty-acid beta-oxidation. HPA places it in liver, skeletal muscle, and tongue and in hepatocytes, and its deficiency is associated with hepatic dysfunction, fasting hypoglycemia, and encephalopathy. It also has the largest literature volume among the module genes.
- **Conclusion**: Established evidence identifies ACADM as a core fatty-acid oxidation enzyme and a biologically important anchor of the module. Its network position and independent interaction evidence make it the strongest candidate for representing the module's lipid-oxidation component, although the module does not prove that ACADM regulates the other genes.

#### DECR1

- **Related proteins** (co-abundance neighbors): COQ9 (0.84), ACADM (0.82); STRING partners: ACADM (0.755)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 2,4-dienoyl-CoA reductase 1. This gene encodes an accessory enzyme which participates in the beta-oxidation and metabolism of unsaturated fatty enoyl-CoA esters. [provided by RefSeq, Jul 2008]
- **Diseases (Open Targets)**: progressive encephalopathy with leukodystrophy due to DECR deficiency (0.411); hypertensive disorder (0.214); insomnia (0.200); neurodegenerative disease (0.198); exostosis (0.089)
- **Europe PMC papers**: 999
- **Why important**: DECR1 connects to both COQ9 and ACADM in the module and has an independent STRING-supported relationship with ACADM. Its established role is as an accessory enzyme for mitochondrial metabolism of unsaturated fatty enoyl-CoA esters, with annotations involving fatty-acid beta-oxidation and cold-induced thermogenesis. It is liver-enhanced and associated with a progressive encephalopathy caused by DECR deficiency.
- **Conclusion**: Established evidence supports DECR1 as a functional extension of the ACADM-centered fatty-acid oxidation signal. The co-abundance connection to COQ9 suggests coordinated mitochondrial regulation, but whether DECR1 links lipid oxidation to ubiquinone metabolism in this tissue pair remains a hypothesis.

#### SCP2

- **Related proteins** (co-abundance neighbors): COQ9 (0.87); STRING partners: ACADM (0.745)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Peroxisomes; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sterol carrier protein 2. This gene encodes two proteins: sterol carrier protein X (SCPx) and sterol carrier protein 2 (SCP2), as a result of transcription initiation from 2 independently regulated promoters. The transcript initiated from the proximal promoter encodes the longer SCPx protein, and the transcript initiated from the distal promoter encodes the shorter SCP2 protein, with the 2 proteins sharing a common C-termi…
- **Diseases (Open Targets)**: sterol carrier protein 2 deficiency (0.708); spermatogenic failure (0.191); stroke disorder (0.187); alcohol drinking (0.186); leukodystrophy (0.119)
- **Europe PMC papers**: 2268
- **Why important**: SCP2 connects to COQ9 in the co-abundance graph and to ACADM through a STRING-supported relationship. Its established annotations span peroxisomal sterol transport and lipid metabolism, including fatty-acid, steroid, and bile-acid pathways. It is liver-enhanced and enriched in hepatocytes and other epithelial cell types, and SCP2 deficiency has disease associations.
- **Conclusion**: Established evidence supports SCP2 as the principal peroxisomal and sterol-lipid component of the module. Its connection to ACADM supports coordination between peroxisomal lipid handling and mitochondrial fatty-acid oxidation, but the cross-organelle coordination is a hypothesis rather than a demonstrated mechanism.

#### HIBADH

- **Related proteins** (co-abundance neighbors): ACADM (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 3-hydroxyisobutyrate dehydrogenase. This gene encodes a mitochondrial 3-hydroxyisobutyrate dehydrogenase enzyme. The encoded protein plays a critical role in the catabolism of L-valine by catalyzing the oxidation of 3-hydroxyisobutyrate to methylmalonate semialdehyde. [provided by RefSeq, Nov 2011].
- **Diseases (Open Targets)**: nephrolithiasis (0.354); hypertensive disorder (0.298); Hallux valgus (0.288); Increased blood pressure (0.283); osteoarthritis (0.282)
- **Europe PMC papers**: 530
- **Why important**: HIBADH is connected to ACADM and contributes a distinct metabolic dimension through its established role in mitochondrial catabolism of L-valine. It is detected in liver and has cell-type enhancement in syncytiotrophoblasts. Its disease associations include blood-pressure-related and metabolic phenotypes, although its literature volume is smaller than that of the principal lipid-metabolism genes.
- **Conclusion**: Established evidence supports HIBADH as a mitochondrial branched-chain amino-acid catabolism gene that may broaden the module beyond fatty-acid metabolism. Its connection to ACADM is compatible with coordinated mitochondrial fuel use, but the module does not establish direct biochemical coupling between these enzymes.

## Module 1

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (34)**: SLC3A2, ATL3, CNOT1, CPNE1, CTNND1, DYNC1I2, DHCR24, DLG1, DPYSL2, EWSR1, HMOX2, HNRNPH1, HNRNPL, HNRNPR, ME2, NSFL1C, NUP210, PSMC2, PSMA1, UQCRC1, RECQL, SACM1L, SERPINH1, SFXN3, SUPT16H, DARS2, TCEA1, ALYREF, F2, TMOD3, TXNDC5, EFTUD2, UBTF, ATP6V1H

### Function

The strongest interpretation is a mixed nuclear gene-expression and RNA-processing module, with supporting links to transcription elongation, chromatin handling, proteostasis, mitochondrial metabolism, and cell-structural processes. The module contains a recognizable hnRNP-centered subnetwork: HNRNPL, HNRNPR, and HNRNPH1 are connected in STRING, while ALYREF links several RNA-associated proteins and is connected to EFTUD2, which is a spliceosome component. EWSR1 also connects to HNRNPH1 and HNRNPR. A separate proteasome pair, PSMA1–PSMC2, and a transcription elongation pair, SUPT16H–TCEA1, provide additional coherent but relatively small subnetworks. RECQL connects the RNA-associated component to mitochondrial, redox, trafficking, and liver-associated signals. No GO or KEGG term passed global correction, so no pathway-level enrichment can be claimed as primary evidence. The absence of a globally significant term does not invalidate the module; it indicates that the gene set is heterogeneous or too small for confident pathway enrichment.

**Cell composition.** This is not predominantly a plasma or secreted-protein module. Only a minority of genes are annotated as secreted or intracellular-and-membrane proteins, with F2 being the clearest liver-derived secreted component. Most genes have low tissue specificity in HPA and are intracellular, especially nuclear proteins. The HPA profile therefore supports a substantial broadly expressed housekeeping or core cellular component rather than a specialized autonomic or hepatic program. Many genes are cell-type enhanced, including erythroid or megakaryocytic progenitor, glial, epithelial, and reproductive cell types, but immune-cell specificity is generally low. The shared signal could consequently reflect common cellular composition or general cellular activity in the sampled tissues, with a possible contribution from blood or liver-associated material rather than a dedicated autonomic–liver mechanism.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several already known relationships rather than an isolated novel interaction system. The most coherent known cluster is formed by ALYREF, HNRNPH1, HNRNPL, and HNRNPR, with EFTUD2 and EWSR1 also connected to parts of this cluster. STRING also confirms the PSMA1–PSMC2 proteasome relationship and the SUPT16H–TCEA1 transcription-related relationship. There is no STRING functional-enrichment result for this module. hu.MAP independently supports recurring hnRNP assemblies containing HNRNPL and HNRNPR across (hu.MAP huMAP3_07225.1), (hu.MAP huMAP3_06093.1), (hu.MAP huMAP3_09654.1), (hu.MAP huMAP3_07581.1), (hu.MAP huMAP3_10659.1), and (hu.MAP huMAP3_10625.1). It also places TCEA1 with RECQL in larger complexes in (hu.MAP huMAP3_10088.1) and (hu.MAP huMAP3_14982.1), and PSMA1 with PSMC2 in proteasome complexes in (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). These complexes contain many proteins outside the module, so the evidence supports membership in known cellular machines and partial recovery of those machines, not a complete module-specific complex.

**STRING interactions (score >= 0.7)**: 11 of 561 gene pairs: ALYREF–EFTUD2 (0.89); ALYREF–HNRNPH1 (0.914); ALYREF–HNRNPL (0.844); ALYREF–HNRNPR (0.851); EWSR1–HNRNPH1 (0.816); EWSR1–HNRNPR (0.786); HNRNPH1–HNRNPL (0.982); HNRNPH1–HNRNPR (0.947); HNRNPL–HNRNPR (0.961); PSMA1–PSMC2 (0.999); SUPT16H–TCEA1 (0.874)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07225.1 (HNRNPR, HNRNPL; 2/7); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_10088.1 (TCEA1, RECQL; 2/10); huMAP3_09654.1 (HNRNPR, HNRNPL; 2/13); huMAP3_07581.1 (HNRNPR, HNRNPL; 2/21); huMAP3_10659.1 (HNRNPR, HNRNPL; 2/28); huMAP3_14982.1 (TCEA1, RECQL; 2/28); huMAP3_10625.1 (HNRNPR, HNRNPL; 2/57); huMAP3_09656.1 (PSMA1, PSMC2; 2/64); huMAP3_13725.1 (PSMA1, PSMC2; 2/69)

### Novelty

The module should not be described as a newly discovered molecular pathway. Its most interpretable relationships are already represented by established hnRNP, spliceosome-associated, transcription, and proteasome machinery in STRING and hu.MAP. The co-abundance connection across autonomic nervous system and liver may still be a useful tissue-pair observation, because it suggests that these components vary together in the analyzed samples, but that observation alone does not establish a new biochemical interaction or disease mechanism. The lack of a STRING or hu.MAP record for some individual edges is not evidence of novelty, especially given the broadly expressed nature of many genes and the heterogeneous composition. A defensible novelty claim would require independent replication, control for cell composition and blood contamination, and comparison with other tissue-pair and co-expression datasets.

**Hypothesis.** Hypothesis: the conserved module reflects coordinated variation in the abundance of a general nuclear gene-expression and RNA-quality-control program that is shared by hepatocytes and cells represented in autonomic nervous system samples. In this model, an hnRNP-centered RNA-processing system involving ALYREF, HNRNPL, HNRNPR, HNRNPH1, and EFTUD2 is coupled indirectly to transcription elongation, proteasomal turnover, mitochondrial metabolism, and stress handling. F2 and the HPA cell-type patterns may mark tissue or sample-composition contributions rather than define the core mechanism. This hypothesis predicts that the central RNA-processing genes will remain associated after adjustment for cell composition, whereas peripheral liver-, blood-, or cell-type-associated genes will weaken.

### Important genes

#### ALYREF

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.87), HNRNPR (0.86), SERPINH1 (0.85), CPNE1 (0.84), RECQL (0.83), ME2 (0.81), TMOD3 (0.80); STRING partners: EFTUD2 (0.89), HNRNPH1 (0.914), HNRNPL (0.844), HNRNPR (0.851)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Aly/REF export factor. The protein encoded by this gene is a heat stable, nuclear protein and functions as a molecular chaperone. It is thought to regulate dimerization, DNA binding, and transcriptional activity of basic region-leucine zipper (bZIP) proteins. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: neurodegenerative disease (0.542); dengue disease (0.370); neoplasm (0.103); non-small cell lung carcinoma (0.102); hepatocellular carcinoma (0.098)
- **Europe PMC papers**: 1636
- **Why important**: ALYREF is one of the strongest network connectors in the module and links EFTUD2, HNRNPR, HNRNPH1, HNRNPL, RECQL, and additional module genes. STRING directly supports its relationships with the hnRNP-centered component. Its established functions in nuclear mRNA export, mRNA metabolism, and nonsense-mediated decay make it a plausible bridge between the module's RNA-processing signals and the broader co-abundance pattern. HPA places it in nuclear speckles and shows enhancement in bone-marrow and erythroid or megakaryocytic-related cell populations. It also has substantial literature and disease links involving neurodegenerative disease and cancer.
- **Conclusion**: Established evidence supports ALYREF as a central RNA-export and RNA-metabolism component of the module. It is a strong candidate for the core shared program, but the HPA cell-type pattern means that its co-abundance may partly reflect cellular composition. It is not established that ALYREF mechanistically links autonomic nervous system biology to liver biology in this dataset.

#### HNRNPL

- **Related proteins** (co-abundance neighbors): PSMC2 (0.90), SUPT16H (0.88), HNRNPH1 (0.81); STRING partners: ALYREF (0.844), HNRNPH1 (0.982), HNRNPR (0.961)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_07581.1, huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein L. Heterogeneous nuclear RNAs (hnRNAs) which include mRNA precursors and mature mRNAs are associated with specific proteins to form heterogenous ribonucleoprotein (hnRNP) complexes. Heterogeneous nuclear ribonucleoprotein L is among the proteins that are stably associated with hnRNP complexes and along with other hnRNP proteins is likely to play a major role in the formation, packaging, processing, a…
- **Diseases (Open Targets)**: dengue disease (0.370); neuromuscular disease (0.118); ovarian cancer (0.093); ovarian carcinoma (0.093); urinary bladder cancer (0.080)
- **Europe PMC papers**: 2574
- **Why important**: HNRNPL is a central member of the module's most coherent known interaction structure. It connects in STRING to ALYREF, HNRNPH1, and HNRNPR and recurs with HNRNPR in multiple hu.MAP complexes, including (hu.MAP huMAP3_07225.1), (hu.MAP huMAP3_06093.1), (hu.MAP huMAP3_09654.1), (hu.MAP huMAP3_07581.1), (hu.MAP huMAP3_10659.1), and (hu.MAP huMAP3_10625.1). Its annotated functions in alternative splicing, RNA processing, and regulation of RNA splicing directly match the network structure. It has broad tissue distribution, nuclear localization, substantial literature, and disease associations involving neurological and neoplastic conditions.
- **Conclusion**: Established evidence supports HNRNPL as a core RNA-processing hub and a particularly well-supported representative of the module's shared machinery. The data support a role in coordinated RNA handling, but do not show that the module changes a particular transcript or splicing event in either tissue.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): EFTUD2 (0.87), ALYREF (0.86), CPNE1 (0.83); STRING partners: ALYREF (0.851), EWSR1 (0.786), HNRNPH1 (0.947), HNRNPL (0.961)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_07225.1, huMAP3_06093.1, huMAP3_09654.1, huMAP3_07581.1, huMAP3_10659.1, huMAP3_10625.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is another central hnRNP component, with STRING links to ALYREF, EWSR1, HNRNPH1, and HNRNPL. It recurs with HNRNPL across the same family of hu.MAP complexes, including (hu.MAP huMAP3_07225.1), (hu.MAP huMAP3_06093.1), (hu.MAP huMAP3_09654.1), (hu.MAP huMAP3_07581.1), (hu.MAP huMAP3_10659.1), and (hu.MAP huMAP3_10625.1). Its established role in spliceosome-associated pre-mRNA processing and transport provides direct functional support for the module's nuclear RNA-processing interpretation. Its disease associations include neurodevelopmental and intellectual-disability phenotypes, making it biologically relevant to the autonomic nervous system context.
- **Conclusion**: Established evidence supports HNRNPR as a core spliceosome-associated component that reinforces the interpretation centered on RNA processing. Its presence does not demonstrate a tissue-specific autonomic or hepatic function, and the disease associations should be treated as contextual rather than as evidence that this module causes those disorders.

#### RECQL

- **Related proteins** (co-abundance neighbors): ME2 (0.88), UQCRC1 (0.85), SFXN3 (0.83), ALYREF (0.83), HMOX2 (0.82), F2 (0.81), ATP6V1H (0.81), NSFL1C (0.80), UBTF (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_10088.1, huMAP3_14982.1
- **Function (MyGene.info)**: RecQ like helicase. The protein encoded by this gene is a member of the RecQ DNA helicase family. DNA helicases are enzymes involved in various types of DNA repair, including mismatch repair, nucleotide excision repair and direct repair. The encoded protein is involved in the processing of Holliday junctions, the suppression of sister chromatid exchanges, telomere maintenance, and is required for genotoxic stress res…
- **Diseases (Open Targets)**: RECON progeroid syndrome (0.595); hereditary neoplastic syndrome (0.505); obesity disorder (0.404); myofibrillar myopathy 8 (0.334); hereditary breast ovarian cancer syndrome (0.328)
- **Europe PMC papers**: 954
- **Why important**: RECQL has the strongest network connectivity in the module and acts as a bridge from the hnRNP-associated region to ME2, UQCRC1, SFXN3, HMOX2, F2, ATP6V1H, and NSFL1C. It is linked to TCEA1 in hu.MAP complexes (hu.MAP huMAP3_10088.1) and (hu.MAP huMAP3_14982.1). Its established RecQ helicase functions in DNA repair, replication, recombination, Holliday-junction processing, telomere maintenance, and genotoxic-stress resistance provide a plausible genome-stability component. It has extensive disease relevance through progeroid and cancer-related conditions and is detected in liver by HPA.
- **Conclusion**: Established evidence supports RECQL as a highly connected genome-maintenance protein and a bridge gene in this module. Its network position makes it important for interpretation, but the data do not establish that DNA repair is the principal module function; it may instead capture broad cellular stress or proliferative state.

#### F2

- **Related proteins** (co-abundance neighbors): RECQL (0.81); STRING partners: none
- **HPA**: Tissue enriched; Cell type enriched; blood Not detected in immune cells; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coagulation factor II, thrombin. This gene encodes the prothrombin protein (also known as coagulation factor II). This protein is proteolytically cleaved in multiple steps to form the activated serine protease thrombin. The activated thrombin enzyme plays an important role in thrombosis and hemostasis by converting fibrinogen to fibrin during blood clot formation, by stimulating platelet aggregation, and by activating additional …
- **Diseases (Open Targets)**: congenital prothrombin deficiency (0.827); thrombophilia due to thrombin defect (0.738); venous thromboembolism (0.727); deep vein thrombosis (0.690); blood coagulation disease (0.670)
- **Europe PMC papers**: 109299
- **Why important**: F2 is important because it is the clearest tissue-specific outlier in the module: HPA describes it as liver-enriched, hepatocyte-enriched, and secreted to blood. Its established function in thrombin generation, coagulation, platelet activation, wound response, and vascular signaling is biologically distinct from the nuclear RNA-processing core. It has very extensive literature and strong disease associations involving prothrombin deficiency, thrombophilia, and venous thromboembolism. Its direct module connection is to RECQL rather than to the central hnRNP cluster.
- **Conclusion**: Established evidence supports F2 as a liver and blood-related marker that may explain part of the cross-tissue co-abundance signal. It should not be used to assign a coagulation function to the whole module. The hypothesis that F2 reflects sample composition or liver secretory state is more defensible than a claim that thrombin directly organizes the nuclear RNA-processing subnetwork.

## Module 2

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (33)**: NT5E, ACACA, ALG2, AMPD2, PRMT5, ARFIP1, ATP5PB, CENPV, DRG2, TBRG4, FNDC3A, HTATIP2, ILK, DTYMK, LANCL1, LRBA, IGF2R, NAA15, NCKAP1, NTPCR, NUP160, PAK2, PDXDC1, GART, CTPS2, POLR2B, SEC63, TBL2, UBA3, UBA6, VAPB, ATP6V1A, ZW10

### Function

The module does not support a single statistically established GO or KEGG function: no GO/KEGG term passed global correction. Its gene content nevertheless points to a mixed intracellular maintenance program rather than a canonical tissue-specific pathway. The strongest functional themes suggested by individual gene annotations are lipid and acetyl-CoA metabolism through ACACA, purine and pyrimidine nucleotide metabolism through GART, AMPD2, DTYMK and CTPS2, protein processing and trafficking through ALG2, SEC63, ATP6V1A, IGF2R and VAPB, and regulation of transcription, chromatin or protein modification through PRMT5, POLR2B, UBA3 and UBA6. The co-abundance structure therefore appears compatible with coordinated metabolic, biosynthetic, trafficking and quality-control activity, but the absence of globally significant enrichment means this interpretation remains integrative rather than pathway-proven.

**Cell composition.** The module is not dominated by plasma or secreted proteins: only NT5E is annotated as intracellular and membrane-associated secretome protein, and the other genes are not secreted. Most genes have low tissue specificity, which is consistent with broadly expressed cellular machinery rather than a narrowly specialized autonomic or hepatic program. The HPA single-cell annotations include several cell-type-enhanced genes, especially neutrophil-associated genes, but immune-cell specificity is generally low across the module. AMPD2 and ATP6V1A show particularly relevant myeloid or neutrophil associations, while IGF2R is neutrophil-enriched and NT5E is enhanced in selected lymphocyte populations. Thus, blood or shared cell-type composition could contribute to the cross-tissue co-abundance signal, although the module is not characterized as a predominantly blood-cell module. Protein detection in liver is broad but incomplete, whereas there is no matching HPA tissue for autonomic nervous system, so tissue-level protein evidence cannot establish equivalent expression in both tissues.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING reports only a small set of high-confidence relationships: ACACA with GART, AMPD2 with NT5E, DTYMK with GART, DTYMK with NT5E, and UBA3 with UBA6. These links provide plausible biochemical support for connections among lipid metabolism, purine or nucleotide handling, extracellular nucleotide processing, and ubiquitin-like modification. STRING functional enrichment is absent, so the interactions do not establish a unified pathway. The hu.MAP evidence consists of one low-coverage complex, C1, containing ZW10, NUP160 and TBRG4 among many other complex members. This supports a possible shared complex context involving chromosome or nuclear organization and mitochondrial or cellular maintenance, but only a minority of that complex is represented in the module. Most module edges are therefore co-abundance relationships without direct STRING or hu.MAP support, and should not be treated as physical interactions.

**STRING interactions (score >= 0.7)**: 5 of 528 gene pairs: ACACA–GART (0.893); AMPD2–NT5E (0.885); DTYMK–GART (0.835); DTYMK–NT5E (0.92); UBA3–UBA6 (0.712)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11232.1 (ZW10, NUP160, TBRG4; 3/78)

### Novelty

This module may be a new cross-tissue co-abundance observation, but the fact sheet does not establish it as a new biological pathway or a newly discovered physical complex. The presence of established STRING relationships, the hu.MAP complex overlap, and the broadly expressed functions of many genes indicate that several component relationships are already known. Conversely, the particular joint co-abundance configuration across autonomic nervous system and liver is not represented by the available STRING or hu.MAP evidence. That pattern is potentially novel, but absence from those resources alone cannot prove novelty because databases are incomplete and the module may reflect shared cell composition, common cellular state, or coordinated abundance without direct molecular binding. A stronger novelty claim would require independent replication, adjustment for cell composition, comparison with published tissue co-expression modules, and experimental or perturbational validation.

**Hypothesis.** Hypothesis: the module represents a shared cellular homeostasis state linking hepatic and autonomic-system cells through coordinated biosynthetic metabolism, organelle and protein trafficking, nucleotide turnover, and stress or quality-control processes. ACACA may mark lipid-building demand; GART, AMPD2, DTYMK and CTPS2 may reflect nucleotide supply; SEC63, ALG2, ATP6V1A, VAPB and IGF2R may support secretory, endosomal and lysosomal handling; and UBA3, UBA6 and PRMT5 may provide protein-modification and regulatory control. NT5E could connect intracellular nucleotide metabolism to extracellular purine signaling, particularly where vascular, neural or immune cells contribute to the samples. This is a mechanistic model rather than an established conclusion, and an alternative explanation is shared abundance of broadly expressed housekeeping machinery or variable blood and cell-type content.

### Important genes

#### ACACA

- **Related proteins** (co-abundance neighbors): UBA6 (0.88), TBL2 (0.87), NCKAP1 (0.86), LANCL1 (0.86), PRMT5 (0.85), ZW10 (0.83), AMPD2 (0.83), ALG2 (0.81); STRING partners: GART (0.893)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA carboxylase alpha. Acetyl-CoA carboxylase (ACC) is a complex multifunctional enzyme system. ACC is a biotin-containing enzyme which catalyzes the carboxylation of acetyl-CoA to malonyl-CoA, the rate-limiting step in fatty acid synthesis. There are two ACC forms, alpha and beta, encoded by two different genes. ACC-alpha is highly enriched in lipogenic tissues. The enzyme is under long term control at the transcriptio…
- **Diseases (Open Targets)**: neurodegenerative disease (0.550); Alzheimer disease (0.463); lysosomal storage disease (0.460); Parkinson disease (0.460); autoimmune disorder of central nervous system (0.383)
- **Europe PMC papers**: 6268
- **Why important**: ACACA is among the most connected genes in the module and links directly to several module neighborhoods, including GART, AMPD2, TBL2, NCKAP1, LANCL1, PRMT5 and ZW10. Its established function is acetyl-CoA carboxylation and malonyl-CoA production, placing it at a control point for fatty-acid biosynthesis and acetyl-CoA metabolism. It is detected in liver, has neural cell-type-enhanced annotations, and has extensive literature and disease links including neurodegenerative and Alzheimer disease associations. Its STRING relationship with GART provides an independently supported connection between lipid and purine biosynthetic machinery.
- **Conclusion**: Established: ACACA is a central network-associated metabolic enzyme with liver detection, neural relevance, and a known STRING link to GART. Conclusion: it is a strong candidate marker of the module's metabolic arm. Hypothesis: coordinated ACACA abundance may reflect lipid-synthesis demand coupled to nucleotide and cellular maintenance demands, but the module does not prove that ACACA drives the shared tissue signal.

#### SEC63

- **Related proteins** (co-abundance neighbors): GART (0.86), ALG2 (0.86), TBRG4 (0.85), DTYMK (0.82), NUP160 (0.81), PAK2 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC63 protein translocation regulator. The Sec61 complex is the central component of the protein translocation apparatus of the endoplasmic reticulum (ER) membrane. The protein encoded by this gene and SEC62 protein are found to be associated with ribosome-free SEC61 complex. It is speculated that Sec61-Sec62-Sec63 may perform post-translational protein translocation into the ER. The Sec61-Sec62-Sec63 complex might also perform the bac…
- **Diseases (Open Targets)**: autosomal dominant polycystic liver disease (0.795); neurodegenerative disease (0.526); polycystic liver disease 1 (0.430); Biliary tract abnormality (0.346); placental abruption (0.232)
- **Europe PMC papers**: 1756
- **Why important**: SEC63 is highly connected within the module and links ALG2, GART, TBRG4, DTYMK, NUP160 and PAK2. Its established role is in the ER protein-translocation machinery associated with SEC61 and SEC62, making it relevant to protein targeting, membrane insertion and ER quality control. It is detected in liver and has disease associations involving polycystic liver disease and neurodegenerative disease. Although it has no listed STRING or hu.MAP partner in this module, its network position connects metabolic, nuclear-pore and trafficking-related genes.
- **Conclusion**: Established: SEC63 is an ER protein-translocation regulator with liver detection and disease relevance. Conclusion: it is a plausible systems-level bridge between biosynthetic activity and organelle proteostasis. Hypothesis: its co-abundance may indicate shared ER processing demand across the two tissues, but this cannot be distinguished from general housekeeping expression using the module alone.

#### NT5E

- **Related proteins** (co-abundance neighbors): TBRG4 (0.83); STRING partners: AMPD2 (0.885), DTYMK (0.92)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: 5'-nucleotidase ecto. The protein encoded by this gene is a plasma membrane protein that catalyzes the conversion of extracellular nucleotides to membrane-permeable nucleosides. The encoded protein is used as a determinant of lymphocyte differentiation. Defects in this gene can lead to the calcification of joints and arteries. Two transcript variants encoding different isoforms have been found for this gene.[provided b…
- **Diseases (Open Targets)**: hereditary arterial and articular multiple calcification syndrome (0.721); autosomal recessive spinocerebellar ataxia 20 (0.556); Spinocerebellar atrophy (0.340); non-small cell lung carcinoma (0.329); placental abruption (0.289)
- **Europe PMC papers**: 4404
- **Why important**: NT5E is functionally distinctive because it is a plasma-membrane ectonucleotidase that converts extracellular nucleotides to nucleosides and is involved in lymphocyte differentiation and nucleotide catabolism. It has supported STRING relationships with AMPD2 and DTYMK, connecting extracellular purine handling to intracellular nucleotide metabolism. It is liver-detected, has cell-type-enhanced annotations involving adrenal medulla and oligodendrocyte progenitor cells, and shows immune-cell enhancement in selected lymphocyte populations. Its disease associations include hereditary arterial and articular calcification and spinocerebellar ataxia, while its literature volume is substantial.
- **Conclusion**: Established: NT5E provides a membrane and extracellular-nucleotide interface and has multiple disease and cell-context associations. Conclusion: it is the most compelling candidate for linking the module to extracellular purine signaling and possible vascular, neural or immune context. Hypothesis: NT5E may couple tissue stress or cell-surface nucleotide turnover to the intracellular metabolic program, although blood or endothelial composition could also explain its co-abundance.

#### AMPD2

- **Related proteins** (co-abundance neighbors): TBL2 (0.84), ACACA (0.83), TBRG4 (0.82); STRING partners: NT5E (0.885)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adenosine monophosphate deaminase 2. The protein encoded by this gene is important in purine metabolism by converting AMP to IMP. The encoded protein, which acts as a homotetramer, is one of three AMP deaminases found in mammals. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: pontocerebellar hypoplasia type 9 (0.813); hereditary spastic paraplegia 63 (0.696); pontocerebellar hypoplasia (0.670); hereditary disease (0.404); Abnormality of the nervous system (0.340)
- **Europe PMC papers**: 560
- **Why important**: AMPD2 occupies a metabolically informative position connected to ACACA, TBL2 and TBRG4, and has a high-confidence STRING relationship with NT5E. Its established biochemical role is conversion of AMP to IMP, with broader involvement in purine and ATP metabolism. It is tissue-enhanced in brain, detected in liver, and has strong myeloid and neutrophil-related HPA annotations. Its disease associations include pontocerebellar hypoplasia and hereditary spastic paraplegia, giving it relevance to the autonomic or neural side of the tissue pair.
- **Conclusion**: Established: AMPD2 is a purine-metabolism enzyme with neural, hepatic and myeloid expression context and a supported connection to NT5E. Conclusion: it is a strong candidate for the nucleotide-turnover component of the module. Hypothesis: AMPD2 and NT5E may form a functional axis spanning intracellular and extracellular purine metabolism, but the observed co-abundance could partly reflect neutrophil or other shared-cell contamination.

#### IGF2R

- **Related proteins** (co-abundance neighbors): NAA15 (0.84), LANCL1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Immune cell enhanced; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: insulin like growth factor 2 receptor. This gene encodes a receptor for both insulin-like growth factor 2 and mannose 6-phosphate. The binding sites for each ligand are located on different segments of the protein. This receptor has various functions, including in the intracellular trafficking of lysosomal enzymes, the activation of transforming growth factor beta, and the degradation of insulin-like growth factor 2. Mutation or loss o…
- **Diseases (Open Targets)**: hepatocellular carcinoma (0.498); coronary artery disorder (0.477); Hypercholesterolemia (0.369); myocardial ischemia (0.359); coronary atherosclerosis (0.349)
- **Europe PMC papers**: 12245
- **Why important**: IGF2R is connected to LANCL1 and NAA15 and is a multifunctional receptor involved in IGF2 handling, mannose-six-phosphate-dependent lysosomal enzyme trafficking, TGF-beta activation and lysosomal transport. It is detected in liver and is enriched in neutrophils, while its annotations include liver development and hepatocellular carcinoma associations. Its very large literature base makes it one of the better-established genes in the module. Although it has no listed STRING or hu.MAP interaction here, its trafficking and signaling functions provide a biologically plausible connection between hepatic physiology, lysosomal handling and cell-state regulation.
- **Conclusion**: Established: IGF2R is a liver-relevant trafficking and signaling receptor with lysosomal functions, neutrophil enrichment and substantial disease literature. Conclusion: it is an important contextual gene for interpreting the module as an organelle-trafficking and cell-state program rather than as a pure metabolic pathway. Hypothesis: IGF2R may help couple extracellular growth-factor or lysosomal cargo handling to the broader module, but the current network does not demonstrate direct mechanistic coupling.

## Module 3

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (50)**: ABCF1, ACIN1, ACSL3, AKR1B1, ATAD1, BCLAF1, GLB1, BPNT1, CAPZB, CSTF3, DDX46, DPP3, DUSP3, DYNC1H1, EGFR, EIF3C, EML4, EMC1, FABP5, GAPVD1, HSP90AA1, IDH3A, MYBBP1A, NSF, NUDCD2, NUP85, ALDH18A1, PDCD6IP, PPP4C, PPM1F, RCC1, UPF1, SAMHD1, SEPTIN9, SF3A1, SNW1, SNX5, CTTN, SRP68, SRP72, CARS1, EPRS1, QARS1, TARS1, TFAM, UFD1, UMPS, ATP6V0A1, XPNPEP1, ZFR

### Function

No GO or KEGG term passed global correction, so the module should not be assigned a specific pathway on enrichment evidence alone. Its gene content is nevertheless coherent with broadly conserved cellular infrastructure: protein synthesis and translation control through EPRS1, QARS1, TARS1 and EIF3C; pre-mRNA processing and splicing through SF3A1, DDX46, BCLAF1, ACIN1 and CSTF3; nucleocytoplasmic transport through NUP85 and RCC1; intracellular trafficking, vesicle handling and cytoskeletal organization through DYNC1H1, ATP6V0A1, CAPZB, CTTN, PDCD6IP and SNX5; and mitochondrial or metabolic maintenance through TFAM, ALDH18A1, IDH3A, ACSL3, UMPS and AKR1B1. The network therefore most plausibly represents a conserved cellular maintenance and biosynthetic program rather than a narrowly specialized autonomic or hepatic pathway. The centrality of ABCF1, ALDH18A1, UMPS and DYNC1H1 supports integration across translation, metabolism, transport and organelle function, but co-abundance does not establish direct biochemical regulation.

**Cell composition.** This is not predominantly a plasma or secreted-protein module: the HPA summary identifies only a small minority of genes as secreted, and several of those are intracellular-and-membrane proteins rather than classical circulating factors. It is also not strongly blood-cell enriched. Most genes have low tissue specificity and low immune-cell specificity, arguing for a broadly expressed housekeeping-like component rather than a blood-cell signature. Liver protein detection is common among the genes, but this is compatible with the liver being a protein-rich tissue and does not by itself establish liver specificity. The scattered tissue-enhanced annotations, including brain, adrenal gland, parathyroid gland, bone marrow and skeletal muscle, do not form a single tissue program. Cell-type-enhanced annotations are heterogeneous, with reproductive, epithelial, neural, stromal and immune-associated labels. Thus, the shared signal is more consistent with conserved cellular composition or common basal activity than with plasma contamination or a single shared specialized cell type.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several established relationships within the module. The strongest coherent groups include EPRS1 with QARS1 and TARS1, SF3A1 with DDX46 and SNW1, SRP68 with SRP72, EGFR with HSP90AA1, CTTN, EML4 and PDCD6IP, and DYNC1H1 with HSP90AA1 and CAPZB. These links indicate that parts of the co-abundance structure recapitulate known translation, spliceosomal, signal-recognition-particle, chaperone, receptor-trafficking and cytoskeletal biology. hu.MAP independently supports the aminoacyl-tRNA synthetase group through (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1), spliceosome-associated groups through (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1), RNA-processing groups involving BCLAF1 and ACIN1 through (hu.MAP huMAP3_06097.1), (hu.MAP huMAP3_10564.1), (hu.MAP huMAP3_11073.1) and (hu.MAP huMAP3_09943.1), RNA surveillance through (hu.MAP huMAP3_10625.1), and nuclear-pore organization through (hu.MAP huMAP3_12581.1). The metabolic and mitochondrial association involving ALDH18A1 and BPNT1 in (hu.MAP huMAP3_13468.1) is more weakly represented within the module because only a small subset of each large complex is present. STRING supplies no functional enrichment result, so these are relationship-level supports rather than globally significant enrichment evidence. Overall, the module contains several recognizable subnetworks connected by co-abundance edges, rather than one experimentally established multiprotein complex.

**STRING interactions (score >= 0.7)**: 20 of 1225 gene pairs: AKR1B1–GLB1 (0.903); ALDH18A1–EPRS1 (0.723); BCLAF1–SNW1 (0.823); CAPZB–DYNC1H1 (0.964); CARS1–EPRS1 (0.849); CARS1–QARS1 (0.838); CARS1–TARS1 (0.817); CTTN–EGFR (0.829); DDX46–SF3A1 (0.999); DYNC1H1–HSP90AA1 (0.909); EGFR–EML4 (0.904); EGFR–HSP90AA1 (0.999); EGFR–PDCD6IP (0.913); EIF3C–EPRS1 (0.755); EPRS1–HSP90AA1 (0.701); EPRS1–QARS1 (0.999); EPRS1–TARS1 (0.928); QARS1–TARS1 (0.807); SF3A1–SNW1 (0.989); SRP68–SRP72 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_02637.1 (EPRS1, TARS1, QARS1; 3/14); huMAP3_13688.1 (EPRS1, TARS1, QARS1; 3/14); huMAP3_06097.1 (BCLAF1, ACIN1; 2/22); huMAP3_10564.1 (BCLAF1, ACIN1; 2/37); huMAP3_04549.1 (SF3A1, DDX46; 2/52); huMAP3_10625.1 (UPF1, ZFR; 2/57); huMAP3_12581.1 (RCC1, NUP85; 2/58); huMAP3_11073.1 (BCLAF1, ACIN1; 2/67); huMAP3_09943.1 (BCLAF1, ACIN1; 2/78); huMAP3_06511.1 (SF3A1, DDX46; 2/79); huMAP3_08980.1 (SF3A1, DDX46; 2/97); huMAP3_13468.1 (BPNT1, ALDH18A1; 2/99)

### Novelty

A claim that this is a wholly new biological pathway is not justified. Many internal relationships are already documented by STRING or hu.MAP, and the module contains widespread housekeeping genes with substantial prior literature. The potentially novel observation is the conserved co-abundance arrangement across autonomic nervous system and liver, including the way translation, RNA processing, transport, metabolism and cytoskeletal genes are linked in the same cross-tissue module. Absence of a particular edge from STRING or hu.MAP would not prove novelty, because those resources emphasize physical or curated relationships and do not represent every expression-level association. The appropriate conclusion is that the module may provide a new cross-tissue co-abundance pattern or systems-level organization, but its component biology is largely established and requires replication, tissue-cell deconvolution and perturbation experiments before being called a new mechanism.

**Hypothesis.** Hypothesis: the module reflects a conserved cellular-resilience program shared by cells in the two tissues. Coordinated aminoacyl-tRNA charging and translation initiation could maintain proteome production; spliceosome, RNA-surveillance and nuclear-pore components could preserve transcript quality and trafficking; mitochondrial, lysosomal, vesicular and cytoskeletal machinery could support energy management, cargo movement and membrane turnover. EGFR-linked trafficking and signaling, together with DYNC1H1-dependent transport, may connect extracellular or membrane events to intracellular maintenance. This model predicts that module activity will track protein-synthesis demand, organelle stress, vesicle traffic or cellular composition rather than a unique autonomic-liver endocrine function. It is a hypothesis, not a demonstrated causal pathway.

### Important genes

#### EPRS1

- **Related proteins** (co-abundance neighbors): ATP6V0A1 (0.84), ABCF1 (0.83), ALDH18A1 (0.81), ACSL3 (0.80); STRING partners: ALDH18A1 (0.723), CARS1 (0.849), EIF3C (0.755), HSP90AA1 (0.701), QARS1 (0.999), TARS1 (0.928)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_02637.1, huMAP3_13688.1
- **Function (MyGene.info)**: glutamyl-prolyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determine…
- **Diseases (Open Targets)**: leukodystrophy, hypomyelinating, 15 (0.657); hereditary disease (0.416); leukodystrophy (0.372); Global developmental delay (0.343); Intellectual disability (0.340)
- **Europe PMC papers**: 210
- **Why important**: EPRS1 is a high-connectivity bridge in the module and is supported by STRING links to QARS1, TARS1, CARS1, EIF3C, HSP90AA1 and ALDH18A1. It is also present in the aminoacyl-tRNA synthetase complexes (hu.MAP huMAP3_02637.1) and (hu.MAP huMAP3_13688.1). Its established function is charging glutamyl and prolyl tRNAs, placing it at the intersection of translation, protein demand and the module's strongest recognized complex. Its disease associations include hypomyelinating leukodystrophy and developmental disorders, while its literature volume is more limited than that of canonical receptors or chaperones, making its appearance as a cross-tissue bridge informative.
- **Conclusion**: Established evidence supports EPRS1 as a translation-related structural and functional anchor. It is plausible, but unproven, that EPRS1 coordinates the module's biosynthetic and stress-related components.

#### SF3A1

- **Related proteins** (co-abundance neighbors): UMPS (0.91), ABCF1 (0.87), EML4 (0.85), DYNC1H1 (0.84); STRING partners: DDX46 (0.999), SNW1 (0.989)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_04549.1, huMAP3_06511.1, huMAP3_08980.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a relatively central connector and has exceptionally strong STRING relationships with DDX46 and SNW1. It appears in several hu.MAP spliceosome complexes through (hu.MAP huMAP3_04549.1), (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1). Its established role is in U2 snRNP assembly and pre-mRNA splice-site recognition. It links the module's RNA-processing arm to metabolic, transport and cytoskeletal genes, and it has associations with lymphoma, neurodegenerative disease, diabetes and schizophrenia in the supplied evidence. Its literature volume is substantial, supporting confidence in the annotation.
- **Conclusion**: Established evidence identifies SF3A1 as a spliceosomal anchor. The hypothesis that its co-abundance with transport and metabolic genes marks coordinated RNA-processing demand is reasonable but not demonstrated.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): HSP90AA1 (0.85), DDX46 (0.85), SF3A1 (0.84), SRP72 (0.83), UMPS (0.83), ALDH18A1 (0.82), BCLAF1 (0.82); STRING partners: CAPZB (0.964), HSP90AA1 (0.909)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 is among the most connected genes in the module and links HSP90AA1, DDX46, SF3A1, SRP72, UMPS, ALDH18A1 and BCLAF1. STRING supports known relationships with CAPZB and HSP90AA1. Its established function as a cytoplasmic dynein motor connects retrograde transport, organelle movement, protein sorting and spindle dynamics to the module's RNA, metabolic and membrane systems. It is tissue-enhanced in brain and is associated with spinal muscular atrophy, Charcot-Marie-Tooth disease and intellectual disability. Its literature volume is substantial.
- **Conclusion**: Established evidence supports DYNC1H1 as a transport and architecture bridge. The module may couple cargo transport to biosynthetic and RNA-maintenance capacity, but the co-abundance data do not prove motor-dependent regulation.

#### EGFR

- **Related proteins** (co-abundance neighbors): UFD1 (0.82); STRING partners: CTTN (0.829), EML4 (0.904), HSP90AA1 (0.999), PDCD6IP (0.913)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Golgi apparatus, Plasma membrane; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epidermal growth factor receptor. The protein encoded by this gene is a transmembrane glycoprotein that is a member of the protein kinase superfamily. This protein is a receptor for members of the epidermal growth factor family. EGFR is a cell surface protein that binds to epidermal growth factor, thus inducing receptor dimerization and tyrosine autophosphorylation leading to cell proliferation. Mutations in this gene are associat…
- **Diseases (Open Targets)**: non-small cell lung carcinoma (0.850); lung adenocarcinoma (0.774); cancer (0.737); head and neck squamous cell carcinoma (0.725); lung cancer (0.717)
- **Europe PMC papers**: 223694
- **Why important**: EGFR is a membrane receptor with established kinase signaling and is linked by STRING to CTTN, EML4, HSP90AA1 and PDCD6IP. It is connected to vesicle, cytoskeletal and chaperone biology within the module and is tissue-enhanced in placenta while being detected in liver. Its disease associations and very large literature volume make its functional interpretation particularly well established, especially for proliferative and receptor-signaling biology.
- **Conclusion**: Established evidence supports EGFR as a signaling and membrane-trafficking node rather than evidence for a module-specific role. Its presence raises the hypothesis that extracellular signaling may modulate the conserved maintenance program, but this cannot be inferred causally from co-abundance.

#### ALDH18A1

- **Related proteins** (co-abundance neighbors): MYBBP1A (0.83), DYNC1H1 (0.82), ATP6V0A1 (0.82), EPRS1 (0.81), RCC1 (0.81), ABCF1 (0.81), SRP72 (0.80), UPF1 (0.80); STRING partners: EPRS1 (0.723)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: aldehyde dehydrogenase 18 family member A1. This gene is a member of the aldehyde dehydrogenase family and encodes a bifunctional ATP- and NADPH-dependent mitochondrial enzyme with both gamma-glutamyl kinase and gamma-glutamyl phosphate reductase activities. The encoded protein catalyzes the reduction of glutamate to delta1-pyrroline-5-carboxylate, a critical step in the de novo biosynthesis of proline, ornithine and arginine. Mutations in …
- **Diseases (Open Targets)**: ALDH18A1-related de Barsy syndrome (0.832); cutis laxa, autosomal dominant 3 (0.816); autosomal recessive complex spastic paraplegia type 9B (0.814); de Barsy syndrome (0.731); autosomal dominant spastic paraplegia type 9 (0.706)
- **Europe PMC papers**: 1168
- **Why important**: ALDH18A1 is highly connected and links MYBBP1A, DYNC1H1, ATP6V0A1, EPRS1, RCC1 and SRP72. It is the mitochondrial enzyme initiating proline, ornithine and arginine biosynthesis from glutamate, and it participates with BPNT1 in hu.MAP complex (hu.MAP huMAP3_13468.1). Its established disease associations include de Barsy syndrome and spastic paraplegia, with a substantial literature base. It provides a direct metabolic and mitochondrial connection to the translation, transport and organelle components of the module.
- **Conclusion**: Established evidence supports ALDH18A1 as a metabolic and mitochondrial bridge. A plausible hypothesis is that amino-acid availability and proteome demand help synchronize this module, but the present data do not establish metabolic control of the network.

## Module 4

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (43)**: ABHD10, ACLY, ATP2A2, ATXN10, BAX, CASP3, CNN3, COPB1, DCTN1, DDX6, DIAPH1, DNM1L, EIF3F, FDFT1, GARS1, GMPS, LAMC1, NOP56, NUP155, NUP205, NUP62, PFDN6, PRKDC, PTBP1, PFAS, ADSL, ADSS2, RSL1D1, RPL9, PDCD11, MRPS22, SNRPA1, RUVBL2, PSAT1, SF3B3, SNX6, SRSF7, SUPV3L1, IARS1, TMX1, TXNRD1, TXLNA, TJP2

### Function

The module does not have a GO or KEGG term that passed global correction, so no pathway-level enrichment can be assigned from the primary evidence. Its genes nevertheless suggest a broad cellular-maintenance program spanning nucleocytoplasmic transport through NUP62, NUP155 and NUP205; RNA processing, splicing and ribosome biogenesis through SNRPA1, SF3B3, PTBP1, SRSF7, NOP56, PDCD11 and RSL1D1; purine and nucleotide metabolism through ADSL, GMPS, ADSS2 and PFAS; translation through EIF3F, GARS1, IARS1 and RPL9; and intracellular trafficking, cytoskeletal organization, mitochondrial regulation, calcium handling, lipid metabolism and apoptosis. The network topology is consistent with several connected cellular processes rather than a single specialized tissue function. NUP62 is the strongest network hub, linking nuclear-pore, metabolic, cytoskeletal and trafficking-associated genes. These interpretations are functional annotations and network-based hypotheses, not globally significant enrichment claims.

**Cell composition.** The module is dominated by genes with low tissue specificity in HPA, which is compatible with broadly expressed housekeeping or core cellular functions. Most genes also have low immune-cell specificity, arguing against a module primarily driven by blood-cell composition. Only a small minority are annotated as secreted or extracellular; LAMC1 is secreted to the extracellular matrix, whereas the other highlighted secretome annotations are intracellular or membrane-associated. Thus this is not predominantly a plasma-protein module. Liver protein detection is broad across the module, while several genes show enhanced expression in testis, muscle, placenta or particular reproductive and developmental cell types. The strong representation of housekeeping-like genes means that shared cell states, general biosynthetic demand, or sample-composition effects should be considered before interpreting the module as a liver–autonomic-nervous-system-specific mechanism. HPA provides no matched autonomic-nervous-system protein comparison in this fact sheet.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports several coherent known relationships within the module. The strongest groups include the nuclear-pore relationships among NUP62, NUP155 and NUP205; purine-pathway relationships among ADSL, GMPS, ADSS2, PFAS and ACLY; nucleolar and ribosome-associated relationships involving NOP56, PDCD11, RSL1D1 and RPL9; spliceosome relationships involving SNRPA1 and SF3B3; the apoptosis relationship between BAX and CASP3; and trafficking or cytoskeletal relationships involving DCTN1, SNX6, TJP2 and related genes. These known interactions show that parts of the co-abundance module recapitulate established molecular machinery, but STRING does not provide a supplementary enrichment result for the module as a whole. hu.MAP gives partial support for several complexes: (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_07789.1), (hu.MAP huMAP3_05673.1) and (hu.MAP huMAP3_06791.1) connect PRKDC, NUP205 and ATXN10 or related nuclear and membrane-associated components; (hu.MAP huMAP3_14442.1) connects ADSL, GARS1 and GMPS in a broader metabolic complex; (hu.MAP huMAP3_12581.1) supports the NUP155–NUP62 nuclear-pore relationship; and (hu.MAP huMAP3_06511.1) and (hu.MAP huMAP3_08980.1) support the SNRPA1–SF3B3 spliceosomal relationship. Because each complex contributes only a subset of its members to the module, these results support embedded known complexes rather than a single assembled module complex. Co-abundance edges without STRING or hu.MAP support should be interpreted as coordinated expression, not direct physical binding.

**STRING interactions (score >= 0.7)**: 25 of 903 gene pairs: ACLY–ADSL (0.879); ADSL–ADSS2 (0.999); ADSL–GMPS (0.913); ADSL–PFAS (0.847); ADSS2–GMPS (0.834); BAX–CASP3 (0.884); CASP3–PRKDC (0.732); CASP3–TJP2 (0.806); DCTN1–SNX6 (0.934); EIF3F–RPL9 (0.74); GARS1–IARS1 (0.97); GMPS–NOP56 (0.823); NOP56–PDCD11 (0.997); NOP56–RSL1D1 (0.991); NOP56–RUVBL2 (0.847); NUP155–NUP205 (0.999); NUP155–NUP62 (0.997); NUP205–NUP62 (0.998); PDCD11–RPL9 (0.975); PDCD11–RSL1D1 (0.978); PFDN6–RUVBL2 (0.977); PRKDC–RUVBL2 (0.831); PTBP1–SRSF7 (0.933); RPL9–RSL1D1 (0.858); SF3B3–SNRPA1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09042.1 (PRKDC, NUP205, ATXN10; 3/26); huMAP3_14442.1 (ADSL, GARS1, GMPS; 3/57); huMAP3_09592.1 (ATP2A2, PRKDC, ATXN10; 3/95); huMAP3_07789.1 (PRKDC, NUP205; 2/7); huMAP3_05673.1 (PRKDC, NUP205; 2/11); huMAP3_06791.1 (NUP205, ATXN10; 2/31); huMAP3_12581.1 (NUP155, NUP62; 2/58); huMAP3_06511.1 (SNRPA1, SF3B3; 2/79); huMAP3_08980.1 (SNRPA1, SF3B3; 2/97)

### Novelty

The individual genes and many of their relationships are well established, so the module should not be described as a newly discovered molecular pathway. Its potentially novel aspect is the coordinated abundance pattern shared between autonomic nervous system and liver, particularly the way nuclear transport, RNA processing, purine metabolism, trafficking, cytoskeleton, mitochondrial processes and apoptosis appear together. However, the lack of globally corrected GO or KEGG enrichment, the absence of STRING functional enrichment, the broad low-tissue-specificity profile, and the partial rather than complete hu.MAP overlap all limit a strong novelty claim. Absence of a relationship from STRING or hu.MAP would not establish novelty. Independent replication, tissue-specific cellular deconvolution, perturbation experiments, and comparison with previously reported cross-tissue co-abundance modules would be needed to determine whether the shared pattern is genuinely new rather than a consequence of ubiquitous cellular programs or sample composition.

**Hypothesis.** Hypothesis: the module represents a shared cellular stress and biosynthetic-capacity state in liver and autonomic nervous system tissue. In this model, coordinated nucleotide production, translation, RNA maturation, nuclear transport, mitochondrial and ER-related maintenance, vesicle trafficking, cytoskeletal organization and controlled apoptosis support high-throughput cellular renewal or adaptation. NUP62 and the other nucleoporins could coordinate transport of RNA and proteins; ADSL and GMPS could support nucleotide availability; SNRPA1, SF3B3, NOP56 and PDCD11 could sustain RNA and ribosome maturation; DCTN1, TJP2 and LAMC1 could connect intracellular maintenance with cellular architecture; and BAX with CASP3 could mark a regulated cell-survival or cell-turnover component. This is a mechanistic hypothesis generated from annotations and network structure, not a demonstrated causal pathway or evidence of direct signaling between the two tissues.

### Important genes

#### NUP62

- **Related proteins** (co-abundance neighbors): CNN3 (0.92), TJP2 (0.91), GMPS (0.89), COPB1 (0.89), EIF3F (0.88), GARS1 (0.86), DNM1L (0.86), RSL1D1 (0.86), DDX6 (0.85), TXNRD1 (0.84), DIAPH1 (0.83), ATXN10 (0.83), SNRPA1 (0.81), TXLNA (0.80); STRING partners: NUP155 (0.997), NUP205 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nuclear membrane; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_12581.1
- **Function (MyGene.info)**: nucleoporin 62. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a member of the FG-repeat containing nucleoporins and is localized to the nuclear pore ce…
- **Diseases (Open Targets)**: infantile bilateral striatal necrosis (0.609); familial infantile bilateral striatal necrosis (0.590); HIV infectious disease (0.541); Orthomyxoviridae infectious disease (0.541); viral infectious disease (0.529)
- **Europe PMC papers**: 1582
- **Why important**: NUP62 is the central network hub in the supplied topology and connects many otherwise diverse module components. It is a nucleoporin involved in nucleocytoplasmic transport and is linked by STRING to NUP155 and NUP205, with additional co-abundance links to metabolic, trafficking and cytoskeletal genes. It is detected in liver, has low tissue specificity, and has a substantial literature and disease-association record.
- **Conclusion**: Established evidence supports NUP62 as a nuclear-pore component and as the principal topological connector in this module. The hypothesis that it organizes the cross-process co-abundance pattern is plausible from network position but is not established as a causal role in the shared tissue module.

#### GMPS

- **Related proteins** (co-abundance neighbors): NUP62 (0.89), SNRPA1 (0.85), DCTN1 (0.83), LAMC1 (0.83), CNN3 (0.81); STRING partners: ADSL (0.913), ADSS2 (0.834), NOP56 (0.823)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria, Cytosol; IHC detected in none
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: guanosine monophosphate synthase. In the de novo synthesis of purine nucleotides, IMP is the branch point metabolite at which point the pathway diverges to the synthesis of either guanine or adenine nucleotides. In the guanine nucleotide pathway, there are 2 enzymes involved in converting IMP to GMP, namely IMP dehydrogenase (IMPD1), which catalyzes the oxidation of IMP to XMP, and GMP synthetase, which catalyzes the amination of …
- **Diseases (Open Targets)**: rheumatoid arthritis (0.277); nephrotic syndrome (0.259); lupus nephritis (0.259); rhabdomyosarcoma (0.247); hepatocellular carcinoma (0.237)
- **Europe PMC papers**: 5161
- **Why important**: GMPS is a core enzyme in guanine-nucleotide biosynthesis and occupies a bridge position between the module's metabolic and RNA-associated portions. It has STRING relationships with ADSL, ADSS2 and NOP56 and is represented in hu.MAP complex (hu.MAP huMAP3_14442.1). HPA shows tissue enhancement in testis and cell-type enhancement in spermatogenic populations, while the fact sheet reports disease associations including hepatocellular carcinoma.
- **Conclusion**: Established evidence supports GMPS as a purine-biosynthetic enzyme and as part of a known interaction neighborhood. Its coordinated abundance may reflect nucleotide demand or biosynthetic state, but a specific liver–autonomic-nervous-system role remains a hypothesis.

#### PRKDC

- **Related proteins** (co-abundance neighbors): RUVBL2 (0.88), EIF3F (0.86), RSL1D1 (0.85), SF3B3 (0.83); STRING partners: CASP3 (0.732), RUVBL2 (0.831)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_09042.1, huMAP3_09592.1, huMAP3_07789.1, huMAP3_05673.1
- **Function (MyGene.info)**: protein kinase, DNA-activated, catalytic subunit. This gene encodes the catalytic subunit of the DNA-dependent protein kinase (DNA-PK). It functions with the Ku70/Ku80 heterodimer protein in DNA double strand break repair and recombination. The protein encoded is a member of the PI3/PI4-kinase family.[provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to DNA-PKcs deficiency (0.752); neurodegenerative disease (0.548); severe combined immunodeficiency (0.470); combined immunodeficiency (0.464); ovarian neoplasm (0.210)
- **Europe PMC papers**: 12461
- **Why important**: PRKDC encodes the catalytic subunit of DNA-dependent protein kinase and is annotated for DNA repair, double-strand-break repair, telomere maintenance and innate immune activation. It connects to RUVBL2, EIF3F, RSL1D1 and CASP3 in STRING and appears in several hu.MAP complexes, including (hu.MAP huMAP3_09042.1), (hu.MAP huMAP3_09592.1), (hu.MAP huMAP3_07789.1) and (hu.MAP huMAP3_05673.1). It has the largest literature volume among the highlighted genes and disease associations involving DNA-PK deficiency and immune disease.
- **Conclusion**: Established evidence supports PRKDC as a DNA-repair and genome-maintenance factor embedded in several known complexes. Its presence may indicate genome-integrity maintenance or stress response in the module, but the co-abundance data do not show that DNA damage is the initiating process.

#### DCTN1

- **Related proteins** (co-abundance neighbors): PDCD11 (0.94), DIAPH1 (0.86), LAMC1 (0.84), GMPS (0.83), CNN3 (0.82); STRING partners: SNX6 (0.934)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Microtubules; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynactin subunit 1. This gene encodes the largest subunit of dynactin, a macromolecular complex consisting of 10 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein. Dynactin is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, chromosome movement, nuclear positi…
- **Diseases (Open Targets)**: Perry syndrome (0.798); amyotrophic lateral sclerosis (0.764); neuronopathy, distal hereditary motor, type 7B (0.743); cancer (0.547); neurodegenerative disease (0.530)
- **Europe PMC papers**: 1985
- **Why important**: DCTN1 is the largest dynactin subunit and connects microtubule-based transport with ER-to-Golgi transport, organelle movement, nuclear positioning and axonogenesis. Within the module it links PDCD11, DIAPH1, LAMC1, GMPS and CNN3, and STRING supports a relationship with SNX6. It is detected in liver, is enhanced in other brain neurons, and has strong disease associations with Perry syndrome, amyotrophic lateral sclerosis and hereditary neuronopathy.
- **Conclusion**: Established evidence supports DCTN1 as a cytoskeletal transport and neuronal-maintenance factor. Its position suggests that intracellular transport may connect several module processes, but whether it explains sharing between autonomic nervous system and liver is a hypothesis requiring cell-type and perturbation evidence.

#### TJP2

- **Related proteins** (co-abundance neighbors): COPB1 (0.94), NUP62 (0.91), CNN3 (0.86); STRING partners: CASP3 (0.806)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tight junction protein 2. This gene encodes a zonula occluden that is a member of the membrane-associated guanylate kinase homolog family. The encoded protein functions as a component of the tight junction barrier in epithelial and endothelial cells and is necessary for proper assembly of tight junctions. Mutations in this gene have been identified in patients with hypercholanemia, and genomic duplication of a 270 kb regio…
- **Diseases (Open Targets)**: cholestasis, progressive familial intrahepatic, 4 (0.800); hypercholanemia, familial 1 (0.647); autosomal dominant nonsyndromic hearing loss (0.558); progressive familial intrahepatic cholestasis type 2 (0.527); deafness (0.467)
- **Europe PMC papers**: 1748
- **Why important**: TJP2 is a tight-junction component involved in epithelial and endothelial barrier organization, cell adhesion and maintenance of the blood–brain barrier. It connects NUP62, CNN3 and COPB1 in the module, and STRING links it with CASP3. Its liver detection and associations with progressive familial intrahepatic cholestasis and hypercholanemia make it especially relevant to the liver side of the tissue pair.
- **Conclusion**: Established evidence supports TJP2 as a barrier and junctional protein with important liver disease associations. Its co-abundance with nuclear transport and trafficking genes may reflect coordinated epithelial integrity or cellular architecture, but a direct mechanistic bridge to autonomic nervous system biology is not established.

## Module 5

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (44)**: ANXA5, APEX1, BLMH, CLIC1, COXFA4, DSTN, EIF2B5, ELOC, GAR1, HSP90AB2P, EIF4E, ISYNA1, PKM, LSM5, EEF1E1, MAT2A, CHCHD3, MOGS, MTFP1, MYG1, NDUFAF4, OXA1L, PDXK, PGK1, PDXP, LCP1, CTSA, PSMD13, PSMF1, RAB10, RAN, MRPL11, RPRD1B, SRRT, FARSB, VARS1, WARS1, YARS1, YARS2, TACO1, TUBB4B, CCT8, NAE1, XRCC6

### Function

No GO or KEGG term passed global correction for this module, and STRING functional enrichment was absent. Therefore, the function should be inferred from the gene composition and network rather than from statistically significant pathway enrichment. The strongest coherent signals are constitutive cellular maintenance processes: cytosolic and mitochondrial translation, aminoacyl-tRNA charging, glycolysis, mitochondrial respiratory-chain biogenesis, proteasome-associated protein turnover, DNA repair, RNA processing, and protein folding. The network hubs APEX1, YARS1, and PKM connect several of these processes, while YARS2, OXA1L, and MRPL11 provide a mitochondrial translation and respiratory-chain axis. This is best interpreted as a broad cellular proteostasis, translation, energy-metabolism, and genome-maintenance module rather than as a tissue-specific autonomic or hepatic pathway. The module may represent coordinated abundance of core cellular machinery across the two tissues, but co-abundance does not establish direct regulation or physical interaction.

**Cell composition.** The HPA profile argues against a plasma-protein or secreted-protein module: only a single module gene is annotated as secreted, and the blood-cell profile is predominantly low immune-cell specificity. The genes are also not dominated by a single blood lineage. Instead, most annotated genes have low tissue specificity, with a smaller set showing tissue or cell-type enhancement across diverse tissues and cell types, including germ-cell, epithelial, muscle, neural, placental, and vascular populations. This breadth is compatible with broadly expressed housekeeping-like cellular machinery, although the presence of cell-type-enhanced genes means that cellular composition cannot be excluded. Liver protein detection is widespread among the measured genes, whereas autonomic-nervous-system matching HPA protein data are unavailable. The shared module therefore could reflect conserved cellular activity in the sampled tissues, technical or abundance-linked co-regulation, or shared cell states; the evidence does not support interpreting it primarily as blood contamination.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING supports a concentrated set of established relationships rather than a densely connected whole-module interactome. The clearest known interaction cluster is formed by YARS1, YARS2, WARS1, VARS1, and FARSB, consistent with aminoacyl-tRNA synthetase biology. PKM is linked to PGK1, PDXK to PDXP, MRPL11 to OXA1L, and CCT8 to RAN and TUBB4B. These relationships provide biological anchors for translation, glycolysis, vitamin B-six metabolism, mitochondrial function, and protein handling, but STRING functional enrichment is absent and the remaining module edges are not independently established physical interactions. hu.MAP supplies partial complex support. APEX1, PKM, and YARS1 co-occur in (hu.MAP huMAP3_14442.1); OXA1L, YARS2, and MRPL11 recur together in mitochondrial ribosome-associated complexes (hu.MAP huMAP3_06550.1), (hu.MAP huMAP3_08458.1), (hu.MAP huMAP3_09483.1), (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_04652.1), (hu.MAP huMAP3_07939.1), and (hu.MAP huMAP3_09113.1); APEX1 and YARS1 recur in several complexes (hu.MAP huMAP3_04783.1), (hu.MAP huMAP3_10115.1), and (hu.MAP huMAP3_13998.1); and PSMF1 with PSMD13 occurs in proteasome complexes (hu.MAP huMAP3_09656.1) and (hu.MAP huMAP3_13725.1). These are partial overlaps with larger complexes, so they support shared molecular context but do not demonstrate that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 14 of 946 gene pairs: CCT8–RAN (0.712); CCT8–TUBB4B (0.717); FARSB–VARS1 (0.776); FARSB–YARS1 (0.946); FARSB–YARS2 (0.705); MRPL11–OXA1L (0.874); PDXK–PDXP (0.966); PGK1–PKM (0.936); VARS1–WARS1 (0.901); VARS1–YARS1 (0.956); VARS1–YARS2 (0.878); WARS1–YARS1 (0.997); WARS1–YARS2 (0.932); YARS1–YARS2 (0.974)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_14442.1 (PKM, APEX1, YARS1; 3/57); huMAP3_06550.1 (OXA1L, YARS2, MRPL11; 3/62); huMAP3_08458.1 (OXA1L, YARS2, MRPL11; 3/70); huMAP3_09483.1 (OXA1L, YARS2, MRPL11; 3/74); huMAP3_06589.1 (OXA1L, YARS2, MRPL11; 3/79); huMAP3_04783.1 (APEX1, YARS1; 2/4); huMAP3_10115.1 (APEX1, YARS1; 2/14); huMAP3_13998.1 (APEX1, YARS1; 2/23); huMAP3_04652.1 (YARS2, MRPL11; 2/30); huMAP3_09656.1 (PSMF1, PSMD13; 2/64); huMAP3_13725.1 (PSMF1, PSMD13; 2/69); huMAP3_07939.1 (YARS2, MRPL11; 2/68); huMAP3_09113.1 (YARS2, MRPL11; 2/72)

### Novelty

The co-abundance module may be a new cross-tissue observation, but the available evidence is insufficient to call it a newly discovered molecular pathway. Its principal components and relationships are largely established: aminoacyl-tRNA synthetases have known functional links in STRING, mitochondrial translation components recur in hu.MAP, PKM and PGK1 are established glycolytic partners, and proteasome subunits are represented in hu.MAP. Conversely, the absence of a STRING enrichment result or the absence of some genes from hu.MAP does not prove novelty. The potentially novel aspect is the coordinated abundance pattern linking translation, mitochondrial machinery, glycolysis, DNA repair, proteostasis, and RNA processing across autonomic nervous system and liver. That claim requires replication in independent cohorts, assessment of cell composition, and comparison with published cross-tissue co-expression modules.

**Hypothesis.** Hypothesis: this module reflects a conserved cellular resource-allocation state shared by autonomic nervous system and liver, in which translational capacity and proteostasis are coordinated with glycolytic energy production, mitochondrial respiratory-chain assembly, RNA processing, and DNA repair. A possible mechanistic chain is that cellular energetic or proteotoxic demand increases glycolytic activity through PKM and PGK1, supports cytosolic and mitochondrial protein synthesis through YARS1, YARS2, WARS1, VARS1, and FARSB, and requires mitochondrial assembly factors such as OXA1L and MRPL11. APEX1, RPRD1B, RAN, and associated nuclear factors could couple this state to genome maintenance and transcriptional processing, while proteasome-associated genes could support quality control. This remains a hypothesis: the co-abundance network and partial complex overlaps do not establish directionality, causality, or a single shared physical pathway.

### Important genes

#### APEX1

- **Related proteins** (co-abundance neighbors): YARS2 (0.86), PSMD13 (0.85), PKM (0.85), ISYNA1 (0.84), NAE1 (0.83), CLIC1 (0.82), RPRD1B (0.81), NDUFAF4 (0.81), MTFP1 (0.80), HSP90AB2P (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_04783.1, huMAP3_10115.1, huMAP3_13998.1
- **Function (MyGene.info)**: apurinic/apyrimidinic endodeoxyribonuclease 1. The APEX gene encodes the major AP endonuclease in human cells. It encodes the APEX endonuclease, a DNA repair enzyme with apurinic/apyrimidinic (AP) activity. Such AP activity sites occur frequently in DNA molecules by spontaneous hydrolysis, by DNA damaging agents or by DNA glycosylases that remove specific abnormal bases. The AP sites are the most frequent pre-mutagenic lesions that can prevent…
- **Diseases (Open Targets)**: neurodegenerative disease (0.464); Galloway-Mowat syndrome (0.429); hereditary disease (0.161); neoplasm (0.118); non-small cell lung carcinoma (0.115)
- **Europe PMC papers**: 2928
- **Why important**: APEX1 is a central network hub and connects to YARS2, PSMD13, PKM, ISYNA1, NAE1, CLIC1, RPRD1B, and NDUFAF4. Its established function is the major apurinic/apyrimidinic endonuclease in base-excision DNA repair, and it is represented in several hu.MAP overlaps, including (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_04783.1), (hu.MAP huMAP3_10115.1), and (hu.MAP huMAP3_13998.1). It has liver protein detection, broad tissue and cell-type distribution, disease associations involving neurodegenerative disease and Galloway-Mowat syndrome, and substantial literature support.
- **Conclusion**: Established evidence supports APEX1 as a highly connected DNA-repair component embedded in a broader cellular-maintenance network. Its co-abundance with translation, glycolysis, and mitochondrial genes suggests coordinated cellular stress or maintenance biology, but the module does not prove that APEX1 regulates those processes. A role for APEX1 as a mechanistic bridge is therefore plausible but remains hypothetical.

#### YARS1

- **Related proteins** (co-abundance neighbors): YARS2 (0.92), GAR1 (0.88), EIF2B5 (0.84), BLMH (0.84), NAE1 (0.84), PKM (0.84), MYG1 (0.83), RPRD1B (0.81), HSP90AB2P (0.80); STRING partners: FARSB (0.946), VARS1 (0.956), WARS1 (0.997), YARS2 (0.974)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_14442.1, huMAP3_04783.1, huMAP3_10115.1, huMAP3_13998.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 1. Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. Tyrosyl-tRNA synthetase belongs to the class I tRNA synthetase family. Cytokine activities have also been observ…
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease dominant intermediate C (0.739); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset 2 (0.707); hereditary disease (0.509); Charcot-Marie-Tooth disease (0.418); neurologic, endocrine, and pancreatic disease, multisystem, infantile-onset (0.333)
- **Europe PMC papers**: 215
- **Why important**: YARS1 is one of the strongest network hubs and has direct STRING relationships with FARSB, VARS1, WARS1, and YARS2. It encodes the cytosolic tyrosyl-tRNA synthetase and is annotated for tRNA aminoacylation, translation, stress, starvation, and apoptosis-related biology. It participates in hu.MAP overlaps (hu.MAP huMAP3_14442.1), (hu.MAP huMAP3_04783.1), (hu.MAP huMAP3_10115.1), and (hu.MAP huMAP3_13998.1), has liver protein detection, broad tissue distribution, disease associations including Charcot-Marie-Tooth disease and multisystem neurologic disease, and meaningful literature support.
- **Conclusion**: Established evidence identifies YARS1 as a central translation-related anchor and the main connector of the aminoacyl-tRNA synthetase cluster. Its position makes it an important marker of the module's translational component. The data do not establish that altered YARS1 drives the cross-tissue module or that its noncanonical cytokine activities operate here.

#### PKM

- **Related proteins** (co-abundance neighbors): PSMD13 (0.92), TUBB4B (0.87), BLMH (0.85), APEX1 (0.85), CCT8 (0.85), YARS1 (0.84), WARS1 (0.83), ANXA5 (0.81); STRING partners: PGK1 (0.936)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_14442.1
- **Function (MyGene.info)**: pyruvate kinase M1/2. This gene encodes a protein involved in glycolysis. The encoded protein is a pyruvate kinase that catalyzes the transfer of a phosphoryl group from phosphoenolpyruvate to ADP, generating ATP and pyruvate. This protein has been shown to interact with thyroid hormone and may mediate cellular metabolic effects induced by thyroid hormones. This protein has been found to bind Opa protein, a bacterial o…
- **Diseases (Open Targets)**: neurodegenerative disease (0.457); autoimmune disorder of central nervous system (0.370); tympanic membrane perforation (0.204); neoplasm (0.121); hepatocellular carcinoma (0.120)
- **Europe PMC papers**: 8544
- **Why important**: PKM is a prominent network hub linked to PSMD13, TUBB4B, BLMH, APEX1, CCT8, YARS1, WARS1, and ANXA5, and it has a strong STRING relationship with PGK1. It is the glycolytic pyruvate kinase, is included with APEX1 and YARS1 in (hu.MAP huMAP3_14442.1), shows liver protein detection, and has tissue enhancement in skeletal muscle and tongue. Its disease associations include neurodegenerative disease and hepatocellular carcinoma, and it has extensive literature support.
- **Conclusion**: Established evidence supports PKM as the module's clearest energy-metabolism anchor and as a connector between glycolysis, translation-associated genes, cytoskeletal proteins, and proteasome-related genes. Its co-abundance may indicate shared energetic demand or cell-state composition. It does not demonstrate a liver-specific metabolic program because global enrichment was not significant and PKM is broadly used across tissues.

#### YARS2

- **Related proteins** (co-abundance neighbors): YARS1 (0.92), APEX1 (0.86), EIF4E (0.85), PSMD13 (0.83); STRING partners: FARSB (0.705), VARS1 (0.878), WARS1 (0.932), YARS1 (0.974)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06550.1, huMAP3_08458.1, huMAP3_09483.1, huMAP3_06589.1, huMAP3_04652.1, huMAP3_07939.1, huMAP3_09113.1
- **Function (MyGene.info)**: tyrosyl-tRNA synthetase 2. This gene encodes a mitochondrial protein that catalyzes the attachment of tyrosine to tRNA(Tyr). Mutations in this gene are associated with myopathy with lactic acidosis and sideroblastic anemia type 2 (MLASA2). [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: myopathy, lactic acidosis, and sideroblastic anemia (0.794); mitochondrial disease (0.509); neurodegenerative disease (0.478); hereditary disease (0.452); pericarditis (0.214)
- **Europe PMC papers**: 430
- **Why important**: YARS2 links the cytosolic aminoacyl-tRNA synthetase cluster to mitochondrial biology. It is connected in STRING to FARSB, VARS1, WARS1, and YARS1, and it repeatedly overlaps with OXA1L and MRPL11 in mitochondrial hu.MAP complexes (hu.MAP huMAP3_06550.1), (hu.MAP huMAP3_08458.1), (hu.MAP huMAP3_09483.1), (hu.MAP huMAP3_06589.1), (hu.MAP huMAP3_04652.1), (hu.MAP huMAP3_07939.1), and (hu.MAP huMAP3_09113.1). It encodes mitochondrial tyrosyl-tRNA synthetase and is associated with myopathy, lactic acidosis, and sideroblastic anemia, as well as mitochondrial disease and neurodegenerative disease.
- **Conclusion**: Established evidence supports YARS2 as a mitochondrial translation component that gives the module a specific mitochondrial dimension beyond generic housekeeping. Its connection to YARS1 suggests coordination between cytosolic and mitochondrial translation. The module does not establish that mitochondrial translation dysfunction caused the observed cross-tissue co-abundance.

#### OXA1L

- **Related proteins** (co-abundance neighbors): PSMD13 (0.81); STRING partners: MRPL11 (0.874)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in none
- **hu.MAP 3.0**: huMAP3_06550.1, huMAP3_08458.1, huMAP3_09483.1, huMAP3_06589.1
- **Function (MyGene.info)**: OXA1L mitochondrial inner membrane insertase. This gene encodes an evolutionarily conserved protein that is localized to the inner mitochondrial membrane. The encoded protein is essential for the translocation of the N-terminal tail of subunit 2 of cytochrome c oxidase, and is involved in the assembly of the cytochrome c oxidase and ATPase complexes of the mitochondrial respiratory chain. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: lysinuric protein intolerance (0.573); mitochondrial disease (0.465); hereditary disease (0.192); autoinflammatory syndrome (0.179); gastroparesis (0.114)
- **Europe PMC papers**: 385
- **Why important**: OXA1L is part of the mitochondrial interaction cluster with YARS2 and MRPL11 across multiple hu.MAP complexes and has a STRING relationship with MRPL11. It is an inner-mitochondrial-membrane insertase required for respiratory-chain and ATPase-complex assembly, and it is associated with mitochondrial disease and lysinuric protein intolerance. Its network degree is limited, but its functional specificity makes it informative despite not being a hub.
- **Conclusion**: Established evidence supports OXA1L as a mitochondrial respiratory-chain assembly component that complements the mitochondrial translation signal represented by YARS2 and MRPL11. Its presence strengthens the interpretation of coordinated mitochondrial maintenance. The limited network connectivity and absent liver protein detection caution against treating OXA1L as a dominant driver of the entire module.

#### RPRD1B

- **Related proteins** (co-abundance neighbors): PSMF1 (0.86), ELOC (0.82), RAB10 (0.82), CLIC1 (0.82), APEX1 (0.81), YARS1 (0.81), CTSA (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: regulation of nuclear pre-mRNA domain containing 1B. Enables RNA polymerase II complex binding activity and identical protein binding activity. Involved in positive regulation of cell population proliferation; regulation of cell cycle process; and regulation of transcription by RNA polymerase II. Located in nucleoplasm. Part of RNA polymerase II, holoenzyme. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.399); alcohol drinking (0.167); gastric carcinoma (0.153); neoplasm (0.115); colorectal carcinoma (0.101)
- **Europe PMC papers**: 260
- **Why important**: RPRD1B is a relatively well-connected nuclear gene linked to PSMF1, ELOC, RAB10, CLIC1, APEX1, YARS1, and CTSA. It binds RNA polymerase II and is involved in transcriptional regulation, cell-cycle regulation, promoter clearance, and messenger-RNA processing. HPA shows liver tissue enhancement and liver protein detection. Its disease associations include neurodegenerative disease and several cancers, while its literature volume is more limited than that of APEX1 or PKM.
- **Conclusion**: Established evidence supports RPRD1B as a nuclear transcription and RNA-processing component that may connect the module's metabolic and translational signals to gene-expression control. Its liver enhancement is compatible with a tissue-relevant contribution, but this is not evidence of a liver-specific mechanism. Any role as a transcriptional coordinator of the module remains a hypothesis.

## Module 6

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (7)**: ARPC5L, CAPN1, EIF2B2, FNTA, REXO2, MRPL13, SCFD1

### Function

No GO or KEGG term passed global correction, and no STRING functional-enrichment term was reported. The module therefore has no statistically supported single pathway interpretation. Its genes span translational initiation, intracellular vesicle transport, mitochondrial translation, mitochondrial RNA surveillance, protein prenylation, actin nucleation and cell migration, and intracellular calcium-activated proteolysis. The most cautious interpretation is a mixed cellular-maintenance module involving protein synthesis, mitochondrial RNA and protein handling, vesicle trafficking, cytoskeletal regulation, and proteolysis.

**Cell composition.** No module member is annotated as secreted, and all members have low immune-cell specificity. No enriched blood-cell population was reported, so the supplied HPA evidence does not support a blood-cell contamination explanation. Liver protein detection is present for every module member. Most genes have low tissue specificity, whereas CAPN1 is tissue enhanced in esophagus. Several genes show cell-type-enhanced expression in esophageal epithelial cells, reproductive cells, trophoblast-related cells, or parietal cells. The pattern is more consistent with broadly expressed cellular machinery and possible shared cell-state variation than with a liver-specific or autonomic-nervous-system-specific program. Matching autonomic-nervous-system HPA protein data are unavailable.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING gene pair met the supplied high-confidence interaction threshold, and no STRING functional-enrichment term was reported. No hu.MAP complex contained multiple module members. The co-abundance relationships are therefore not corroborated by the supplied curated interaction or complex resources and should not be interpreted as direct physical binding. Internally, EIF2B2 connects with ARPC5L, SCFD1, and CAPN1; SCFD1 connects with FNTA and MRPL13; and MRPL13 connects with REXO2. These relationships support coordinated abundance in the analysed data but do not establish a common molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The particular co-abundance pattern may be dataset-specific, but it cannot be claimed as a new biological mechanism from these data alone. Its lack of STRING and hu.MAP support means that the combination is not represented in the supplied reference resources, but database absence does not prove novelty. The absence of globally significant GO or KEGG enrichment also prevents assigning a newly discovered pathway label. A stronger novelty claim would require replication in independent datasets, adjustment for cell composition, and comparison with published co-expression and proteomic modules.

**Hypothesis.** Hypothesis: the module reflects coordinated variation in a general cellular-maintenance state that couples translational control and mitochondrial RNA handling with vesicle trafficking, protein prenylation, cytoskeletal remodeling, and calcium-dependent proteolysis. EIF2B2 and SCFD1 may act as abundance bridges between translation-related and trafficking-related processes, while MRPL13 and REXO2 form a mitochondrial branch. CAPN1 and ARPC5L may represent proteolytic and cytoskeletal outputs of the same cell state. This is a testable hypothesis, not an established pathway. A competing explanation is shared cell-state or cell-composition variation across the tissues.

### Important genes

#### EIF2B2

- **Related proteins** (co-abundance neighbors): ARPC5L (0.89), SCFD1 (0.83), CAPN1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Focal adhesion sites; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: eukaryotic translation initiation factor 2B subunit beta. This gene encodes the beta subunit of eukaryotic initiation factor-2B (EIF2B). EIF2B is involved in protein synthesis and exchanges GDP and GTP for its activation and deactivation. [provided by RefSeq, Aug 2011].
- **Diseases (Open Targets)**: leukoencephalopathy with vanishing white matter (0.812); leukoencephalopathy with vanishing white matter 1 (0.720); leukoencephalopathy with vanishing white matter 2 (0.643); ovarioleukodystrophy (0.557); neurodegenerative disease (0.550)
- **Europe PMC papers**: 540
- **Why important**: EIF2B2 is a central network node connecting ARPC5L, SCFD1, and CAPN1. It encodes a subunit of EIF2B, which regulates translational initiation, and is associated with vanishing-white-matter leukoencephalopathy and related neurological disease. Its substantial literature base and central network position make it the strongest candidate for anchoring interpretation of the module.
- **Conclusion**: Established evidence supports EIF2B2 as a translation-initiation regulator and central co-abundance hub. The module does not establish that EIF2B2 drives the other genes or that it represents a neurological disease mechanism. Its organizing role is therefore a hypothesis.

#### SCFD1

- **Related proteins** (co-abundance neighbors): FNTA (0.89), EIF2B2 (0.83), MRPL13 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: sec1 family domain containing 1. Predicted to enable syntaxin binding activity. Involved in negative regulation of autophagosome assembly; regulation of protein transport; and response to toxic substance. Located in cis-Golgi network. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.527); bronchial disorder (0.270); placental retention (0.240); bladder calculus (0.205); amyotrophic lateral sclerosis (0.195)
- **Europe PMC papers**: 391
- **Why important**: SCFD1 connects FNTA, EIF2B2, and MRPL13. It is annotated for syntaxin binding, Golgi localization, intracellular protein transport, and endoplasmic-reticulum-to-Golgi trafficking. It also has disease associations involving neurodegenerative disease and amyotrophic lateral sclerosis, supported by a substantial literature base. Its bridging position makes it a strong candidate for linking trafficking with the other module processes.
- **Conclusion**: Established evidence supports SCFD1 in intracellular vesicle transport and syntaxin-related biology. Its network position supports coordinated abundance with the translation and mitochondrial branches, but direct physical interaction and causal control are not demonstrated.

#### MRPL13

- **Related proteins** (co-abundance neighbors): REXO2 (0.83), SCFD1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitochondrial ribosomal protein L13. Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and p…
- **Diseases (Open Targets)**: neurodegenerative disease (0.357); asthma (0.196); refractive error (0.178); pathological myopia (0.138); Abnormality of the immune system (0.133)
- **Europe PMC papers**: 478
- **Why important**: MRPL13 connects SCFD1 with REXO2 and encodes a mitochondrial ribosomal protein involved in mitochondrial translation. It gives the module a defined mitochondrial protein-synthesis component and has disease associations involving neurodegenerative disease and immune-system abnormalities. Its literature base makes it an informative marker of the mitochondrial branch.
- **Conclusion**: Established evidence supports MRPL13 as a mitoribosomal component involved in mitochondrial translation. Its co-abundance with REXO2 is compatible with coordinated mitochondrial RNA and protein handling, but does not prove a shared complex or a specific mitochondrial stress response.

#### CAPN1

- **Related proteins** (co-abundance neighbors): EIF2B2 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calpain 1. The calpains, calcium-activated neutral proteases, are nonlysosomal, intracellular cysteine proteases. The mammalian calpains include ubiquitous, stomach-specific, and muscle-specific proteins. The ubiquitous enzymes consist of heterodimers with distinct large, catalytic subunits associated with a common small, regulatory subunit. This gene encodes the large subunit of the ubiquitous enzyme, calpa…
- **Diseases (Open Targets)**: Autosomal recessive spastic paraplegia type 76 (0.781); Alzheimer disease (0.383); neurodegenerative disease (0.326); hereditary spastic paraplegia 11 (0.266); hereditary disease (0.193)
- **Europe PMC papers**: 1869
- **Why important**: CAPN1 connects to EIF2B2 and is the module member with tissue-enhanced HPA expression in esophagus. It encodes an intracellular calcium-activated cysteine protease involved in proteolysis, macroautophagy regulation, and glutamate-receptor signaling. It has the largest literature base among the module genes and established associations with spastic paraplegia and neurodegenerative disease.
- **Conclusion**: Established evidence supports CAPN1 as an intracellular calcium-dependent protease with regulatory roles in cells. Its connection to EIF2B2 may reflect coordinated cell-state variation, but the module does not demonstrate that CAPN1 directly couples proteolysis to translational control.

#### FNTA

- **Related proteins** (co-abundance neighbors): SCFD1 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: farnesyltransferase, CAAX box, subunit alpha. Prenyltransferases can attach either a farnesyl group or a geranylgeranyl group in thioether linkage to the cysteine residue of proteins with a C-terminal CAAX box. CAAX geranylgeranyltransferase and CAAX farnesyltransferase are heterodimers that share the same alpha subunit but have different beta subunits. This gene encodes the alpha subunit of these transferases. Alternative splicing results in…
- **Diseases (Open Targets)**: Hutchinson-Gilford progeria syndrome (0.547); neurodegenerative disease (0.540); laminopathy (0.370); progeroid syndrome (0.370); myelodysplastic syndrome (0.357)
- **Europe PMC papers**: 544
- **Why important**: FNTA is connected to SCFD1 and encodes the shared alpha subunit of CAAX prenyltransferases, which mediate protein farnesylation and geranylgeranylation. It is associated with progeroid syndromes, laminopathies, and neurodegenerative disease and has a substantial literature base. Although peripheral in the network, it provides a plausible membrane-associated signaling component.
- **Conclusion**: Established evidence supports FNTA as a prenyltransferase alpha subunit involved in lipid modification of CAAX-containing proteins. Its co-abundance with SCFD1 is compatible with coordinated membrane or trafficking biology, but the module does not establish a direct FNTA-SCFD1 interaction.

## Module 7

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (7)**: ATAD3A, CORO1C, GET3, MAT2B, SEC24C, U2SURP, THOP1

### Function

No GO or KEGG term passed global correction, so the module does not support a statistically established pathway-level function from enrichment. Its annotated genes span several cellular processes: RNA processing through U2SURP, endoplasmic-reticulum and vesicle trafficking through SEC24C and GET3, mitochondrial organization and cholesterol-related biology through ATAD3A, actin and signaling processes through CORO1C, methionine-related metabolism through MAT2B, and cytosolic peptide processing through THOP1. The co-abundance structure therefore appears more consistent with a mixed cellular-maintenance or cell-state module than with a narrowly defined pathway. A possible interpretation is coordinated variation in intracellular protein handling, organelle maintenance, and regulatory metabolism, but this remains an interpretation rather than an enrichment-supported conclusion.

**Cell composition.** The module is not dominated by secreted or plasma proteins: no member is annotated as secreted. All members have low tissue specificity and low immune-cell specificity, arguing against a clearly blood-derived or broadly immune-cell module. The cell-type annotations are heterogeneous, including esophageal epithelial populations, oocytes, late spermatids, colonocytes, enterocytes, hepatocytes, and platelets, with no single cell type dominating the evidence. This heterogeneity, together with broad tissue distribution, suggests that the shared signal could reflect common intracellular biology, mixed cell composition, or sample-level cellular state rather than a specialized autonomic-nervous-system or liver program. Liver protein detection supports presence of most members in liver, whereas there is no matching HPA tissue for the autonomic nervous system; GET3 was not detected in liver by the reported HPA assay.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the reported high-confidence threshold, and there was no supplementary STRING functional-enrichment result. No hu.MAP complex contained multiple module members. Thus, the external interaction resources provide no established physical-complex support for the module. The co-abundance graph itself links U2SURP with SEC24C, CORO1C, and ATAD3A; SEC24C with MAT2B; ATAD3A with THOP1; and CORO1C with GET3. These are observed abundance relationships, not established protein interactions. Their lack of confirmation in STRING and hu.MAP favors interpreting the graph as a tissue-shared co-regulation or cellular-state association rather than a known molecular complex.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This may be a novel co-abundance observation because the complete module is not represented by a matching high-confidence STRING interaction network or a shared hu.MAP complex. However, that absence does not establish biological novelty: databases are incomplete, co-abundance relationships need not be physical interactions, and the module has no globally significant GO or KEGG enrichment to provide independent pathway support. The heterogeneous HPA cell-type pattern also raises the possibility that the signal reflects shared cell composition or a general intracellular state. A strong novelty claim would require replication in independent autonomic-nervous-system and liver datasets, preservation after cell-composition adjustment, and comparison with published co-expression modules.

**Hypothesis.** Hypothesis: the module reflects coordinated regulation of intracellular protein and organelle homeostasis across the two tissue groups. In this model, SEC24C and GET3 represent endoplasmic-reticulum cargo handling and membrane-protein insertion, ATAD3A represents mitochondrial organization and metabolic coordination, U2SURP represents RNA-processing support, CORO1C represents cytoskeletal and signaling regulation, and MAT2B and THOP1 represent metabolic and peptide-processing inputs. Their shared abundance could arise from a common cellular-maintenance state or from coordinated variation in hepatocyte and other epithelial-like cellular content. This hypothesis is not proven by enrichment or interaction evidence and should be tested experimentally and in independent cohorts.

### Important genes

#### U2SURP

- **Related proteins** (co-abundance neighbors): SEC24C (0.83), CORO1C (0.83), ATAD3A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: U2 snRNP associated SURP domain containing. Enables RNA binding activity. Predicted to be involved in RNA processing. Located in nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: dengue disease (0.370); arthropathy (0.277); neurodegenerative disease (0.264); alcohol drinking (0.244); Hypercholesterolemia (0.207)
- **Europe PMC papers**: 228
- **Why important**: U2SURP has the strongest network position in the module and connects the RNA-processing annotation to SEC24C, CORO1C, and ATAD3A. Its nucleoplasmic localization and RNA-binding role provide a plausible regulatory bridge between transcript processing and the other cellular systems represented in the module. It has a substantial literature base, although its disease associations in the fact sheet are mainly broad or exploratory.
- **Conclusion**: Established evidence supports U2SURP as an RNA-processing factor and as the most central abundance node in this module. It is a reasonable candidate for coordinating the module signal, but there is no enrichment, STRING, or hu.MAP evidence establishing it as a physical or mechanistic organizer. Its proposed bridging role is therefore a hypothesis.

#### SEC24C

- **Related proteins** (co-abundance neighbors): MAT2B (0.84), U2SURP (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SEC24 homolog C, COPII component. The protein encoded by this gene is a member of the SEC24 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec24p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The product of this gene may play a role in shaping the vesicle, as well as in cargo selection and concentration.…
- **Diseases (Open Targets)**: 22q11.2 deletion syndrome (0.370); neurodegenerative disease (0.369); Alzheimer disease (0.281); lysosomal storage disease (0.274); Parkinson disease (0.274)
- **Europe PMC papers**: 693
- **Why important**: SEC24C is a relatively central node and connects the module to MAT2B and U2SURP. Its established COPII function in endoplasmic-reticulum exit, cargo selection, and ER-to-Golgi transport gives the module a concrete intracellular-trafficking component. Its disease associations include a chromosomal deletion syndrome and several neurodegenerative or lysosomal disease categories, while its literature support is substantial.
- **Conclusion**: Established evidence supports SEC24C as a COPII vesicle-trafficking and cargo-loading factor with liver detection. Its module position makes it an important candidate for explaining shared protein-handling variation. A direct role in coordinating the entire module is not established and remains hypothetical.

#### ATAD3A

- **Related proteins** (co-abundance neighbors): THOP1 (0.82), U2SURP (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATPase family AAA domain containing 3A. This gene encodes a ubiquitously expressed mitochondrial membrane protein that contributes to mitochondrial dynamics, nucleoid organization, protein translation, cell growth, and cholesterol metabolism. This gene is a member of the ATPase family AAA-domain containing 3 gene family which, in humans, includes two other paralogs. Naturally occurring mutations in this gene are associated with distinct…
- **Diseases (Open Targets)**: Harel-Yoon syndrome (0.824); pontocerebellar hypoplasia, hypotonia, and respiratory insufficiency syndrome, neonatal lethal (0.785); lactic acidosis (0.462); hereditary disease (0.418); isolated cerebellar hypoplasia/agenesis (0.342)
- **Europe PMC papers**: 879
- **Why important**: ATAD3A is among the more central nodes and links U2SURP with THOP1. It contributes to mitochondrial dynamics, nucleoid organization, protein translation, cell growth, and cholesterol metabolism, thereby connecting organelle maintenance with liver-relevant metabolic biology. Its severe neurological disease associations are comparatively strong in the supplied evidence, and it has a substantial literature base.
- **Conclusion**: Established evidence supports ATAD3A as a mitochondrial membrane protein with broad roles in mitochondrial organization and metabolism, as well as disease relevance. It could be a major biological driver of the shared co-abundance pattern, but the module does not demonstrate that ATAD3A regulates the other members.

#### CORO1C

- **Related proteins** (co-abundance neighbors): GET3 (0.87), U2SURP (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: coronin 1C. This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis,…
- **Diseases (Open Targets)**: neurodegenerative disease (0.453); Parkinson disease (0.322); Alzheimer disease (0.312); lysosomal storage disease (0.310); liver disorder (0.261)
- **Europe PMC papers**: 774
- **Why important**: CORO1C occupies a central position relative to GET3 and U2SURP and contributes actin-filament organization, signal transduction, regulation of phosphorylation, phagocytosis, and neural crest cell migration. It is associated in the supplied disease evidence with neurodegenerative, Parkinson, Alzheimer, lysosomal, and liver disorders and has the largest literature base among the listed genes.
- **Conclusion**: Established evidence supports CORO1C as a multifunctional cytoskeletal and signaling protein with broad disease relevance. Its position may indicate that cytoskeletal or signaling state contributes to the module, but the platelet annotation and heterogeneous cell-type evidence also make cell-composition effects plausible. A specific role in the shared tissue module is not demonstrated.

#### THOP1

- **Related proteins** (co-abundance neighbors): ATAD3A (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: thimet oligopeptidase 1. The protein encoded by this gene is a kininase that uses zinc as a cofactor. The encoded oligopeptidase cleaves cytosolic peptides, making them unavailable for display on antigen-presenting cells. This protein also cleaves neuropeptides under 20 aa in length and can degrade beta-amyloid precursor protein to amyloidogenic peptides. [provided by RefSeq, Nov 2015].
- **Diseases (Open Targets)**: neurodegenerative disease (0.371); Hypercholesterolemia (0.325); atrial fibrillation (0.246); asthma (0.245); neuroendocrine neoplasm (0.144)
- **Europe PMC papers**: 460
- **Why important**: THOP1 links ATAD3A to cytosolic peptide processing. It is a zinc-dependent oligopeptidase that processes cytosolic peptides and neuropeptides and can cleave amyloid precursor protein to amyloidogenic peptides. Its annotations connect peptide turnover with neurobiology, and the supplied evidence includes associations with neurodegenerative disease, hypercholesterolemia, atrial fibrillation, asthma, and neuroendocrine neoplasm.
- **Conclusion**: Established evidence supports THOP1 as a cytosolic peptidase involved in peptide degradation and proteolysis. Its connection to ATAD3A makes it relevant to the proposed organelle and proteostasis interpretation, but no evidence establishes a direct interaction or a causal role in the module. Its participation as a functional module driver remains a hypothesis.

## Module 8

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (41)**: CAPZA2, CIAO1, CIT, DNM2, TUFM, EIF2B4, ELP1, ERO1A, FKBP4, FLII, FLNB, RAP1GDS1, GFPT1, GGCT, GBE1, GNL1, HSPA4L, EIF6, ITGAV, MAIP1, APOOL, IMMT, NAA25, NSUN2, NUDT5, PCK2, PEPD, PGM2, PLS3, PITRM1, MRPL1, MRPL48, SEC23A, SNRPD1, AARS1, NARS1, RARS1, TUBB2A, TIMM9, UGGT1, WDR1

### Function

The module appears to represent a broadly expressed cellular maintenance program rather than a sharply defined tissue-specific pathway. Its strongest biological themes are interconnected protein production and quality control, mitochondrial function, carbohydrate and energy metabolism, cytoskeletal organization, and intracellular trafficking. The network places GFPT1, GNL1, NARS1, ELP1, and related translation or RNA-processing genes near the central part of the subgraph, while mitochondrial genes form a connected branch through IMMT, APOOL, TIMM9, MRPL1, MRPL48, and TUFM. Additional links connect carbohydrate metabolism through GFPT1, PGM2, GBE1, and NUDT5, and cytoskeletal or adhesion biology through WDR1, FLII, CAPZA2, FLNB, ITGAV, and PLS3. No GO or KEGG term passed global correction, so these functional themes are interpretive and annotation-based rather than globally significant enrichment results. The lack of a globally significant term does not invalidate the co-abundance module.

**Cell composition.** The HPA profile argues against a plasma-protein or secreted-protein module and against a module dominated by blood-cell markers. Most genes have low tissue specificity, nearly all have low immune-cell specificity, and only a small subset are secreted or intracellular-and-membrane proteins. Liver protein detection is broad across the module, whereas autonomic-nervous-system protein data are unavailable in the supplied HPA summary. A minority of genes show tissue or cell-type enhancement in brain, skeletal muscle, intestine, kidney, liver, esophageal cells, germ-cell populations, or selected blood-cell populations. Therefore the shared signal is more consistent with broadly expressed cellular machinery, with possible contributions from common cell states or technical and compositional effects, than with a liver-specific secretome or blood-cell contamination. The HPA evidence does not establish that blood accounts for the module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a set of already known relationships concentrated in several coherent pairs or small groups: aminoacyl-tRNA synthetases involving AARS1, NARS1, and RARS1; mitochondrial inner-membrane or cristae biology involving APOOL and IMMT; mitochondrial translation involving MRPL1, MRPL48, and TUFM; and carbohydrate metabolism involving GFPT1, PGM2, GBE1, and NUDT5. Other known links connect EIF6 with GNL1 and MRPL1, and FLNB with ITGAV. STRING functional enrichment is absent, so the interaction evidence supports selected local relationships but not a single established pathway for the whole module. hu.MAP independently recovers several complexes containing module members, including AARS1 with PLS3, AARS1 with NARS1, APOOL with IMMT, MRPL1 with MRPL48, and complexes containing EIF2B4, PEPD, or DNM2. These complexes are partial overlaps with larger complexes, not proof that all module genes form one physical complex. Together, STRING and hu.MAP indicate that portions of the co-abundance structure recapitulate known translation, mitochondrial, cytoskeletal, and cellular-machinery relationships, while much of the module remains connected only at the co-abundance level.

**STRING interactions (score >= 0.7)**: 13 of 820 gene pairs: AARS1–NARS1 (0.947); AARS1–RARS1 (0.85); APOOL–IMMT (0.999); EIF6–GNL1 (0.875); EIF6–MRPL1 (0.784); FLNB–ITGAV (0.724); GBE1–PGM2 (0.714); GFPT1–PGM2 (0.716); MRPL1–MRPL48 (0.887); MRPL1–TUFM (0.988); MRPL48–TUFM (0.913); NARS1–RARS1 (0.909); NUDT5–PGM2 (0.912)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11232.1 (CIAO1, DNM2, EIF2B4; 3/78); huMAP3_03533.1 (PLS3, AARS1; 2/4); huMAP3_07456.1 (PLS3, AARS1; 2/5); huMAP3_02950.1 (IMMT, APOOL; 2/8); huMAP3_09022.1 (IMMT, APOOL; 2/9); huMAP3_10281.1 (PLS3, AARS1; 2/9); huMAP3_10302.1 (NARS1, AARS1; 2/9); huMAP3_10776.1 (IMMT, APOOL; 2/10); huMAP3_10660.1 (IMMT, APOOL; 2/13); huMAP3_10115.1 (NARS1, AARS1; 2/14); huMAP3_10287.1 (PEPD, EIF2B4; 2/53); huMAP3_14442.1 (PLS3, AARS1; 2/57); huMAP3_06439.1 (MRPL48, MRPL1; 2/57); huMAP3_06589.1 (MRPL48, MRPL1; 2/79)

### Novelty

This module should not be called a wholly new molecular pathway. Several of its relationships and complexes are already documented by STRING and hu.MAP, and many component genes have established functions and disease associations. The potentially novel observation is the cross-tissue co-abundance configuration shared by autonomic nervous system and liver, especially the simultaneous association of translation-related, mitochondrial, metabolic, proteostasis, and cytoskeletal genes. However, absence of a relationship from STRING or hu.MAP would not by itself prove novelty, because those resources emphasize experimentally supported or curated interactions and may not capture tissue-specific co-abundance. The appropriate conclusion is a potentially novel systems-level module or tissue-pair association built partly from known molecular relationships, requiring replication and perturbational validation.

**Hypothesis.** Hypothesis: the shared module reflects coordinated demand for cellular maintenance in autonomic nervous system and liver cells, coupling nutrient and carbohydrate handling with protein synthesis, folding, RNA processing, mitochondrial translation, mitochondrial membrane organization, and cytoskeletal or vesicle trafficking. GFPT1-linked hexosamine metabolism could influence glycoprotein production and proteostasis, while the mitochondrial branch could support respiratory and organelle maintenance. Cytoskeletal and adhesion genes may couple these metabolic and proteostatic demands to cell architecture and trafficking. The co-abundance pattern may therefore be a common cell-state program rather than a dedicated tissue pathway. This hypothesis predicts that module activity will track coordinated changes in metabolic flux, translational capacity, mitochondrial integrity, and proteostasis, but the supplied evidence does not establish causality or direct physical assembly of the entire module.

### Important genes

#### GFPT1

- **Related proteins** (co-abundance neighbors): GNL1 (0.94), NAA25 (0.93), ELP1 (0.91), CAPZA2 (0.88), SNRPD1 (0.86), WDR1 (0.86), NARS1 (0.84), MRPL48 (0.84), TUFM (0.83), FKBP4 (0.83), RARS1 (0.82), CIAO1 (0.82), TIMM9 (0.81), FLII (0.80); STRING partners: PGM2 (0.716)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nucleoli; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glutamine--fructose-6-phosphate transaminase 1. This gene encodes the first and rate-limiting enzyme of the hexosamine pathway and controls the flux of glucose into the hexosamine pathway. The product of this gene catalyzes the formation of glucosamine 6-phosphate. [provided by RefSeq, Sep 2008].
- **Diseases (Open Targets)**: congenital myasthenic syndrome (0.819); neurodegenerative disease (0.559); congenital myasthenic syndromes with glycosylation defect (0.503); spinal stenosis (0.379); congenital disorder of glycosylation type I (0.370)
- **Europe PMC papers**: 1684
- **Why important**: GFPT1 is the most connected gene in the supplied module network and links the central co-abundance structure to GNL1, NAA25, ELP1, cytoskeletal genes, NARS1, and the carbohydrate-related STRING relationship with PGM2. Its established function as the rate-limiting entry enzyme of the hexosamine pathway provides a plausible metabolic bridge to glycoprotein production and cellular stress handling. It has extensive literature and disease associations including congenital myasthenic and glycosylation disorders and neurodegenerative disease. It has low tissue specificity and no secreted annotation, supporting a general cellular role rather than a circulating-protein explanation.
- **Conclusion**: Established evidence supports GFPT1 as a central metabolic and network-connected component. It is a strong candidate for coordinating nutrient-sensitive glycosylation-related metabolism with the broader maintenance program. It remains a hypothesis that GFPT1 activity drives the shared module or links the module causally to autonomic and liver physiology.

#### AARS1

- **Related proteins** (co-abundance neighbors): GNL1 (0.91), UGGT1 (0.84), ELP1 (0.81), PGM2 (0.80), RARS1 (0.80); STRING partners: NARS1 (0.947), RARS1 (0.85)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_03533.1, huMAP3_07456.1, huMAP3_10281.1, huMAP3_10302.1, huMAP3_10115.1, huMAP3_14442.1
- **Function (MyGene.info)**: alanyl-tRNA synthetase 1. The human alanyl-tRNA synthetase (AARS) belongs to a family of tRNA synthases, of the class II enzymes.  Class II tRNA synthases evolved early in evolution and are highly conserved. This is reflected by the fact that 498 of the 968-residue polypeptide human AARS shares 41% identity witht the E.coli protein.  tRNA synthases are the enzymes that interpret the RNA code and attach specific aminoacids …
- **Diseases (Open Targets)**: Charcot-Marie-Tooth disease axonal type 2N (0.762); developmental and epileptic encephalopathy, 29 (0.747); undetermined early-onset epileptic encephalopathy (0.678); trichothiodystrophy 8, nonphotosensitive (0.568); Charcot-Marie-Tooth disease type 2 (0.566)
- **Europe PMC papers**: 672
- **Why important**: AARS1 is connected to multiple hu.MAP complexes, including complexes shared with PLS3 and NARS1, and has strong STRING relationships with NARS1 and RARS1. Its network position connects aminoacyl-tRNA charging with GNL1, UGGT1, ELP1, PGM2, and the central metabolic neighborhood. Its established role in alanyl-tRNA aminoacylation makes it a direct indicator of translational capacity, while its disease associations include axonal Charcot-Marie-Tooth disease and developmental epileptic encephalopathy. Its literature support is substantial.
- **Conclusion**: Established evidence supports AARS1 as a translation-related anchor and as part of known synthetase and protein-complex relationships. Its presence is compatible with a shared protein-production and maintenance program. A causal role for AARS1 in coordinating the other module branches is not established.

#### ELP1

- **Related proteins** (co-abundance neighbors): GFPT1 (0.91), NSUN2 (0.90), RARS1 (0.90), SNRPD1 (0.86), WDR1 (0.82), AARS1 (0.81), UGGT1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: elongator acetyltransferase complex subunit 1. The protein encoded by this gene is a scaffold protein and a regulator for three different kinases involved in proinflammatory signaling. The encoded protein can bind NF-kappa-B-inducing kinase and I-kappa-B kinases through separate domains and assemble them into an active kinase complex. Mutations in this gene have been associated with familial dysautonomia. Alternative splicing results in multip…
- **Diseases (Open Targets)**: Riley-Day syndrome (0.807); medulloblastoma (0.721); primary dysautonomia (0.407); hereditary sensory and autonomic neuropathy (0.374); mathematical ability (0.361)
- **Europe PMC papers**: 960
- **Why important**: ELP1 occupies a connected position near GFPT1, NSUN2, RARS1, SNRPD1, WDR1, AARS1, and UGGT1. It is an established scaffold and regulator of kinase assemblies, participates in tRNA wobble modification and translation regulation, and is associated with familial dysautonomia and other autonomic or neurodevelopmental disease contexts. Its presence is especially informative for this tissue pair because autonomic disease relevance is directly represented in the supplied annotation. It is broadly expressed and not secreted.
- **Conclusion**: Established evidence supports ELP1 as a biologically relevant translation and signaling scaffold with a strong autonomic-disease connection. It is a compelling interpretive gene for the module, but the co-abundance data do not show that ELP1 is the cause of the shared tissue pattern.

#### IMMT

- **Related proteins** (co-abundance neighbors): ITGAV (0.83), TIMM9 (0.83); STRING partners: APOOL (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_02950.1, huMAP3_09022.1, huMAP3_10776.1, huMAP3_10660.1
- **Function (MyGene.info)**: inner membrane mitochondrial protein. Enables RNA binding activity. Involved in cristae formation. Located in mitochondrial inner membrane. Part of MICOS complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.512); multinodular goiter (0.196); alcohol drinking (0.190); breast cancer (0.094); neoplasm (0.087)
- **Europe PMC papers**: 933
- **Why important**: IMMT is a mitochondrial inner-membrane and cristae-organization protein, and it participates in several hu.MAP complexes with APOOL. Its STRING relationship with APOOL is a particularly strong known connection, while the module network also links IMMT to TIMM9 and ITGAV. This gives the module a defined mitochondrial-architecture component rather than only generic housekeeping signals. IMMT has substantial literature and disease associations involving neurodegenerative disease and other disorders. HPA detects it in liver and places it in mitochondria, with low immune-cell specificity.
- **Conclusion**: Established evidence supports IMMT as an anchor of the mitochondrial cristae branch and a known APOOL-associated complex component. Its participation supports mitochondrial structural maintenance as part of the module. Whether mitochondrial architecture is the organizing principle of the entire module remains a hypothesis.

#### PEPD

- **Related proteins** (co-abundance neighbors): GNL1 (0.92), RAP1GDS1 (0.82), PITRM1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_10287.1
- **Function (MyGene.info)**: peptidase D. This gene encodes a member of the peptidase family. The protein forms a homodimer that hydrolyzes dipeptides or tripeptides with C-terminal proline or hydroxyproline residues. The enzyme serves an important role in the recycling of proline, and may be rate limiting for the production of collagen. Mutations in this gene result in prolidase deficiency, which is characterized by the excretion of larg…
- **Diseases (Open Targets)**: prolidase deficiency (0.822); type 2 diabetes mellitus (0.425); Abnormality of the skeletal system (0.411); diabetes mellitus (0.409); obesity disorder (0.354)
- **Europe PMC papers**: 1500
- **Why important**: PEPD connects GNL1, RAP1GDS1, and PITRM1 in the module network and is represented in hu.MAP complex (hu.MAP huMAP3_10287.1) with EIF2B4. Its established enzymatic function in degradation of proline-containing peptides links amino-acid recycling to collagen-related metabolism and cellular proteolysis. HPA identifies tissue enhancement in intestine and kidney and cell-type enhancement in hepatocytes, making PEPD one of the more informative genes for the liver component. Prolidase deficiency is a direct disease association, with additional metabolic and skeletal disease links, and its literature volume is substantial.
- **Conclusion**: Established evidence supports PEPD as a liver-relevant amino-acid and peptide-recycling component that connects metabolic and mitochondrial neighborhoods. It may help explain tissue-associated metabolic content within an otherwise broadly expressed module. A direct role for PEPD in autonomic nervous system biology or in organizing the full module is not established.

## Module 9

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (9)**: COPS3, CUL2, FAM98B, FUS, SLC16A1, SNU13, PTPA, RPL12, LARS1

### Function

No GO or KEGG term passed global correction, so the module should not be assigned a specific pathway on enrichment evidence alone. Its gene content instead supports a mixed intracellular maintenance module involving RNA processing and splicing, translation, amino-acid charging, monocarboxylate transport, ubiquitin-dependent protein turnover, and phosphatase-related regulation. The co-abundance graph is sparse and contains several cross-functional links, with FUS occupying a central position among the observed edges and COPS3 linking RNA-associated, translational, and ubiquitin-system genes. This pattern is more consistent with coordinated cellular housekeeping and proteostasis than with a narrowly defined tissue-specific pathway.

**Cell composition.** The module is not dominated by plasma or secreted proteins: none of its genes is annotated as secreted. All genes have low tissue specificity, and protein detection is reported for every module gene in liver, which supports a broadly expressed intracellular component of liver samples rather than a liver-exclusive program. Most genes have low immune-cell specificity, with only SLC16A1 showing immune-cell enhancement in T-reg cells. The single-cell annotations are heterogeneous, including germ-cell, epithelial, erythrocyte-progenitor, glial, and renal tubular cell categories, rather than a coherent autonomic-nervous-system or liver cell type. Because no matching HPA tissue is available for autonomic nervous system, the apparent cross-tissue conservation should be interpreted cautiously. The module could reflect broadly expressed cellular machinery or shared cell-composition effects, but the available HPA evidence does not support a plasma-protein or broad blood-contamination explanation.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides two high-confidence relationships within the module: COPS3–CUL2 and RPL12–SNU13. These are established molecular connections and support the interpretation that at least part of the module reflects real intracellular machinery rather than arbitrary co-abundance. hu.MAP independently places COPS3 and CUL2 together in three complexes, (hu.MAP huMAP3_08550.1), (hu.MAP huMAP3_09779.1), and (hu.MAP huMAP3_14528.1), each representing a larger cullin or COP-nine-related complex in which only these module members are present. This convergent evidence makes the COPS3–CUL2 substructure the best-supported physical-complex feature. RPL12–SNU13 is supported by STRING but not by the listed hu.MAP complexes. The remaining co-abundance edges, including those involving FUS, SLC16A1, LARS1, PTPA, and the other genes, are not established by the supplied STRING or hu.MAP evidence and should be regarded as module-level associations rather than confirmed physical interactions.

**STRING interactions (score >= 0.7)**: 2 of 36 gene pairs: COPS3–CUL2 (0.965); RPL12–SNU13 (0.731)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_08550.1 (CUL2, COPS3; 2/34); huMAP3_09779.1 (CUL2, COPS3; 2/44); huMAP3_14528.1 (CUL2, COPS3; 2/49)

### Novelty

The module may be novel as a cross-tissue co-abundance pattern, but the evidence does not justify claiming a newly discovered molecular complex or pathway. Its strongest internal relationship, COPS3–CUL2, is already represented by STRING and by multiple hu.MAP complexes, and RPL12–SNU13 is also already represented in STRING. The potentially novel aspect is the particular association of these established intracellular components with FUS, SLC16A1, LARS1, PTPA, and the other module genes across autonomic nervous system and liver. However, absence of a relationship from STRING or hu.MAP cannot by itself establish novelty. A stronger novelty claim would require replication in independent cohorts, preservation after adjustment for cell composition and abundance, and comparison with previously published tissue co-abundance modules.

**Hypothesis.** Hypothesis: the module represents a coordinated intracellular stress-adaptation and proteostasis state shared by liver and autonomic-nervous-system samples. In this model, FUS and SNU13 connect RNA handling and spliceosomal functions, LARS1 and RPL12 reflect protein-production capacity, COPS3–CUL2 represent regulation of ubiquitin-dependent protein turnover, and SLC16A1 links cellular metabolic flux through monocarboxylate transport to these maintenance processes. PTPA could connect the state to phosphatase-dependent control, although that connection is not established by the supplied interaction evidence. This is a mechanistic hypothesis, not a demonstrated pathway: the lack of globally significant GO or KEGG enrichment and the sparse network mean that direct biochemical coordination remains to be tested.

### Important genes

#### COPS3

- **Related proteins** (co-abundance neighbors): RPL12 (0.87), FUS (0.83), LARS1 (0.82); STRING partners: CUL2 (0.965)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_08550.1, huMAP3_09779.1, huMAP3_14528.1
- **Function (MyGene.info)**: COP9 signalosome subunit 3. The protein encoded by this gene possesses kinase activity that phosphorylates regulators involved in signal transduction. It phosphorylates I kappa-Balpha, p105, and c-Jun. It acts as a docking site for complex-mediated phosphorylation. The gene is located within the Smith-Magenis syndrome region on chromosome 17. Several transcript variants encoding different isoforms have been found for this ge…
- **Diseases (Open Targets)**: neurodegenerative disease (0.416); osteosarcoma (0.101); lung carcinoma (0.071); lung cancer (0.071); neoplasm (0.067)
- **Europe PMC papers**: 1103
- **Why important**: COPS3 is among the most connected genes in the module and is the clearest structural anchor because it connects to CUL2 in STRING and occurs with CUL2 in three hu.MAP complexes, (hu.MAP huMAP3_08550.1), (hu.MAP huMAP3_09779.1), and (hu.MAP huMAP3_14528.1). Its annotation supports roles in the COP-nine signalosome, protein deneddylation, ubiquitin-dependent protein catabolism, and signal transduction. It also has liver protein detection and substantial literature coverage, making it more interpretable than the sparsely studied genes.
- **Conclusion**: Established evidence supports COPS3 as a central member of a ubiquitin-regulatory and signal-transduction-related substructure. It is plausible that COPS3 helps organize the module, but the co-abundance data do not demonstrate that it controls the other module genes.

#### CUL2

- **Related proteins** (co-abundance neighbors): PTPA (0.81), LARS1 (0.81); STRING partners: COPS3 (0.965)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: huMAP3_08550.1, huMAP3_09779.1, huMAP3_14528.1
- **Function (MyGene.info)**: cullin 2. Enables ubiquitin protein ligase binding activity. Predicted to be involved in SCF-dependent proteasomal ubiquitin-dependent protein catabolic process and protein ubiquitination. Predicted to act upstream of or within protein catabolic process. Located in nucleoplasm. Part of Cul2-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Crohn disease (0.382); obesity disorder (0.265); Moyamoya disease (0.259); inflammatory bowel disease (0.244); skin disorder (0.241)
- **Europe PMC papers**: 2492
- **Why important**: CUL2 is directly linked to COPS3 by a high-confidence STRING relationship and is present with COPS3 in the three hu.MAP complexes, (hu.MAP huMAP3_08550.1), (hu.MAP huMAP3_09779.1), and (hu.MAP huMAP3_14528.1). Its annotated role as a cullin scaffold in ubiquitin ligase complexes gives the module a plausible protein-turnover component. It is also one of the more connected genes and has relevant disease associations, including inflammatory and metabolic disorders.
- **Conclusion**: Established evidence supports CUL2 as a component of the module's best-supported ubiquitin-system feature. Its association with the broader module may indicate coordinated proteostasis, but a specific CUL2 substrate or tissue mechanism cannot be inferred.

#### FUS

- **Related proteins** (co-abundance neighbors): FAM98B (0.92), COPS3 (0.83), SLC16A1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: FUS RNA binding protein. This gene encodes a multifunctional protein component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complex. The hnRNP complex is involved in pre-mRNA splicing and the export of fully processed mRNA to the cytoplasm. This protein belongs to the FET family of RNA-binding proteins which have been implicated in cellular processes that include regulation of gene expression, maintenance of gen…
- **Diseases (Open Targets)**: amyotrophic lateral sclerosis (0.710); sporadic amyotrophic lateral sclerosis (0.683); frontotemporal dementia with motor neuron disease (0.667); essential tremor (0.557); juvenile amyotrophic lateral sclerosis (0.527)
- **Europe PMC papers**: 19869
- **Why important**: FUS has the greatest network connectivity in the listed module and links FAM98B, COPS3, and SLC16A1. It is a multifunctional RNA-binding protein involved in hnRNP biology, pre-mRNA splicing, mRNA export, RNA processing, and gene-expression regulation. Its extensive literature and disease associations with amyotrophic lateral sclerosis and frontotemporal dementia make it an important biological and translational anchor.
- **Conclusion**: Established evidence supports FUS as a central RNA-processing gene with strong disease relevance. Its module-level links to COPS3 and SLC16A1 suggest coordinated RNA and metabolic regulation, but these links remain hypotheses because they are not supported by listed STRING or hu.MAP relationships.

#### SLC16A1

- **Related proteins** (co-abundance neighbors): SNU13 (0.89), FUS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cell Junctions; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 16 member 1. The protein encoded by this gene is a proton-linked monocarboxylate transporter that catalyzes the movement of many monocarboxylates, such as lactate and pyruvate, across the plasma membrane. Mutations in this gene are associated with erythrocyte lactate transporter defect. Alternatively spliced transcript variants have been found for this gene.[provided by RefSeq, Oct 2009].
- **Diseases (Open Targets)**: exercise-induced hyperinsulinism (0.720); ketoacidosis due to monocarboxylate transporter-1 deficiency (0.717); metabolic myopathy due to lactate transporter defect (0.707); neurodegenerative disease (0.509); inborn errors of metabolism (0.370)
- **Europe PMC papers**: 6642
- **Why important**: SLC16A1 is a plasma-membrane monocarboxylate transporter for lactate and pyruvate and connects in the module to FUS and SNU13. It has substantial literature coverage, liver detection, and disease associations involving monocarboxylate transport, exercise-induced hyperinsulinism, ketoacidosis, and metabolic myopathy. Its cell-type annotations are heterogeneous and include several epithelial, neural-associated, germ-cell, and immune categories.
- **Conclusion**: Established evidence supports SLC16A1 as the module's clearest metabolic-transport component. Its connection to RNA-processing genes could reflect a shared cellular state or indirect co-abundance, but a direct regulatory relationship is not established.

#### LARS1

- **Related proteins** (co-abundance neighbors): COPS3 (0.82), CUL2 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear bodies, Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: leucyl-tRNA synthetase 1. This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals w…
- **Diseases (Open Targets)**: infantile liver failure syndrome 1 (0.670); acute infantile liver failure due to synthesis defect of mtDNA-encoded proteins (0.510); Global developmental delay (0.119); sensorineural hearing loss disorder (0.119); Generalized-onset seizure (0.118)
- **Europe PMC papers**: 267
- **Why important**: LARS1 encodes cytosolic leucyl-tRNA synthetase and connects to COPS3 and CUL2 in the co-abundance graph. Its function links amino-acid sensing and leucine charging to protein translation, while its disease associations include infantile liver failure and disorders caused by defects in synthesis of mitochondrial proteins. Its liver detection makes it relevant to interpretation of the liver component of the module.
- **Conclusion**: Established evidence supports LARS1 as a translation and amino-acid-response factor with particular relevance to liver disease. Its co-abundance with the COPS3–CUL2 substructure is consistent with coordinated translation and proteostasis, but it does not prove a shared complex.

## Module 10

**Tissue pair**: autonomic_nervous_system and liver  
**Genes (6)**: COLGALT1, MAN1A1, MARS1, CCT5, TRAP1, XPO1

### Function

No GO or KEGG term passed global correction, and there is no supplementary STRING enrichment. The module therefore does not support a specific pathway-level function from enrichment analysis. Its genes instead suggest a heterogeneous cellular-maintenance program spanning translation, protein folding, glycoprotein processing, collagen-related modification, mitochondrial stress control, and nucleocytoplasmic transport. The co-abundance structure is compatible with coordinated proteostasis and secretory or extracellular-matrix support, but this interpretation remains inferential rather than an established functional annotation. MARS1, CCT5, and TRAP1 support protein synthesis, folding, and stress handling; MAN1A1 and COLGALT1 support processing of glycoproteins or matrix-associated proteins; and XPO1 supports nuclear transport. The absence of globally significant enrichment does not invalidate the module, but it limits confidence in assigning one unified biological process.

**Cell composition.** This is not predominantly a plasma or secreted-protein module. Most members are intracellular, with one member annotated as intracellular and membrane-associated, and the remaining proteins assigned to cytosol, Golgi, nucleoplasm or nuclear membrane, mitochondria, or vesicles. Most genes have low tissue specificity, while one is liver-enhanced. Most genes have cell-type-enhanced annotations, including macrophages and related myeloid populations, and one gene has enriched blood-cell annotations across several myeloid cell types. This pattern raises the possibility that the shared signal partly reflects common immune or myeloid-cell content in autonomic nervous system and liver samples, rather than a specialized autonomic–liver program. Liver protein detection is mixed across the module, while there is no matching autonomic nervous system protein-detection assessment in the supplied HPA summary.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No STRING interaction met the supplied high-confidence threshold, and no hu.MAP complex contained multiple module members. Thus the observed co-abundance links are not corroborated by the supplied physical-interaction or complex resources. The individual annotations nevertheless describe known cellular roles: MARS1 participates in the multi-tRNA synthetase complex; CCT5 is a subunit of the CCT folding complex; MAN1A1 is a Golgi mannosidase; COLGALT1 is an endoplasmic-reticulum collagen-modifying enzyme; XPO1 is a nuclear export factor; and TRAP1 is a mitochondrial chaperone. These established functions are biologically diverse and do not by themselves establish a single physical complex or direct interaction among the module members.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The co-abundance pattern may represent a previously unreported association in this tissue pair, because the supplied resources provide no high-confidence STRING links, no multi-member hu.MAP complex, and no globally significant GO or KEGG term. However, it cannot be called a new biological discovery from these results alone. Novelty is weakened by the small module, the heterogeneous functions, the lack of external interaction support, and the HPA evidence for shared cell-type composition. A defensible conclusion is that the module is a potentially novel co-abundance pattern whose biological novelty remains unvalidated. Replication in independent cohorts, adjustment for cell composition, and targeted testing of the proposed relationships would be required.

**Hypothesis.** Hypothesis: the module reflects coordinated proteostasis and secretory-interface activity in a shared cellular population, potentially including myeloid cells present in both tissues. In this model, MARS1 supports translational capacity, CCT5 and TRAP1 buffer protein-folding and cellular stress, MAN1A1 processes glycoproteins through the Golgi and quality-control pathway, COLGALT1 modifies collagen-related substrates in the secretory pathway, and XPO1 coordinates nuclear export needed to sustain cellular adaptation. The observed co-abundance could therefore arise from a cell-state program coupling biosynthetic load, protein quality control, extracellular-matrix or glycoprotein handling, and stress adaptation. This is a mechanistic hypothesis, not a demonstrated pathway or direct interaction network.

### Important genes

#### MARS1

- **Related proteins** (co-abundance neighbors): CCT5 (0.89), MAN1A1 (0.88), XPO1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: methionyl-tRNA synthetase 1. This gene encodes a member of the class I family of aminoacyl-tRNA synthetases. These enzymes play a critical role in protein biosynthesis by charging tRNAs with their cognate amino acids. The encoded protein is a component of the multi-tRNA synthetase complex and catalyzes the ligation of methionine to tRNA molecules. [provided by RefSeq, Jan 2011].
- **Diseases (Open Targets)**: severe early-onset pulmonary alveolar proteinosis due to MARS deficiency (0.745); Charcot-Marie-Tooth disease axonal type 2U (0.676); autosomal recessive spastic paraplegia type 70 (0.614); trichothiodystrophy 9, nonphotosensitive (0.428); pulmonary alveolar proteinosis (0.338)
- **Europe PMC papers**: 435
- **Why important**: MARS1 is a central network member with the strongest apparent connectivity in the module and links to CCT5, MAN1A1, and XPO1. Its established role is methionyl-tRNA charging as part of the multi-tRNA synthetase complex, placing it at the entry point of protein biosynthesis. It has substantial literature coverage and disease associations involving MARS deficiency, peripheral neuropathy, and spastic paraplegia, which are relevant to a module shared with autonomic nervous system tissue.
- **Conclusion**: Established evidence supports MARS1 as a translation-related hub and a plausible marker of biosynthetic demand. The hypothesis that it coordinates the other module processes is not established, because neither STRING nor hu.MAP supports direct relationships within this module.

#### MAN1A1

- **Related proteins** (co-abundance neighbors): MARS1 (0.88), COLGALT1 (0.85), CCT5 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus; IHC detected in liver
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mannosidase alpha class 1A member 1. This gene encodes a class I mammalian Golgi 1,2-mannosidase which is a type II transmembrane protein. This protein catalyzes the hydrolysis of three terminal mannose residues from peptide-bound Man(9)-GlcNAc(2) oligosaccharides and belongs to family 47 of glycosyl hydrolases. [provided by RefSeq, Jul 2012].
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.368); nervous system benign neoplasm (0.353); smoking initiation (0.311); eye disorder (0.292); hypertrophic cardiomyopathy (0.280)
- **Europe PMC papers**: 645
- **Why important**: MAN1A1 is a network hub connected to MARS1, CCT5, and COLGALT1, and it is the only tissue-enhanced gene in the module, with liver enhancement. Its established Golgi mannosidase activity links it to N-glycan trimming, glycoprotein processing, and ER-associated quality control. Its cell-type annotations include macrophages and other hematopoietic populations, making it informative for both the secretory interpretation and the possibility of cell-composition effects.
- **Conclusion**: Established evidence supports MAN1A1 as the strongest liver- and Golgi-related anchor of the module. It may connect biosynthetic activity with glycoprotein quality control, but a specific shared autonomic–liver mechanism remains hypothetical.

#### CCT5

- **Related proteins** (co-abundance neighbors): MARS1 (0.89), MAN1A1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 is directly connected to MARS1 and MAN1A1 and encodes a subunit of the CCT or TRiC chaperonin complex, which folds proteins including actin and tubulin. It has the largest literature volume among the non-transport genes listed here and is associated with hereditary sensory and autonomic neuropathy and spastic paraplegia. Its role provides a plausible proteostasis component in a module involving autonomic nervous system tissue.
- **Conclusion**: Established evidence supports CCT5 as a protein-folding factor with disease relevance to autonomic and peripheral nervous system phenotypes. Its participation in a coordinated cross-tissue proteostasis program is a reasonable hypothesis, but the supplied interaction resources do not validate this module-level claim.

#### COLGALT1

- **Related proteins** (co-abundance neighbors): MAN1A1 (0.85), TRAP1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: collagen beta(1-O)galactosyltransferase 1. The protein encoded by this gene is one of two enzymes that transfers galactose moieties to hydroxylysine residues of collagen and mannose binding lectin. This gene is constitutively expressed and encodes a soluble protein that localizes to the endoplasmic reticulum. [provided by RefSeq, Dec 2015].
- **Diseases (Open Targets)**: cerebral small vessel disease (0.733); hereditary disease (0.415); familial porencephaly (0.370); vascular dementia (0.111); neoplasm (0.085)
- **Europe PMC papers**: 309
- **Why important**: COLGALT1 connects MAN1A1 and TRAP1 and encodes an enzyme that galactosylates collagen hydroxylysine residues and mannose-binding lectin. It is the clearest matrix- or secretory-interface gene in the module. HPA annotations associate it with macrophages, Kupffer cells, monocytes, and other myeloid populations, as well as several blood-cell groups. Its disease associations include cerebral small-vessel disease and familial porencephaly, giving it vascular and tissue-structure relevance.
- **Conclusion**: Established evidence supports COLGALT1 as a collagen-modification enzyme and a marker potentially sensitive to myeloid or vascular-cell composition. A connection between collagen processing, mitochondrial stress, and translation in this module is hypothetical and requires experimental testing.

#### XPO1

- **Related proteins** (co-abundance neighbors): MARS1 (0.85); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear membrane; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: exportin 1. This cell-cycle-regulated gene encodes a protein that mediates leucine-rich nuclear export signal (NES)-dependent protein transport. The protein specifically inhibits the nuclear export of Rev and U snRNAs. It is involved in the control of several cellular processes by controlling the localization of cyclin B, MPAK, and MAPKAP kinase 2. This protein also regulates NFAT and AP-1. [provided by RefSe…
- **Diseases (Open Targets)**: plasma cell myeloma (0.642); B-cell chronic lymphocytic leukemia (0.626); diffuse large B-cell lymphoma (0.602); HIV infectious disease (0.561); neurodegenerative disease (0.522)
- **Europe PMC papers**: 5357
- **Why important**: XPO1 is connected to MARS1 and encodes the major exportin responsible for transport of multiple nuclear cargos, including ribosomal subunits and messenger RNA. It has extensive literature coverage and disease associations involving plasma-cell myeloma, chronic lymphocytic leukemia, diffuse large B-cell lymphoma, HIV infection, and neurodegenerative disease. Its position provides a plausible regulatory link between nuclear transport and cellular biosynthetic state.
- **Conclusion**: Established evidence supports XPO1 as a broadly acting nuclear-export factor with substantial disease relevance. Its inclusion may reflect general cellular activity or stress rather than a tissue-specific mechanism; any role as a coordinator of this module is therefore a hypothesis.
