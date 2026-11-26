# Integrity Verification — Sprint 4L.18

**Date:** 2026-11-25  
**Scope:** New Sprint 4L.18 package only.  
**Result:** **PASS — 13 registered files, 0 SHA-256 mismatches.**

---

## 1. Register

| Item | Value |
|---|---|
| Register | `EVIDENCE_SHA256_REGISTER.csv` |
| Sidecar | `EVIDENCE_SHA256_REGISTER.csv.sha256` |
| Algorithm | SHA-256 |
| Registered files | 13 |
| Register SHA-256 | `63ab03ea55b444a85c85508cdf6e740bb72b09f1e462222689583763ad6a30d2` |

---

## 2. Registered files

| File | Bytes |
|---|---:|
| `BUFFALO_POUND_CUSTODIAN_ENQUIRY.md` | 4,696 |
| `CONTRADICTORY_EVIDENCE_REGISTER.csv` | 2,416 |
| `CUSTODIAN_EVIDENCE_REQUIREMENTS.csv` | 3,457 |
| `D05_QC_EVIDENCE_RESOLUTION_REPORT.md` | 15,894 |
| `EXTERNAL_SEARCH_LOG.md` | 5,032 |
| `INDEPENDENT_REVIEWER_ENQUIRY_DRAFTS.md` | 5,190 |
| `MISSING_EVIDENCE_REGISTER.csv` | 3,338 |
| `README.md` | 3,505 |
| `SCIENTIFIC_REVIEWER_BRIEF.md` | 5,781 |
| `SPRINT_4L18_REPORT.md` | 9,514 |
| `STATISTICAL_REVIEWER_BRIEF.md` | 5,801 |
| `UPDATED_DECISION_STATUS_MATRIX.csv` | 4,753 |
| `UPDATED_SOURCE_REGISTER.csv` | 5,167 |

---

## 3. Verification result

The register was re-read and every listed file was re-hashed:

```text
rows 13, mismatches 0
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

Existing 4L.14, 4L.16, 4L.17, strategic reconstruction and Müggelsee packages were read but not modified. Independent checks:

- `sprint_4l16_human_review_preparation`: 10 rows, 0 mismatches.
- `sprint_4l17_human_review_continuation`: 7 rows, 0 mismatches.
- `strategic_reconciliation_and_muggelsee_enquiry_2026_11_25`: 16 rows, 0 mismatches.

---

## 6. Limitations

- This verifies package integrity, not the truth of the underlying evidence.
- It does not authenticate reviewer identities, custodian statements, or external sources.
- It does not verify files outside this package.
- No analysis or count audit was performed.

---

## 7. Status

**PASS.** The Sprint 4L.18 package is internally consistent and complete as listed in `README.md`.

**Governance remains unchanged:** protocol not approved; Gate 2 paused; all 15 decisions outstanding; D-15 not approved; analysis not authorised.
