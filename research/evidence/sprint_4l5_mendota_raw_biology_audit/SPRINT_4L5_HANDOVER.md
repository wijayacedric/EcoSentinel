# Sprint 4L.5 Handover

**Date:** 2026-11-24T07:23:09.883291+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status: COMPLETE for the requested raw audit; confirmatory work remains prohibited.**

## What was done

- Verified raw file size/MD5/SHA256 and CSV structure: 2,448,830 B, 18,654 rows, 15 columns, no parse errors.
- Audited coverage, sampling intervals, all seven biological variables, taxonomy, duplicates, depth/station structure.
- Generated machine-readable tables and this report set from the raw file using `scripts/audit_raw.py` and `scripts/supplemental_tables.py`.
- Conducted targeted external research on NTL/PhycoTech methods, biovolume/biomass, taxonomy, temporal resolution and prior art.
- No labels, event intervals, modelling, hypothesis tests, protocol changes, commits or pushes.

## Headline findings

- ME: 402 dates / 9,401 records, 1995–2020, 13–19 dates/year, median gap 14 days.
- MO: 355 dates; 2012 missing. WI/FI sparse (23/1 dates).
- Cyanophyta: 8,581 records / 127 taxa, 73.2% of summed biovolume; ME median sample share 67.2%.
- 469 name-units / 177 genera; 12 blank taxa, 1,632 blank genus, 8,514 trailing-space records, 889 genus mismatches.
- 204 pre-only / 72 post-only names; transitions span 2008–2020, not just 2013.
- 29 exact duplicate groups/58 rows, all MO 1999-11-22; 1,009 same-key groups/2,048 rows.
- Depth exceptions: 40 ME 0–2m; 310 MO 0–8m.
- Relative totals: 14 groups sum ~200, 3 sum 0, one at 98.864, one catastrophic outlier (row 283,806.87 / group sum 283,906.85).
- 61 biomass zeros with positive biovolume; one catastrophic Coelastrum row.

## What remains unresolved

- Why depth labels contradict metadata.
- Why 14 groups sum to ~200 relative total; whether it is aggregation/rounding.
- Whether Coelastrum/Actinastrum extremes are data-entry/unit errors.
- Exact sample times, field protocol, station IDs.
- Validated taxonomy crosswalk/QC/detection limits.
- Sensor data/QC/calibration and depth comparator for future alignment.

## Recommended next steps

1. Build a documented taxonomic crosswalk from HCB-1/AlgaeBase and apply it only in a derived layer.
2. Resolve/flag depth anomalies and relative/biomass inconsistencies with NTL/PhycoTech.
3. Acquire/audit 129.42 daily data and sensor list; define the depth comparator.
4. Conduct exploratory seasonal/multi-week analyses only; no labels or confirmatory claims.
5. Gate 2 remains paused; event/non-bloom design requires separate approval.

## Files

All deliverables and tables under `research/evidence/sprint_4l5_mendota_raw_biology_audit/`; scripts under `scripts/`; raw file remains in the 4L acquisition directory, unmodified.
