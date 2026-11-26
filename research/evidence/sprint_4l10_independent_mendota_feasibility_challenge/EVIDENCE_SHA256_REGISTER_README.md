# Sprint 4L.10 Evidence SHA-256 Register — Scope and Verification

This register covers the Sprint 4L.10 decision evidence under:

`research/evidence/sprint_4l10_independent_mendota_feasibility_challenge/`

## Scope

- All Markdown reports, CSV tables, JSON summaries and Python scripts in this directory are listed.
- Root-level convenience copies and the canonical `tables/` copies are both listed; if they diverge, `tables/` is canonical.
- The register **excludes itself** (`EVIDENCE_SHA256_REGISTER.csv`) and its sidecar (`EVIDENCE_SHA256_REGISTER.csv.sha256`) to avoid a self-reference problem.
- The original raw daily and biology files are outside this directory and are **not** re-hashed here. Their actual hashes are recorded in `summary.json` and in the Sprint 4L.9/4L.8A evidence.
- Prior sprint evidence is preserved and is not included in this register.

## Verify the register

```bash
cd /Users/cedricbw/Documents/EcoSentinel/research/evidence/sprint_4l10_independent_mendota_feasibility_challenge
shasum -a 256 EVIDENCE_SHA256_REGISTER.csv
cat EVIDENCE_SHA256_REGISTER.csv.sha256
```

The two outputs must match.

## Verify individual files

```bash
cd /Users/cedricbw/Documents/EcoSentinel
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
for row in csv.DictReader(open('research/evidence/sprint_4l10_independent_mendota_feasibility_challenge/EVIDENCE_SHA256_REGISTER.csv', newline='', encoding='utf-8')):
    p = Path(row['path'])
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    print('OK' if h == row['sha256'] else 'MISMATCH', row['path'])
PY
```

## Regeneration

```bash
python3 research/evidence/sprint_4l10_independent_mendota_feasibility_challenge/scripts/verify_4l10.py
python3 research/evidence/sprint_4l10_independent_mendota_feasibility_challenge/scripts/write_4l10_reports.py
```

The register is generated only after the independent calculation and reports are final. No commit or push is performed.
