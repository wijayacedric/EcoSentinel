# Sprint 4L.9 Handover

**Date:** 2026-11-24  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status: COMPLETE — EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS.**

## 1. What is complete

- Raw daily file re-verified against the Sprint 4L.8A baseline: 490,187 B; MD5 `eb7b3a3848b27074bac4504236ccefc3`; SHA-1 `bb1d8a281a3d580cad45549551abdbaed1ae03fe`; SHA-256 `104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343`; 3,996 rows; 38 columns.
- Full schema/parse audit: 0 malformed rows, 0 duplicate dates, 0 date errors, 0 non-numeric non-empty values.
- Variable-by-variable coverage, annual and seasonal coverage, interval/gap analysis.
- QC flag audit, including undocumented codes and flag-value distributions.
- Sensor-era comparability, Turner/YSI paired 2019 comparison, DO/water-temperature/pCO2/PAR/conductance caveats.
- Biology–sensor same-day and ±1/±3/±7/±14-day overlap for all 18 variables.
- Depth/spatial compatibility and four-use feasibility assessment.
- Independent second-method verification: zero coverage/overlap/percentage mismatches.
- External search log and source register; full local metadata and authoritative USGS guidance inspected.
- SHA-256 evidence register and sidecar.

## 2. Key facts to carry forward

- **Do not concatenate Turner and YSI chlorophyll/phycocyanin.** 2019 paired medians differ by ~3 orders of magnitude; no crosswalk.
- **Do not treat `avg_do_wtemp` as a clean continuous water-temperature series.** It is YSI-labelled but exists from 2006; 2019+ is heavily `C`-flagged. Ancillary 130 is documented but not acquired.
- **Do not treat `C` as missing** without checking the value column; many `C` records contain numeric values.
- **Do not treat unflagged as validated.** Negative turbidity, negative YSI phycocyanin/chlorophyll and negative PAR below exist unflagged.
- **Do not pool the 2006 conductivity values with 2019+ conductance.** 2006 values are ~0.4 µS/cm and all flagged; 2019+ is ~122–596 µS/cm.
- **Do not pool 0.5 m sensor values with 0–8 m microscopy as if equivalent.** Depth/spatial compatibility is weak/conditional.
- **Do not use 2019+ pH/fDOM/turbidity/conductance for long-term comparison.** Only ~22 same-day biology dates, all 2019–2020.
- **Strongest exploratory biological pairing:** Turner chlorophyll/phycocyanin vs cyanobacteria biovolume or cell density, 2006–2019, 128–139 same-day dates, with all caveats.

## 3. Unresolved issues

1. Undefined `O` flag (one 2006 specific-conductance value).
2. Eight flag columns with values outside their daily-EML code lists.
3. `avg_do_wtemp` pre-2019 provenance and definition conflict.
4. DO instrument identity 2006–2015 (not in sensor inventory).
5. pCO2 inventory start 2017 vs data start 2016.
6. PAR 2007 near-zero values before the sustained 2016+ record.
7. 2006 conductivity scale problem.
8. Unflagged physically implausible values.
9. No per-record calibration, coefficients, serial numbers, detection limits or maintenance logs.
10. No exact within-year sensor-change dates.
11. Biology taxonomy harmonisation unresolved (separate 4L.5/4L.6 issue).
12. No protocol-approved bloom/non-bloom definition.

## 4. Safe next steps (descriptive only)

- If the project continues exploratory work, define a **variable-specific inclusion rule** (e.g., unflagged numeric only; retain flagged values for sensitivity), and state the denominator.
- Define an explicit **depth comparator** before any sensor–biology comparison (surface layer vs 0–8 m composite; sensitivity analysis).
- Keep Turner and YSI eras separate; do not apply an undocumented correction.
- If water temperature is needed, consider the ancillary 130 dataset **only with explicit authorisation**; do not acquire it as part of this sprint.
- Treat same-day overlap as day-level, not intraday.
- Do not create bloom/non-bloom labels, event intervals, model inputs or early-warning claims.

## 5. Reproduce

From the repository root:

```bash
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/audit_sensor_raw.py
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/verify_audit.py
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/write_reports.py
```

## 6. Governance

**Gate 2 remains PAUSED / NOT APPROVED.** No labels, event intervals, confirmatory models, hypothesis tests, protocol changes, external contacts, uploads, commits or pushes were made. The raw daily file and all prior sprint evidence remain unchanged.
