# Sprint 4L.10 Handover

**Date:** 2026-11-24  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)  
**Status: COMPLETE — independent challenge delivered.**

## 1. Final decision

**Primary recommendation: RETAIN — LIMITED EXPLORATORY USE.**  
**For the original early-warning research question: REJECT Mendota as a validation dataset.**

Mendota remains usable for:
- descriptive seasonal analysis of environmental variables;
- pairwise descriptive comparison of sensor conditions with cyanobacteria biovolume/cell density, with Turner/YSI eras separate and the 0.5 m vs 0–8 m limitation explicit.

It is not usable for bloom/non-bloom labels, event intervals, confirmatory modelling, threshold optimisation or early-warning validation.

## 2. What was independently verified

- **5,439 comparable checks** recomputed from the raw daily and biology files.
- **0 numerical mismatches** versus Sprint 4L.9.
- **0 numerical mismatches** versus a second SQLite calculation.
- **10 interpretive discrepancy rows** recorded in `DISCREPANCY_REGISTER.csv`; no numerical discrepancy.
- Raw daily identity: 490,187 bytes; 38 columns; 3,996 rows; 0 duplicates; 2006-07-09 to 2025-11-18.
- Biology: 402 Mendota dates; 400 0–8 m; 2 0–2 m; 371/402 dates with no station value.

## 3. Decisive new evidence

4L.9 quantified variable-by-variable overlap but not joint sensor–biology coverage. The independent calculation shows:

| Set | Biology dates with all variables valid |
|---|---:|
| Turner chlorophyll + phycocyanin + DO | 79/402 |
| Turner chlorophyll + phycocyanin + DO + water temperature | 64/402 |
| 7-variable Turner core | 58/402 |
| 9-variable Turner + PAR core | 23/402 |
| YSI chlorophyll + phycocyanin + DO | 16/402 |
| YSI chlorophyll + phycocyanin + DO + water temp + pH | 2/402 |
| 11-variable YSI core | 2/402 |

Only **165/402** biology dates have any same-day unflagged sensor variable; **165/230** within 2006–2020.

Sensor-only complete-case coverage is much larger: **939** Turner-core dates and **306** YSI-core dates. The limiting factor is the sensor–biology common support, not the sensor matrix alone.

## 4. Assessment of 4L.9

The 4L.9 arithmetic is reproducible. Its overall verdict — “EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS” — is **directionally correct but insufficiently qualified**:

- A: supported with major limitations.
- B: partially supported, pairwise/descriptive only; not sensor validation.
- C: limited for sensor-only descriptive work; not robustly supported for sensor–biology multivariate analysis.
- D: not supported; reject for the original early-warning question.

The single label should not be used as a green light for B-as-validation or C-as-biological-multivariate.

## 5. Prior-art constraint

Mendota already has:
- high-frequency phycocyanin research (Carpenter et al. 2020, 2022);
- seasonal/sub-seasonal cyanobacteria forecasts (Beal et al. 2021, 2022);
- inclusion in a multi-lake empirical EWS assessment where most indicators performed poorly (O'Brien et al. 2023).

Phycocyanin–biovolume validation is weak/variable (Cotterill et al. 2019; Levi et al. 2025). No novelty can be claimed from the dataset alone or from matched false-alarm rates.

## 6. Unresolved issues carried forward

1. No bloom/non-bloom definition or independent event adjudication.
2. No time-of-day or sub-weekly biology; 14-day median interval.
3. 0.5 m point sensor vs 0–8 m composite; no depth profile.
4. No Turner/YSI cross-calibration.
5. Undefined `O` flag; eight flag columns with undocumented values.
6. Pre-2016 DO and pre-2019 `avg_do_wtemp` provenance unresolved.
7. Taxonomy non-stationarity; 200% relative-bio volume groups; Coelastrum anomaly; repeated records.
8. Unflagged physical implausibilities (negative turbidity/phycocyanin/PAR).
9. No per-record calibration/maintenance history.

## 7. Safe next steps

- If the project continues Mendota work, restrict it to A and pairwise B.
- Define an explicit depth comparator before any sensor–biology comparison.
- Keep Turner/YSI eras separate; use `unflagged_numeric` and report flag sensitivity.
- Use pairwise or small (2–4 variable) descriptive comparisons; do not build 7–11-variable biological multivariate models.
- Do not create labels, event intervals, predictive models or early-warning claims.
- No new dataset acquisition or broad dataset search is justified by this challenge alone.

## 8. Reproduce

```bash
python3 research/evidence/sprint_4l10_independent_mendota_feasibility_challenge/scripts/verify_4l10.py
python3 research/evidence/sprint_4l10_independent_mendota_feasibility_challenge/scripts/write_4l10_reports.py
```

## 9. Governance

Gate 2 remains **PAUSED / NOT APPROVED — option C**. No labels, event intervals, confirmatory models, hypothesis tests, threshold optimisation, protocol changes, external contacts, uploads, commits or pushes were made. The raw daily file, 88.31 biology file and all prior sprint evidence remain unchanged.
