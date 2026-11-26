# Integrity Verification — Sprint 4L.19

**Date:** 2026-11-25  
**Scope:** New Sprint 4L.19 package only.  
**Result:** **PASS — 27 registered files, 0 SHA-256 mismatches.**

---

## 1. Register

| Item | Value |
|---|---|
| Register | `EVIDENCE_SHA256_REGISTER.csv` |
| Sidecar | `EVIDENCE_SHA256_REGISTER.csv.sha256` |
| Algorithm | SHA-256 |
| Registered files | 27 |
| Register SHA-256 | `42fdd5ca1efb71bc8c2f96f67a7eea56651c79dd868eb38e45ac743324b425d5` |

---

## 2. Registered files

| File | Bytes |
|---|---:|
| `ADVERSARIAL_AUDIT.md` | 17,687 |
| `BUFFALO_POUND_FINAL_CUSTODIAN_EMAIL.md` | 8,398 |
| `BUFFALO_POUND_PROVENANCE_INVESTIGATION.md` | 25,183 |
| `BUFFALO_POUND_UNRESOLVED_QUESTIONS.csv` | 6,672 |
| `CONTRADICTORY_EVIDENCE_REGISTER.csv` | 5,665 |
| `CUSTODIAN_CONTACT_VERIFICATION.csv` | 3,098 |
| `EXTERNAL_RESPONSE_DECISION_TREE.md` | 10,769 |
| `EXTERNAL_SEARCH_LOG.md` | 13,446 |
| `INDEPENDENT_REVIEW_PROTOCOL.md` | 11,473 |
| `MUGGELSEE_STAGE2_EVIDENCE_REASSESSMENT.md` | 12,449 |
| `README.md` | 7,940 |
| `REVIEWER_CONFLICT_OF_INTEREST_CHECKLIST.md` | 5,351 |
| `REVIEWER_EVIDENCE_PACKAGE_MANIFEST.csv` | 5,698 |
| `SCIENTIFIC_REVIEWER_CANDIDATES.csv` | 4,983 |
| `SCIENTIFIC_REVIEWER_CANDIDATE_ASSESSMENTS.md` | 14,251 |
| `SCIENTIFIC_REVIEWER_FINAL_INVITATION.md` | 6,809 |
| `SPRINT_4L19_REPORT.md` | 26,909 |
| `STAGE1_COMPETITION_SUITABILITY_ASSESSMENT.md` | 12,297 |
| `STAGE1_ORIGINALITY_AND_PRIOR_ART_REVIEW.md` | 12,997 |
| `STAGE1_VIABILITY_REASSESSMENT.md` | 16,896 |
| `STAGE2_DATASET_QUALIFICATION_CHECKLIST.md` | 12,954 |
| `STATISTICAL_REVIEWER_CANDIDATES.csv` | 4,457 |
| `STATISTICAL_REVIEWER_CANDIDATE_ASSESSMENTS.md` | 13,097 |
| `STATISTICAL_REVIEWER_FINAL_INVITATION.md` | 7,128 |
| `UPDATED_DECISION_DEPENDENCY_MATRIX.csv` | 7,141 |
| `UPDATED_MISSING_EVIDENCE_REGISTER.csv` | 6,531 |
| `UPDATED_SOURCE_REGISTER.csv` | 13,623 |

---

## 3. Verification result

The register was re-read and every listed file was re-hashed:

```text
rows 27, mismatches 0
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

Existing 4L.14, 4L.16, 4L.17, 4L.18, strategic reconstruction and strategic reconciliation/Müggelsee packages were read but not modified. Independent checks:

| Package | Rows | Mismatches |
|---|---:|---:|
| `sprint_4l14_protocol_revision` | 18 | 0 |
| `sprint_4l16_human_review_preparation` | 10 | 0 |
| `sprint_4l17_human_review_continuation` | 7 | 0 |
| `sprint_4l18_human_review_and_qc_resolution` | 13 | 0 |
| `strategic_reconstruction_original_goal_2026_11_25` | 6 | 0 |
| `strategic_reconciliation_and_muggelsee_enquiry_2026_11_25` | 16 | 0 |

No historical package failed.

---

## 6. Verification commands

From the package directory:

```bash
cd /Users/cedricbw/Documents/EcoSentinel/research/evidence/sprint_4l19_external_engagement_preparation
shasum -a 256 -c EVIDENCE_SHA256_REGISTER.csv.sha256
```

Verify every registered file:

```bash
cd /Users/cedricbw/Documents/EcoSentinel
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
base = Path('research/evidence/sprint_4l19_external_engagement_preparation')
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
for pkg in ['sprint_4l14_protocol_revision','sprint_4l16_human_review_preparation','sprint_4l17_human_review_continuation','sprint_4l18_human_review_and_qc_resolution','strategic_reconstruction_original_goal_2026_11_25','strategic_reconciliation_and_muggelsee_enquiry_2026_11_25']:
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
- It does not resolve the FRDR version ambiguity.
- No analysis or count audit was performed.

---

## 8. Status

**PASS.** The Sprint 4L.19 package is internally consistent and complete as listed in `README.md`.

**Governance remains unchanged:** protocol not approved; Gate 2 paused; all 15 decisions outstanding; D-15 not approved; analysis not authorised. No external contact was made in this sprint.
