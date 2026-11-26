# Estimand Hierarchy Recommendation

**Sprint:** 4L.20  
**Date:** 2026-11-26  
**Purpose:** Replace the four equal-status estimands with a defensible, pre-specified hierarchy.  
**Status:** Recommendation. **Not approved. No analysis authorised.**

---

## 1. The problem with four equal-status estimands

The 4L.14 protocol proposed four sensor–endpoint pairs:

| ID | Lake / era | Sensor | Endpoint |
|---|---|---|---|
| P1 | Mendota / Turner | Chlorophyll RFU | Cyanobacteria biovolume (0–8 m) |
| P2 | Mendota / Turner | Phycocyanin RFU | Cyanobacteria biovolume (0–8 m) |
| P3 | Buffalo Pound / YSI | Chlorophyll RFU | Cyanobacteria biomass (0.8 m) |
| P4 | Buffalo Pound / YSI | Phycocyanin RFU | Cyanobacteria biomass (0.8 m) |

They are **not four independent quantities**:

- P1/P2 share the same biological endpoint, dates and depth mismatch.
- P3/P4 share the same biological endpoint, dates and provenance problems.
- The two pigments within each lake are correlated.
- The two lakes are not a controlled comparison.

Reporting four “primary” estimates creates:

- a **false impression of replication**;
- **selective emphasis** risk (the “best” sensor/lake may be highlighted);
- **multiplicity** without p-values;
- **reviewer burden** and a diffuse story;
- a temptation to retain weak estimands because they are already in the protocol.

The 4L.14 addendum tried to control this by requiring all four to be reported as equal-status exploratory estimates. That is better than selecting a winner, but it does not solve the underlying problem: **the four are not equally defensible.**

---

## 2. Evidence quality by estimand

| Estimand | Endpoint quality | Depth alignment | Temporal sampling | QC/provenance | Overall |
|---|---|---|---|---|---|
| **P1** Mendota chlorophyll | True biovolume; broad division total; taxonomic non-stationarity | Poor: 0.5 m vs 0–8 m | Biweekly; 128 upper bound | H/negative/station unresolved; actual n unknown | Conditional |
| **P2** Mendota phycocyanin | True biovolume; more cyanobacteria-specific pigment | Poor: 0.5 m vs 0–8 m | Biweekly; 139 upper bound | H/negative/station unresolved; 4 negatives; actual n unknown | Conditional; strongest Mendota estimand |
| **P3** Buffalo Pound chlorophyll | Derived wet-weight-equivalent biomass; duplicates/REP unresolved | Good: 0.82 m vs 0.8 m | 42 dates over two seasons | Biomass derivation, B7, coverage, time zone, negative/>100, version, licence unresolved | Weak/exploratory at best |
| **P4** Buffalo Pound phycocyanin | Same as P3 plus *Planktothrix* detection concern | Good | Same | Same | Weak/exploratory at best |

**Conclusion:** P2 is the strongest single estimand; P1 is a credible secondary comparator; P3/P4 are not equal-status primary candidates and are removed from Stage 1.

---

## 3. Why P2 is primary

P2 is phycocyanin fluorescence versus cyanobacteria biovolume.

### 3.1 Biological rationale

- Phycocyanin is a pigment characteristic of cyanobacteria; chlorophyll a is present in all phytoplankton.
- A cyanobacteria-specific pigment has a stronger **a priori** rationale for tracking a cyanobacteria endpoint than a broad chlorophyll signal.
- The literature on phycocyanin probes is directly relevant (Brient 2008; Loisa 2015; Kong 2013; Hodges 2017; Cotterill 2019).

### 3.2 Data rationale

- Turner phycocyanin has 139 same-day unflagged upper-bound dates, slightly more than Turner chlorophyll (128).
- Both share the same endpoint/dates; the choice is not driven by a larger n alone.
- The Turner phycocyanin record has only 4 negative RFU values; manageable with a sensitivity.

### 3.3 Why not P1 primary?

- Chlorophyll is a broad phytoplankton pigment; it is not cyanobacteria-specific.
- A chlorophyll–cyanobacteria association is expected to be weaker and more confounded by other phytoplankton.
- P1 is useful as a **comparator**: does the broader pigment do as well as the more specific one?
- Making P1 secondary avoids a false “two independent pigments” claim.

### 3.4 Why not both co-primary?

- They share dates and endpoint; co-primary status is statistically redundant.
- Two co-primary estimates invite selective emphasis.
- A hierarchy is pre-specified by pigment biology, not by expected results.

---

## 4. Why P1 remains

P1 is not dropped because it answers a useful secondary question:

> Does the broader chlorophyll signal show a similar descriptive rank association with cyanobacteria biovolume, or does the more specific phycocyanin signal perform differently?

This is a **descriptive comparison**, not a formal test of dependent correlations. It can be reported as:

- P2 rho and n;
- P1 rho and n;
- a statement that the two share dates/endpoint and are not independent;
- no claim that one is “better” unless a pre-specified criterion exists (none is).

P1 also provides continuity with the original two-pigment design and a richer poster narrative without adding a second lake or endpoint.

---

## 5. Why P3/P4 are removed

P3/P4 are not demoted to “secondary” because:

- Their endpoint is a derived wet-weight-equivalent biomass, not biovolume.
- Duplicate/`REP` semantics are unresolved; mean/sum/first-row are different endpoints.
- The exact biomass derivation/density is not provider-confirmed.
- B7 is a caution interval; retention/treatment is unresolved.
- Coverage, time zone and sample times are unresolved.
- Two seasons cannot support a stable association.
- The sensor missed an autumn *Planktothrix* bloom in the published record.
- The biological dataset has a different licence (CC BY-NC-SA 4.0).
- The custodian has not responded.

A “secondary” label would not make these problems disappear; it would only make them easier to ignore. Remove P3/P4 from Stage 1 and preserve them for a future Buffalo Pound/Stage 2 study.

---

## 6. Recommended hierarchy

| Level | Estimand | Status | Reporting |
|---|---|---|---|
| **Primary** | **P2 — Mendota Turner phycocyanin vs cyanobacteria biovolume** | Confirmatory-descriptive? No — **primary descriptive** | Full rho, n, influence, sensitivities, limitations |
| **Secondary** | **P1 — Mendota Turner chlorophyll vs cyanobacteria biovolume** | Descriptive comparator | Full rho, n, same limitations; no “winner” claim |
| **Removed** | P3 — Buffalo Pound chlorophyll vs biomass | Not in Stage 1 | Preserve evidence; future/Stage 2 only |
| **Removed** | P4 — Buffalo Pound phycocyanin vs biomass | Not in Stage 1 | Preserve evidence; future/Stage 2 only |

**Terminology:** “Primary” means the pre-specified focus of the descriptive audit, not a confirmatory hypothesis test. “Secondary” means a pre-specified descriptive comparator, not an exploratory afterthought.

---

## 7. Multiplicity and reporting rules

1. **Pre-specify the hierarchy before analysis.** Do not choose P2 because it looks stronger after seeing results.
2. **Report both P2 and P1 in full.** Do not report only the favourable one.
3. **State that P1/P2 are not independent.** They share dates and endpoint.
4. **No “best sensor” claim.** A descriptive difference between rho values is not a formal test.
5. **Report all pre-specified sensitivities**, not only favourable ones.
6. **No p-values, no confidence intervals, no significance language.**
7. **No subgroup fishing.** Seasonal strata are descriptive; n<10 → no stratum rho.
8. **No outcome-dependent switching.** If P2 is weak and P1 is stronger, that is a descriptive finding, not a reason to relabel P1 as primary.

---

## 8. What would change the hierarchy

- The scientific reviewer concludes phycocyanin is not a defensible primary pigment for this endpoint → P1 primary or pause.
- The statistical reviewer concludes the two pigments are too collinear to report separately → one estimand only.
- The count audit shows P2 n is too small → P1 primary or pause.
- A reviewer requires equal-status reporting for transparency → report both, but retain the pre-specified P2 focus and label P1 secondary.
- A stronger question emerges → new protocol, not a post-hoc hierarchy.

---

## 9. Verdict

**P2 primary; P1 secondary; P3/P4 removed.**

This is the minimum hierarchy that preserves a meaningful pigment comparison without pretending the four estimates are independent or equally defensible. It reduces multiplicity, simplifies the protocol, and gives the project a clear primary question.

**No analysis was performed. No decision was approved.**
