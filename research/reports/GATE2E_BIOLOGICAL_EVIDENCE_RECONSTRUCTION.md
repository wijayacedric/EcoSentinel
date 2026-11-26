# Gate 2E — Biological Evidence Reconstruction, Remaining Evidence Resolution, and Human-Decision Preparation

**Project:** EcoSentinel — Detecting Early Changes in Freshwater Ecosystems Using Multivariate Time-Series Analysis  
**Research question:** "Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?"  
**Primary dataset:** Buffalo Pound Lake, Saskatchewan, Canada (DOI: 10.20383/103.01100)  
**Date:** 2026-11-22  
**Status:** Gate 2E assessment complete within authorised scope. **Gate 2 NOT approved. No labels created. No modeling performed. No Gate 4 started.**  
**Author:** OpenCode (primary research execution agent)

## 1. Executive summary

Gate 2E inspected the actual downloaded Painter 2022 source files and BPWTP annual reports, generated reproducible derived summaries, investigated the 2019-07-17 anomaly, assessed interval-censored candidate evidence, and reassessed Gate 2 feasibility.

**What was verified:**
- Painter 2022 in-repo evidence (`research/evidence/gate2d/painter_2022_borealis/`) contains 2018 and 2019 phytoplankton taxonomy, group biomass, toxin, nutrient, and README files with checksums matching Borealis metadata. A reproducible derived summary was generated at `research/evidence/gate2d/derived/painter_summary.json` using `research/evidence/gate2d/derived/analyze_painter.py`.
- 2018: 25 discrete sampling dates (DOY 149–260, 2018-05-29–2018-09-17), gaps 1–12 days (median 4). 2019: 17 discrete dates (DOY 149–276, 2019-05-29–2019-10-03), gaps 4–16 days (median 7.5).
- The 2019-07-17 (DOY 198) anomaly is confirmed in source files: 9 taxonomy rows, all `REP2`, same location/depth (Buffalo Pound, 0.8 m), total biomass 45.81 mg/m3, cyanophyte 41.02 mg/m3 (89.54% of total). Group biomass file agrees exactly. Neighboring dates are high-biomass (DOY 191: 12587.13 total, 11919.83 cyano; DOY 210: 9497.89 total, 6755.17 cyano). Toxin file contains same-date sample ID 25993 with three fractions (non-filtered/extracellular/intracellular), but the toxin CSV format/encoding/compound mapping remains not fully verified for confirmed-evidence use. The anomaly remains **unresolved**.
- BPWTP 2014–2021 annual reports (public PDFs in `research/evidence/gate2d/bpwtp_reports/`) were previously downloaded and text-extracted. Re-verification of the derived extraction confirms monthly raw/treated microcystin tables for 2017–2021 (May–Oct), a 2016 narrative with July/September measurements and peak 7 µg/L raw, and limited 2014–2015 annual organics screening entries. This is independent lab toxin evidence but sparse, intake-located, and not phytoplankton taxonomy/biovolume.

**What this means for Gate 2:**
- Painter provides independent biological observations at discrete sampling occasions. It can support **candidate, interval-censored biological observations**, not approved bloom events and not continuous non-bloom exposure.
- **0 independently reconstructed biological bloom events** can be confirmed from accessible evidence under pre-approved biological-only criteria.
- **No defensible independent non-bloom exposure denominator** can be established.
- **Matched-FAR confirmatory evaluation remains not defensible.**
- **Final recommendation: C — Exploratory only.**

## 2. Source inventory

| Source | Location | Type | Access | Independence (method) | Role |
|---|---|---|---|---|---|
| Painter 2022 dataset | `research/evidence/gate2d/painter_2022_borealis/` (Borealis DOI 10.5683/SP3/MP6NXF, CC BY-NC-SA 4.0) | Public biological dataset | Downloaded, checksums verified | Microscopy/taxonomy/biomass independent of buoy RFU | Primary candidate biological observations (2018–2019) |
| Painter 2022 paper | DOI 10.1039/D2EM00078D | Peer-reviewed paper | Metadata/abstract level previously accessed | Descriptive | Context; no event ground truth by itself |
| BPWTP annual reports 2014–2021 | `research/evidence/gate2d/bpwtp_reports/annual-report-2014.pdf`–`2021.pdf` | Public PDFs | Downloaded | Lab microcystin assay independent of buoy RFU | Toxin-context evidence; sparse |
| BPWTP microcystin extraction | `research/evidence/gate2d/bpwtp_reports/bpwtp_microcystin_extract.txt` | Derived text | Derived 2026-11-22 | Derived from independent lab reports | Verification aid; not original |
| Painter derived summary | `research/evidence/gate2d/derived/painter_summary.json`, `analyze_painter.py` | Derived | Generated 2026-11-22 | Derived from original Painter files | Reproducible summary |
| Boyer 2025 | DOI 10.1111/fwb.70131 | Peer-reviewed paper | Full text previously accessed; SI/raw inaccessible | Biological assays independent methods; phase boundaries mixed | Publication-level 2017 context; not reconstructable |
| Boyer 2021 thesis | USask HARVEST 10388/13318 | Public thesis | Accessed/text-searched 2026-11-22 | Publication-level | Corroboration only |
| WSA Primary Station portal | https://waterquality.saskatchewan.ca/PrimaryStation | Public portal | Inspected 2026-11-22 | Chemical/field params; no phytoplankton/toxin visible | Not usable for biological event reconstruction |
| Buffalo Pound buoy dataset | DOI 10.20383/103.01100 | Primary predictor dataset | In project scope | Not independent ground truth | Predictor/evaluation data only |

## 3. Painter 2018 biological reconstruction

### 3.1 Sampling record (verified from source files)

- **n dates:** 25
- **Date span:** DOY 149–260 (2018-05-29 to 2018-09-17)
- **Gaps:** min 1 day, median 4 days, max 12 days
- **Location/depth:** Buffalo Pound, 0.8 m (per rows inspected)
- **Replicates:** no `REP` field populated in 2018 taxonomy rows (REP column absent in schema); sample IDs present.
- **Measurements:** species-level cell density (cells/L), biomass (mg/m3), biovolume dimensions, taxonomic group/phylum/family/genus/species.

| DOY | Rows | Taxa | Cyano taxa | Total biomass (mg/m3) | Cyano biomass (mg/m3) | Cyano proportion | Interval note |
|---:|---:|---:|---:|---:|---:|---:|---|
| 149 | 37 | 35 | 6 | 716.82 | 11.60 | 0.016 | Low cyano observation |
| 158 | 23 | 23 | 3 | 183.37 | 33.62 | 0.183 | Low-moderate |
| 164 | 38 | 37 | 7 | 691.13 | 338.04 | 0.489 | Mixed |
| 170 | 21 | 21 | 4 | 3826.27 | 2718.13 | 0.710 | Cyano-dominant observation |
| 172 | 25 | 25 | 6 | 1464.32 | 974.05 | 0.665 | Cyano-dominant observation |
| 176 | 27 | 27 | 5 | 2197.33 | 693.55 | 0.316 | Mixed |
| 184 | 31 | 31 | 6 | 4119.66 | 2858.26 | 0.694 | Cyano-dominant observation |
| 187 | 31 | 30 | 7 | 9319.53 | 6365.96 | 0.683 | Cyano-dominant observation |
| 190 | 30 | 30 | 7 | 9333.71 | 8019.97 | 0.859 | Cyano-dominant observation |
| 193 | 24 | 24 | 5 | 3041.02 | 2554.70 | 0.840 | Cyano-dominant observation |
| 197 | 37 | 35 | 8 | 13501.24 | 10898.69 | 0.807 | Cyano-dominant observation |
| 199 | 41 | 39 | 7 | 8404.02 | 5540.45 | 0.659 | Cyano-dominant observation |
| 205 | 31 | 30 | 6 | 8985.01 | 6350.60 | 0.707 | Cyano-dominant observation |
| 206 | 34 | 33 | 7 | 3333.97 | 2569.45 | 0.771 | Cyano-dominant observation |
| 211 | 39 | 38 | 6 | 8923.06 | 6775.20 | 0.759 | Cyano-dominant observation |
| 212 | 35 | 34 | 7 | 6993.96 | 5637.93 | 0.806 | Cyano-dominant observation |
| 220 | 38 | 37 | 7 | 10287.72 | 8451.34 | 0.822 | Cyano-dominant observation |
| 221 | 38 | 36 | 6 | 8205.96 | 5184.19 | 0.632 | Cyano-dominant observation |
| 226 | 37 | 36 | 6 | 3883.36 | 1369.42 | 0.353 | Mixed |
| 229 | 36 | 35 | 8 | 4752.83 | 2320.44 | 0.488 | Mixed |
| 233 | 34 | 33 | 7 | 3950.09 | 2081.37 | 0.527 | Mixed/slight cyano majority |
| 235 | 32 | 32 | 7 | 4441.61 | 2135.08 | 0.481 | Mixed |
| 240 | 31 | 30 | 5 | 6643.32 | 5278.97 | 0.795 | Cyano-dominant observation |
| 248 | 33 | 33 | 6 | 12685.86 | 10744.46 | 0.847 | Cyano-dominant observation |
| 260 | 34 | 34 | 5 | 6547.54 | 4349.03 | 0.664 | Cyano-dominant observation (last sample; right-censored) |

### 3.2 Interval-censored interpretation (candidate only)

- **Confirmed observations:** Only the sampled DOYs above are confirmed biological observations. No day between samples is confirmed.
- **Candidate cyano-dominant observations:** Many dates have cyano proportion >=0.5 and high cyano biomass. These are point observations, not continuous event confirmation.
- **Possible onset uncertainty:** First strong cyano-dominant observation is DOY 170 (0.710). Preceding sample DOY 164 is mixed (0.489). Onset, if any event definition is later approved, would be interval-censored between DOY 164–170 at best, and only under an approved definition.
- **Possible termination uncertainty:** Last sample DOY 260 is still cyano-dominant (0.664). Right-censored; no post-260 biological observation.
- **No approved event definition applied.** No labels created.

## 4. Painter 2019 biological reconstruction

### 4.1 Sampling record (verified from source files)

- **n dates:** 17
- **Date span:** DOY 149–276 (2019-05-29 to 2019-10-03)
- **Gaps:** min 4 days, median 7.5 days, max 16 days
- **Location/depth:** Buffalo Pound, 0.8 m
- **Replicates:** `REP` present (`REP1`/`REP2`); DOY 198 is `REP2`.
- **Measurements:** same schema as 2018 plus REP and slightly different column order.

| DOY | Rows | Taxa | Cyano taxa | Total biomass (mg/m3) | Cyano biomass (mg/m3) | Cyano proportion | REP | Interval note |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 149 | 21 | 20 | 2 | 490.81 | 4.00 | 0.008 | REP1 | Low cyano observation |
| 154 | 23 | 22 | 2 | 495.14 | 15.74 | 0.032 | REP1 | Low cyano observation |
| 163 | 22 | 22 | 2 | 1430.38 | 1030.28 | 0.720 | REP1 | Cyano-dominant observation |
| 170 | 16 | 16 | 2 | 123.62 | 30.36 | 0.246 | REP1 | Low-moderate; large drop from DOY 163 |
| 186 | 19 | 19 | 3 | 2554.38 | 1922.59 | 0.753 | REP2 | Cyano-dominant observation |
| 191 | 24 | 24 | 4 | 12587.13 | 11919.83 | 0.947 | REP2 | Cyano-dominant observation |
| 198 | 9 | 9 | 4 | 45.81 | 41.02 | 0.895 | REP2 | **Anomaly: very low total biomass, high cyano proportion, few taxa** |
| 210 | 28 | 28 | 5 | 9497.89 | 6755.17 | 0.711 | REP1 | Cyano-dominant observation |
| 219 | 30 | 30 | 4 | 17944.26 | 15956.56 | 0.889 | REP2 | Cyano-dominant observation |
| 227 | 29 | 29 | 8 | 7331.86 | 5846.33 | 0.797 | REP1 | Cyano-dominant observation |
| 233 | 29 | 29 | 6 | 15555.21 | 4619.13 | 0.297 | REP2 | Mixed (high total, lower cyano prop) |
| 242 | 22 | 22 | 7 | 6007.23 | 1464.89 | 0.244 | REP1 | Mixed/low cyano prop |
| 246 | 26 | 26 | 6 | 17187.83 | 10079.21 | 0.586 | REP1 | Cyano-majority observation |
| 256 | 30 | 30 | 7 | 15883.05 | 10499.03 | 0.661 | REP1 | Cyano-dominant observation |
| 260 | 22 | 22 | 5 | 10038.70 | 7006.45 | 0.698 | REP1 | Cyano-dominant observation |
| 269 | 30 | 30 | 6 | 16814.65 | 13460.73 | 0.800 | REP1 | Cyano-dominant observation |
| 276 | 25 | 25 | 5 | 21122.37 | 19259.68 | 0.912 | REP1 | Cyano-dominant observation (last sample; right-censored) |

### 4.2 Interval-censored interpretation (candidate only)

- **Confirmed observations:** Sampled DOYs only.
- **Anomaly impact:** DOY 198 cannot be interpreted as bloom termination or non-bloom. It also cannot be silently excluded. Any candidate interval spanning DOY 191–210 must carry an unresolved anomaly flag.
- **Gaps:** 16-day gap DOY 170–186 and 12-day gaps around anomaly period; onset/termination cannot be precisely bounded.
- **Right-censored:** last sample DOY 276 remains high cyano.

## 5. 2019-07-17 anomaly investigation

| Check | Result | Evidence |
|---|---|---|
| Date/sample identity | DOY 198, 2019-07-17 equivalent in toxin file; sample ID 25993 in toxin rows | Painter taxonomy + toxin CSVs |
| Replicate/designation | All 9 taxonomy rows marked `REP2`; no REP1 row for same DOY in file | `BP_PhytoTax_2019_KP.csv` |
| Location/depth | Buffalo Pound, 0.8 m for all rows | Taxonomy rows |
| Biomass units/consistency | Biomass_mg_m3 values sum to 45.81; group biomass file gives same total 45.81 and cyano 41.02 (89.54%) | Taxonomy vs `BP_GroupsBiomass_2019_KP.csv` |
| Taxonomy/group agreement | Group biomass file agrees with taxonomy aggregation for DOY 198 | Derived check |
| Toxin same sample? | Toxin file has 2019-07-17, sample 25993, three fractions (Non_filtré/Extracellulaire/Intracellulaire), depth 0.8 | `BP_2019_toxins_0.8.csv` raw lines |
| Toxin interpretation | Messy wide/encoded format; compound columns/units not fully verified. Presence of same-date sample confirmed; quantitative interpretation not confirmed. | Raw inspection |
| Parsing/transcription/duplicate? | No duplicate DOY 198 rows beyond 9 taxa rows; values parse as normal decimals; no obvious parsing artifact identified | Scripted inspection |
| Plausible explanations | Patchiness, replicate handling, field/lab processing, subsampling/entry issue, or real short-lived change. **None confirmed.** | — |

**Conclusion:** Anomaly remains **unresolved**. Retain as explicit uncertainty. Do not discard, correct, or treat as non-bloom/termination.

## 6. Interval-censoring assessment

- **What can be established:** Biological observations at specific sampled DOYs (point observations), with measured biomass/taxonomy/replicate metadata as recorded.
- **What can be bounded:** Possible onset/termination only as intervals between adjacent observations, and only if a pre-approved biological event definition is later adopted. Bounds would be wide (days to weeks).
- **What cannot be established:** Continuous bloom presence between samples; precise onset/termination dates; bloom duration; non-bloom status of unsampled intervals.
- **Required handling:** Any future use must be interval-censored, definition-dependent, and uncertainty-labeled. Sparse sampling makes few-day lead-time claims unreliable.

## 7. Independent non-bloom assessment

| Evidence type | Can it establish non-bloom exposure? | Reason |
|---|---|---|
| Absence of sample | No | Missing observation ≠ non-bloom |
| Low toxin concentration (<LOD or low) | No | Toxin absence/low does not prove absence of cyanobacterial biomass/community event |
| Low total biomass on a single sampled date | **Only a point observation**, not a confirmed interval | No approved non-bloom definition; cannot extend to unsampled days |
| Single low-cyano sample (e.g., 2018 DOY 149, 2019 DOY 149/154) | Point observation only | Adjacent intervals unsampled/uncertain |
| BPWTP monthly microcystin <0.1 µg/L | No | Monthly sparse; toxin-only; intake location; LOD handling; no approved definition |

**Conclusion:** No defensible independent non-bloom exposure denominator can be established from accessible evidence.

## 8. BPWTP report verification

Source: `research/evidence/gate2d/bpwtp_reports/annual-report-2014.pdf`–`2021.pdf`; derived extraction `bpwtp_microcystin_extract.txt`.

| Year | Verified evidence | Raw/treated microcystin (µg/L) as extracted | PDF evidence note | Limitations |
|---|---|---|---|---|
| 2014 | Annual organics screening including microcystin | Feb 26 entry in organics table; no monthly May–Oct table extracted | Found in extraction; annual format | Limited temporal resolution |
| 2015 | Annual organics screening including Microcystin LR | July 13 entry; “one (1) sample per year...” | Found in extraction | Limited temporal resolution |
| 2016 | Narrative microcystin monitoring | July and September analyses; peak 7 µg/L raw; reduced to 0.1 µg/L or less by conventional treatment; non-detectable after GAC | Found in extraction | Narrative, not full monthly table in extraction |
| 2017 | Monthly May–Oct table | May 2 <0.1/<0.1; Jun 6 <0.1/<0.1; Jul 4 <0.1/<0.1; Aug 8 0.3/<0.1; Sep 11 0.7/<0.1; Oct 16 0.1/<0.1 | Extracted table block present | Monthly; intake; toxin only |
| 2018 | Monthly May–Oct table | May 8 <0.1/<0.1; Jun 18 0.4/<0.1; Jul 16 0.3/<0.1; Aug 20 <0.1/<0.1; Sep 17 <0.1/<0.1; Oct 16 0.1/<0.1 | Extracted table block present | Monthly; intake; toxin only |
| 2019 | Monthly May–Oct table | May 6 <0.1/<0.1; Jun 17 0.3/<0.1; Jul 15 0.6/<0.1; Aug 12 4.5/<0.1; Sep 16 0.3/<0.1; Oct 28 0.3/<0.1 | Extracted table block present | Monthly; intake; toxin only |
| 2020 | Monthly May–Oct table | May 5 <0.1/<0.1; Jun 15 1.1/<0.1; Jul 13 0.9/<0.1; Aug 10 0.3/<0.1; Sep 14 <0.1/<0.1; Oct 26 <0.1/<0.1 | Extracted table block present | Monthly; intake; toxin only |
| 2021 | Monthly May–Oct table | May 3 <0.1/<0.1; Jun 14 0.38/0.04; Jul 12 0.2/<0.1; Aug 9 0.4/<0.1; Sep 13 <0.1/<0.1; Oct 25 <0.1/<0.1 | Extracted table block present | Monthly; intake; toxin only |

**Assessment:** BPWTP provides independent toxin measurements. It can corroborate that cyanotoxin presence occurred in some summers, but cannot establish phytoplankton bloom onset/termination, taxonomic composition, or non-bloom exposure. Not a substitute for taxonomy/biovolume.

## 9. Evidence-independence assessment

| Evidence | Independent of buoy RFU predictors? | Independent of buoy-informed phase boundaries? | Suitable for confirmatory event ground truth? |
|---|---:|---:|---:|
| Painter microscopy/taxonomy/biomass | Yes, by method | Yes, by method | Candidate only; sparse/interval-censored; no approved definition |
| Painter toxins | Potentially by method | Potentially | Not verified; not sufficient alone |
| Boyer biological assays | Yes, by method | Measurements yes; published phases no (mixed) | No accessible raw data; phases not ground truth |
| BPWTP microcystin | Yes, by method | Yes | No; toxin-only, monthly, intake-located |
| WSA Primary Station chlorophyll a | Method independent from buoy RFU but river station/chemical param | N/A | No |
| Painter 2023 / buoy phycocyanin | No | No | No |

## 10. Event and sampling-occasion counts

| Quantity | 2017 (Boyer, publication-level) | 2018 (Painter) | 2019 (Painter) | BPWTP toxin 2014–2021 | Notes |
|---|---:|---:|---:|---:|---|
| Independent sampling occasions (biological/toxin records) | 15 reported | 25 | 17 | 2014–2015 limited; 2016 narrative 2+; 2017–2021 6/year monthly | Sampling occasions ≠ events |
| Biologically/toxin positive observations | Not reconstructable from accessible raw data | Multiple cyano-dominant point observations; definition-dependent | Multiple cyano-dominant point observations; anomaly | Several positive raw microcystin detections | Depends on definition |
| Candidate event intervals | 0 reconstructable | 0 approved; possible candidate intervals only | 0 approved; possible candidate intervals only | 0 | Requires pre-approved criteria |
| Independently reconstructed events | **0** | **0** | **0** | **0** | No pre-approved biological-only reconstruction |
| Defensible non-bloom observations/intervals | **0 defensible intervals** | Point observations only | Point observations only | None | No approved non-bloom definition |
| Events suitable for confirmatory evaluation | **0** | **0** | **0** | **0** | Confirmatory use not defensible |

## 11. Matched-FAR feasibility assessment

| Requirement | Status | Reason |
|---|---|---|
| Independent bloom events | Not met | 0 independently reconstructed events from accessible evidence |
| Independent non-bloom exposure | Not met | No defensible non-bloom denominator; missing/unsampled ≠ non-bloom |
| Sufficient temporal coverage | Not met | 2014–2016, 2020–2021 lack verified phytoplankton/biovolume records; 2017–2019 sparse |
| Defensible event boundaries | Not met | Interval-censored, sparse, anomaly, buoy-informed 2017 phases |
| Comparable observation opportunities | Not met | No exposure model; irregular sampling |
| Pre-specified false-alarm definition | Not met | No approved exposure/non-event definition |
| Meaningful missed-event definition | Not met | No approved event definition |
| Valid lead-time comparison | Not met | Sampling gaps and boundary uncertainty exceed plausible few-day effects |

**Conclusion:** Matched-FAR confirmatory evaluation is **not defensible**.

## 12. Remaining evidence gaps

1. Accessible record-level Boyer 2017 biological data (SI/raw) for biological-only reconstruction.
2. 2014–2016, 2020–2021 independent phytoplankton/cyanobacteria taxonomy, cell counts, biovolume/biomass.
3. Defensible non-bloom exposure data/definition.
4. Verified toxin file interpretation for Painter 2018–2019 (units, compound mapping, sample identity).
5. Resolution or formal handling rule for 2019-07-17 anomaly.
6. Pre-approved Gate 2/3 event definition, interval-censoring rule, exposure rule, and matched-FAR evaluation design.

## 13. Final A–D recommendation

**C — Exploratory only.**

The evidence supports descriptive/exploratory analysis but not the proposed confirmatory claim. Painter 2022 and BPWTP microcystin provide useful independent observations, but they do not yield independently reconstructed bloom events, defensible non-bloom exposure, or a defensible matched-FAR evaluation design. Choosing A or B would overstate what the evidence can support.

## 14. Explicit human decisions required

1. **Authorize/decline external data requests:** Boyer 2025 corresponding author (SI/raw 2017 biological records) and BPWTP/WSA (2014–2021 phytoplankton/toxin/lab chl-a records). Do not send without teacher/responsible adult review and explicit authorization.
2. **Decide scope posture:** accept exploratory-only status for now, or pause confirmatory claims until new evidence is obtained and approved.
3. **If new evidence obtained:** convene Gate 2/3 review to approve biological-only event criteria, interval-censoring rules, non-event exposure rules, and matched-FAR design before any label creation or modeling.

## 15. Source references and reproducibility details

- Painter dataset: Borealis DOI 10.5683/SP3/MP6NXF (CC BY-NC-SA 4.0), accessed/downloaded 2026-11-22, checksums verified.
- Derived summary: `research/evidence/gate2d/derived/analyze_painter.py` -> `research/evidence/gate2d/derived/painter_summary.json` (generated 2026-11-22).
- BPWTP reports: https://www.buffalopoundwtp.ca/publications/annual-report, downloaded 2026-11-22; extraction `research/evidence/gate2d/bpwtp_reports/bpwtp_microcystin_extract.txt`.
- Boyer 2025: DOI 10.1111/fwb.70131.
- Boyer 2021 thesis: https://hdl.handle.net/10388/13318.
- Baulch 2025: DOI 10.1016/j.dib.2025.112290.
- WSA Primary Station: https://waterquality.saskatchewan.ca/PrimaryStation, accessed 2026-11-22.
- No raw primary dataset modified; no labels created; no model training.