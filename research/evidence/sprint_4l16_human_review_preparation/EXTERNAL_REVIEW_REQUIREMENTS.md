# External Review Requirements

**Sprint:** 4L.16  
**Status:** Requirements definition. No reviewer has been appointed or has responded.  
**Purpose:** Specify who must review what, what evidence they need, and what counts as a valid approval.

---

## 1. Reviewer roles

| Role | Required competence | Decisions in scope | What they must inspect | Independence requirement | Valid output |
|---|---|---|---|---|---|
| **Independent scientific reviewer** | Freshwater ecology, phytoplankton/microscopy, sensor ecology, or equivalent | D-01, D-02, D-03, D-06, D-07, D-09, D-12, D-13 concurrence | Protocol, addendum, research question, endpoints, claims, prior art | Not the student, not a co-author of the data, no undisclosed conflict | Written decision with rationale, name, date, scope |
| **Independent statistical reviewer** | Applied statistics/time series, rank methods, dependence, uncertainty | D-01, D-04, D-05, D-06, D-07, D-10, D-11, D-12 | Statistical specification, addendum, QC plan, uncertainty plan, n rule | Not the student, no involvement in producing the expected result | Written decision with rationale, name, date, scope |
| **Data custodian** | Familiar with the Buffalo Pound/Painter data and/or Mendota NTL data documentation | D-02, D-03, D-04, D-05, D-06, D-08, D-09 | Source data dictionaries, methods, replicate structure, flags, biomass field, coverage | Can be the data provider; must have authority to explain the data | Written data-provenance statement and decision |
| **Licence/competition reviewer** | Copyright/licensing and competition rules | D-14 | CC BY-NC-SA 4.0 terms, data provenance, SciFest rules, intended display/report | Not the student; can be a teacher/mentor with documented competence, but legal advice is not implied | Written licence/competition assessment |
| **Gate 2 governance authority** | Project governance, Option C scope | D-12, D-13 concurrence, D-15 | Protocol, addendum, decision register, claims matrix | As defined by the project’s governance | Recorded Gate 2 decision |
| **Project owner/student** | Owns the project and competition goals | D-13 (with scientific/Gate 2 concurrence) | Whole package | Is the student | Written rationale and choice |

---

## 2. Current appointment status

| Role | Status |
|---|---|
| Project owner/student | **Known** — Cedric Wijaya |
| Independent scientific reviewer | **Not identified in the repository** |
| Independent statistical reviewer | **Not identified in the repository** |
| Data custodian — Buffalo Pound | **Not formally appointed**; Painter/Baulch data providers are potential contacts, but no permission or response is documented |
| Data custodian — Mendota | **NTL-LTER is the data provider**; no formal reviewer appointment is documented |
| Licence/competition reviewer | **Not identified** |
| Gate 2 governance authority | **Not identified in the current package** |

**This is a material gap.** The project cannot record independent approvals until the reviewers are named and confirm their scope.

---

## 3. What each reviewer should receive

### Scientific reviewer

- `SPRINT_4L14_REVIEW_ADDENDUM.md`
- 4L.14 `REVISED_PROTOCOL.md`
- 4L.14 `UPDATED_HUMAN_DECISION_REGISTER.md`
- 4L.14 independent review findings F-01–F-13
- 4L.14 `TWO_CASE_STUDY_DESIGN.md`
- 4L.14 `BIOLOGICAL_ENDPOINT_AND_BIOMASS_REVIEW.md`
- 4L.16 `DECISION_REVIEW_MATRIX.csv`
- This requirements document

### Statistical reviewer

- 4L.14 `REVISED_PROTOCOL.md` §11–§13
- 4L.14 `UNCERTAINTY_AND_SENSITIVITY_PLAN.md`
- 4L.14 `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md`
- 4L.14 independent statistical review
- 4L.16 addendum F-01/F-05/F-08/F-11
- `DECISION_REVIEW_MATRIX.csv`

### Data custodian

- Data dictionaries and source files relevant to the specific decision
- 4L.14 `QC_AND_MISSINGNESS_RULES.md`
- 4L.14 `BIOLOGICAL_ENDPOINT_AND_BIOMASS_REVIEW.md`
- 4L.14 `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md`
- 4L.14 independent QC/estimand findings
- A precise list of the questions in D-02/D-05/D-06/D-08/D-09

### Licence/competition reviewer

- Painter data licence (CC BY-NC-SA 4.0)
- Official Creative Commons terms
- SciFest 2027 rules and entry requirements
- Intended report/display plan
- `DECISION_REVIEW_MATRIX.csv` D-14

### Gate 2 governance

- Protocol and addendum
- Decision register
- Claims matrix
- This package
- Evidence of reviewer appointments

---

## 4. Independence and conflicts

A reviewer is not independent if they:

- are the student or a family member;
- co-authored the dataset or the paper whose endpoint is being assessed;
- have a direct interest in a particular result;
- have not disclosed a relevant conflict.

A data custodian is allowed to be the data provider; that is not a conflict for provenance questions, but they cannot substitute for an independent scientific or statistical reviewer.

**No reviewer response has been received.** No approval should be recorded until a named person confirms their role and scope in writing.

---

## 5. What counts as a valid approval

A valid approval record should include:

- decision ID;
- reviewer name and role;
- date;
- documents/evidence considered;
- explicit decision (approve / reject / defer / approve with specified changes);
- rationale;
- any conditions;
- signature or verifiable written confirmation.

Email “looks fine” is not a sufficient record for D-15 or D-14.

---

## 6. What does not count

- A recommendation in the 4L.14 register.
- A student’s own agreement.
- An AI review.
- A reviewer commenting on one section without the full package.
- A data custodian explaining one field but not the decision.
- A licence reviewer saying “probably fine” without checking the competition terms.
- A “conditional approval” that depends on evidence nobody has obtained.

---

## 7. Suggested sequence and timing

| Step | Action | Owner | Target |
|---|---|---|---|
| 1 | Confirm package integrity and governance | Project owner/OpenCode | Now |
| 2 | Appoint scientific reviewer | Project owner | Before review |
| 3 | Appoint statistical reviewer | Project owner | Before review |
| 4 | Request custodian clarification | Project owner | Before D-02/D-05/D-06/D-08/D-09 |
| 5 | Appoint licence/competition reviewer | Project owner | Before D-14 |
| 6 | Review Phase 1 decisions | Scientific/statistical | December 2026 |
| 7 | Record D-13 direction | Project owner + reviewers | December 2026 |
| 8 | Custodian track | Data custodian | January 2027 |
| 9 | Count audit (separate authorisation) | Statistical/OpenCode | After D-01–D-14 |
| 10 | D-15 decision | All approvers | After everything |

These dates are planning suggestions, not governance deadlines.

---

## 8. Missing documentation that prevents informed review

- No named independent scientific reviewer.
- No named independent statistical reviewer.
- No written data-custodian statement on Buffalo Pound duplicates/biomass/coverage.
- No written NTL-LTER statement on Mendota station/depth semantics.
- No licence/competition review.
- No count-audit authorisation or result.
- No reviewer appointment/conflict declarations.

Until these are supplied, the relevant decisions are **not ready for approval**, even if the documents are complete.
