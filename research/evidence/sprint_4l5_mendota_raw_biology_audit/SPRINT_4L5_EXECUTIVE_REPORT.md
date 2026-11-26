# Sprint 4L.5 Executive Report — Raw Mendota Phytoplankton Dataset Audit

**Date:** 2026-11-24T07:22:12.805937+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. What was inspected

The actual CSV `North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__f2de15b2fff6ae962a04c150c0a1c510.dat` was read-only audited: 2,448,830 bytes, MD5 `a0363cc7fdfd6c12889750fea27bd542`, SHA-256 `a63d7cfa0502e3cdab6d8939f21820f305295e030d4d08bf10bfc69b22829db2`. It is ASCII CSV with CRLF, 15 columns, 18,654 data rows, no malformed records, no parse errors.

## 2. Verified dimensions and coverage

- Overall: **18,654 rows / 18,654 records**, 15 columns, 640 unique sampling dates, 1995-01-24 to 2020-12-10.
- **ME:** 9,401 records / **402 dates**; 1995-01-24 to 2020-12-10.
- **MO:** 8,696 records / 355 dates; 2012 is absent; 2020 has only 5 dates.
- **WI:** 532 records / 23 dates (1996–2002 only).
- **FI:** 25 records / 1 date (1995-03-28).
- Mendota: 13–19 dates/year across all 26 years; median gap **14 days**; 72 gaps ≥30 d, 35 ≥60 d, 6 ≥90 d (mostly winter).
- MO has a **462-day gap** from 2011-11-01 to 2013-02-05 (2012 missing).

## 3. Most important data-quality findings

- All seven numeric variables are present (no blanks, negatives or non-finite values), but zeros and extreme values matter.
- `cells_per_ml` is arithmetically consistent with `cells_per_nu × nu_per_ml` (max relative error 0.000228).
- `biomass_conc` is generally ~`biovolume_conc × 1e-6`, but **61 rows have biomass=0 with small positive biovolume**, consistent with low-value truncation; one catastrophic record (ME 2011-07-25 *Coelastrum reticulatum*) has cells=0, biovolume=7.688e-05, biomass=84.6924 and relative=283806.87.
- **`relative_total_biovolume` is not uniformly a percentage summing to 100:** 762/781 sample-groups sum ~100, **14 sum ~200**, 3 sum 0, and 2 are other (one at 98.864 and one catastrophic outlier at 283,906.85). The cause is unresolved.
- **29 exact duplicate row-groups / 58 rows**, all MO 1999-11-22.
- **1,009 same-key groups / 2,048 rows** (11.0% of rows) share lake/date/station/depth/taxon; most differ in cell/biovolume values, consistent with variants/vegetative states. They are not independent observations.
- **40 ME records are labelled 0–2m** (2002) and **310 MO records are labelled 0–8m** (1995/2002–2004), contradicting metadata depth assignments.
- `sta` is blank for 17,518/18,654 records.
- 8,514 records have trailing whitespace in `taxa_name`; 927 have double spaces.

## 4. Biological and taxonomic findings

- **469 distinct cleaned taxa names / 177 genera / 11 divisions**; Cyanophyta is 8,581 records / 127 taxa and **73.2% of summed biovolume** (70.8% of biomass). In ME, median per-sample cyanobacteria biovolume share is **67.2%** (IQR 14.2–94.3%).
- 12 records have blank `taxa_name`; 1,632 have blank `genus` (mostly family/group labels). 20 names are unresolved/infraspecific (`sp.`, `var.`, `cf.`).
- **889 records have genus-field mismatches**: e.g., Coelosphaerium naegelianum → genus Woronichinia (361), Phormidium mucicola → Pseudanabaena (214), Oscillatoria agardhii → Planktothrix (29). These are generally known synonym updates, but `taxa_name` and `genus` are inconsistent.
- Names transition at different times (2008, 2010/2011, 2013, 2015/2016, 2018, 2020), not just February 2013. 204 names occur only pre-2013 and 72 only post-2013. Without a crosswalk, longitudinal species comparisons are not stable.
- The 469-name count is an upper bound; it includes group labels, varieties, and formatting variants (`sp1` vs `sp. 1`).

## 5. Did the original feasibility assumptions survive?

**Partly.**
- **Confirmed:** species-level microscopy, cell density/biovolume/biomass fields, predominantly Mendota 0–8m, biweekly-ish sampling, no QC flags/detection limits, multiple same-date variants.
- **Strengthened:** actual Mendota coverage is 402 dates over 26 years, not merely a metadata claim.
- **Contradicted/weakened:** depth assignments are not perfectly consistent; station IDs are mostly absent; `relative_total_biovolume` is internally anomalous in 19 groups; biomass has truncation/zero issues; taxonomy is not longitudinally stable.

## 6. Is Mendota viable?

**Viable for seasonal/multi-week exploratory comparison of independent microscopy-based cyanobacteria biovolume or cell density with environmental variables — not yet confirmatory.** The dataset supplies a genuine independent biological endpoint and a long Mendota record, but the 0–8m composite vs point-sensor mismatch, 14-day median sampling, taxonomic changes, and unresolved data anomalies prevent a confirmatory early-warning claim.

## 7. Remaining Gate 2 blockers

1. Define and justify the depth comparator for 0–8m composite vs sensor depths.
2. Build and validate a taxonomic crosswalk (2013 and later changes) before longitudinal species-level analysis.
3. Resolve/flag the depth anomalies, `relative_total_biovolume` groups summing to ~200, and the Coelastrum row.
4. Establish detection limits/QC and a defensible biological endpoint definition (biovolume vs cell density vs biomass).
5. Acquire and audit aligned sensor data (129.42/130.29/415.2) with QC and sensor-era mapping.
6. Protocol-approved bloom/non-bloom definitions and matched-FAR/leakage-resistant design (Gate 2; not authorised).

## 8. Recommendation

**Retain as exploratory; continue investigating; do not reject.** The raw data materially improve Mendota's biological evidence base, but they do not make it confirmatory-ready. No labels, event intervals, modelling or hypothesis tests were created.
