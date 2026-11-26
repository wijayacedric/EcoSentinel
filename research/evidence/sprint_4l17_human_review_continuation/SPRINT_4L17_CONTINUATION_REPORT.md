# Sprint 4L.17 Continuation Report

**Sprint:** 4L.17 — Human Review Continuation and Remaining Decisions  
**Date:** 2026-11-25  
**Status:** Documentation and decision-support package. **No decision approved. No analysis authorised.**  
**Governance:** Protocol **PROPOSED — NOT APPROVED**; Gate 2 **PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY)**; all 15 decisions **OUTSTANDING**; D-15 **NOT APPROVED**; analysis **NOT AUTHORISED**.

---

## 1. Work completed

- Read `AGENTS.md` in full.
- Inspected the Git working tree and the current repository state.
- Read the complete Sprint 4L.16 human-review package.
- Read the strategic reconstruction and Müggelsee reconciliation packages.
- Read the 4L.14 protocol, its review addendum, the 4L.13/4L.14 reviews, and the relevant Mendota/Buffalo Pound evidence.
- Completed a focused D-06 evidence assessment.
- Reviewed the remaining decisions in dependency order: D-09, D-11, D-14, D-15.
- Verified the CC BY-NC-SA 4.0 legal code and SciFest 2027 rules/terms from official sources.
- Prepared a new decision-status matrix and updated source register.
- Created this package and its integrity records.

**No analysis, count audit, labels, event intervals, derived datasets, models, emails, contacts, data acquisition, commits or pushes were performed.**

---

## 2. D-06 — Primary daily summary

### 2.1 Options

| Option | Summary |
|---|---|
| **A** | Full-day mean for both lakes |
| **B** | Nighttime summary for Buffalo Pound only |
| **C** | Daytime summary for both lakes |

### 2.2 Evidence assessment

**Mendota**

- Daily values are provider daily means of 1-minute data.
- The daily file does not provide within-day observation counts or a documented within-day completeness measure.
- Biology has dates, not sampling times.
- Turner chlorophyll has 128 same-day unflagged dates; Turner phycocyanin 139; YSI chlorophyll 21; YSI phycocyanin 22.
- Sensors are at 0.5 m; biology is generally a 0–8 m composite.
- Diel quenching and sample-time uncertainty cannot be removed.

**Buffalo Pound**

- Sensors are 10-minute records; 2018 daily counts are 121–144; 2019 are 42–131.
- The fixed “≥72 of 144 and both halves” coverage rule has been withdrawn because 144 is not a documented date-specific expectation.
- B7 fouling, negative/above-range RFU, and calibration issues remain unresolved.
- Day/night medians are computable in principle but only where coverage and time zone are documented.
- The two seasons are not equivalent to Mendota’s multi-year record.

**Cross-lake**

- The same label “daily mean” does not mean the same exposure, precision, or biological support.
- Mendota’s mean is provider-defined with unknown within-day counts; Buffalo Pound’s is computed from variable 10-minute coverage.
- Neither represents the exact biological sample time or the same water parcel.

### 2.3 Option assessment

| Option | Assessment |
|---|---|
| **A** | Best available common descriptive statistic; supported only with explicit non-equivalence wording |
| **B** | Not comparable to Mendota; no evidence that nighttime is more representative; at most a sensitivity |
| **C** | Cannot be reconstructed for Mendota without within-day data; not implementable for both lakes |

### 2.4 Recommendation

**Provisional project-owner preference: Option A.**

Retain full-day means for both lakes as the proposed primary daily summaries, with Buffalo Pound daytime/nighttime medians as sensitivity summaries only, and explicit wording that the summaries:

- are not equivalent exposures;
- do not represent the exact biological sample time or same water parcel;
- do not remove diel variation or quenching;
- do not imply biological equivalence.

**D-06 remains OUTSTANDING — NOT APPROVED.**

**Required before finalisation:**

- D-05 resolution;
- Buffalo Pound date-specific coverage/time-zone documentation;
- Mendota within-day coverage if available;
- independent scientific reviewer sign-off;
- independent statistical reviewer sign-off.

**If evidence fails:** do not switch to Option B or C to rescue the design. Restrict Buffalo Pound to adequately covered dates; retain Mendota only as a descriptive provider mean; report points/n and exclude the affected estimand if representativeness fails.

Full assessment: `D06_EVIDENCE_ASSESSMENT.md`.

---

## 3. Remaining decisions

### D-09 — 2019-07-17 anomaly

**Status:** **OUTSTANDING — NOT APPROVED.**  
**Dependency:** D-05 remains unresolved.

**Can be documented now:**

- provisional handling: retain and flag; exclusion sensitivity only if analysis is later authorised; no correction; no bloom/non-bloom interpretation;
- no influence/delta-rho calculation before D-15.

**Blocked:**

- final D-09 decision until D-05 is resolved;
- any influence calculation, rank extremeness, or leave-one-date-out result.

**Required:** data custodian + scientific reviewer acceptance of the handling plan; D-05 resolution; D-15 before any calculation.

### D-11 — Small-sample reporting

**Status:** **OUTSTANDING — NOT APPROVED.**

**Can be reviewed now:** the principle — no stratum rho if n < 10; show points; no pooling; no post-hoc minimum; overall minimum set before estimation.

**Blocked:** the numeric overall minimum until a separately authorised count-only audit is completed. No count audit was performed.

**Required:** independent statistical reviewer; separate count-audit authorisation; count-audit result.

### D-14 — Licence and competition compliance

**Status:** **OUTSTANDING — NOT APPROVED.**

**Verified:**

- Painter data are CC BY-NC-SA 4.0.
- The legal code requires attribution, non-commercial use, and share-alike for Adapted Material; “Share” includes public display/dissemination.
- SciFest requires a report book and visual display; project content may be used by SciFest for exhibition/publication.
- A student science-fair project is not automatically exempt from the licence.

**Not resolved:** whether the intended competition display/report is compliant; whether share-alike extends to the whole report or only adapted figures/tables; whether permission is needed. This requires a written licence/competition review, not a legal conclusion by this package.

**Options:** (a) use under CC BY-NC-SA with an attribution/share-alike plan; (b) exclude Painter data; (c) seek written permission.

**D-14 remains unapproved.**

### D-15 — Final analysis authorisation

**Status:** **NOT APPROVED.**

Prerequisites:

1. D-01–D-14 formally recorded by their authorities.
2. Custodian clarifications obtained or affected analyses excluded.
3. Licence/competition compliance resolved.
4. Count-only audit separately authorised and completed.
5. Independent scientific and statistical reviews completed.
6. Protocol and addendum reconciled.
7. Explicit human approval of D-15.

**No analysis was initiated.**

Full detail: `REMAINING_DECISIONS_REGISTER.md`.

---

## 4. Project-owner preferences vs formal approvals

| Item | Project-owner preference | Formal status |
|---|---|---|
| D-06 | **Option A, provisional** — full-day means for both; BP day/night sensitivity; non-equivalence wording | **NOT APPROVED** |
| D-13 | Prior assessment suggests conditional proceed as a modest audit, but no formal owner decision is recorded in this sprint | **NOT APPROVED** |
| D-09 | Provisional retain/flag handling | **NOT APPROVED** |
| D-11 | Principle supported; numeric threshold not set | **NOT APPROVED** |
| D-14 | Options remain open | **NOT APPROVED** |
| D-15 | No preference; do not approve | **NOT APPROVED** |

A project-owner preference is not a scientific, statistical, data-custodian, licence, or governance approval.

---

## 5. Dependencies and blockers

| Decision | Dependency | Blocker |
|---|---|---|
| D-06 | D-05; BP coverage; Mendota within-day caveat | Custodian + scientific/statistical review |
| D-09 | D-05 | No influence calculation before D-15 |
| D-11 threshold | Separate count audit | Not authorised |
| D-14 | D-13 direction; competition terms | No written licence review |
| D-15 | D-01–D-14; count audit; reviews | Premature |

**No new dataset or reviewer response changes these dependencies.**

---

## 6. New evidence and Option C

**New evidence:** official CC BY-NC-SA legal code; official SciFest 2027 rules/terms; D-06 sensor evidence.  
**Effect on Option C:** none. Müggelsee remains sent but unanswered; no Stage 2 dataset is available; Stage 1 remains the current project.

---

## 7. Verification

- All required 4L.17 deliverables created.
- `DECISION_STATUS_MATRIX.csv` has D-01–D-15 (15 rows).
- `UPDATED_SOURCE_REGISTER.csv` has 20 entries.
- SHA-256 register and sidecar generated; independent re-hash returned 0 mismatches.
- Historical packages were read but not modified.
- No analysis, count audit, labels, derived datasets, models, emails, contacts, commits or pushes.

See `INTEGRITY_VERIFICATION.md`.

---

## 8. Governance statement

**Research direction: CONTINUE — NARROWED RESEARCH QUESTION.**

**Protocol: PROPOSED — NOT APPROVED.**

**Gate 2: PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY).**

**All 15 human decisions: OUTSTANDING — NOT APPROVED.**

**D-15: NOT APPROVED.**

**Analysis: NOT AUTHORISED.**
