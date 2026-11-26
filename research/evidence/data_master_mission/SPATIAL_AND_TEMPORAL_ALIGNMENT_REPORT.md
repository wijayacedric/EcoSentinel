# Spatial and Temporal Alignment Report

**Date:** 2026-11-23T23:18:29.122618+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Buffalo Pound — VERIFIED ALIGNMENT (descriptive)

- **Biological location/depth:** "Buffalo Pound", 0.8 m (all 2018/2019 taxonomy rows).
- **Buoy shallow sensors:** 0.8 m (TempShallow, pHShallow, ODOShallow, SpCondShallow, TurbShallow, ChlRFUShallow, BGPCShallow). **Exact depth match.**
- **Date overlap:** all 25 biological dates in 2018 matched buoy days; all 17 in 2019 matched. On matched days, ~130-134 buoy records/day and BGPC/pH/DO present on every matched day.
- **Spatial:** single buoy and single biological station; no horizontal separation analysis possible from files; biological README coordinates (50°35'8.8"N, 105°23'0.24"W) are the lake site. Buoy coordinates not independently re-verified in this mission.
- **Temporal precision:** biological dates are day-level (DOY), no sample time; buoy is 10-min. Alignment should use daily aggregates, not sub-daily matching.
- **No interpolation performed; no labels created.**

## Lake Mendota — UNRESOLVED

- Lake name match alone is insufficient. 88.31 is "Madison Lakes Area" with `lakeid`; Mendota subset not isolatable without data.
- Station/depth/timestamp alignment cannot be assessed. 129/130/415 depths differ and require reconciliation.
- 130.29 2015 HR gap is bounded (one year) but relevance depends on chosen analysis window.

## Western Lake Erie — UNRESOLVED

- 10 stations vs buoy locations; depth compatibility unknown; no raw files.

## Greifensee — PARTIAL

- Aquascope at 3 m; CTD profile/nutrients; temporal overlap high but biological endpoint classifier-derived.

## Bottom line

**Only Buffalo Pound has verified biological–environmental alignment** (same depth, all sampling dates matched, 10-min predictors). Mendota could be equal or better if access is granted, but that is unverified.
