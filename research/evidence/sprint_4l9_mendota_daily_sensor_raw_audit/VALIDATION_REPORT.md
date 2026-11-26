# Validation and Independent QC

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Checksums and structure

- Raw bytes **490,187**; MD5 `eb7b3a3848b27074bac4504236ccefc3`; SHA-1 `bb1d8a281a3d580cad45549551abdbaed1ae03fe`; SHA-256 `104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343`.
- **3,996** data rows; **38** columns; **0** malformed rows; **0** blank lines.
- **0** date-parse errors; **0** duplicate dates; **0** exact duplicate rows; **0** year/date mismatches.
- Header order matches the expected daily schema.
- Independent parser (simple comma splitting) reproduced 3,996 rows, 38 columns, 0 bad field counts, 0 duplicate dates, 0 exact duplicates, and the same date range.
- `wc -l` = 3,997 lines including header; `awk` found 0 lines with field count ≠ 38.

## 2. Audit validation

The audit's own checks: **17 passed / 1 failed**.

The one failed check is **not an arithmetic failure**: it records that eight flag columns contain values outside their own daily-EML code list. This is a documented metadata non-conformance:

| Variable | Documented daily codes | Extra values |
|---|---|---|
| `avg_rel_hum` | C, E | H |
| `avg_wind_speed` | C | H |
| `avg_par_below` | C, G | H |
| `avg_do_wtemp` | C, H | E |
| `avg_ph` | C | E |
| `avg_fdom` | C | E |
| `avg_turbidity` | C | E |
| `avg_spec_cond` | C, H | E, O |

The extra codes include the undefined `O` value in `flag_avg_spec_cond`, `H` values in `flag_avg_wind_speed`/`flag_avg_rel_hum`/`flag_avg_par_below`, and `E` values in several 2019+ columns. They are retained and reported, not corrected.

## 3. Arithmetic and percentage reconciliation

- For every variable: `missing + numeric_any = total_records`.
- For every variable: `valid_unflagged + flagged_numeric = numeric_any`.
- For every variable: `C + E + H + G + O + other + none = total_records`.
- All percentages are in 0–100 and reconcile with their counts to 1e-6.
- Biology overlap: `same_day_valid + same_day_flagged = same_day_any_numeric`; `same_day_any + same_day_variable_missing = same_day_record_present`; `same_day_record_present + same_day_date_absent = within_valid_span`.
- Window counts are monotonic: same-day ≤ ±1 ≤ ±3 ≤ ±7 ≤ ±14.

These checks were reproduced by the independent second-method script with **zero coverage mismatches, zero overlap mismatches, and zero percentage issues** (`INDEPENDENT_VERIFICATION.md`).

## 4. Unresolved discrepancies

1. **Undefined `O` flag** in `flag_avg_spec_cond` (1 value, 2006-08-11).
2. **Daily EML code-list omissions** for eight columns (above).
3. **`avg_do_wtemp` definition conflict:** labelled YSI water temp but present from 2006, before the YSI EXO2 era.
4. **DO inventory conflict:** daily DO exists from 2006, but the sensor inventory's DO records begin 2016.
5. **pCO2 inventory conflict:** daily pCO2 begins 2016-03-22, but the inventory lists the CO2 sensor from 2017.
6. **PAR 2007 near-zero values:** 11 unflagged near-zero values (ten 0.0, one 0.002) before the sustained 2016+ PAR record.
7. **Conductivity 2006 scale:** values ~0.38–0.48 µS/cm, all flagged; no valid 2006 value.
8. **Unflagged implausible values:** negative turbidity, negative YSI phycocyanin/chlorophyll, negative PAR below; these are not automatically valid.
9. **No per-record calibration/maintenance history** or exact sensor-change dates.

These are reported as unresolved. No value was silently corrected, deleted or imputed.

## 5. Reproducibility

From the repository root:

```bash
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/audit_sensor_raw.py
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/verify_audit.py
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/write_reports.py
```

The audit reads the preserved raw files and writes only under the Sprint 4L.9 evidence directory. It does not modify the raw file or prior sprint evidence.
