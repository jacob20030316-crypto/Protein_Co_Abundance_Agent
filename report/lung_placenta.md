# Conserved co-abundance modules: lung and placenta

## Module 0

**Tissue pair**: lung and placenta  
**Genes (6)**: HSPA5, GANAB, HNRNPK, HYOU1, PDIA4, PLIN3

### Function

The module is best interpreted as an endoplasmic-reticulum protein-folding, glycoprotein-quality-control, and cellular-stress module. This interpretation is supported by the functions of HYOU1, HSPA5, PDIA4, and GANAB, by their tightly connected STRING subnetwork, and by their membership in hu.MAP complexes (hu.MAP huMAP3_06775.1), (hu.MAP huMAP3_09327.1), and (hu.MAP huMAP3_07455.1). The supplementary STRING results link part of the module to protein processing in the endoplasmic reticulum (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0212) and to an unfolded-protein-response and stress-signaling context (STRING NetworkNeighborAL Photodynamic therapy-induced unfolded protein response, and IRE1-TRAF2-ASK1 complex; within-query FDR = 0.0447). These STRING findings are supportive rather than globally corrected enrichment evidence. No GO or KEGG term passed global correction, so there is no globally significant GO or KEGG enrichment claim for this module. HNRNPK and PLIN3 form a smaller peripheral branch, consistent with RNA-processing and lipid-droplet or vesicle-related biology, but they do not independently establish a second module function.

**Cell composition.** The module is not strongly tissue-specific: every gene has low tissue specificity in HPA, and all proteins were detected in placenta while nearly all were detected in lung. HPA reports low immune-cell specificity for every gene, so the module is not best explained as a blood-cell-enriched module. HPA also identifies plasma cells and extravillous trophoblasts among recurring enhanced cell types, with syncytiotrophoblast enhancement for part of the module; this raises the possibility that shared cellular composition, particularly placental trophoblast biology or a related secretory cell state, contributes to the cross-tissue signal. The HPA summary classifies four genes as secreted genes, although the individual annotations mainly place the core proteins in intracellular or ER-associated compartments. Thus, the module could partly reflect a broadly expressed secretory or stress-related program rather than a lung- and placenta-exclusive mechanism. HNRNPK is nucleoplasmic and PLIN3 is associated with lipid droplets, showing that the module is not compositionally uniform.

**GO/KEGG enrichment**: 0 terms pass global BH (q_global < 0.05).

### STRING and hu.MAP

Known relationships are concentrated in the ER-protein-folding core. STRING supports the connections among GANAB, HSPA5, HYOU1, and PDIA4, including particularly strong links within the HSPA5-HYOU1-PDIA4 group and a strong GANAB connection to that group. The same three genes GANAB, HYOU1, and PDIA4 recur in hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), while HSPA5 and HYOU1 occur together in (hu.MAP huMAP3_07455.1). These convergent resources indicate that the central co-abundance pattern largely recapitulates known molecular relationships and complexes, rather than representing an entirely unexplored interaction network. HNRNPK and PLIN3 have no reported STRING partners or hu.MAP complexes in the supplied evidence, so their links to the ER core are less independently supported and may represent co-regulation, indirect biology, or tissue-state coupling.

**STRING interactions (score >= 0.7)**: 6 of 15 gene pairs: GANAB–HSPA5 (0.846); GANAB–HYOU1 (0.83); GANAB–PDIA4 (0.717); HSPA5–HYOU1 (0.999); HSPA5–PDIA4 (0.99); HYOU1–PDIA4 (0.997)
**STRING functional enrichment (supplementary, within-query FDR)**: KEGG Protein processing in endoplasmic reticulum (FDR = 0.0212, 4 genes); NetworkNeighborAL Photodynamic therapy-induced unfolded protein response, and IRE1-TRAF2-ASK1 complex (FDR = 0.0447, 3 genes)
**hu.MAP 3.0 complexes with >= 2 module members**: huMAP3_06775.1 (PDIA4, GANAB, HYOU1; 3/60); huMAP3_09327.1 (PDIA4, GANAB, HYOU1; 3/93); huMAP3_07455.1 (HSPA5, HYOU1; 2/4)

### Novelty

The module should not be described as a wholly new protein-complex discovery. Most of its central relationships and complex memberships are already represented in STRING and hu.MAP, and the ER-folding interpretation is consistent with established gene functions. Its potentially novel aspect is the coordinated co-abundance of this ER-quality-control core with HNRNPK and PLIN3 across lung and placenta, and the specific conservation of that pattern between these tissues. That cross-tissue organization may be biologically informative even though the underlying molecular interactions are known. Absence of database support for the HNRNPK-PLIN3 branch does not by itself prove novelty; it may reflect indirect regulation, context dependence, incomplete database coverage, or a sample-composition effect.

**Hypothesis.** Hypothesis: a shared secretory-cell or stress-adapted state in lung and placenta increases ER protein folding, glycoprotein maturation, disulfide-bond formation, and unfolded-protein handling. HSPA5 and HYOU1 could provide chaperone and stress-response capacity, PDIA4 could support oxidative folding and antibody or secretory-protein assembly, and GANAB could process immature N-glycoproteins. The HNRNPK-PLIN3 branch may couple this state to RNA processing and lipid-droplet or vesicle metabolism. This is a mechanistic hypothesis rather than a demonstrated causal pathway, because the module has no globally significant GO or KEGG term and co-abundance does not establish directionality or physical causation.

### Important genes

#### HSPA5

- **Related proteins** (co-abundance neighbors): GANAB (0.84), HYOU1 (0.82); STRING partners: GANAB (0.846), HYOU1 (0.999), PDIA4 (0.99)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Cytosol, Annulus; IHC detected in lung, placenta
- **hu.MAP 3.0**: huMAP3_07455.1
- **Function (MyGene.info)**: heat shock protein family A (Hsp70) member 5. The protein encoded by this gene is a member of the heat shock protein 70 (HSP70) family. This protein localizes to the lumen of the endoplasmic reticulum (ER) where it operates as a typical HSP70 chaperone involved in the folding and assembly of proteins in the ER and is a master regulator of ER homeostasis. During cellular stress, as during viral infection or tumorogenesis, this protein interact…
- **Diseases (Open Targets)**: dengue disease (0.512); neurodegenerative disease (0.469); glioblastoma (0.121); neoplasm (0.120); cancer (0.118)
- **Europe PMC papers**: 12403
- **Why important**: HSPA5 is a central member of the ER-associated STRING network, connects to HYOU1, PDIA4, and GANAB, and participates in hu.MAP complex (hu.MAP huMAP3_07455.1). Its established function is that of an ER HSP seventy chaperone and master regulator of ER homeostasis, including protein folding and the unfolded-protein response. It has by far the largest literature volume in this module, making it the best-established biological anchor and the strongest candidate for interpreting the module's stress and folding signal.
- **Conclusion**: Established evidence supports HSPA5 as a core ER chaperone and homeostasis regulator that explains much of the module's function. A role as the main driver of the conserved lung-placenta co-abundance pattern is plausible but remains a hypothesis, because network co-abundance does not demonstrate regulatory causation.

#### HYOU1

- **Related proteins** (co-abundance neighbors): PDIA4 (0.84), HNRNPK (0.82), HSPA5 (0.82); STRING partners: GANAB (0.83), HSPA5 (0.999), PDIA4 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location None; IHC detected in placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1, huMAP3_07455.1
- **Function (MyGene.info)**: hypoxia up-regulated 1. The protein encoded by this gene belongs to the heat shock protein 70 family. This gene uses alternative transcription start sites. A cis-acting segment found in the 5' UTR is involved in stress-dependent induction, resulting in the accumulation of this protein in the endoplasmic reticulum (ER) under hypoxic conditions. The protein encoded by this gene is thought to play an important role in prote…
- **Diseases (Open Targets)**: granulocytopenia with immunoglobulin abnormality (0.567); neurodegenerative disease (0.537); dengue disease (0.370); coronary artery disorder (0.337); type 2 diabetes mellitus (0.233)
- **Europe PMC papers**: 1543
- **Why important**: HYOU1 has the greatest network connectivity in the module and links the ER core to HNRNPK as well as to HSPA5 and PDIA4. It is present in all listed hu.MAP complexes (hu.MAP huMAP3_06775.1), (hu.MAP huMAP3_09327.1), and (hu.MAP huMAP3_07455.1), and appears in both supplementary STRING functional contexts (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0212) and (STRING NetworkNeighborAL Photodynamic therapy-induced unfolded protein response, and IRE1-TRAF2-ASK1 complex; within-query FDR = 0.0447). Its established biology includes hypoxia and ischemia responses, ER stress, protein folding, secretion, and prevention of apoptosis, which is especially relevant to tissues exposed to variable oxygen and secretory demands. It also has substantial literature and disease associations involving stress-related and systemic disorders.
- **Conclusion**: Established evidence supports HYOU1 as a stress-responsive ER folding and secretion factor and as a topological bridge between the ER core and the peripheral branch. Its possible role in linking hypoxia adaptation to secretory-cell behavior in lung and placenta is a hypothesis.

#### PDIA4

- **Related proteins** (co-abundance neighbors): GANAB (0.85), HYOU1 (0.84); STRING partners: GANAB (0.717), HSPA5 (0.99), HYOU1 (0.997)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung, placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: protein disulfide isomerase family A member 4. This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhan…
- **Diseases (Open Targets)**: neurodegenerative disease (0.529); neoplasm (0.097); liver disorder (0.096); ovarian carcinoma (0.094); ovarian cancer (0.094)
- **Europe PMC papers**: 1539
- **Why important**: PDIA4 is a central ER node connected to HSPA5, HYOU1, and GANAB, occurs in hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1), and contributes to both supplementary STRING contexts (STRING KEGG Protein processing in endoplasmic reticulum; within-query FDR = 0.0212) and (STRING NetworkNeighborAL Photodynamic therapy-induced unfolded protein response, and IRE1-TRAF2-ASK1 complex; within-query FDR = 0.0447). Its established function is catalysis of protein folding and thiol-disulfide interchange in the ER; it also supports immunoglobulin disulfide bonding and antibody assembly. Its disease associations and substantial literature make it an informative marker of secretory-protein folding capacity rather than merely a generic co-abundance partner.
- **Conclusion**: Established evidence supports PDIA4 as an ER oxidative-folding and secretory-protein assembly component within the conserved core. Its possible contribution to trophoblast or plasma-cell-like secretory activity is a hypothesis suggested by HPA cell-type annotations, not a demonstrated mechanism.

#### GANAB

- **Related proteins** (co-abundance neighbors): PDIA4 (0.85), HSPA5 (0.84); STRING partners: HSPA5 (0.846), HYOU1 (0.83), PDIA4 (0.717)
- **HPA**: Low tissue specificity; Cell type enhanced; blood Low immune cell specificity; location Endoplasmic reticulum; IHC detected in lung, placenta
- **hu.MAP 3.0**: huMAP3_06775.1, huMAP3_09327.1
- **Function (MyGene.info)**: glucosidase II alpha subunit. This gene encodes the alpha subunit of glucosidase II and a member of the glycosyl hydrolase 31 family of proteins. The heterodimeric enzyme glucosidase II plays a role in protein folding and quality control by cleaving glucose residues from immature glycoproteins in the endoplasmic reticulum. Expression of the encoded protein is elevated in lung tumor tissue and in response to UV irradiation. Mut…
- **Diseases (Open Targets)**: polycystic kidney disease 3 with or without polycystic liver disease (0.792); autosomal dominant polycystic liver disease (0.515); autosomal dominant polycystic kidney disease (0.470); Biliary tract abnormality (0.438); COVID-19 (0.370)
- **Europe PMC papers**: 1240
- **Why important**: GANAB connects to HSPA5, HYOU1, and PDIA4 in STRING and is included with HYOU1 and PDIA4 in hu.MAP complexes (hu.MAP huMAP3_06775.1) and (hu.MAP huMAP3_09327.1). It encodes the alpha subunit of glucosidase II, an ER glycoprotein-quality-control enzyme involved in N-glycan processing and protein folding. HPA detects it in both lung and placenta and identifies enhancement in extravillous trophoblasts. Its established disease associations, including autosomal-dominant polycystic kidney and liver disease, add functional and clinical relevance.
- **Conclusion**: Established evidence supports GANAB as the glycoprotein-processing component of the ER-quality-control core. Its trophoblast-associated expression may help explain conservation in placenta, but whether it contributes specifically to the cross-tissue module rather than reflecting general secretory activity is a hypothesis.
