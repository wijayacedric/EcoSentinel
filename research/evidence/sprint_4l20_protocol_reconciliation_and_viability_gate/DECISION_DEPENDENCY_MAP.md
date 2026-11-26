# Decision Dependency Map

**Sprint:** 4L.20  
**Date:** 2026-11-26  
**Purpose:** Show what depends on what after the proposed reduction to Mendota-only.  
**Status:** Map only. **No decision approved. D-15 NOT APPROVED.**

---

## 1. Current governance

| Item | Status |
|---|---|
| Research direction | **CONTINUE — NARROWED RESEARCH QUESTION** |
| Protocol | **PROPOSED — NOT APPROVED** |
| Gate 2 | **PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY)** |
| D-01–D-14 | **OUTSTANDING — NOT APPROVED** |
| D-15 | **NOT APPROVED** |
| Analysis | **NOT AUTHORISED** |

The 4L.20 recommendation does not change these statuses. It proposes a scope reduction for human decision.

---

## 2. Dependency graph

```text
D-13 scope decision (Mendota-only vs pause)
   │
   ├── if pause ──► record pause; set resumption gates; no analysis
   │
   └── if Mendota-only
         │
         ├── Protocol revision v2
         │      ├── remove Buffalo Pound
         │      ├── P2 primary / P1 secondary
         │      ├── Turner-only
         │      ├── QC reconciliation (H, negative, C/E/O, station)
         │      ├── detection-conditioned population
         │      ├── claims matrix
         │      └── sensitivity set
         │
         ├── D-01 comparability definition
         ├── D-03 depth comparator
         ├── D-05 Mendota QC
         ├── D-06 Mendota daily summary
         ├── D-07 same-date matching
         ├── D-10 uncertainty/influence
         ├── D-11 small-n rule
         ├── D-12 claims
         ├── D-14 licence/competition
         │
         ├── Independent scientific review
         ├── Independent statistical review
         │
         ├── Count-only audit (separate authorisation)
         │      └── actual n / minimum n
         │
         ├── D-15 approval
         │
         └── Analysis (only after D-15)
```

---

## 3. Decision-by-decision map

| Decision | Topic | Current status | Depends on | What it unlocks | Stage 1 after reduction |
|---|---|---|---|---|---|
| **D-01** | Operational definition of comparability | Outstanding | Scientific/statistical review | Defines what “comparability” means | **Core**; revise to surface-vs-composite rank audit |
| **D-02** | Buffalo Pound endpoint | Outstanding | Custodian + scientific review | P3/P4 endpoint | **Re-scoped out of Stage 1**; future/Stage 2 |
| **D-03** | Mendota depth comparator | Outstanding | Scientific review | Accepts/rejects surface-vs-composite framing | **Core**; critical |
| **D-04** | Turner/YSI handling | Outstanding | Data custodian/statistical review | Era separation | **Simplified**: Turner-only; YSI removed |
| **D-05** | Primary QC rule | Outstanding | Custodian + statistical review | Analysis population | **Core**; Mendota-only QC reconciliation |
| **D-06** | Primary daily summary | Outstanding | D-05 + reviewers | Daily mean definition | **Simplified**: Mendota provider mean only |
| **D-07** | Temporal window | Outstanding | Reviewers | Same-date matching | **Simplified**: same-date only; ±1 removed |
| **D-08** | Buffalo Pound replicate handling | Outstanding | Custodian | P3/P4 totals | **Re-scoped out of Stage 1**; future/Stage 2 |
| **D-09** | 2019-07-17 anomaly | Outstanding | D-05 + reviewers | Buffalo Pound anomaly | **Re-scoped out of Stage 1**; future/Stage 2 |
| **D-10** | Uncertainty method | Outstanding | Statistical review | Influence diagnostics | **Core**; leave-one-year-out only |
| **D-11** | Small-n reporting | Outstanding | Count audit + statistical review | Minimum n/strata | **Core**; reviewer sets after count audit |
| **D-12** | Claims matrix | Outstanding | Scientific/Gate 2 | Permitted claims | **Core**; Mendota-only wording |
| **D-13** | Originality sufficiency | Outstanding | Owner + scientific/Gate 2 | Proceed/pause | **Gate**: accept modest audit or pause |
| **D-14** | Licence/competition compliance | Outstanding | Licence reviewer | Public display/use | **Simplified**: Mendota CC BY 4.0; still review |
| **D-15** | Approval to begin analysis | Outstanding | D-01–D-14 + count audit + reviews | Analysis | **Final gate**; not approved |

---

## 4. External dependencies

| Dependency | Who | What is needed | Effect if unavailable |
|---|---|---|---|
| NTL-LTER H-range clarification | NTL-LTER provider | Numeric H range or guidance | Reviewer decides H treatment; both reported |
| Instrument negative-RFU clarification | Turner/YSI or NTL-LTER | Meaning of negative pigment RFU | Reviewer decides; exclude primary with sensitivity |
| Mendota station semantics | NTL-LTER | Station/deep-hole documentation | All dates + station sensitivity; limitation |
| Independent scientific reviewer | External | Written opinion on depth mismatch/endpoints | No D-15 |
| Independent statistical reviewer | External | Written opinion on rho/dependence/QC | No D-15 |
| Licence/competition reviewer | External | Written review of CC BY 4.0 use/display | No public display; D-14 unresolved |
| Count-audit authorisation | Governance | Separate approval | Actual n unknown; no analysis |
| Student contribution statement | Project owner | What the student did | Competition eligibility risk |
| Buffalo Pound custodian | External | Full D-02/D-08/D-05 answers | Buffalo Pound stays out of Stage 1 |
| Müggelsee/IGB | External | Access, event definition, calibration/QC | Stage 2 not qualified |

---

## 5. What depends on what

### 5.1 If D-13 = Mendota-only

Then:

- D-02, D-08, D-09 are re-scoped out of Stage 1.
- D-04 simplifies to Turner-only.
- D-05 becomes Mendota-only QC.
- D-06 becomes Mendota provider mean.
- D-07 becomes same-date only.
- D-14 becomes Mendota CC BY 4.0.
- The protocol must be revised before review.
- No analysis until D-15.

### 5.2 If D-13 = pause

Then:

- No protocol revision is required for analysis.
- D-02/D-08/D-09 remain future issues.
- D-15 remains not approved.
- Resumption requires a qualified Stage 2 dataset or a stronger question.
- No analysis, no count audit, no contact.

### 5.3 If D-13 is left open

Then nothing else can proceed. The project remains in documentation limbo. This is the least defensible state.

---

## 6. Gates

| Gate | Required | Who decides | Unlocks |
|---|---|---|---|
| **G0 — Scope** | D-13: Mendota-only or pause | Project owner + scientific/Gate 2 | Protocol revision or pause |
| **G1 — Protocol v2** | Revised protocol with QC/claims/hierarchy | Project owner | Independent review |
| **G2 — Scientific review** | Written report + disclosure | Project owner | D-03/D-12/D-13 input |
| **G3 — Statistical review** | Written report + disclosure | Project owner | D-05/D-10/D-11 input |
| **G4 — Licence** | Written review/permission | Licence reviewer | Public display/use |
| **G5 — Count audit** | Actual n, exclusions | Project owner + statistical reviewer | Minimum n/estimability |
| **G6 — D-15** | All prior gates recorded | All approvers | Analysis |

No gate may be skipped. A positive review is not D-15 approval. A count audit is not analysis authorisation.

---

## 7. Critical path

The shortest defensible path to a completed Mendota-only project:

1. **D-13 scope decision** (owner).
2. **Protocol v2** (Mendota-only, P2/P1, QC reconciliation, claims).
3. **Scientific + statistical reviews** (external).
4. **Licence/competition review** (external).
5. **Count audit** (separate authorisation).
6. **D-01–D-14 decisions** (governance).
7. **D-15 approval** (governance).
8. **Analysis, figures, report/display.**

The longest lead items are the external reviews and the count audit. If reviews are not secured by mid-January 2027, the competition timeline is at risk.

---

## 8. What does not depend on anything else

- The decision to remove Buffalo Pound from Stage 1 is a scope decision; it does not require custodian input.
- The decision to use Turner-only is supported by the n and instrument evidence.
- The decision to use P2 primary/P1 secondary is supported by pigment biology and multiplicity control.
- The decision to keep D-15 unapproved is fixed.

---

## 9. Verdict

**The project is blocked at D-13.** Until the project owner decides whether a modest Mendota-only audit is worth doing, no protocol revision, review or analysis should proceed. The decision map shows that removing Buffalo Pound simplifies the dependency chain substantially; it does not remove the need for reviewers, count audit, licence review and D-15.

**No decision was approved. No analysis was authorised.**
