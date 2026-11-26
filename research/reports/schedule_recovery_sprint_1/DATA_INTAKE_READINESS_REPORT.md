# Data Intake Readiness Report

**Sprint:** Schedule Recovery Sprint 1  
**Date:** 2026-11-22  
**Scope:** Technical/operational readiness only. No biological interpretation, no label generation, no Gate 2 approval.

## 1. Intake workflow (current)

1. **Receive file** (human-authorized only). Do not request/send externally in this sprint.
2. **Preserve original** in a source-specific raw intake location; do not modify original file.
3. **Record provenance** using `research/evidence/gate2g/data_intake/templates/provenance_template.json` and manifest template.
4. **Compute checksum** (SHA-256) and record size/retrieval metadata.
5. **Validate read-only** with `research/evidence/gate2g/scripts/validate_intake.py`.
6. **Review report** (errors/warnings) before any derived normalization.
7. **Create derived copy only if needed** in a clearly named derived folder; document every transformation. No silent unit conversion.
8. **Human scientific review** before any use in evidence adjudication. No automatic bloom/non-bloom labeling.

## 2. Validation checks implemented

Script: `research/evidence/gate2g/scripts/validate_intake.py` (read-only).

| Check | Status | Behavior |
|---|---|---|
| File existence/size/SHA-256 | Implemented | Reports `exists`, `sha256`, `size_bytes`; errors if missing |
| CSV/XLSX read | Implemented | CSV stdlib; XLSX requires `openpyxl` (reports limitation if unavailable) |
| Required biological fields | Implemented | Warns if `sample_date`, `location`, `depth_m` missing for `--kind biological` |
| Recommended biological fields | Implemented | Reports missing recommended fields |
| Duplicate column names | Implemented | Case-insensitive warning |
| Empty rows | Implemented | Counted in summary |
| Sample date validity | Implemented | YYYY-MM-DD validated with `strptime`; non-ISO parseable date warned; invalid errors |
| Numeric field parsing | Implemented | Invalid numeric values error for known numeric fields |
| Duplicate-row heuristic | Implemented | Warns on duplicate key (date/location/depth/sample_id/taxon/replicate) |
| Qualifier/detection-limit consistency | Implemented | Warnings only; does not infer missing/below-LOD meaning |
| Measurement unit presence | Implemented | Warns when measurement has value but unit missing or unit field absent |
| Provenance note | Implemented | Report includes `provenance_note` stating no source modification/no labels |

## 3. Provenance preservation

- Source files are never modified by validator.
- Validator outputs JSON report to `--out`; can be stored in `research/evidence/gate2g/derived/` or source-specific derived folder.
- Templates available: `provenance_template.json`, `intake_manifest_template.csv`, `biological_observation_data_dictionary.csv`.
- Checksum recorded in report; original checksum should also be recorded in manifest/provenance template.

## 4. Supported formats

| Format | Read | Validation | Notes |
|---|---:|---:|---|
| CSV | Yes | Yes | Stdlib, UTF-8-sig, replacement errors |
| XLSX/XLSM | Partial | Partial | Requires `openpyxl`; validator reports clear error if unavailable |
| Other | No | No | Manual human-reviewed conversion required; preserve original |

## 5. Remaining limitations / human-review requirements

- **No automatic schema mapping:** files with different column names require human mapping to data dictionary.
- **No unit conversion:** conversion must be explicit, documented, and reviewed; never silent.
- **No biological interpretation:** validator does not adjudicate bloom/non-bloom, taxonomic validity, or ecological meaning.
- **No merge across locations/methods without documentation.**
- **Missing/ND/<LOD:** preserved as reported; validator warns on inconsistencies but does not infer.
- **XLSX dependency:** `openpyxl` not verified in base env; may be present in ecosentinel env but not tested here.
- **Duplicate heuristic** is conservative and may over/under-flag; human review required.
- **Timezones and datetime precision** need human confirmation for cross-source comparison.
- **Real institutional data** may include PII/licensing restrictions; handle per provenance/authorization.

## 6. Synthetic testing results

Command:
```bash
python3 -m unittest discover -s research/evidence/gate2g/data_intake/tests -p 'test_*.py'
```
Result: **Ran 5 tests in 0.167s — OK**.

Tests cover: synthetic fixture validation, source hash unchanged, missing required fields warning, invalid date/numeric errors, duplicate-row warning, missing-file error. All fixtures are synthetic and labeled as such.
