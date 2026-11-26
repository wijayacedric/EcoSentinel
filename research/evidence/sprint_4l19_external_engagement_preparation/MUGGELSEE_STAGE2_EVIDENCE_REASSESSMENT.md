# Müggelsee Stage 2 Evidence Reassessment

**Sprint:** 4L.19  
**Question:** What is publicly verifiable about the Müggelsee data resources, and do they qualify for the original early-warning ambition?  
**Status:** Stage 2 remains **conditional and unqualified**. Müggelsee is a candidate, not an approved dataset.  
**Contact status:** The Müggelsee enquiry was sent on 2026-11-25. No reply has been recorded. **No further message was sent in this sprint.**

---

## 1. Bottom line

Müggelsee is the strongest Stage 2 lead identified so far, but it **does not meet the Stage 2 qualification threshold** on the public evidence.

What is publicly verifiable:

- a long-term phytoplankton biomass/biovolume series from 1979 to ongoing, sampled weekly in the growing season and biweekly under ice, with Utermöhl microscopy and a documented biomass conversion;
- a weekly multiparameter probe series from 1978 to 2019, including chlorophyll a and phycocyanin;
- a high-frequency multiparameter probe series from 2001 to ongoing at 1.5 m, with 5-minute nominal records, hourly gaps before 2013, and hourly under-ice data;
- formal DOIs and metadata records for all three packages.

What is not publicly verifiable:

- a pre-specified, sensor-independent bloom-event definition;
- the number of independent bloom events and non-bloom exposures;
- exact phytoplankton sample times;
- sensor calibration and QC records at the required level;
- spatial co-location between the sensor station and the phytoplankton sampling stations;
- permission to use the data (all rights reserved);
- whether the sensor series and the microscopy series can be matched at the event scale without circularity.

**Conclusion:** Müggelsee is a credible Stage 2 candidate, but it is not a qualified dataset. The original threshold should be **strengthened**, not lowered.

---

## 2. The three FRED packages

### 2.1 FRED 867 — Müggelsee phytoplankton

| Field | Evidence |
|---|---|
| Title | Müggelsee phytoplankton |
| DOI | `10.18728/igb-fred-867.2` |
| Period | 1979-03-01 to ongoing |
| Sampling interval | Irregular; weekly during the growing season, biweekly under ice |
| Study site | Müggelsee; stations M3, M5, M7, M8, M10, MS1 |
| Parameters | Biomass, biovolume |
| Contact | Sabine Hilt, IGB |
| Licence | **All rights reserved**; request to Sabine Hilt |
| Data file | `Mueggelsee_phytoplankton.csv`; access restricted |
| Metadata | PDF sampling protocol; EML/XML |

**Methods (from the public metadata PDF):**

- Weekly sampling during the growing season, biweekly during ice cover.
- 1979–1986: samples at the deepest station M7, integrated from 0.5, 4 and 7 m.
- Since 1987: integrated samples at five stations; integration scheme depends on stratification and ice cover.
- Phytoplankton fixed with Lugol’s solution; concentrated live sample screened for species composition.
- Utermöhl inverted microscopy; sedimentation tubes 2–100 mL; transects counted; at least 400 individuals per sample; rare/large taxa whole-chamber.
- Cell dimensions measured; biovolume estimated from geometric forms; biomass calculated assuming 10⁹ µm³ = 1 mm³ = 1 mg (specific weight 1 g cm⁻³), reported as µg/L or mg/m³.
- Taxonomic resolution increased in 1993–1995; processors changed in 1998 and 2015, with a one-year training overlap.

**What this supports:** a high-quality, long-term, microscopy-derived biomass/biovolume series with documented methods and taxonomic caveats. This is the strongest biological component of any Stage 2 candidate identified.

**What it does not support:** event definition, sample times, sensor co-location, calibration/QC, or permission.

### 2.2 FRED 1 — Müggelsee weekly multiparameter probe

| Field | Evidence |
|---|---|
| Title | Müggelsee weekly sampling multiparameter probe |
| Period | 1978-07-26 to 2019-03-18 |
| Sampling interval | 7 days; 14 days in winter |
| Parameters | Secchi, turbidity, water temperature, conductivity, oxygen, oxygen saturation, pH, chlorophyll a (HPLC and YSI), phycocyanin (RFU) |
| Contact | Sabine Hilt, IGB |
| Licence | **All rights reserved**; request to Sabine Hilt |
| Data file | `mueggelsee_weekly_insitu.csv`; access restricted |

**Methods (from the public metadata PDF):**

- Depth profiles at 0.5–1 m intervals at stations MS3 and M7.
- YSI 6600 V2 4 probe for temperature, conductivity, pH, oxygen, chlorophyll a fluorescence.
- Secchi depth at MS3 and M7.
- Chlorophyll a has two methods: HPLC (ex situ) and YSI sensor (in situ); they are not equivalent.
- Phycocyanin is reported in RFU.

**What this supports:** a long-term weekly sensor series with chlorophyll and phycocyanin, co-located in time with the phytoplankton sampling programme (same lake, weekly visits). It ends in 2019, so it does not overlap the most recent phytoplankton data.

**What it does not support:** high-frequency exposure, event-scale analysis after 2019, or calibration/QC at record level. The chlorophyll method changes (HPLC vs YSI) are a major comparability issue.

### 2.3 FRED 1145 — Müggelsee Station High Frequency insitu

| Field | Evidence |
|---|---|
| Title | Müggelsee Station High Frequency insitu |
| DOI | `10.18728/igb-fred-1145.0` |
| Period | 2001-10-31 to ongoing |
| Sampling interval | 5 minutes nominal; irregular; gaps every hour before 2013; 1-hour interval in winter |
| Location | Müggelsee station M210, 52.44617, 13.65; water depth ~5.5 m; ~300 m from the north shore |
| Depth | 1.5 m |
| Parameters | Turbidity, water temperature, oxygen, oxygen saturation, pH, chlorophyll a, phycocyanin (RFU) |
| Contact | Tom Shatwell, IGB |
| Licence | **All rights reserved**; request to Tom Shatwell |
| Data files | Split 2001–2007, 2007–2012, 2013–2019, 2019–ongoing; under-ice 1-hour file |

**What this supports:** a high-frequency sensor series spanning more than two decades, with chlorophyll and phycocyanin, suitable in principle for event-scale exposure.

**What it does not support:** exact co-location with the phytoplankton stations, sensor-depth matching to integrated samples, publicly verified calibration/QC, or permission. The station is M210, not the phytoplankton stations M3/M5/M7/M8/M10; the spatial offset is not quantified in the public metadata.

---

## 3. Assessment against the original Stage 2 threshold

The original threshold was:

1. at least five years of data;
2. at least ten independently defined bloom events;
3. weekly-or-better time-stamped microscopy;
4. co-located high-frequency sensors;
5. sampled non-bloom periods;
6. calibration metadata.

| Requirement | Evidence | Status |
|---|---|---|
| ≥5 years | Phytoplankton 1979–ongoing; weekly probe 1978–2019; high-frequency 2001–ongoing | **Pass** |
| ≥10 independent bloom events | No pre-specified event definition; no event count | **Fail / unknown** |
| Weekly-or-better time-stamped microscopy | Weekly growing season, biweekly ice; dates but sample times not verified | **Conditional** |
| Co-located high-frequency sensors | Sensor station M210, phytoplankton stations M3/M5/M7/M8/M10; depth 1.5 m vs integrated 0–4/0–7 m | **Conditional / likely fail** |
| Sampled non-bloom periods | Long-term weekly series likely includes non-bloom dates, but event definition absent | **Conditional** |
| Calibration metadata | Not publicly verified; data paper/metadata do not provide record-level calibration | **Unknown** |

**Result:** 1 pass, 3 conditional/unknown, 1 fail, 1 unknown. The dataset is **not qualified**.

---

## 4. Additional requirements that should be added

The original threshold is necessary but insufficient. The following should be required for Stage 2:

1. **A pre-specified, sensor-independent event definition.** The bloom/non-bloom labels must not be derived from the same sensor variable used as the predictor. Otherwise the analysis is circular.
2. **Event independence.** Overlapping or consecutive samples from one bloom must not be counted as separate events. The event window, minimum duration and separation rule must be defined in advance.
3. **Adequate non-bloom exposure.** The dataset must sample non-bloom periods at a comparable seasonal and temporal resolution; otherwise the model learns “summer vs winter,” not “bloom vs non-bloom.”
4. **Sampling-time documentation.** The microscopy sample time and the sensor averaging window must be documented, or the analysis must explicitly model the mismatch.
5. **Depth matching.** The sensor depth must match the biological sample depth, or the mismatch must be quantified and bounded. Integrated 0–4/0–7 m biomass is not equivalent to a 1.5 m point sensor.
6. **Spatial co-location.** The sensor and the biological station must be the same water parcel or the offset must be documented and justified.
7. **Calibration and QC records.** Record-level calibration, maintenance, fouling and flag definitions are required; a data descriptor is not enough.
8. **Taxonomic consistency.** Taxonomic resolution changes, processor changes and detection limits must be documented; biovolume methods must be stable or correctable.
9. **Data access and licence.** Written permission for the proposed use, including any derived outputs, is required before analysis.
10. **Version and correction history.** The dataset version, DOI, update history and any errata must be recorded.
11. **Sufficient event count after exclusions.** The number of independent events and non-events must be counted after QC and matching, not assumed from the record length.
12. **A negative-control analysis.** The design should include a check that the association is not merely seasonal co-trending (e.g., within-season permutation or seasonal stratification), without turning Stage 2 into an exploratory fishing exercise.

---

## 5. What is publicly verifiable vs not

### Verifiable

- The three FRED packages exist and have DOIs.
- The phytoplankton series is long-term, weekly/biweekly, microscopy-based, with documented biomass conversion.
- The weekly probe includes chlorophyll a and phycocyanin, 1978–2019.
- The high-frequency station includes chlorophyll a and phycocyanin, 2001–ongoing, at 1.5 m.
- The data are all rights reserved and require permission.
- The phytoplankton stations and the high-frequency station are not the same location.
- The sensor depth and the integrated sample depth differ.

### Not verifiable from public sources

- Bloom event counts or an event definition.
- Exact sample times for the microscopy.
- Record-level calibration/QC.
- Whether the high-frequency sensor is representative of the phytoplankton station.
- Whether the 2019–present high-frequency series has the same sensor configuration as earlier years.
- Whether the data licence permits the intended Stage 2 use.
- Whether the phytoplankton taxonomy is consistent enough for event-scale analysis.

---

## 6. Does Müggelsee remain the best Stage 2 lead?

**Yes, but as a candidate, not a qualified dataset.** It has the strongest combination of long-term microscopy and long-term sensor data identified so far. The biological series is exceptional; the sensor series is long and includes both chlorophyll and phycocyanin. The weaknesses are event definition, co-location, depth matching, calibration/QC and access.

No other dataset identified in this sprint meets the Stage 2 threshold either. The correct conclusion is **not** “Müggelsee qualifies”; it is “Müggelsee is worth pursuing if access and metadata are obtained, and no Stage 2 dataset is currently qualified.”

---

## 7. Müggelsee enquiry status

The enquiry to Dr Sabine Hilt and Dr Tom Shatwell was sent on 2026-11-25. No reply has been recorded. The absence of a reply is not evidence of refusal. Do **not** send another message in this sprint. If a reply arrives, record:

- who replied;
- what they confirmed;
- what they declined;
- what access route they offered;
- what licence terms apply;
- what metadata/calibration/QC files are available.

Until then, Stage 2 remains a **conditional ambition**, not a secured path.

---

## 8. Verdict

**Müggelsee is a credible Stage 2 lead but does not meet the qualification threshold. The original threshold should be strengthened with event-definition, co-location, depth-matching, calibration/QC, licence and non-bloom exposure requirements. No Stage 2 dataset is qualified. No contact beyond the existing enquiry was made.**
