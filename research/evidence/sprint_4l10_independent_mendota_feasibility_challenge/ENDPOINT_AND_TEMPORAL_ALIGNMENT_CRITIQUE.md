# Endpoint and Temporal-Alignment Critique

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. What the microscopy endpoint is

The 88.31 file is a direct microscopy export: cell counts, natural-unit counts, geometry-based biovolume and derived biomass. It is **measurement-source independent** of the buoy’s optical sensors, but it is not independent of the lake processes the sensors also observe.

It can support an exploratory **cyanobacterial abundance/biovolume** endpoint. It does **not** establish:

- bloom/non-bloom status;
- bloom onset or termination;
- toxicity or toxin-producing taxa;
- surface scum or lake-wide exposure;
- absence of a bloom elsewhere in the lake;
- a sample time within the date.

The endpoint is also taxonomically non-stationary: 468 nonblank taxa names, 176 nonblank genera, 204 names only pre-2013 and 72 only post-2013, 889 genus-field mismatches, 8,514 trailing-space records. Broad cyanobacterial totals are more defensible than species-level longitudinal comparisons, but even the broad total has historical identification and taxonomy caveats.

## 2. What same-day overlap means

The independent recount confirms:

- 402 Mendota biology dates, 1995-01-24 to 2020-12-10, median 14-day interval.
- 400 dates 0–8 m composite; 2 dates 0–2 m.
- 371/402 dates have no station value; 31 have station “1”.
- Turner chlorophyll: **128** same-day unflagged dates.
- Turner phycocyanin: **139**.
- YSI chlorophyll: **21**; YSI phycocyanin **22**.
- DO raw: **99**; DO saturation **98**; water temp **94**.

Same-day means **date availability**, not temporal alignment. The biology file has no sample time. A sensor daily average integrates 1-minute values over the day; a microscopy sample is a date-stamped composite. They are not paired observations at a known hour.

## 3. Surrounding windows

The ±1/±3/±7/±14-day windows are reported in `tables/INDEPENDENT_OVERLAP.csv`. They increase the count modestly:

- Turner chlorophyll ±7: **156/402**; ±14: **163/402**.
- Turner phycocyanin ±7: **154/402**; ±14: **160/402**.
- DO raw ±7: **147/402**; ±14: **166/402**.

These are **not lead/lag estimates**. A ±7-day window can span a bloom onset and decline, and it can mix different weather, stratification and seasonal states. A sparse biology series can make a sensor change appear to lead a biological change simply because the next sample is two weeks away. The data cannot distinguish that from a true lead.

## 4. Can the biology support a claimed lead time?

No.

- The median biology interval is 14 days; maximum gap 120 days.
- There is no bloom/non-bloom event definition or independent adjudication.
- There is no verified non-event exposure.
- The sensor record is daily; the biology is date-only.
- A lead-time claim requires a defined onset, a time-matched predictor, and enough events/non-events to validate. None exists.
- Prior experimental EWS work (Pace et al. 2016; Wilkinson et al. 2018) achieved warnings 1–57/61 days before blooms under controlled enrichment and high-frequency monitoring; that does not transfer to a 14-day observational series with no event labels.

## 5. What the endpoint can and cannot support

**Can support:**
- descriptive seasonal patterns in cyanobacteria biovolume;
- pairwise descriptive comparisons with same-day sensor conditions;
- exploratory low/high abundance contrasts, with taxonomic and depth caveats.

**Cannot support:**
- bloom labels or event intervals;
- onset detection or lead-time estimation;
- sensor validation against 0–8 m biomass;
- causal attribution;
- early-warning performance claims.

## 6. What would change the endpoint assessment

- Sub-weekly, time-stamped, depth-resolved microscopy or a validated biomass series.
- A protocol-approved bloom/non-bloom definition with independent adjudication.
- Verified non-event exposure and adequate event counts.
- A taxonomic crosswalk and documented handling of the 200% groups, Coelastrum anomaly and repeated records.
