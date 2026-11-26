# Sprint 4L.14 External Search Log

**Search date:** 2026-11-24  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Source categories

1. Sprint 4L.12 protocol and Sprint 4L.13 review records.
2. Primary dataset metadata/data dictionaries.
3. Buffalo Pound biomass derivation: local files, GitHub repo, paper/supplement.
4. Sensor–microscopy literature.
5. Contradictory positive/negative evidence.
6. Depth/sample integration.
7. Bootstrap/dependence methodology.
8. Source metadata verification (Crossref).
9. Licence/competition context.

## 2. Project evidence inspected

| # | Route | Sources | Finding | Status |
|---:|---|---|---|---|
| 1 | Governance | `AGENTS.md`, `README.md`, `SCIENTIFIC_PROTOCOL_DRAFT.md` | Rules; original question; definitions | Full |
| 2 | 4L.12 protocol | All deliverables, index, SHA register/README | Original question, estimands, QC, decisions | Full |
| 3 | 4L.13 review | All deliverables | R-01–R-12; 15 decisions; outcome | Full |
| 4 | 4L.11 decision | Final recommendation, executive/handover | CONTINUE — NARROWED | Full |
| 5 | 4L.10 Mendota | Final decision, coverage, critiques | Retain limited/reject validation | Full |
| 6 | 4L.9 sensor | Report/QC/depth/era | Flags; Turner/YSI; coverage | Full |
| 7 | 4L.5/4L.6 biology | Endpoint/taxonomy/depth | 402 dates; 0–8 m; anomalies | Full |
| 8 | 4F Buffalo Pound | Stress test, QC, alignment | 42 dates; 0.8 m; B7; 2019-07-17 | Full |
| 9 | Gate 2F/G/H | Inventory/anomaly/limitations | No new public dataset; anomaly unresolved | Full |

## 3. Biomass derivation searches

| # | Query / route | Sources inspected | Finding | Status |
|---:|---|---|---|---|
| 10 | Local `BP_PhytoTax_2018/2019` headers | `Cell_Density_L`, `Biomass_mg_m3`, `Cell_Volume_um3` | No biovolume column; biomass likely derived | Full |
| 11 | GitHub `biogeochem/buffalopound_blooms` tree | Repo README, code files, processed data list | Code uses `Biomass_mg_m3`; no raw biomass formula in code | Full code/README |
| 12 | `BP_PhytoTax` arithmetic consistency | 2018 all 817 positive rows; 2019 all 405 | Ratio median 1.000 × 10⁻⁶; range consistent with `Cell_Volume × Cell_Density × 10⁻⁶` | Metadata check only |
| 13 | Painter et al. 2022 paper | RSC landing/article HTML | 403; abstract/README only | Abstract/README |
| 14 | RSC supplementary info | Supplement metadata/search snippet | Biomass mg/m³ for cyanobacterial species at 0.8 m; exact formula not retrieved | Metadata |
| 15 | ESSOAr version | `essoar.10510183.2` | 403; no full text | Inaccessible |
| 16 | ResearchGate search | Painter 2022 records | Full-text links exist but not accessible without login | Identified only |
| 17 | Search “Biomass_mg_m3 Buffalo Pound phytoplankton” | Dataset/code references | Units mg/m³; no formula statement | Metadata |

**Conclusion:** The local data structure and arithmetic are consistent with `Biomass = Cell_Volume × Cell_Density × 10⁻⁶` under a 1 g cm⁻³ assumption. The exact formula is not quoted in the accessible local metadata/full paper. This is documented as a conditional derivation, not a proven methods statement.

## 4. Literature searches

| # | Query | Sources | Finding | Access |
|---:|---|---|---|---|
| 18 | chlorophyll fluorescence vs microscopy biovolume | Hartmann 2019; Rogora 2023; USGS 2024; Kovalenko 2026 | Mixed; total biomass often better than group-specific | Abstract/full |
| 19 | phycocyanin vs cyanobacteria biovolume | Bowling 2016; Hodges 2018; Thomson-Laing 2020; Cotterill 2019 | Mixed; taxon/morphology/instrument dependent | Abstract |
| 20 | positive phycocyanin–biovolume results | Rozina 2018; Ma 2023; Thomson-Laing 2020; Rogora 2023 | Strong results exist; not uniformly weak | Abstract/full |
| 21 | negative/non-significant PC results | USGS 2024; Hodges 2018; Cotterill 2019; Bowling 2016 | Weak/non-significant results also exist | Abstract/full |
| 22 | depth-integrated vs surface fluorescence | Rogora 2023; USGS 2024; Felip & Catalan 2000 | Surface/integrated can diverge; composition matters | Abstract/full |
| 23 | seasonal/community effects | Kovalenko 2026; Hartmann 2019; Hodges 2018 | Seasonal/group-specific | Abstract |
| 24 | quenching | Rousso 2021 | 79% chl, 59% PC reduction | Abstract |
| 25 | fouling/calibration | Levi 2025; Bertone 2018/2019; USGS guidance | Calibration/fouling/composition limits | Full/abstract |
| 26 | negative fluorescence | Sea-Bird Q&A; Ma 2023; USGS 2018-5166 appendix | Negative can be baseline/noise/below detection; ambiguous | Technical/abstract |
| 27 | Mendota HF PC | Carpenter 2020/2022; Beal 2022; NTL page | Prior sensor/forecast work; no direct validation | Abstract/full |
| 28 | Buffalo Pound bloom phases | Painter 2022/2023; Boyer 2025 | *Planktothrix* missed by sensor/lab chl | Abstract/full |
| 29 | PhytoFind evaluation | USGS SIR 2022-5103 | Overestimated chlorophyll; group % variable | Full XML |
| 30 | raw fluorescence vs toxins | Haggard 2023 | RFU thresholds vs microcystin | Abstract |

## 5. Bootstrap/dependence searches

| # | Query | Sources | Finding | Access |
|---:|---|---|---|---|
| 31 | block bootstrap autocorrelated time series | Politis & Romano 1994; Künsch 1989; Ólafsdóttir & Mudelsee 2014 | Block methods preserve dependence; correlation intervals need care | Abstract/metadata |
| 32 | few-cluster bootstrap | Cameron et al. 2008; Field & Welsh 2007; MacKinnon et al. 2023 | Few clusters can invalidate cluster bootstrap | Abstract/metadata |
| 33 | autocorrelation in correlation analyses | Pyper & Peterman 1998 | Effective sample size/autocorrelation adjustments | Abstract/metadata |
| 34 | bootstrap foundations | Efron & Tibshirani 1993; Davison & Hinkley 1997 | Standard methods; assumptions matter | Metadata |

## 6. Metadata verification

Crossref API was used on 2026-11-24 to verify:

- Hartmann 2019, *Aquatic Sciences* 81:19;
- Bowling 2016, *Water Research* 105:22–33;
- Hodges 2018, *ESPR* 25(2):1079–1088;
- Thomson-Laing 2020, *Harmful Algae* 97:101869;
- Rogora 2023, *Frontiers in Environmental Science* 10:1058515;
- USGS SIR 2024-5010;
- Kovalenko 2026, *L&O Methods* 24:e70033;
- Cotterill 2019, *NZ J Mar Freshw Res* 53(4):555–570;
- Levi 2025, *Open Research Europe*, DOI;
- Rousso 2021, *Water Research* 198:117133;
- Bertone 2018, *Water Research* 141:152–162;
- Bertone 2019, *Harmful Algae* 87:101625;
- Ma 2023, *Environ Monit Assess* 195:1042;
- Rozina 2018, *Acta Biologica Slovenica* 61(2):29–37;
- Haggard 2023, *J Contemp Water Res Educ* 177:63–71;
- USGS SIR 2022-5103;
- Carpenter 2020, *L&O Letters* 5(5):331–336;
- Carpenter 2022, *PNAS* 119(48):e2214343119;
- Buelo 2022, *Ecological Applications* 32(5):e2616;
- Beal 2022/2023, *Lake and Reservoir Management* 39(1):37–52;
- Recknagel 2025, *Water Research* 287:124514;
- Fournier 2024, *Water Research* 267:122553;
- Painter 2023, *Ecosphere* 14(3):e4472;
- Baulch 2025, *Data in Brief* 63:112290;
- methodological sources S57–S63.

## 7. Inclusion/exclusion decisions

Included:

- direct sensor–microscopy/biovolume studies;
- reviews of fluorescence limitations;
- depth/sample-integration studies;
- studies of taxonomy, morphology, season, quenching, fouling, calibration;
- Mendota/Buffalo Pound site studies;
- authoritative USGS guidance;
- bootstrap/dependence methods;
- original dataset metadata/code needed for endpoint verification.

Excluded:

- satellite-only PC retrieval without in situ sensor–microscopy comparison;
- pure culture studies without field relevance, unless mechanism;
- marine/wastewater studies without freshwater lake relevance, unless methodological;
- marketing material, except manufacturer technical notes for specs;
- toxin studies without sensor–abundance comparison;
- any new dataset acquisition or researcher contact.

## 8. Evidence gaps

1. Painter 2022 full text/supplement inaccessible (403); biomass formula inferred, not quoted.
2. Some key sensor studies abstract-only.
3. No time-stamped/sub-weekly biology.
4. No depth-resolved paired profiles at buoy.
5. No Turner/YSI cross-calibration.
6. No per-record calibration/detection limits.
7. No independent bloom/non-bloom event table.
8. No documented researcher reply/additional Buffalo Pound data.
9. No systematic citation index; forward citation tracking limited.

## 9. Why searching stopped

The defined categories and closest accessible primary sources were covered, including contradictory positive/negative evidence and methodological sources. Remaining gaps are data/access gaps, not search gaps. More literature cannot create the missing full methods text, time-stamped biology, depth profiles, or cross-calibration.

## 10. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No external contact; no dataset acquisition; no uploads/commits/pushes; no analysis.
