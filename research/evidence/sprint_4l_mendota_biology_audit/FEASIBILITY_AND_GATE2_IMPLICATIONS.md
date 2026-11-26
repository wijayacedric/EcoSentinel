# Feasibility and Gate 2 Implications — Mendota Phytoplankton 88.31

**Date:** 2026-11-23T23:58:36.852965+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Adversarial assessment

### 1. Biological sampling cadence and long gaps

Documented biweekly ice-free, 4-weekly late season, usually one winter sample. This can resolve seasonal and multi-week changes but **cannot resolve sub-biweekly onset**. Under-ice gaps are long. Actual gaps are unverified because raw data were not acquired.

### 2. Depth mismatch: 0–8 m composite vs point sensors

Mendota phytoplankton is a **depth-integrated 0–8 m composite**. Buoy chlorophyll/phycocyanin is documented at **0.5 m**, DO at ~0.5 m, temperature at discrete depths. A composite biomass is not equivalent to a surface-point sensor. A defensible comparator (surface layer, euphotic-zone integration, or biomass-weighted depth) must be defined before any comparison. This is a first-order limitation, not a technicality.

### 3. Temporal alignment

The biological schema has **date only**, no sample time. Buoy data are 1-minute. Matching can be **day-level only**; diel DO/pH cycles and within-day bloom movement cannot be aligned. Any claim of exact temporal co-location would be false.

### 4. Independent cyanobacterial presence/abundance

Microscopy counts and biovolume can independently establish cyanobacterial presence and abundance **if** the raw taxonomy is complete and harmonised. Unlike phycocyanin RFU, they are not sensor-derived. This is the dataset's main strength. But species may be unresolved, and 2013 taxonomy changes must be handled.

### 5. Sufficient non-bloom exposure

The long record includes winter/spring/fall and low-biomass periods, so non-bloom exposure is **plausibly available**. However, "bloom" and "non-bloom" are not defined in the dataset, and no labels were created. A protocol-approved event definition and independent evidence (biovolume threshold, toxins, visual/remote sensing) are required. Without that, non-bloom exposure is not defensible.

### 6. Methodological changes

- February 2013 taxonomic updates.
- Possible changes in analyst/QA after 2010/2023 (not verified).
- Detection limits/QC flags absent.
- Sampling schedule changes (biweekly vs monthly vs winter).
These can create artificial step changes in richness/composition and must be harmonised or stratified.

### 7. Independence from sensor-derived pigments

Microscopy is **measurement-independent** of Turner/YSI chlorophyll/phycocyanin. It is not statistically independent of the same lake/environment, but it can serve as an independent biological validation of sensor proxies. This is scientifically valuable.

### 8. Can it support the early-warning question at any defensible resolution?

- **Seasonal/multi-week:** potentially yes, with 25 years of biweekly biology and 1-min environmental data, subject to raw verification, depth comparator and event definitions.
- **Sub-weekly/daily:** no, because biology is biweekly/monthly.
- **Matched-FAR evaluation:** potentially feasible over many years if independent events/non-events can be defined; not established now.

### 9. Appropriate analysis scale

Seasonal to multi-week. Not finer than the biological sampling interval. Any "early warning" should be framed at that scale, not daily.

### 10. Evidence required to resolve uncertainties

- Raw CSV acquisition and structural audit (Mendota subset, dates, taxa, missingness, duplicates, units).
- Detection limits/QC documentation and taxonomy crosswalk.
- Sample times/station/depth records.
- Protocol-approved event/non-bloom definitions and independent event evidence.
- Sensor validation and depth comparator.
- Version reconciliation (31 vs 32) and licence confirmation.

## Gate 2 implications

| Requirement | Status |
|---|---|
| Independent biological ground truth | **Potentially supported** (metadata; raw unverified) |
| Defensible bloom/non-bloom evidence | **Unresolved** (no labels; no event definition) |
| Adequate temporal resolution | **Conditional** (seasonal/multi-week; not sub-weekly) |
| Spatial/depth alignment | **Unresolved** (0–8 m composite vs point sensors) |
| Fair false-alarm/leakage-resistant validation | **Potentially feasible** over 25 years, not established |
| Access | **Blocked** (no EDI key) |

## Adversarial conclusion

The dataset is **not disqualified** by its design: it has a genuine, independent, species-level biological endpoint over 25 years and a plausible seasonal/multi-week use. It is **not yet suitable for confirmatory early warning**: raw data are unverified, depth mismatch is serious, sampling is biweekly, and no event/non-bloom protocol exists.

**Recommendation: continue investigating under Option C; retain as exploratory; do not advance to Gate 2.**
