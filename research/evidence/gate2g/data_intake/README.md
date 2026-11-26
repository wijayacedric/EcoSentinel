# Gate 2G Data Intake Package

**Status:** Templates and validation utilities only. No incoming institutional biological data has been received as of 2026-11-22.

## Purpose
Prepare a reproducible, read-only intake process for any future biological/environmental records received from institutions/researchers. This package does **not** authorize external contact, does **not** create labels, and does **not** change Gate 2 status.

## Contents
- `templates/biological_observation_data_dictionary.csv` - field dictionary/template (includes synthetic example values marked as examples only).
- `templates/provenance_template.json` - provenance metadata template.
- `templates/intake_manifest_template.csv` - manifest for received files.
- `tests/synthetic_biological_sample.csv` - **synthetic software-test fixture only**; not research evidence.
- `../scripts/validate_intake.py` - read-only validator producing JSON report.

## Rules
- Never modify original received files; store originals separately and write derived outputs to `research/evidence/gate2g/derived/` or a source-specific derived folder.
- Record checksums, retrieval date, source, license/terms, and human authorization for acquisition.
- Do not infer missing biological measurements, dates, locations, units, or qualifiers.
- Do not convert units silently; record original units and any conversion as a derived field with documented formula.
- Synthetic test fixtures must be clearly named and never mixed with actual evidence.

## Validation
```bash
python3 research/evidence/gate2g/scripts/validate_intake.py \
  research/evidence/gate2g/data_intake/tests/synthetic_biological_sample.csv \
  --kind biological \
  --out research/evidence/gate2g/derived/validation_synthetic.json
```
