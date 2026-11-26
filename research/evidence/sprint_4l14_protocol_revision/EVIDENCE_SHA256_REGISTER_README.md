# Sprint 4L.14 Evidence SHA-256 Register — Generation and Verification

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Scope

This register covers every file in:

`research/evidence/sprint_4l14_protocol_revision/`

It excludes:

- `EVIDENCE_SHA256_REGISTER.csv`;
- `EVIDENCE_SHA256_REGISTER.csv.sha256`.

Each row records the repository-relative path, byte size, and SHA-256 digest.

## What is new vs prior

- **New:** Sprint 4L.14 protocol revision documents, source register, search log, and handover.
- **Not included:** raw data files, Sprint 4L.12/4L.13 packages, and prior sprint evidence. Those remain unchanged and separately registered.
- No external correspondence, credentials, or private data are included.

## Generation

The register was generated from the repository root with a deterministic Python script:

```bash
cd /Users/cedricbw/Documents/EcoSentinel
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
root = Path('.').resolve()
base = root / 'research/evidence/sprint_4l14_protocol_revision'
reg = base / 'EVIDENCE_SHA256_REGISTER.csv'
side = base / 'EVIDENCE_SHA256_REGISTER.csv.sha256'
files = [p for p in sorted(base.rglob('*'))
         if p.is_file() and p not in (reg, side)
         and '__pycache__' not in p.parts]
rows = []
for p in files:
    b = p.read_bytes()
    rows.append({'path': str(p.resolve().relative_to(root)),
                 'bytes': len(b),
                 'sha256': hashlib.sha256(b).hexdigest()})
with reg.open('w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=['path', 'bytes', 'sha256'])
    w.writeheader(); w.writerows(rows)
h = hashlib.sha256(reg.read_bytes()).hexdigest()
side.write_text(f"{h}  EVIDENCE_SHA256_REGISTER.csv\n", encoding='utf-8')
print('registered', len(rows), 'files')
print('register sha256', h)
PY
```

## Verification

```bash
cd /Users/cedricbw/Documents/EcoSentinel
shasum -a 256 -c research/evidence/sprint_4l14_protocol_revision/EVIDENCE_SHA256_REGISTER.csv.sha256
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
bad = 0
for row in csv.DictReader(open('research/evidence/sprint_4l14_protocol_revision/EVIDENCE_SHA256_REGISTER.csv', newline='', encoding='utf-8')):
    p = Path(row['path'])
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
        bad += 1
        print('MISMATCH', row['path'])
print('mismatches:', bad)
PY
```

## Verification result

The register was verified after generation:

- registered files: **18** (including this README);
- mismatches: **0**;
- the sidecar hash matches the register SHA-256.

The exact register hash is recorded in:

`EVIDENCE_SHA256_REGISTER.csv.sha256`

## Governance

This register records integrity only. It does not approve the protocol, any of the 15 decisions, or Gate 2. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory Only)**. No analysis is authorised.
