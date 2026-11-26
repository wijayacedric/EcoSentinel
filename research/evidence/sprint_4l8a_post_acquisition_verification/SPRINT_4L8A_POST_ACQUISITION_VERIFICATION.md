# Sprint 4L.8A — Post-Acquisition Filename Discrepancy and Integrity Verification

**Date:** 2026-11-24T09:48:53.772752+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Verdict: INTEGRITY PASS — the downloaded bytes are correct; the helper warning is a filename-extension false negative.**

## 1. Actual file identity and format

- Package: `knb-lter-ntl.129.42`
- DOI: `10.6073/pasta/9c4b1eecf7a019c7239297b6bf4513c4`
- Entity: `cba9ed12834b8f315d6b10675bb60c5a`
- EML object name: `ntl129_1_v16.csv`
- Local path: `research/evidence/sprint_4l7_mendota_daily_sensor_audit/acquisition/129.42/North_Temperate_Lakes_LTER_Daily_Meteorological_and_Metabolism_Data_-_Lake_Mendota__cba9ed12834b8f315d6b10675bb60c5a.dat`
- Local extension: `.dat`
- Format: **CSV text** (ASCII, LF line endings, no BOM), despite `.dat` extension.
- Header: **38 columns**.
- Data rows: **3,996**; malformed rows: **0**.
- Date range: **2006-07-09 to 2025-11-18**; unique dates **3,996**; unique years **20**.

This is a structural/format check only; the full variable/QC audit is not part of this sprint.

## 2. Independent hashes

| Check | Actual | Expected | Result |
|---|---|---|---|
| Bytes | **490,187** | 490,187 | **PASS** |
| MD5 | **`eb7b3a3848b27074bac4504236ccefc3`** | `eb7b3a3848b27074bac4504236ccefc3` | **PASS** |
| SHA-1 | **`bb1d8a281a3d580cad45549551abdbaed1ae03fe`** | CN sysmeta `bb1d8a281a3d580cad45549551abdbaed1ae03fe` | **PASS** |
| SHA-256 | **`104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343`** | independently calculated | recorded |

**Integrity verdict: PASS.** The actual downloaded bytes match the EML size/MD5 and the DataONE CN SHA-1. This is a byte-level verification, not a scientific validation of the observations.

## 3. Provenance and entity identity

- The acquisition provenance row records the correct entity ID, source URL, local path, 490,187 bytes, and SHA-256 `104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343`.
- The provenance `eml_checksum` field is blank and its note says `no EML checksum`. That is a **provenance-parser gap**, not an integrity failure: the EML uses `<authentication method="MD5">` while the parser looks for `<checksum>`. Independent MD5 verification above establishes the match.
- The local filename is derived from the EML entity name + entity ID + extension; it is not the EML `objectName` (`ntl129_1_v16.csv`). The original object bytes were not renamed or modified.

## 4. `.dat` versus `.csv` discrepancy — precise cause

1. `parse_eml_inventory()` in `edi_mendota_acquire.py` only populates `entity["format"]` from an EML `<formatName>` element.
2. The 129.42 daily EML contains `<dataFormat><textFormat>...` but **no `<formatName>`**; therefore `entity["format"]` is empty.
3. `download_entity()` sets:
   `ext = ".csv" if "csv" in (entity.get("format") or "").lower() else ".dat"`
   Empty format → `.dat`.
4. The helper's final discovery step searches only:
   `find "$OUTDIR/129.42" -name "*${ENTITY}*.csv"`
   so it cannot find the `.dat` file and prints:
   `Acquisition completed but no expected CSV was found`.

The warning is therefore a **cosmetic helper false negative**. The downloaded file is correct CSV data.

## 5. Minimal correction (proposed, not applied)

Do **not** rename the original file. The smallest safe fix is in the helper discovery rule, not the acquisition bytes:

```bash
# Proposed minimal change
FILE="$(find "$OUTDIR/129.42" -maxdepth 1 -type f -name "*${ENTITY}*" -print -quit)"
```

Then verify the file is CSV by inspecting the header/`file` output, and keep the existing size/MD5/SHA-256 checks.

Optional, separate provenance improvement (not required for this file): make the EML inventory parser also read `<authentication method="MD5">` so `provenance.csv` records the EML checksum instead of `no EML checksum`.

No correction was applied; no existing script, provenance, or raw file was overwritten.

## 6. Handover for the raw daily sensor audit

The daily file is now safe to use as the **original** for the next audit:

- Preserve `North_Temperate_Lakes_LTER_Daily_Meteorological_and_Metabolism_Data_-_Lake_Mendota__cba9ed12834b8f315d6b10675bb60c5a.dat` unchanged.
- Use the hash values above as the integrity baseline.
- Proceed to the 38-field schema/18-variable/18-flag audit, variable-specific coverage, missingness, intervals/gaps, C/E/H/G distributions, Turner/YSI eras, and biology-date overlap.
- Do not label blooms, define events, model, or change Gate 2.

**Gate 2 remains PAUSED / NOT APPROVED.**
