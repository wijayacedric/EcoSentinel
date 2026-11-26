# Sprint 4L.12 External Search Log

**Search date:** 2026-11-24  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Source categories defined before searching

1. Project governance, protocol and decision records.
2. Existing project evidence for Mendota, Buffalo Pound and prior feasibility audits.
3. Primary dataset metadata and data dictionaries (EDI/NTL, FRDR, Borealis).
4. Peer-reviewed sensor–microscopy comparisons.
5. Chlorophyll/phycocyanin proxy validation and limitations.
6. Depth-integrated vs surface fluorescence comparisons.
7. Seasonal, community-composition, morphology and temperature effects.
8. Multi-lake sensor comparability and intercalibration.
9. Quenching, fouling and calibration technical guidance.
10. Mendota and Buffalo Pound site-specific studies.
11. Competition context (secondary; not the main search).

## 2. Project evidence inspected

| # | Route | Sources | What it establishes | Status |
|---:|---|---|---|---|
| 1 | Governance/protocol | `AGENTS.md`, `README.md`, `documentation/SCIENTIFIC_PROTOCOL_DRAFT.md` | Project rules; original question; unresolved definitions | Full |
| 2 | 4L.11 decision | `FINAL_STRATEGIC_RECOMMENDATION.md`, `SPRINT_4L11_EXECUTIVE_REPORT.md`, `SPRINT_4L11_HANDOVER.md`, `CURRENT_PROJECT_STATE.md` | CONTINUE — NARROWED RESEARCH QUESTION; original question not testable | Full |
| 3 | 4L.10 Mendota | `FINAL_DATASET_DECISION.md`, `summary.json`, coverage tables, critiques | Mendota retain limited/reject validation; 128/139 Turner, 21/22 YSI; 58/402 7-var core; 2/402 11-var core | Full |
| 4 | 4L.9 sensor audit | `SPRINT_4L9_EXECUTIVE_REPORT.md`, QC tables, depth/era critiques | 3,996 daily records; 38 columns; Turner/YSI non-comparability; flag gaps | Full |
| 5 | 4L.5/4L.6 biology | Raw biology audit, endpoint/taxonomy/depth critiques | 402 Mendota dates; 400 0–8 m; 2 0–2 m; taxonomy non-stationarity; anomalies | Full |
| 6 | 4F Buffalo Pound | Stress-test report, biological/environmental audits, alignment | 42 dates; two seasons; 0.8 m; no non-bloom; 2019-07-17 anomaly; QC issues | Full |
| 7 | 4H response readiness | Researcher response framework, comparison matrix, requirement tracker | Buffalo Pound pending; additional data not assumed | Full |
| 8 | Gate 2 integrated | `GATE2_2017_2019_INTEGRATED_EVIDENCE_ASSESSMENT.md` | 0 independently reconstructed events; no non-bloom exposure | Full |
| 9 | Gate 2F/G/H | Institutional inventory, anomaly investigation, limitations | No new public dataset; 2019-07-17 unresolved; prototype synthetic only | Full |
| 10 | Competition context | `COMPETITION_LEVEL_CRITICAL_ASSESSMENT.md`, 4L.11 competition assessment | Current confirmatory claim not defensible; measurement study moderate fit | Full |

## 3. Dataset metadata and data dictionaries

| # | Source | What was inspected | Finding | Status |
|---:|---|---|---|---|
| 11 | EDI `knb-lter-ntl.129.42` EML | 38-field schema, attribute definitions, flags, depths, event notes | Turner 2006–2019, YSI 2019–present; 0.5 m; “significant magnitude differences”; 2017 DO biofouling; 2023 wiper failure | Full |
| 12 | EDI 129.42 daily CSV | Header, sample rows, row count, date range | 3,996 rows; 2006-07-09 to 2025-11-18; 18 variables; no duplicate dates | Full (header/audit) |
| 13 | EDI `knb-lter-ntl.88.31` EML | Methods, depths, taxonomy update note, units | 0–8 m tube composite for Mendota; 0–2 m for other lakes; PhycoTech microscopy; Feb 2013 taxonomic update | Full |
| 14 | NTL 88.31 CSV | Header, Mendota subset counts, depth codes, divisions | 402 Mendota dates; 400 0–8 m; 2 0–2 m; 11 divisions; `biovolume_conc` µm³ mL⁻¹ | Full (audit) |
| 15 | FRDR Buffalo Pound README/data paper | Sensor models, depths, flags, maintenance, units | 0.82 m shallow; 0.82/2.83 m; 10-min; RFU; pigment accuracy not specified; B7 fouling; CC BY 4.0 | Full |
| 16 | Painter 2022 Borealis README/data | 2018/2019 microscopy schema, dates, biomass units, licence | 25/17 dates; 0.8 m; `Biomass_mg_m3`; CC BY-NC-SA 4.0; autumn *Planktothrix* missed by sensor/lab chl | Full (abstract/README + project data) |

## 4. Literature searches

| # | Query / route | Sources inspected | What it establishes | Status |
|---:|---|---|---|---|
| 17 | “chlorophyll fluorescence sensor versus microscopy biovolume lake validation depth-integrated” | Rogora 2023; USGS SIR 2024-5010; Kovalenko 2026; Hartmann 2019; Levi 2025 | Sensor–microscopy comparisons exist; total biomass often tracks better than group-specific; depth/composition matter | Mixed: full/abstract |
| 18 | “phycocyanin in situ fluorometer cyanobacteria biovolume validation lake study” | Bowling 2016; Hodges 2018; Thomson-Laing 2020; Cotterill 2019; USGS SIR 2024-5010 | PC–biovolume relationships variable; taxon/morphology/instrument dependent; USGS found non-significant PC–cyanobacteria biovolume | Mixed: full/abstract |
| 19 | “Turner Cyclops YSI EXO chlorophyll phycocyanin sensor comparison lake” | Mendota EML; Levi 2025; USGS SIR 2024-5010; Turner/YSI technical pages | Turner/YSI differ by orders of magnitude; no cross-calibration; sensors are instrument-specific | Mixed |
| 20 | “depth-integrated chlorophyll a versus surface fluorometer lake mismatch” | Rogora 2023; USGS SIR 2024-5010; profiling buoy literature | Surface vs integrated can diverge; deep chlorophyll maxima and stratification matter | Mixed |
| 21 | “seasonal variation chlorophyll fluorescence sensor validation lake phytoplankton composition” | Rogora 2023; Kovalenko 2026; Hartmann 2019; Hodges 2018 | Seasonal/community effects are established; cyanobacteria often underestimated | Mixed |
| 22 | “multi-lake sensor comparability chlorophyll phycocyanin validation study” | Kovalenko 2026; USGS SIR 2024-5010; Thomson-Laing 2020 | Multi-lake comparisons exist; relationships are lake-specific | Mixed |
| 23 | “review in situ chlorophyll phycocyanin sensors freshwater validation limitations” | Zamyadi 2016 review; Levi 2025; USGS TM1-D10; Ma 2022 | RFU is a proxy; calibration/fouling/community limits are well known | Mixed |
| 24 | “phycocyanin fluorescence sensor intercomparison manufacturer temperature morphology” | Hodges 2018; Ma 2022; Levi 2025 | Manufacturer, temperature, morphology affect PC fluorescence | Mixed |
| 25 | “chlorophyll a biovolume conversion variability phytoplankton community lake” | Felip & Catalan 2000; Rogora 2023; Hartmann 2019 | Chlorophyll–biovolume relationship varies with community and lake; not a fixed conversion | Abstract/metadata |
| 26 | “Lake Mendota phycocyanin fluorescence microscopy phytoplankton biovolume comparison” | Carpenter 2020/2022; NTL buoy page; project 4L.10 | Mendota HF PC prior work is sensor-only; no direct sensor–microscopy validation found | Mixed |
| 27 | “Buffalo Pound Lake Planktothrix chlorophyll sensor not detected microscopy” | Painter 2022; Painter 2023; Boyer 2025 | Autumn *Planktothrix* >60% biomass was not detected by sensor or lab chlorophyll-a | Full/abstract |
| 28 | “chlorophyll fluorescence quenching nighttime sensor validation lake” | Rousso 2021; Rogora 2023; Levi 2025 | Daytime quenching can reduce chl by up to 79% and PC by up to 59%; nighttime sampling recommended | Abstract/metadata |
| 29 | “sensor fouling biofouling chlorophyll phycocyanin high-frequency lake data quality” | Baulch 2025; USGS TM1-D10/D11; Levi 2025; 4F audit | Fouling and maintenance are major QC issues; B7 flags mark intervals | Full/mixed |
| 30 | “harmful algal bloom sensor validation recommendations USGS” | USGS SIR 2024-5010; USGS TM1-D10/D11 | USGS found variable sensor performance; PC–cyanobacteria biovolume not significant; temperature/turbidity informative | Full |

## 5. Citation chasing and verification notes

- References and related-work sections of the accessible studies (Rogora 2023; Hartmann 2019 abstract; Bowling 2016 abstract; Hodges 2018 abstract; USGS SIR 2024-5010) were inspected for additional sensor–microscopy and phycocyanin-validation studies.
- Forward citation tracking was limited to search-engine related results and review references; a full Web of Science/Scopus citation index was not available. This is a coverage limitation, not a claim that no further studies exist.
- Key numerical claims (e.g., R² values, non-significant phycocyanin relations, quenching percentages) were checked against the accessible abstract, full text, or XML. Where only an abstract was accessible, the claim is marked as abstract-level.
- No source was treated as full-text if only a preview/abstract was accessible.

## 6. Key findings

1. **The measurement question is not novel.** Sensor–microscopy comparisons exist across lakes, reservoirs, and sensors (S31–S40). The expected answer is “variable, often weak, taxon/season/instrument-dependent.”
2. **Chlorophyll and phycocyanin answer different questions.** Chlorophyll tends to track total phytoplankton biomass better than cyanobacteria specifically; phycocyanin is intended to track cyanobacteria but is affected by taxonomy, morphology, temperature, and quenching.
3. **Depth mismatch is recognized but not cleanly testable here.** Mendota 0.5 m vs 0–8 m is a known limitation; Buffalo Pound 0.82 m vs 0.8 m is better aligned. The two-lake contrast is confounded by lake, instrument, period, community, and endpoint.
4. **The original early-warning question remains untestable.** No independent events, no non-bloom exposure, no time-stamped/sub-weekly biology, no matched-FAR denominator.
5. **The narrowed study is feasible but modest.** It can produce a defensible descriptive/negative result; it cannot produce a novel early-warning method or a validated sensor.
6. **Buffalo Pound’s *Planktothrix* case is a warning, not a validation.** Prior work reported a bloom that sensor/lab chlorophyll missed; this directly cautions against assuming depth alignment guarantees agreement.

## 7. Inaccessible or partially inspected sources

| Source | Access issue | What was used instead |
|---|---|---|
| Hartmann et al. 2019 | Springer paywall; abstract/preview only | Abstract and metadata |
| Bowling et al. 2016 | Publisher abstract page; full text not accessed | Monash abstract |
| Hodges et al. 2018 | Springer paywall; abstract/preview only | Abstract and metadata |
| Thomson-Laing et al. 2020 | ScienceDirect blocked; abstract page | Publisher abstract + Our Lakes page |
| Kovalenko et al. 2026 | UMN abstract page; full PDF not accessible | Abstract |
| Cotterill et al. 2019 | Taylor & Francis 403 | Abstract (prior sprint) |
| Rousso et al. 2021 | PubMed page blocked; abstract snippet | Abstract/metadata |
| Beal et al. 2021/2022 | Publisher 403/search-indexed | Prior project audits |
| Recknagel 2025; Fournier 2024 | Publisher 403 | Abstract/metadata (prior) |
| Buelo 2022 | Publisher 403 | Abstract/excerpts + code (prior) |
| Zamyadi 2016 review; Ma 2022; Felip & Catalan 2000 | Abstract/metadata; MDPI 403 | Abstracts/search-index |
| Painter toxin files | Format/units/sample identity unverified | Not used |
| Buffalo Pound researcher reply | No repository send record/reply/data summary | Pending/unknown; no data assumed |

## 8. Why searching stopped

The search covered the defined categories and the closest accessible primary studies. Remaining gaps are **data/evidence gaps**, not search gaps:

- no independent bloom/non-bloom event table;
- no time-stamped/sub-weekly biology;
- no depth-resolved paired profiles at the sensor;
- no Turner/YSI cross-calibration;
- no per-record calibration/detection limits;
- no documented Buffalo Pound reply or additional data.

More literature cannot create these data. The search is sufficient to establish that the proposed measurement study is **not novel** and that its originality is **low–moderate**.

## 9. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No external contact was initiated.
- No data were acquired, uploaded, committed, or pushed.
- No analysis was performed.
