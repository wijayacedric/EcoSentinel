# Project Owner Review Checklist

**Sprint:** 4L.16  
**Purpose:** A practical way for the project owner/student to work through D-01–D-15 without accidentally granting scientific, statistical, data-custodian, governance or licence approval.

> **This checklist does not approve anything.** Recommendations remain recommendations. Every decision stays `OUTSTANDING — NOT APPROVED` until the named authority records it.

---

## 1. Before starting

- [ ] Read `AGENTS.md`.
- [ ] Read `SPRINT_4L14_REVIEW_ADDENDUM.md`.
- [ ] Read `DECISION_REVIEW_MATRIX.csv`.
- [ ] Read `REVIEW_DEPENDENCY_ORDER.md`.
- [ ] Confirm the governance banner: protocol proposed; Gate 2 paused; all 15 decisions outstanding; D-15 not approved; analysis not authorised.
- [ ] Confirm the Müggelsee email was sent on 2026-11-25; do not confuse it with the older unsent 9:59 PM draft.
- [ ] Do not open or run analysis code.

---

## 2. The key distinction

You can:

- read the evidence;
- record your own preference;
- ask reviewers questions;
- decide D-13 (continue/pause) within your authority;
- prepare the competition/licence information.

You cannot:

- approve a scientific or statistical decision because you understand it;
- approve a data-custodian decision because the data are yours to use;
- approve a licence decision because the competition “probably” allows it;
- approve D-15 because you want to start;
- turn “recommended” into “approved” in the register.

---

## 3. Decision-by-decision checklist

### Ready now — document review

- [ ] **D-01 — Comparability.** Read the rank-association rationale. Ask: do I accept that this study measures rank co-variation, not agreement? Record your view. **Scientific + statistical reviewers must sign.**
- [ ] **D-03 — Mendota depth.** Read the 0.5 m vs 0–8 m limitation and the proposed station rule. Ask: is any depth claim made? If yes, stop. **Scientific + data custodian must sign.**
- [ ] **D-04 — Turner/YSI.** Confirm the two eras are separate. Ask: is any concatenation or conversion proposed? If yes, stop. **Data custodian + statistical reviewer must sign.**
- [ ] **D-07 — Temporal window.** Confirm same-calendar-date primary and ±1 day exploratory only. Ask: is any lag/lead/onset claim made? If yes, stop. **Scientific + statistical reviewers must sign.**
- [ ] **D-10 — Uncertainty.** Confirm no bootstrap/CI/p-values; only influence diagnostics. Ask: is any interval described as a confidence interval? If yes, stop. **Statistical reviewer must sign.**
- [ ] **D-12 — Claims matrix.** Read the prohibited claims. Ask: does the draft protocol or competition narrative claim validation, prediction or early warning? If yes, stop. **Scientific + Gate 2 must sign.**

### Project-owner decision

- [ ] **D-13 — Originality / proceed-pause.** Ask yourself:
  - Am I willing to present a modest measurement audit with a possible negative/limited result?
  - Do I need a novel early-warning result for my competition goals?
  - Am I willing to keep Stage 2 conditional and not promise it?
  - Do I accept the low–moderate originality assessment?

  Then choose one:
  - [ ] (a) Proceed as a modest exploratory measurement audit.
  - [ ] (b) Pause because the study is not worth doing for my goals.
  - [ ] (c) Pivot — **only** with a specific, evidence-based alternative and a new protocol.

  Record your rationale. **Scientific and Gate 2 reviewers must concur; this is not a unilateral approval.**

### Conditional — custodian evidence required

- [ ] **D-08 — Buffalo Pound replicates.** Do not choose mean/sum/first yourself. Request/obtain the source documentation. If unavailable, record “deferred; P3/P4 exploratory only.” **Data custodian must sign.**
- [ ] **D-02 — Buffalo Pound endpoint.** Confirm the exact biomass derivation and field provenance. If unavailable, keep P3/P4 exploratory. **Data custodian + scientific reviewer must sign.**
- [ ] **D-05 — QC.** Confirm instrument ranges, flag meanings, B7 overlap and negative counts. Do not approve the fixed 72/144 rule. **Data custodian + statistical reviewer must sign.**
- [ ] **D-06 — Daily summary.** Confirm the asymmetry and coverage evidence. Do not claim the lakes’ daily means are equivalent. **Scientific + statistical reviewers must sign.**
- [ ] **D-09 — 2019-07-17.** Confirm retain/flag/influence plan; no correction; no bloom interpretation. **Data custodian + scientific reviewer must sign.**

### Licence

- [ ] **D-14 — Licence/competition.** Obtain a written licence review of CC BY-NC-SA 4.0 for the intended display/report. If the competition cannot accommodate it, choose exclude Buffalo Pound or seek permission. **Licence/competition reviewer must sign.**

### Premature

- [ ] **D-11 — Small-n threshold.** Set the principle now; do not set the numeric threshold until the count-only audit is authorised and completed. **Statistical reviewer must sign.**
- [ ] **D-15 — Analysis authorisation.** Do **not** sign. It remains premature until D-01–D-14 are recorded, the addendum is re-reviewed, and the count audit is separately authorised.

---

## 4. Review meeting agenda

Use this order:

1. Confirm governance and package integrity.
2. Review the addendum.
3. D-01.
4. D-03.
5. D-04.
6. D-07.
7. D-10.
8. D-12.
9. D-13 (project-owner direction).
10. D-08 → D-02 → D-05 → D-06 → D-09 (custodian track).
11. D-14 (licence).
12. D-11 principle; threshold deferred.
13. D-15 deferred.

Do not combine approvals. If a reviewer is absent, record “deferred,” not “approved by email.”

---

## 5. Questions to ask each reviewer

### Scientific reviewer

- Is the question still a measurement/comparability question, not an early-warning question?
- Are the two case studies kept separate?
- Is the depth limitation stated without a depth-effect claim?
- Are the claims limited to rank association?
- Is the detection-conditioned population clearly described?

### Statistical reviewer

- Is Spearman rho the only association statistic?
- Are all four estimates treated as equal-status exploratory?
- Are influence diagnostics clearly not confidence intervals?
- Is the overall-n rule set before estimation?
- Is there any p-value, bootstrap, or model hiding in the plan?

### Data custodian

- What do duplicate/REP rows mean?
- What is the exact biomass derivation and density assumption?
- What is the date-specific sensor cadence/coverage?
- What do the flags and negative/above-range values mean?
- What is the provenance of the 2019-07-17 record?
- What does a missing cyanobacteria row mean?

### Licence/competition reviewer

- Can CC BY-NC-SA 4.0 material be displayed in the competition?
- Does the report/display count as non-commercial?
- What attribution and share-alike notices are required?
- Is permission needed?
- Does the competition’s own terms add restrictions?

---

## 6. Record-keeping rules

For each decision, record:

- date;
- decision ID;
- who reviewed it;
- what they approved/rejected/deferred;
- evidence considered;
- unresolved issues;
- signature/name;
- whether it is an approval or a recommendation.

Do not edit the 4L.14 register in place. Add a dated addendum/decision log.

---

## 7. What not to do

- Do not mark all decisions “approved” to unblock analysis.
- Do not treat a “recommended” column as an approval.
- Do not let one reviewer sign for another role.
- Do not call the count audit “analysis.”
- Do not start correlations before D-15.
- Do not describe Stage 1 as early warning.
- Do not claim Müggelsee data are available.
- Do not delete the older 9:59 PM Gmail draft without checking it.

**If in doubt: defer. A deferral is honest; a false approval is not.**
