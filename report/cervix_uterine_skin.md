# Conserved co-abundance modules: cervix_uterine and skin

## Module 0

**Tissue pair**: cervix_uterine and skin  
**Genes (23)**: SLC3A2, AKR1C3, MTHFD1L, CD55, DHCR24, EPPK1, EZR, HSPA4L, IKBIP, KRT18, KRT7, KRT8, CKB, MKI67, KYNU, NBN, NDC1, PALLD, PC, RFC1, OXCT1, TARS1, ZNF638

### Function

The strongest functional interpretation is an epithelial structural module centered on keratin intermediate filaments. The only globally corrected GO/KEGG evidence is (GO:CC keratin filament; q_global = 0.0203), the keratin filament term, supported by EPPK1, KRT18, KRT7 and KRT8. The supplementary STRING tissue and component results (STRING TISSUES Squamous epithelium; within-query FDR = 0.0285), (STRING Component Keratin filament; within-query FDR = 0.0341) and (STRING COMPARTMENTS Keratin filament; within-query FDR = 0.0354) are concordant, pointing to squamous or other epithelial structural biology. The remaining genes suggest accompanying membrane–cytoskeleton organization, cell adhesion and migration, complement regulation, intermediary metabolism, protein folding, DNA replication or repair, and proliferative state, but these are distributed annotations rather than globally enriched module functions. The network is sparse, with a keratin core and several peripheral links, so the module should not be interpreted as a single biochemical pathway.

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: CD55 is the only gene annotated as secreted to blood, while the other genes are intracellular or membrane-associated. The module contains a clear epithelial component, especially the keratin genes and EPPK1, with HPA detection in both cervix_uterine and skin for most genes. HPA indicates low immune-cell specificity for many genes, although several genes are immune-cell enhanced or enriched and some show neutrophil, basophil, monocyte or dendritic-cell associations. The broad cell-type enhancement across the module and the occurrence of epithelial, trophoblast, urothelial and alveolar associations suggest that shared epithelial or epithelial-like cell populations are more plausible than a purely blood-derived explanation. Nevertheless, CD55 and immune-associated genes mean that blood contamination, vascular material or shared immune–epithelial context cannot be excluded.

**GO/KEGG enrichment**: 1 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC keratin filament | 0.0203 | EPPK1, KRT18, KRT7, KRT8 |

### STRING and hu.MAP

STRING supports only a small, selective part of the co-abundance structure. The established high-confidence relationships are KRT18–KRT8, KRT7–KRT8 and EZR–PALLD. The keratin pair and KRT7 connection directly reinforce the keratin-filament interpretation, while EZR–PALLD supports a membrane–actin cytoskeletal link. No other module relationships are represented by the supplied STRING threshold, so most co-abundance edges are not established protein interactions in this evidence set. No hu.MAP complex contains multiple module members. Thus, the module is consistent with a known epithelial cytoskeletal core embedded in a broader, mostly unvalidated co-abundance neighborhood; co-abundance should not be treated as physical interaction.

**STRING interactions (score >= 0.7)**: 3 of 253 gene pairs: EZR–PALLD (0.846); KRT18–KRT8 (0.999); KRT7–KRT8 (0.746)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Squamous epithelium (FDR = 0.0285, 3 genes); Component Keratin filament (FDR = 0.0341, 4 genes); COMPARTMENTS Keratin filament (FDR = 0.0354, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The keratin-filament component is not a new biological concept: KRT8 and KRT18 are established epithelial intermediate-filament partners, KRT7 is a known keratin component, and EPPK1 is linked to keratin-network organization. The module-level observation may still be novel because it combines this conserved epithelial core with CD55, AKR1C3, metabolic genes, DNA-maintenance genes and stress-related genes in a cervix_uterine–skin co-abundance pattern. However, absence of most module edges from STRING and absence of a hu.MAP complex do not establish novelty; they may reflect incomplete interaction coverage, context dependence or correlations rather than direct binding. The defensible conclusion is a potentially interesting cross-tissue co-abundance configuration built around a previously known epithelial program, not a demonstrated new molecular complex or pathway.

**Hypothesis.** Hypothesis: the shared module reflects a conserved epithelial state in which keratin filament integrity and membrane–actin organization are coordinated with epithelial differentiation, barrier or cell-shape demands, while metabolic, proteostasis, DNA-repair and proliferation genes capture the physiological state of the sampled cells. CD55 may connect this epithelial state to complement protection or local immune context, and AKR1C3 may connect it to steroid and prostaglandin metabolism. The module could therefore represent epithelial structural maintenance under tissue-specific metabolic or inflammatory conditions. This is a mechanistic hypothesis rather than a demonstrated causal pathway; the supplied data establish co-abundance and selected known interactions, not directionality or regulation.

### Important genes

#### KRT8

- **Related proteins** (co-abundance neighbors): KRT7 (0.91), KRT18 (0.86), AKR1C3 (0.85); STRING partners: KRT18 (0.999), KRT7 (0.746)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Intermediate filaments; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 8. This gene is a member of the type II keratin family clustered on the long arm of chromosome 12. Type I and type II keratins heteropolymerize to form intermediate-sized filaments in the cytoplasm of epithelial cells. The product of this gene typically dimerizes with keratin 18 to form an intermediate filament in simple single-layered epithelial cells. This protein plays a role in maintaining cellul…
- **Diseases (Open Targets)**: cirrhosis of liver (0.596); cirrhosis, familial (0.401); neurodegenerative disease (0.371); prostate carcinoma (0.314); Abnormality of the liver (0.306)
- **Europe PMC papers**: 5942
- **Why important**: KRT8 is a central member of the keratin subnetwork, connects to KRT7 and KRT18 through established STRING relationships, and is one of the four genes supporting the globally corrected keratin-filament result (GO:CC keratin filament; q_global = 0.0203). Its HPA cell-type associations include colonocytes, enterocytes, goblet cells and trophoblast-related epithelial populations, and its documented function is epithelial intermediate-filament organization and structural integrity. It also has substantial literature and disease association through liver disease and neoplasia.
- **Conclusion**: Established evidence supports KRT8 as a core epithelial structural gene and a principal anchor of the module. Its high network connectivity and concordant GO and STRING evidence make it more informative than a generic housekeeping marker. The hypothesis that KRT8 coordinates the other module branches is plausible but not proven by this co-abundance analysis.

#### KRT18

- **Related proteins** (co-abundance neighbors): KRT8 (0.86), CKB (0.84), MKI67 (0.80); STRING partners: KRT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 18. KRT18 encodes the type I intermediate filament chain keratin 18. Keratin 18, together with its filament partner keratin 8, are perhaps the most commonly found members of the intermediate filament gene family. They are expressed in single layer epithelial tissues of the body. Mutations in this gene have been linked to cryptogenic cirrhosis. Two transcript variants encoding the same protein have bee…
- **Diseases (Open Targets)**: cirrhosis of liver (0.623); cirrhosis, familial (0.396); prostate carcinoma (0.140); neoplasm (0.117); breast carcinoma (0.113)
- **Europe PMC papers**: 6539
- **Why important**: KRT18 is directly paired with KRT8 by a very strong STRING relationship and is included in (GO:CC keratin filament; q_global = 0.0203) and (STRING TISSUES Squamous epithelium; within-query FDR = 0.0285) through (STRING COMPARTMENTS Keratin filament; within-query FDR = 0.0354). It is a type I keratin expressed with KRT8 in simple epithelial tissues and has module links to CKB and MKI67, connecting structural biology with energy and proliferation-related signals. It has extensive literature and established associations with cirrhosis and neoplasia.
- **Conclusion**: Established evidence identifies KRT18 as the partner component of the module's epithelial keratin core. Its link with MKI67 may reflect proliferative epithelial state, but the module does not establish that KRT18 regulates proliferation or that proliferation drives the module.

#### EPPK1

- **Related proteins** (co-abundance neighbors): PC (0.89), OXCT1 (0.80); STRING partners: none
- **HPA**: Tissue enriched; Cell type enhanced; blood Not detected in immune cells; location Intermediate filaments; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: epiplakin 1. The protein encoded by this gene belongs to the plakin family of proteins, which play a role in the organization of cytoskeletal architecture. This family member is composed of several highly homologous plakin repeats. It may function to maintain the integrity of keratin intermediate filament networks in epithelial cells. Studies of the orthologous mouse protein suggest that it accelerates keratin…
- **Diseases (Open Targets)**: neurodegenerative disease (0.451); Parkinson disease (0.298); gout (0.238); Hypercholesterolemia (0.125); myoepithelial tumor (0.111)
- **Europe PMC papers**: 618
- **Why important**: EPPK1 is one of the genes in the globally corrected keratin-filament term (GO:CC keratin filament; q_global = 0.0203) and the STRING keratin-filament terms (STRING Component Keratin filament; within-query FDR = 0.0341) and (STRING COMPARTMENTS Keratin filament; within-query FDR = 0.0354). HPA places it in intermediate filaments, enriches it in skin tissue, and associates it with basal and suprabasal keratinocytes. Its documented role concerns organization and integrity of keratin networks, keratinocyte migration and wound healing. It also provides a bridge from the keratin component toward PC and OXCT1 in the module.
- **Conclusion**: Established evidence supports EPPK1 as a tissue-relevant epithelial cytoskeletal organizer, particularly for the skin side of the shared module. Its absence of cervix_uterine immunohistochemical detection cautions against treating it as a universally active driver across both tissues. A role in coordinating tissue repair or barrier adaptation is a hypothesis requiring validation.

#### CD55

- **Related proteins** (co-abundance neighbors): SLC3A2 (0.89), KYNU (0.88), AKR1C3 (0.86), IKBIP (0.86), MTHFD1L (0.84), EZR (0.84), HSPA4L (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location None; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD55 molecule (Cromer blood group). This gene encodes a glycoprotein involved in the regulation of the complement cascade. Binding of the encoded protein to complement proteins accelerates their decay, thereby disrupting the cascade and preventing damage to host cells. Antigens present on this protein constitute the Cromer blood group system (CROM). Alternative splicing results in multiple transcript variants. The predominant transc…
- **Diseases (Open Targets)**: Protein-losing enteropathy (0.468); primary intestinal lymphangiectasia (0.466); complement deficiency (0.463); refractive error (0.360); diverticular disease (0.331)
- **Europe PMC papers**: 8137
- **Why important**: CD55 has the strongest network centrality in the supplied module and connects to several otherwise weakly connected branches, including EZR, SLC3A2, KYNU, AKR1C3, IKBIP, MTHFD1L and HSPA4L. It is a complement-regulatory glycoprotein, is detected in both tissues, is associated with neutrophils, and is the only module gene annotated as secreted to blood. Its disease and immune annotations provide a plausible interface between epithelial tissue and extracellular or immune context.
- **Conclusion**: Established evidence supports CD55 as a complement-protective and network-bridging gene that may help explain why this module is shared across tissues with possible vascular or immune context. The hypothesis that CD55 is the biological organizer of the entire module is not established; its centrality may instead reflect shared expression across mixed cell populations.

#### AKR1C3

- **Related proteins** (co-abundance neighbors): CD55 (0.86), KRT8 (0.85), OXCT1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldo-keto reductase family 1 member C3. This gene encodes a member of the aldo/keto reductase superfamily, which consists of more than 40 known enzymes and proteins. These enzymes catalyze the conversion of aldehydes and ketones to their corresponding alcohols by utilizing NADH and/or NADPH as cofactors. The enzymes display overlapping but distinct substrate specificity. This enzyme catalyzes the reduction of prostaglandin (PG) D2, PGH2…
- **Diseases (Open Targets)**: prostate cancer (0.129); Familial prostate cancer (0.129); hepatocellular carcinoma (0.114); posterior cortical atrophy (0.104); neoplasm (0.101)
- **Europe PMC papers**: 3255
- **Why important**: AKR1C3 occupies a connecting position between CD55, KRT8 and OXCT1. It is detected in both tissues and has annotations for prostaglandin, retinoid and steroid metabolism, as well as regulation of cell population proliferation. Its HPA associations include epithelial and hematopoietic cell types, and it has substantial literature together with cancer-related disease associations.
- **Conclusion**: Established evidence supports AKR1C3 as a metabolic and signaling-associated connector rather than as a member of the keratin filament itself. It could link epithelial structural state to lipid-derived signaling or tissue metabolism, but that proposed bridge is a hypothesis because no globally corrected metabolic term or direct STRING relationship was supplied.

## Module 1

**Tissue pair**: cervix_uterine and skin  
**Genes (23)**: NT5C3A, APMAP, PYCARD, CDK5RAP3, DHRS7, DIP2B, HADHB, GALNS, GCA, FECH, ITGB5, MVK, METAP2, MBOAT7, MYADM, SLC27A4, SAMD9, SQOR, SSH3, TAP1, ACAA2, UBAP1, URB2

### Function

The module does not have a statistically supported GO or KEGG functional enrichment: no globally significant GO/KEGG term passed global correction. Its gene-level composition nevertheless points to a mixed cellular program involving lipid and sterol handling, mitochondrial fatty-acid oxidation, membrane and vesicle biology, cytoskeletal regulation, antigen transport, lysosomal glycosaminoglycan degradation, and innate immune signaling. The strongest coherent functional threads are lipid metabolism through SLC27A4, ACAA2, HADHB, MBOAT7, MVK, DHRS7 and SQOR, together with cell-surface or intracellular trafficking through SLC27A4, UBAP1, ITGB5, TAP1 and GALNS. These are gene-level annotations and do not constitute significant module-level enrichment. The network is therefore better interpreted as a cross-tissue co-abundance program with several metabolic and immune-associated components than as a narrowly defined pathway module.

**Cell composition.** The module is not dominated by secreted or plasma proteins, since only a single member is annotated as secreted. It is also not uniformly blood-cell specific: most genes have low immune-cell specificity, although HPA links several members to neutrophils, eosinophils, basophils, monocytes or related myeloid populations. GCA is especially informative because it is tissue enriched in bone marrow and group enriched in neutrophil-related populations, while PYCARD, MBOAT7, MYADM and APMAP also have immune or neutrophil-associated HPA patterns. Conversely, many genes show epithelial, enterocyte, liver, skeletal-muscle or broadly distributed expression, and nearly all proteins are detected in at least one of the two tissues. Thus, the shared cervix_uterine and skin signal could reflect a combination of resident epithelial biology, metabolic state and variable myeloid-cell content rather than a single conserved tissue-specific mechanism. The HPA evidence does not support calling the module a plasma-protein module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides only a small set of high-confidence relationships within the module. The most direct metabolic connection is ACAA2 with HADHB, both involved in mitochondrial fatty-acid beta-oxidation, and ACAA2 also connects to MVK, which participates in mevalonate and sterol biosynthesis. These links support a real metabolic substructure rather than proving that the entire co-abundance module is a physical complex. No STRING functional-enrichment result was returned, and no hu.MAP complex contains multiple module members. Most module edges therefore lack corroboration from the supplied interaction resources. The network should be viewed as an abundance-based association network containing a limited known metabolic core, not as an established multiprotein complex.

**STRING interactions (score >= 0.7)**: 2 of 253 gene pairs: ACAA2–HADHB (0.961); ACAA2–MVK (0.833)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be claimed as a new biological pathway or complex. The absence of hu.MAP complexes and the sparse STRING support indicate that the overall cross-tissue co-abundance pattern is not already represented as a well-established shared complex. However, absence from these resources does not demonstrate novelty, because the module contains many broadly expressed genes, several poorly characterized relationships, and associations that may arise from shared cell composition or coordinated tissue state. The defensible conclusion is that the specific cervix_uterine and skin co-abundance configuration is potentially under-characterized, while its component biology is largely established and heterogeneous. Replication in independent cohorts, adjustment for cell composition, and comparison with published tissue co-expression resources would be required before describing it as a new finding.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial and tissue-stress state in cervix_uterine and skin that couples membrane lipid handling and mitochondrial fuel metabolism with vesicle trafficking and conditional innate immune activity. In this model, SLC27A4, MBOAT7, MVK, ACAA2 and HADHB support fatty-acid, phospholipid, sterol and mitochondrial metabolic remodeling; UBAP1, ITGB5 and GALNS contribute to membrane trafficking, adhesion or intracellular substrate processing; and PYCARD together with the HPA myeloid signatures reflects either local immune surveillance or variable myeloid-cell admixture. The hypothesis is consistent with the annotations and network structure, but it is not established by the nonsignificant enrichment analysis and requires validation with cell-resolved expression, protein measurements and perturbation experiments.

### Important genes

#### SLC27A4

- **Related proteins** (co-abundance neighbors): SAMD9 (0.88), DIP2B (0.84), CDK5RAP3 (0.82), NT5C3A (0.82), MVK (0.81), GALNS (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: solute carrier family 27 member 4. This gene encodes a member of a family of fatty acid transport proteins, which are involved in translocation of long-chain fatty acids cross the plasma membrane. This protein is expressed at high levels on the apical side of mature enterocytes in the small intestine, and appears to be the principal fatty acid transporter in enterocytes. Clinical studies suggest this gene as a candidate gene for th…
- **Diseases (Open Targets)**: ichthyosis prematurity syndrome (0.805); neurodegenerative disease (0.485); hereditary disease (0.471); lamellar ichthyosis (0.414); autosomal recessive disease (0.370)
- **Europe PMC papers**: 947
- **Why important**: SLC27A4 is the highest-connectivity node and links several otherwise distinct parts of the network, including SAMD9, DIP2B, CDK5RAP3, NT5C3A, MVK and GALNS. Its established function is long-chain fatty-acid transport, and its HPA profile is compatible with epithelial and enterocyte-like biology while showing detection in both tissues. Its disease associations include ichthyosis prematurity syndrome and lamellar ichthyosis, making it particularly relevant to skin barrier biology. The literature base is substantial, supporting stronger prior biological interpretation than for many peripheral nodes.
- **Conclusion**: Established: SLC27A4 is a lipid-transport gene with a central position in this module and relevance to epithelial barrier disease. Hypothesis: it may act as a metabolic anchor linking tissue lipid handling to the broader shared co-abundance state.

#### GCA

- **Related proteins** (co-abundance neighbors): GALNS (0.85), MYADM (0.83), METAP2 (0.83); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Group enriched; location Cytosol; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: grancalcin. This gene encodes a calcium-binding protein that is abundant in neutrophils and macrophages. In the absence of divalent cation, this protein localizes to the cytosolic fraction; with magnesium alone, it partitions with the granule fraction; and in the presence of magnesium and calcium, it associates with both the granule and membrane fractions. Alternative splicing and use of alternative promoters…
- **Diseases (Open Targets)**: intelligence (0.326); psoriasis (0.237); placenta praevia (0.232); psoriasis vulgaris (0.208); type 2 diabetes mellitus (0.128)
- **Europe PMC papers**: 91431
- **Why important**: GCA is the clearest indicator of a possible myeloid or blood-cell contribution. It is tissue enriched in bone marrow and group enriched in neutrophil-related populations, and its established function is calcium-dependent regulation of membrane and granule-associated behavior in neutrophils and macrophages. Its connection to GALNS, MYADM and METAP2 places an immune-associated node within the module. GCA also has a very substantial literature base and disease associations including psoriasis, which is relevant to skin inflammation.
- **Conclusion**: Established: GCA supports a neutrophil or myeloid component and is not a generic epithelial marker. Hypothesis: its presence may report immune-cell admixture or local innate immune activity shared by the tissues, rather than a direct metabolic role for the whole module.

#### ACAA2

- **Related proteins** (co-abundance neighbors): FECH (0.88), UBAP1 (0.81); STRING partners: HADHB (0.961), MVK (0.833)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: acetyl-CoA acyltransferase 2. The encoded protein catalyzes the last step of the mitochondrial fatty acid beta-oxidation spiral. Unlike most mitochondrial matrix proteins, it contains a non-cleavable amino-terminal targeting signal. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: bone remodeling disease (0.270); sinusitis (0.260); refractive error (0.190); kidney disorder (0.151); myopia (0.141)
- **Europe PMC papers**: 3056
- **Why important**: ACAA2 is a mitochondrial enzyme catalyzing the final step of fatty-acid beta-oxidation. It is directly connected in STRING to HADHB and MVK, providing the most explicit known interaction-supported metabolic bridge in the module. Its tissue-enhanced liver profile and epithelial metabolic associations complement the lipid-transport signal from SLC27A4. Its disease and literature records are substantial, including mitochondrial and metabolic relevance.
- **Conclusion**: Established: ACAA2 marks mitochondrial fatty-acid oxidation and belongs to the best-supported metabolic substructure of the module. Hypothesis: coordinated ACAA2 and SLC27A4 abundance may indicate matching fatty-acid uptake and oxidation demands in shared tissue states.

#### MBOAT7

- **Related proteins** (co-abundance neighbors): PYCARD (0.84), UBAP1 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: membrane bound acylglycerophosphatidylinositol O-acyltransferase MBOAT7. This gene encodes a member of the membrane-bound O-acyltransferases family of integral membrane proteins that have acyltransferase activity. The encoded protein is a lysophosphatidylinositol acyltransferase that has specificity for arachidonoyl-CoA as an acyl donor. This protein is involved in the reacylation of phospholipids as part of the phospholipid remodeling pathway known as the Land cycle. …
- **Diseases (Open Targets)**: intellectual disability, autosomal recessive 57 (0.754); hereditary disease (0.487); autosomal recessive non-syndromic intellectual disability (0.462); complex neurodevelopmental disorder (0.370); neurodegenerative disease (0.345)
- **Europe PMC papers**: 1344
- **Why important**: MBOAT7 provides a mechanistic link to phospholipid remodeling, especially arachidonoyl-containing phospholipids, and is connected in the module to UBAP1 and PYCARD. Its annotation supports membrane lipid composition as a possible interface between metabolism and inflammatory signaling. HPA associates it with several immune-cell populations, and its disease associations include inherited neurodevelopmental disorders. The literature base is established enough to support interpretation, while its lack of protein detection in the two listed tissues cautions against treating it as a confirmed local protein marker.
- **Conclusion**: Established: MBOAT7 participates in phospholipid remodeling and is network-adjacent to an innate immune adaptor. Hypothesis: it may couple membrane lipid remodeling to inflammatory responsiveness, although the tissue protein evidence is insufficient to establish that mechanism here.

#### PYCARD

- **Related proteins** (co-abundance neighbors): MBOAT7 (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: PYD and CARD domain containing. This gene encodes an adaptor protein that is composed of two protein-protein interaction domains: a N-terminal PYRIN-PAAD-DAPIN domain (PYD) and a C-terminal caspase-recruitment domain (CARD). The PYD and CARD domains are members of the six-helix bundle death domain-fold superfamily that mediates assembly of large signaling complexes in the inflammatory and apoptotic signaling pathways via the act…
- **Diseases (Open Targets)**: severe acute respiratory syndrome (0.370); neoplasm (0.086); Alzheimer disease (0.086); prostate cancer (0.085); Familial prostate cancer (0.085)
- **Europe PMC papers**: 3928
- **Why important**: PYCARD is an adaptor for inflammasome and related innate immune signaling, with established roles in activation of caspase-associated inflammatory complexes and antigen-related defense responses. It is connected to MBOAT7 and has HPA associations with lymphoid tissue, skin and multiple myeloid populations. Its disease and literature records are substantial, making it a biologically interpretable immune node despite its peripheral network position.
- **Conclusion**: Established: PYCARD is a plausible marker of innate immune signaling and myeloid-associated biology in the module. Hypothesis: PYCARD may represent inducible inflammatory activity in resident or infiltrating cells, but the co-abundance data do not show that it drives the metabolic genes.

#### GALNS

- **Related proteins** (co-abundance neighbors): GCA (0.85), SSH3 (0.85), URB2 (0.84), SLC27A4 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: galactosamine (N-acetyl)-6-sulfatase. This gene encodes N-acetylgalactosamine-6-sulfatase which is a lysosomal exohydrolase required for the degradation of the glycosaminoglycans, keratan sulfate, and chondroitin 6-sulfate. Sequence alterations including point, missense and nonsense mutations, as well as those that affect splicing, result in a deficiency of this enzyme. Deficiencies of this enzyme lead to Morquio A syndrome, a lysosom…
- **Diseases (Open Targets)**: mucopolysaccharidosis type 4A (0.873); mucopolysaccharidosis type 4 (0.745); hereditary disease (0.525); skeletal dysplasia (0.409); mucopolysaccharidosis (0.376)
- **Europe PMC papers**: 3367
- **Why important**: GALNS is a lysosomal enzyme required for degradation of keratan sulfate and chondroitin six-sulfate, and deficiency causes Morquio A syndrome. It has a relatively central position, connecting GCA, SSH3, URB2 and SLC27A4, thereby linking lysosomal processing with immune, cytoskeletal and lipid-associated nodes. Its disease associations and literature base are especially strong among the module genes. HPA detects the protein in both tissues and places it in intracellular and membrane compartments.
- **Conclusion**: Established: GALNS represents lysosomal glycosaminoglycan catabolism and is a well-supported disease-relevant node with broad network connections. Hypothesis: its position may reflect shared extracellular-matrix turnover or intracellular recycling demands in both tissues, but a direct role in the full module remains unproven.

## Module 2

**Tissue pair**: cervix_uterine and skin  
**Genes (17)**: APP, CDK13, DYNC2H1, EPHA2, EXOC1, IKBKB, ABCC4, PIK3C2A, PCCA, HSPG2, PIP4K2A, PI4KB, PKN1, PLS1, RFC5, RNF31, VPS8

### Function

This module is most consistent with a broadly distributed membrane-associated signaling, phosphoinositide-handling, vesicle-trafficking, cytoskeletal, and extracellular-matrix program. The primary enrichment supports generic ion binding and small-molecule binding across the module ((GO:MF ion binding; q_global = 0.00479), (GO:MF small molecule binding; q_global = 0.00747)), while receptor-complex enrichment involves APP, EPHA2, IKBKB, and RNF31 ((GO:CC receptor complex; q_global = 0.0483)). The strong overlap of every module gene with the broad molecular-function terms means that these terms establish biochemical breadth rather than a single specific pathway. Supplementary STRING signals for kinase and ATP-binding activities, cell periphery, and plasma membrane localization ((STRING COMPARTMENTS Cell periphery; within-query FDR = 0.0137) through (STRING Function Anion binding; within-query FDR = 0.0435)) support a coordinated signaling and membrane-trafficking interpretation. The gene annotations further connect the module to receptor signaling through EPHA2, PKN1, and IKBKB; phosphoinositide metabolism through PIK3C2A, PI4KB, and PIP4K2A; vesicle delivery through EXOC1 and VPS8; cytoskeletal organization through PKN1 and PLS1; and extracellular-matrix or cell-surface biology through HSPG2 and APP.

**Cell composition.** The module is not dominated by plasma proteins, secreted proteins, or immune-cell markers. Only APP and HSPG2 are annotated as secreted, with HSPG2 secreted to the extracellular matrix and APP secreted to blood. HSPG2 is also tissue enhanced in blood vessel and is not detected in immune cells, whereas APP has plasmacytoid-dendritic-cell enrichment but otherwise low tissue specificity. Most genes have low tissue specificity or broad cellular distribution, and the module contains several genes with cell-type-enhanced rather than blood-cell-specific expression. Platelet-associated annotations occur for PIP4K2A, and plasmacytoid-dendritic-cell enrichment occurs for EPHA2 and APP, but the overall HPA profile has low immune-cell specificity. Therefore, a blood-contamination explanation is not supported as the dominant interpretation, although shared epithelial, vascular, stromal, or other cell populations could contribute to the cervix_uterine and skin co-abundance pattern. Protein detection in both tissues for several genes, including PCCA, PKN1, PIK3C2A, HSPG2, RNF31, IKBKB, DYNC2H1, RFC5, and EXOC1, is compatible with a genuine tissue-shared cellular program.

**GO/KEGG enrichment**: 3 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF ion binding | 0.00479 | ABCC4, APP, CDK13, DYNC2H1, EPHA2, EXOC1, HSPG2, IKBKB, PCCA, PI4KB, PIK3C2A, PIP4K2A, PKN1, PLS1, RFC5, RNF31, VPS8 |
| GO:MF small molecule binding | 0.00747 | ABCC4, APP, CDK13, DYNC2H1, EPHA2, EXOC1, HSPG2, IKBKB, PCCA, PI4KB, PIK3C2A, PIP4K2A, PKN1, PLS1, RFC5, RNF31, VPS8 |
| GO:CC receptor complex | 0.0483 | APP, EPHA2, IKBKB, RNF31 |

### STRING and hu.MAP

STRING provides three high-confidence pairwise relationships within the module: APP with HSPG2, IKBKB with RNF31, and PI4KB with PIK3C2A. These relationships are established molecular links and support an extracellular or cell-surface interaction branch, an NF-kappa-B and linear ubiquitin-signaling branch, and a phosphoinositide-signaling branch, respectively. STRING functional enrichment also supports cell-periphery and plasma-membrane localization, kinase activity, ATP binding, and ion binding ((STRING Function Ion binding; within-query FDR = 0.0018) through (STRING Function Anion binding; within-query FDR = 0.0435)); these findings are supplementary and do not replace the globally corrected GO evidence. No hu.MAP complex contains multiple members of this module. Thus, the module is not explained by a recognized multi-protein complex; rather, it appears to combine several related cellular processes with only limited direct physical interaction support.

**STRING interactions (score >= 0.7)**: 3 of 136 gene pairs: APP–HSPG2 (0.841); IKBKB–RNF31 (0.879); PI4KB–PIK3C2A (0.912)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Ion binding (FDR = 0.0018, 17 genes); COMPARTMENTS Cell periphery (FDR = 0.0137, 11 genes); Keyword ATP-binding (FDR = 0.0152, 11 genes); COMPARTMENTS Plasma membrane (FDR = 0.0182, 10 genes); Keyword Kinase (FDR = 0.022, 7 genes); Function ATP binding (FDR = 0.0327, 11 genes); Function Phosphotransferase activity, alcohol group as acceptor (FDR = 0.0327, 7 genes); Function Carbohydrate derivative binding (FDR = 0.0327, 12 genes); Function Kinase activity (FDR = 0.0435, 7 genes); Function Anion binding (FDR = 0.0435, 12 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module should not be declared a wholly new molecular mechanism. Several of its relationships are already represented in STRING, and the functions of its major genes are established in the literature. Nevertheless, the co-abundance association of this particular gene collection across cervix_uterine and skin may represent a new tissue-pair-level observation, because the module has no corresponding hu.MAP multi-member complex and only a sparse set of known within-module STRING links. That observation is suggestive rather than proof of novelty: absence from STRING or hu.MAP does not establish that the co-abundance pattern or its biological interpretation is previously unknown. The appropriate claim is a potentially novel cross-tissue co-abundance module built from largely established genes and partial known interactions.

**Hypothesis.** Hypothesis: in epithelial or vascular-associated cells shared by cervix_uterine and skin, coordinated abundance of EPHA2, PKN1, PIK3C2A, PI4KB, and PIP4K2A may couple receptor and phosphoinositide signaling to actin remodeling, exocytosis, endocytic trafficking, and cell-surface organization. HSPG2 and APP could provide extracellular or membrane-associated scaffolding, while IKBKB and RNF31 could connect the state to regulated inflammatory or NF-kappa-B signaling. PCCA, DYNC2H1, RFC5, and the remaining broadly expressed genes may reflect metabolic, ciliary, replication, and housekeeping requirements of the contributing cells rather than one unified signaling complex. This model predicts coordinated regulation of membrane organization and stress-responsive signaling, but it requires validation with cell-type-resolved expression, perturbation experiments, and direct protein or phosphoinositide measurements.

### Important genes

#### EPHA2

- **Related proteins** (co-abundance neighbors): PKN1 (0.85), HSPG2 (0.85), PIP4K2A (0.83), PCCA (0.82), APP (0.82), PLS1 (0.81), DYNC2H1 (0.81), ABCC4 (0.80), PI4KB (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane, Cell Junctions; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: EPH receptor A2. This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are d…
- **Diseases (Open Targets)**: early-onset posterior polar cataract (0.770); total early-onset cataract (0.770); early-onset non-syndromic cataract (0.681); colorectal cancer (0.594); chronic myeloid leukemia (0.583)
- **Europe PMC papers**: 8524
- **Why important**: EPHA2 is the central network connector in the module, linking PKN1, HSPG2, PIP4K2A, PCCA, APP, PLS1, DYNC2H1, and ABCC4. It is present in all primary GO terms ((GO:MF ion binding; q_global = 0.00479), (GO:MF small molecule binding; q_global = 0.00747), (GO:CC receptor complex; q_global = 0.0483)) and all listed STRING supplementary terms. Its established function as an Eph receptor tyrosine kinase, together with annotations for cell-surface receptor signaling, angiogenesis, stress response, and lamellipodium assembly, makes it a strong candidate for connecting membrane signaling to epithelial or vascular organization. It also has substantial literature and disease associations including cataract and cancer.
- **Conclusion**: Established evidence supports EPHA2 as the principal signaling and membrane-organizing hub of this module. It is plausible, but not demonstrated, that EPHA2 coordinates the cross-tissue co-abundance state.

#### PKN1

- **Related proteins** (co-abundance neighbors): EPHA2 (0.85), CDK13 (0.83), EXOC1 (0.80), PCCA (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Plasma membrane; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase N1. The protein encoded by this gene belongs to the protein kinase C superfamily. This kinase is activated by Rho family of small G proteins and may mediate the Rho-dependent signaling pathway. This kinase can be activated by phospholipids and by limited proteolysis. The 3-phosphoinositide dependent protein kinase-1 (PDPK1/PDK1) is reported to phosphorylate this kinase, which may mediate insulin signa…
- **Diseases (Open Targets)**: neurodegenerative disease (0.344); Alzheimer disease (0.300); Parkinson disease (0.296); lysosomal storage disease (0.296); exocrine pancreatic carcinoma (0.273)
- **Europe PMC papers**: 1034
- **Why important**: PKN1 is a network connector between EPHA2, CDK13, EXOC1, and PCCA and is represented in the primary binding terms ((GO:MF ion binding; q_global = 0.00479), (GO:MF small molecule binding; q_global = 0.00747)) and broadly across the STRING supplementary terms. It is a Rho-regulated protein kinase that can link phospholipid signaling to the actin cytoskeleton, epithelial migration, and intracellular signaling. Its membrane location and detection in both tissues make it particularly relevant to a shared tissue-cellular program. Its literature is more moderate than that of APP or EPHA2, but its functional position is highly informative.
- **Conclusion**: Established evidence supports PKN1 as a plausible cytoskeletal and motility effector within the module. Its role as a bridge between receptor signaling and exocytic or actin remodeling processes remains a mechanistic interpretation rather than a demonstrated property of this module.

#### PIK3C2A

- **Related proteins** (co-abundance neighbors): PCCA (0.89), VPS8 (0.87); STRING partners: PI4KB (0.912)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 alpha. The protein encoded by this gene belongs to the phosphoinositide 3-kinase (PI3K) family. PI3-kinases play roles in signaling pathways involved in cell proliferation, oncogenic transformation, cell survival, cell migration, and intracellular protein trafficking. This protein contains a lipid kinase catalytic domain as well as a C-terminal C2 domain, a characteristic of class II PI3-kinases. C2 doma…
- **Diseases (Open Targets)**: oculocerebrodental syndrome (0.750); Short stature (0.333); Alzheimer disease (0.325); Parkinson disease (0.323); neurodegenerative disease (0.323)
- **Europe PMC papers**: 1123
- **Why important**: PIK3C2A connects PCCA and VPS8 in the co-abundance network and has a known STRING relationship with PI4KB. It is present in the primary binding terms ((GO:MF ion binding; q_global = 0.00479), (GO:MF small molecule binding; q_global = 0.00747)) and in all listed STRING supplementary terms. Its established class II phosphoinositide 3-kinase activity, together with roles in phosphatidylinositol biosynthesis, exocytosis, endocytosis, receptor signaling, and autophagy, gives it a direct functional link to the module's membrane-trafficking interpretation. It also has disease associations including oculocerebrodental syndrome and neurodegenerative disease.
- **Conclusion**: Established evidence supports PIK3C2A as a core lipid-signaling and trafficking component. The module may coordinate PIK3C2A with PI4KB, but co-abundance alone does not establish a joint enzymatic pathway in these tissues.

#### HSPG2

- **Related proteins** (co-abundance neighbors): RNF31 (0.86), EPHA2 (0.85); STRING partners: APP (0.841)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location None; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate proteoglycan 2. This gene encodes the perlecan protein, which consists of a core protein to which three long chains of glycosaminoglycans (heparan sulfate or chondroitin sulfate) are attached. The perlecan protein is a large multidomain proteoglycan that binds to and cross-links many extracellular matrix components and cell-surface molecules. It has been shown that this protein interacts with laminin, prolargin, …
- **Diseases (Open Targets)**: Schwartz-Jampel syndrome (0.802); Silverman-Handmaker type dyssegmental dysplasia (0.767); atrial fibrillation (0.573); COVID-19 (0.547); dengue disease (0.462)
- **Europe PMC papers**: 3887
- **Why important**: HSPG2 links EPHA2 and RNF31 in the module and has the known STRING relationship with APP. It appears in the primary binding terms ((GO:MF ion binding; q_global = 0.00479), (GO:MF small molecule binding; q_global = 0.00747)) and in the STRING cell-periphery and plasma-membrane-related terms ((STRING Function Ion binding; within-query FDR = 0.0018), (STRING COMPARTMENTS Cell periphery; within-query FDR = 0.0137), (STRING COMPARTMENTS Plasma membrane; within-query FDR = 0.0182)). Perlecan is an extracellular-matrix proteoglycan that cross-links matrix and cell-surface molecules, and HPA places it in the extracellular matrix, with blood-vessel tissue enhancement and detection in both tissues. Its disease associations include skeletal dysplasia and Schwartz-Jampel syndrome, and it has substantial literature.
- **Conclusion**: Established evidence supports HSPG2 as the extracellular-matrix and cell-surface scaffolding component of the module. It could organize or stabilize signaling interactions at tissue interfaces, but that scaffolding role within this co-abundance module is a hypothesis.

#### IKBKB

- **Related proteins** (co-abundance neighbors): PCCA (0.81); STRING partners: RNF31 (0.879)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: inhibitor of nuclear factor kappa B kinase subunit beta. The protein encoded by this gene phosphorylates the inhibitor in the inhibitor/NF-kappa-B complex, causing dissociation of the inhibitor and activation of NF-kappa-B. The encoded protein itself is found in a complex of proteins. Several transcript variants, some protein-coding and some not, have been found for this gene. [provided by RefSeq, Sep 2011].
- **Diseases (Open Targets)**: severe combined immunodeficiency due to IKK2 deficiency (0.778); immunodeficiency 15a (0.649); severe combined immunodeficiency (0.592); COVID-19 (0.482); combined immunodeficiency (0.466)
- **Europe PMC papers**: 4855
- **Why important**: IKBKB is included in all primary GO terms ((GO:MF ion binding; q_global = 0.00479), (GO:MF small molecule binding; q_global = 0.00747), (GO:CC receptor complex; q_global = 0.0483)) and all listed STRING supplementary terms. Its known function is phosphorylation of the inhibitor in the NF-kappa-B complex, with roles in pattern-recognition, Toll-like-receptor, inflammatory, and antigen-processing pathways. Its established STRING relationship with RNF31 connects it to the linear ubiquitin-assembly machinery. It is detected in both tissues, has low immune-cell specificity, and has well-established immunodeficiency disease associations.
- **Conclusion**: Established evidence supports IKBKB as an inflammatory and receptor-signaling component that is not necessarily evidence of blood-cell contamination. Its co-abundance with RNF31 may indicate coordinated stress or innate-signaling capacity, but activation of NF-kappa-B in these samples is not proven.

#### PCCA

- **Related proteins** (co-abundance neighbors): PIK3C2A (0.89), EPHA2 (0.82), IKBKB (0.81), RFC5 (0.81), PKN1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit alpha. The protein encoded by this gene is the alpha subunit of the heterodimeric mitochondrial enzyme Propionyl-CoA carboxylase. PCCA encodes the biotin-binding region of this enzyme. Mutations in either PCCA or PCCB (encoding the beta subunit) lead to an enzyme deficiency resulting in propionic acidemia. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by…
- **Diseases (Open Targets)**: propionic acidemia (0.853); hereditary disease (0.487); dilated cardiomyopathy (0.370); neurodegenerative disease (0.357); pontocerebellar hypoplasia type 2D (0.340)
- **Europe PMC papers**: 2633
- **Why important**: PCCA is a connector linking PIK3C2A, EPHA2, IKBKB, RFC5, and PKN1, and it contributes to the primary binding terms ((GO:MF ion binding; q_global = 0.00479), (GO:MF small molecule binding; q_global = 0.00747)) and several STRING supplementary terms. Its established role is the biotin-binding alpha subunit of mitochondrial propionyl-CoA carboxylase, supporting branched-chain amino-acid and short-chain-fatty-acid metabolism. It is tissue enhanced in epididymis, detected in both tissues, and strongly associated with propionic acidemia and related metabolic disease. Its network placement suggests that metabolic state may be coupled to signaling abundance.
- **Conclusion**: Established evidence supports PCCA as a mitochondrial metabolic component rather than a receptor or scaffold. Its inclusion may reflect metabolic support for the shared cell state, but a direct metabolic-signaling mechanism within this module remains hypothetical.

## Module 3

**Tissue pair**: cervix_uterine and skin  
**Genes (15)**: PRKAG1, B3GLCT, CDK9, CHEK1, LIG1, ILK, RPS6KA1, MARCKS, MAP2K4, ROCK1, POLR2B, SACK1H, SLK, TLK1, ZNF106

### Function

The strongest interpretation is a conserved intracellular protein-phosphorylation and signal-integration module. The primary evidence is the coherent set of globally corrected terms (GO:MF protein kinase activity; q_global = 0.000104) through (GO:MF transferase activity; q_global = 0.0104), which collectively identify protein kinase activity, serine/threonine kinase activity, phosphotransferase activity, and protein phosphorylation. The kinase-rich genes include CHEK1, ILK, MAP2K4, PRKAG1, ROCK1, RPS6KA1, SLK, TLK1, and CDK9. Their annotations span DNA-damage and replication checkpoints, MAPK signaling, focal-adhesion and cytoskeletal regulation, energy sensing, chromatin organization, and transcriptional control. This is therefore broader than a single linear pathway: it is most consistent with a shared regulatory state involving cell-cycle integrity, stress responses, adhesion or migration, and transcription. The STRING enrichment results (STRING Function Protein serine/threonine kinase activity; within-query FDR = 5.62e-06) through (STRING Function Carbohydrate derivative binding; within-query FDR = 0.0054) independently support the kinase and phosphorylation interpretation, but they remain supplementary rather than global enrichment evidence. The non-kinase members may represent connected cellular contexts rather than a separate dominant function.

**Cell composition.** This does not look like a plasma-protein or secreted-protein module: the HPA summary identifies only a minority as secreted, and most members are intracellular, including nucleoplasmic, cytosolic, focal-adhesion, membrane, or nuclear-body proteins. The module is also not uniformly blood-cell specific. Most genes have low tissue specificity, while several show enhanced cell-type patterns. Nevertheless, immune and blood-related signals are present, especially neutrophil-associated patterns, T-reg or monocyte associations, erythrocyte-progenitor associations, and platelet or megakaryocyte associations. Thus, shared abundance could reflect a common epithelial, stromal, or proliferative cellular program, but contribution from immune or other shared cell types cannot be excluded. Protein detection in both cervix and skin for many members is compatible with a genuine shared tissue program, although the lack of uniform tissue specificity argues against treating the module as an organ-exclusive signature.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF protein kinase activity | 0.000104 | CDK9, CHEK1, ILK, MAP2K4, PRKAG1, ROCK1, RPS6KA1, SLK, TLK1 |
| GO:MF transferase activity, transferring phosphorus-containing groups | 0.000447 | CDK9, CHEK1, ILK, MAP2K4, POLR2B, PRKAG1, ROCK1, RPS6KA1, SLK, TLK1 |
| GO:MF phosphotransferase activity, alcohol group as acceptor | 0.000534 | CDK9, CHEK1, ILK, MAP2K4, PRKAG1, ROCK1, RPS6KA1, SLK, TLK1 |
| GO:MF protein serine/threonine kinase activity | 0.000558 | CDK9, CHEK1, MAP2K4, PRKAG1, ROCK1, RPS6KA1, SLK, TLK1 |
| GO:BP protein phosphorylation | 0.00096 | CDK9, CHEK1, ILK, MAP2K4, PRKAG1, ROCK1, RPS6KA1, SLK, TLK1 |
| GO:MF kinase activity | 0.00134 | CDK9, CHEK1, ILK, MAP2K4, PRKAG1, ROCK1, RPS6KA1, SLK, TLK1 |
| GO:BP phosphorylation | 0.00175 | CDK9, CHEK1, ILK, MAP2K4, PRKAG1, ROCK1, RPS6KA1, SLK, TLK1 |
| GO:MF protein serine kinase activity | 0.0032 | CDK9, CHEK1, MAP2K4, ROCK1, RPS6KA1, SLK, TLK1 |
| GO:MF transferase activity | 0.0104 | B3GLCT, CDK9, CHEK1, ILK, MAP2K4, POLR2B, PRKAG1, ROCK1, RPS6KA1, SLK, TLK1 |

### STRING and hu.MAP

The high-confidence STRING network is sparse: the only reported high-confidence physical or functional pair is CHEK1-LIG1. This relationship is biologically coherent because CHEK1 coordinates DNA-damage and replication checkpoints whereas LIG1 functions in DNA replication and repair. The strong STRING functional enrichment (STRING Function Protein serine/threonine kinase activity; within-query FDR = 5.62e-06) through (STRING Function Carbohydrate derivative binding; within-query FDR = 0.0054) therefore supports shared annotation and kinase-domain content more strongly than it demonstrates a densely connected physical complex. The hu.MAP evidence is limited to (hu.MAP huMAP3_12394.1), where SACK1H and ZNF106 occur together in a much larger trafficking-associated complex. This provides some complex-context support for those genes, but the small representation of the complex within the module does not establish that the whole module is that complex. Overall, the co-abundance edges appear to capture a regulatory or cellular-state relationship that is only partly represented by currently catalogued protein interactions.

**STRING interactions (score >= 0.7)**: 1 of 105 gene pairs: CHEK1–LIG1 (0.794)
**STRING functional enrichment (supplementary, within-query FDR)**: Function Protein serine/threonine kinase activity (FDR = 5.62e-06, 9 genes); Function Transferase activity, transferring phosphorus-containing groups (FDR = 2.47e-05, 10 genes); Keyword Serine/threonine-protein kinase (FDR = 2.63e-05, 8 genes); InterPro Protein kinase domain (FDR = 6.4e-05, 8 genes); InterPro Serine/threonine-protein kinase, active site (FDR = 0.00012, 7 genes); InterPro Protein kinase-like domain superfamily (FDR = 0.00012, 8 genes); InterPro Protein kinase, ATP binding site (FDR = 0.00012, 7 genes); Process Protein phosphorylation (FDR = 0.00019, 9 genes); Function Protein serine kinase activity (FDR = 0.00019, 7 genes); Function Transferase activity (FDR = 0.00025, 11 genes); SMART Serine/Threonine protein kinases, catalytic domain (FDR = 0.00068, 6 genes); Keyword Transferase (FDR = 0.00078, 10 genes); Keyword ATP-binding (FDR = 0.0024, 10 genes); Function ATP binding (FDR = 0.005, 10 genes); Function Carbohydrate derivative binding (FDR = 0.0054, 11 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_12394.1 (SACK1H, ZNF106; 2/98)

### Novelty

The module should not be called a wholly new biological pathway. Its central activities, including checkpoint control, MAPK signaling, cytoskeletal regulation, transcriptional elongation, and energy sensing, are established biology, and the CHEK1-LIG1 relationship is already represented in STRING. The co-abundance combination across cervix_uterine and skin may still be a potentially novel tissue-pair observation, particularly because the module is kinase-enriched but has little high-confidence STRING connectivity and only limited hu.MAP representation. That is a dataset-level novelty claim rather than proof of a new molecular mechanism. Absence of additional STRING or hu.MAP links is informative about current database coverage, not evidence that the relationships are biologically absent. Independent replication, cell-composition adjustment, and perturbation or phosphoproteomic testing would be needed to establish novelty.

**Hypothesis.** Hypothesis: in both cervix_uterine and skin, a shared mixture of proliferative, stress-responsive, and adhesion-related cellular states produces coordinated abundance of kinase and kinase-associated proteins. CHEK1 and LIG1 may couple replication or DNA-repair demand to the module, while CDK9 and POLR2B link the state to RNA-polymerase-II transcription. MAP2K4 and RPS6KA1 could transmit stress or growth signals, and ROCK1, ILK, SLK, and MARCKS could connect those signals to cell adhesion, cytoskeletal remodeling, migration, and membrane behavior. PRKAG1 may provide an energy-status component, and TLK1 may connect replication stress with chromatin organization. The hypothesis predicts that module activity will track cellular stress, proliferation, or tissue remodeling rather than secretion, and that some apparent cross-tissue conservation may be mediated by shared immune or stromal cell populations.

### Important genes

#### CHEK1

- **Related proteins** (co-abundance neighbors): ILK (0.95), PRKAG1 (0.85), SLK (0.82), CDK9 (0.82), POLR2B (0.81); STRING partners: LIG1 (0.794)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: checkpoint kinase 1. The protein encoded by this gene belongs to the Ser/Thr protein kinase family. It is required for checkpoint mediated cell cycle arrest in response to DNA damage or the presence of unreplicated DNA. This protein acts to integrate signals from ATM and ATR, two cell cycle proteins involved in DNA damage responses, that also associate with chromatin in meiotic prophase I. Phosphorylation of CDC25A pr…
- **Diseases (Open Targets)**: neurodegenerative disease (0.542); oocyte/zygote/embryo maturation arrest 21 (0.482); female infertility due to oocyte meiotic arrest (0.370); Male infertility due to gonadal dysgenesis or sperm disorder (0.266); alopecia areata (0.172)
- **Europe PMC papers**: 9282
- **Why important**: CHEK1 is the most connected and strongest hub in the module and participates in every primary enrichment term (GO:MF protein kinase activity; q_global = 0.000104) through (GO:MF transferase activity; q_global = 0.0104). It is an established serine/threonine checkpoint kinase integrating DNA-damage and replication signals, and its direct STRING relationship with LIG1 provides the clearest known molecular link inside the module. Its broad disease relevance and extensive literature make it a particularly informative anchor for testing whether the module reflects replication stress or proliferative state.
- **Conclusion**: Established evidence supports CHEK1 as a central checkpoint kinase and as the best-supported interaction hub. It is plausible, but not demonstrated here, that CHEK1 helps explain the shared module across the two tissues.

#### ROCK1

- **Related proteins** (co-abundance neighbors): B3GLCT (0.84), LIG1 (0.83), ZNF106 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: Rho associated coiled-coil containing protein kinase 1. This gene encodes a protein serine/threonine kinase that is activated when bound to the GTP-bound form of Rho. The small GTPase Rho regulates formation of focal adhesions and stress fibers of fibroblasts, as well as adhesion and aggregation of platelets and lymphocytes by shuttling between the inactive GDP-bound form and the active GTP-bound form. Rho is also essential in cytokinesis and plays a r…
- **Diseases (Open Targets)**: open-angle glaucoma (0.605); ocular hypertension (0.590); glaucoma (0.563); neurodegenerative disease (0.555); graft versus host disease (0.554)
- **Europe PMC papers**: 9251
- **Why important**: ROCK1 is a connected kinase with links to B3GLCT, LIG1, and ZNF106 and is represented across all primary kinase and phosphorylation terms (GO:MF protein kinase activity; q_global = 0.000104) through (GO:MF transferase activity; q_global = 0.0104). Its established function downstream of Rho connects signaling to cytokinesis, focal adhesions, stress fibers, smooth-muscle behavior, and leukocyte adhesion. Its detection in both tissues and neutrophil-associated HPA pattern make it a strong candidate for linking tissue remodeling with possible cell-composition effects.
- **Conclusion**: Established evidence supports ROCK1 as a cytoskeletal and adhesion regulator with relevant immune-cell associations. Its role as the module's tissue-remodeling bridge remains a hypothesis requiring cell-resolved validation.

#### ILK

- **Related proteins** (co-abundance neighbors): CHEK1 (0.95), LIG1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Focal adhesion sites; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: integrin linked kinase. This gene encodes a protein with a kinase-like domain and four ankyrin-like repeats. The encoded protein associates at the cell membrane with the cytoplasmic domain of beta integrins, where it regulates integrin-mediated signal transduction. Activity of this protein is important in the epithelial to mesenchymal transition, and over-expression of this gene is implicated in tumor growth and metastas…
- **Diseases (Open Targets)**: neurodegenerative disease (0.468); familial hypertrophic cardiomyopathy (0.194); Abnormality of the cardiovascular system (0.148); Prolonged QT interval (0.118); neoplasm (0.118)
- **Europe PMC papers**: 8401
- **Why important**: ILK occupies a highly weighted connection to CHEK1 and also connects to LIG1. It is included in most primary kinase terms (GO:MF protein kinase activity; q_global = 0.000104) through (GO:MF phosphotransferase activity, alcohol group as acceptor; q_global = 0.000534), (GO:BP protein phosphorylation; q_global = 0.00096), (GO:MF kinase activity; q_global = 0.00134), and (GO:MF transferase activity; q_global = 0.0104), while its focal-adhesion location and integrin-linked signaling provide a direct mechanistic route from extracellular matrix attachment to intracellular regulation. Its association with epithelial-to-mesenchymal transition and tumor growth gives it disease and remodeling relevance. HPA detects it in cervix_uterine but not skin, so it may be a tissue-asymmetric component of a shared abundance program.
- **Conclusion**: Established evidence supports ILK as an integrin-associated signaling and adhesion regulator, although its kinase-like domain should not by itself be interpreted as proof of catalytic kinase activity. Its contribution to cross-tissue conservation is a testable hypothesis.

#### SLK

- **Related proteins** (co-abundance neighbors): SACK1H (0.87), CHEK1 (0.82), TLK1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: STE20 like kinase. Enables protein homodimerization activity and protein serine/threonine kinase activity. Involved in several processes, including cytoplasmic microtubule organization; protein autophosphorylation; and regulation of focal adhesion assembly. Located in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.448); uterine corpus leiomyoma (0.408); stroke disorder (0.339); coronary artery disorder (0.288); Menorrhagia (0.202)
- **Europe PMC papers**: 2571
- **Why important**: SLK is connected to SACK1H, CHEK1, and TLK1 and is present in every primary enrichment term (GO:MF protein kinase activity; q_global = 0.000104) through (GO:MF transferase activity; q_global = 0.0104). Its established annotations include serine/threonine kinase activity, focal-adhesion regulation, cytoplasmic microtubule organization, cell migration, and apoptosis-related regulation. It is detected by HPA in both tissues, and its literature supports a role in linking cytoskeletal organization with intracellular signaling.
- **Conclusion**: Established evidence supports SLK as a shared cytoplasmic kinase associated with migration and adhesion. The apparent connection between SLK, checkpoint control, and chromatin-related genes is a module-level hypothesis rather than an established single pathway.

#### CDK9

- **Related proteins** (co-abundance neighbors): CHEK1 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: cyclin dependent kinase 9. The protein encoded by this gene is a member of the cyclin-dependent protein kinase (CDK) family. CDK family members are highly similar to the gene products of S. cerevisiae cdc28, and S. pombe cdc2, and known as important cell cycle regulators. This kinase was found to be a component of the multiprotein complex TAK/P-TEFb, which is an elongation factor for RNA polymerase II-directed transcription…
- **Diseases (Open Targets)**: HIV infectious disease (0.595); Global developmental delay (0.463); Intellectual disability (0.370); choanal atresia (0.370); Abnormal vertebral morphology (0.370)
- **Europe PMC papers**: 8266
- **Why important**: CDK9 is a connected module member linked to CHEK1 and is represented in every primary term (GO:MF protein kinase activity; q_global = 0.000104) through (GO:MF transferase activity; q_global = 0.0104) and throughout the supplementary STRING kinase terms. It is an established component of transcriptional elongation through RNA polymerase II and also has roles in cell-cycle and DNA-repair regulation. Its co-abundance with POLR2B provides a plausible transcriptional dimension to a module otherwise dominated by signaling kinases, while its substantial literature and disease associations make it a useful regulatory readout.
- **Conclusion**: Established evidence supports CDK9 as a transcriptional kinase that can couple signaling state to gene expression. Whether it drives the shared tissue module or simply marks a broadly active transcriptional state is unresolved.

## Module 4

**Tissue pair**: cervix_uterine and skin  
**Genes (33)**: ABCB7, ARIH1, ASCC3, NCAPH, DCAF13, DPYSL2, EFL1, FADS1, FASN, FLOT1, KIF11, MAP1S, MCM2, MCM4, MCM7, MOV10, NUP155, NUP205, PHAX, PLOD2, PODXL, PRRC2A, PUM1, ATIC, RAB3GAP2, ARHGAP17, SCD, SEH1L, USO1, WDR44, CSE1L, XPO5, ZC3HAV1

### Function

This is a heterogeneous intracellular module with three prominent components. The FADS1–SCD–FASN relationships support fatty-acid desaturation and lipid biosynthesis, while the coordinated MCM2–MCM4–MCM7 relationships support DNA replication initiation and replication-fork biology. Nuclear transport and RNA-handling are represented by CSE1L, NUP205, NUP155, SEH1L, XPO5, PHAX, PUM1 and MOV10. Mitotic chromosome and spindle functions are also compatible with the KIF11 and NCAPH relationships. Thus, the most defensible interpretation is a shared proliferative and biosynthetic state involving lipid metabolism, genome duplication, nucleocytoplasmic transport and post-transcriptional regulation, rather than a single narrowly defined biological pathway. No GO or KEGG term passed global correction; therefore the functional interpretation rests on individual gene annotations, network structure, STRING relationships and hu.MAP complex membership rather than on globally significant enrichment.

**Cell composition.** The module is not dominated by plasma proteins or secreted proteins. The HPA summary identifies only a single secreted gene, and most proteins are intracellular, with nuclear, cytosolic, mitochondrial, endoplasmic-reticulum or membrane localizations. Most genes have low tissue specificity, while a substantial subset is enhanced in bone marrow and in erythrocyte or megakaryocyte progenitor populations. This pattern is compatible with broadly expressed housekeeping and proliferation-associated biology, with a possible contribution from shared progenitor or cycling-cell content in the cervix and skin samples. The HPA data do not support a predominantly immune-cell module, although selected genes show enhancement in particular blood or progenitor populations. Protein detection in both tissues is widespread, so the shared signal is biologically plausible but should not automatically be interpreted as cervix-specific or skin-specific biology.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides direct support for several coherent relationships. FADS1 is linked to SCD, and SCD is linked to FASN, forming a lipid-biosynthetic subnetwork. MCM2, MCM4 and MCM7 are strongly connected to one another, and KIF11 connects to the MCM proteins and NCAPH, supporting a replication and mitotic-chromosome component. NUP155, NUP205 and SEH1L form a nuclear-pore relationship, with NUP205 also connected to XPO5; CSE1L is linked to XPO5. These are known relationships and make parts of the module mechanistically credible, but they do not establish that every co-abundance edge reflects physical interaction. hu.MAP independently supports the MCM2–MCM4–MCM7 complexes across (hu.MAP huMAP3_06061.1), (hu.MAP huMAP3_05529.1), (hu.MAP huMAP3_07113.1), (hu.MAP huMAP3_14758.1), (hu.MAP huMAP3_08554.1), (hu.MAP huMAP3_11832.1), (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_09860.1), (hu.MAP huMAP3_00154.1), (hu.MAP huMAP3_11119.1), (hu.MAP huMAP3_09466.1), (hu.MAP huMAP3_10862.1) and (hu.MAP huMAP3_14306.1). It also places SCD with ABCB7 and CSE1L in (hu.MAP huMAP3_06791.1), (hu.MAP huMAP3_09592.1) and (hu.MAP huMAP3_08167.1), CSE1L with NUP205 in (hu.MAP huMAP3_09042.1), PUM1 with MOV10 in (hu.MAP huMAP3_06975.1), and NUP155 with SEH1L in (hu.MAP huMAP3_12581.1). These complexes show that the module contains several established molecular subassemblies, but the complete module is not itself a single known complex.

**STRING interactions (score >= 0.7)**: 15 of 528 gene pairs: CSE1L–XPO5 (0.766); FADS1–SCD (0.959); FASN–SCD (0.96); KIF11–MCM2 (0.848); KIF11–MCM4 (0.874); KIF11–MCM7 (0.745); KIF11–NCAPH (0.908); MCM2–MCM4 (0.999); MCM2–MCM7 (0.999); MCM4–MCM7 (0.999); MCM4–NCAPH (0.711); NUP155–NUP205 (0.999); NUP155–SEH1L (0.999); NUP205–SEH1L (0.999); NUP205–XPO5 (0.755)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06791.1 (SCD, ABCB7, CSE1L, NUP205; 4/31); huMAP3_06061.1 (MCM4, MCM7, MCM2; 3/5); huMAP3_05529.1 (MCM4, MCM7, MCM2; 3/6); huMAP3_07113.1 (MCM4, MCM7, MCM2; 3/6); huMAP3_14758.1 (MCM4, MCM7, MCM2; 3/14); huMAP3_08554.1 (MCM4, MCM7, MCM2; 3/15); huMAP3_11832.1 (MCM4, MCM7, MCM2; 3/15); huMAP3_12180.1 (MCM4, MCM7, MCM2; 3/17); huMAP3_09592.1 (SCD, ABCB7, CSE1L; 3/95); huMAP3_09860.1 (MCM4, MCM2; 2/4); huMAP3_00154.1 (MCM4, MCM2; 2/5); huMAP3_11119.1 (MCM4, MCM7; 2/14); huMAP3_09466.1 (MCM4, MCM2; 2/23); huMAP3_08167.1 (SCD, ABCB7; 2/24); huMAP3_09042.1 (CSE1L, NUP205; 2/26); huMAP3_06975.1 (PUM1, MOV10; 2/31); huMAP3_10862.1 (MCM4, MCM2; 2/33); huMAP3_14306.1 (MCM4, MCM2; 2/55); huMAP3_12581.1 (NUP155, SEH1L; 2/58)

### Novelty

The module should not be called a wholly new molecular pathway. Several of its internal relationships are already established by STRING and hu.MAP, especially the MCM replication assemblies, the nuclear-pore relationships and the fatty-acid enzyme relationships. The potentially distinctive observation is their co-abundance as one conserved module across cervix_uterine and skin. However, the absence of a matching entry in interaction resources would not prove novelty, and the fact sheet does not demonstrate prior absence from tissue co-abundance studies. Because the module has no globally significant GO or KEGG enrichment, no STRING functional enrichment, and contains multiple functional subcomponents, the appropriate conclusion is that it is a potentially interesting cross-tissue co-abundance configuration requiring replication, not a demonstrated novel biological discovery.

**Hypothesis.** Hypothesis: the module reflects a shared cycling or biosynthetically active cell state present in both tissues. In this model, increased demand for membrane lipid production is represented by FADS1 and SCD, while DNA synthesis and mitotic progression are represented by the MCM subnetwork, KIF11 and NCAPH. Nuclear pores and RNA-export or RNA-regulatory proteins could coordinate the transport and processing of transcripts needed for this state. The HPA pattern raises the alternative possibility that shared progenitor-like or proliferative cell content, rather than a tissue-specific program, drives the conservation. This hypothesis should be tested with cell-resolved data, independent cohorts and measurements of cell-cycle, lipid metabolism and cell-composition markers.

### Important genes

#### FADS1

- **Related proteins** (co-abundance neighbors): ASCC3 (0.90), KIF11 (0.86), PUM1 (0.85), ARHGAP17 (0.84), PRRC2A (0.84), NCAPH (0.81), EFL1 (0.81), MCM7 (0.81), PLOD2 (0.81), DPYSL2 (0.81), MCM2 (0.80); STRING partners: SCD (0.959)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: fatty acid desaturase 1. The protein encoded by this gene is a member of the fatty acid desaturase (FADS) gene family. Desaturase enzymes regulate unsaturation of fatty acids through the introduction of double bonds between defined carbons of the fatty acyl chain. FADS family members are considered fusion products composed of an N-terminal cytochrome b5-like domain and a C-terminal multiple membrane-spanning desaturase po…
- **Diseases (Open Targets)**: neurodegenerative disease (0.554); Hypercholesterolemia (0.424); colonic neoplasm (0.338); Thrombocytopenia (0.332); Alzheimer disease (0.331)
- **Europe PMC papers**: 4197
- **Why important**: FADS1 has the strongest network position in the supplied module and links otherwise distinct parts of the graph, including the lipid enzymes, MCM-associated genes and RNA or cytoskeletal regulators. Its annotated function is fatty-acid desaturation and unsaturated-fatty-acid biosynthesis, and STRING supports a strong relationship with SCD. It is detected in both tissues, has low tissue specificity, and has a large literature record with disease links including neurodegenerative disease, hypercholesterolemia, colonic neoplasm and thrombocytopenia.
- **Conclusion**: Established evidence supports FADS1 as a central lipid-metabolism component and a network bridge. It may help connect membrane-lipid state with proliferation or cellular stress, but that cross-process role is a hypothesis rather than a demonstrated function of this module.

#### SCD

- **Related proteins** (co-abundance neighbors): PUM1 (0.82); STRING partners: FADS1 (0.959), FASN (0.96)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_06791.1, huMAP3_09592.1, huMAP3_08167.1
- **Function (MyGene.info)**: stearoyl-CoA desaturase. This gene encodes an enzyme involved in fatty acid biosynthesis, primarily the synthesis of oleic acid. The protein belongs to the fatty acid desaturase family and is an integral membrane protein located in the endoplasmic reticulum. Transcripts of approximately 3.9 and 5.2 kb, differing only by alternative polyadenlyation signals, have been detected. A gene encoding a similar enzyme is located on…
- **Diseases (Open Targets)**: Alzheimer disease (0.483); Parkinson disease (0.476); neurodegenerative disease (0.463); lysosomal storage disease (0.462); cataract (0.397)
- **Europe PMC papers**: 36923
- **Why important**: SCD is an endoplasmic-reticulum fatty-acid desaturase with a direct STRING relationship to FADS1 and FASN, and it is represented in hu.MAP complexes (hu.MAP huMAP3_06791.1), (hu.MAP huMAP3_09592.1) and (hu.MAP huMAP3_08167.1). It is tissue enhanced in adipose tissue, brain and liver, yet detected in both tissues represented here. Its very large literature record and disease associations including neurodegenerative disease and lysosomal storage disease make it a strong biological anchor for the lipid component.
- **Conclusion**: Established evidence supports SCD as a genuine lipid-biosynthetic element of the module. Its co-abundance may indicate membrane remodeling or metabolic demand, but the data do not establish whether lipid metabolism drives the other module components or merely covaries with them.

#### MCM2

- **Related proteins** (co-abundance neighbors): MCM7 (0.87), FADS1 (0.80); STRING partners: KIF11 (0.848), MCM4 (0.999), MCM7 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_06061.1, huMAP3_05529.1, huMAP3_07113.1, huMAP3_14758.1, huMAP3_08554.1, huMAP3_11832.1, huMAP3_12180.1, huMAP3_09860.1, huMAP3_00154.1, huMAP3_09466.1, huMAP3_10862.1, huMAP3_14306.1
- **Function (MyGene.info)**: minichromosome maintenance complex component 2. The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication relat…
- **Diseases (Open Targets)**: autosomal dominant nonsyndromic hearing loss 70 (0.483); autosomal dominant nonsyndromic hearing loss (0.373); Abnormality of the gastrointestinal tract (0.211); alcohol drinking (0.198); urolithiasis (0.198)
- **Europe PMC papers**: 8146
- **Why important**: MCM2 is part of the densely supported MCM2–MCM4–MCM7 subnetwork and appears across many hu.MAP complexes, including (hu.MAP huMAP3_06061.1), (hu.MAP huMAP3_05529.1), (hu.MAP huMAP3_07113.1), (hu.MAP huMAP3_14758.1), (hu.MAP huMAP3_08554.1), (hu.MAP huMAP3_11832.1), (hu.MAP huMAP3_12180.1), (hu.MAP huMAP3_09860.1), (hu.MAP huMAP3_00154.1), (hu.MAP huMAP3_09466.1), (hu.MAP huMAP3_10862.1) and (hu.MAP huMAP3_14306.1). Its established role is initiation of eukaryotic DNA replication and replication-fork biology. HPA indicates enhancement in bone marrow and lymphoid tissue and in several progenitor populations, while the literature record is especially extensive and includes hearing-loss and developmental disease associations.
- **Conclusion**: Established evidence identifies MCM2 as a core replication component and a strong marker of a cycling or replication-competent cell state. Its presence does not prove that all samples contain actively dividing cells, because co-abundance can also reflect cell composition.

#### CSE1L

- **Related proteins** (co-abundance neighbors): NUP155 (0.87), ATIC (0.82), FASN (0.80); STRING partners: XPO5 (0.766)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_06791.1, huMAP3_09592.1, huMAP3_09042.1
- **Function (MyGene.info)**: chromosome segregation 1 like. Proteins that carry a nuclear localization signal (NLS) are transported into the nucleus by the importin-alpha/beta heterodimer. Importin-alpha binds the NLS, while importin-beta mediates translocation through the nuclear pore complex. After translocation, RanGTP binds importin-beta and displaces importin-alpha. Importin-alpha must then be returned to the cytoplasm, leaving the NLS protein behind.…
- **Diseases (Open Targets)**: intelligence (0.293); neurodegenerative disease (0.269); Alzheimer disease (0.199); celiac disease (0.187); autism spectrum disorder (0.178)
- **Europe PMC papers**: 860
- **Why important**: CSE1L connects multiple module neighborhoods through NUP155, ATIC and FASN, and it has STRING support with XPO5. It is represented in hu.MAP complexes (hu.MAP huMAP3_06791.1), (hu.MAP huMAP3_09592.1) and (hu.MAP huMAP3_09042.1). Its established function in nuclear export and recycling of importin-alpha provides a plausible link between nucleocytoplasmic transport, RNA handling and cellular biosynthetic activity. It is detected in both tissues and has disease associations spanning neurodegenerative disease, Alzheimer disease, celiac disease and autism-spectrum disorder.
- **Conclusion**: Established evidence supports CSE1L as a transport-related connector rather than a pathway-specific marker. Its bridging position makes it useful for interpreting the module's integration of nuclear transport with metabolism, but the inferred integration remains provisional.

#### PUM1

- **Related proteins** (co-abundance neighbors): FADS1 (0.85), ABCB7 (0.84), PRRC2A (0.82), SCD (0.82), WDR44 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_06975.1
- **Function (MyGene.info)**: pumilio RNA binding family member 1. This gene encodes a member of the PUF family, evolutionarily conserved RNA-binding proteins related to the Pumilio proteins of Drosophila and the fem-3 mRNA binding factor proteins of C. elegans. The encoded protein contains a sequence-specific RNA binding domain comprised of eight repeats and N- and C-terminal flanking regions, and serves as a translational regulator of specific mRNAs by binding …
- **Diseases (Open Targets)**: spinocerebellar ataxia 47 (0.751); neurodevelopmental disorder with motor abnormalities, seizures, and facial dysmorphism (0.676); hereditary disease (0.504); neurodegenerative disease (0.487); hypertensive disorder (0.290)
- **Europe PMC papers**: 2316
- **Why important**: PUM1 links FADS1 and SCD to ABCB7, PRRC2A and WDR44 in the co-abundance graph and is paired with MOV10 in hu.MAP complex (hu.MAP huMAP3_06975.1). Its annotated function as a sequence-specific RNA-binding translational regulator, including regulation of mRNA stability and post-transcriptional gene expression, provides a plausible regulatory layer connecting the metabolic and proliferative signals. It is broadly expressed, detected in both tissues, and has substantial literature and disease associations including spinocerebellar ataxia and neurodevelopmental disease.
- **Conclusion**: Established evidence supports PUM1 as an RNA-regulatory component that could modulate the abundance of transcripts represented in the module. It is reasonable to hypothesize that PUM1 contributes to coordination of the module, but the co-abundance data do not show direct regulation of the other module genes.

## Module 5

**Tissue pair**: cervix_uterine and skin  
**Genes (38)**: ABLIM1, ADIRF, AFDN, ALDH2, ANXA4, CAPN1, CGN, CNOT12, CORO1B, CORO1C, CTNND1, DSP, ERO1A, FABP5, FAR1, FN1, AGL, GFPT1, GIT1, GTPBP4, HSPA2, HK1, LAS1L, LTA4H, MYLK, PGM2, LCP1, ALPL, PRPF31, PRPF4, RAB18, RELCH, RPL3, RRBP1, SEPTIN2, VASP, WASF2, XPO4

### Function

The most coherent interpretation is a shared epithelial structural and interface module, centered on cell junctions, cortical actin organization, adhesion, and tissue-barrier architecture. CGN, AFDN, CTNND1, and DSP connect the module to tight-junction, adherens-junction, and desmosomal biology, while CORO1B, CORO1C, VASP, WASF2, ABLIM1, and MYLK support actin remodeling, lamellipodium formation, and cell-shape regulation. FABP5 and several esophageal- and keratinocyte-associated signals are consistent with epithelial differentiation and surface-barrier biology. The module also contains metabolic, secretory-pathway, RNA-processing, and ribosome-associated genes, so it is not a functionally pure junctional complex. No GO or KEGG term passed global correction; therefore those annotations provide biological context but not globally significant enrichment. The lamellipodium result is supplementary STRING evidence only (STRING Component Lamellipodium; within-query FDR = 0.0401).

**Cell composition.** This is not predominantly a plasma-protein or secreted-protein module: the HPA summary identifies only a small secreted subset, and most genes are intracellular, membrane-associated, or junctional. The composition is strongly compatible with epithelial and surface-lining cell states. Esophageal apical and suprabasal cells are recurrently represented, and genes such as DSP, FABP5, CGN, and WASF2 support epithelial-barrier interpretation. There is also a mixed-cell signal involving neutrophils, platelets, monocytes, dendritic cells, megakaryocytes, and trophoblast-related cell types. Thus the shared cervix and skin pattern may reflect conserved epithelial architecture, but partial contribution from common vascular, platelet, or immune-associated cell populations cannot be excluded. The broad HPA tissue distribution of many genes and the presence of housekeeping-like translation, splicing, metabolism, and protein-folding genes argue against treating the module as a narrowly tissue-specific pathway. Protein detection is generally strong in both tissues, although several individual genes are detected preferentially in one tissue or not detected in either tissue.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING provides a coherent set of already known relationships rather than a single complete interaction network. High-confidence links connect AFDN with CGN and CTNND1, CORO1B with CORO1C, CTNND1 with DSP, VASP with WASF2, carbohydrate-metabolism genes such as HK1, GFPT1, PGM2, and AGL, and spliceosome-related genes PRPF4 and PRPF31. The supplementary lamellipodium component (STRING Component Lamellipodium; within-query FDR = 0.0401) independently supports an actin-remodeling interpretation, but it is not globally corrected enrichment. hu.MAP shows repeated CORO1B-CORO1C co-membership across several actin-associated complexes (hu.MAP huMAP3_04826.1) through (hu.MAP huMAP3_10673.1), junction or cytoskeletal co-membership involving ABLIM1, AFDN, and CGN (hu.MAP huMAP3_05977.1) and (hu.MAP huMAP3_08205.1) through (hu.MAP huMAP3_09542.1), epithelial structural co-membership involving DSP and FABP5 (hu.MAP huMAP3_09929.1), and spliceosomal co-membership involving PRPF4 and PRPF31 (hu.MAP huMAP3_06511.1) through (hu.MAP huMAP3_08980.1). These observations indicate that several local relationships are established and that the module combines multiple connected cellular subsystems. They support biological coherence, but the partial membership of the hu.MAP complexes does not establish that the entire module is one physical complex.

**STRING interactions (score >= 0.7)**: 13 of 703 gene pairs: AFDN–CGN (0.978); AFDN–CTNND1 (0.998); AGL–PGM2 (0.929); CORO1B–CORO1C (0.917); CTNND1–DSP (0.808); FN1–RRBP1 (0.766); GFPT1–HK1 (0.936); GFPT1–PGM2 (0.716); GTPBP4–RPL3 (0.986); HK1–PGM2 (0.945); LAS1L–PRPF31 (0.902); PRPF31–PRPF4 (0.999); VASP–WASF2 (0.792)
**STRING functional enrichment (supplementary, within-query FDR)**: Component Lamellipodium (FDR = 0.0401, 8 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_05977.1 (ABLIM1, AFDN, CGN; 3/12); huMAP3_04826.1 (CORO1B, CORO1C; 2/4); huMAP3_07776.1 (CORO1B, CORO1C; 2/7); huMAP3_05614.1 (CORO1B, CORO1C; 2/8); huMAP3_09579.1 (CORO1B, CORO1C; 2/9); huMAP3_11076.1 (CORO1B, CORO1C; 2/10); huMAP3_10784.1 (CORO1B, CORO1C; 2/13); huMAP3_10673.1 (MYLK, CORO1B; 2/14); huMAP3_08205.1 (ABLIM1, CGN; 2/17); huMAP3_09542.1 (ABLIM1, CGN; 2/38); huMAP3_09929.1 (DSP, FABP5; 2/75); huMAP3_06511.1 (PRPF4, PRPF31; 2/79); huMAP3_08980.1 (PRPF4, PRPF31; 2/97)

### Novelty

The module should not be described as a wholly new molecular complex or as a newly discovered pathway. Several of its strongest relationships and subnetworks are already represented in STRING and hu.MAP, especially epithelial junction, coronin-actin, spliceosomal, and metabolic connections. At the same time, the conserved co-abundance of this particular combination across cervix and skin, including junctional, cortical-actin, epithelial lipid-handling, metabolic, and intracellular processing genes, may represent a new tissue-pair-level organization or a useful composite signature. Absence of some genes from STRING or hu.MAP is not evidence of novelty, and the lack of globally significant GO/KEGG enrichment limits claims of pathway discovery. The defensible conclusion is contextual novelty of the cross-tissue co-abundance pattern, not novelty of the individual molecular functions.

**Hypothesis.** Hypothesis: the module reflects a conserved epithelial-interface state shared by cervix and skin in which cell-cell junctions and desmosomes are coordinated with cortical actin remodeling, epithelial lipid handling, and biosynthetic capacity. In this model, CGN, AFDN, CTNND1, and DSP maintain junctional connectivity; CORO1B, CORO1C, VASP, WASF2, ABLIM1, and MYLK tune actin architecture and cell movement; FABP5 supports epithelial lipid handling; and ALPL may mark a broader tissue or cell-state component that links several otherwise distinct subnetworks. The metabolic, ER, ribosome, and splicing genes could reflect the biosynthetic demands of a differentiated epithelial population rather than direct physical interaction with the junctional proteins. A competing explanation is compositional: shared epithelial cells, with variable platelet or immune admixture, generate the observed co-abundance pattern. Testing this hypothesis would require cell-type-resolved data, matched tissue histology, and perturbation or localization experiments rather than enrichment alone.

### Important genes

#### ALPL

- **Related proteins** (co-abundance neighbors): CTNND1 (0.92), FABP5 (0.92), CNOT12 (0.91), RRBP1 (0.89), GFPT1 (0.86), ALDH2 (0.86), ERO1A (0.86), RPL3 (0.85), CORO1C (0.85), PGM2 (0.84), RAB18 (0.84), ANXA4 (0.84), CORO1B (0.83), VASP (0.83), SEPTIN2 (0.83), HK1 (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Group enriched; blood Immune cell enriched; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alkaline phosphatase, biomineralization associated. This gene encodes a member of the alkaline phosphatase family of proteins. There are at least four distinct but related alkaline phosphatases: intestinal, placental, placental-like, and liver/bone/kidney (tissue non-specific). The first three are located together on chromosome 2, while the tissue non-specific form is located on chromosome 1. The product of this gene is a membrane bound glycosylate…
- **Diseases (Open Targets)**: hypophosphatasia (0.873); infantile hypophosphatasia (0.828); adult hypophosphatasia (0.773); childhood hypophosphatasia (0.759); odontohypophosphatasia (0.671)
- **Europe PMC papers**: 8096
- **Why important**: ALPL is the strongest network hub in the supplied subgraph and connects junctional, metabolic, ER, and ribosome-associated signals. It is detected in both tissues and has HPA associations with neutrophils and alveolar cells, while its annotation supports membrane-associated enzyme activity and responses linked to tissue remodeling and lipopolysaccharide. Its extensive disease and literature record makes it a useful anchor for distinguishing a broad cell-state signal from a narrowly epithelial mechanism.
- **Conclusion**: Established evidence supports ALPL as a central co-abundance organizer and a marker of a broad tissue or cell-state program, but not as proof that alkaline-phosphatase activity drives the whole module. Its direct mechanistic role in the shared cervix-skin module remains a hypothesis.

#### CGN

- **Related proteins** (co-abundance neighbors): AFDN (0.92), FN1 (0.90), WASF2 (0.85), CAPN1 (0.85), CTNND1 (0.83), LTA4H (0.82), VASP (0.81); STRING partners: AFDN (0.978)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Plasma membrane, Cell Junctions; IHC detected in cervix_uterine
- **hu.MAP 3.0**: huMAP3_05977.1, huMAP3_08205.1, huMAP3_09542.1
- **Function (MyGene.info)**: cingulin. Enables cadherin binding activity. Predicted to act upstream of or within bicellular tight junction assembly; epithelial cell morphogenesis; and microtubule cytoskeleton organization. Located in bicellular tight junction and plasma membrane. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Abnormality of the skeletal system (0.359); nonsyndromic deafness (0.118); skin disorder (0.094); colorectal carcinoma (0.086); ovarian carcinoma (0.065)
- **Europe PMC papers**: 3593
- **Why important**: CGN is a central junction-associated connector with links to AFDN, CTNND1, FN1, WASF2, CAPN1, LTA4H, and VASP. HPA places it at the plasma membrane and cell junctions and associates it with epithelial cell types. Its established cingulin functions in cadherin binding, tight-junction assembly, epithelial morphogenesis, and microtubule organization directly match the module interpretation. Its relationship with AFDN is supported by STRING and its membership with AFDN and ABLIM1 is supported by hu.MAP (hu.MAP huMAP3_05977.1).
- **Conclusion**: Established evidence identifies CGN as a plausible structural organizer of the epithelial junctional component. The specific claim that it coordinates the entire cross-tissue module is not established and should be tested experimentally.

#### DSP

- **Related proteins** (co-abundance neighbors): AGL (0.88), LAS1L (0.83), RELCH (0.82), GIT1 (0.82), LCP1 (0.82), PRPF31 (0.81), GTPBP4 (0.81); STRING partners: CTNND1 (0.808)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Cell Junctions; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_09929.1
- **Function (MyGene.info)**: desmoplakin. This gene encodes a protein that anchors intermediate filaments to desmosomal plaques and forms an obligate component of functional desmosomes. Mutations in this gene are the cause of several cardiomyopathies and keratodermas, including skin fragility-woolly hair syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016].
- **Diseases (Open Targets)**: arrhythmogenic cardiomyopathy with wooly hair and keratoderma (0.841); arrhythmogenic right ventricular dysplasia 8 (0.812); arrhythmogenic right ventricular cardiomyopathy (0.760); lethal acantholytic epidermolysis bullosa (0.745); cardiomyopathy, dilated, with wooly hair, keratoderma, and tooth agenesis (0.741)
- **Europe PMC papers**: 17350
- **Why important**: DSP is a prominent junction-associated node linked to metabolic, cytoskeletal, trafficking, and RNA-processing signals in the subgraph. HPA strongly associates it with skin and epithelial cell types, and its annotation identifies desmoplakin as an obligate desmosomal component anchoring intermediate filaments. Its disease associations with cardiomyopathy, keratoderma, and skin fragility provide strong evidence that altered DSP function can affect epithelial and mechanical integrity. Its relationship with CTNND1 is supported by STRING, and its epithelial complex context with FABP5 is represented in hu.MAP (hu.MAP huMAP3_09929.1).
- **Conclusion**: Established evidence supports DSP as a biologically important epithelial-barrier component and a strong explanation for the skin-related aspect of the module. Its involvement in the cervix-skin co-abundance pattern is supported by the network and HPA data, but a direct causal role in shared regulation remains hypothetical.

#### CTNND1

- **Related proteins** (co-abundance neighbors): ALPL (0.92), CGN (0.83), GIT1 (0.80); STRING partners: AFDN (0.998), DSP (0.808)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Plasma membrane; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: catenin delta 1. This gene encodes a member of the Armadillo protein family, which function in adhesion between cells and signal transduction. Multiple translation initiation codons and alternative splicing result in many different isoforms being translated. Not all of the full-length natures of the described transcript variants have been determined. Read-through transcription also exists between this gene and the…
- **Diseases (Open Targets)**: blepharocheilodontic syndrome (0.724); listeriosis (0.526); cleft lip (0.510); hereditary disease (0.415); exudative vitreoretinopathy (0.376)
- **Europe PMC papers**: 3021
- **Why important**: CTNND1 links ALPL, CGN, and GIT1 and is detected in both tissues. It encodes a catenin involved in cadherin-mediated adhesion, cell-cell adhesion, signaling, and cell migration. Its STRING relationships with AFDN and DSP connect adherens-junction and desmosomal systems, while the supplementary lamellipodium annotation (STRING Component Lamellipodium; within-query FDR = 0.0401) places it within a broader adhesion and motility context. Disease associations involving developmental and epithelial abnormalities further support its importance.
- **Conclusion**: Established evidence supports CTNND1 as an integrative adhesion and signaling node connecting multiple junctional structures. Its role as a regulatory bridge within this module is a reasonable hypothesis, but co-abundance does not establish molecular directionality.

#### CORO1B

- **Related proteins** (co-abundance neighbors): ALPL (0.83); STRING partners: CORO1C (0.917)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_04826.1, huMAP3_07776.1, huMAP3_05614.1, huMAP3_09579.1, huMAP3_11076.1, huMAP3_10784.1, huMAP3_10673.1
- **Function (MyGene.info)**: coronin 1B. Members of the coronin family, such as CORO1B, are WD repeat-containing actin-binding proteins that regulate cell motility (Cai et al., 2005 [PubMed 16027158]).[supplied by OMIM, Mar 2008].
- **Diseases (Open Targets)**: Abnormality of refraction (0.067); refractive error (0.049); alcohol drinking (0.027); asthma (0.025); diabetes mellitus (0.025)
- **Europe PMC papers**: 339
- **Why important**: CORO1B is part of a repeated hu.MAP actin-associated pattern with CORO1C (hu.MAP huMAP3_04826.1) through (hu.MAP huMAP3_10673.1) and is included in the supplementary lamellipodium signal (STRING Component Lamellipodium; within-query FDR = 0.0401). Its annotation supports actin filament organization, cell migration, ruffle organization, and regulation of Arp2/3-mediated actin nucleation. HPA links it to epithelial and monocyte-associated cell types, making it relevant both to epithelial remodeling and to possible cellular admixture. Its close STRING relationship with CORO1C provides direct support for this local subnetwork.
- **Conclusion**: Established evidence supports CORO1B as a meaningful actin-remodeling component and as evidence that the module includes a cortical motility program. Whether this reflects epithelial plasticity, immune-cell contribution, or both is unresolved.

#### FABP5

- **Related proteins** (co-abundance neighbors): ALPL (0.92); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_09929.1
- **Function (MyGene.info)**: fatty acid binding protein 5. This gene encodes the fatty acid binding protein found in epidermal cells, and was first identified as being upregulated in psoriasis tissue. Fatty acid binding proteins are a family of small, highly conserved, cytoplasmic proteins that bind long-chain fatty acids and other hydrophobic ligands. FABPs may play roles in fatty acid uptake, transport, and metabolism. Polymorphisms in this gene are ass…
- **Diseases (Open Targets)**: phlebitis (0.289); Thrombophlebitis (0.289); nephrotic syndrome (0.215); response to xenobiotic stimulus (0.170); preeclampsia (0.158)
- **Europe PMC papers**: 6055
- **Why important**: FABP5 has a direct connection to the major ALPL-centered portion of the network and is strongly associated by HPA with cervix, esophagus, and epithelial suprabasal or keratinocyte-like cells. Its established function in binding and transporting long-chain fatty acids, epidermis development, and lipid metabolism provides a metabolic complement to the junctional and cytoskeletal interpretation. Its presence in the epithelial structural hu.MAP context with DSP (hu.MAP huMAP3_09929.1) makes it especially informative for interpreting the module as a differentiated surface-barrier state rather than as a generic actin signature.
- **Conclusion**: Established evidence supports FABP5 as an epithelial lipid-handling marker that strengthens the surface-barrier interpretation. Its participation in coordinating lipid metabolism with junctional integrity is a hypothesis rather than a demonstrated mechanism in this module.

## Module 6

**Tissue pair**: cervix_uterine and skin  
**Genes (18)**: ACLY, MTHFD1, DPP9, HSPH1, EIF4G1, IMPDH2, NUP93, PSMC2, PAICS, PURA, SNUPN, AARS1, SYNE2, CCT5, CCT3, CCT7, CCT8, XPO1

### Function

This is primarily an intracellular proteostasis and nuclear RNA-organization module. The strongest signal is the CCT chaperonin core formed by CCT3, CCT5, CCT7 and CCT8, which supports globally corrected terms for the chaperonin-containing T-complex, ATP-dependent protein folding, protein localization to the nucleus and Cajal body, telomerase-RNA localization, and telomere maintenance (13 globally significant GO/KEGG terms, q_global 9.42e-05–0.000414; see the table), (GO:BP positive regulation of telomere maintenance via telomerase; q_global = 0.0015), (5 globally significant GO/KEGG terms, q_global 0.0024–0.00401; see the table), (10 globally significant GO/KEGG terms, q_global 0.00414–0.0488; see the table). NUP93, SNUPN and XPO1 support the nuclear-transport and RNA-localization interpretation (GO:BP RNA localization; q_global = 0.0024), (GO:BP protein localization to nucleus; q_global = 0.00401). HSPH1 adds stress-buffering and protein-folding support (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000414), (GO:MF protein folding chaperone; q_global = 0.00332). PAICS, IMPDH2 and MTHFD1 indicate connections to purine and folate metabolism, while ACLY links the module to cytosolic acetyl-CoA production. The sperm-recognition and cell-recognition terms (GO:BP binding of sperm to zona pellucida; q_global = 0.000795), (GO:BP sperm-egg recognition; q_global = 0.0015), (GO:BP cell-cell recognition; q_global = 0.00414), (GO:BP cell recognition; q_global = 0.0266), (GO:BP single fertilization; q_global = 0.0405) should be interpreted cautiously because they are driven by the same CCT quartet and do not establish a reproductive-specific function. Overall, the module is best interpreted as coordinated folding, nuclear trafficking and biosynthetic support.

**Cell composition.** The module contains no secreted genes according to HPA, so it is not a plasma or secreted-protein module. It is also not strongly blood-cell enriched: most genes have low immune-cell specificity, with only SYNE2 classified as immune-cell enhanced. Most genes have low tissue specificity, and protein detection is broadly compatible with both cervix_uterine and skin. Cell-type enhancements are mixed, including germ-cell populations, epithelial and progenitor populations, muscle, liver, pancreatic and other cell types. This pattern is consistent with broadly expressed intracellular or housekeeping-type proteins. A shared cell-type contribution or sample-composition effect remains possible, but the HPA evidence does not specifically support blood contamination.

**GO/KEGG enrichment**: 32 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC chaperonin-containing T-complex | 9.42e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nuclear body | 9.42e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to Cajal body | 9.42e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of protein localization to Cajal body | 9.42e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of protein localization to Cajal body | 9.42e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP regulation of telomerase RNA localization to Cajal body | 9.42e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomerase RNA localization to Cajal body | 9.42e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP protein localization to nucleoplasm | 9.42e-05 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to Cajal body | 0.000329 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization to Cajal body | 0.000329 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP telomerase RNA localization | 0.000329 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP RNA localization to nucleus | 0.000329 | CCT3, CCT5, CCT7, CCT8 |
| GO:MF ATP-dependent protein folding chaperone | 0.000414 | CCT3, CCT5, CCT7, CCT8, HSPH1 |
| GO:BP binding of sperm to zona pellucida | 0.000795 | CCT3, CCT5, CCT7, CCT8 |
| GO:BP positive regulation of telomere maintenance via telomerase | 0.0015 | CCT3, CCT5, CCT7, CCT8 |

### STRING and hu.MAP

STRING supports the CCT core: CCT3, CCT5, CCT7 and CCT8 have very strong known pairwise relationships and are enriched for CCT, ATP-dependent folding and actin-folding annotations (14 supplementary STRING terms; within-query FDR 0.00019–0.0019). Known supplementary relationships also include CCT7 with IMPDH2, CCT8 with PSMC2, NUP93 with XPO1, SNUPN with XPO1, ACLY with MTHFD1, MTHFD1 with PAICS and IMPDH2 with PAICS. hu.MAP independently places CCT3, CCT5, CCT7 and CCT8 together in several complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1), and places NUP93 with XPO1 in a nuclear-transport complex (hu.MAP huMAP3_09042.1). Therefore, the central physical relationships are established rather than newly discovered. The co-abundance module may instead reflect coordinated regulation of these known complexes with metabolic, translation, stress and proteostasis partners.

**STRING interactions (score >= 0.7)**: 13 of 153 gene pairs: ACLY–MTHFD1 (0.723); CCT3–CCT5 (0.999); CCT3–CCT7 (0.999); CCT3–CCT8 (0.999); CCT5–CCT7 (0.999); CCT5–CCT8 (0.999); CCT7–CCT8 (0.999); CCT7–IMPDH2 (0.758); CCT8–PSMC2 (0.733); IMPDH2–PAICS (0.744); MTHFD1–PAICS (0.9); NUP93–XPO1 (0.712); SNUPN–XPO1 (0.999)
**STRING functional enrichment (supplementary, within-query FDR)**: TISSUES Lymphoblast (FDR = 2.62e-05, 9 genes); Pfam TCP-1/cpn60 chaperonin family (FDR = 0.00019, 4 genes); Function ATP-dependent protein folding chaperone (FDR = 0.00031, 5 genes); Component Chaperonin-containing T-complex (FDR = 0.00066, 4 genes); COMPARTMENTS Chaperonin-containing T-complex (FDR = 0.00069, 4 genes); InterPro Chaperonin TCP-1, conserved site (FDR = 0.00092, 4 genes); InterPro Chaperonin Cpn60/GroEL/TCP-1 family (FDR = 0.00092, 4 genes); InterPro Chaperone tailless complex polypeptide 1 (TCP-1) (FDR = 0.00092, 4 genes); InterPro GroEL-like apical domain superfamily (FDR = 0.00092, 4 genes); InterPro TCP-1-like chaperonin intermediate domain superfamily (FDR = 0.00092, 4 genes); InterPro GroEL-like equatorial domain superfamily (FDR = 0.00092, 4 genes); RCTM Folding of actin by CCT/TriC (FDR = 0.0019, 4 genes); RCTM Association of TriC/CCT with target proteins during biosynthesis (FDR = 0.0019, 4 genes); RCTM Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding (FDR = 0.0019, 4 genes); NetworkNeighborAL Chaperonin TCP-1, conserved site, and Cellular proteostasis (FDR = 0.0019, 4 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_07938.1 (CCT5, CCT3, CCT8, CCT7; 4/23); huMAP3_06559.1 (CCT5, CCT3, CCT8, CCT7; 4/25); huMAP3_09191.1 (CCT5, CCT3, CCT8, CCT7; 4/32); huMAP3_10656.1 (CCT5, CCT3, CCT8, CCT7; 4/36); huMAP3_14584.1 (CCT5, CCT3, CCT8, CCT7; 4/61); huMAP3_01951.1 (CCT5, CCT3, CCT7; 3/8); huMAP3_09042.1 (XPO1, NUP93; 2/26)

### Novelty

This should not be described as a newly discovered molecular complex. The central CCT quartet and the main nuclear-transport relationships are already represented in STRING and hu.MAP, while the CCT functions are supported by extensive prior annotation and literature. The potentially novel observation is their coordinated co-abundance across cervix_uterine and skin, together with peripheral metabolic and proteostasis genes. That cross-tissue pattern is hypothesis-generating and does not prove a new biochemical interaction, tissue-specific pathway or disease mechanism. Lack of STRING or hu.MAP support for some peripheral genes cannot by itself establish novelty.

**Hypothesis.** Hypothesis: a shared intracellular proteostasis state in cervix_uterine and skin coordinates CCT-mediated folding with nuclear import, RNA trafficking and biosynthetic capacity. The CCT core may maintain folding-competent cytoskeletal and regulatory proteins, while HSPH1 buffers unfolded proteins. NUP93, SNUPN and XPO1 may couple this state to nuclear and RNA transport. ACLY, MTHFD1, PAICS and IMPDH2 may reflect the acetyl-CoA, folate and purine resources needed for macromolecule production and cellular maintenance. This is a mechanistic hypothesis inferred from co-abundance and annotation, not an established causal pathway.

### Important genes

#### CCT5

- **Related proteins** (co-abundance neighbors): CCT7 (0.87), AARS1 (0.85), CCT3 (0.84), HSPH1 (0.83), PAICS (0.82); STRING partners: CCT3 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mid piece; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 5. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: hereditary sensory and autonomic neuropathy with spastic paraplegia (0.525); neurodegenerative disease (0.450); esophageal ulcer (0.268); alcohol drinking (0.264); eye injury (0.254)
- **Europe PMC papers**: 1252
- **Why important**: CCT5 has the strongest network position and connects the CCT core to AARS1, HSPH1 and PAICS. It is a member of the ATP-dependent CCT folding machine and contributes to every globally corrected CCT, protein-folding, Cajal-body and telomere-related term (32 globally significant GO/KEGG terms, q_global 9.42e-05–0.0488; see the table). It is present in multiple hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1) and has strong STRING support (14 supplementary STRING terms; within-query FDR 0.00019–0.0019). Its established disease associations include hereditary sensory and autonomic neuropathy and neurodegenerative disease, and it has substantial literature support.
- **Conclusion**: Established evidence identifies CCT5 as a central TRiC/CCT folding subunit and a principal marker of this module. Its network position makes it a plausible coordinator of the module signal, but the data do not show that CCT5 causes the cross-tissue co-abundance pattern or directly controls telomere biology in these tissues.

#### CCT3

- **Related proteins** (co-abundance neighbors): IMPDH2 (0.92), CCT8 (0.85), CCT5 (0.84), PURA (0.80); STRING partners: CCT5 (0.999), CCT7 (0.999), CCT8 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_07938.1, huMAP3_06559.1, huMAP3_09191.1, huMAP3_10656.1, huMAP3_14584.1, huMAP3_01951.1
- **Function (MyGene.info)**: chaperonin containing TCP1 subunit 3. The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various prote…
- **Diseases (Open Targets)**: neurodevelopmental disorder with speech or visual impairment and brain hypomyelination (0.624); neurodegenerative disease (0.472); osteoarthritis (0.310); autoimmune disorder of central nervous system (0.249); atrial fibrillation (0.183)
- **Europe PMC papers**: 1301
- **Why important**: CCT3 is a highly connected CCT-core member linked to IMPDH2, CCT8, CCT5 and PURA. It contributes to all globally corrected terms driven by the CCT quartet (32 globally significant GO/KEGG terms, q_global 9.42e-05–0.0488; see the table), is supported by STRING (14 supplementary STRING terms; within-query FDR 0.00019–0.0019), and appears in multiple hu.MAP CCT complexes (hu.MAP huMAP3_07938.1) (hu.MAP huMAP3_06559.1) (hu.MAP huMAP3_09191.1) (hu.MAP huMAP3_10656.1) (hu.MAP huMAP3_14584.1) (hu.MAP huMAP3_01951.1). Its established folding function, disease associations involving neurodevelopmental and neurodegenerative conditions, and substantial literature make it important for the module’s central interpretation.
- **Conclusion**: Established evidence supports CCT3 as a core protein-folding component with annotations related to nuclear localization and telomere maintenance. Coordinated coupling to nucleotide metabolism and DNA or RNA processes is a module-level hypothesis rather than a demonstrated CCT3-specific mechanism.

#### HSPH1

- **Related proteins** (co-abundance neighbors): CCT5 (0.83), CCT7 (0.82), SNUPN (0.82), ACLY (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heat shock protein family H (Hsp110) member 1. This gene encodes a member of the heat shock protein 70 family of proteins. The encoded protein functions as a nucleotide exchange factor for the molecular chaperone heat shock cognate 71 kDa protein (Hsc70). In addition, this protein plays a distinct but related role as a holdase that inhibits the aggregation of misfolded proteins, including the cystic fibrosis transmembrane conductance regulator…
- **Diseases (Open Targets)**: Parkinson disease (0.205); Phenotypic abnormality (0.187); hypertensive disorder (0.131); neoplasm (0.104); major depressive disorder (0.096)
- **Europe PMC papers**: 2050
- **Why important**: HSPH1 is a highly connected stress and proteostasis bridge, linking CCT5 and CCT7 to SNUPN and ACLY. It contributes to the globally corrected ATP-dependent and protein-folding chaperone terms (GO:MF ATP-dependent protein folding chaperone; q_global = 0.000414), (GO:MF protein folding chaperone; q_global = 0.00332) and to the supplementary STRING folding and lymphoblast terms (STRING TISSUES Lymphoblast; within-query FDR = 2.62e-05), (STRING Function ATP-dependent protein folding chaperone; within-query FDR = 0.00031). Its known function as a nucleotide-exchange factor and holdase for misfolded proteins, disease associations including Parkinson disease and neoplasm, and substantial literature support its importance.
- **Conclusion**: Established evidence supports HSPH1 as a protein-quality-control component that complements the CCT core. Its position suggests that stress-buffering may be coordinated with nuclear transport and metabolism, but this proposed integration is not proven by the co-abundance data.

#### NUP93

- **Related proteins** (co-abundance neighbors): XPO1 (0.83), SNUPN (0.83), ACLY (0.82); STRING partners: XPO1 (0.712)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_09042.1
- **Function (MyGene.info)**: nucleoporin 93. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central…
- **Diseases (Open Targets)**: nephrotic syndrome, type 12 (0.687); familial idiopathic steroid-resistant nephrotic syndrome (0.595); Orthomyxoviridae infectious disease (0.544); HIV infectious disease (0.541); viral infectious disease (0.527)
- **Europe PMC papers**: 3932
- **Why important**: NUP93 links the module’s metabolic and structural side to XPO1, SNUPN and ACLY. It contributes to globally corrected RNA and protein nuclear-localization terms (GO:BP RNA localization; q_global = 0.0024), (GO:BP protein localization to nucleus; q_global = 0.00401), has STRING support with XPO1, and participates with XPO1 in a hu.MAP nuclear-transport complex (hu.MAP huMAP3_09042.1). Its established role as a nuclear-pore component and its disease associations with nephrotic syndrome and viral infectious disease make it an informative non-CCT anchor.
- **Conclusion**: Established evidence supports NUP93 as a nuclear-pore component that gives the module a credible transport and compartmentalization dimension. The hypothesis that it couples proteostasis to metabolic state in these tissues is plausible from the network but remains untested.

#### ACLY

- **Related proteins** (co-abundance neighbors): NUP93 (0.82), HSPH1 (0.82), MTHFD1 (0.82), SYNE2 (0.81); STRING partners: MTHFD1 (0.723)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: ATP citrate lyase. ATP citrate lyase is the primary enzyme responsible for the synthesis of cytosolic acetyl-CoA in many tissues. The enzyme is a tetramer (relative molecular weight approximately 440,000) of apparently identical subunits. It catalyzes the formation of acetyl-CoA and oxaloacetate from citrate and CoA with a concomitant hydrolysis of ATP to ADP and phosphate. The product, acetyl-CoA, serves several im…
- **Diseases (Open Targets)**: familial hypercholesterolemia (0.532); Hypercholesterolemia (0.532); atherosclerosis (0.470); inherited lipid metabolism disorder (0.467); cardiovascular disorder (0.449)
- **Europe PMC papers**: 7957
- **Why important**: ACLY is a network bridge connecting NUP93, HSPH1, MTHFD1 and SYNE2. It is the module’s clearest link to cytosolic acetyl-CoA generation and lipid and cholesterol biosynthesis, and it has a substantial literature base with disease associations involving hypercholesterolemia and atherosclerosis. Its protein is detected in cervix_uterine but not skin, which may be relevant when interpreting the shared module.
- **Conclusion**: Established evidence supports ACLY as a cytosolic acetyl-CoA-producing enzyme and a metabolic connector in the network. Its role as a driver of the shared cervix_uterine–skin module is not established, especially because its HPA detection differs between the two tissues.

## Module 7

**Tissue pair**: cervix_uterine and skin  
**Genes (21)**: ACSL3, AIFM1, ATP1A1, ATP2A2, ATXN10, CANX, CENPV, CKAP4, EMC1, SHMT2, GPD2, IMMT, MYO1E, NDUFA10, NDUFS1, NCSTN, DDOST, ALDH18A1, PRKDC, UQCRC1, TIMM50

### Function

The strongest interpretation is a conserved cellular membrane and mitochondrial organization module. The globally corrected GO evidence is dominated by mitochondrial membrane, mitochondrial envelope, and mitochondrial inner membrane terms (6 globally significant GO/KEGG terms, q_global 8.08e-05–0.00447; see the table), with additional support for membrane protein complexes (GO:CC membrane protein complex; q_global = 0.00538). The transporter terms (GO:MF active monoatomic ion transmembrane transporter activity; q_global = 0.00655), (GO:MF primary active transmembrane transporter activity; q_global = 0.0209), and (GO:MF monoatomic cation transmembrane transporter activity; q_global = 0.0496) point particularly to electrochemical and cation transport through ATP1A1, ATP2A2, and mitochondrial respiratory components. The module therefore combines mitochondrial respiration and inner-membrane organization with endoplasmic-reticulum membrane function, calcium handling, membrane-protein folding, and selected metabolic processes. The membrane term (GO:CC membrane; q_global = 0.00869) is broad, but its complete module overlap is consistent with a general membrane-rich cellular program rather than a specific disease pathway. The STRING compartment results (15 supplementary STRING terms; within-query FDR 2.66e-06–0.0013) independently reinforce the mitochondrial and organelle-membrane interpretation, but remain supplementary evidence.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes, and protein detection is nearly complete in both cervix_uterine and skin. It is also not primarily a blood-cell module: most genes have low immune-cell specificity, although a minority show enrichment in neutrophil, monocyte, eosinophil, basophil, or related cell populations. Most genes have low tissue specificity, while the tissue-enhanced signals include muscle, tongue, parathyroid, salivary gland, and liver. The broad detection and mixture of mitochondrial, endoplasmic-reticulum, plasma-membrane, transport, and housekeeping-like functions make a shared cellular or metabolic state more plausible than a circulating blood or secreted-protein artifact. Cell-type-enhanced annotations are heterogeneous, so contribution from shared epithelial, metabolic, or other resident cell states cannot be excluded.

**GO/KEGG enrichment**: 11 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:CC mitochondrial membrane | 8.08e-05 | ACSL3, AIFM1, ALDH18A1, CANX, GPD2, IMMT, NDUFA10, NDUFS1, SHMT2, TIMM50, UQCRC1 |
| GO:CC organelle membrane | 0.000124 | ACSL3, AIFM1, ALDH18A1, ATP1A1, ATP2A2, CANX, CENPV, CKAP4, DDOST, EMC1, GPD2, IMMT, NCSTN, NDUFA10, NDUFS1, SHMT2, TIMM50, UQCRC1 |
| GO:CC mitochondrial envelope | 0.000241 | ACSL3, AIFM1, ALDH18A1, CANX, GPD2, IMMT, NDUFA10, NDUFS1, SHMT2, TIMM50, UQCRC1 |
| GO:CC mitochondrial inner membrane | 0.000376 | AIFM1, ALDH18A1, GPD2, IMMT, NDUFA10, NDUFS1, SHMT2, TIMM50, UQCRC1 |
| GO:CC organelle inner membrane | 0.000828 | AIFM1, ALDH18A1, GPD2, IMMT, NDUFA10, NDUFS1, SHMT2, TIMM50, UQCRC1 |
| GO:CC organelle envelope | 0.00447 | ACSL3, AIFM1, ALDH18A1, CANX, CENPV, GPD2, IMMT, NDUFA10, NDUFS1, SHMT2, TIMM50, UQCRC1 |
| GO:CC membrane protein complex | 0.00538 | ATP1A1, ATP2A2, DDOST, EMC1, IMMT, NCSTN, NDUFA10, NDUFS1, TIMM50, UQCRC1 |
| GO:MF active monoatomic ion transmembrane transporter activity | 0.00655 | ATP1A1, ATP2A2, NDUFA10, NDUFS1, UQCRC1 |
| GO:CC membrane | 0.00869 | ACSL3, AIFM1, ALDH18A1, ATP1A1, ATP2A2, ATXN10, CANX, CENPV, CKAP4, DDOST, EMC1, GPD2, IMMT, MYO1E, NCSTN, NDUFA10, NDUFS1, PRKDC, SHMT2, TIMM50, UQCRC1 |
| GO:MF primary active transmembrane transporter activity | 0.0209 | ATP1A1, ATP2A2, NDUFA10, NDUFS1, UQCRC1 |
| GO:MF monoatomic cation transmembrane transporter activity | 0.0496 | ATP1A1, ATP2A2, NDUFA10, NDUFS1, UQCRC1 |

### STRING and hu.MAP

STRING provides several coherent, high-confidence relationships. The respiratory core is supported by NDUFA10 with NDUFS1 and UQCRC1, and by IMMT with NDUFS1. The ER and membrane quality-control portion is supported by CANX with DDOST, EMC1, NCSTN, and ATP2A2, while ATP1A1 and ATP2A2 form a calcium and ion-transport pair. ALDH18A1 and SHMT2 provide a metabolic connection. These known relationships show that parts of the co-abundance module correspond to established molecular machinery rather than arbitrary gene pairing. hu.MAP independently places NDUFA10, NDUFS1, and UQCRC1 in respiratory complexes (hu.MAP huMAP3_14018.1), (hu.MAP huMAP3_09982.1), and related complexes (hu.MAP huMAP3_07653.1), (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). ATP1A1 and ATP2A2 occur together in (hu.MAP huMAP3_10473.1), and the ACSL3, ATP2A2, PRKDC, and ATXN10 grouping occurs in (hu.MAP huMAP3_09592.1). PRKDC and ATXN10 also co-occur in (hu.MAP huMAP3_09042.1). The complexes are partial overlaps, so they support modular organization but do not show that the entire co-abundance module is one physical complex.

**STRING interactions (score >= 0.7)**: 11 of 210 gene pairs: ALDH18A1–SHMT2 (0.804); ATP1A1–ATP2A2 (0.82); ATP2A2–CANX (0.849); CANX–DDOST (0.886); CANX–EMC1 (0.854); CANX–NCSTN (0.754); DDOST–EMC1 (0.818); IMMT–NDUFS1 (0.901); NDUFA10–NDUFS1 (0.999); NDUFA10–UQCRC1 (0.996); NDUFS1–UQCRC1 (0.998)
**STRING functional enrichment (supplementary, within-query FDR)**: COMPARTMENTS Organelle membrane (FDR = 2.66e-06, 17 genes); COMPARTMENTS Mitochondrial inner membrane (FDR = 1.25e-05, 9 genes); COMPARTMENTS Mitochondrial membrane (FDR = 1.25e-05, 10 genes); Component Organelle membrane (FDR = 1.63e-05, 18 genes); Component Mitochondrial inner membrane (FDR = 6.66e-05, 9 genes); Component Mitochondrial membrane (FDR = 6.66e-05, 10 genes); COMPARTMENTS Membrane (FDR = 0.0001, 18 genes); COMPARTMENTS Organelle envelope (FDR = 0.00014, 11 genes); Component Integral component of membrane (FDR = 0.00024, 13 genes); Component Membrane protein complex (FDR = 0.00035, 10 genes); Component Membrane (FDR = 0.00037, 21 genes); Keyword Mitochondrion inner membrane (FDR = 0.00071, 7 genes); Component Organelle envelope (FDR = 0.0012, 11 genes); COMPARTMENTS Membrane protein complex (FDR = 0.0013, 10 genes); Component Inner mitochondrial membrane protein complex (FDR = 0.0013, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_09592.1 (ACSL3, ATP2A2, PRKDC, ATXN10; 4/95); huMAP3_14018.1 (NDUFA10, NDUFS1, UQCRC1; 3/48); huMAP3_09982.1 (NDUFA10, NDUFS1, UQCRC1; 3/49); huMAP3_07653.1 (NDUFA10, NDUFS1; 2/7); huMAP3_10473.1 (ATP1A1, ATP2A2; 2/24); huMAP3_09042.1 (PRKDC, ATXN10; 2/26); huMAP3_02819.1 (NDUFA10, NDUFS1; 2/34); huMAP3_06397.1 (NDUFA10, NDUFS1; 2/49); huMAP3_09567.1 (NDUFA10, NDUFS1; 2/52); huMAP3_14878.1 (NDUFA10, NDUFS1; 2/53)

### Novelty

The individual biology is not a new discovery: mitochondrial respiratory-chain, inner-membrane, calcium-pump, ER-chaperone, glycosylation, and metabolic functions are established for several members. The module may nevertheless represent a new systems-level observation if its coordinated co-abundance and conservation across cervix_uterine and skin have not previously been reported. The strongest claim is therefore novelty of the tissue-pair co-abundance pattern and its integrated cross-organelle organization, not novelty of the genes or their functions. Known STRING edges and hu.MAP complexes make the pattern biologically credible, while the many genes without recorded STRING partners or hu.MAP membership indicate that existing databases do not fully explain the module. That database incompleteness alone cannot establish novelty. Independent replication, comparison with other tissue pairs, cell-composition adjustment, and perturbation or activity data would be needed for a firm novelty claim.

**Hypothesis.** Hypothesis: the shared module reflects a coordinated membrane-homeostasis state in resident cells of cervix_uterine and skin. In this state, mitochondrial import and cristae organization through TIMM50 and IMMT, respiratory electron transfer through NDUFA10, NDUFS1, and UQCRC1, mitochondrial metabolic support through SHMT2 and related enzymes, ER folding and membrane protein insertion through CANX, DDOST, EMC1, and NCSTN, and calcium or cation transport through ATP1A1 and ATP2A2 are transcriptionally or post-transcriptionally coordinated. The proposed link is that membrane-protein and calcium demands alter mitochondrial energetic requirements, producing the shared co-abundance signal. This is a mechanistic hypothesis, not a demonstrated causal pathway; the data establish coordinated abundance and annotated components, but do not establish directionality, cell origin, or physical interaction among all module members.

### Important genes

#### TIMM50

- **Related proteins** (co-abundance neighbors): ACSL3 (0.85), AIFM1 (0.83), CANX (0.83), ATP1A1 (0.81), EMC1 (0.81), IMMT (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Nucleoplasm, Mitochondria; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocase of inner mitochondrial membrane 50. This gene encodes a subunit of the TIM23 inner mitochondrial membrane translocase complex. The encoded protein functions as the receptor subunit that recognizes the mitochondrial targeting signal, or presequence, on protein cargo that is destined for the mitochondrial inner membrane and matrix. This protein may also play a role in maintaining the membrane permeability barrier, and knockdown of thi…
- **Diseases (Open Targets)**: 3-methylglutaconic aciduria type 9 (0.773); neurodegenerative disease (0.519); Mitochondrial encephalopathy (0.425); hereditary disease (0.415); Epileptic encephalopathy (0.370)
- **Europe PMC papers**: 442
- **Why important**: TIMM50 is the strongest network-centered member and connects mitochondrial import and membrane organization with CANX, ATP1A1, EMC1, IMMT, ACSL3, and AIFM1. Its annotated role as a receptor subunit of the TIM23 translocase, together with mitochondrial membrane and apoptosis-related functions, directly matches the central interpretation supported by (7 globally significant GO/KEGG terms, q_global 8.08e-05–0.00538; see the table). It is also supported broadly by the supplementary STRING compartment terms (15 supplementary STRING terms; within-query FDR 2.66e-06–0.0013). Its disease associations include mitochondrial and neurologic disorders, and its literature base is substantial.
- **Conclusion**: Established evidence supports TIMM50 as a plausible organizational anchor for the mitochondrial component of the module. It is reasonable to hypothesize that its co-abundance marks mitochondrial protein-import or membrane-stability demand, but the module does not prove that TIMM50 regulates the other genes.

#### NDUFS1

- **Related proteins** (co-abundance neighbors): IMMT (0.82); STRING partners: IMMT (0.901), NDUFA10 (0.999), UQCRC1 (0.998)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_09982.1, huMAP3_07653.1, huMAP3_02819.1, huMAP3_06397.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase core subunit S1. The protein encoded by this gene belongs to the complex I 75 kDa subunit family. Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Thi…
- **Diseases (Open Targets)**: mitochondrial complex I deficiency, nuclear type 5 (0.810); mitochondrial complex I deficiency (0.647); type 2 diabetes mellitus (0.608); Parkinson disease (0.603); diabetes mellitus (0.580)
- **Europe PMC papers**: 2567
- **Why important**: NDUFS1 is a core mitochondrial complex I subunit and one of the most strongly connected respiratory members in the external evidence. It is linked by STRING to IMMT, NDUFA10, and UQCRC1, and is repeatedly represented in hu.MAP respiratory complexes (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_07653.1) and (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1). It appears in every globally corrected mitochondrial and transporter term relevant to the respiratory interpretation, including (8 globally significant GO/KEGG terms, q_global 8.08e-05–0.00655; see the table) and (GO:MF primary active transmembrane transporter activity; q_global = 0.0209) (GO:MF monoatomic cation transmembrane transporter activity; q_global = 0.0496). Its established associations with complex I deficiency, Parkinson disease, and diabetes increase its biological importance.
- **Conclusion**: Established evidence identifies NDUFS1 as a respiratory-chain core marker and a key anchor for the module's mitochondrial interpretation. Its co-abundance may report respiratory capacity or energetic demand, but it cannot by itself establish altered electron transport activity.

#### NDUFA10

- **Related proteins** (co-abundance neighbors): ATP2A2 (0.82), CKAP4 (0.81); STRING partners: NDUFS1 (0.999), UQCRC1 (0.996)
- **HPA**: Tissue enhanced; Low cell type specificity; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_14018.1, huMAP3_09982.1, huMAP3_07653.1, huMAP3_02819.1, huMAP3_06397.1, huMAP3_09567.1, huMAP3_14878.1
- **Function (MyGene.info)**: NADH:ubiquinone oxidoreductase subunit A10. The protein encoded by this gene is a component of 42 kDa complex I, the first enzyme complex in the electron transport chain of mitochondria. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. A mutation in this gene was found in an individual with Leigh syndrome. [provided by RefSeq, Apr 2016].
- **Diseases (Open Targets)**: mitochondrial complex I deficiency (0.677); Leigh syndrome (0.674); mitochondrial complex I deficiency, nuclear type 22 (0.668); type 2 diabetes mellitus (0.620); diabetes mellitus (0.578)
- **Europe PMC papers**: 1163
- **Why important**: NDUFA10 is a mitochondrial complex I component with strong network integration and especially strong known links to NDUFS1 and UQCRC1. It is present in the full set of globally corrected mitochondrial, membrane-complex, and transporter terms (11 globally significant GO/KEGG terms, q_global 8.08e-05–0.0496; see the table). Its repeated placement in hu.MAP respiratory complexes (hu.MAP huMAP3_14018.1) (hu.MAP huMAP3_09982.1) (hu.MAP huMAP3_07653.1) and (hu.MAP huMAP3_02819.1) (hu.MAP huMAP3_06397.1) (hu.MAP huMAP3_09567.1) (hu.MAP huMAP3_14878.1) provides orthogonal complex-level support. The gene is associated with complex I deficiency, Leigh syndrome, and metabolic disease.
- **Conclusion**: Established evidence supports NDUFA10 as a core respiratory component rather than a generic membrane marker. Together with NDUFS1 and UQCRC1 it defines the most convincing known substructure in the module; causal coordination beyond that substructure remains a hypothesis.

#### ATP2A2

- **Related proteins** (co-abundance neighbors): SHMT2 (0.84), NDUFA10 (0.82), ALDH18A1 (0.80); STRING partners: ATP1A1 (0.82), CANX (0.849)
- **HPA**: Group enriched; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Plasma membrane; IHC detected in skin
- **hu.MAP 3.0**: huMAP3_09592.1, huMAP3_10473.1
- **Function (MyGene.info)**: ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2. This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of the skeletal muscle. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol into the sarcoplasmic reticulum lumen, and is involved in regulation of the contraction/relaxation cycle. Mutations in this gene cause Darie…
- **Diseases (Open Targets)**: Darier disease (0.823); acrokeratosis verruciformis (0.663); neurodegenerative disease (0.507); hereditary disease (0.416); schizophrenia (0.406)
- **Europe PMC papers**: 9327
- **Why important**: ATP2A2 connects the module to calcium homeostasis and membrane transport. It is linked to ATP1A1 and CANX by STRING and appears with ATP1A1 in hu.MAP complex (hu.MAP huMAP3_10473.1). It contributes to the globally corrected transporter and membrane-complex terms (GO:CC organelle membrane; q_global = 0.000124), (5 globally significant GO/KEGG terms, q_global 0.00538–0.0496; see the table). Its established role in sarco/endoplasmic-reticulum calcium transport connects membrane energetics to ER function, and its disease association with Darier disease is particularly relevant to skin biology. It is tissue-enhanced in muscle- and tongue-related contexts and is detected in skin.
- **Conclusion**: Established evidence supports ATP2A2 as the clearest calcium-handling component and a bridge between membrane transport and organelle homeostasis. Its presence is compatible with a shared epithelial membrane-stress or calcium-demand state, but that tissue-level mechanism is not directly demonstrated.

#### CANX

- **Related proteins** (co-abundance neighbors): TIMM50 (0.83), AIFM1 (0.83), ATP1A1 (0.82); STRING partners: ATP2A2 (0.849), DDOST (0.886), EMC1 (0.854), NCSTN (0.754)
- **HPA**: Low tissue specificity; Cell type enriched; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calnexin. This gene encodes a member of the calnexin family of molecular chaperones. The encoded protein is a calcium-binding, endoplasmic reticulum (ER)-associated protein that interacts transiently with newly synthesized N-linked glycoproteins, facilitating protein folding and assembly. It may also play a central role in the quality control of protein folding by retaining incorrectly folded protein subuni…
- **Diseases (Open Targets)**: neurodegenerative disease (0.462); COVID-19 (0.377); Orthomyxoviridae infectious disease (0.372); dengue disease (0.370); severe acute respiratory syndrome (0.370)
- **Europe PMC papers**: 2520
- **Why important**: CANX is a network bridge between TIMM50, AIFM1, and ATP1A1, while STRING connects it to ATP2A2, DDOST, EMC1, and NCSTN. This places calnexin at the interface of ER protein folding, membrane quality control, calcium handling, and the mitochondrial-associated signal. Its annotations support ER glycoprotein folding and ER-associated degradation, and it contributes to the globally corrected membrane and organelle terms (GO:CC mitochondrial membrane; q_global = 8.08e-05) (GO:CC organelle membrane; q_global = 0.000124) (GO:CC mitochondrial envelope; q_global = 0.000241), (GO:CC organelle envelope; q_global = 0.00447), and (GO:CC membrane; q_global = 0.00869). Its extensive literature and disease-related associations make it an informative marker of cellular proteostasis.
- **Conclusion**: Established evidence supports CANX as the principal ER quality-control representative of the module and as a plausible cross-organelle bridge. The hypothesis that ER proteostasis demand drives the shared module should be tested experimentally rather than inferred solely from co-abundance.

#### SHMT2

- **Related proteins** (co-abundance neighbors): ATP2A2 (0.84), PRKDC (0.80); STRING partners: ALDH18A1 (0.804)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine hydroxymethyltransferase 2. This gene encodes the mitochondrial form of a pyridoxal phosphate-dependent enzyme that catalyzes the reversible reaction of serine and tetrahydrofolate to glycine and 5,10-methylene tetrahydrofolate. The encoded product is primarily responsible for glycine synthesis. The activity of the encoded protein has been suggested to be the primary source of intracellular glycine. The gene which encodes th…
- **Diseases (Open Targets)**: neurodevelopmental disorder with cardiomyopathy, spasticity, and brain abnormalities (0.771); microcephaly (0.370); polymicrogyria (0.370); neurodevelopmental disorder (0.336); hereditary disease (0.192)
- **Europe PMC papers**: 2579
- **Why important**: SHMT2 links mitochondrial one-carbon and glycine metabolism to the module. It is network-connected to ATP2A2 and PRKDC and has a known STRING relationship with ALDH18A1. It appears in the globally corrected mitochondrial terms (6 globally significant GO/KEGG terms, q_global 8.08e-05–0.00447; see the table) and (GO:CC membrane; q_global = 0.00869), while its established functions include mitochondrial serine, glycine, and one-carbon metabolism and regulation of oxidative phosphorylation. Its disease associations include neurodevelopmental and cardiomyopathy-related disorders, and it has a substantial literature base.
- **Conclusion**: Established evidence supports SHMT2 as a metabolic-support component that could couple biosynthetic state to mitochondrial respiration. Its position suggests a plausible metabolic bridge, but the data do not establish that one-carbon metabolism is the cause of the shared tissue-pair pattern.

## Module 8

**Tissue pair**: cervix_uterine and skin  
**Genes (31)**: AGO2, PRMT3, AP2B1, CBS, CDC73, CTR9, DCAF8, ELP1, ELP2, FKBP5, GOPC, IPO11, KIFBP, LACTB, MLH1, MSH2, MSH6, NRDC, NUP98, RRM1, POLR3B, MRPS22, MRPS27, SHTN1, SMC2, SMC5, TXLNG, TDP2, USP15, USP8, PPIP5K2

### Function

The strongest interpretation is a nuclear gene-regulatory and genome-maintenance module with two connected functional axes. The first is transcriptional regulation: AGO2, CDC73, CTR9 and ELP2 jointly support the globally significant RNA polymerase binding and basal transcription terms (GO:MF RNA polymerase II complex binding; q_global = 0.0096), (GO:MF RNA polymerase core enzyme binding; q_global = 0.0096), (GO:MF basal transcription machinery binding; q_global = 0.0257) and (GO:MF basal RNA polymerase II transcription machinery binding; q_global = 0.0257). CDC73 and CTR9 are components of the PAF1/RNA polymerase II regulatory machinery, ELP2 is an Elongator subunit associated with transcriptional elongation and chromatin remodeling, and AGO2 contributes RNA-mediated gene regulation. The second axis is mismatch recognition and DNA surveillance: MLH1, MSH2 and MSH6 support the globally significant mismatch-binding, mismatch-repair-complex, DNA-damage-sensor and single-stranded-DNA-binding terms (GO:MF guanine/thymine mispair binding; q_global = 0.0145), (GO:CC mismatch repair complex; q_global = 0.0427), (GO:MF DNA damage sensor activity; q_global = 0.0427), (GO:MF ATP-dependent DNA damage sensor activity; q_global = 0.0427) and (GO:MF single-stranded DNA binding; q_global = 0.0496). SMC2, SMC5, TDP2 and RRM1 provide additional annotations compatible with chromosome organization, DNA repair or nucleotide supply, but these genes do not by themselves establish a single unified pathway. The network therefore appears to combine transcriptional control with DNA replication, repair and genome-stability functions rather than representing a narrowly tissue-specific pathway.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary identifies only one secreted gene, and the listed proteins are predominantly intracellular, nuclear, cytosolic or mitochondrial. Most genes have low tissue specificity, with a smaller set showing tissue enhancement in organs such as skeletal muscle, liver, pancreas, tongue or brain. The module is therefore broadly compatible with common cellular machinery in both cervix and skin rather than a specialized secretory program. HPA also shows frequent cell-type enhancement, especially for neutrophils, together with enrichment signals involving monocyte, erythrocyte-progenitor and other cell types. However, most genes have low immune-cell specificity and the module is not dominated by canonical secreted or blood proteins. A shared contribution from immune or other common cell populations is consequently possible, but the HPA evidence does not justify labeling the module as a blood-contamination signature. Protein detection in both cervix and skin for most genes supports the plausibility that the module reflects cellular biology present in both tissues.

**GO/KEGG enrichment**: 9 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA polymerase II complex binding | 0.0096 | AGO2, CDC73, CTR9, ELP2 |
| GO:MF RNA polymerase core enzyme binding | 0.0096 | AGO2, CDC73, CTR9, ELP2 |
| GO:MF guanine/thymine mispair binding | 0.0145 | MLH1, MSH2, MSH6 |
| GO:MF basal transcription machinery binding | 0.0257 | AGO2, CDC73, CTR9, ELP2 |
| GO:MF basal RNA polymerase II transcription machinery binding | 0.0257 | AGO2, CDC73, CTR9, ELP2 |
| GO:CC mismatch repair complex | 0.0427 | MLH1, MSH2, MSH6 |
| GO:MF DNA damage sensor activity | 0.0427 | MLH1, MSH2, MSH6 |
| GO:MF ATP-dependent DNA damage sensor activity | 0.0427 | MLH1, MSH2, MSH6 |
| GO:MF single-stranded DNA binding | 0.0496 | MLH1, MSH2, SMC2, SMC5, TDP2 |

### STRING and hu.MAP

STRING provides strong known relationships within the mismatch-repair branch: MLH1--MSH2, MLH1--MSH6 and MSH2--MSH6 are highly supported, matching the established MutL and MutS mismatch-repair machinery. It also supports the CDC73--CTR9 relationship and links CDC73 and CTR9 with ELP2, while ELP1--ELP2 is strongly supported. The SMC2--SMC5 relationship is present but weaker than the core mismatch-repair links, and MRPS22--MRPS27 identifies a mitochondrial-ribosome substructure. The hu.MAP evidence independently places CDC73 and CTR9 in multiple transcription or RNA-polymerase-associated complexes, and repeatedly places ELP1 and ELP2 in Elongator-related complexes. These convergent STRING and hu.MAP observations mean that parts of the module recapitulate established molecular machinery rather than being unexplained associations. At the same time, most module edges are not represented by the reported high-confidence STRING interactions or hu.MAP complexes. Thus the co-abundance module is broader than any one known physical complex and should not be interpreted as a single stable protein complex.

**STRING interactions (score >= 0.7)**: 10 of 465 gene pairs: AGO2–CTR9 (0.744); CDC73–CTR9 (0.999); CDC73–ELP2 (0.768); CTR9–ELP2 (0.76); ELP1–ELP2 (0.998); MLH1–MSH2 (0.999); MLH1–MSH6 (0.999); MRPS22–MRPS27 (0.999); MSH2–MSH6 (0.999); SMC2–SMC5 (0.705)
**STRING functional enrichment (supplementary, within-query FDR)**: DISEASES Organ system benign neoplasm (FDR = 0.0346, 6 genes); DISEASES Sebaceous adenoma (FDR = 0.0346, 3 genes); DISEASES Familial adenomatous polyposis (FDR = 0.0402, 3 genes); DISEASES Muir-Torre syndrome (FDR = 0.0402, 3 genes); DISEASES Endometrial cancer (FDR = 0.0402, 3 genes); DISEASES Endocrine system disease (FDR = 0.0409, 5 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_11092.1 (CDC73, CTR9, POLR3B; 3/65); huMAP3_06234.1 (CDC73, CTR9; 2/3); huMAP3_00156.1 (ELP1, ELP2; 2/4); huMAP3_06545.1 (ELP1, ELP2; 2/4); huMAP3_05863.1 (ELP1, ELP2; 2/5); huMAP3_08256.1 (ELP1, ELP2; 2/5); huMAP3_07900.1 (ELP1, ELP2; 2/6); huMAP3_12672.1 (ELP1, ELP2; 2/6); huMAP3_10066.1 (ELP1, ELP2; 2/7); huMAP3_10779.1 (ELP1, ELP2; 2/8); huMAP3_07948.1 (CDC73, CTR9; 2/9); huMAP3_11018.1 (CDC73, CTR9; 2/15); huMAP3_12111.1 (CDC73, CTR9; 2/16); huMAP3_07454.1 (CDC73, CTR9; 2/27); huMAP3_07749.1 (CDC73, CTR9; 2/28); huMAP3_09843.1 (CDC73, CTR9; 2/29)

### Novelty

The biological components are not novel individually: mismatch repair, PAF1-associated transcriptional regulation, Elongator biology, chromosome maintenance and mitochondrial translation are established functions, and several relationships are supported by STRING or hu.MAP. What may be novel is the co-abundance organization of these genes as a conserved module shared by cervix_uterine and skin. The fact sheet does not provide a prior tissue-pair module, independent cohort replication, perturbation experiment or literature comparison demonstrating that this exact gene set and cross-tissue structure have been reported before. Accordingly, the module should be described as a potentially new systems-level observation, not as a proven new biological pathway or a newly discovered physical complex. The absence of some genes or edges from STRING and hu.MAP cannot establish novelty, because those resources capture known physical or curated relationships rather than every co-abundance pattern.

**Hypothesis.** Hypothesis: in shared epithelial or stromal cellular populations of cervix and skin, coordinated transcriptional and RNA-processing activity may be coupled to ongoing DNA surveillance and repair. A PAF1/Elongator-associated transcriptional state involving CDC73, CTR9 and ELP2 could covary with AGO2-mediated post-transcriptional regulation, while MLH1, MSH2 and MSH6 maintain mismatch recognition and repair during replication or transcription-associated stress. TDP2, SMC2, SMC5 and RRM1 could connect this state to DNA-break processing, chromosome organization and nucleotide availability. The observed module may therefore reflect a common tissue-cellular state that balances gene expression, genome integrity and cell maintenance. This is a mechanistic hypothesis generated from co-abundance and annotations; the data do not establish physical interaction between all module members, causal regulation, or a tissue-specific disease mechanism.

### Important genes

#### MSH2

- **Related proteins** (co-abundance neighbors): TDP2 (0.85), AGO2 (0.84), LACTB (0.82), MSH6 (0.81); STRING partners: MLH1 (0.999), MSH6 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 2. This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: Lynch syndrome (0.891); colorectal cancer (0.776); mismatch repair cancer syndrome (0.775); Muir-Torre syndrome (0.752); mismatch repair cancer syndrome 1 (0.740)
- **Europe PMC papers**: 22581
- **Why important**: MSH2 is central to the DNA-surveillance interpretation. It occupies a relatively connected position in the module, forms the established STRING relationships with MLH1 and MSH6, and contributes to every globally significant mismatch-repair or DNA-damage-sensor term involving that branch (GO:MF guanine/thymine mispair binding; q_global = 0.0145), (GO:CC mismatch repair complex; q_global = 0.0427), (GO:MF DNA damage sensor activity; q_global = 0.0427), (GO:MF ATP-dependent DNA damage sensor activity; q_global = 0.0427) and (GO:MF single-stranded DNA binding; q_global = 0.0496). Its disease associations include Lynch syndrome, colorectal cancer, mismatch-repair cancer syndrome and Muir-Torre syndrome, and it has extensive literature support. The supplementary STRING disease terms (STRING DISEASES Organ system benign neoplasm; within-query FDR = 0.0346) through (STRING DISEASES Endocrine system disease; within-query FDR = 0.0409) also repeatedly contain MSH2 with MLH1 and MSH6.
- **Conclusion**: Established evidence supports MSH2 as a core mismatch-recognition component and one of the most informative anchors of the module. It is reasonable to hypothesize that its co-abundance marks genome-maintenance demand in the shared cellular context, but the module does not show that MSH2 activity is altered or causally driving the tissue-shared pattern.

#### MLH1

- **Related proteins** (co-abundance neighbors): NRDC (0.85), ELP2 (0.84), CTR9 (0.82); STRING partners: MSH2 (0.999), MSH6 (0.999)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutL homolog 1. The protein encoded by this gene can heterodimerize with mismatch repair endonuclease PMS2 to form MutL alpha, part of the DNA mismatch repair system. When MutL alpha is bound by MutS beta and some accessory proteins, the PMS2 subunit of MutL alpha introduces a single-strand break near DNA mismatches, providing an entry point for exonuclease degradation. The encoded protein is also involved in DNA…
- **Diseases (Open Targets)**: Lynch syndrome (0.848); colorectal cancer (0.820); mismatch repair cancer syndrome 1 (0.806); Muir-Torre syndrome (0.758); colon carcinoma (0.744)
- **Europe PMC papers**: 25031
- **Why important**: MLH1 is an essential partner in the mismatch-repair branch and has strong STRING relationships with MSH2 and MSH6. It contributes to all globally significant mismatch-repair and DNA-sensing terms (GO:MF guanine/thymine mispair binding; q_global = 0.0145), (GO:CC mismatch repair complex; q_global = 0.0427), (GO:MF DNA damage sensor activity; q_global = 0.0427), (GO:MF ATP-dependent DNA damage sensor activity; q_global = 0.0427) and (GO:MF single-stranded DNA binding; q_global = 0.0496). Its annotations include mismatch repair and DNA-damage signaling, while its disease associations prominently include Lynch syndrome, colorectal cancer, mismatch-repair cancer syndrome and Muir-Torre syndrome. It also has very extensive literature support.
- **Conclusion**: Established evidence identifies MLH1 as a core repair-system member, not merely a peripheral correlated gene. Its presence supports genome-integrity biology in the module, whereas any claim that the module indicates deficient repair, cancer risk or active DNA damage would remain a hypothesis requiring functional or clinical validation.

#### MSH6

- **Related proteins** (co-abundance neighbors): AGO2 (0.82), MSH2 (0.81); STRING partners: MLH1 (0.999), MSH2 (0.999)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Golgi apparatus, Vesicles; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mutS homolog 6. This gene encodes a member of the DNA mismatch repair MutS family. In E. coli, the MutS protein helps in the recognition of mismatched nucleotides prior to their repair. A highly conserved region of approximately 150 aa, called the Walker-A adenine nucleotide binding motif, exists in MutS homologs. The encoded protein heterodimerizes with MSH2 to form a mismatch recognition complex that functions …
- **Diseases (Open Targets)**: Lynch syndrome (0.878); colorectal cancer (0.832); endometrial cancer (0.819); mismatch repair cancer syndrome (0.799); mismatch repair cancer syndrome 1 (0.737)
- **Europe PMC papers**: 17901
- **Why important**: MSH6 completes the strongly supported MSH2-associated mismatch-recognition unit and contributes to the globally significant mismatch-binding, mismatch-repair-complex and DNA-damage-sensor terms (GO:MF guanine/thymine mispair binding; q_global = 0.0145), (GO:CC mismatch repair complex; q_global = 0.0427), (GO:MF DNA damage sensor activity; q_global = 0.0427) and (GO:MF ATP-dependent DNA damage sensor activity; q_global = 0.0427). It has strong STRING relationships with both MSH2 and MLH1. Its disease associations include Lynch syndrome, colorectal cancer, endometrial cancer and mismatch-repair cancer syndrome, with substantial literature support.
- **Conclusion**: Established evidence supports MSH6 as a core component of the module's mismatch-repair interpretation. The coordinated appearance of MSH2, MLH1 and MSH6 is more persuasive than any one gene alone, but co-abundance cannot determine whether repair activity is increased, decreased or simply reflects cell composition.

#### CDC73

- **Related proteins** (co-abundance neighbors): TDP2 (0.84), LACTB (0.80); STRING partners: CTR9 (0.999), ELP2 (0.768)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_11092.1, huMAP3_06234.1, huMAP3_07948.1, huMAP3_11018.1, huMAP3_12111.1, huMAP3_07454.1, huMAP3_07749.1, huMAP3_09843.1
- **Function (MyGene.info)**: cell division cycle 73. This gene encodes a tumor suppressor that is involved in transcriptional and post-transcriptional control pathways. The protein is a component of the the PAF protein complex, which associates with the RNA polymerase II subunit POLR2A and with a histone methyltransferase complex. This protein appears to facilitate the association of 3' mRNA processing factors with actively-transcribed chromatin. Mu…
- **Diseases (Open Targets)**: hyperparathyroidism 2 with jaw tumors (0.810); parathyroid gland carcinoma (0.802); familial isolated hyperparathyroidism (0.738); hyperparathyroidism (0.599); hereditary neoplastic syndrome (0.555)
- **Europe PMC papers**: 2210
- **Why important**: CDC73 is a key transcriptional anchor despite a modest direct network degree, because it contributes with CTR9, AGO2 and ELP2 to the globally significant RNA polymerase and basal transcription terms (GO:MF RNA polymerase II complex binding; q_global = 0.0096), (GO:MF RNA polymerase core enzyme binding; q_global = 0.0096), (GO:MF basal transcription machinery binding; q_global = 0.0257) and (GO:MF basal RNA polymerase II transcription machinery binding; q_global = 0.0257). It has a very strong STRING relationship with CTR9 and appears with CTR9 in multiple hu.MAP transcription-associated complexes (hu.MAP huMAP3_11092.1), (hu.MAP huMAP3_06234.1) and (hu.MAP huMAP3_07948.1) through (hu.MAP huMAP3_09843.1). CDC73 is a PAF1-complex component involved in transcriptional and post-transcriptional control and is associated with hyperparathyroidism-jaw tumor syndrome and related neoplastic disorders. Its literature volume is substantial.
- **Conclusion**: Established evidence supports CDC73 as a credible marker of the module's transcriptional-regulatory branch and as an experimentally grounded connection to PAF1-associated complexes. The module does not establish that CDC73 dysfunction or tumor-suppressor loss is present in either tissue; that would be an unsupported disease inference.

#### CTR9

- **Related proteins** (co-abundance neighbors): ELP2 (0.84), MLH1 (0.82); STRING partners: AGO2 (0.744), CDC73 (0.999), ELP2 (0.76)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_11092.1, huMAP3_06234.1, huMAP3_07948.1, huMAP3_11018.1, huMAP3_12111.1, huMAP3_07454.1, huMAP3_07749.1, huMAP3_09843.1
- **Function (MyGene.info)**: CTR9 component of Paf1/RNA polymerase II complex. The protein encoded by this gene is a component of the PAF1 complex, which associates with RNA polymerase II and functions in transcriptional regulation and elongation. This complex also plays a role in the modification of histones. [provided by RefSeq, Oct 2016].
- **Diseases (Open Targets)**: CTR9-related neurodevelopmental disorder (0.615); neurodegenerative disease (0.518); Wilms tumor (0.486); hereditary disease (0.477); Nephroblastoma (0.465)
- **Europe PMC papers**: 882
- **Why important**: CTR9 is part of the PAF1/RNA polymerase II regulatory machinery and contributes to all four globally significant transcription-related terms (GO:MF RNA polymerase II complex binding; q_global = 0.0096), (GO:MF RNA polymerase core enzyme binding; q_global = 0.0096), (GO:MF basal transcription machinery binding; q_global = 0.0257) and (GO:MF basal RNA polymerase II transcription machinery binding; q_global = 0.0257). Its strong STRING links to CDC73 and ELP2, together with repeated hu.MAP membership with CDC73 in transcription-associated complexes (hu.MAP huMAP3_11092.1), (hu.MAP huMAP3_06234.1) and (hu.MAP huMAP3_07948.1) through (hu.MAP huMAP3_09843.1), provide independent support for its functional placement. CTR9 is associated with transcriptional elongation, chromatin organization and developmental regulation, and with CTR9-related neurodevelopmental disorder and Wilms tumor.
- **Conclusion**: Established evidence supports CTR9 as a central interpretive bridge between the co-abundance pattern and transcriptional regulation. Its association with the DNA-repair branch through module co-abundance is suggestive but does not prove direct molecular coupling between PAF1 activity and mismatch repair.

#### ELP2

- **Related proteins** (co-abundance neighbors): IPO11 (0.84), CTR9 (0.84), MLH1 (0.84), PRMT3 (0.83); STRING partners: CDC73 (0.768), CTR9 (0.76), ELP1 (0.998)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_00156.1, huMAP3_06545.1, huMAP3_05863.1, huMAP3_08256.1, huMAP3_07900.1, huMAP3_12672.1, huMAP3_10066.1, huMAP3_10779.1
- **Function (MyGene.info)**: elongator acetyltransferase complex subunit 2. The protein encoded by this gene is a core subunit of the elongator complex, a histone acetyltransferase complex that associates with RNA polymerase II. In addition to histone acetylation, the encoded protein effects transcriptional elongation and may help remodel chromatin. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: intellectual disability, autosomal recessive 58 (0.749); neurodegenerative disease (0.535); hereditary disease (0.495); Profound intellectual disability (0.379); complex neurodevelopmental disorder with motor features (0.370)
- **Europe PMC papers**: 528
- **Why important**: ELP2 contributes to all globally significant transcription-related terms (GO:MF RNA polymerase II complex binding; q_global = 0.0096), (GO:MF RNA polymerase core enzyme binding; q_global = 0.0096), (GO:MF basal transcription machinery binding; q_global = 0.0257) and (GO:MF basal RNA polymerase II transcription machinery binding; q_global = 0.0257), has strong STRING support with ELP1, CDC73 and CTR9, and is repeatedly represented with ELP1 in hu.MAP Elongator-related complexes (hu.MAP huMAP3_00156.1) through (hu.MAP huMAP3_10779.1). Its annotation supports transcriptional elongation, chromatin remodeling and tRNA wobble modification, providing a possible link between transcription and translation. It is associated with autosomal-recessive intellectual disability and neurodevelopmental disease and has a moderate literature base.
- **Conclusion**: Established evidence supports ELP2 as a genuine transcriptional and Elongator-associated component of the module. The hypothesis that ELP2 coordinates transcriptional output with the DNA-repair branch is plausible from the network and enrichment pattern, but it is not demonstrated by the supplied data.

## Module 9

**Tissue pair**: cervix_uterine and skin  
**Genes (5)**: AKR1C2, ANXA3, PCCB, TRADD, VTN

### Function

No GO or KEGG term passed global correction, so there is no statistically supported pathway annotation for this module. The gene set instead suggests a mixed biological signal involving extracellular adhesion and matrix interactions through VTN, inflammatory and death-receptor signalling through TRADD and ANXA3, epithelial and steroid or prostaglandin metabolism through AKR1C2, and mitochondrial propionyl-CoA and related short-chain fatty-acid catabolism through PCCB. The co-abundance structure links ANXA3 with VTN and AKR1C2, and links VTN and PCCB indirectly through TRADD, but this arrangement does not establish one unified biochemical pathway. The appropriate interpretation is therefore a tissue-shared expression module with plausible extracellular, inflammatory, epithelial-metabolic, and mitochondrial components rather than a validated canonical pathway.

**Cell composition.** The module is not predominantly a plasma or secreted-protein module: only VTN is annotated as secreted to blood. VTN is liver-enriched, absent by HPA immune-cell detection, and not detected by immunohistochemistry in cervix or skin, so its co-abundance may reflect circulating protein, tissue-adjacent vascular or extracellular-matrix biology, or transcript-level regulation rather than local protein abundance. Most members are not immune-cell enriched; ANXA3 is associated with neutrophils, while the other genes are not detected in immune cells or have low immune-cell specificity. The HPA profile is broadly tissue and cell-type selective, with repeated liver and hepatocyte associations and additional epithelial-cell associations. Thus, contamination by blood cells is not the leading explanation, although a circulating VTN contribution or a shared epithelial, stromal, or vascular component remains plausible. Protein detection is present for ANXA3 and PCCB in both tissues, whereas VTN and AKR1C2 lack tissue immunohistochemical detection in the relevant tissues and TRADD is detected in cervix but not skin.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

There are no high-confidence STRING interactions among the module genes and no hu.MAP complex containing multiple module members. Consequently, the co-abundance edges are not corroborated by the supplied physical-interaction or curated-complex resources. This weakens a claim that the module is a stable multiprotein complex. It is still compatible with co-regulation, shared cellular composition, indirect signalling, extracellular coupling, or coordinated tissue-state responses. The absence of STRING and hu.MAP support is evidence against an already well-established physical network, not evidence that the co-abundance pattern is artifactual.

**STRING interactions (score >= 0.7)**: 0 of 10 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a previously unreported tissue-pair co-abundance pattern, because its member combination has no supplied STRING interaction support, no shared hu.MAP complex, and no globally significant GO or KEGG enrichment. However, it cannot be called a new biological pathway or a definitive novel mechanism. Several individual genes have established functions and disease or literature associations, so the potentially novel feature is their coordinated abundance across cervix_uterine and skin, not the genes themselves. Independent replication, adjustment for tissue composition and circulating proteins, and validation at the protein or single-cell level would be needed before claiming biological novelty.

**Hypothesis.** Hypothesis: the module reflects a shared epithelial or stromal tissue-state program that couples local inflammatory and adhesion biology with metabolic adaptation. In this model, ANXA3 may connect neutrophil-associated or membrane-signalling processes with VTN-dependent extracellular adhesion, TRADD may represent a parallel inflammatory and death-receptor signalling component, AKR1C2 may mark epithelial steroid or prostaglandin handling, and PCCB may reflect mitochondrial substrate metabolism. VTN could contribute a blood-borne or extracellular-matrix signal that makes the module appear conserved between tissues. This is a mechanistic hypothesis only; the lack of globally enriched GO or KEGG terms and the absence of STRING or hu.MAP support prevent treating it as established.

### Important genes

#### ANXA3

- **Related proteins** (co-abundance neighbors): AKR1C2 (0.87), VTN (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enriched; location Plasma membrane; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A3. This gene encodes a member of the annexin family.  Members of this calcium-dependent phospholipid-binding protein family play a role in the regulation of cellular growth and in signal transduction pathways.  This protein functions in the inhibition of phopholipase A2 and cleavage of inositol 1,2-cyclic phosphate to form inositol 1-phosphate. This protein may also play a role in anti-coagulation. […
- **Diseases (Open Targets)**: rheumatoid arthritis (0.318); Meniere disease (0.276); insomnia (0.255); hair color (0.209); refractive error (0.176)
- **Europe PMC papers**: 2243
- **Why important**: ANXA3 is among the most connected members of the co-abundance subgraph and links VTN with AKR1C2. Its established annexin functions include calcium-dependent phospholipid binding, phospholipase A2 inhibition, signal transduction, phagocytosis, neutrophil degranulation, antibacterial defence, endothelial migration, and angiogenesis. HPA associates it with bone marrow and neutrophils and detects it in both cervix and skin. Its extensive literature and disease associations make it a strong candidate for connecting inflammatory or vascular biology with the rest of the module.
- **Conclusion**: Established: ANXA3 has membrane-associated, inflammatory, phagocytic, and migration-related functions and is detected in both tissues. Hypothesis: within this module it may be the local cellular component linking VTN-related adhesion with epithelial or inflammatory state. The co-abundance relationship does not prove direct molecular interaction.

#### VTN

- **Related proteins** (co-abundance neighbors): TRADD (0.84), ANXA3 (0.84); STRING partners: none
- **HPA**: Tissue enriched; Group enriched; blood Not detected in immune cells; location Endoplasmic reticulum, Vesicles; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: vitronectin. The protein encoded by this gene functions in part as an adhesive glycoprotein. Differential expression of this protein can promote either cell adhesion or migration as it links cells to the extracellular matrix through a variety of ligands. These ligands include integrins, plasminogen activator inhibitor-1, and urokinase plasminogen activator receptor. This secreted protein can be present in the …
- **Diseases (Open Targets)**: hypertensive disorder (0.421); dengue disease (0.376); neurodegenerative disease (0.343); temporal arteritis (0.338); age-related macular degeneration (0.313)
- **Europe PMC papers**: 3940
- **Why important**: VTN is a central connector in the observed co-abundance graph, linked with ANXA3 and TRADD. It is an established secreted adhesive glycoprotein involved in cell adhesion, cell-matrix adhesion, integrin signalling, and migration, and it can circulate in plasma and form extracellular-matrix multimers. HPA identifies it as liver-enriched, associated with cholangiocytes and hepatocytes, secreted to blood, and not detected in immune cells. Its substantial literature and disease associations make it important for interpreting whether the module reflects extracellular or circulating biology rather than a local intracellular complex.
- **Conclusion**: Established: VTN can mediate extracellular adhesion and is a circulating or matrix-associated protein with strong liver and hepatobiliary expression evidence. Hypothesis: VTN may be the shared extracellular or blood-borne signal contributing to conservation between cervix and skin. Its lack of local immunohistochemical detection argues for caution in interpreting it as locally produced protein in both tissues.

#### TRADD

- **Related proteins** (co-abundance neighbors): VTN (0.84), PCCB (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: TNFRSF1A associated via death domain. The protein encoded by this gene is a death domain containing adaptor molecule that interacts with TNFRSF1A/TNFR1 and mediates programmed cell death signaling and NF-kappaB activation. This protein binds adaptor protein TRAF2, reduces the recruitment of inhibitor-of-apoptosis proteins (IAPs) by TRAF2, and thus suppresses TRAF2 mediated apoptosis. This protein can also interact with receptor TNFRSF…
- **Diseases (Open Targets)**: hereditary disease (0.370); Abnormality of the skeletal system (0.222); cataract 5 multiple types (0.181); androgenetic alopecia (0.091); non-small cell lung carcinoma (0.085)
- **Europe PMC papers**: 6284
- **Why important**: TRADD is a central connector linking VTN and PCCB in the co-abundance graph. It is an established death-domain adaptor for TNFRSF1A and related receptor pathways, with roles in programmed cell death, inflammatory signalling, and canonical NF-kappaB activation. HPA reports low tissue and immune-cell specificity, with epithelial cell-type enhancement and protein detection in cervix. Its extensive literature and disease associations support its importance as the signalling component of an otherwise mixed module.
- **Conclusion**: Established: TRADD participates in death-receptor and NF-kappaB-related signalling. Hypothesis: its co-abundance with VTN and PCCB may indicate coordinated tissue stress or inflammatory signalling rather than a direct physical complex. The lack of STRING and hu.MAP support means this proposed connection remains indirect.

#### AKR1C2

- **Related proteins** (co-abundance neighbors): ANXA3 (0.87); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm, Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldo-keto reductase family 1 member C2. This gene encodes a member of the aldo/keto reductase superfamily, which consists of more than 40 known enzymes and proteins. These enzymes catalyze the conversion of aldehydes and ketones to their corresponding alcohols using NADH and/or NADPH as cofactors. The enzymes display overlapping but distinct substrate specificity. This enzyme binds bile acid with high affinity, and shows minimal 3-alpha…
- **Diseases (Open Targets)**: 17,20-lyase deficiency, isolated (0.690); CIC-rearranged sarcoma (0.333); neurodegenerative disease (0.240); Abnormal nasolacrimal system morphology (0.218); bipolar disorder (0.191)
- **Europe PMC papers**: 1855
- **Why important**: AKR1C2 is directly connected to ANXA3 and provides a distinct metabolic and epithelial dimension. It encodes an aldo-keto reductase involved in aldehyde and ketone reduction, has high-affinity bile-acid binding, and is annotated for prostaglandin metabolism, steroid metabolism, epithelial differentiation, and cell-population proliferation. HPA reports tissue enhancement in adipose tissue and liver and enhancement in several epithelial cell types. Its established enzymatic function and substantial literature make it a useful marker for metabolic or epithelial-state contributions to the module.
- **Conclusion**: Established: AKR1C2 is an epithelial-associated metabolic enzyme with steroid and prostaglandin-related functions. Hypothesis: its relationship with ANXA3 may reflect coordinated epithelial inflammatory and lipid-mediator biology. The available evidence does not establish that AKR1C2 drives the shared tissue module.

#### PCCB

- **Related proteins** (co-abundance neighbors): TRADD (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: propionyl-CoA carboxylase subunit beta. The protein encoded by this gene is a subunit of the propionyl-CoA carboxylase (PCC) enzyme, which is involved in the catabolism of propionyl-CoA. PCC is a mitochondrial enzyme that probably acts as a dodecamer of six alpha subunits and six beta subunits. This gene encodes the beta subunit of PCC. Defects in this gene are a cause of propionic acidemia type II (PA-2). Multiple transcript variants e…
- **Diseases (Open Targets)**: propionic acidemia (0.861); hereditary disease (0.517); hypertensive disorder (0.453); coronary artery disorder (0.438); coronary atherosclerosis (0.428)
- **Europe PMC papers**: 1404
- **Why important**: PCCB is connected to TRADD and represents the mitochondrial metabolic component of the module. It encodes the beta subunit of propionyl-CoA carboxylase, which participates in propionyl-CoA, branched-chain amino-acid, short-chain fatty-acid, and related fatty-acid catabolism. HPA reports liver tissue enhancement, germ-cell-type enhancement, low immune-cell specificity, and protein detection in both cervix and skin. Its established enzyme-complex role and disease association with propionic acidemia make it important even though it is peripheral in the co-abundance graph.
- **Conclusion**: Established: PCCB supports mitochondrial propionyl-CoA catabolism and is detected in both tissues. Hypothesis: its co-abundance with TRADD may mark a shared metabolic response accompanying tissue stress or inflammatory signalling. There is no evidence here that PCCB physically interacts with TRADD or that this module is a propionyl-CoA pathway.

## Module 10

**Tissue pair**: cervix_uterine and skin  
**Genes (7)**: ALDH1A3, ANPEP, ANXA1, CD47, DNM2, PRKCD, PAPSS2

### Function

The strongest functional interpretation is a coordinated phagocytosis- and hormone-level-regulation program. Phagocytosis is supported by the globally corrected term (GO:BP phagocytosis; q_global = 0.00683), containing ANXA1, CD47, DNM2, and PRKCD. This set spans anti-inflammatory membrane regulation, cell-surface signaling, endocytic membrane remodeling, and kinase-controlled stress or apoptotic responses. Regulation of hormone levels is independently supported by (GO:BP regulation of hormone levels; q_global = 0.0343), containing ALDH1A3, ANPEP, ANXA1, and PAPSS2. The latter group suggests a broader metabolic and epithelial-interface context involving retinal and retinoic acid metabolism, peptide processing, and sulfation. The star-like co-abundance structure centered on ALDH1A3 links these two functional themes, while the ANPEP-DNM2 edge provides a secondary membrane and endocytic branch. These results support a coordinated biological state, but they do not establish direct physical binding among the proteins.

**Cell composition.** This is not primarily a secreted-protein module: ANXA1 is the only gene identified as secreted to blood, whereas the other proteins are intracellular or membrane-associated. It is also not a uniformly blood-cell module. HPA shows mixed immune-cell specificity, with neutrophil-associated evidence for ANPEP, PRKCD, and DNM2, basophil-associated evidence for ANXA1, and myeloid-cell associations for PAPSS2, but CD47 has low immune-cell specificity and ALDH1A3 is not detected in immune cells. The module instead has substantial cell-type structure, including epithelial, stromal, neutrophil, platelet, and other specialized cell associations. Its tissue annotations are heterogeneous, including prostate, urinary bladder, intestine, pancreas, esophagus, and adrenal gland, rather than being specific to cervix or skin. Thus, the shared signal could reflect a common epithelial or stromal state, an inflammatory or phagocytic cell component, or sample-composition effects. Protein detection in both cervix and skin supports biological detectability for most genes, but the absence of PAPSS2 protein detection in those tissues cautions against treating every transcript-level association as a local protein mechanism.

**GO/KEGG enrichment**: 2 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:BP phagocytosis | 0.00683 | ANXA1, CD47, DNM2, PRKCD |
| GO:BP regulation of hormone levels | 0.0343 | ALDH1A3, ANPEP, ANXA1, PAPSS2 |

### STRING and hu.MAP

No STRING functional enrichment was reported, and no STRING pairwise relationship reached the supplied interaction threshold. No hu.MAP complex contained multiple module members. Therefore, the module is not supported by an already catalogued high-confidence interaction network or shared protein complex. The co-abundance edges should consequently be interpreted as coordinated expression relationships, not as demonstrated physical interactions. The absence of STRING and hu.MAP support is informative about known molecular connectivity, but it does not invalidate the module and does not by itself imply that the biology is novel.

**STRING interactions (score >= 0.7)**: 0 of 21 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The module may represent a novel cross-tissue co-abundance pattern, because its specific combination of ALDH1A3, ANPEP, PAPSS2, CD47, ANXA1, PRKCD, and DNM2 is not accompanied by a reported STRING interaction set or hu.MAP complex. However, it cannot be called a new biological pathway on the basis of this evidence alone. The individual functions of the genes and the phagocytosis and hormone-level associations are established, and the HPA annotations indicate several plausible shared cell types and tissue states that could generate the pattern. A defensible novelty claim is therefore limited to the shared cervix-skin co-abundance configuration and its proposed connection between retinoid or hormone-related metabolism and phagocytic membrane biology. Independent cohorts, cell-composition adjustment, and perturbation or spatial validation would be needed to establish that this is a tissue-intrinsic mechanism rather than a composition-driven signal.

**Hypothesis.** Hypothesis: a shared epithelial or stromal stress state in cervix and skin coordinates retinoid-related metabolism with immune-interface remodeling. ALDH1A3 may mark or help organize the metabolic state, while ANXA1, CD47, PRKCD, and DNM2 could connect that state to phagocytic recognition, membrane trafficking, and inflammatory-cell behavior. ANPEP and PAPSS2 could extend the program through peptide processing and sulfation-dependent regulation of extracellular or hormone-related signals. Under this model, the module reflects communication between tissue cells and infiltrating or resident phagocytic cells. This is a hypothesis generated from co-abundance and annotation convergence; the supplied data do not show causality, direct protein binding, or the direction of regulation.

### Important genes

#### ALDH1A3

- **Related proteins** (co-abundance neighbors): ANPEP (0.88), PAPSS2 (0.87), CD47 (0.82), ANXA1 (0.81), PRKCD (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Not detected in immune cells; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: aldehyde dehydrogenase 1 family member A3. This gene encodes an aldehyde dehydrogenase enzyme that uses retinal as a substrate. Mutations in this gene have been associated with microphthalmia, isolated 8, and expression changes have also been detected in tumor cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014].
- **Diseases (Open Targets)**: isolated anophthalmia-microphthalmia syndrome (0.803); microphthalmia (0.615); anophthalmia-microphthalmia syndrome (0.554); nanophthalmia (0.389); microphthalmia, isolated, with coloboma (0.385)
- **Europe PMC papers**: 3750
- **Why important**: ALDH1A3 is the central network hub, connecting to most other module members, and it is present in (GO:BP regulation of hormone levels; q_global = 0.0343). Its established enzymatic role in retinal conversion and retinoic acid biosynthesis gives the module a plausible metabolic axis. HPA places it in tissue-enhanced urogenital tissues and in stromal cell contexts, while its absence from immune cells argues against interpreting it solely as a blood marker. Its disease associations include microphthalmia-spectrum disorders, and its substantial literature supports a well-studied gene whose module role may nevertheless be context-dependent.
- **Conclusion**: Established evidence supports ALDH1A3 as the principal co-abundance organizer and a retinoid-metabolism marker. It is hypothesized, but not demonstrated, to coordinate the metabolic and phagocytic arms of this module.

#### ANXA1

- **Related proteins** (co-abundance neighbors): ALDH1A3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enriched; blood Immune cell enhanced; location Plasma membrane, Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: annexin A1. This gene encodes a membrane-localized protein that binds phospholipids. This protein inhibits phospholipase A2 and has anti-inflammatory activity. Loss of function or expression of this gene has been detected in multiple tumors. [provided by RefSeq, Dec 2014].
- **Diseases (Open Targets)**: schizophrenia (0.434); myopathy (0.413); type 1 diabetes mellitus (0.346); spinal cord injury (0.335); Abnormal nasolacrimal system morphology (0.327)
- **Europe PMC papers**: 9690
- **Why important**: ANXA1 participates in both globally corrected terms, (GO:BP phagocytosis; q_global = 0.00683) and (GO:BP regulation of hormone levels; q_global = 0.0343), and is connected directly to the central ALDH1A3 node. Its known phospholipid-binding, anti-inflammatory, leukocyte-migration, neutrophil-homeostasis, and phagocytosis-related functions make it the clearest bridge between tissue signaling and immune-interface biology. HPA identifies it as secreted to blood and associates it with esophageal and basophil-related contexts. It also has a large literature base and reported links to inflammatory and neurological disease areas.
- **Conclusion**: Established evidence makes ANXA1 a strong effector or marker of the phagocytic and inflammatory component. Its secreted status raises the possibility of extracellular signaling, but the module does not show whether ANXA1 drives or merely reflects the shared state.

#### CD47

- **Related proteins** (co-abundance neighbors): ALDH1A3 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: CD47 molecule. This gene encodes a membrane protein, which is involved in the increase in intracellular calcium concentration that occurs upon cell adhesion to extracellular matrix. The encoded protein is also a receptor for the C-terminal cell binding domain of thrombospondin, and it may play a role in membrane transport and signal transduction. This gene has broad tissue distribution, and is reduced in express…
- **Diseases (Open Targets)**: myelodysplastic syndrome (0.370); smoking initiation (0.341); Abnormality of refraction (0.295); hypothyroidism (0.280); systemic lupus erythematosus (0.279)
- **Europe PMC papers**: 20803
- **Why important**: CD47 is included in the globally corrected phagocytosis term (GO:BP phagocytosis; q_global = 0.00683) and is directly connected to ALDH1A3. As a broadly distributed plasma-membrane protein involved in adhesion, migration, signaling, and regulation of immune interactions, it is biologically suited to represent tissue-cell recognition at the immune interface. HPA shows low immune-cell specificity and an alveolar-cell association, which favors a general membrane-state interpretation rather than a strict blood-cell explanation. CD47 also has extensive literature and disease associations involving hematologic and immune disorders.
- **Conclusion**: Established evidence supports CD47 as a membrane recognition and adhesion component of the phagocytosis-associated signal. A role as the tissue-cell checkpoint linking ALDH1A3-associated state to phagocytic behavior remains a hypothesis.

#### ANPEP

- **Related proteins** (co-abundance neighbors): ALDH1A3 (0.88), DNM2 (0.80); STRING partners: none
- **HPA**: Group enriched; Cell type enriched; blood Immune cell enriched; location Plasma membrane; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: alanyl aminopeptidase, membrane. Aminopeptidase N is located in the small-intestinal and renal microvillar membrane, and also in other plasma membranes. In the small intestine aminopeptidase N plays a role in the final digestion of peptides generated from hydrolysis of proteins by gastric and pancreatic proteases. Its function in proximal tubular epithelial cells and other cell types is less clear. The large extracellular carboxy…
- **Diseases (Open Targets)**: cholelithiasis (0.520); gallstones (0.471); Self-injurious behavior (0.187); cesarean section (0.187); acute myeloid leukemia (0.138)
- **Europe PMC papers**: 2771
- **Why important**: ANPEP occurs in (GO:BP regulation of hormone levels; q_global = 0.0343) and connects ALDH1A3 to DNM2, giving it a position at the module's secondary membrane and endocytic branch. Its established function as a plasma-membrane aminopeptidase links peptide processing and angiotensin maturation to epithelial surface biology. HPA associates it with intestine, pancreas, enterocytes, and neutrophils, so it may report either epithelial differentiation or immune-cell admixture. Its disease associations include biliary and hematologic conditions, and it has a substantial literature.
- **Conclusion**: Established evidence supports ANPEP as a surface peptidase that connects hormone-related processing with epithelial or immune interfaces. Its precise contribution to the cervix-skin module is uncertain and could be compositional rather than mechanistic.

#### PRKCD

- **Related proteins** (co-abundance neighbors): ALDH1A3 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein kinase C delta. The protein encoded by this gene is a member of the protein kinase C family of serine- and threonine-specific protein kinases. The encoded protein is activated by diacylglycerol and is both a tumor suppressor and a positive regulator of cell cycle progression. Also, this protein can positively or negatively regulate apoptosis. Defects in this gene are a cause of autoimmune lymphoproliferative synd…
- **Diseases (Open Targets)**: autoimmune lymphoproliferative syndrome (0.685); acute myeloid leukemia (0.556); mast cell leukemia (0.475); systemic mastocytosis (0.471); mastocytosis (0.464)
- **Europe PMC papers**: 3335
- **Why important**: PRKCD is present in the globally corrected phagocytosis term (GO:BP phagocytosis; q_global = 0.00683) and is connected to the ALDH1A3 hub. As a protein kinase involved in phosphorylation, stress responses, apoptosis, and signal transduction, it provides a regulatory mechanism that could convert cellular stress or membrane signals into altered phagocytic behavior. HPA associates it with neutrophils, platelets, and late spermatids, while its disease associations include autoimmune lymphoproliferative and myeloid disorders. Its literature supports a well-established signaling role.
- **Conclusion**: Established evidence supports PRKCD as a signaling and stress regulator within the phagocytosis-associated arm. Its placement near the ALDH1A3 hub suggests coordination, but does not prove that PRKCD mediates the metabolic-to-phagocytic connection.

## Module 11

**Tissue pair**: cervix_uterine and skin  
**Genes (11)**: AP3B1, BICD2, DIAPH2, DYNC1H1, FASTKD2, NAA25, NLN, LARS2, TMF1, ATP6V1C1, VPS18

### Function

The module most plausibly represents a broad intracellular logistics and organelle-maintenance program rather than a sharply defined pathway. Its annotations converge on Golgi and vesicle trafficking, endosome and lysosome organization, microtubule-dependent transport, cytoskeletal organization, and mitochondrial RNA handling or translation. BICD2 and DYNC1H1 provide a particularly coherent dynein-dependent retrograde transport connection, while AP3B1, VPS18, and ATP6V1C1 point toward vesicle sorting, lysosomal or organelle biogenesis, and compartment acidification. NAA25, LARS2, FASTKD2, DIAPH2, TMF1, and NLN add protein acetylation, mitochondrial translation or RNA regulation, actin organization, Golgi trafficking, and proteolysis-related functions. No GO or KEGG term passed global correction, so the proposed function is an interpretation of the individual gene annotations and network structure, not evidence of significant pathway enrichment.

**Cell composition.** The module is not dominated by plasma or secreted proteins: the HPA summary reports no secreted genes. Most genes have low tissue specificity, are detected in both cervix_uterine and skin, and have intracellular locations such as the Golgi apparatus, cytosol, mitochondria, vesicles, or endoplasmic reticulum. Many genes are cell-type enhanced, including signals in neutrophils, neutrophil progenitors, epithelial cells, myonuclei, and other specialized cell types, but the blood-cell specificity is generally low. NLN is group-enriched in monocyte and myeloid dendritic-cell categories, whereas the module as a whole is not blood-cell specific. Thus, sample blood contamination is not the leading interpretation, although shared cellular composition or broadly expressed intracellular machinery could contribute to the conserved co-abundance pattern. BICD2 has skin-enriched expression and DYNC1H1 has brain-enriched expression, but these specialized signals do not establish a skin- or brain-specific module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The network contains a high-confidence STRING relationship between BICD2 and DYNC1H1, consistent with cargo-adaptor-mediated cytoplasmic dynein transport. No other module pair reaches the stated STRING confidence threshold, and no hu.MAP complex contains multiple module members. This supports a real mechanistic anchor around dynein-dependent transport, but argues against interpreting the entire module as a single established protein complex. The remaining co-abundance edges may reflect coordinated expression of related intracellular processes, indirect biological coupling, shared cell states, or technical covariance rather than documented physical interactions.

**STRING interactions (score >= 0.7)**: 1 of 55 gene pairs: BICD2–DYNC1H1 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The conserved co-abundance observation may be a new result for the cervix_uterine and skin tissue comparison, but the module cannot be claimed as a newly discovered molecular complex or pathway. Its genes and functions are individually well established, and the BICD2-DYNC1H1 relationship is already represented in STRING. The absence of a multi-member hu.MAP complex and the lack of broad STRING support indicate that the particular cross-tissue co-abundance grouping may be under-characterized, but absence from those resources alone does not prove novelty. The absence of globally significant GO or KEGG enrichment further means that novelty and biological coherence should be tested in independent cohorts, cell-composition analyses, and perturbation experiments.

**Hypothesis.** Hypothesis: in both cervix_uterine and skin, a shared population of viable cells coordinates intracellular trafficking and organelle quality control, producing co-abundance of dynein-cargo transport, Golgi and endolysosomal sorting, vacuolar acidification, cytoskeletal remodeling, and mitochondrial gene-expression machinery. BICD2-DYNC1H1 could organize the transport component, AP3B1 and VPS18 could support cargo sorting and late endosomal or lysosomal routing, and ATP6V1C1 could support acidification of those compartments. The mitochondrial genes and cytoskeletal genes may reflect the energetic and structural demands of this state. This is a mechanistic hypothesis, not a demonstrated causal model; the sparse physical-interaction evidence and lack of globally significant enrichment make validation essential.

### Important genes

#### BICD2

- **Related proteins** (co-abundance neighbors): AP3B1 (0.83), DYNC1H1 (0.82), TMF1 (0.81); STRING partners: DYNC1H1 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Plasma membrane, Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BICD cargo adaptor 2. This gene is one of two human homologs of Drosophila bicaudal-D and a member of the Bicoid family. It has been implicated in dynein-mediated, minus end-directed motility along microtubules. It has also been reported to be a phosphorylation target of NIMA related kinase 8. Two alternative splice variants have been described. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy with contractures (0.807); spinal muscular atrophy, lower extremity-predominant, 2B, prenatal onset, autosomal dominant (0.740); hereditary disease (0.478); neuronopathy, distal hereditary motor, autosomal dominant (0.460); arthrogryposis multiplex congenita (0.437)
- **Europe PMC papers**: 925
- **Why important**: BICD2 is a central network connector linking AP3B1, DYNC1H1, and TMF1, and it has the module's clearest functional bridge to microtubule-based retrograde transport and Golgi localization. Its high-confidence STRING relationship with DYNC1H1 is the strongest external interaction evidence. It is skin-enriched, detected in both tissues, and has substantial literature and disease evidence for motor-neuron and spinal-muscular disorders.
- **Conclusion**: Established evidence supports BICD2 as an adaptor for dynein-mediated intracellular transport and as a key organizational anchor of this module. It is plausible, but not proven, that BICD2 helps drive the conserved tissue-level co-abundance pattern.

#### DYNC1H1

- **Related proteins** (co-abundance neighbors): BICD2 (0.82); STRING partners: BICD2 (0.999)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: dynein cytoplasmic 1 heavy chain 1. Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polyp…
- **Diseases (Open Targets)**: autosomal dominant childhood-onset proximal spinal muscular atrophy without contractures (0.816); intellectual disability, autosomal dominant 13 (0.815); Charcot-Marie-Tooth disease axonal type 2O (0.799); autosomal dominant non-syndromic intellectual disability (0.634); hereditary disease (0.545)
- **Europe PMC papers**: 1731
- **Why important**: DYNC1H1 is the motor partner of BICD2 in the only high-confidence STRING interaction and is annotated for retrograde transport, organelle movement, cytoplasmic microtubule organization, and spindle-related functions. It is tissue-enhanced in brain, detected in both sampled tissues, has extensive literature, and is associated with several neurological and peripheral-neuropathy disorders.
- **Conclusion**: Established evidence identifies DYNC1H1 as the motor component of a dynein transport mechanism represented in the module. Its participation in a broader cervix_uterine and skin co-abundance program remains an association rather than a demonstrated tissue-specific mechanism.

#### AP3B1

- **Related proteins** (co-abundance neighbors): BICD2 (0.83), ATP6V1C1 (0.81), NAA25 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Vesicles; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: adaptor related protein complex 3 subunit beta 1. This gene encodes a protein that may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. The encoded protein is part of the heterotetrameric AP-3 protein complex which interacts with the scaffolding protein clathrin. Mutations in this gene are associated with Hermansky-Pudlak syndrome type 2. Two transcript variants encoding different isoforms h…
- **Diseases (Open Targets)**: Hermansky-Pudlak syndrome 2 (0.837); Hermansky-Pudlak syndrome (0.752); cancer (0.546); Parkinson disease (0.470); neurodegenerative disease (0.452)
- **Europe PMC papers**: 1324
- **Why important**: AP3B1 connects BICD2 with ATP6V1C1 and NAA25 and encodes a subunit of the AP-three adaptor complex involved in intracellular transport, lysosome-related organelle biogenesis, melanosomes, and platelet dense granules. Its association with Hermansky-Pudlak syndrome provides strong disease relevance, and it has substantial literature. Its vesicular localization fits the module's trafficking interpretation.
- **Conclusion**: Established evidence supports AP3B1 as a vesicle-sorting and organelle-biogenesis component that could connect transport with specialized organelles. The module does not establish that AP3B1 is responsible for the cross-tissue co-abundance or for a shared pigment or platelet-related process.

#### VPS18

- **Related proteins** (co-abundance neighbors): NAA25 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: VPS18 core subunit of CORVET and HOPS complexes. Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene encodes the human homolog of yeast class C Vps18 protein. The mammalian class C Vps proteins are predominantly associated with late…
- **Diseases (Open Targets)**: neurodegenerative disease (0.541); COVID-19 (0.372); male infertility (0.190); neoplasm (0.091); ulcerative colitis (0.062)
- **Europe PMC papers**: 802
- **Why important**: VPS18 links NAA25 to the CORVET and HOPS vesicle-tethering systems and is annotated for endosome organization, lysosome organization, and intracellular protein transport. It is detected in both tissues and has disease associations involving neurodegeneration, infection, infertility, and neoplasm. Although its direct network connectivity is limited, its function provides an important late-endosomal and lysosomal complement to AP3B1 and ATP6V1C1.
- **Conclusion**: Established evidence supports VPS18 as a component of endolysosomal trafficking machinery. Its inclusion supports a coordinated organelle-trafficking interpretation, but the co-abundance data do not demonstrate a physical VPS18 complex within this module.

#### NAA25

- **Related proteins** (co-abundance neighbors): VPS18 (0.84), NLN (0.82), LARS2 (0.81), AP3B1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Golgi apparatus, Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-alpha-acetyltransferase 25, NatB auxiliary subunit. This gene encodes the auxiliary subunit of the heteromeric N-terminal acetyltransferase B complex. This complex acetylates methionine residues that are followed by acidic or asparagine residues.[provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: angina pectoris (0.223); colorectal cancer (0.201); alcohol drinking (0.166); type 1 diabetes mellitus (0.158); ischemic stroke (0.140)
- **Europe PMC papers**: 277
- **Why important**: NAA25 has the strongest network connectivity in the module and links VPS18, NLN, LARS2, and AP3B1. It encodes the auxiliary subunit of the NatB N-terminal acetyltransferase complex and is annotated for cytoskeleton organization. Its broad tissue detection and substantial literature make it a potential expression-level scaffold connecting general protein maturation with trafficking and cytoskeletal processes.
- **Conclusion**: Established evidence supports NAA25 as a broadly acting protein-acetylation factor with a prominent position in this co-abundance graph. Its role as a functional coordinator of the module is a hypothesis based on network position, not a demonstrated biochemical role in the proposed tissue program.

## Module 12

**Tissue pair**: cervix_uterine and skin  
**Genes (6)**: NUDT2, HMMR, HS2ST1, CAMK2G, SAP30BP, STK3

### Function

No GO or KEGG term passed global correction, and there are no supplementary STRING enrichment terms. Therefore, the module does not support a specific pathway-level functional assignment. Its genes instead span intracellular nucleotide turnover, calcium-dependent kinase signaling, apoptosis and Hippo-related regulation, cell motility and microtubule biology, transcriptional and chromatin regulation, antiviral response, and heparan-sulfate biosynthesis. The co-abundance pattern is therefore best interpreted as a possible shared cellular-state or regulatory module rather than an established biochemical pathway. The network topology places NUDT2 as the main connector, with linked relationships involving CAMK2G, STK3, SAP30BP, HMMR, and HS2ST1.

**Cell composition.** This is not a plasma-protein or secreted-protein module: all listed genes are annotated as non-secreted. Most genes have low tissue specificity and low immune-cell specificity, arguing against a uniformly blood-cell-derived or tissue-exclusive signature. However, several genes show cell-type-enhanced patterns, including signals involving cytotrophoblasts, astrocytes, neutrophils, eosinophils, T-reg cells, and germ-cell populations. HMMR is tissue-enhanced in bone marrow, lymphoid tissue, and testis, while CAMK2G is immune-cell-enhanced in eosinophils. Thus, contamination by circulating plasma proteins is unlikely, but shared or variable cell-state composition remains a plausible contributor. Protein detection is broadly present in both cervix and skin, with slightly less complete detection in cervix.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

No module pair reaches the reported high-confidence STRING interaction threshold, and no STRING functional enrichment is reported. No hu.MAP complex contains multiple module members. Consequently, the co-abundance edges should not be interpreted as established direct protein interactions or as a known multiprotein complex. The observed network may reflect coordinated expression, indirect regulation, shared cell composition, or technical and biological covariation. NUDT2 is the topological connector, whereas SAP30BP-HS2ST1 forms a peripheral relationship and CAMK2G-HMMR-STK3 forms another connected segment.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

The cross-tissue co-abundance pattern is potentially novel because the module has no matching high-confidence STRING interactions, no multi-member hu.MAP complex, and no globally significant GO or KEGG annotation. Nevertheless, these absences do not establish biological novelty: known relationships may be context-dependent, below database thresholds, indirect, or expressed through cell composition rather than physical binding. The defensible conclusion is that this is a newly observed, hypothesis-generating co-abundance module whose biological interpretation requires validation in independent cohorts, cell-resolved data, and perturbation experiments.

**Hypothesis.** Hypothesis: the module may represent a shared tissue-remodeling and stress-response state in cervix and skin. In this model, HS2ST1 could alter heparan-sulfate signaling environments, HMMR could connect extracellular-matrix-associated motility cues with microtubule behavior, CAMK2G could relay calcium-dependent signals, and STK3 could couple those signals to growth suppression or apoptotic regulation. NUDT2 may reflect nucleotide and oxidative-stress homeostasis, while SAP30BP may influence transcriptional, splicing, chromatin, or antiviral responses. The co-abundance pattern could therefore arise from coordinated remodeling, differentiation, or stress signaling rather than a stable physical complex. This is a hypothesis, not a demonstrated mechanism.

### Important genes

#### NUDT2

- **Related proteins** (co-abundance neighbors): CAMK2G (0.83), STK3 (0.83), SAP30BP (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nudix hydrolase 2. This gene encodes a member of the MutT family of nucleotide pyrophosphatases, a subset of the larger NUDIX hydrolase family. The gene product possesses a modification of the MutT sequence motif found in certain nucleotide pyrophosphatases. The enzyme asymmetrically hydrolyzes Ap4A to yield AMP and ATP and is responsible for maintaining the intracellular level of the dinucleotide Ap4A, the function…
- **Diseases (Open Targets)**: intellectual developmental disorder with or without peripheral neuropathy (0.665); Intellectual disability (0.456); polyneuropathy (0.372); Global developmental delay (0.371); developmental disability (0.370)
- **Europe PMC papers**: 328
- **Why important**: NUDT2 is the principal network connector, linking CAMK2G, STK3, and SAP30BP. Its encoded Nudix-family enzyme regulates intracellular Ap4A by hydrolyzing it to AMP and ATP, providing a plausible connection to nucleotide balance, apoptosis, and oxidative-stress responses. It has a moderate literature base and disease associations involving intellectual disability, developmental delay, and peripheral neuropathy.
- **Conclusion**: Established evidence supports NUDT2 as a nucleotide-homeostasis enzyme and as the central co-abundance connector. It is a strong candidate for coordinating metabolic and stress-related aspects of the module. Whether its network centrality reflects causal regulation or merely shared expression remains unresolved.

#### STK3

- **Related proteins** (co-abundance neighbors): NUDT2 (0.83), HMMR (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Intermediate filaments, Rods & Rings; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine/threonine kinase 3. This gene encodes a serine/threonine protein kinase activated by proapoptotic molecules indicating the encoded protein functions as a growth suppressor. Cleavage of the protein product by caspase removes the inhibitory C-terminal portion. The N-terminal portion is transported to the nucleus where it homodimerizes to form the active kinase which promotes the condensation of chromatin during apoptos…
- **Diseases (Open Targets)**: benign prostatic hyperplasia (0.254); Alzheimer disease (0.222); hypotensive disorder (0.175); placenta praevia (0.175); esophageal squamous cell carcinoma (0.083)
- **Europe PMC papers**: 10406
- **Why important**: STK3 is connected to NUDT2 and HMMR and has the most extensive literature support among the module genes. It encodes a serine/threonine kinase associated with apoptosis, nuclear import, gene-expression regulation, and Hippo signaling. Its disease associations include several tissue and neurological conditions, although the reported associations are not specific evidence for this module.
- **Conclusion**: Established evidence supports STK3 as a regulatory kinase with roles in growth suppression and apoptosis. Its position between the nucleotide-related NUDT2 signal and the motility-related HMMR signal makes it a plausible signaling integrator. A module-specific STK3 mechanism is still a hypothesis because no direct interaction or enrichment evidence is present.

#### HMMR

- **Related proteins** (co-abundance neighbors): CAMK2G (0.88), STK3 (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Microtubules; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: hyaluronan mediated motility receptor. The protein encoded by this gene is involved in cell motility. It is expressed in breast tissue and together with other proteins, it forms a complex with BRCA1 and BRCA2, thus is potentially associated with higher risk of breast cancer. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Dec 2008].
- **Diseases (Open Targets)**: ovarian cancer (0.342); thyroid gland carcinoma (0.306); alcohol drinking (0.298); Alzheimer disease (0.279); Parkinson disease (0.279)
- **Europe PMC papers**: 2289
- **Why important**: HMMR is connected to CAMK2G and STK3 and is the clearest tissue- and cell-state-linked gene in the module, with enhancement in bone marrow, lymphoid tissue, testis, cytotrophoblasts, germ-cell populations, enteric transient amplifying cells, and T-reg cells. Its established functions involve cell motility, hyaluronan-related biology, receptor-mediated endocytosis, and microtubule localization. It has a substantial literature base and disease associations spanning cancer and neurodegenerative conditions.
- **Conclusion**: Established evidence supports HMMR as a motility and cytoskeletal regulator with strong cell-state associations. It may be especially informative for determining whether the shared module reflects remodeling or differing cell composition. The data do not establish that HMMR physically connects the other module members.

#### CAMK2G

- **Related proteins** (co-abundance neighbors): HMMR (0.88), NUDT2 (0.83); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Plasma membrane, Primary cilium tip, Primary cilium transition zone, Principal piece; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: calcium/calmodulin dependent protein kinase II gamma. The product of this gene is one of the four subunits of an enzyme which belongs to the serine/threonine protein kinase family, and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. Calcium signaling is crucial for several aspects of plasticity at glutamatergic synapses. In mammalian cells the enzyme is composed of four different chains: alpha, beta, gamma, and delta. The product of this…
- **Diseases (Open Targets)**: intellectual developmental disorder 59 (0.643); psoriasis (0.454); Severe intellectual disability (0.399); dengue disease (0.370); psoriasis vulgaris (0.345)
- **Europe PMC papers**: 1587
- **Why important**: CAMK2G links HMMR with NUDT2 and encodes a calcium/calmodulin-dependent serine/threonine kinase. Its annotations include calcium transport, neuronal plasticity, neuronal projection development, skeletal-muscle adaptation, and insulin secretion. It has a substantial literature base and disease associations involving intellectual disability and psoriasis. HPA identifies cell-type enhancement across several neural, epithelial, and immune-related populations, including eosinophils.
- **Conclusion**: Established evidence supports CAMK2G as a calcium-responsive signaling regulator with broad cell-type expression. It could provide a signaling bridge between tissue remodeling and intracellular stress responses. The module does not demonstrate that calcium signaling is globally enriched, so this interpretation remains provisional.

#### HS2ST1

- **Related proteins** (co-abundance neighbors): SAP30BP (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: heparan sulfate 2-O-sulfotransferase 1. Heparan sulfate biosynthetic enzymes are key components in generating a myriad of distinct heparan sulfate fine structures that carry out multiple biologic activities. This gene encodes a member of the heparan sulfate biosynthetic enzyme family that transfers sulfate to the 2 position of the iduronic acid residue of heparan sulfate. The disruption of this gene resulted in no kidney formation in kn…
- **Diseases (Open Targets)**: neurofacioskeletal syndrome with or without renal agenesis (0.712); Intellectual disability (0.528); multiple congenital anomalies/dysmorphic syndrome-intellectual disability (0.378); arthrogryposis (0.370); developmental disability (0.370)
- **Europe PMC papers**: 501
- **Why important**: HS2ST1 is the module's connection to extracellular-matrix and glycan signaling, through heparan-sulfate biosynthesis. It is linked to SAP30BP in the co-abundance graph and has cell-type-enhanced expression in adrenal cortex cells, astrocytes, and choroid plexus epithelial cells. Its disease associations include neurofacioskeletal syndrome with or without renal agenesis, intellectual disability, and developmental abnormalities. Its literature base is smaller than that of STK3 or HMMR but sufficient to support a defined developmental and glycan-biology role.
- **Conclusion**: Established evidence supports HS2ST1 as a heparan-sulfate patterning enzyme with developmental importance. It could influence local signaling environments in skin and cervix, but the current evidence does not show that its glycan products drive the entire module.

#### SAP30BP

- **Related proteins** (co-abundance neighbors): NUDT2 (0.81), HS2ST1 (0.80); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SAP30 binding protein. Involved in modulation by host of symbiont transcription; positive regulation of histone deacetylation; and response to virus. Located in intermediate filament cytoskeleton and nucleoplasm. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.442); rotator cuff syndrome (0.099); ovarian dysfunction (0.085); Diamond-Blackfan anemia (0.085); Paralysis (0.083)
- **Europe PMC papers**: 179
- **Why important**: SAP30BP is connected to NUDT2 and HS2ST1 and is annotated in transcriptional regulation, mRNA splicing, histone deacetylation, and antiviral response. Its nucleoplasmic localization and association with intermediate-filament structures provide a possible regulatory link between gene control and cellular architecture. It has a more limited literature base than the best-studied module genes and reported associations including neurodegenerative disease and hematological or developmental conditions.
- **Conclusion**: Established evidence supports SAP30BP as a candidate transcriptional and stress-response regulator. Its position may indicate coordinated regulation of gene expression rather than direct pathway membership. The proposed connection to HS2ST1 or NUDT2 is a co-abundance hypothesis, not an established molecular interaction.

## Module 13

**Tissue pair**: cervix_uterine and skin  
**Genes (8)**: ASAH1, IDH3A, KRT10, KRT1, RAP2B, RAB27A, STX7, TSPO

### Function

The module has no GO or KEGG term passing global correction, so its function cannot be assigned from statistically significant pathway enrichment. Its gene-level evidence suggests a mixed epithelial maintenance and intracellular trafficking program. KRT1 and KRT10 support keratinocyte differentiation, keratinization, epidermal development, and intermediate-filament organization. ASAH1 supports lysosomal sphingolipid and ceramide metabolism, while RAB27A and STX7 support vesicle transport, exocytosis, endolysosomal fusion, and protein trafficking. RAP2B adds small-GTPase and platelet-related signaling, TSPO adds mitochondrial steroidogenic and heme-related functions, and IDH3A adds mitochondrial tricarboxylic-acid-cycle metabolism. The network therefore most plausibly reflects epithelial structural differentiation coupled to vesicle, lysosomal, lipid, and mitochondrial processes, rather than a single established pathway. These interpretations are gene-level and mechanistic hypotheses, not globally significant enrichment results.

**Cell composition.** The module is not predominantly a plasma or secreted-protein module: only a minority of its genes are classified as secreted, and several members are intracellular or membrane-associated. It is also not a simple broadly expressed housekeeping module. HPA evidence strongly supports an epithelial component, especially suprabasal keratinocytes and skin, through KRT1 and KRT10, with KRT1 detected in both tissues and KRT10 showing skin enrichment. At the same time, the module has a substantial immune and blood-cell signal: STX7 is group enriched across several myeloid and lymphoid populations, while RAB27A, ASAH1, TSPO, IDH3A, and other members show enrichment or enhancement in neutrophil-lineage, monocyte, dendritic-cell, platelet, or related cell types. The shared cervix and skin signal may therefore reflect epithelial differentiation and vesicle biology, but it could also be influenced by shared immune-cell content, tissue admixture, or coordinated epithelial and immune states.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The only high-confidence STRING relationship among module members is the KRT1-KRT10 pair, which is biologically coherent because these are paired type II and type I keratins in differentiated stratified epithelium. No other listed pair has a reported high-confidence STRING interaction in the supplied data, and no STRING functional-enrichment result is available. No hu.MAP complex contains multiple module members. Thus, the co-abundance network extends beyond currently catalogued physical interactions, with the KRT1-KRT10 edge providing the clearest established molecular anchor while the remaining edges should be interpreted as coordinated expression relationships rather than proven direct binding or membership in one complex.

**STRING interactions (score >= 0.7)**: 1 of 28 gene pairs: KRT1–KRT10 (0.999)
**hu.MAP 3.0 complexes with >= 2 module members**: none

### Novelty

This module can be considered a potentially interesting co-abundance pattern, but it cannot be called a newly discovered biological mechanism from the supplied evidence alone. The lack of globally significant GO or KEGG enrichment, the absence of STRING enrichment, the absence of a multi-member hu.MAP complex, and the limited STRING support argue against a previously established unified pathway. However, absence from STRING or hu.MAP does not prove novelty: these resources emphasize curated or experimentally supported relationships and may not capture tissue-specific co-abundance, cell-composition effects, indirect regulation, or context-dependent coordination. The most defensible conclusion is that the cross-tissue co-abundance pattern is a candidate observation requiring replication and orthogonal validation, not proof of a novel complex or pathway.

**Hypothesis.** Hypothesis: a shared differentiated epithelial state in cervix and skin increases keratin-pair expression while coordinating membrane traffic, lysosomal lipid turnover, and mitochondrial metabolism. In this model, KRT1-KRT10 marks the structural epithelial component; RAB27A and STX7 organize vesicle and endolysosomal trafficking; ASAH1 adjusts ceramide metabolism; and TSPO and IDH3A reflect mitochondrial metabolic support. RAP2B may connect this state to signaling or platelet-associated biology. An alternative, not mutually exclusive explanation is that the apparent module combines epithelial differentiation with variable immune-cell or platelet admixture. Testing these alternatives would require cell-resolved data, replication across cohorts, and perturbation or protein-level validation.

### Important genes

#### KRT1

- **Related proteins** (co-abundance neighbors): KRT10 (0.88); STRING partners: KRT10 (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Immune cell enhanced; location None; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 1. The protein encoded by this gene is a member of the keratin gene family. The type II cytokeratins consist of basic or neutral proteins which are arranged in pairs of heterotypic keratin chains coexpressed during differentiation of simple and stratified epithelial tissues. This type II cytokeratin is specifically expressed in the spinous and granular layers of the epidermis with family member KRT10…
- **Diseases (Open Targets)**: epidermolytic ichthyosis (0.846); diffuse nonepidermolytic palmoplantar keratoderma (0.714); ichthyosis hystrix of Curth-Macklin (0.681); epidermolytic palmoplantar keratoderma, 1 (0.674); annular epidermolytic ichthyosis (0.621)
- **Europe PMC papers**: 8548
- **Why important**: KRT1 is a central epithelial anchor in the module through its coherent pairing with KRT10 and its skin and suprabasal-keratinocyte enrichment. It has the largest literature volume among the module genes, strong disease associations with inherited keratinization disorders, and annotations for keratinization, intermediate-filament organization, oxidative-stress response, and epithelial structure.
- **Conclusion**: Established evidence supports KRT1 as a structural marker of differentiated stratified epithelium and as the best-supported epithelial context marker in this module. Its role as a driver of the entire shared co-abundance program remains a hypothesis.

#### KRT10

- **Related proteins** (co-abundance neighbors): KRT1 (0.88), RAP2B (0.84), RAB27A (0.82); STRING partners: KRT1 (0.999)
- **HPA**: Tissue enriched; Cell type enriched; blood Low immune cell specificity; location None; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: keratin 10. This gene encodes a member of the type I (acidic) cytokeratin family, which belongs to the superfamily of intermediate filament (IF) proteins. Keratins are heteropolymeric structural proteins which form the intermediate filament. These filaments, along with actin microfilaments and microtubules, compose the cytoskeleton of epithelial cells. Mutations in this gene are associated with epidermolytic …
- **Diseases (Open Targets)**: epidermolytic hyperkeratosis 2A, autosomal dominant (0.787); epidermolytic ichthyosis (0.772); congenital reticular ichthyosiform erythroderma (0.727); ichthyosis, annular epidermolytic 1 (0.647); annular epidermolytic ichthyosis (0.642)
- **Europe PMC papers**: 2736
- **Why important**: KRT10 is the strongest network-connected gene in the supplied subgraph and forms the sole high-confidence STRING pair with KRT1. Its tissue and cell-type annotations specifically identify skin and suprabasal keratinocytes, while its functions include keratinocyte differentiation, cornification, epidermal development, and intermediate-filament organization. Its disease associations provide functional support for the importance of keratin integrity.
- **Conclusion**: Established evidence supports KRT10 as a differentiated epithelial and epidermal-keratinization marker tightly linked to KRT1. Its connections to RAP2B and RAB27A are co-abundance associations in this dataset, not established physical interactions.

#### RAB27A

- **Related proteins** (co-abundance neighbors): ASAH1 (0.84), KRT10 (0.82), IDH3A (0.81); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Mid piece, Principal piece; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RAB27A, member RAS oncogene family. The protein encoded by this gene belongs to the small GTPase superfamily, Rab family. The protein is membrane-bound and may be involved in protein transport and small GTPase mediated signal transduction. Mutations in this gene are associated with Griscelli syndrome type 2. Alternative splicing occurs at this locus and four transcript variants encoding the same protein have been identified. [provid…
- **Diseases (Open Targets)**: Griscelli syndrome type 2 (0.812); Griscelli syndrome (0.749); autoinflammatory syndrome (0.499); hereditary disease (0.450); acrocephalopolydactyly (0.370)
- **Europe PMC papers**: 5437
- **Why important**: RAB27A is highly connected within the co-abundance subgraph and links the keratin-associated branch to ASAH1 and IDH3A. It is a Rab-family small GTPase with established roles in protein transport, exocytosis, melanosome transport, and antigen processing, and it has strong disease relevance through Griscelli syndrome and related disorders. HPA also links it to neutrophil-related and basophil-associated cell states.
- **Conclusion**: Established evidence supports RAB27A as a vesicle-trafficking regulator and a plausible bridge between epithelial secretory biology and immune-cell biology. Whether it mechanistically couples keratinization to the other module processes is a hypothesis.

#### ASAH1

- **Related proteins** (co-abundance neighbors): STX7 (0.89), RAB27A (0.84); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: N-acylsphingosine amidohydrolase 1. This gene encodes a member of the acid ceramidase family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed. Processing of this preproprotein generates alpha and beta subunits that heterodimerize to form the mature lysosomal enzyme, which catalyzes the degradation of ceramide into sphingosine an…
- **Diseases (Open Targets)**: Farber lipogranulomatosis (0.838); spinal muscular atrophy-progressive myoclonic epilepsy syndrome (0.806); ASAH1-related sphingolipidosis (0.600); atrial fibrillation (0.557); hydrops fetalis (0.467)
- **Europe PMC papers**: 2292
- **Why important**: ASAH1 connects the vesicle-trafficking branch through STX7 and RAB27A and is detected in both tissues. It encodes acid ceramidase, linking lysosomal ceramide degradation to sphingolipid metabolism and keratinocyte differentiation. Its disease associations include Farber lipogranulomatosis and ASAH1-related sphingolipidosis, and its literature supports a substantial biological knowledge base.
- **Conclusion**: Established evidence supports ASAH1 as a lysosomal sphingolipid-metabolism enzyme with relevance to epithelial differentiation and disease. Its coordinated expression with the keratin and trafficking genes suggests a possible lipid-trafficking connection, but the module does not establish causality.

#### STX7

- **Related proteins** (co-abundance neighbors): ASAH1 (0.89); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Group enriched; location Lysosomes; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: syntaxin 7. The protein encoded by this gene is a syntaxin family membrane receptor involved in vesicle transport. The encoded protein binds alpha-SNAP, an important regulator of transport vesicle fusion. Along with syntaxin 13, this protein plays a role in the ordered fusion of endosomes and lysosomes with the phagosome. [provided by RefSeq, May 2016].
- **Diseases (Open Targets)**: neurodegenerative disease (0.489); Abnormality of neuronal migration (0.259); Raynaud disease (0.180); placental abruption (0.166); aortic stenosis (0.081)
- **Europe PMC papers**: 701
- **Why important**: STX7 is the module's direct network link to ASAH1 and encodes a lysosomal syntaxin involved in vesicle fusion, intracellular transport, and ordered endosome, lysosome, and phagosome fusion. HPA shows detection in both tissues and broad enrichment across immune-cell populations, making it important for interpreting the module's possible immune-cell contribution.
- **Conclusion**: Established evidence supports STX7 as an endolysosomal vesicle-fusion factor and as a marker compatible with immune-cell activity. Its position may indicate coordination between lysosomal lipid metabolism and trafficking, but that connection is a hypothesis rather than a demonstrated complex.

#### TSPO

- **Related proteins** (co-abundance neighbors): RAP2B (0.82); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: translocator protein. Present mainly in the mitochondrial compartment of peripheral tissues, the protein encoded by this gene interacts with some benzodiazepines and has different affinities than its endogenous counterpart. The protein is a key factor in the flow of cholesterol into mitochondria to permit the initiation of steroid hormone synthesis. Alternatively spliced transcript variants have been reported; one of t…
- **Diseases (Open Targets)**: neurodegenerative disease (0.455); Alzheimer disease (0.396); anxiety disorder (0.391); Parkinson disease (0.385); lysosomal storage disease (0.358)
- **Europe PMC papers**: 5321
- **Why important**: TSPO links the module to a mitochondrial compartment and is detected in both tissues. Its annotations concern cholesterol transport into mitochondria, steroid-hormone biosynthesis, heme biosynthesis, and ion transport. It also has substantial literature and disease associations, although its network support within this module is limited to the RAP2B edge.
- **Conclusion**: Established evidence supports TSPO as a mitochondrial and cholesterol-transport-related protein. Its inclusion may reflect metabolic support for epithelial or immune-cell states, but a specific TSPO-mediated mechanism in this module is not established.

## Module 14

**Tissue pair**: cervix_uterine and skin  
**Genes (21)**: ATG7, CDK12, EIF2AK4, GET3, GSK3B, CAMK2D, PRKD2, PRKCI, LRRFIP2, MAP2K6, ACP2, RBMXL1, SASH1, SMG1, SRPK2, STK38L, TRAP1, VWA8, WDR62, WFS1, XRCC4

### Function

The strongest interpretation is a conserved intracellular protein-phosphorylation and kinase-regulatory module. The primary evidence is the globally corrected enrichment for protein serine kinase activity (GO:MF protein serine kinase activity; q_global = 3.1e-05), protein serine/threonine kinase activity (GO:MF protein serine/threonine kinase activity; q_global = 8.2e-05), protein kinase activity (GO:MF protein kinase activity; q_global = 0.000235), protein phosphorylation (GO:BP protein phosphorylation; q_global = 0.000339), protein autophosphorylation (GO:BP protein autophosphorylation; q_global = 0.00114), and broader protein modification (GO:BP protein modification process; q_global = 0.00482). The kinase genes include CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SMG1, SRPK2, and STK38L. The module also contains genes compatible with stress adaptation, autophagy, RNA processing, translation control, DNA repair, membrane-protein insertion, and mitochondrial proteostasis. These additional processes should be viewed as biological context rather than as equally established module functions. The STRING enrichment independently supports a serine/threonine-kinase and phosphorylation signature (4 supplementary STRING terms; within-query FDR 3.42e-06–0.00089), but STRING results are supplementary and do not replace the global GO correction.

**Cell composition.** This is not a plasma-protein or secreted-protein module: the HPA summary reports no secreted genes. Most genes have low tissue specificity, and nearly all have some cell-type-enhanced annotation. Neutrophils and neutrophil progenitors are recurring cell-type annotations, with additional signals involving monocytes, plasmacytoid dendritic cells, myonuclei, germ-cell populations, and epithelial or endothelial populations. Thus the shared cervix and skin signal may partly reflect broadly expressed intracellular machinery and shared cell types, with a possible contribution from immune-cell composition, rather than a tissue-specific secretory program. Protein detection is broadly compatible with the module in both tissues, although WDR62, SRPK2, CAMK2D, and PRKD2 show tissue-specific detection limitations in the supplied HPA evidence. The HPA information therefore supports biological presence in the tissues but does not establish that every gene is expressed in the same cell type or that the co-abundance relationship is cell-autonomous.

**GO/KEGG enrichment**: 15 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF protein serine kinase activity | 3.1e-05 | CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SMG1, SRPK2, STK38L |
| GO:MF protein serine/threonine kinase activity | 8.2e-05 | CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SMG1, SRPK2, STK38L |
| GO:MF protein kinase activity | 0.000235 | CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SMG1, SRPK2, STK38L |
| GO:BP protein phosphorylation | 0.000339 | CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SASH1, SMG1, SRPK2, STK38L |
| GO:BP phosphorylation | 0.000715 | CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SASH1, SMG1, SRPK2, STK38L |
| GO:BP protein autophosphorylation | 0.00114 | CAMK2D, CDK12, EIF2AK4, GSK3B, PRKD2, SMG1 |
| GO:MF phosphotransferase activity, alcohol group as acceptor | 0.00137 | CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SMG1, SRPK2, STK38L |
| GO:MF kinase activity | 0.00381 | CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SMG1, SRPK2, STK38L |
| GO:BP protein modification process | 0.00482 | ATG7, CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SASH1, SMG1, SRPK2, STK38L, WFS1 |
| GO:BP macromolecule modification | 0.0122 | ATG7, CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SASH1, SMG1, SRPK2, STK38L, WFS1 |
| GO:MF transferase activity, transferring phosphorus-containing groups | 0.0131 | CAMK2D, CDK12, EIF2AK4, GSK3B, MAP2K6, PRKCI, PRKD2, SMG1, SRPK2, STK38L |
| GO:BP peptidyl-serine phosphorylation | 0.0177 | CAMK2D, GSK3B, PRKD2, SMG1, SRPK2 |
| GO:BP peptidyl-serine modification | 0.0177 | CAMK2D, GSK3B, PRKD2, SMG1, SRPK2 |
| GO:MF ATP binding | 0.0322 | CAMK2D, CDK12, EIF2AK4, GET3, GSK3B, MAP2K6, PRKCI, PRKD2, SMG1, SRPK2, STK38L, TRAP1, VWA8 |
| GO:MF adenyl ribonucleotide binding | 0.0331 | CAMK2D, CDK12, EIF2AK4, GET3, GSK3B, MAP2K6, PRKCI, PRKD2, SMG1, SRPK2, STK38L, TRAP1, VWA8 |

### STRING and hu.MAP

No module gene pair reaches the supplied high-confidence STRING interaction threshold. Therefore the co-abundance edges are not supported as pre-existing high-confidence physical or functional STRING interactions, and the module should not be described as a known protein complex. STRING functional enrichment nevertheless reproduces the kinase and phosphorylation theme (4 supplementary STRING terms; within-query FDR 3.42e-06–0.00089), which supports convergence of annotation without proving direct interaction among the module proteins. hu.MAP provides a more specific relationship between CDK12 and SRPK2 in a high-confidence two-member complex (hu.MAP huMAP3_03314.1). The same pair occurs among a much larger RNA-processing and splicing complex (hu.MAP huMAP3_09621.1). This suggests a plausible connection between phosphorylation and RNA-processing machinery, while the limited overlap with the large complex means that hu.MAP does not explain the whole module.

**STRING interactions (score >= 0.7)**: 0 of 210 gene pairs.
**STRING functional enrichment (supplementary, within-query FDR)**: Keyword Serine/threonine-protein kinase (FDR = 3.42e-06, 10 genes); Function Protein serine kinase activity (FDR = 5.84e-06, 10 genes); Function Protein serine/threonine kinase activity (FDR = 1.11e-05, 10 genes); InterPro Serine/threonine-protein kinase, active site (FDR = 1.54e-05, 9 genes); InterPro Protein kinase-like domain superfamily (FDR = 1.54e-05, 10 genes); InterPro Protein kinase, ATP binding site (FDR = 1.54e-05, 9 genes); InterPro Protein kinase domain (FDR = 3.5e-05, 9 genes); SMART Serine/Threonine protein kinases, catalytic domain (FDR = 0.00052, 7 genes); Process Protein phosphorylation (FDR = 0.00089, 10 genes); Keyword ATP-binding (FDR = 0.00092, 13 genes); Process Peptidyl-serine phosphorylation (FDR = 0.0014, 7 genes); Function ATP binding (FDR = 0.0018, 13 genes); Process Protein autophosphorylation (FDR = 0.003, 6 genes); Function Catalytic activity, acting on a protein (FDR = 0.0053, 11 genes); Function Protein kinase C activity (FDR = 0.0145, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_03314.1 (SRPK2, CDK12; 2/2); huMAP3_09621.1 (SRPK2, CDK12; 2/56)

### Novelty

The module may represent a new tissue-pair co-abundance observation, but it is not a new discovery of kinase biology. Its central functions are well established through the globally corrected GO terms, the convergent STRING annotations, the known functions of several member genes, and the CDK12–SRPK2 hu.MAP relationship. The absence of high-confidence STRING edges and the limited hu.MAP overlap indicate that this particular cross-tissue co-abundance organization is not already represented as a single canonical interaction complex. However, absence from those resources alone cannot establish novelty. A defensible novelty claim would require comparison with published co-expression modules, tissue-pair analyses, and independent datasets, followed by replication and cell-composition adjustment. At present, the strongest claim is that the shared cervix–skin organization and its possible relationship to immune or epithelial cell composition are potentially novel, whereas the underlying kinase functions are established.

**Hypothesis.** Hypothesis: this module captures a shared stress-responsive intracellular program in cervix and skin, combining serine/threonine kinase signaling with RNA surveillance and processing, translation control, autophagy, membrane-protein handling, and cellular stress protection. MAP2K6, PRKCI, PRKD2, GSK3B, CAMK2D, STK38L, and EIF2AK4 could integrate inflammatory, calcium, metabolic, and environmental stress signals; CDK12, SRPK2, and SMG1 could couple those signals to transcription, splicing, and messenger-RNA quality control; ATG7, TRAP1, GET3, WFS1, and ACP2 could support proteostasis, organelle function, or degradation pathways. A nonexclusive alternative is that the apparent shared program is driven substantially by common immune or epithelial cell fractions. Testing this hypothesis requires cell-resolved expression, perturbation of the proposed kinase nodes, and replication in independent cervix and skin cohorts.

### Important genes

#### STK38L

- **Related proteins** (co-abundance neighbors): TRAP1 (0.83), GET3 (0.82), GSK3B (0.82), CAMK2D (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: serine/threonine kinase 38 like. Enables ATP binding activity; magnesium ion binding activity; and protein serine/threonine kinase activity. Involved in intracellular signal transduction. Acts upstream of or within protein phosphorylation. Located in cytosol. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: Alzheimer disease (0.268); Parkinson disease (0.268); neurodegenerative disease (0.268); lysosomal storage disease (0.268); pulmonary vascular congestion (0.205)
- **Europe PMC papers**: 498
- **Why important**: STK38L is the most central node by the supplied network ranking and connects to TRAP1, GET3, GSK3B, and CAMK2D. It is included in the primary kinase and phosphorylation evidence (5 globally significant GO/KEGG terms, q_global 3.1e-05–0.00482; see the table) and in the convergent STRING kinase evidence (STRING Keyword Serine/threonine-protein kinase; within-query FDR = 3.42e-06) (STRING Function Protein serine kinase activity; within-query FDR = 5.84e-06) (STRING Process Protein phosphorylation; within-query FDR = 0.00089). Its HPA profile is compatible with both tissues and highlights vascular and neutrophil-related cell contexts. Its literature volume is substantial enough to support a recognized signaling role, while its absence from the supplied STRING and hu.MAP relationships leaves the specific module placement open.
- **Conclusion**: Established: STK38L is a serine/threonine kinase involved in intracellular signal transduction and is a central, annotation-supported module member. Hypothesis: it may act as a local signaling connector between kinase activity, cellular organization, and stress or proteostasis processes in the shared tissue context.

#### GSK3B

- **Related proteins** (co-abundance neighbors): STK38L (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: glycogen synthase kinase 3 beta. The protein encoded by this gene is a serine-threonine kinase belonging to the glycogen synthase kinase subfamily. It is a negative regulator of glucose homeostasis and is involved in energy metabolism, inflammation, ER-stress, mitochondrial dysfunction, and apoptotic pathways. Defects in this gene have been associated with Parkinson disease and Alzheimer disease. [provided by RefSeq, Aug 2017].
- **Diseases (Open Targets)**: bipolar disorder (0.614); major depressive disorder (0.572); bipolar I disorder (0.571); cancer (0.557); Alzheimer disease (0.554)
- **Europe PMC papers**: 15204
- **Why important**: GSK3B is a well-studied serine/threonine kinase with broad links to energy metabolism, inflammation, ER stress, mitochondrial dysfunction, and apoptosis. It appears across the primary kinase, phosphorylation, autophosphorylation, and protein-modification terms (5 globally significant GO/KEGG terms, q_global 3.1e-05–0.00482; see the table) and across nearly all corresponding STRING kinase terms. Its direct module degree is limited, but its biological breadth and large literature base make it an important functional anchor.
- **Conclusion**: Established: GSK3B provides a credible biochemical link between phosphorylation and metabolic or stress-related cell regulation. Hypothesis: its co-abundance with STK38L may reflect coordinated stress signaling rather than a direct physical interaction.

#### SMG1

- **Related proteins** (co-abundance neighbors): PRKCI (0.82), WDR62 (0.82), RBMXL1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enhanced; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: SMG1 nonsense mediated mRNA decay associated PI3K related kinase. This gene encodes a protein involved in nonsense-mediated mRNA decay (NMD) as part of the mRNA surveillance complex. The protein has kinase activity and is thought to function in NMD by phosphorylating the regulator of nonsense transcripts 1 protein. Alternatively spliced transcript variants have been described, but their full-length nature has yet to be determined. [provided by RefSeq, Mar 2013].
- **Diseases (Open Targets)**: alcohol drinking (0.251); stroke disorder (0.251); contracture (0.158); neoplasm (0.107); refractive error (0.098)
- **Europe PMC papers**: 1969
- **Why important**: SMG1 is a highly connected kinase node linked to PRKCI, WDR62, and RBMXL1, and it is present in every primary enrichment term listed for the module (15 globally significant GO/KEGG terms, q_global 3.1e-05–0.0331; see the table). Its established role in nonsense-mediated messenger-RNA decay, RNA export, DNA-damage response, and serine phosphorylation gives the module a strong RNA-surveillance dimension. It also has extensive literature support and is detected in both tissues in the supplied HPA evidence.
- **Conclusion**: Established: SMG1 is a multifunctional kinase and messenger-RNA surveillance regulator that strongly supports the module's phosphorylation and RNA-quality-control interpretation. Hypothesis: SMG1 may couple cellular stress or damage in these tissues to coordinated transcript surveillance.

#### CDK12

- **Related proteins** (co-abundance neighbors): WFS1 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_03314.1, huMAP3_09621.1
- **Function (MyGene.info)**: cyclin dependent kinase 12. Enables RNA polymerase II CTD heptapeptide repeat kinase activity and cyclin binding activity. Involved in phosphorylation of RNA polymerase II C-terminal domain; protein autophosphorylation; and regulation of MAP kinase activity. Located in nuclear speck. Part of cyclin K-CDK12 complex. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: prostate adenocarcinoma (0.638); neurodegenerative disease (0.565); Alzheimer disease (0.502); lysosomal storage disease (0.501); Parkinson disease (0.501)
- **Europe PMC papers**: 4245
- **Why important**: CDK12 is a primary-enrichment kinase (4 globally significant GO/KEGG terms, q_global 3.1e-05–0.00482; see the table) with a direct hu.MAP relationship to SRPK2 (hu.MAP huMAP3_03314.1) and membership in a larger RNA-processing complex (hu.MAP huMAP3_09621.1). Its established functions include RNA polymerase transcriptional control, transcription elongation, RNA splicing, and regulation of MAPK signaling. It is detected in both tissues and has a large disease and literature record, making it a strong bridge between the kinase signature and nuclear RNA biology.
- **Conclusion**: Established: CDK12 supports a transcriptional and RNA-processing interpretation of the module and has the clearest supplied complex-level link through hu.MAP. Hypothesis: coordinated CDK12 and SRPK2 abundance may mark coupling between transcriptional elongation and serine-rich splicing regulation.

#### MAP2K6

- **Related proteins** (co-abundance neighbors): PRKD2 (0.85); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: mitogen-activated protein kinase kinase 6. This gene encodes a member of the dual specificity protein kinase family, which functions as a mitogen-activated protein (MAP) kinase kinase. MAP kinases, also known as extracellular signal-regulated kinases (ERKs), act as an integration point for multiple biochemical signals. This protein phosphorylates and activates p38 MAP kinase in response to inflammatory cytokines or environmental stress. As…
- **Diseases (Open Targets)**: neurodegenerative disease (0.504); osteoarthritis, hip (0.493); osteoarthritis, knee (0.482); osteoarthritis (0.460); Abnormality of the skeletal system (0.425)
- **Europe PMC papers**: 1961
- **Why important**: MAP2K6 is the upstream signaling kinase in the module's most direct stress-response interpretation. It is included in the primary kinase and phosphorylation terms (4 globally significant GO/KEGG terms, q_global 3.1e-05–0.00482; see the table) and in the corresponding STRING kinase evidence (STRING Keyword Serine/threonine-protein kinase; within-query FDR = 3.42e-06) (STRING Function Protein serine kinase activity; within-query FDR = 5.84e-06) (STRING Process Protein phosphorylation; within-query FDR = 0.00089). Its established role is activation of p38 MAPK signaling in response to inflammatory cytokines and environmental stress. It has a direct module edge to PRKD2 and HPA annotations involving intestine, skeletal muscle, monocytes, plasmacytoid dendritic cells, and neutrophils.
- **Conclusion**: Established: MAP2K6 is a biologically plausible stress and inflammatory signaling component of the module. Hypothesis: MAP2K6 may provide an upstream trigger that coordinates the kinase-rich program in shared epithelial or immune-associated cell states.

## Module 15

**Tissue pair**: cervix_uterine and skin  
**Genes (42)**: ATXN2L, CCAR1, CHD4, DDX21, DHX9, DIAPH1, ADAR, EIF3C, FAM120A, GTF2I, HNRNPL, HNRNPR, IGF2BP1, LMNB1, MATR3, MYBBP1A, MVP, NASP, NOP2, NOP56, NUP214, PLRG1, PPM1G, PRRC2C, PSMC4, CAD, RBM10, UPF1, PDCD11, SEC23IP, SF3A1, SF3B3, SNW1, SUPT16H, SRRT, EPRS1, IARS1, LARS1, MARS1, TCERG1, EFTUD2, USP5

### Function

The module is best interpreted as a conserved nuclear RNA-processing and gene-expression module. The primary evidence is the broad convergence of globally corrected GO terms for RNA binding (GO:MF RNA binding; q_global = 1.45e-06), nucleic-acid binding (GO:MF nucleic acid binding; q_global = 2.12e-06), ribonucleoprotein complexes (GO:CC ribonucleoprotein complex; q_global = 3.56e-06), RNA metabolism (GO:BP RNA metabolic process; q_global = 8.24e-05), nuclear lumen and nucleoplasm (GO:CC nuclear lumen; q_global = 0.00029) (GO:CC nucleoplasm; q_global = 0.00143), gene expression (GO:BP gene expression; q_global = 0.00108), RNA and mRNA processing (GO:BP RNA processing; q_global = 0.00121) (GO:BP mRNA processing; q_global = 0.00201), RNA splicing (4 globally significant GO/KEGG terms, q_global 0.00381–0.0112; see the table), spliceosomal complexes (GO:CC spliceosomal complex; q_global = 0.00788) (GO:CC catalytic step 2 spliceosome; q_global = 0.0296), and regulatory RNA binding (GO:MF regulatory RNA binding; q_global = 0.0433). The module therefore does not indicate a single specialized pathway; it represents coordinated activity spanning RNA binding, RNA modification and surveillance, ribosome and nucleolar RNA maturation, spliceosome function, nuclear transport, and transcriptional or post-transcriptional regulation. The presence of aminoacyl-tRNA synthetases and translation-related genes is consistent with coupling RNA processing to protein synthesis. The network contains a particularly coherent spliceosomal branch involving EFTUD2, PLRG1, SF3A1, SF3B3, SNW1, TCERG1, and related RNA-binding proteins, together with nucleolar and RNA-helicase branches. The globally corrected GO results support this interpretation; the STRING functional terms (STRING RCTM Metabolism of RNA; within-query FDR = 1.43e-08) through (STRING Process Nucleic acid metabolic process; within-query FDR = 0.00024) are supportive but are not treated as independent global significance.

**Cell composition.** This is not a secreted-protein module: the HPA summary reports no secreted genes. Most members have low tissue specificity and are detected at the protein level in both cervix_uterine and skin, which is consistent with broadly expressed, intracellular housekeeping or core gene-expression machinery rather than a tissue-restricted program. HPA does show selective signals in testis, placenta, bone marrow, lymphoid tissue, and several germ-cell or neural cell types, but these are distributed across individual genes rather than defining the whole module. A few members show neutrophil or progenitor-associated signals, while overall immune-cell specificity is low. Thus a shared cell-type contribution, including possible hematopoietic or proliferative-cell representation, should be considered, but the evidence does not support describing the module as predominantly blood-cell enriched. IGF2BP1 is an informative exception because HPA assigns it group enrichment in placenta and testis and does not detect it in the two named tissues; this may reflect transcript-level co-abundance, cell composition, or measurement differences and warrants validation.

**GO/KEGG enrichment**: 26 terms pass global BH (q_global < 0.05).

| Term | q_global | genes |
|---|---|---|
| GO:MF RNA binding | 1.45e-06 | ADAR, ATXN2L, CCAR1, DDX21, DHX9, DIAPH1, EFTUD2, EIF3C, EPRS1, FAM120A, HNRNPL, HNRNPR, IARS1, IGF2BP1, MARS1, MATR3, MYBBP1A, NOP2, NOP56, PDCD11, PRRC2C, RBM10, SEC23IP, SF3A1, SF3B3, SNW1, SRRT, SUPT16H, TCERG1, UPF1 |
| GO:MF nucleic acid binding | 2.12e-06 | ADAR, ATXN2L, CCAR1, CHD4, DDX21, DHX9, DIAPH1, EFTUD2, EIF3C, EPRS1, FAM120A, GTF2I, HNRNPL, HNRNPR, IARS1, IGF2BP1, LMNB1, MARS1, MATR3, MYBBP1A, NOP2, NOP56, PDCD11, PRRC2C, RBM10, SEC23IP, SF3A1, SF3B3, SNW1, SRRT, SUPT16H, TCERG1, UPF1 |
| GO:CC ribonucleoprotein complex | 3.56e-06 | ADAR, DHX9, EFTUD2, EIF3C, EPRS1, HNRNPL, HNRNPR, IGF2BP1, MVP, NOP56, PDCD11, PLRG1, SF3A1, SF3B3, SNW1, SRRT, UPF1 |
| GO:BP RNA metabolic process | 8.24e-05 | ADAR, ATXN2L, CCAR1, CHD4, DDX21, DHX9, EFTUD2, EPRS1, GTF2I, HNRNPL, HNRNPR, IARS1, IGF2BP1, LARS1, MARS1, MYBBP1A, NOP2, NOP56, PDCD11, PLRG1, PPM1G, RBM10, SF3A1, SF3B3, SNW1, SRRT, SUPT16H, TCERG1, UPF1 |
| GO:CC nuclear lumen | 0.00029 | ADAR, ATXN2L, CAD, CCAR1, CHD4, DDX21, DHX9, EFTUD2, GTF2I, HNRNPL, HNRNPR, IARS1, IGF2BP1, LARS1, LMNB1, MARS1, MATR3, MYBBP1A, NASP, NOP2, NOP56, NUP214, PDCD11, PLRG1, PPM1G, PSMC4, RBM10, SF3A1, SF3B3, SNW1, SRRT, SUPT16H, TCERG1, UPF1 |
| GO:BP nucleic acid metabolic process | 0.000422 | ADAR, ATXN2L, CCAR1, CHD4, DDX21, DHX9, EFTUD2, EPRS1, GTF2I, HNRNPL, HNRNPR, IARS1, IGF2BP1, LARS1, MARS1, MYBBP1A, NASP, NOP2, NOP56, PDCD11, PLRG1, PPM1G, RBM10, SF3A1, SF3B3, SNW1, SRRT, SUPT16H, TCERG1, UPF1 |
| GO:BP gene expression | 0.00108 | ADAR, CCAR1, CHD4, DDX21, DHX9, EFTUD2, EIF3C, EPRS1, GTF2I, HNRNPL, HNRNPR, IARS1, IGF2BP1, LARS1, LMNB1, MARS1, MATR3, MVP, MYBBP1A, NOP2, NOP56, NUP214, PDCD11, PLRG1, PPM1G, RBM10, SF3A1, SF3B3, SNW1, SRRT, SUPT16H, TCERG1, UPF1 |
| GO:BP RNA processing | 0.00121 | ADAR, DDX21, DHX9, EFTUD2, HNRNPL, HNRNPR, NOP2, NOP56, PDCD11, PLRG1, RBM10, SF3A1, SF3B3, SNW1, SRRT, TCERG1, UPF1 |
| GO:CC nucleoplasm | 0.00143 | ADAR, ATXN2L, CCAR1, CHD4, DDX21, DHX9, EFTUD2, GTF2I, HNRNPL, HNRNPR, IARS1, IGF2BP1, LARS1, LMNB1, MYBBP1A, NASP, NOP2, NOP56, NUP214, PDCD11, PLRG1, PPM1G, PSMC4, RBM10, SF3A1, SF3B3, SNW1, SRRT, SUPT16H, TCERG1, UPF1 |
| GO:BP mRNA processing | 0.00201 | ADAR, DHX9, EFTUD2, HNRNPL, HNRNPR, PLRG1, RBM10, SF3A1, SF3B3, SNW1, SRRT, TCERG1, UPF1 |
| GO:BP macromolecule metabolic process | 0.00259 | ADAR, ATXN2L, CAD, CCAR1, CHD4, DDX21, DHX9, EFTUD2, EIF3C, EPRS1, GTF2I, HNRNPL, HNRNPR, IARS1, IGF2BP1, LARS1, LMNB1, MARS1, MATR3, MVP, MYBBP1A, NASP, NOP2, NOP56, NUP214, PDCD11, PLRG1, PPM1G, PSMC4, RBM10, SF3A1, SF3B3, SNW1, SRRT, SUPT16H, TCERG1, UPF1, USP5 |
| GO:BP RNA splicing, via transesterification reactions | 0.00381 | DHX9, EFTUD2, HNRNPL, HNRNPR, PLRG1, RBM10, SF3A1, SF3B3, SNW1, UPF1 |
| GO:BP RNA splicing, via transesterification reactions with bulged adenosine as nucleophile | 0.00381 | DHX9, EFTUD2, HNRNPL, HNRNPR, PLRG1, RBM10, SF3A1, SF3B3, SNW1, UPF1 |
| GO:BP mRNA splicing, via spliceosome | 0.00381 | DHX9, EFTUD2, HNRNPL, HNRNPR, PLRG1, RBM10, SF3A1, SF3B3, SNW1, UPF1 |
| GO:CC nucleus | 0.00386 | ADAR, ATXN2L, CAD, CCAR1, CHD4, DDX21, DHX9, DIAPH1, EFTUD2, FAM120A, GTF2I, HNRNPL, HNRNPR, IARS1, IGF2BP1, LARS1, LMNB1, MARS1, MATR3, MVP, MYBBP1A, NASP, NOP2, NOP56, NUP214, PDCD11, PLRG1, PPM1G, PSMC4, RBM10, SF3A1, SF3B3, SNW1, SRRT, SUPT16H, TCERG1, UPF1, USP5 |

### STRING and hu.MAP

STRING provides substantial known molecular support for the inferred function. The strongest established relationships include the spliceosomal core connections among EFTUD2, PLRG1, SF3A1, SF3B3, SNW1, and TCERG1; the hnRNP and RNA-helicase relationships involving DHX9, HNRNPL, HNRNPR, ADAR, MATR3, and IGF2BP1; and the nucleolar RNA-processing relationships linking DDX21, NOP2, NOP56, MYBBP1A, and PDCD11. The aminoacyl-tRNA synthetase relationships among EPRS1, IARS1, LARS1, and MARS1 are also strongly represented. These links indicate that the co-abundance graph recapitulates known complexes and functional neighborhoods rather than being a collection of unrelated genes. hu.MAP independently supports known assemblies: an hnRNP and RNA-binding complex containing HNRNPR, HNRNPL, MATR3, ADAR, UPF1, and FAM120A (hu.MAP huMAP3_10625.1); multisynthetase complexes containing EPRS1, IARS1, MARS1, and LARS1 (hu.MAP huMAP3_02637.1) (hu.MAP huMAP3_13688.1); spliceosomal assemblies containing PLRG1, SNW1, EFTUD2, SF3A1, SF3B3, RBM10, and CCAR1 (hu.MAP huMAP3_10359.1) (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1) (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_11912.1) (hu.MAP huMAP3_06726.1) (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_06511.1); and additional hnRNP assemblies (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_05721.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09281.1) (hu.MAP huMAP3_09223.1) (hu.MAP huMAP3_06975.1). The network consequently appears to integrate several established RNA-protein assemblies, with co-abundance extending across them.

**STRING interactions (score >= 0.7)**: 62 of 861 gene pairs: ADAR–DHX9 (0.922); ADAR–UPF1 (0.983); CCAR1–DHX9 (0.851); CCAR1–RBM10 (0.743); CCAR1–SRRT (0.857); CCAR1–TCERG1 (0.92); CHD4–NOP2 (0.724); CHD4–SRRT (0.76); CHD4–SUPT16H (0.815); DDX21–DHX9 (0.908); DDX21–HNRNPR (0.73); DDX21–MYBBP1A (0.963); DDX21–NOP2 (0.761); DDX21–NOP56 (0.811); DHX9–HNRNPL (0.901); DHX9–HNRNPR (0.909); DHX9–IGF2BP1 (0.985); DHX9–MATR3 (0.786); DHX9–SF3B3 (0.73); DHX9–SRRT (0.92); DHX9–TCERG1 (0.841); EFTUD2–EPRS1 (0.744); EFTUD2–PDCD11 (0.828); EFTUD2–PLRG1 (0.999); EFTUD2–SF3A1 (0.999); EFTUD2–SF3B3 (0.999); EFTUD2–SNW1 (0.999); EFTUD2–TCERG1 (0.974); EIF3C–EPRS1 (0.755); EPRS1–IARS1 (0.999); EPRS1–LARS1 (0.999); EPRS1–MARS1 (0.999); EPRS1–NOP56 (0.739); EPRS1–PDCD11 (0.75); FAM120A–UPF1 (0.741); HNRNPL–HNRNPR (0.961); HNRNPL–MATR3 (0.757); HNRNPL–SRRT (0.725); HNRNPR–MATR3 (0.714); IARS1–LARS1 (0.999); IARS1–MARS1 (0.999); IGF2BP1–MATR3 (0.91); LARS1–MARS1 (0.999); MYBBP1A–NOP2 (0.864); MYBBP1A–NOP56 (0.737); MYBBP1A–PDCD11 (0.949); NASP–SUPT16H (0.727); NOP2–NOP56 (0.969); NOP2–PDCD11 (0.927); NOP56–PDCD11 (0.997); PLRG1–SF3A1 (0.982); PLRG1–SF3B3 (0.973); PLRG1–SNW1 (0.999); PLRG1–TCERG1 (0.98); RBM10–SF3A1 (0.858); SF3A1–SF3B3 (0.999); SF3A1–SNW1 (0.989); SF3A1–TCERG1 (0.992); SF3B3–SNW1 (0.99); SF3B3–TCERG1 (0.977); SNW1–TCERG1 (0.987); SRRT–TCERG1 (0.839)
**STRING functional enrichment (supplementary, within-query FDR)**: RCTM Metabolism of RNA (FDR = 1.43e-08, 22 genes); Function RNA binding (FDR = 2.87e-07, 30 genes); Function Nucleic acid binding (FDR = 3.34e-07, 33 genes); Keyword Isopeptide bond (FDR = 4.71e-06, 24 genes); COMPARTMENTS Ribonucleoprotein complex (FDR = 4.93e-06, 16 genes); RCTM mRNA Splicing - Major Pathway (FDR = 6.5e-06, 12 genes); COMPARTMENTS Nuclear lumen (FDR = 1.38e-05, 24 genes); Process RNA metabolic process (FDR = 1.48e-05, 24 genes); RCTM Processing of Capped Intron-Containing Pre-mRNA (FDR = 2.15e-05, 13 genes); Component Nuclear lumen (FDR = 3.72e-05, 34 genes); Component Ribonucleoprotein complex (FDR = 3.72e-05, 16 genes); Keyword Ubl conjugation (FDR = 8.34e-05, 24 genes); Component Nucleoplasm (FDR = 0.00012, 31 genes); Process Gene expression (FDR = 0.0002, 25 genes); Process Nucleic acid metabolic process (FDR = 0.00024, 25 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10625.1 (HNRNPR, HNRNPL, MATR3, ADAR, UPF1, FAM120A; 6/57); huMAP3_02637.1 (EPRS1, IARS1, MARS1, LARS1; 4/14); huMAP3_13688.1 (EPRS1, IARS1, MARS1, LARS1; 4/14); huMAP3_07225.1 (HNRNPR, HNRNPL, FAM120A; 3/7); huMAP3_09654.1 (HNRNPR, HNRNPL, FAM120A; 3/13); huMAP3_07581.1 (HNRNPR, HNRNPL, MATR3; 3/21); huMAP3_10359.1 (RBM10, SF3A1, CCAR1; 3/27); huMAP3_10659.1 (HNRNPR, HNRNPL, FAM120A; 3/28); huMAP3_08501.1 (PLRG1, SNW1, EFTUD2; 3/47); huMAP3_09504.1 (PLRG1, SNW1, EFTUD2; 3/51); huMAP3_09945.1 (PLRG1, SNW1, EFTUD2; 3/61); huMAP3_08980.1 (EFTUD2, SF3B3, SF3A1; 3/97); huMAP3_05721.1 (HNRNPL, MATR3; 2/6); huMAP3_06093.1 (HNRNPR, HNRNPL; 2/10); huMAP3_09281.1 (HNRNPR, FAM120A; 2/14); huMAP3_09223.1 (MATR3, FAM120A; 2/15); huMAP3_11912.1 (RBM10, CCAR1; 2/16); huMAP3_06975.1 (MATR3, UPF1; 2/31); huMAP3_10862.1 (PPM1G, SUPT16H; 2/33); huMAP3_06726.1 (PLRG1, SNW1; 2/37); huMAP3_04549.1 (SF3B3, SF3A1; 2/52); huMAP3_06511.1 (SF3B3, SF3A1; 2/79)

### Novelty

The biological components and many of their relationships are not new: STRING and hu.MAP already document the spliceosome, hnRNP, nucleolar RNA-processing, and multisynthetase relationships represented here. Therefore this module should not be presented as discovery of a new molecular function or a new protein complex. The potentially novel observation is the reproducible conservation of this particular co-abundance configuration across cervix_uterine and skin, especially the coordinated connection between spliceosomal, nucleolar, RNA-surveillance, nuclear-transport, and translation-supporting genes. However, the fact sheet does not provide a comparison with previously published tissue co-abundance modules, independent cohorts, or perturbation experiments. Absence of some module members from STRING or hu.MAP is not evidence of novelty. The appropriate conclusion is that the module-level tissue-pair observation may be a useful integration or replication finding, but novelty remains unestablished until external module catalogs and independent datasets are compared.

**Hypothesis.** Hypothesis: in both cervix_uterine and skin, a shared state of active nuclear gene expression coordinates pre-mRNA splicing, RNA editing, RNA surveillance, nucleolar RNA maturation, nuclear export, and translation capacity. The spliceosomal core may provide the structural processing arm, DHX9 and ADAR may regulate RNA structure and editing, UPF1 may couple processing to surveillance and export, the nucleolar group may support ribosome biogenesis, and the aminoacyl-tRNA synthetase group may maintain translational readiness. NUP214 and LMNB1 could connect these activities to nuclear transport and nuclear architecture. The co-abundance could arise from a common proliferative or differentiated epithelial-cell state, from shared cellular composition, or from both. This is a mechanistic model rather than proof of direct regulation; it should be tested with cell-resolved measurements, perturbation of spliceosomal or RNA-surveillance genes, and independent cervix and skin cohorts.

### Important genes

#### ADAR

- **Related proteins** (co-abundance neighbors): NOP2 (0.87), PLRG1 (0.85), NOP56 (0.84), DHX9 (0.84), PDCD11 (0.83), MYBBP1A (0.82), IGF2BP1 (0.80); STRING partners: DHX9 (0.922), UPF1 (0.983)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoli; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_10625.1
- **Function (MyGene.info)**: adenosine deaminase RNA specific. This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010].
- **Diseases (Open Targets)**: Aicardi-Goutieres syndrome 6 (0.838); dyschromatosis symmetrica hereditaria (0.823); Aicardi-Goutieres syndrome (0.713); ADAR-related type 1 interferonopathy (0.568); hereditary disease (0.520)
- **Europe PMC papers**: 6966
- **Why important**: ADAR is a high-connectivity module member and links to DHX9, UPF1, NOP2, NOP56, PDCD11, MYBBP1A, and IGF2BP1 in the co-abundance graph. It is represented across the RNA-binding, RNA-processing, ribonucleoprotein, splicing, nucleic-acid, and regulatory-RNA terms (7 globally significant GO/KEGG terms, q_global 1.45e-06–0.0433; see the table). Its established function is site-specific adenosine-to-inosine RNA editing and destabilization of double-stranded RNA, with roles in RNA processing and antiviral response. Its disease associations include Aicardi-Goutieres syndrome and dyschromatosis symmetrica hereditaria, and it has a substantial literature base. HPA detects it in both named tissues and shows neutrophil cell-type enhancement.
- **Conclusion**: Established: ADAR is a biologically informative bridge between RNA binding, RNA editing, RNA structure, and surveillance. Hypothesis: it may help couple the module's nuclear RNA-processing state to tissue stress or antiviral sensing, but the co-abundance data do not establish altered editing or causal regulation.

#### EFTUD2

- **Related proteins** (co-abundance neighbors): CHD4 (0.85), NUP214 (0.85), PRRC2C (0.85), FAM120A (0.81), MVP (0.80); STRING partners: EPRS1 (0.744), PDCD11 (0.828), PLRG1 (0.999), SF3A1 (0.999), SF3B3 (0.999), SNW1 (0.999), TCERG1 (0.974)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1, huMAP3_08980.1
- **Function (MyGene.info)**: elongation factor Tu GTP binding domain containing 2. This gene encodes a GTPase which is a component of the spliceosome complex which processes precursor mRNAs to produce mature mRNAs. Mutations in this gene are associated with mandibulofacial dysostosis with microcephaly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012].
- **Diseases (Open Targets)**: mandibulofacial dysostosis-microcephaly syndrome (0.833); hereditary disease (0.541); neurodegenerative disease (0.478); Global developmental delay (0.409); plasma cell myeloma (0.371)
- **Europe PMC papers**: 981
- **Why important**: EFTUD2 is embedded in the strongest known spliceosomal relationships in STRING and in several hu.MAP spliceosomal complexes (hu.MAP huMAP3_08501.1) (hu.MAP huMAP3_09504.1) (hu.MAP huMAP3_09945.1) (hu.MAP huMAP3_08980.1). It connects directly with PLRG1, SF3A1, SF3B3, SNW1, and TCERG1 and appears in essentially the full set of primary RNA-processing and spliceosome terms (10 globally significant GO/KEGG terms, q_global 3.56e-06–0.0399; see the table). Its established function is as a GTPase component of the spliceosome, including tri-snRNP assembly and spliceosome conformational change. Mandibulofacial dysostosis with microcephaly is a prominent disease association, and the gene has a substantial literature base.
- **Conclusion**: Established: EFTUD2 is a core mechanistic anchor for the module's pre-mRNA splicing interpretation. Hypothesis: coordinated EFTUD2 abundance may indicate variation in spliceosomal capacity across the shared tissue state, but it does not demonstrate a particular alternative-splicing program.

#### DHX9

- **Related proteins** (co-abundance neighbors): DDX21 (0.87), ADAR (0.84), MARS1 (0.83), MATR3 (0.82), HNRNPR (0.81), PRRC2C (0.80); STRING partners: ADAR (0.922), CCAR1 (0.851), DDX21 (0.908), HNRNPL (0.901), HNRNPR (0.909), IGF2BP1 (0.985), MATR3 (0.786), SF3B3 (0.73), SRRT (0.92), TCERG1 (0.841)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DExH-box helicase 9. This gene encodes a member of the DEAH-containing family of RNA helicases. The encoded protein is an enzyme that catalyzes the ATP-dependent unwinding of double-stranded RNA and DNA-RNA complexes. This protein localizes to both the nucleus and the cytoplasm and functions as a transcriptional regulator. This protein may also be involved in the expression and nuclear export of retroviral RNAs. Alter…
- **Diseases (Open Targets)**: intellectual developmental disorder, autosomal dominant 75 (0.646); neurodegenerative disease (0.548); hereditary disease (0.517); dengue disease (0.373); lysosomal storage disease (0.306)
- **Europe PMC papers**: 3648
- **Why important**: DHX9 is a highly connected RNA helicase hub with established STRING relationships to ADAR, DDX21, HNRNPL, HNRNPR, IGF2BP1, MATR3, SF3B3, SRRT, and TCERG1. It is represented in nearly all of the primary RNA-binding, RNA-processing, splicing, nucleic-acid, and regulatory-RNA categories, including the spliceosomal terms (12 globally significant GO/KEGG terms, q_global 1.45e-06–0.0433; see the table). Its established function is ATP-dependent unwinding of RNA and DNA-RNA structures, with roles in transcription, alternative splicing, nuclear export, and interferon regulation. It is associated with developmental and neurodegenerative disease, and has a substantial literature base.
- **Conclusion**: Established: DHX9 is a plausible functional hub connecting RNA structure, splicing, export, and innate-response biology. Hypothesis: it may coordinate transitions between processed nuclear RNA and cytoplasmic RNA fate in this module, but direct flux through those pathways was not measured.

#### NUP214

- **Related proteins** (co-abundance neighbors): FAM120A (0.87), PRRC2C (0.86), IARS1 (0.85), EFTUD2 (0.85), CHD4 (0.84), NASP (0.83), ATXN2L (0.82), USP5 (0.80), LMNB1 (0.80), CCAR1 (0.80); STRING partners: none
- **HPA**: Tissue enhanced; Cell type enhanced; blood Group enriched; location None; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nucleoporin 214. The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene is a member of the FG-repeat-containing nucleoporins. The protein encoded by this gene is localized to the cytoplas…
- **Diseases (Open Targets)**: familial acute necrotizing encephalopathy (0.664); Orthomyxoviridae infectious disease (0.543); HIV infectious disease (0.542); viral infectious disease (0.527); Global developmental delay (0.435)
- **Europe PMC papers**: 2712
- **Why important**: NUP214 has the highest network position in the supplied module graph and connects to FAM120A, PRRC2C, IARS1, EFTUD2, CHD4, NASP, ATXN2L, and USP5. It occurs in the primary nuclear-lumen, nucleoplasm, gene-expression, and nuclear-complex terms (7 globally significant GO/KEGG terms, q_global 0.00029–0.0192; see the table). Its established function is as a cytoplasmic-face nucleoporin involved in nucleocytoplasmic transport, including RNA export and protein transport. It has disease associations involving acute necrotizing encephalopathy, developmental delay, and viral infection, with a substantial literature base. HPA also reports testis, neutrophil, and classical-monocyte enrichment signals.
- **Conclusion**: Established: NUP214 provides a credible nuclear-transport interface for a module otherwise dominated by RNA-processing machinery. Hypothesis: it may couple RNA maturation to export in the shared tissue state, although the graph cannot distinguish transport regulation from correlated expression.

#### HNRNPR

- **Related proteins** (co-abundance neighbors): FAM120A (0.94), SUPT16H (0.85), IARS1 (0.85), HNRNPL (0.81), DHX9 (0.81), LMNB1 (0.80); STRING partners: DDX21 (0.73), DHX9 (0.909), HNRNPL (0.961), MATR3 (0.714)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_10625.1, huMAP3_07225.1, huMAP3_09654.1, huMAP3_07581.1, huMAP3_10659.1, huMAP3_06093.1, huMAP3_09281.1
- **Function (MyGene.info)**: heterogeneous nuclear ribonucleoprotein R. This gene encodes an RNA-binding protein that is a member of the spliceosome C complex, which functions in pre-mRNA processing and transport. The encoded protein also promotes transcription at the c-fos gene. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes 4, 11, and 10. [provided by RefSeq, Jul 2014].
- **Diseases (Open Targets)**: neurodevelopmental disorder with dysmorphic facies and skeletal and brain abnormalities (0.711); Intellectual disability (0.554); Global developmental delay (0.462); Seizure (0.462); Secondary microcephaly (0.462)
- **Europe PMC papers**: 652
- **Why important**: HNRNPR is a central RNA-binding and spliceosomal member, with strong graph relationships to FAM120A, HNRNPL, DHX9, DDX21, MATR3, IARS1, and SUPT16H. It is present in the primary terms spanning RNA binding, ribonucleoprotein complexes, RNA processing, mRNA splicing, spliceosomal complexes, and regulatory RNA binding (13 globally significant GO/KEGG terms, q_global 1.45e-06–0.0433; see the table). STRING and hu.MAP independently place it in hnRNP assemblies (hu.MAP huMAP3_10625.1) (hu.MAP huMAP3_07225.1) (hu.MAP huMAP3_09654.1) (hu.MAP huMAP3_07581.1) (hu.MAP huMAP3_10659.1) (hu.MAP huMAP3_06093.1) (hu.MAP huMAP3_09281.1). Its established function includes participation in the spliceosome C complex, pre-mRNA processing, and RNA transport. It is associated with neurodevelopmental disorders and has a substantial literature base.
- **Conclusion**: Established: HNRNPR is a strong representative of the module's hnRNP and spliceosome arm. Hypothesis: it may help define transcript-selective RNA processing in the shared cervix and skin state, but specific target transcripts are not identified here.

#### SF3A1

- **Related proteins** (co-abundance neighbors): SF3B3 (0.86), GTF2I (0.82), PPM1G (0.81), TCERG1 (0.81); STRING partners: EFTUD2 (0.999), PLRG1 (0.982), RBM10 (0.858), SF3B3 (0.999), SNW1 (0.989), TCERG1 (0.992)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm, Nuclear speckles; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_10359.1, huMAP3_08980.1, huMAP3_04549.1, huMAP3_06511.1
- **Function (MyGene.info)**: splicing factor 3a subunit 1. This gene encodes a subunit of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer is a component of the mature U2 small nuclear ribonucleoprotein particle (snRNP). U2 small nuclear ribonucleoproteins play a critical role in spliceosome assembly and pre-mRNA splicing. [provided by RefSeq, Aug 2014].
- **Diseases (Open Targets)**: dengue disease (0.370); diffuse large B-cell lymphoma (0.334); neurodegenerative disease (0.320); type 2 diabetes mellitus (0.126); schizophrenia (0.077)
- **Europe PMC papers**: 1069
- **Why important**: SF3A1 is a core U2 snRNP and spliceosomal component with strong STRING relationships to EFTUD2, PLRG1, SF3B3, SNW1, TCERG1, and RBM10. It occurs throughout the primary RNA-processing and splicing terms (12 globally significant GO/KEGG terms, q_global 1.45e-06–0.0399; see the table). hu.MAP places it in multiple spliceosomal assemblies (hu.MAP huMAP3_10359.1) (hu.MAP huMAP3_08980.1) (hu.MAP huMAP3_04549.1) (hu.MAP huMAP3_06511.1). Its established function is U2 snRNP assembly and pre-mRNA splice-site recognition. Disease associations include lymphoma, neurodegenerative disease, and metabolic disease, and it has a substantial literature base. HPA detects it in both named tissues.
- **Conclusion**: Established: SF3A1 is a direct molecular anchor for the module's spliceosomal interpretation. Hypothesis: its coordinated abundance may reflect broad control of intron-containing transcript processing, but no particular splice-site outcome can be inferred.

## Module 16

**Tissue pair**: cervix_uterine and skin  
**Genes (40)**: BUB1B, CC2D1B, CPSF3, CTTNBP2NL, CXADR, DCTN1, DDX24, DDX55, GFM1, EPS15L1, FERMT2, GLS, HELLS, MTIF2, KIF21A, KIF14, LEMD3, MDN1, IGF2R, NAA15, NEMF, IKBKG, NUP37, OPA1, LPCAT1, PDLIM5, PELO, PLCB3, PITRM1, RBM22, ELAC2, TES, TLN1, TRIO, SNRNP200, UBR5, WAPL, WDHD1, XPO7, TJP1

### Function

The module does not support a single statistically established GO or KEGG function: no GO or KEGG term passed global correction. Its structure instead suggests a mixed cellular-maintenance program. The strongest network-centered signals involve cell-cycle and chromosome-segregation control around BUB1B, RNA processing and spliceosome biology around RBM22 and SNRNP200, mitochondrial translation around GFM1 and MTIF2, ribosome quality control around NEMF and PELO, and epithelial junction or adhesion biology around TJP1, CXADR, FERMT2 and TLN1. These are coherent biological annotations for individual subnetworks, but their co-abundance should not be treated as proof of one unified pathway.

**Cell composition.** The module is not predominantly composed of plasma or secreted proteins; only CXADR is annotated as secreted with unknown location, and the other genes are intracellular or membrane-associated. It is also not uniformly tissue-specific: most genes have low tissue specificity, while a substantial subset is enhanced in lymphoid tissue, bone marrow, reproductive cell populations, erythrocyte progenitors, neutrophils and other blood-related cell types. Several genes are detected in both cervix_uterine and skin, although some are absent from one of those tissues. The HPA profile therefore raises a meaningful shared-cell-type or blood-related contribution, especially for genes associated with lymphoid, myeloid, erythroid or megakaryocytic populations, but it does not establish that the module is merely plasma contamination or a pure blood-cell signature. The broad expression of many genes is also compatible with a general cellular-maintenance component.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

The high-confidence STRING network is sparse but contains biologically interpretable relationships. BUB1B is linked to KIF14 and UBR5; RBM22 is very strongly linked to SNRNP200; CPSF3 is linked to ELAC2; DDX24 is linked to DDX55; GFM1 is linked to MTIF2; NEMF is linked to PELO; FERMT2 is linked to TLN1; and CXADR is linked to TJP1. These relationships support known molecular neighborhoods rather than a single STRING-defined pathway, and there is no STRING functional enrichment. hu.MAP provides stronger complex-level context for the mitochondrial translation or mitochondrial RNA-processing neighborhood containing GLS, MTIF2, GFM1 and ELAC2 in (hu.MAP huMAP3_13468.1), with a related subset in (hu.MAP huMAP3_10458.1). SNRNP200 and RBM22 recur together in several spliceosome-related hu.MAP complexes (hu.MAP huMAP3_06726.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1) and (hu.MAP huMAP3_09945.1). PLCB3 and TES occur together in (hu.MAP huMAP3_14442.1), while NUP37 and XPO7 occur together in (hu.MAP huMAP3_11232.1). Thus, several relationships are already known at the interaction or complex level, but most module edges are not represented by the listed STRING or hu.MAP relationships. The module is consequently best viewed as a co-abundance assembly containing multiple established cellular subsystems.

**STRING interactions (score >= 0.7)**: 9 of 780 gene pairs: BUB1B–KIF14 (0.878); BUB1B–UBR5 (0.782); CPSF3–ELAC2 (0.794); CXADR–TJP1 (0.815); DDX24–DDX55 (0.812); FERMT2–TLN1 (0.705); GFM1–MTIF2 (0.791); NEMF–PELO (0.717); RBM22–SNRNP200 (0.998)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_13468.1 (GLS, MTIF2, GFM1, ELAC2; 4/99); huMAP3_10458.1 (GLS, MTIF2, ELAC2; 3/16); huMAP3_06726.1 (SNRNP200, RBM22; 2/37); huMAP3_08501.1 (SNRNP200, RBM22; 2/47); huMAP3_09504.1 (SNRNP200, RBM22; 2/51); huMAP3_14442.1 (PLCB3, TES; 2/57); huMAP3_09945.1 (SNRNP200, RBM22; 2/61); huMAP3_11232.1 (NUP37, XPO7; 2/78)

### Novelty

This dataset does not demonstrate that the module is a new biological complex or a newly discovered pathway. The known STRING links and recurring hu.MAP complexes show that several parts of the module recapitulate established molecular machinery. Conversely, the particular cross-tissue co-abundance combination of cell-cycle, RNA-processing, mitochondrial, ribosome-quality-control and epithelial-junction genes is not mechanistically resolved by the supplied databases. Absence of a complete match in STRING or hu.MAP would not prove novelty, because those resources primarily capture physical interactions or curated complexes rather than tissue-pair co-abundance patterns. The defensible conclusion is that the tissue-shared co-abundance pattern may be a novel observation, but its biological novelty requires replication in independent cervix and skin cohorts, adjustment for cell composition and blood contribution, and comparison with published co-expression modules.

**Hypothesis.** Mechanistic hypothesis: the module reflects a shared state of viable, proliferative or renewing epithelial-associated samples in which junctional organization and adhesion are coupled to increased demands for chromosome segregation, RNA processing, mitochondrial protein synthesis and ribosome surveillance. A contribution from lymphoid, erythroid, neutrophil or other hematopoietic cells may create or strengthen the cross-tissue signal. This hypothesis predicts that the module will weaken after cell-composition adjustment if it is mainly driven by shared infiltrating or circulating cells, whereas a residual epithelial signal should track junction integrity, cytoskeletal organization and tissue repair. The hypothesis is not established by the absence of globally significant GO or KEGG enrichment.

### Important genes

#### BUB1B

- **Related proteins** (co-abundance neighbors): MDN1 (0.89), FERMT2 (0.88), PLCB3 (0.84), NEMF (0.83), WAPL (0.82), DDX55 (0.82), SNRNP200 (0.81), RBM22 (0.81), TLN1 (0.80), UBR5 (0.80); STRING partners: KIF14 (0.878), UBR5 (0.782)
- **HPA**: Tissue enhanced; Cell type enhanced; blood Immune cell enhanced; location Cytosol; IHC detected in none
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: BUB1 mitotic checkpoint serine/threonine kinase B. This gene encodes a kinase involved in spindle checkpoint function. The protein has been localized to the kinetochore and plays a role in the inhibition of the anaphase-promoting complex/cyclosome (APC/C), delaying the onset of anaphase and ensuring proper chromosome segregation. Impaired spindle checkpoint function has been found in many forms of cancer. [provided by RefSeq, Jul 2008].
- **Diseases (Open Targets)**: mosaic variegated aneuploidy syndrome (0.815); mosaic variegated aneuploidy syndrome 1 (0.794); premature chromatid separation trait (0.631); neurodegenerative disease (0.537); colorectal cancer (0.503)
- **Europe PMC papers**: 3723
- **Why important**: BUB1B is the leading network hub by weighted connectivity in the supplied graph and connects to genes spanning chromosome segregation, adhesion, RNA-processing and ribosome-related neighborhoods. Its established function is the spindle checkpoint, inhibition of the anaphase-promoting complex and faithful chromosome segregation. HPA associates it with bone marrow, lymphoid tissue, testis and several progenitor populations, and its disease associations include mosaic variegated aneuploidy and cancer. Its large literature base makes it a strong anchor for interpreting a proliferation or cell-cycle component.
- **Conclusion**: Established evidence supports BUB1B as a mitotic-checkpoint gene and as a central co-abundance hub. The module does not establish that BUB1B activity is increased or that checkpoint dysfunction causes the shared tissue pattern. A proliferative-state interpretation is therefore plausible but remains a hypothesis.

#### RBM22

- **Related proteins** (co-abundance neighbors): WAPL (0.86), PDLIM5 (0.85), LPCAT1 (0.83), WDHD1 (0.83), XPO7 (0.81), DCTN1 (0.81), NAA15 (0.81), BUB1B (0.81), CPSF3 (0.80), NUP37 (0.80); STRING partners: SNRNP200 (0.998)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_06726.1, huMAP3_08501.1, huMAP3_09504.1, huMAP3_09945.1
- **Function (MyGene.info)**: RNA binding motif protein 22. This gene encodes an RNA binding protein. The encoded protein may play a role in cell division and may be involved in pre-mRNA splicing. Related pseudogenes exist on chromosomes 6, 7, 9, 13, 16, 18, and X. [provided by RefSeq, Mar 2009].
- **Diseases (Open Targets)**: dengue disease (0.370); neurodegenerative disease (0.358); pneumonitis (0.111); glioblastoma (0.078); anencephaly 1 (0.056)
- **Europe PMC papers**: 353
- **Why important**: RBM22 is another leading network hub and is directly connected to SNRNP200 in STRING with very high confidence. It occurs with SNRNP200 in several independent hu.MAP spliceosome complexes (hu.MAP huMAP3_06726.1), (hu.MAP huMAP3_08501.1), (hu.MAP huMAP3_09504.1) and (hu.MAP huMAP3_09945.1). Its established functions include RNA binding and pre-mRNA splicing, and HPA detects it in both cervix_uterine and skin. It therefore provides a strong molecular explanation for the RNA-processing portion of the module and has a substantial literature base.
- **Conclusion**: Established evidence supports a spliceosome-related RBM22-SNRNP200 subnetwork. The co-abundance result does not show altered splicing, a particular transcript isoform program or a causal role for RBM22 in either tissue. Those interpretations require transcript-level or functional validation.

#### TJP1

- **Related proteins** (co-abundance neighbors): WDHD1 (0.82), CTTNBP2NL (0.82), NEMF (0.81), MDN1 (0.81); STRING partners: CXADR (0.815)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Not detected in immune cells; location Cell Junctions; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: tight junction protein 1. This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) family of proteins, and acts as a tight junction adaptor protein that also regulates adherens junctions. Tight junctions regulate the movement of ions and macromolecules between endothelial and epithelial cells. The multidomain structure of this scaffold protein, including a postsynaptic density 95/disc-large/zona occlu…
- **Diseases (Open Targets)**: dengue disease (0.476); COVID-19 (0.373); skin disorder (0.312); Hypocalcemia (0.264); cataract (0.256)
- **Europe PMC papers**: 6421
- **Why important**: TJP1 is a junctional scaffold connected within the module to several genes involved in cytoskeletal, nuclear and membrane organization, and it has a high-confidence STRING relationship with CXADR. Its established functions include tight-junction and adherens-junction organization, actin-cytoskeleton regulation, cell migration and maintenance of epithelial barriers. HPA detects it in both tissues, making it especially relevant to a conserved cervix_uterine-skin interpretation. Its disease associations include skin disorder and other junction-related phenotypes.
- **Conclusion**: Established evidence supports TJP1 as an epithelial junction and barrier marker that could explain part of the tissue-shared signal. The module does not prove that junctions are functionally strengthened or disrupted, nor that TJP1 directly coordinates the cell-cycle and RNA-processing genes.

#### GFM1

- **Related proteins** (co-abundance neighbors): MTIF2 (0.84), PITRM1 (0.83); STRING partners: MTIF2 (0.791)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Mitochondria; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_13468.1
- **Function (MyGene.info)**: G elongation factor mitochondrial 1. Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongati…
- **Diseases (Open Targets)**: hepatoencephalopathy due to combined oxidative phosphorylation defect type 1 (0.822); neurodegenerative disease (0.463); combined oxidative phosphorylation deficiency (0.451); hereditary disease (0.341); Leigh syndrome (0.313)
- **Europe PMC papers**: 1380
- **Why important**: GFM1 represents the mitochondrial translation component of the module. It is connected to MTIF2 in STRING and both genes occur in the high-confidence hu.MAP mitochondrial complex (hu.MAP huMAP3_13468.1). Its established function is mitochondrial translation elongation, which is required for respiratory-chain maintenance, and its disease associations include combined oxidative-phosphorylation defects and Leigh syndrome. HPA detects GFM1 in both tissues, supporting relevance to a shared cellular program rather than a tissue-exclusive marker.
- **Conclusion**: Established evidence supports a mitochondrial protein-synthesis relationship between GFM1 and MTIF2. The module does not establish mitochondrial stress, altered respiration or increased translation in cervix_uterine or skin. Those are testable hypotheses rather than conclusions from co-abundance alone.

#### NEMF

- **Related proteins** (co-abundance neighbors): BUB1B (0.83), LEMD3 (0.83), TJP1 (0.81), KIF21A (0.81); STRING partners: PELO (0.717)
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nucleoplasm, Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: nuclear export mediator factor. This gene encodes a component of the ribosome quality control complex. The encoded protein facilitates the recognition and ubiquitination of stalled 60S subunits by the ubiquitin ligase listerin. A similar protein in fly functions as a tumor suppressor. [provided by RefSeq, Jul 2016].
- **Diseases (Open Targets)**: intellectual developmental disorder with speech delay and axonal peripheral neuropathy (0.708); hereditary disease (0.471); Global developmental delay (0.374); Intellectual disability (0.371); cerebellar ataxia (0.370)
- **Europe PMC papers**: 2061
- **Why important**: NEMF links the module's translational-quality-control component to several network neighborhoods and has a STRING relationship with PELO. Its established function is recognition and processing of stalled ribosomes within ribosome-associated quality control, including cooperation with ubiquitin-mediated disposal. It is detected in both tissues and has well-documented associations with developmental and neurological disease. Its position near BUB1B, TJP1 and KIF21A makes it useful for interpreting the module as a broader stress, renewal or proteostasis-related state rather than as an isolated ribosome pathway.
- **Conclusion**: Established evidence supports NEMF as a ribosome-surveillance factor and supports a NEMF-PELO quality-control subnetwork. The co-abundance module does not demonstrate stalled translation, proteotoxic stress or direct coupling between ribosome rescue and epithelial junction remodeling.

## Module 17

**Tissue pair**: cervix_uterine and skin  
**Genes (6)**: POLA1, ERBIN, GIGYF2, PPP1R12A, RBM26, USP10

### Function

The module does not support a single statistically established pathway-level function: no GO or KEGG term passed global correction, and STRING reported no functional enrichment. Its gene annotations instead suggest a mixed intracellular program involving RNA processing and post-transcriptional regulation through RBM26 and GIGYF2, ubiquitin-dependent protein regulation and stress-related processes through USP10, epithelial signaling and cytoskeletal organization through ERBIN, DNA replication and repair through POLA1, and actomyosin regulation and cell adhesion through PPP1R12A. The co-abundance structure is therefore more consistent with coordinated regulation of general cellular state, RNA and protein homeostasis, genome maintenance, and cell architecture than with a confidently assigned specialized pathway.

**Cell composition.** All module genes have low tissue specificity in HPA, and none is secreted. Protein detection is present for the module in both tissues, although ERBIN is not detected in cervix_uterine by IHC. Most genes have low immune-cell specificity, while USP10 is immune-cell enriched and associated with neutrophils; several genes also show cell-type-enhanced patterns involving neutrophils, neutrophil progenitors, erythrocyte progenitors, oligodendrocytes, late spermatids, or smooth muscle cells. This broad and heterogeneous profile does not indicate a coherent tissue-specific program. The neutrophil association means that shared immune-cell composition or blood-related variation could contribute to the conserved co-abundance signal, but the absence of secreted proteins and the generally low immune specificity argue against simply labeling the module as a plasma-protein module or a definitive blood-cell module.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

STRING contains no high-confidence interaction among the module gene pairs and no STRING functional enrichment. Thus, the observed co-abundance edges are not supported by the supplied STRING interaction network. hu.MAP provides a more specific form of support: USP10 and GIGYF2 co-occur as module members in three hu.MAP complexes, tagged (hu.MAP huMAP3_10976.1), (hu.MAP huMAP3_14270.1), and (hu.MAP huMAP3_14559.1). However, each complex contains many additional proteins and only this pair is shared with the module. These results indicate that part of the module may reflect a known protein-complex or translation-associated cellular context involving USP10 and GIGYF2, while the remaining relationships are not established by STRING or hu.MAP. The network should therefore be interpreted primarily as a co-abundance pattern rather than a demonstrated physical interaction complex.

**STRING interactions (score >= 0.7)**: 0 of 15 gene pairs.
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_10976.1 (USP10, GIGYF2; 2/12); huMAP3_14270.1 (USP10, GIGYF2; 2/47); huMAP3_14559.1 (USP10, GIGYF2; 2/47)

### Novelty

The module is a potentially novel cross-tissue co-abundance pattern, but the fact sheet does not establish a new molecular mechanism. Its novelty is supported by the lack of high-confidence STRING links, the lack of STRING enrichment, the absence of a module-wide GO or KEGG term passing global correction, and the limited overlap with hu.MAP, where only USP10 and GIGYF2 recur together in the listed complexes. These observations show that the particular combination and cross-tissue co-abundance relationship is not already explained by the supplied interaction resources. They do not prove biological novelty, because undocumented interactions, indirect regulation, shared cell composition, and technical or sampling effects remain possible.

**Hypothesis.** Hypothesis: the conserved signal may reflect a shared cellular-state program in cervix_uterine and skin that couples RNA and translation control with protein-quality regulation, genome maintenance, epithelial signaling, and cytoskeletal remodeling. USP10 and GIGYF2 may provide a post-translational and post-transcriptional regulatory link, while ERBIN and PPP1R12A connect cellular signaling and actomyosin organization, and POLA1 reflects replication or repair capacity. RBM26 could connect the module to RNA processing. A contribution from neutrophil-related cell composition is also plausible, particularly because USP10 and several other module genes have HPA cell-type associations, but this remains a hypothesis requiring cell-resolved or perturbation-based validation.

### Important genes

#### USP10

- **Related proteins** (co-abundance neighbors): RBM26 (0.82), GIGYF2 (0.81), PPP1R12A (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Immune cell enriched; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_10976.1, huMAP3_14270.1, huMAP3_14559.1
- **Function (MyGene.info)**: ubiquitin specific peptidase 10. Ubiquitin is a highly conserved protein that is covalently linked to other proteins to regulate their function and degradation. This gene encodes a member of the ubiquitin-specific protease family of cysteine proteases. The enzyme specifically cleaves ubiquitin from ubiquitin-conjugated protein substrates. The protein is found in the nucleus and cytoplasm. It functions as a co-factor of the DNA-bo…
- **Diseases (Open Targets)**: tricuspid valve disorder (0.254); Abnormality of the skeletal system (0.221); metabolic disease (0.207); alcohol drinking (0.198); neoplasm (0.117)
- **Europe PMC papers**: 2531
- **Why important**: USP10 is a central network node connected to RBM26, GIGYF2, and PPP1R12A. Its established annotations include protein deubiquitination, regulation of protein stability, autophagy, DNA-damage response, translesion synthesis, and p53-related signaling. It is also the module gene with an HPA immune-cell-enriched neutrophil association and participates with GIGYF2 in all three listed hu.MAP complexes. Its extensive literature and disease-annotation record make it a strong candidate for interpreting the module, while its broad tissue profile prevents a tissue-specific conclusion.
- **Conclusion**: Established evidence supports USP10 as a multifunctional cytosolic and nuclear regulatory protein and as the strongest network bridge between the hu.MAP-supported USP10-GIGYF2 pair and the PPP1R12A and RBM26 edges. It is a plausible driver or marker of the module, but the co-abundance data do not establish that USP10 physically regulates the other module genes or that neutrophils cause the pattern.

#### GIGYF2

- **Related proteins** (co-abundance neighbors): RBM26 (0.84), USP10 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: huMAP3_10976.1, huMAP3_14270.1, huMAP3_14559.1
- **Function (MyGene.info)**: GRB10 interacting GYF protein 2. This gene contains CAG trinucleotide repeats and encodes a protein containing several stretches of polyglutamine residues. The encoded protein may be involved in the regulation of tyrosine kinase receptor signaling. This gene is located in a chromosomal region that was genetically linked to Parkinson disease type 11, and mutations in this gene were thought to be causative for this disease. However…
- **Diseases (Open Targets)**: neurodegenerative disease (0.528); Leber congenital amaurosis 16 (0.525); schizophrenia (0.397); Parkinson disease (0.390); snowflake vitreoretinal degeneration (0.375)
- **Europe PMC papers**: 832
- **Why important**: GIGYF2 is connected to both RBM26 and USP10 and is the second member of the pair recurring in hu.MAP complexes (hu.MAP huMAP3_10976.1), (hu.MAP huMAP3_14270.1), and (hu.MAP huMAP3_14559.1). Its annotations point to post-transcriptional gene silencing, negative regulation of translation and translational initiation, mRNA destabilization, insulin-like growth factor receptor signaling, and negative regulation of type I interferon signaling. It has substantial literature and disease associations, including neurodegenerative and retinal disease annotations.
- **Conclusion**: Established evidence supports GIGYF2 as a translational and mRNA-regulatory protein that provides the clearest complex-level anchor for the module. Its joint occurrence with USP10 supports a possible regulatory context, but it does not demonstrate that the entire module is a translation complex or that GIGYF2 explains the cross-tissue conservation.

#### RBM26

- **Related proteins** (co-abundance neighbors): ERBIN (0.86), GIGYF2 (0.84), USP10 (0.82); STRING partners: none
- **HPA**: Low tissue specificity; Low cell type specificity; blood Low immune cell specificity; location Nuclear speckles; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: RNA binding motif protein 26. Enables RNA binding activity. Predicted to be involved in mRNA processing. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Apr 2022]
- **Diseases (Open Targets)**: neurodegenerative disease (0.495); adolescent idiopathic scoliosis (0.269); schizophrenia (0.263); substance-related disorder (0.175); sialolithiasis (0.161)
- **Europe PMC papers**: 257
- **Why important**: RBM26 has the most connected position in the supplied module graph, linking ERBIN, GIGYF2, and USP10. It is localized to nuclear speckles and is annotated for RNA binding and predicted mRNA processing, with a GO biological-process annotation involving RNA catabolism. It is detected in both tissues and has a broad tissue and cell-type profile. Although its literature base is smaller than that of several other selected genes, its network position makes it important for connecting the RNA-related and signaling-related parts of the module.
- **Conclusion**: Established evidence supports RBM26 as an RNA-associated nuclear protein and a central co-abundance connector. Its role as an organizer of this module is a hypothesis based on network position rather than a demonstrated molecular interaction.

#### ERBIN

- **Related proteins** (co-abundance neighbors): RBM26 (0.86), POLA1 (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Plasma membrane, Cell Junctions; IHC detected in skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: erbb2 interacting protein. This gene is a member of the leucine-rich repeat and PDZ domain (LAP) family. The encoded protein contains 17 leucine-rich repeats and one PDZ domain. It binds to the unphosphorylated form of the ERBB2 protein and regulates ERBB2 function and localization. It has also been shown to affect the Ras signaling pathway by disrupting Ras-Raf interaction. Alternatively spliced transcript variants encodin…
- **Diseases (Open Targets)**: cancer (0.599); alcohol drinking (0.307); tuberculosis (0.257); adolescent idiopathic scoliosis (0.233); ovarian neoplasm (0.212)
- **Europe PMC papers**: 944
- **Why important**: ERBIN links the RBM26-centered portion of the graph to POLA1. It is a membrane and cell-junction protein of the LAP family, binds unphosphorylated ERBB2, and is annotated for ERBB2 localization, Ras signaling, cytoskeleton organization, and keratinocyte differentiation. It is detected in skin but not cervix_uterine by HPA IHC, despite the module being conserved across the tissue pair. Its substantial literature and cancer-related disease annotations make it biologically important for an epithelial interpretation.
- **Conclusion**: Established evidence supports ERBIN as an epithelial signaling, junctional, and cytoskeletal regulator. Its skin-specific detection and its edge to POLA1 are compatible with tissue-state or cellular-composition effects, but they do not establish that ERBIN mechanistically links epithelial signaling to DNA replication in this module.

#### POLA1

- **Related proteins** (co-abundance neighbors): ERBIN (0.84); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Nucleoplasm; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: DNA polymerase alpha 1, catalytic subunit. This gene encodes the catalytic subunit of DNA polymerase, which together with a regulatory and two primase subunits, forms the DNA polymerase alpha complex. The catalytic subunit plays an essential role in the initiation of DNA replication. [provided by RefSeq, Mar 2010].
- **Diseases (Open Targets)**: X-linked reticulate pigmentary disorder (0.747); X-linked intellectual disability, van Esch type (0.731); acute lymphoblastic leukemia (0.598); non-small cell lung carcinoma (0.593); B-cell chronic lymphocytic leukemia (0.590)
- **Europe PMC papers**: 1674
- **Why important**: POLA1 is the catalytic subunit of DNA polymerase alpha and is connected to ERBIN in the module graph. Its established annotations concern DNA replication initiation, primer synthesis, strand elongation, and DNA synthesis involved in repair. It is detected in both tissues and has substantial literature and disease associations, including X-linked disorders and hematologic and solid malignancies. Although it is a peripheral network member, its function provides a distinct genome-maintenance axis within an otherwise mixed module.
- **Conclusion**: Established evidence supports POLA1 as a core DNA-replication and repair enzyme. Its presence may indicate variation in proliferative or repair-related cellular state, but the module does not show enough pathway-level evidence to conclude that DNA replication is its principal function.

#### PPP1R12A

- **Related proteins** (co-abundance neighbors): USP10 (0.81); STRING partners: none
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Actin filaments, Cytosol; IHC detected in cervix_uterine, skin
- **hu.MAP 3.0**: no complex with >= 2 module members
- **Function (MyGene.info)**: protein phosphatase 1 regulatory subunit 12A. Myosin phosphatase target subunit 1, which is also called the myosin-binding subunit of myosin phosphatase, is one of the subunits of myosin phosphatase. Myosin phosphatase regulates the interaction of actin and myosin downstream of the guanosine triphosphatase Rho. The small guanosine triphosphatase Rho is implicated in myosin light chain (MLC) phosphorylation, which results in contraction of smo…
- **Diseases (Open Targets)**: genitourinary and/or brain malformation syndrome (0.777); neurodegenerative disease (0.572); hereditary disease (0.415); holoprosencephaly (0.371); Genetic 46,XY disorder of sex development (0.370)
- **Europe PMC papers**: 1121
- **Why important**: PPP1R12A is connected to USP10 and encodes the myosin phosphatase target subunit. Its annotations link it to actomyosin regulation downstream of Rho, protein dephosphorylation, cell adhesion, signal transduction, and the mitotic cell cycle. HPA associates it with neutrophils, neutrophil progenitors, and smooth muscle cells, while detecting it in both tissues. Its literature and disease-annotation record is substantial, and its position adds a cytoskeletal and contractility component to the module.
- **Conclusion**: Established evidence supports PPP1R12A as a regulator of myosin phosphatase, cell adhesion, and actomyosin behavior. Its connection to USP10 may reflect coordinated cellular-state regulation, but a direct USP10-PPP1R12A mechanism is not demonstrated by the supplied interaction evidence.
