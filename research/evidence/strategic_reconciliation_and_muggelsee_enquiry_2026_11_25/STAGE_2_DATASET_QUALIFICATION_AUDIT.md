# Stage 2 Dataset Qualification Audit

**Date:** 2026-11-25  
**Status:** Assessment of proposed Stage 2 criteria and the Lake Müggelsee candidate. No dataset acquired or analysed.  
**Governance:** Gate 2 remains **PAUSED / NOT APPROVED — Option C**; no Stage 2 analysis is authorised.

---

## 1. Purpose

The sequential programme makes Stage 2 — the original early-warning question — conditional on acquiring a qualifying dataset. This audit asks:

1. Are the proposed minimum criteria defensible, overly restrictive, or insufficient?
2. Does Lake Müggelsee meet them?
3. What must be verified before Stage 2 can be authorised?

---

## 2. The proposed criteria

| ID | Proposed criterion | Initial assessment |
|---|---|---|
| C1 | At least five years of suitable data | **Defensible minimum, insufficient alone.** Five years gives some year-to-year variation but may contain too few events for stable false-alarm estimates. It should mean five **overlapping** years with adequate biological and sensor coverage, not five calendar years with one event each. |
| C2 | At least ten independently defined bloom events | **Defensible minimum for exploratory event-level analysis; not confirmatory.** Ten events is a floor, not a comfortable sample. It must count independent events, not peaks within one event or repeated dates. |
| C3 | Time-stamped weekly-or-better microscopy | **Defensible but conditional.** Weekly sampling bounds onset to about seven days. If the claimed warning horizon is shorter than two weeks, weekly data are too coarse. Require sample time and depth, not just a date. |
| C4 | Co-located high-frequency sensors | **Necessary but underspecified.** “Co-located” must mean same station or a documented spatial offset with evidence that the biological sample represents the sensor's water parcel; otherwise it is a same-lake comparison, not a paired measurement. |
| C5 | Sampled non-bloom periods | **Necessary and correctly prioritised.** Without non-events, false-alarm rates are undefined. Require non-bloom observations in multiple seasons/years, not merely “some dates.” |
| C6 | Calibration and instrument metadata | **Necessary but incomplete.** Require instrument change log, calibration/maintenance records, QC flags, detection limits, and missingness documentation. A sensor list alone is not enough. |

**Conclusion:** The six criteria are a good first filter, but they are **insufficient** for a valid Stage 2. They omit event-definition independence, taxonomic consistency, spatial representativeness, data-access terms, and non-event balance. Some are also too permissive in wording (five years, ten events, “co-located”, “calibration metadata”).

---

## 3. Revised qualification standard

A dataset should satisfy all of the following before Stage 2 is authorised. These are proposed criteria for human review, not governance changes.

| ID | Criterion | Why it is required | Evidence needed |
|---|---|---|---|
| Q1 | **Access and licence** | A dataset that cannot be used is not a candidate | Written permission or open licence covering educational research, attribution, and competition use |
| Q2 | **Independent biological endpoint** | Avoids circularity with sensor predictors | Microscopy cell counts/biovolume/biomass, not chlorophyll, phycocyanin, classifier labels, or toxins alone |
| Q3 | **Cyanobacteria-specific taxonomy** | The question is about cyanobacteria, not total phytoplankton | Species/genus or documented cyanobacteria group, with taxonomic crosswalk |
| Q4 | **Time-stamped sampling** | Bounds onset and lead time | Date and, ideally, time; depth; station |
| Q5 | **Cadence tied to warning horizon** | A 14-day series cannot resolve a 7-day lead time | At least weekly during bloom season; finer if the claimed horizon is short |
| Q6 | **Multi-year overlap** | Enables year/event holdout and stable FAR | ≥5 overlapping years of biology and sensors, with adequate within-year coverage |
| Q7 | **Adequate independent events** | Event-level evaluation needs events, not rows | ≥10 independent bloom events, separated in time; non-events sampled by the same method |
| Q8 | **Non-bloom exposure** | Defines the false-alarm denominator | Multiple non-bloom periods per year/season, not just winter absence |
| Q9 | **Spatial/depth representativeness** | A point sensor is not a lake-wide composite | Same station/depth, or documented offset and depth-integration model; profiles preferred |
| Q10 | **Sensor QC and calibration** | Distinguishes artefact from ecology | Instrument change log, calibration/maintenance records, QC flags, detection limits, missingness rules |
| Q11 | **Pre-specified, independent event definition** | Prevents label leakage and post hoc thresholds | Written definition using biological data only, with sensitivity to alternatives |
| Q12 | **Documented data structure and provenance** | Enables reproducible intake and audit | Data dictionary, units, sample identifiers, replicate semantics, version/DOI |
| Q13 | **Practical intake feasibility** | A dataset that cannot be audited in time is not usable | File formats, size, documentation, and a feasible audit plan |

**Q11 is the most important addition.** None of the original six criteria requires an event definition. Without it, “ten events” is not an analysable quantity.

---

## 4. Lake Müggelsee assessment

### 4.1 Summary

| Criterion | Status | Evidence | Verdict |
|---|---|---|---|
| Q1 Access/licence | **Unresolved** | FRED data “all rights reserved”; request to Hilt/Shatwell; metadata CC BY 4.0 | **Fail until permission** |
| Q2 Independent biology | **Pass (metadata)** | Utermöhl microscopy; species counts; biovolume/biomass | Strong |
| Q3 Cyanobacteria taxonomy | **Partial** | Species list; taxonomic resolution changes 1993–1995; cyanobacteria-specific consistency not verified | Needs crosswalk |
| Q4 Time-stamped sampling | **Partial** | Sampling dates; times not confirmed; depth integration documented | Needs verification |
| Q5 Cadence | **Pass for ≥2-week horizon; partial for shorter** | Weekly growing season; biweekly ice | Adequate for weekly-scale onset |
| Q6 Multi-year overlap | **Pass** | Phytoplankton 1979–ongoing; HF 2001–ongoing; PC 2007–ongoing | 19+ years of PC overlap |
| Q7 Events | **Unresolved** | No approved event definition; ≥10 events not counted | Fail until defined |
| Q8 Non-bloom exposure | **Likely pass; unverified** | Year-round weekly/biweekly sampling | Needs file-level confirmation |
| Q9 Spatial/depth | **Partial/fail as strict co-location** | HF 1.5 m fixed station; phytoplankton integrated across five stations/depths; offset ~0.3–2 km | Material limitation |
| Q10 Sensor QC/calibration | **Partial** | Instrument history, maintenance description; full calibration/QC not verified | Needs documentation |
| Q11 Event definition | **Fail** | No pre-specified biological definition | Must be created/approved |
| Q12 Data structure | **Unresolved** | Data files restricted; data dictionary not inspected | Needs metadata |
| Q13 Intake feasibility | **Plausible** | CSV, four HF blocks, long series; access and size unknown | Needs audit |

### 4.2 What is strong

- **Biological depth:** species-level microscopy, cell counts, biovolume, and biomass with a documented 1 g/cm³ conversion.
- **Duration:** phytoplankton from 1979; high-frequency sensors from 2001; phycocyanin from 2007.
- **Cadence:** weekly growing-season biology; 5-minute sensor averages.
- **Non-bloom potential:** year-round sampling, including ice-cover periods.
- **Depth context:** profile data from 2004 at 0.5–5 m.
- **Documentation:** sampling protocol, station coordinates, instrument history, and maintenance description are available.

### 4.3 What is weak or unresolved

1. **No strict co-location.** The HF station is a fixed 1.5 m point; the phytoplankton sample is a five-station integrated composite. The nearest station (M5) is a few hundred metres away; the deepest station (M7) is over a kilometre away. A same-lake analysis is possible; a point-to-point validation is not.
2. **No approved event definition.** The record may contain many seasonal peaks, but “events” must be defined independently and counted. Ten events is not established.
3. **Phycocyanin starts in 2007.** The high-frequency station starts in 2001, but the cyanobacteria-specific channel does not. Stage 2 overlap is 2007–present, not 2001–present.
4. **Instrument changes.** YSI 6600 → 6600V2-4 (2007) → EXO2 (2019); station replacement in 2019; pre-2013 hourly gaps; under-ice deployment changes. Cross-era comparability requires a documented QC/crosswalk.
5. **Taxonomic changes.** Resolution increased in 1993–1995; counters changed in 1998 and 2015. A cyanobacteria crosswalk is required.
6. **Access.** All data are request-only. No permission has been granted.
7. **Data structure.** The phytoplankton file columns, replicate semantics, detection limits, and QC flags are not verified.

### 4.4 What would qualify Müggelsee

Müggelsee would become a qualified Stage 2 candidate only if:

- IGB grants access for the intended educational research;
- the phytoplankton file provides sample-level cyanobacteria biovolume/biomass and dates/depths;
- at least ten independent bloom events can be defined from the biological series with a pre-specified, biologically justified rule;
- non-bloom periods are adequately sampled across years/seasons;
- the HF and phytoplankton spatial/depth mismatch can be justified or modelled;
- sensor QC/calibration and instrument changes are documented;
- a taxonomic crosswalk is available;
- the data can be audited within the available time.

### 4.5 What would disqualify Müggelsee

- Access denied or restricted to aggregate outputs only.
- Cyanobacteria cannot be separated from total phytoplankton.
- Sampling is not actually weekly across the relevant period.
- Fewer than ten independent events can be defined.
- Non-bloom periods are absent or unsampled.
- The spatial/depth mismatch cannot be justified.
- Instrument changes make the sensor series non-comparable without a crosswalk.

---

## 5. Are the criteria overly restrictive?

**No, in broad structure.** Requiring multiple years, multiple events, weekly biology, co-located sensors, non-events, and calibration metadata is the minimum for a credible early-warning test. A study with fewer years/events could be a useful exploratory pilot, but it could not support a matched-FAR claim.

However, some wording is unnecessarily rigid or ambiguous:

- **“Five years”** should not exclude a five-year overlapping window with strong within-year coverage; it should exclude five years of sparse token sampling.
- **“Ten events”** should be a floor for exploratory event-level analysis, not a claim of statistical power. If only 6–9 well-defined events exist, a descriptive event catalogue may still be useful, but not a matched-FAR performance claim.
- **“Weekly-or-better”** should be tied to the warning horizon; weekly is adequate for a two-week-plus horizon, not for a two-day horizon.
- **“Co-located”** should allow a documented same-lake offset if the biological sample is demonstrably representative, but must not be used to hand-wave a point-vs-composite mismatch.

---

## 6. Verdict

**The six proposed criteria are necessary but not sufficient. They should be expanded to Q1–Q13, with Q11 (independent event definition) as a mandatory addition.**

**Lake Müggelsee is a credible Stage 2 lead, not a qualified dataset.** It passes the duration, cadence, and biological-endpoint criteria at metadata level; it fails or remains unresolved on access, strict co-location, event definition, and QC/calibration. The authorised research enquiry has been sent; access is awaited.

**Recommended Stage 2 gate:** **31 January 2027**. By that date, either a qualifying dataset is documented (including access, event definition, and QC) or Stage 2 remains deferred and Stage 1 is the SciFest project. This is a planning recommendation, not a governance decision.

**No Stage 2 analysis is authorised.** No data have been acquired. Gate 2 remains paused.
