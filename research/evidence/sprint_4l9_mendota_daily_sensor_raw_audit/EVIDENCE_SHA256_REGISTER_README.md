# Evidence SHA-256 Register — Scope and Verification

This register covers the Sprint 4L.9 deliverables under:

`research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/`

## Scope

- All Markdown reports, CSV audit tables, JSON summaries/validations, and Python scripts in the Sprint 4L.9 directory are listed.
- Root-level convenience copies and the canonical `tables/` copies are both listed; if they diverge, `tables/` is canonical.
- The register **excludes itself** (`EVIDENCE_SHA256_REGISTER.csv`) and its sidecar (`EVIDENCE_SHA256_REGISTER.csv.sha256`) to avoid a self-reference problem.
- The original raw daily file is outside this directory and is **not** re-hashed here. Its actual hashes are recorded in `RAW_FILE_INTEGRITY.csv` and `RAW_FILE_INTEGRITY_VERIFICATION.md`, and match the Sprint 4L.8A baseline.
- Prior sprint evidence is preserved and not included in this register.

## Verify the register

```bash
cd /Users/cedricbw/Documents/EcoSentinel/research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit
shasum -a 256 EVIDENCE_SHA256_REGISTER.csv
cat EVIDENCE_SHA256_REGISTER.csv.sha256
```

The two outputs must match.

## Verify individual files

```bash
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
for row in csv.DictReader(open('EVIDENCE_SHA256_REGISTER.csv', newline='', encoding='utf-8')):
    p = Path(row['path'])
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    print('OK' if h == row['sha256'] else 'MISMATCH', row['path'])
PY
```

Run from the repository root, because the register stores repository-relative paths.

## Regeneration

The register is generated only after the audit, independent verification and reports are final. The scripts that produce the underlying outputs are:

```bash
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/audit_sensor_raw.py
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/verify_audit.py
python3 research/evidence/sprint_4l9_mendota_daily_sensor_raw_audit/scripts/write_reports.py
```

No commit or push is performed.
