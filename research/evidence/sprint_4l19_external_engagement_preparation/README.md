# Sprint 4L.19 — External Engagement Preparation

**Date:** 2026-11-25  
**Status:** Documentation and external-engagement preparation. **No decision approved. No analysis authorised. No external contact made in this sprint.**

---

## 1. What this package is

This package investigates the external evidence bottleneck that prevents EcoSentinel from progressing to an independently reviewable Stage 1 protocol. It covers:

- the provenance of the two Buffalo Pound datasets used by P3/P4;
- the identification and verification of the Buffalo Pound custodian route;
- independent scientific and statistical reviewer candidates;
- a structured independent review process;
- Stage 1 viability and originality;
- competition suitability;
- Müggelsee Stage 2 evidence;
- decision dependencies, missing evidence and contradictory evidence;
- source and search audit;
- integrity verification.

It does **not** contain analysis, a count audit, derived datasets, biological event labels, correlations or models.

---

## 2. Governance status

| Item | Status |
|---|---|
| Research direction | **CONTINUE — NARROWED RESEARCH QUESTION** |
| Protocol | **PROPOSED — NOT APPROVED** |
| Gate 2 | **PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY)** |
| D-01–D-15 | **OUTSTANDING — NOT APPROVED** |
| D-15 | **NOT APPROVED** |
| Analysis | **NOT AUTHORISED** |

These statuses were not changed by this sprint.

---

## 3. Key findings

1. **Buffalo Pound P3/P4 use two separate datasets**, not one: a 2014–2021 buoy dataset (FRDR, CC BY 4.0) and a 2018–2019 microscopy dataset (Borealis, CC BY-NC-SA 4.0).
2. **The custodian route is verified**: Helen Baulch (PI), Katy Nugent (operational/data), Kristin Painter (biological/corresponding author). No custody confirmation has been obtained.
3. **The essential custodian questions remain unresolved**: duplicate/`REP`, biomass derivation, B7 retention, negative/>100 RFU, coverage, time zone and sample times.
4. **B7 is a caution interval**, not a removal flag; the impacted period is the entire interval between maintenance visits.
5. **The current protocol’s QC section is inconsistent with the D-05 evidence** and must be formally revised before approval.
6. **Stage 1 remains conditionally viable only as a reduced, exploratory measurement audit**: P1/P2 core; P3/P4 conditional exploratory appendices; Mendota-only fallback; pause if conditions fail.
7. **Originality is low to moderate**: the core sensor–biomass association is established; the contribution is the pre-specified non-equivalence audit.
8. **Müggelsee is a Stage 2 candidate, not a qualified dataset**: long-term microscopy and sensors exist, but access, event definition, co-location, depth matching and calibration/QC are unresolved.
9. **Reviewer candidates are identified but not appointed**: Cayelan Carey (preferred scientific), Mark Scheuerell (preferred statistical).

---

## 4. File guide

### Main report and audit

- `SPRINT_4L19_REPORT.md` — full sprint report.
- `ADVERSARIAL_AUDIT.md` — ecologist, statistician and science-fair judge critiques.

### Buffalo Pound

- `BUFFALO_POUND_PROVENANCE_INVESTIGATION.md` — two-dataset provenance, biomass, duplicates, B7, RFU, coverage.
- `BUFFALO_POUND_FINAL_CUSTODIAN_EMAIL.md` — ready-to-send email, verified routing, not sent.
- `CUSTODIAN_CONTACT_VERIFICATION.csv` — roles, profiles, emails, verification status.
- `BUFFALO_POUND_UNRESOLVED_QUESTIONS.csv` — 14 structured questions.

### Scientific reviewers

- `SCIENTIFIC_REVIEWER_CANDIDATES.csv` — 7 candidates.
- `SCIENTIFIC_REVIEWER_CANDIDATE_ASSESSMENTS.md` — detailed assessments.
- `SCIENTIFIC_REVIEWER_FINAL_INVITATION.md` — invitation to Cayelan Carey, not sent.

### Statistical reviewers

- `STATISTICAL_REVIEWER_CANDIDATES.csv` — 6 candidates.
- `STATISTICAL_REVIEWER_CANDIDATE_ASSESSMENTS.md` — detailed assessments.
- `STATISTICAL_REVIEWER_FINAL_INVITATION.md` — invitation to Mark Scheuerell, not sent.

### Review framework

- `INDEPENDENT_REVIEW_PROTOCOL.md` — independence, process, outcomes, reserved decisions.
- `REVIEWER_EVIDENCE_PACKAGE_MANIFEST.csv` — what to send and what to exclude.
- `REVIEWER_CONFLICT_OF_INTEREST_CHECKLIST.md` — disclosure form.

### Stage 1

- `STAGE1_VIABILITY_REASSESSMENT.md` — outcomes A–D and recommendation.
- `STAGE1_ORIGINALITY_AND_PRIOR_ART_REVIEW.md` — direct prior art and originality rating.
- `STAGE1_COMPETITION_SUITABILITY_ASSESSMENT.md` — SciFest 2027 context and suitability.

### Stage 2

- `MUGGELSEE_STAGE2_EVIDENCE_REASSESSMENT.md` — FRED 867/1/1145 evidence.
- `STAGE2_DATASET_QUALIFICATION_CHECKLIST.md` — mandatory and early-warning requirements.

### Decision management

- `EXTERNAL_RESPONSE_DECISION_TREE.md` — how to respond to custodian/reviewer/licence outcomes.
- `UPDATED_DECISION_DEPENDENCY_MATRIX.csv` — D-01–D-15 status and dependencies.
- `UPDATED_MISSING_EVIDENCE_REGISTER.csv` — 23 evidence gaps.
- `CONTRADICTORY_EVIDENCE_REGISTER.csv` — 16 contradictions/disagreements.

### Research audit

- `UPDATED_SOURCE_REGISTER.csv` — 57 sources with evidence grades.
- `EXTERNAL_SEARCH_LOG.md` — queries, sources, inaccessible material, stop rules.

### Integrity

- `EVIDENCE_SHA256_REGISTER.csv` — hashes of every content file.
- `EVIDENCE_SHA256_REGISTER.csv.sha256` — detached checksum of the register.
- `INTEGRITY_VERIFICATION.md` — verification result and historical checks.

---

## 5. What is complete

- Buffalo Pound dataset identity, authors, licences, sensor models, B7 semantics, calibration practice and arithmetic form.
- Custodian roles and verified professional contact routes.
- 7 scientific and 6 statistical reviewer candidates with assessments.
- Independent review protocol, manifest and conflict checklist.
- Stage 1 viability, originality and competition assessments.
- Stage 2 Müggelsee reassessment and qualification checklist.
- Decision dependency, missing evidence and contradiction registers.
- Source register and search log.
- Integrity register and verification.

## 6. What is not complete

- Custodian answers.
- Reviewer appointments or reports.
- Written licence/competition review.
- Protocol revision.
- Count audit.
- D-01–D-14 approvals.
- D-15 approval.
- Any analysis.
- Stage 2 access/permission.
- Competition eligibility/venue confirmation.

---

## 7. How to verify integrity

From this directory:

```bash
cd /Users/cedricbw/Documents/EcoSentinel/research/evidence/sprint_4l19_external_engagement_preparation
shasum -a 256 -c EVIDENCE_SHA256_REGISTER.csv.sha256
```

Then verify every registered file:

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

Integrity verifies file identity, not scientific truth.

---

## 8. What was not done

- No analysis, count audit, correlation, p-value, confidence interval, model, label, event interval, derived dataset or threshold optimisation.
- No data acquisition or upload.
- No emails, reviewer invitations, custodian contact or Gmail drafts were sent in this sprint. (The earlier Müggelsee enquiry remains the only external message recorded in the project.)
- No commits or pushes.
- No modification of historical protocols, registers or evidence packages.

---

## 9. Next action

**Obtain human authorisation to send the Buffalo Pound custodian enquiry to Professor Helen Baulch, copied to Katy Nugent and Dr Kristin Painter.**

Do not analyse while waiting. Do not finalise D-05/D-06. Do not approve D-15.
