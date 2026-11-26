# Raw-File Integrity Verification

**Sprint:** 4L.9  
**Date:** 2026-11-24  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Verdict: PASS — the inspected bytes match the Sprint 4L.8A baseline.**

## 1. Identity

- Package: `knb-lter-ntl.129.42`
- DOI: `10.6073/pasta/9c4b1eecf7a019c7239297b6bf4513c4`
- Entity: `cba9ed12834b8f315d6b10675bb60c5a`
- EML object name: `ntl129_1_v16.csv`
- Local filename: `North_Temperate_Lakes_LTER_Daily_Meteorological_and_Metabolism_Data_-_Lake_Mendota__cba9ed12834b8f315d6b10675bb60c5a.dat`
- Local extension: `.dat` (the bytes are CSV; the extension is a helper/parser artefact documented in Sprint 4L.8A)
- Encoding/format: ASCII CSV text, LF line endings, no BOM
- Date range: **2006-07-09 to 2025-11-18**
- Unique dates: **3,996**
- Data rows: **3,996**
- Columns: **38**
- Calendar-day span: **7,073** days; the file contains records on **56.5%** of those days.

The difference between the calendar span and 3,996 records is the winter/seasonal deployment pattern, not missing daily rows within a claimed year-round series.

## 2. Actual bytes versus baseline

| Check | Actual | Expected | Result |
|---|---|---|---|
| Bytes | **490,187** | 490,187 | **PASS** |
| MD5 | **`eb7b3a3848b27074bac4504236ccefc3`** | `eb7b3a3848b27074bac4504236ccefc3` | **PASS** |
| SHA-1 | **`bb1d8a281a3d580cad45549551abdbaed1ae03fe`** | `bb1d8a281a3d580cad45549551abdbaed1ae03fe` | **PASS** |
| SHA-256 | **`104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343`** | `104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343` | **PASS** |

The bytes were independently hashed with `md5`, `shasum -a 1`, `shasum -a 256` and Python's `hashlib`; all agree.

## 3. Structural checks

- Header order matches the expected 38-field daily schema exactly (2 date fields + 18 variables + 18 interleaved flag columns).
- Every non-header line has 38 comma-separated fields; no malformed records.
- `year4` equals the calendar year of `sampledate` for all 3,996 rows.
- No duplicate dates and no exact duplicate rows.
- All non-empty numeric fields parse as finite floats; there are **no non-numeric non-empty values**.
- Flag fields contain only blank, `C`, `E`, `H`, `G` or `O`. `O` is undocumented (see QC audit).

## 4. Metadata provenance

- The local EML metadata file is `metadata_129.42.xml`, **146,471 bytes**, SHA-256 `c853f0df32f67c49ac47084d4c6f656100b9d014f90da869f0f47ef0db7ebb97`.
- The EML records the daily entity size as 490,187 bytes and MD5 as `eb7b3a3848b27074bac4504236ccefc3`.
- The acquisition provenance log records the PASTA data URL, entity ID, HTTP 200, `text/csv`, 490,187 bytes and SHA-256 `104ef1b33769bc0ad1d3e9e6dff28219b743b81ce89ee888460d2df255981343`.
- The original acquired bytes were not renamed, rewritten or normalised. The `.dat` extension is retained.

## 5. What this establishes and does not establish

**Establishes:** the local file is the intended daily entity; its bytes match the EML size/MD5 and the DataONE CN SHA-1; it is structurally a 38-column CSV with 3,996 daily records and no duplicate dates.

**Does not establish:** that the observations are accurate, calibrated, comparable across sensor eras, or suitable for confirmatory inference. Those are separate scientific and QC questions.

The raw file remains unchanged. No labels, event intervals, models, hypothesis tests or Gate 2 approval were created.
