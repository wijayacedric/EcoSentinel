# Review Dependency Order

**Sprint:** 4L.16  
**Status:** Planning document. No decision is approved.  
**Purpose:** Define a practical order for human review of D-01–D-15 without accidentally treating a recommendation as an approval.

---

## 1. Principles

1. **Decision IDs are fixed.** D-01–D-15 are preserved exactly; no merging, renaming, removal, or silent rewording.
2. **Recommendations are not approvals.** Every decision remains `OUTSTANDING — NOT APPROVED` until the named authority records it.
3. **Approval types are separate.** Scientific, statistical, data-custodian, Gate 2, licence/competition, D-13 and D-15 approvals are not interchangeable.
4. **No analysis is authorised.** The count-only audit is a separate authorisation and is not D-15.
5. **Premature decisions are not forced.** If the evidence is not available, record the decision as deferred, not approved “with conditions” that cannot be checked.
6. **The addendum must be reviewed first.** It is the current interpretation of 4L.14, but it is not approved.

---

## 2. Dependency map

| Decision | Depends on | Blocks |
|---|---|---|
| D-01 comparability | None | D-07, D-10, D-12 |
| D-02 Buffalo Pound endpoint | D-08; custodian evidence | D-05, D-06, D-09, D-15 |
| D-03 Mendota depth | None | D-12, D-15 |
| D-04 Turner/YSI | None | D-15 |
| D-05 QC | D-02 | D-06, D-09, D-15 |
| D-06 daily summary | D-05 | D-15 |
| D-07 temporal window | D-01 | D-12, D-15 |
| D-08 Buffalo Pound replicates | Custodian evidence | D-02, D-15 |
| D-09 2019-07-17 | D-05 framework | D-15 |
| D-10 uncertainty | D-01 | D-15 |
| D-11 small-n | Separate count-audit authorisation | D-15 |
| D-12 claims | D-01, D-03, D-07 | D-15 |
| D-13 originality | Addendum review; competition framing | D-14, D-15 |
| D-14 licence | D-13 | D-15 |
| D-15 analysis | D-01–D-14; addendum review; count-audit authorisation | Analysis start |

---

## 3. Recommended review phases

### Phase 0 — Verification only (no decisions)

- Confirm the 4L.14 package and 4L.16 package integrity.
- Confirm the 4L.16 addendum is the current review document.
- Confirm the Müggelsee email was sent and is not confused with the older unsent draft.
- Confirm governance status.
- Do not record any approval.

### Phase 1 — Foundational document review (can run in parallel)

| Order | Decision | Reviewer(s) | Why now |
|---:|---|---|---|
| 1 | **D-01** comparability | Scientific + statistical | Defines the statistic and the meaning of “comparability”; D-07/D-10/D-12 depend on it |
| 2 | **D-03** Mendota depth | Scientific + data custodian | Document-only framing; no new data needed |
| 3 | **D-04** Turner/YSI | Data custodian + statistical | Separation is clear from existing evidence |
| 4 | **D-07** temporal window | Scientific + statistical | Same-date framing follows from D-01 |
| 5 | **D-10** uncertainty | Statistical | Remove bootstrap; influence diagnostics only |
| 6 | **D-12** claims matrix | Scientific + Gate 2 | Must follow D-01/D-03/D-07 |

**Outcome:** These can be reviewed now. They do not require the missing custodian evidence, except that D-03’s station rule needs source semantics.

### Phase 2 — Project-owner direction

| Order | Decision | Reviewer(s) | Why |
|---:|---|---|---|
| 7 | **D-13** originality / proceed-pause | Project owner + scientific + Gate 2 | The project owner must decide whether a modest measurement audit is acceptable. This is the main student-owned decision. |

**Outcome:** D-13 can be considered after the Phase 1 documents are reviewed. It should be recorded with a rationale. It does not authorise analysis.

### Phase 3 — Custodian track

| Order | Decision | Reviewer(s) | Why |
|---:|---|---|---|
| 8 | **D-08** Buffalo Pound replicates | Data custodian | Must resolve duplicate/REP semantics before D-02 |
| 9 | **D-02** Buffalo Pound endpoint | Data custodian + scientific | Depends on D-08 and biomass provenance |
| 10 | **D-05** QC | Data custodian + statistical | Depends on D-02; needs instrument ranges/flags and B7/negative evidence |
| 11 | **D-06** daily summary | Scientific + statistical | Depends on D-05 and date-specific coverage |
| 12 | **D-09** 2019-07-17 | Data custodian + scientific | Handling can be reviewed after D-05 framework; cause is not required |

**Outcome:** These are conditional or premature until the data custodian provides documentation. Do not approve them on the basis of the current addendum alone.

### Phase 4 — Licence and competition review

| Order | Decision | Reviewer(s) | Why |
|---:|---|---|---|
| 13 | **D-14** licence/competition | Licence/competition reviewer | Requires the actual competition terms and CC BY-NC-SA review |

**Outcome:** D-14 can be reviewed once D-13 direction is clear. It does not approve D-15.

### Phase 5 — Count audit and final authorisation

| Order | Decision | Reviewer(s) | Why |
|---:|---|---|---|
| 14 | **D-11** small-n threshold | Statistical reviewer | Principle can be set now; numeric threshold requires the count audit |
| 15 | **D-15** analysis authorisation | All approvers | Only after D-01–D-14 are recorded, addendum re-reviewed, and count audit separately authorised |

**Outcome:** D-15 remains premature. The count-only audit is a separate authorisation and is not a correlation analysis.

---

## 4. What can run in parallel

- D-01, D-03, D-04, D-07, D-10 and D-12 can be reviewed in parallel because they are primarily document-level.
- D-08 can be requested from the data custodian immediately; it does not depend on other decisions.
- D-13 can be prepared in parallel but should be recorded after the addendum is reviewed.
- D-14 can be prepared in parallel but should be recorded after D-13 direction is clear.
- D-05, D-06 and D-09 must follow D-02/D-08.
- D-11’s threshold must follow the count audit.
- D-15 must follow everything.

---

## 5. Correct review order at a glance

1. Verify package and governance.
2. Review addendum.
3. D-01.
4. D-03.
5. D-04.
6. D-07.
7. D-10.
8. D-12.
9. D-13.
10. D-08 (custodian).
11. D-02 (custodian + scientific).
12. D-05 (custodian + statistical).
13. D-06 (scientific + statistical).
14. D-09 (custodian + scientific).
15. D-14 (licence).
16. D-11 threshold (after count audit).
17. D-15 (all approvers).

This is a logical order, not a requirement that every reviewer be available in that exact sequence.

---

## 6. Stop conditions

Stop and record a deferral if:

- the addendum has not been reviewed;
- a reviewer is asked to approve a decision outside their authority;
- the data custodian has not supplied the evidence needed for D-02/D-05/D-06/D-08/D-09;
- the count audit has not been separately authorised for D-11;
- the licence review is incomplete for D-14;
- anyone proposes to treat a recommendation or “conditional approval” as an approval;
- anyone proposes to start analysis before D-15.

**Governance remains unchanged: no decision is approved by this document.**
