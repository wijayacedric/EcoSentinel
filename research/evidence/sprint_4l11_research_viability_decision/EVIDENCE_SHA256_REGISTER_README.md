# Sprint 4L.11 Evidence SHA-256 Register — Scope and Verification

This register covers the Sprint 4L.11 strategic decision evidence under:

`research/evidence/sprint_4l11_research_viability_decision/`

## Scope

- All Markdown reports, CSV decision tables and the source register in this directory are listed.
- Root-level convenience copies and canonical `tables/` copies are both listed; if they diverge, `tables/` is canonical.
- The register **excludes itself** (`EVIDENCE_SHA256_REGISTER.csv`) and its sidecar (`EVIDENCE_SHA256_REGISTER.csv.sha256`) to avoid self-reference.
- No raw data or prior sprint evidence is included; those remain unchanged and separately registered.
- No external correspondence, credentials or private data are included.

## Verify the register

```bash
cd /Users/cedricbw/Documents/EcoSentinel/research/evidence/sprint_4l11_research_viability_decision
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
for row in csv.DictReader(open('research/evidence/sprint_4l11_research_viability_decision/EVIDENCE_SHA256_REGISTER.csv', newline='', encoding='utf-8')):
    p = Path(row['path'])
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    print('OK' if h == row['sha256'] else 'MISMATCH', row['path'])
PY
```

## Note on the decision

This register records the evidence for the strategic recommendation **CONTINUE — NARROWED RESEARCH QUESTION**. It does not approve Gate 2, create labels, authorise modelling or change the research protocol.
