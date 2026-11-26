# Evidence SHA-256 Register — Scope and Use

**Sprint:** 4L.12  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## What the register covers

`EVIDENCE_SHA256_REGISTER.csv` lists every file in this sprint directory except:

- the register itself (`EVIDENCE_SHA256_REGISTER.csv`);
- its sidecar (`EVIDENCE_SHA256_REGISTER.csv.sha256`).

Each row records the relative path, byte size, and SHA-256 digest.

## What it does not cover

- Raw data files outside this sprint directory.
- Prior sprint evidence outside this sprint directory.
- The `.sha256` sidecar itself (its digest is recorded in the sidecar content and can be verified with `shasum -a 256`).

## How to verify

From the repository root:

```bash
cd /Users/cedricbw/Documents/EcoSentinel
shasum -a 256 -c research/evidence/sprint_4l12_narrowed_question_protocol/EVIDENCE_SHA256_REGISTER.csv.sha256
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
bad = 0
for row in csv.DictReader(open('research/evidence/sprint_4l12_narrowed_question_protocol/EVIDENCE_SHA256_REGISTER.csv', newline='', encoding='utf-8')):
    p = Path(row['path'])
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
        bad += 1
        print('MISMATCH', row['path'])
print('mismatches:', bad)
PY
```

## Regeneration

Regenerate after any edit to a sprint file. The register is a snapshot, not a live integrity monitor.

## Governance

This register records integrity only. It does not approve the protocol, authorise analysis, or change Gate 2. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory Only)**.
