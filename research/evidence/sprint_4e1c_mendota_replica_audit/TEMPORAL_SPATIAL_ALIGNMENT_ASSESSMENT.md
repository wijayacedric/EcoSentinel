# Temporal/Spatial Alignment Assessment — Mendota (Sprint 4E.1C)

**Date:** 2026-11-23T07:05:41.270436+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Status: Unresolved (metadata-only; no raw data alignment performed)

| Check | Status | Evidence | Needed |
|---|---|---|---|
| Lake identity | Unresolved | 88.31 is "Madison Lakes Area" with `lakeid` field; 130.29/415.2 are Lake Mendota-titled. | Confirm Mendota-only records in 88.31. |
| Date overlap | Partially promising | 88.31 1995-2020; 130.29 2006-2019; 415.2 2006-2019. | Exact overlapping dates at usable frequency. |
| Sampling frequency compatibility | Unresolved | Phytoplankton cadence unknown; 130.29 HF/daily/hourly temp; 415.2 routine discrete. | File-level cadence/gap audit. |
| Spatial/depth compatibility | Unresolved | 88.31 has `sta`, `depth_range`; 130.29 has `depth`; 415.2 has `Depth.m`. | Station/depth reconciliation. |
| Missingness/gaps | Unresolved | No file-level audit. | Compute missingness by variable/time. |
| Observation bias | Unresolved | Biological sampling may be routine or event-influenced. | Methods/metadata review. |

**No alignment assumed from matching lake names. No interpolation, labels, or non-bloom intervals created.**
