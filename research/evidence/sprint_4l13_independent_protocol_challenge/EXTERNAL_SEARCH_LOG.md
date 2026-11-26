# Sprint 4L.13 External Search Log

**Search date:** 2026-11-24  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Source categories defined before searching

1. Project governance, decision and protocol records.
2. Sprint 4L.12 deliverables and SHA-256 records.
3. Sprint 4L.9/4L.10/4L.11 evidence.
4. Primary dataset metadata and data dictionaries.
5. Peer-reviewed sensor–microscopy comparisons.
6. Chlorophyll/phycocyanin proxy validation and failure modes.
7. Depth/sample-integration representativeness.
8. Seasonal/community/morphology effects.
9. Negative, contradictory and positive results.
10. Mendota and Buffalo Pound site studies.
11. Bootstrap/dependence methodology.
12. Licence and competition context.

## 2. Project evidence inspected

| # | Route | Sources | What it establishes | Status |
|---:|---|---|---|---|
| 1 | Governance | `AGENTS.md`, `README.md`, `documentation/SCIENTIFIC_PROTOCOL_DRAFT.md` | Project rules; original question; unresolved definitions | Full |
| 2 | 4L.11 decision | `FINAL_STRATEGIC_RECOMMENDATION.md`, executive/handover/state | CONTINUE — NARROWED RESEARCH QUESTION; original question untestable | Full |
| 3 | 4L.10 Mendota | `FINAL_DATASET_DECISION.md`, coverage tables, critiques | Retain limited/reject validation; 128/139 Turner, 21/22 YSI; 58/402 core | Full |
| 4 | 4L.9 sensor audit | Report, QC tables, depth/era critiques | 3,996 daily records; flags; Turner/YSI non-comparability | Full |
| 5 | 4L.5/4L.6 biology | Endpoint/taxonomy/depth critiques | 402 dates; 400 0–8 m; taxonomy non-stationarity; anomalies | Full |
| 6 | 4F Buffalo Pound | Stress test, biological/environmental audits, alignment | 42 dates; two seasons; 0.8 m; no non-bloom; 2019-07-17 | Full |
| 7 | 4L.12 protocol | All 14 deliverables, index, SHA register/README | Question, estimands, QC, matching, stats, claims, 15 decisions | Full |
| 8 | 4L.12 source register | `SOURCE_REGISTER.md`/`.csv` | Prior source metadata; access labels | Full |
| 9 | Gate 2F/G/H | Institutional inventory, anomaly investigation, limitations | No new public dataset; 2019-07-17 unresolved; synthetic-only prototype | Full |
| 10 | Competition | `COMPETITION_LEVEL_CRITICAL_ASSESSMENT.md` | Competition risk; measurement study moderate fit | Full |

## 3. Dataset metadata inspected

| # | Source | What was inspected | Finding | Status |
|---:|---|---|---|---|
| 11 | EDI `knb-lter-ntl.129.42` EML | Schema, flags, depths, event notes | Turner 2006–2019, YSI 2019–present; 0.5 m; significant magnitude differences; fouling/wiper events | Full |
| 12 | EDI 129.42 daily CSV | Header, row count, date range, sample values | 3,996 rows; 2006-07-09 to 2025-11-18; 18 variables | Full (audit) |
| 13 | EDI `knb-lter-ntl.88.31` EML | Methods, depths, taxonomy note, units | 0–8 m tube composite; PhycoTech microscopy; Feb 2013 taxonomic update | Full |
| 14 | NTL 88.31 CSV | Header, Mendota subset, depth codes, divisions | 402 Mendota dates; 400 0–8 m; 2 0–2 m; 11 divisions | Full (audit) |
| 15 | FRDR Buffalo Pound README/data paper | Sensor models, depths, flags, maintenance, units | 0.82 m shallow; 10-min; RFU; pigment accuracy not specified; B7 fouling | Full |
| 16 | Painter 2022 Borealis data | Schema, dates, biomass units, licence | 25/17 dates; 0.8 m; `Biomass_mg_m3`; CC BY-NC-SA 4.0; *Planktothrix* missed | Full (data/README) |

## 4. Literature searches

| # | Query / route | Sources inspected | What it establishes | Inclusion decision |
|---:|---|---|---|---|
| 17 | “chlorophyll fluorescence sensor versus microscopy biovolume lake validation depth-integrated” | Rogora 2023; USGS 2024; Kovalenko 2026; Hartmann 2019; Levi 2025 | Sensor–microscopy comparisons; total vs group-specific; depth/composition effects | Included |
| 18 | “phycocyanin in situ fluorometer cyanobacteria biovolume validation lake study” | Bowling 2016; Hodges 2018; Thomson-Laing 2020; Cotterill 2019; USGS 2024 | PC–biovolume mixed; taxon/morphology/instrument dependent | Included |
| 19 | “Turner Cyclops YSI EXO chlorophyll phycocyanin sensor comparison lake” | Mendota EML; Levi 2025; USGS 2024; manufacturer pages | Turner/YSI differ by orders of magnitude; no cross-calibration | Included |
| 20 | “depth-integrated chlorophyll a versus surface fluorometer lake mismatch” | Rogora 2023; USGS 2024; profiling buoy literature | Surface vs integrated can diverge; DCM/stratification | Included |
| 21 | “seasonal variation chlorophyll fluorescence sensor validation lake phytoplankton composition” | Rogora 2023; Kovalenko 2026; Hartmann 2019; Hodges 2018 | Seasonal/community effects established | Included |
| 22 | “multi-lake sensor comparability chlorophyll phycocyanin validation study” | Kovalenko 2026; USGS 2024; Thomson-Laing 2020 | Multi-lake comparisons exist; lake-specific relationships | Included |
| 23 | “review in situ chlorophyll phycocyanin sensors freshwater validation limitations” | Bertone 2018; Bertone 2019; Levi 2025; USGS TM1-D10; Ma 2022 | RFU proxy; calibration/fouling/composition limits | Included |
| 24 | “phycocyanin fluorescence sensor intercomparison manufacturer temperature morphology” | Hodges 2018; Ma 2022; Levi 2025 | Manufacturer/temperature/morphology effects | Included |
| 25 | “chlorophyll a biovolume conversion variability phytoplankton community lake” | Felip & Catalan 2000; Rogora 2023; Hartmann 2019 | Chlorophyll–biovolume relationship variable | Included as context |
| 26 | “Lake Mendota phycocyanin fluorescence microscopy phytoplankton biovolume comparison” | Carpenter 2020/2022; NTL buoy page; project 4L.10 | Mendota HF PC prior work sensor-only; no direct sensor–microscopy validation found | Included |
| 27 | “Buffalo Pound Lake Planktothrix chlorophyll sensor not detected microscopy” | Painter 2022; Painter 2023; Boyer 2025 | Autumn *Planktothrix* >60% biomass missed by sensor/lab chlorophyll | Included |
| 28 | “chlorophyll fluorescence quenching nighttime sensor validation lake” | Rousso 2021; Rogora 2023; Levi 2025 | Quenching up to 79% chl, 59% PC; nighttime sampling | Included |
| 29 | “sensor fouling biofouling chlorophyll phycocyanin high-frequency lake data quality” | Baulch 2025; USGS TM1-D10/D11; Levi 2025; 4F audit | Fouling/maintenance major QC issues; B7 intervals | Included |
| 30 | “harmful algal bloom sensor validation recommendations USGS” | USGS SIR 2024-5010; TM1-D10/D11 | Variable sensor performance; PC–cyano biovolume not significant | Included |
| 31 | “negative chlorophyll fluorescence values sensor baseline lake” | Sea-Bird Q&A; USGS SIR 2018-5166 appendix; Ma 2023; 4L.12 QC | Negative RFU ambiguous: baseline/noise/below detection | Included as technical context |
| 32 | “block bootstrap autocorrelated ecological time series correlation confidence interval” | Politis & Romano 1994; Künsch 1989; Ólafsdóttir & Mudelsee 2014; Pyper & Peterman 1998 | Block bootstrap preserves autocorrelation; correlation intervals need dependence handling | Included |
| 33 | “bootstrap few clusters cluster robust inference Cameron Miller 2008” | Cameron et al. 2008; Field & Welsh 2007; MacKinnon et al. 2023 | Few clusters can invalidate cluster bootstrap; wild/block alternatives | Included |
| 34 | “Spearman correlation autocorrelation time series biased effective sample size” | Pyper & Peterman 1998; Ólafsdóttir & Mudelsee 2014; rank autocorrelation literature | Serial dependence affects correlation uncertainty | Included |
| 35 | “fluorescence probes real-time remote cyanobacteria monitoring review” | Bertone 2018; Bertone 2019; Zamyadi 2016 | Calibration/turbidity/species composition challenges | Included |
| 36 | “monitoring cyanobacterial breakthrough phycocyanin probe treatment plant” | Ma et al. 2023 | 93-fold daily variation; R=0.73 at high-risk plant; no correlation at low-risk | Included |
| 37 | “combined chlorophyll phycocyanin sensors small water bodies biovolume” | Rozina et al. 2018 | High CHL/PC–biovolume correlation; PC false positives | Included |
| 38 | “chlorophyll phycocyanin raw fluorescence microcystin thresholds lake” | Haggard et al. 2023 | RFU thresholds vs microcystin; applied positive result | Included as applied context |
| 39 | “PhytoFind performance evaluation phytoplankton classification” | USGS SIR 2022-5103 | Overestimated chlorophyll; group % variable | Included |
| 40 | “Painter 2022 Buffalo Pound biomass mg/m3 cell volume methods” | Borealis README/data; paper abstract; 4F audit | Biomass derived; formula not documented locally | Included; evidence gap |
| 41 | “Mendota NTL buoy Turner Cyclops validation” | NTL page; Carpenter 2020/2022; 4L.10 | Sensor-only prior work; no direct validation | Included |
| 42 | “chlorophyll a proxy biovolume review” | Felip & Catalan 2000; Kasprzak-related search results; Rogora 2023 | Variable conversion; context-dependent | Included as context |

## 5. Citation chasing and verification

- References and related-work sections of Rogora 2023, USGS SIR 2024-5010, Bertone 2018, Bertone 2019, Ma 2023, and Painter 2022 were inspected for additional studies.
- Crossref API was used to verify DOIs, journal names, volumes, pages, and years for the key sources.
- Forward citation tracking was limited to search-engine related results and review references; a full Web of Science/Scopus citation index was not available. This is a coverage limitation.
- Claims were checked against the accessible abstract, full text, XML, or data. Abstract-only claims are marked as such.

## 6. Inclusion/exclusion decisions

### Included

- Peer-reviewed studies with direct sensor–microscopy/biovolume comparisons.
- Reviews of fluorescence monitoring limitations.
- Studies of depth/sample integration, seasonality, taxonomy, morphology, quenching, fouling, and calibration.
- Mendota and Buffalo Pound site studies.
- Authoritative USGS guidance/reports.
- Methodological literature on bootstrap/dependence.

### Excluded

- Satellite-only phycocyanin retrieval studies without in situ sensor–microscopy comparison (e.g., Wang et al. 2022) — useful context, not direct validation.
- Pure laboratory culture studies without field relevance, unless they addressed morphology/temperature mechanisms.
- Studies of marine or wastewater systems without freshwater lake relevance, unless methodological.
- Non-peer-reviewed marketing material, except manufacturer technical notes used only for instrument specifications.
- Toxin studies that did not include a sensor–abundance comparison.

### Not used

- Painter toxin files (format/units/sample identity unverified).
- Buffalo Pound researcher correspondence (no repository record; no reply assumed).
- Any new dataset acquisition or contact.

## 7. Evidence gaps

1. **No full text** for Hartmann 2019, Bowling 2016, Hodges 2018, Thomson-Laing 2020, Kovalenko 2026, Cotterill 2019; abstract-level only.
2. **No full text** for Bertone 2018/2019; abstract/metadata.
3. **No documented Buffalo Pound biomass formula** in local metadata; paper full text inaccessible (RSC 403; ESSOAr 403).
4. **No time-stamped/sub-weekly biology** at either lake.
5. **No depth-resolved paired profiles** at the buoy.
6. **No Turner/YSI cross-calibration**.
7. **No per-record calibration/detection limits**.
8. **No independent bloom/non-bloom event table**.
9. **No documented researcher reply** or additional Buffalo Pound data.
10. **No systematic citation index**; forward citation tracking limited.

## 8. Why searching stopped

The review covered the defined categories and the closest accessible primary studies, including contradictory positive and negative results. Remaining gaps are data/access gaps, not search gaps. More literature cannot create the missing biomass formula, time-stamped biology, depth profiles, or cross-calibration.

## 9. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No external contact was initiated.
- No data were acquired, uploaded, committed, or pushed.
- No analysis was performed.
