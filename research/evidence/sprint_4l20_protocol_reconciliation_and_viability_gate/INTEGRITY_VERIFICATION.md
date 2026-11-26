# Integrity Verification — Sprint 4L.20

**Date:** 2026-11-26  
**Scope:** New Sprint 4L.20 package only.  
**Result:** **PASS — 18 registered files, 0 SHA-256 mismatches.**

---

## 1. Register

| Item | Value |
|---|---|
| Register | `EVIDENCE_SHA256_REGISTER.csv` |
| Sidecar | `EVIDENCE_SHA256_REGISTER.csv.sha256` |
| Algorithm | SHA-256 |
| Registered files | 18 |
| Register SHA-256 | `8af47037b49f496c71667cba0ea0e16f2013b39a2bab548d87be921b37ddb8d6` |

---

## 2. Registered files

| File | Bytes |
|---|---:|
| `ADVERSARIAL_REVIEW_4L20.md` | 13,459 |
| `BUFFALO_POUND_STAGE1_DECISION.md` | 10,315 |
| `COMPETITION_STRATEGY_REASSESSMENT.md` | 9,879 |
| `CURRENT_PROTOCOL_RECONSTRUCTION.md` | 14,658 |
| `DECISION_DEPENDENCY_MAP.md` | 8,692 |
| `ESTIMAND_HIERARCHY_RECOMMENDATION.md` | 8,492 |
| `EXTERNAL_SEARCH_LOG.md` | 9,141 |
| `MENDOTA_STANDALONE_VIABILITY.md` | 12,874 |
| `NEXT_ACTION_PLAN.md` | 7,605 |
| `ORIGINALITY_AND_PRIOR_ART_REASSESSMENT.md` | 15,472 |
| `PROTOCOL_CONTRADICTION_MAP.csv` | 11,235 |
| `QC_RULE_RECONCILIATION.md` | 13,815 |
| `README.md` | 8,063 |
| `SPRINT_4L20_EXECUTIVE_DECISION.md` | 14,168 |
| `STAGE2_EARLY_WARNING_REQUIREMENTS_REASSESSMENT.md` | 10,639 |
| `UPDATED_CONTRADICTORY_EVIDENCE_REGISTER.csv` | 5,234 |
| `UPDATED_MISSING_EVIDENCE_REGISTER.csv` | 6,182 |
| `UPDATED_SOURCE_REGISTER.csv` | 11,732 |

---

## 3. Verification result

The register was re-read and every listed file was re-hashed:

```text
rows 18, mismatches 0
```

No registered file is missing. No registered file’s SHA-256 differs from the recorded value.

---

## 4. Exclusions

The following are intentionally excluded because they describe or authenticate the register:

- `EVIDENCE_SHA256_REGISTER.csv`
- `EVIDENCE_SHA256_REGISTER.csv.sha256`
- `INTEGRITY_VERIFICATION.md`

The sidecar contains the SHA-256 of the register.

---

## 5. Historical packages

Existing 4L.13, 4L.14, 4L.14 independent review, 4L.16, 4L.17, 4L.18, 4L.19, strategic reconstruction and strategic reconciliation/Müggelsee packages were read but not modified. Independent checks:

| Package | Rows | Mismatches |
|---|---:|---:|
| `sprint_4l13_independent_protocol_challenge` | 20 | 0 |
| `sprint_4l14_protocol_revision` | 18 | 0 |
| `sprint_4l14_codex_independent_review` | 19 | 0 |
| `sprint_4l16_human_review_preparation` | 10 | 0 |
| `sprint_4l17_human_review_continuation` | 7 | 0 |
| `sprint_4l18_human_review_and_qc_resolution` | 13 | 0 |
| `sprint_4l19_external_engagement_preparation` | 27 | 0 |
| `strategic_reconstruction_original_goal_2026_11_25` | 6 | 0 |
| `strategic_reconciliation_and_muggelsee_enquiry_2026_11_25` | 16 | 0 |

No historical package failed.

---

## 6. Verification commands

From the package directory:

```bash
cd /Users/cedricbw/Documents/EcoSentinel/research/evidence/sprint_4l20_protocol_reconciliation_and_viability_gate
shasum -a 256 -c EVIDENCE_SHA256_REGISTER.csv.sha256
```

Verify every registered file:

```bash
cd /Users/cedricbw/Documents/EcoSentinel
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
base = Path('research/evidence/sprint_4l20_protocol_reconciliation_and_viability_gate')
bad = 0
for row in csv.DictReader(open(base/'EVIDENCE_SHA256_REGISTER.csv', newline='', encoding='utf-8')):
    p = Path(row['path'])
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
        bad += 1
        print('MISMATCH', row['path'])
print('mismatches', bad)
PY
```

Historical packages:

```bash
cd /Users/cedricbw/Documents/EcoSentinel
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
for pkg in ['sprint_4l13_independent_protocol_challenge','sprint_4l14_protocol_revision','sprint_4l14_codex_independent_review','sprint_4l16_human_review_preparation','sprint_4l17_human_review_continuation','sprint_4l18_human_review_and_qc_resolution','sprint_4l19_external_engagement_preparation','strategic_reconstruction_original_goal_2026_11_25','strategic_reconciliation_and_muggelsee_enquiry_2026_11_25']:
    base = Path('research/evidence') / pkg
    reg = base / 'EVIDENCE_SHA256_REGISTER.csv'
    if not reg.exists():
        print(pkg, 'NO REGISTER'); continue
    bad = 0; n = 0
    for row in csv.DictReader(open(reg, newline='', encoding='utf-8')):
        p = Path(row['path']); n += 1
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
            bad += 1; print('MISMATCH', row['path'])
    print(pkg, 'rows', n, 'mismatches', bad)
PY
```

---

## 7. Limitations

- This verifies package integrity, not the truth of the underlying evidence.
- It does not authenticate reviewer identities, custodian statements, or external sources.
- It does not verify files outside this package.
- It does not resolve the protocol contradictions or the depth mismatch.
- No analysis or count audit was performed.

---

## 8. Status

**PASS.** The Sprint 4L.20 package is internally consistent and complete as listed in `README.md`.

**Governance remains unchanged:** protocol not approved; Gate 2 paused; all 15 decisions outstanding; D-15 not approved; analysis not authorised. No external contact was made in this sprint.
