# Gate 2G — Painter 2019-07-17 Anomaly Investigation

**Project:** EcoSentinel — Detecting Early Changes in Freshwater Ecosystems Using Multivariate Time-Series Analysis  
**Date:** 2026-11-22  
**Status:** Investigation complete within accessible evidence. **Anomaly remains unresolved. Gate 2 NOT approved. No labels created.**

## 1. Purpose

Reinspect the 2019-07-17 (DOY 198) Painter 2022 observation flagged in Gate 2D/2E as an unresolved anomaly: very low total biomass (45.81 mg/m3) between high-biomass neighbors (DOY 191: 12587.13; DOY 210: 9497.89), with high cyanobacteria proportion (89.54%).

## 2. Sources inspected

| Source | Path | Role |
|---|---|---|
| Painter 2022 taxonomy 2019 | `research/evidence/gate2d/painter_2022_borealis/BP_PhytoTax_2019_KP.csv` | Original taxon-level records |
| Painter 2022 group biomass 2019 | `research/evidence/gate2d/painter_2022_borealis/BP_GroupsBiomass_2019_KP.csv` | Group aggregation check |
| Painter 2022 toxins 2019 | `research/evidence/gate2d/painter_2022_borealis/BP_2019_toxins_0.8.csv` | Same-date toxin sample check |
| Painter 2022 README | `research/evidence/gate2d/painter_2022_borealis/README.md` | Dataset documentation |
| Gate 2E derived summary | `research/evidence/gate2d/derived/painter_summary.json` | Reproducible prior extraction |

No raw files were modified.

## 3. Taxonomy record check (DOY 198)

From `BP_PhytoTax_2019_KP.csv` (verified by direct inspection and Gate 2E script):

- **n rows:** 9
- **DOY:** 198
- **Location:** Buffalo Pound
- **Depth:** 0.8 m
- **REP:** REP2 (all 9 rows)
- **Sample IDs:** present in schema; rows correspond to DOY 198 records (see source CSV).
- **Total biomass:** 45.81 mg/m3
- **Cyanophyte biomass:** 41.02 mg/m3 (89.54%)
- **Taxa:** 9 total; 4 cyanophyte taxa

| REP | Species | Biomass (mg/m3) | Group |
|---|---|---:|---|
| REP2 | Aphanizomenon flos-aquae Ralfs and ... | 9.4 | Cyanophyte |
| REP2 | Microcystis aeruginosa (Kutzing) Ku... | 3.5 | Cyanophyte |
| REP2 | Anabaena crassa (Lemm.) Kom-Legn. &... | 17.37 | Cyanophyte |
| REP2 | Anabaena flos-aquae (Lyngb.) Breb. ... | 10.75 | Cyanophyte |
| REP2 | Oocystis lacustris Chodat | 0.2 | Chlorophyte |
| REP2 | Small chrysophyceae | 1.34 | Chrysophyte |
| REP2 | Aulacoseira italica v subarctica (O... | 2.05 | Diatom |
| REP2 | Rhodomonas minuta Skuja | 0.6 | Cryptophyte |
| REP2 | Cryptomonas rostratiformis Skuja | 0.6 | Cryptophyte |

**Observation:** Biomass units are `Biomass_mg_m3` (same field name as other 2019 rows). Values are small but internally consistent decimals; no obvious parsing artifact identified.

## 4. Group biomass cross-check

`BP_GroupsBiomass_2019_KP.csv` DOY 198 rows agree with taxonomy aggregation:

| Group | total_biomass | grand_total_biomass | biomass_prop |
|---|---:|---:|---:|
| Chlorophyte | 0.2 | 45.81 | 0.436585898 |
| Chrysophyte | 1.34 | 45.81 | 2.925125518 |
| Cryptophyte | 1.2 | 45.81 | 2.619515389 |
| Cyanophyte | 41.02 | 45.81 | 89.54376774 |
| Diatom | 2.05 | 45.81 | 4.475005457 |

**Conclusion:** No taxonomy/group-biomass aggregation discrepancy detected.

## 5. Replicate/sample identity

- All DOY 198 taxonomy rows are `REP2`. No REP1 rows exist for DOY 198 in the 2019 taxonomy file.
- Neighboring dates include REP1 and REP2 (e.g., DOY 191 REP2, DOY 210 REP1 per Gate 2E summary). The dataset includes REP designations but README/metadata do not fully explain REP2 meaning in this context.
- **Cannot establish** from accessible files alone whether REP2 indicates a routine replicate, replacement sample, alternate lab/count, or other designation.

## 6. Toxin record check

`BP_2019_toxins_0.8.csv` (latin-1/irregular wide format) contains 2019-07-17 sample `25993` in three fractions:

| Sample | Date | Description | Fraction | Depth | Other fields (raw, partially parsed) |
|---|---|---|---|---:|---|
| 25993 | 2019-07-17 | Buffalo Pound (UofS)-Non_filtré | Non_filtré | 0.8 | 2020-08-14, 1045.3, 90.7, ..., 2020-09-21, <135 |
| 25993 | 2019-07-17 | Buffalo Pound (UofS)-Extracellulaire | Extra (filtrat) | 0.8 | 2020-08-14, 511.3, 29, ..., 2020-09-21, <135 |
| 25993 | 2019-07-17 | Buffalo Pound (UofS)-Intracellulaire | Intra (filtre) | 0.8 | 2020-07-28, 627.9, 8.3, ..., 2020-08-03, <5 |

**Observations:**
- Same date and same sample ID `25993` appear in toxin file; depth 0.8 m matches.
- Toxin file has complex header/LOD/LOQ structure and mixed languages/encodings; compound columns and units are **not fully verified**.
- Presence of same-date toxin sample confirms a related sample exists, but does not resolve taxonomy biomass anomaly or confirm quantitative toxin interpretation.

## 7. Plausible explanations (none confirmed)

| Hypothesis | Support | Against / unknown | Status |
|---|---|---|---|
| Genuine low-biomass patch/sample at 0.8 m | Possible in dynamic shallow lake | Contradicted by high neighbors and same-date toxin sample existence; no field note | Unconfirmed |
| Replicate/replacement sample with different context | REP2 present; no REP1 same day | Meaning of REP2 not documented in accessible README | Unconfirmed |
| Subsampling/counting/transcription error | Very low total biomass and few taxa | Group file agrees with taxonomy aggregation; no obvious parse error | Unconfirmed |
| Sample handling/filtration issue affecting biomass record | Toxin file shows multiple fractions | No documented lab QA note in accessible files | Unconfirmed |
| Real short-lived community shift | Ecologically possible but unusual | 7-day gap before and 12-day gap after; cannot confirm | Unconfirmed |

## 8. What can and cannot be established

**Can be established:**
- DOY 198 is present in taxonomy and group-biomass files with consistent values across those files.
- All taxonomy rows are REP2, Buffalo Pound, 0.8 m.
- Biomass is unusually low relative to adjacent sampled dates.
- Toxin file contains same-date sample 25993 with three fractions; same depth.

**Cannot be established from accessible evidence:**
- Whether REP2 is a replacement/replicate/QA sample.
- Whether the observation is a field/lab artifact or genuine biological condition.
- Quantitative toxin interpretation for 2019-07-17 (format/units/compound mapping unverified).
- Whether any correction is warranted.

## 9. Handling decision (Gate 2G)

- **No correction, deletion, or silent reinterpretation applied.**
- Retain DOY 198 as an explicit uncertainty in any exploratory/candidate analysis.
- Any future candidate interval spanning DOY 191–210 must carry an unresolved-anomaly flag.
- Do not treat DOY 198 as confirmed non-bloom or bloom termination.

## 10. Reproducibility

- Prior derived summary: `python3 research/evidence/gate2d/derived/analyze_painter.py`
- Direct inspection used in Gate 2G: `python3 /tmp/inspect_tox.py` (ad hoc; logic captured in this report). For reproducibility, the toxin-file structure should be parsed with a dedicated, documented script if used in future analysis.
- Source checksums: as recorded in Gate 2D inventory and Borealis metadata.