# Biological Endpoint Assessment

**Date:** 2026-11-24T07:23:09.883291+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Independence

The phytoplankton data are direct microscopy observations (Utermöhl method, PhycoTech), not sensor-derived. They are therefore **measurement-independent** of the buoy chlorophyll/phycocyanin/DO sensors. They are not statistically independent of the lake environment, but they can serve as an independent biological reference for sensor proxies.

## Can cyanobacterial abundance be derived?

- `division = Cyanophyta` identifies 8,581 records / 127 taxa.
- Cyanophyta accounts for 73.2% of summed biovolume and 70.8% of summed biomass; in ME, the median per-sample cyanobacteria biovolume share is 67.2% (IQR 14.2–94.3%).
- Derivation is possible, but the taxonomy includes historical names, group labels and unresolved taxa; a crosswalk is required before species-level claims.
- No bloom/non-bloom threshold was defined.

## Which biological metric is most defensible?

| Metric | Strengths | Limitations | Recommended use |
|---|---|---|---|
| **Biovolume** | Integrates cell size and abundance; standard phytoplankton biomass proxy; less sensitive to colony-vs-cell counting than cell density | Derived from geometric shapes; extreme values; some group labels; no detection limits | **Primary exploratory endpoint** |
| Cell density | Direct count; three density fields are arithmetically consistent | Natural-unit/cell distinction; colonial taxa; high variability; not biomass | Complementary abundance endpoint |
| Biomass | Converted from biovolume; familiar units | 61 zero values at low biovolume; one catastrophic row; conversion assumption | Secondary/validation only |
| Relative total biovolume | Compositional context | 14 groups sum ~200, 3 sum 0, one at 98.864, and one catastrophic outlier at 283,906.85 sum (row 283,806.87) | Do not use without resolving denominator |

## Taxonomic comparability

- 204 names only pre-2013, 72 only post-2013; transitions occur across 2008–2020, not only February 2013.
- 889 genus-field mismatches; 8,514 trailing-space records; 1,632 blank-genus records; 20 unresolved names.
- **Species-level longitudinal comparisons are not defensible without a documented crosswalk and QC.**
- Genus/division-level aggregation is more defensible but still requires mapping of historical names.

## Sampling cadence and temporal resolution

- ME: 402 dates over 26 years; 13–19 dates/year; median gap 14 days; 72 gaps ≥30 days (mostly winter).
- MO: 355 dates; 2012 missing; 2020 only 5 dates.
- This supports **seasonal to multi-week** analyses. It cannot resolve hours-to-days bloom onset or short-lived events; the Nyquist-like limit is roughly the 2-week sampling interval.

## Non-bloom exposure

- Low-cyanobacteria samples exist (ME per-sample share IQR lower quartile 14.2%), and winter/spring samples are present.
- But “bloom” and “non-bloom” are not defined in the dataset; no event labels were created. Verified non-bloom exposure requires a protocol-approved definition and independent supporting evidence.
- The dataset is therefore suitable for exploring low/high biomass states, not for asserting verified non-bloom intervals.

## Conclusion

**Suitable as an exploratory biological reference for seasonal/multi-week comparisons, especially cyanobacteria biovolume; not sufficient for confirmatory early warning at daily resolution.** The primary scientific limitations are the depth-integrated composite versus point sensors, 14-day biology, and taxonomic non-stationarity.
