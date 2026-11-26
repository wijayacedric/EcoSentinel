# Sprint 4L.13 Evidence SHA-256 Register — Scope and Verification

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Scope

This register covers every file in:

`research/evidence/sprint_4l13_independent_protocol_challenge/`

It excludes:

- `EVIDENCE_SHA256_REGISTER.csv`;
- `EVIDENCE_SHA256_REGISTER.csv.sha256`.

Each row records the repository-relative path, byte size, and SHA-256 digest.

## Verify the register

From the repository root:

```bash
cd /Users/cedricbw/Documents/EcoSentinel
shasum -a 256 -c research/evidence/sprint_4l13_independent_protocol_challenge/EVIDENCE_SHA256_REGISTER.csv.sha256
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
bad = 0
for row in csv.DictReader(open('research/evidence/sprint_4l13_independent_protocol_challenge/EVIDENCE_SHA256_REGISTER.csv', newline='', encoding='utf-8')):
    p = Path(row['path'])
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
        bad += 1
        print('MISMATCH', row['path'])
print('mismatches:', bad)
PY
```

## Regeneration

Regenerate after any edit. The register is a snapshot, not a live monitor.

## Governance

This register records integrity only. It does not approve the protocol, any of the 15 decisions, or Gate 2. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory Only)**.
