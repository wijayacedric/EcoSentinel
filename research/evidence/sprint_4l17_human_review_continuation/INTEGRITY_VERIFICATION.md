# Integrity Verification — Sprint 4L.17

**Date:** 2026-11-25  
**Scope:** New Sprint 4L.17 package only.  
**Result:** **PASS — 7 registered files, 0 SHA-256 mismatches.**

---

## 1. Register

| Item | Value |
|---|---|
| Register | `EVIDENCE_SHA256_REGISTER.csv` |
| Sidecar | `EVIDENCE_SHA256_REGISTER.csv.sha256` |
| Algorithm | SHA-256 |
| Registered files | 7 |
| Register SHA-256 | `14a273c6e624568be3311dc622934e913f8b4a3c1bf548ca566553d160405025` |

---

## 2. Registered files

| File | Bytes |
|---|---:|
| `D06_EVIDENCE_ASSESSMENT.md` | 9,060 |
| `DECISION_STATUS_MATRIX.csv` | 4,794 |
| `EXTERNAL_SEARCH_LOG.md` | 4,231 |
| `README.md` | 2,925 |
| `REMAINING_DECISIONS_REGISTER.md` | 8,680 |
| `SPRINT_4L17_CONTINUATION_REPORT.md` | 9,277 |
| `UPDATED_SOURCE_REGISTER.csv` | 4,988 |

---

## 3. Verification result

The register was re-read and every listed file was re-hashed:

```text
rows 7, mismatches 0
```

No registered file is missing. No registered file’s SHA-256 differs from the recorded value.

---

## 4. Exclusions

The following are intentionally excluded from the register because they describe or authenticate the register:

- `EVIDENCE_SHA256_REGISTER.csv`
- `EVIDENCE_SHA256_REGISTER.csv.sha256`
- `INTEGRITY_VERIFICATION.md`

The sidecar contains the SHA-256 of the register. This report records that hash.

---

## 5. Historical packages

The 4L.14, 4L.16, strategic reconstruction and Müggelsee reconciliation packages were read but not modified. Their own integrity records remain authoritative.

Independent checks of the existing registers:

- `sprint_4l16_human_review_preparation`: 10 rows, 0 mismatches.
- `strategic_reconciliation_and_muggelsee_enquiry_2026_11_25`: 16 rows, 0 mismatches.

---

## 6. Limitations

- This verifies package integrity, not the truth or completeness of the underlying evidence.
- It does not authenticate reviewer identities, custodian statements, or external sources.
- It does not verify files outside this package.
- No analysis or count audit was performed.

---

## 7. Status

**PASS.** The Sprint 4L.17 package is internally consistent and complete as listed in `README.md`.

**Governance remains unchanged:** protocol not approved; Gate 2 paused; all 15 decisions outstanding; D-15 not approved; analysis not authorised.
