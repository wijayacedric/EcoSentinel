# Remaining Decisions Register — D-09, D-11, D-14, D-15

**Sprint:** 4L.17  
**Status:** Decision-support document. No decision is approved.  
**Purpose:** Record what can be resolved now, what remains blocked, and the exact evidence/approvals required for the remaining decisions.

---

## D-09 — Buffalo Pound 2019-07-17 anomaly

**Original wording:** (a) retain and flag, exclude in sensitivity; (b) exclude from primary; (c) correct  
**Current status:** **OUTSTANDING — NOT APPROVED**  
**Dependency:** **D-05** remains unresolved.

### What can be resolved now

- The **handling principle** can be documented provisionally: retain and flag; plan an exclusion sensitivity only if analysis is later authorised; do not correct; do not interpret as bloom/non-bloom.
- The **dependency** on D-05 can be recorded: the anomaly cannot be finalised until the primary QC population is settled.
- The **prohibition** on calculating influence can be recorded.

### What remains blocked

- Any actual influence calculation, delta-rho, rank extremeness, or leave-one-date-out result. This is analysis and is **not authorised**.
- A final D-09 decision, because D-05 is unresolved.
- Any explanation of the anomaly’s cause; the source record does not provide one.

### Exact evidence/approvals needed

| Item | Needed from |
|---|---|
| D-05 QC framework resolved | Data custodian + statistical reviewer |
| Acceptance of retain/flag/influence plan | Data custodian + scientific reviewer |
| Anomaly provenance (optional) | Data custodian/source records |
| Analysis authorisation before any influence calculation | D-15 |

### Provisional wording

> **D-09 provisional handling (not approved).** Retain and flag the 2019-07-17 record in the primary population. If analysis is later authorised, report its rank extremeness and influence on rho, including full-data and leave-one-date-out estimates and exact delta-rho. Do not correct the value. Do not interpret it as a bloom or non-bloom observation. Do not calculate influence before D-15.

---

## D-11 — Small-sample reporting

**Original wording:** (a) no stratum rho if n<10; show points; (b) compute all; (c) pool strata  
**Current status:** **OUTSTANDING — NOT APPROVED**

### What can be resolved now

The **principle** is reviewable now:

- no stratum-specific Spearman correlation when n < 10;
- display observations without estimating rho where the minimum is not met;
- no pooling across strata/lakes to overcome insufficient n;
- no post-hoc minimum chosen after seeing results;
- an overall minimum-estimability rule must be set by the independent statistical reviewer before estimation.

This principle is consistent with the 4L.13/4L.14 reviews and does not require the count audit.

### What remains blocked

- The **numeric overall minimum n** cannot be set responsibly until the count-only audit is separately authorised and completed.
- Actual n by estimand/stratum is unknown.
- No estimate can be computed before D-15.

### Exact evidence/approvals needed

| Item | Needed from |
|---|---|
| Acceptance of the n<10 principle and no-pooling rule | Independent statistical reviewer |
| Overall estimability principle (not a post hoc threshold) | Independent statistical reviewer |
| Count-only audit authorisation | Separate human authorisation; not D-15 |
| Count-only audit result | OpenCode after authorisation |
| Numeric threshold | Statistical reviewer after count audit |

### Proposed wording

> **D-11 proposed principle (not approved).** No stratum-specific Spearman rho is reported when n < 10; points and n are shown instead. Strata are not pooled to overcome small n. An overall minimum-estimability rule is set by the independent statistical reviewer before estimation, based on the count-only audit and not on observed associations. The numeric threshold is deferred until the count audit is separately authorised and completed.

---

## D-14 — Licence and competition compliance

**Original wording:** (a) use Painter data under CC BY-NC-SA with attribution/share-alike; (b) exclude Painter data; (c) seek permission  
**Current status:** **OUTSTANDING — NOT APPROVED**

### Verified licence terms

The Painter et al. (2022) dataset is distributed under **CC BY-NC-SA 4.0**. The official legal code establishes:

- **Attribution:** retain creator identification, copyright notice, licence notice, disclaimer, and URI/link; indicate modifications.
- **NonCommercial:** use must not be primarily intended for or directed towards commercial advantage or monetary compensation.
- **ShareAlike:** if you share **Adapted Material**, the adapter’s licence must be the same licence elements (or a compatible licence), with a link/text of the adapter’s licence.
- **Share:** includes public display, distribution, dissemination, and communication.
- **Database rights:** extracting/reusing a substantial portion of the database is covered; including substantial contents in another database may make that database Adapted Material.

Source: https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en (accessed 2026-11-25).

### Verified competition context

- SciFest@College 2027 rules require a Project Report Book and Visual Display.
- Projects remain the property of the exhibitors, but project content/material may be used by SciFest for exhibition or publication.
- SciFest’s website terms prohibit commercial use of **SciFest website content**, not necessarily the student’s own project content.
- A student science-fair project is not automatically exempt from the licence; “educational” is not the same as “non-commercial” in every context, and public display/dissemination can trigger attribution/share-alike.

### What can be resolved now

- Document the licence obligations.
- Decide whether the intended display/report will reproduce or adapt Painter data, or only report derived results.
- Identify whether the report/display can carry the required attribution and share-alike notice.
- Decide whether to seek written permission from the data custodians for the intended competition use.

### What remains blocked

- A final compatibility determination requires a **written licence/competition review** by the appropriate authority.
- The exact competition terms for the chosen venue/year should be confirmed.
- Whether share-alike extends to the whole report, only the adapted figures/tables, or a separate data appendix is a legal/interpretive question; this package does not provide legal advice.

### Options

| Option | When appropriate | Consequence |
|---|---|---|
| (a) Use under CC BY-NC-SA | If the display/report can comply with attribution, non-commercial, and share-alike for adapted material | Must include licence/attribution notices; share-alike plan required |
| (b) Exclude Painter data | If compliance is uncertain or the competition cannot accommodate the licence | Buffalo Pound P3/P4 removed from public/competition use; Mendota remains |
| (c) Seek permission | If the custodian can grant broader or clarified terms | Written permission required; not assumed |

### Required approval

**Licence/competition reviewer**, with a written record. D-14 is **not approved** by this document.

---

## D-15 — Final analysis authorisation

**Original wording:** (a) approve; (b) approve with changes; (c) do not approve  
**Current status:** **OUTSTANDING — NOT APPROVED**

### Exact prerequisites for reconsideration

D-15 cannot be reconsidered until **all** of the following are recorded:

1. **D-01–D-14 formally recorded** by their proper authorities, with decision IDs preserved.
2. **Custodian clarifications** obtained for Buffalo Pound duplicates, biomass provenance, coverage, QC, and Mendota station semantics — **or** the affected analyses explicitly excluded.
3. **Licence and competition compliance** resolved (D-14).
4. **Count-only audit separately authorised and completed** under its own scope, with actual n reported.
5. **Independent scientific and statistical reviews** completed.
6. **Protocol and addendum reconciled** into a reviewable version, without silent changes.
7. **Explicit human approval of D-15** by all required approvers.

### What remains blocked

- Every form of analysis: correlations, usable-n calculations, labels, event intervals, derived datasets, models, hypothesis tests, threshold optimisation, predictive/EWS analysis.
- Any count-only audit until separately authorised.
- Any claim that the protocol is approved.

### Required approval

All required approvers: scientific, statistical, data custodian, Gate 2 governance, licence/competition, project owner.

**D-15 remains NOT APPROVED.**
