# External Response Decision Tree

**Sprint:** 4L.19  
**Purpose:** Define how the project will respond to custodian, reviewer and licence outcomes without automatic approval.  
**Status:** Decision framework only. **No response has been received. No decision is approved.**

---

## 1. Governing rule

No external response — custodian, reviewer, licence reviewer or competition organiser — is itself an approval.

- A custodian answer resolves an **evidence gap**, not D-05, D-06 or D-15.
- A reviewer opinion is **advice**, not a decision.
- A licence review is a **compliance input**, not scientific approval.
- A competition rule check is an **eligibility input**, not approval to analyse.

Every pathway ends at a **recorded governance decision** with the required authority.

---

## 2. Master flow

```text
Custodian enquiry
   ├── full response ──► assess evidence ──► update D-02/D-05/D-06/D-08/D-09
   ├── partial response ──► assess gaps ──► conditional population or P3/P4 drop
   ├── decline ──► D-05 unresolved ──► Mendota-only or pause
   └── no response ──► documented wait ──► Mendota-only or pause

Scientific review
   ├── acceptable ──► record advice ──► continue to other conditions
   ├── revisions ──► revise protocol ──► re-review if material
   ├── restrict ──► reduce estimands ──► formal decision
   ├── pause ──► pause ──► no analysis
   └── reject ──► stop current design ──► reassess Stage 1/2

Statistical review
   ├── acceptable ──► record advice ──► continue to other conditions
   ├── revisions ──► revise statistical plan ──► re-review if material
   ├── not estimable ──► reduce/pause
   └── reject ──► stop current design ──► reassess

Licence/competition review
   ├── compatible with conditions ──► record conditions ──► continue
   ├── requires permission ──► obtain permission ──► continue or pause
   └── incompatible ──► no display/analysis ──► pause or redesign

All conditions met?
   ├── yes ──► count audit ──► D-15 decision ──► analysis (if approved)
   └── no ──► do not analyse; record blocker
```

---

## 3. Custodian pathways

### 3.1 Full response — all essential questions answered

**What it means:** duplicate/`REP`, biomass derivation, B7, negative/above-range RFU, coverage, time zone and sample times are documented.

**Actions:**

1. Record the response verbatim (or the exact written statement) in the correspondence log.
2. Update `BUFFALO_POUND_UNRESOLVED_QUESTIONS.csv` statuses.
3. Reassess D-02, D-05, D-06, D-08 and D-09 against the new evidence.
4. If the response contradicts a protocol rule, mark the protocol as requiring revision; do not silently change it.
5. Ask the scientific and statistical reviewers to consider the new evidence.
6. Do **not** mark D-05 approved; it remains a governance decision.

**Possible outcome:** P3/P4 may move from “unresolved” to “conditional exploratory” or “primary candidate,” depending on the quality of the answer and reviewer advice. They do not automatically become primary.

### 3.2 Partial response — some essential questions answered

**What it means:** for example, B7 and coverage are clarified, but duplicate/`REP` or biomass derivation is not.

**Actions:**

1. Record what was answered and what was not.
2. Identify which estimands remain interpretable.
3. If P3/P4 depend on the unanswered items, keep them exploratory or drop them.
4. Do not fill gaps by assumption.
5. Update the missing-evidence register with the exact remaining question.

**Possible outcome:** Mendota-core design (Outcome B) or strict two-lake design with P3/P4 as appendices (Outcome C), depending on reviewer advice.

### 3.3 Decline

**What it means:** the custodian declines to clarify, or states that the information is unavailable.

**Actions:**

1. Record the decline and date.
2. Treat D-05, D-02 and D-08 as unresolved.
3. Do not use the data for a primary Buffalo Pound claim.
4. Choose Mendota-only (Outcome B) or pause (Outcome D), with reasons.
5. Do not send repeated requests; one respectful follow-up after a reasonable period is the maximum unless the custodian invites further contact.

**Possible outcome:** Mendota-only or pause. P3/P4 are not rescued by assumption.

### 3.4 No response

**What it means:** no reply after a reasonable period (suggested 15 working days; longer if the custodian is known to be away).

**Actions:**

1. Record the date of the enquiry and the absence of a reply.
2. Send at most one polite follow-up, if the project owner authorises it.
3. If still no response, treat the evidence as unavailable.
4. Proceed with Mendota-only or pause; do not claim the custodian “confirmed” anything.

**Possible outcome:** Mendota-only or pause. The Buffalo Pound data remain usable only as unverified context, not as a primary estimand.

---

## 4. Scientific reviewer pathways

### 4.1 Acceptable as proposed

1. Record the report and the reviewer’s disclosures.
2. Check that the reviewer actually addressed the fatal/remediable distinction.
3. Continue to the statistical review and other conditions.
4. Do not treat the review as D-15 approval.

### 4.2 Acceptable with specific revisions

1. List each required revision.
2. Decide whether it is editorial, methodological or governance-related.
3. If methodological, revise the protocol and record the change.
4. If material, ask for a limited re-review.
5. Do not analyse until the revision is recorded and the other conditions are met.

### 4.3 Restrict to fewer estimands

1. Record which estimands the reviewer considers defensible.
2. Decide whether to drop P3/P4, restrict to Mendota, or reduce sensitivities.
3. Update the decision matrix and protocol.
4. Re-review if the reduction changes the question.
5. Do not retain a dropped estimand as a “supplementary” result without disclosure.

### 4.4 Exploratory only

1. Strengthen the claims matrix: no inferential language, no validation, no early warning.
2. Ensure the report labels every estimate as descriptive/exploratory.
3. Continue only if the other conditions are met.
4. Do not use exploratory status to bypass QC or provenance.

### 4.5 Pause pending evidence

1. Identify the evidence required.
2. Pause analysis.
3. Record the pause in the decision matrix.
4. Resume only when the evidence is obtained and reviewed.

### 4.6 Reject current design

1. Record the fatal issue.
2. Do not revise around it without addressing it directly.
3. Consider Mendota-only, a different question, or Stage 2.
4. Do not present the rejection as a personal judgement; present the methodological reason.

---

## 5. Statistical reviewer pathways

### 5.1 Spearman acceptable

1. Record the advice.
2. Confirm the tie/zero handling and minimum-n rule.
3. Confirm that the descriptive language is honest.
4. Continue to the other conditions.

### 5.2 Revisions required

Examples: add a seasonal stratification, change the influence diagnostic, drop a sensitivity, set a minimum n, use a different descriptive summary.

1. Record each change.
2. Revise the statistical analysis plan.
3. Re-review if the change affects the estimand or the claims.
4. Do not run the analysis under the old plan.

### 5.3 Not estimable

Examples: too few dates, too much dependence, detection-conditioned population makes rho uninterpretable.

1. Record the reason.
2. Reduce to a descriptive case series or pause.
3. Do not report a rho as if it were meaningful when the reviewer says it is not.

### 5.4 Reject

1. Record the fatal statistical issue.
2. Stop the current design.
3. Reassess Stage 1/Stage 2.

---

## 6. Licence and competition pathways

### 6.1 Compatible with conditions

1. Record the exact conditions (attribution, ShareAlike, non-commercial, permission).
2. Add the attribution wording to the report/poster.
3. Confirm that the competition use is covered.
4. Continue, but do not treat licence compatibility as scientific approval.

### 6.2 Permission required

1. Identify the rights holder.
2. Request written permission (this is a separate external contact; do not send without authorisation).
3. Do not display or redistribute the data until permission is recorded.
4. If permission is refused, remove the data/output from the public material or pause.

### 6.3 Incompatible

1. Do not display or distribute the affected data/output.
2. Reassess whether a different dataset or a data-free presentation is possible.
3. Record the decision.

---

## 7. Decision gates

| Gate | Required evidence | Who decides | What it unlocks |
|---|---|---|---|
| G1 — Custodian evidence | Written answers to the essential questions | Project owner + scientific reviewer | P3/P4 status; D-05 reassessment |
| G2 — Scientific review | Written report and disclosure | Project owner | Protocol revision; Stage 1 scope |
| G3 — Statistical review | Written report and disclosure | Project owner | Statistical plan; estimability |
| G4 — Licence/competition | Written review/permission | Project owner + licence reviewer | Public display; data use |
| G5 — Protocol revision | Revised protocol with traceability | Project owner + reviewers | Count-audit authorisation |
| G6 — Count audit | Completed count-only audit | Project owner + statistical reviewer | Final n and estimability |
| G7 — D-15 | All prior gates recorded | All approvers | Analysis authorisation |

No gate may be skipped. A gate can be “closed — not met,” which stops progress; it cannot be “assumed.”

---

## 8. What never happens automatically

- A custodian reply does not approve D-05.
- A reviewer “yes” does not approve D-15.
- A licence review does not approve the science.
- A competition deadline does not justify skipping review.
- A positive integrity check does not establish validity.
- A completed document does not authorise analysis.
- A weak result does not justify changing the question after the fact.
- A strong result does not justify dropping the limitations.

---

## 9. Current state

| Item | State |
|---|---|
| Custodian enquiry | Prepared, **not sent** |
| Custodian response | None |
| Scientific reviewer | Not appointed |
| Statistical reviewer | Not appointed |
| Licence review | Not completed |
| Protocol revision | Not completed |
| Count audit | Not authorised |
| D-15 | **NOT APPROVED** |
| Analysis | **NOT AUTHORISED** |

**Next action:** obtain human authorisation to send the custodian enquiry and the reviewer invitations. Do not analyse while waiting.
