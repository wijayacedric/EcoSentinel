# Scientific Reviewer Brief

**Status:** Draft for an independent reviewer — **no reviewer has been appointed**.  
**Project:** EcoSentinel  
**Date:** 2026-11-25  
**Governance:** Protocol **PROPOSED — NOT APPROVED**; Gate 2 **PAUSED / NOT APPROVED — OPTION C**; all decisions **OUTSTANDING**; analysis **NOT AUTHORISED**.

---

## 1. What EcoSentinel is

EcoSentinel is a secondary-school research project investigating whether surface chlorophyll and phycocyanin fluorescence can track independent microscopy-derived cyanobacteria abundance in two lakes:

- **Lake Mendota, Wisconsin** — 402 microscopy dates, 1995–2020; sensors at 0.5 m; biology generally a 0–8 m composite.
- **Buffalo Pound Lake, Saskatchewan** — 42 microscopy dates in 2018–2019; sensors and biology nominally at 0.8 m; two seasons only.

The original early-warning ambition — whether persistent changes in relationships among environmental variables warn earlier than conventional monitoring at matched false-alarm rates — is **not testable with the current data** and is not the current analysis. It remains a conditional Stage 2 objective.

---

## 2. Current narrowed question

> In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-calendar-date co-occurrences and analysed as two separate lake-specific case studies, what are the direction and magnitude of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations differ descriptively across seasonal strata, with Mendota’s Turner and YSI eras analysed separately?

**What it is:** a descriptive measurement/comparability audit.  
**What it is not:** validation, calibration, agreement, prediction, bloom detection, or early warning.

---

## 3. Proposed estimands

| ID | Lake / era | Sensor | Endpoint | Maximum possible n | Status |
|---|---|---|---:|---:|---|
| P1 | Mendota / Turner | Chlorophyll RFU | Cyanobacteria biovolume | 128 | Conditional exploratory |
| P2 | Mendota / Turner | Phycocyanin RFU | Cyanobacteria biovolume | 139 | Conditional exploratory |
| P3 | Buffalo Pound / YSI | Chlorophyll RFU | Cyanobacteria biomass | 42 | Exploratory only |
| P4 | Buffalo Pound / YSI | Phycocyanin RFU | Cyanobacteria biomass | 42 | Exploratory only |

The n values are upper bounds, not actual n. No count audit has been authorised. P1/P2 share dates/endpoint; P3/P4 share dates/endpoint; they are not four independent confirmations.

---

## 4. Known limitations

- Biology has **dates, not sampling times**.
- Mendota sensors are at **0.5 m**; biology is a **0–8 m composite**; ~106 m spatial offset.
- Buffalo Pound is **two seasons**, no non-bloom baseline, and has unresolved duplicate-row semantics.
- Turner and YSI are different instruments with order-of-magnitude RFU differences; no crosswalk.
- Mendota daily means have no documented within-day counts.
- Buffalo Pound daily coverage varies (121–144 records/day in 2018; 42–131 in 2019); the fixed 72/144 rule has been withdrawn.
- QC flags are incompletely defined; H has no numeric range; O is undefined; B7 is a caution interval, not a removal flag; negative RFU meaning is unresolved.
- Some apparent associations may reflect seasonal co-trending, autocorrelation, selection, or taxonomic change.

---

## 5. Current decision state

- D-01–D-15: **OUTSTANDING — NOT APPROVED**.
- D-05 QC: unresolved; a conservative interim population is possible but not validated.
- D-06 daily summary: provisional Option A only (full-day means; non-equivalence stated).
- D-09 anomaly handling: provisional; blocked by D-05.
- D-13 originality: project-owner decision outstanding.
- D-15: **NOT APPROVED**.

The 4L.14 review returned **ACCEPT AFTER REVISIONS**. The 4L.14 addendum is ready for review but not approved.

---

## 6. Questions for the scientific reviewer

Please address, with reasons:

1. Is the narrowed measurement question scientifically meaningful and clearly bounded?
2. Are P1–P4 appropriately framed as exploratory descriptive estimates, or should any be dropped?
3. Is the **detection-conditioned population** (dates with a reported cyanobacteria row) acceptable, or does it bias the question beyond usefulness?
4. Is the depth mismatch at Mendota handled honestly, or does it make P1/P2 uninterpretable?
5. Are the proposed QC exclusions conservative and defensible? Specifically:
   - C/E exclusion;
   - H exclusion where no numeric range exists;
   - G as a caution rather than automatic invalidity;
   - B7 as a caution interval rather than automatic invalidity;
   - negative RFU as unresolved.
6. Are the claims appropriately limited to rank association and non-equivalence?
7. Is Stage 1 still scientifically viable as a modest exploratory audit, or should it be paused?
8. Is P3/P4 worth retaining as exploratory, given the duplicate-row and biomass-provenance problems?

You are **not** being asked to approve D-15, endorse the hypothesis, or validate the protocol as a whole. A written opinion with reasons and any conditions is sufficient.

---

## 7. Materials provided

- 4L.14 `REVISED_PROTOCOL.md`
- 4L.14 `UPDATED_HUMAN_DECISION_REGISTER.md`
- 4L.14 review findings F-01–F-13
- 4L.14 addendum
- 4L.16 decision matrix and review order
- 4L.17 D-06 assessment
- 4L.18 D-05 evidence resolution
- This brief

---

## 8. Independence and conflicts

Please disclose any role in the datasets, the Painter/Baulch research, the NTL-LTER programme, or the project. A reviewer with a direct interest in a particular result is not independent.

**No reviewer has been appointed or contacted.** This brief is a draft for a future invitation.
