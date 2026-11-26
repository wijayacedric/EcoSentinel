# Independent Review Protocol

**Sprint:** 4L.19  
**Status:** Proposed review process. **No reviewer has been appointed.**  
**Purpose:** Define how independent scientific and statistical review will be conducted before any decision on Stage 1 or D-15.

---

## 1. Why independent review is required

The proposed study is a descriptive measurement audit, not a validation or early-warning study. Its main risks are not computational:

- the biological endpoints are microscopy-derived and imperfect;
- the sensor variables are relative fluorescence, not absolute pigment concentrations;
- the two lakes differ in depth alignment, sampling, instrumentation and period;
- the Buffalo Pound provenance and replicate semantics are unresolved;
- the sample sizes are small and the observations are temporally structured;
- the same dates and endpoints are reused across four estimands and multiple sensitivities.

Internal review cannot adequately test these risks. Independent reviewers must be able to say that the design is not viable without fearing that they are obstructing the project.

---

## 2. Independence

A reviewer is independent if they:

1. have **no authorship, formal contributor role or data-custodian role** in the Buffalo Pound buoy dataset, the Buffalo Pound biological dataset, or the NTL-LTER Mendota data used here;
2. have **no current employment, studentship, grant, contract or financial relationship** with the dataset PIs or the EcoSentinel project;
3. have **no supervisory or close personal relationship** with the project owner;
4. have **no direct interest in a particular result** (for example, a stake in a sensor manufacturer, a competing study, or a policy position that depends on the result);
5. have not already reviewed the same protocol in a role that would compromise independence.

A reviewer may still be independent if they have a general familiarity with the lake, the sensor type, or the research group, provided it is disclosed. Familiarity is not the same as a conflict.

### 2.1 Disclosable, not automatically disqualifying

- Co-authorship with a dataset author more than five years ago.
- Membership of the same professional network (e.g., GLEON) without a current collaboration.
- Having published on the same lake using different data.
- Having reviewed an earlier version of the protocol.
- Institutional affiliation with a dataset author’s institution, without a direct relationship.

### 2.2 Presumptively disqualifying

- Current or recent co-authorship with a dataset PI on the Buffalo Pound or Mendota data.
- Current funding from the same grant or centre that produced the data.
- A direct supervisory relationship with the project owner.
- A financial interest in the result.
- Refusal to complete the disclosure form.

The project owner records the disclosure and the reason for accepting or rejecting a reviewer. A disclosed conflict does not automatically disqualify; an undisclosed conflict does.

---

## 3. Separate scientific and statistical reviewers

The default is **two separate reviewers**:

- one **scientific reviewer** with freshwater ecology, phytoplankton/cyanobacteria, sensor or monitoring expertise;
- one **statistical reviewer** with ecological/environmental statistics, time-series or measurement-error expertise.

A single person may fill both roles only if they have demonstrable expertise in both areas and no conflict. The project owner must record why one person was used instead of two.

If the two reviewers disagree on a **fatal** issue, the project owner may appoint a third adjudicator with relevant expertise. The adjudicator receives both reports and the project owner’s reconciliation memo. The adjudicator’s role is to advise on the disagreement, not to approve the project.

---

## 4. What reviewers are asked to decide

Reviewers are asked to provide a **written opinion**, not a binary approval. For each question, they should state:

- their judgement;
- the reasons and evidence;
- whether the issue is **fatal**, **remediable with specific revisions**, or **a disclosable limitation**;
- what evidence or change would alter their judgement.

They are not asked to:

- approve D-15;
- endorse a hypothesis;
- validate the protocol as a whole;
- analyse data;
- contact the data custodian;
- take on a project role.

---

## 5. Review materials

The smallest complete package is listed in `REVIEWER_EVIDENCE_PACKAGE_MANIFEST.csv`. It contains:

- the research question and proposed protocol;
- the estimand/eligibility specification;
- the biological endpoint and biomass review;
- the QC evidence report;
- the Buffalo Pound provenance investigation;
- the D-06 daily-summary assessment;
- the decision-status matrix;
- the claims and limitations section;
- the Stage 1 viability reassessment;
- this protocol and the conflict-of-interest checklist;
- the reviewer brief.

It does **not** contain:

- raw data files;
- personal correspondence;
- the Müggelsee email or response tracker;
- unrelated project files;
- the full repository.

Reviewers may request additional public documentation. They should not be given raw data unless a specific need is justified and the project owner records the reason.

---

## 6. Review process

### Step 1 — Invitation

The project owner sends the invitation, the brief and the disclosure checklist. The invitation states the scope, the estimated time, the absence of a fee, and the right to decline.

### Step 2 — Disclosure

The reviewer completes `REVIEWER_CONFLICT_OF_INTEREST_CHECKLIST.md` before receiving the full package. The project owner records the disclosure and decides whether the review can proceed.

### Step 3 — Materials

The project owner sends the manifest and the files. The reviewer confirms receipt and identifies any missing or unreadable material.

### Step 4 — Written review

The reviewer submits a written report using the structured questions in the brief. The report must distinguish fatal issues from remediable limitations. It should not be a general essay about the importance of lakes.

### Step 5 — Clarification (optional)

The project owner may ask written clarification questions. A call is optional and should be minuted. The reviewer is not asked to negotiate the conclusion.

### Step 6 — Reconciliation

The project owner writes a reconciliation memo that:

- lists each reviewer comment;
- states the proposed response;
- distinguishes “accept”, “accept with revision”, “dispute with reasons”, and “cannot resolve without new evidence”;
- records which changes require a formal protocol revision;
- records which decisions remain reserved.

### Step 7 — Decision record

The project owner records the review outcome and the resulting decision status. A review is advice; it does not itself approve D-01–D-15 or D-15.

### Step 8 — Re-review

If the protocol changes materially, the reviewer may be asked to review the revision. A re-review is limited to the changed sections and their consequences. It is not a new endorsement of the whole project.

---

## 7. Outcome framework

Reviewers should choose one of the following for the design as a whole, and explain:

| Outcome | Meaning | Consequence |
|---|---|---|
| **A — Acceptable as proposed** | The design, estimands, QC and claims are defensible as an exploratory audit | Still requires custodian evidence, licence review and D-15 approval |
| **B — Acceptable with specific revisions** | The design is viable if named changes are made | Protocol revision and, if material, re-review |
| **C — Restrict to fewer estimands** | Only a subset (e.g., P1/P2, or one lake) is defensible | Formal reduction; update decision matrix |
| **D — Exploratory only** | The design may proceed only as a descriptive exercise with no inferential or validation language | Strengthen claims matrix; no D-15 until other conditions met |
| **E — Pause pending evidence** | A named missing piece (custodian, coverage, licence) is required first | Pause; no analysis |
| **F — Reject current design** | A fatal methodological problem cannot be remedied within the current data | Stop; reassess Stage 1/Stage 2 |

The reviewer must also classify each major issue as:

- **Fatal** — the design cannot answer the question even with revisions;
- **Remediable** — a specific change would make it defensible;
- **Disclosable** — the limitation can be reported honestly without invalidating the design.

---

## 8. Reserved decisions

Reviewers advise; they do not decide. The following remain with the project owner/governance:

- whether to continue, reduce or pause Stage 1;
- whether to retain P3/P4;
- whether to revise the protocol;
- whether to authorise the count audit;
- whether to approve D-01–D-14;
- whether to approve D-15;
- whether to contact the custodian or reviewers;
- whether the competition entry proceeds.

No reviewer’s opinion overrides the governance statuses. A positive review does not authorise analysis. A negative review does not automatically terminate the project; it must be considered and recorded.

---

## 9. Disagreement and reconciliation

- Do not average reviewer opinions.
- Record the disagreement and the evidence each reviewer relied on.
- If the disagreement concerns a fatal issue, appoint an adjudicator or pause.
- If the disagreement concerns emphasis or scope, the project owner decides and records reasons.
- If the reviewers agree on a fatal issue, do not proceed without resolving it.
- If one reviewer identifies a fatal issue and the other does not, treat it as unresolved until the project owner obtains a reasoned response.

---

## 10. Confidentiality and conflicts

- Review materials are provided for the review only.
- Reviewers should not redistribute the package or quote unpublished project material without permission.
- Reviewers should not contact the data custodian or dataset authors on the project’s behalf.
- The project owner should not publish a reviewer’s name or report without permission.
- If a reviewer later becomes involved in a related study, they should disclose it.

---

## 11. Timeline

A suggested timetable, not a demand:

- invitation and disclosure: 1 week;
- materials and reading: 2 weeks;
- written review: 1 week;
- clarification/reconciliation: 1 week.

If a reviewer needs more time, the project owner records the delay. Do not pressure a reviewer for a positive answer.

---

## 12. Records to retain

- invitation and date;
- disclosure form;
- materials sent;
- reviewer report;
- clarification notes;
- reconciliation memo;
- decision record;
- re-review, if any.

These records are part of the project evidence. They should be hashed and stored with the sprint package.

---

## 13. What would make the review invalid

- The reviewer was selected because they were expected to approve.
- The reviewer has an undisclosed conflict.
- The reviewer was asked to approve D-15 rather than assess the design.
- The reviewer was given only a summary, not the evidence package.
- The project owner changed the protocol after the review without recording the change.
- The review was treated as a substitute for custodian evidence or licence review.

---

## 14. Current status

- Scientific reviewer: **not appointed**.
- Statistical reviewer: **not appointed**.
- Invitations: **drafted, not sent**.
- Review materials: **listed, not sent**.
- D-15: **NOT APPROVED**.
- Analysis: **NOT AUTHORISED**.
