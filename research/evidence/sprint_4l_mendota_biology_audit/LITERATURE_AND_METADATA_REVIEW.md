# Literature and Metadata Review — Mendota Phytoplankton

**Date:** 2026-11-23T23:58:36.852965+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Dataset metadata (primary)

- `knb-lter-ntl.88.31`: 1995-01-24 to 2020-12-31; 4 Madison lakes; one CSV `ntl88_v13.csv`, 2,448,830 B, MD5 `a0363cc7fdfd6c12889750fea27bd542`; 15 columns.
- Mendota: 0–8 m composite; tube sampler at deep hole; glutaraldehyde; PhycoTech slides; Utermöhl; species-level counts; cells/mL, biovolume, biomass.
- Sampling: biweekly late Mar/Apr–early Sep; every 4 weeks to late Nov; usually one winter sample.
- February 2013 taxonomic updates (name changes, genus-to-species, slide revisits).
- Intellectual rights: CC BY 4.0.

## 2. Versioning

- Revision 31 published 2022-11-17 (DOI `10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9`).
- Revision 32 published 2026-05-18 (DOI `10.6073/pasta/19888a181707748619d28cad7ca5ff74`).
- **Same data entity**: `ntl88_v13.csv`, 2,448,830 B, MD5 `a0363cc7fdfd6c12889750fea27bd542`. Metadata differs (33,523 vs 27,408 B; different SHA256), but data object is identical by size/MD5.
- Consequence: acquiring 88.31 gives the same data bytes as 88.32; cite the current revision/DOI for provenance, but do not assume the metadata text is identical.

## 3. Sampling and laboratory methods

- NTL Protocols page: routine sampling biweekly summer/monthly non-summer; phytoplankton biovolume for Mendota/Monona; archived mounted slides.
- Carey et al. 2016 (J Plankton Res 38:27–40, DOI 10.1093/plankt/fbv116): 1995–2010; integrated 8-m tube; 0–8 m composite; glutaraldehyde; >400 natural units/sample; Utermöhl modification; biovolume for up to 15 units/species; Hillebrand geometry; **same taxonomist throughout 1995–2010 (A.L.S.)**.
- PhycoTech materials: Ann L. St. Amand was the sole enumerator of algal samples; company claims 95%+ in-house QA precision; she died 7 October 2023. This supports analyst continuity through 2020 but is self-reported.
- EML: species may not have been determined for all slides; multiple entries per species/date may be variants/vegetative states.

## 4. Biovolume and biomass

- Biovolume from measured cell dimensions matched to geometric solids; average cell biovolume × cell density.
- 10^6 µm³/mL = 1 mm³/mL; assuming cell density ≈ water, 1 mm³/mL ≈ 1 mg/L biomass.
- Hillebrand et al. 1999 and HELCOM/NERC guidance support geometric biovolume, but different shape/equation choices and biomass conversion assumptions can introduce differences.
- **No detection limits or QC flags** in the EML/schema.

## 5. Taxonomic consistency and QC

- Taxonomic bias study (2022): non-zero bias between original and QA samples; total biovolume, cell density and diversity often robust, but not guaranteed.
- Lake Zurich long-term series (rejoinder): taxonomic learning and detection-limit changes can produce step changes; coarser aggregation does not necessarily fix consistency.
- Intercalibration (2024): CV 10–42% for professionals, 8–57% for non-professionals; 4–19% when one person counts. This supports both the value of a single analyst and the reality of non-zero uncertainty.
- **Implication:** Mendota's long-term single-analyst record is a strength for consistency, but not proof of accuracy; 2013 updates and possible later changes require harmonisation.

## 6. Temporal resolution

- "Hit or miss?" (2024): weekly/biweekly sampling resolves general community composition but can miss or underestimate short blooms; at least twice-weekly sampling is advisable for precise bloom timing/comparison.
- Sensor-validation studies: high-frequency fluorometry captures short-term variability but community composition, biofouling and calibration affect readings; regular lab validation is essential.
- Mendota phytoplankton is biweekly (ice-free) to monthly (late season/under ice), so it cannot resolve sub-biweekly onset. It can support seasonal to multi-week comparisons, not daily warning.

## 7. Mendota prior art

- Carpenter et al. 2020 (Limnol Oceanogr Lett 5:331–336): 1-min phycocyanin/chlorophyll 2008–2018, Turner Cyclops 7 at 1 m, single central station, ~250k observations/year; two alternative states; stochastic transitions; **sensor proxy**, not microscopy.
- Beal et al. 2022 (Lake Reserv Manage 39:37–52): 1995–2018 cyanobacteria biomass from biovolume; season-ahead forecast; prior Mendota models; data limitations and short record noted.
- O'Brien et al. 2023 (Nat Commun 14:7942): nine lakes incl. Mendota; EWS generally poor on empirical data; multivariate weakly superior; cautions against assuming critical-transition early warning.
- PNAS 2023 invasions paper: long-term Mendota phytoplankton/microbial phenology shifts; supports complex drivers and non-stationarity.
- **No novelty claim is supportable.** The dataset has been used for Mendota phytoplankton succession and forecasting.

## 8. What is verified vs source-reported

**Verified from primary metadata:** package IDs, DOI, entity ID, objectName, size, MD5, schema, coverage, methods text, CC BY.
**Source-reported (not independently re-audited):** same taxonomist 1995–2010; PhycoTech sole enumerator/95% QA; literature performance claims.
**Unverified:** raw row counts, Mendota subset, missingness, duplicates, detection limits, actual taxonomic consistency, 2010–2020 analyst continuity.

## 9. Conflicting/limiting evidence

- PhycoTech self-reported QA vs independent evidence of long-term taxonomic inconsistency.
- HF sensor studies show useful pigment proxies vs O'Brien's caution that empirical EWS often fail.
- Dataset size/long record vs biweekly resolution and composite depth mismatch with point sensors.

## 10. Sources actually inspected

See `EXTERNAL_SEARCH_LOG.md` for the full table. Key primary sources: EML 88.31/88.32; DataONE CN sysmeta/ORE; NTL protocols page; NSF PAR 10493157; Carey et al. 2016; Carpenter et al. 2020; Beal et al. 2022; O'Brien et al. 2023; PhycoTech materials. PDFs were not parsed with a PDF library; HTML/abstract/method excerpts were inspected where available.
