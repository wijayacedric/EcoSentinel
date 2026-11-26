# Inventory Reconciliation — Sprint 4D vs 4D.1 vs 4D.2

**Date:** 2026-11-22T23:14:01.070201+00:00

## Reconciliation

| Source | 5p0x class_and_feat count | Notes |
|---|---:|---|
| Sprint 4D background download manifest (initial) | 39 ok / 20 skipped (59 rows) | May 2022 was missed due race: append to `/tmp/c2g_monthly_resources.csv` occurred in parallel with download script startup; download script read CSV before append. |
| Sprint 4D.1 audit (initial) | 40/60 after correction | May 2022 identified as missing from manifest; downloaded afterward (58MB, <150MB threshold). Inventory corrected to 40 acquired / 20 skipped / 60 total monthly DOIs. |
| Sprint 4D.2 authoritative inventory | **40 acquired / 20 skipped / 60 total** | Matches C2G landing package 60 monthly sub-DOIs (May 2018–Jun 2023). |

## May 2022 verification

- **C2G landing DOI:** `10.25678/x00B8V` (as listed in C2G resource URL) resolves to ERIC package `aquascope_may_2022` (DOI displayed as `10.25678/X00B8V` on CKAN page).
- **Acquired file:** `class_and_feat_5p0xMAG_may2022.tar.gz`, size 57,853,668 bytes, SHA256 `e9e8960ee678d8c56b57b7daa85a1d65ef65ce8158dc4af09d3e8ed595bcf39a`, local path present.
- **Status:** Acquired and included in 40-package set.

## Authoritative totals

- Total C2G monthly sub-DOIs: **60**
- 5p0x class_and_feat acquired: **40**
- 5p0x class_and_feat skipped (>150MB in Sprint 4D): **20**
- Missing/unaccounted: **0** (all 60 accounted for as acquired or skipped)
