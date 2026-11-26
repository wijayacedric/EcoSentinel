# Statistical Reviewer — Final Invitation

**Status:** Final draft. **NOT SENT.** No reviewer has been contacted or appointed.  
**Prepared:** 2026-11-25  
**Recipient:** Dr Mark D. Scheuerell, USGS Washington Cooperative Fish and Wildlife Research Unit; University of Washington.

---

## 1. Verified recipient

| Field | Value | Evidence |
|---|---|---|
| Name | Dr Mark D. Scheuerell | ORCID `0000-0002-8284-1254`; USGS profile |
| Institution | USGS Washington Cooperative Fish and Wildlife Research Unit; School of Aquatic and Fishery Sciences, University of Washington | ORCID employment record |
| Role | Assistant Unit Leader (USGS); Associate Professor (UW) | ORCID employment record |
| Email | `mscheuerell@usgs.gov` | ORCID record; alternate `scheuerl@uw.edu` |
| Profile | `https://www.usgs.gov/staff-profiles/mark-scheuerell` | Official USGS staff profile (page did not load in this environment; identity verified via ORCID) |
| Subject | Invitation to review the statistical design of an exploratory freshwater sensor–phytoplankton audit | — |

**Verification date:** 2026-11-25. Re-check the address before sending.

---

## 2. Email body

Dear Dr Scheuerell,

I am writing from the EcoSentinel research project, an independent secondary-school study of whether surface chlorophyll and phycocyanin fluorescence can track independent microscopy-derived cyanobacteria abundance in lakes. We are preparing a narrow, descriptive measurement audit and would like an independent statistical opinion before any analysis is authorised. We are not asking you to endorse a result or to approve the project; we are asking whether the proposed statistic and reporting rules are defensible, and where the design cannot support an honest descriptive claim.

The study uses two existing datasets as separate case studies:

- **Lake Mendota, Wisconsin:** daily sensor means and microscopy-derived cyanobacteria biovolume; Turner chlorophyll/phycocyanin (2006–2019), with a separate YSI era; sensors at 0.5 m, biology generally a 0–8 m composite; upper-bound same-day n of 128/139.
- **Buffalo Pound Lake, Saskatchewan:** a 2014–2021 high-frequency buoy dataset and a 2018–2019 microscopy dataset; 42 sampling dates across two seasons; daily record counts vary substantially.

The proposed analysis is deliberately minimal: Spearman’s rho for each of four estimands (P1–P4), with n and descriptive sensitivity ranges; no p-values, no confidence intervals, no bootstrap, no Pearson/log-Pearson, no models, no prediction. Mendota influence is assessed with leave-one-year-out; Buffalo Pound with leave-one-date-out. The study is explicitly **not** a validation, calibration, agreement, prediction or early-warning analysis.

The current protocol is **PROPOSED — NOT APPROVED**; all 15 project decisions are outstanding; analysis is **NOT AUTHORISED**. We are seeking statistical review, not approval.

I would be grateful for your written opinion on the following, with reasons:

1. Is Spearman’s rho a defensible descriptive statistic for date-level co-occurrence, given ties, many zeros, seasonal structure and serial dependence?
2. Is the proposed “descriptive sensitivity range” language honest, or does it still imply inferential uncertainty?
3. Are leave-one-year-out and leave-one-date-out sufficient influence diagnostics, or is another descriptive check needed?
4. Does the detection-conditioned population — dates on which a cyanobacteria row was reported — introduce a selection bias that makes rho uninterpretable?
5. Is the Mendota 0.5 m vs 0–8 m mismatch fatal to P1/P2, or can it be reported as a bounded limitation?
6. Can the two-season Buffalo Pound series support any descriptive rho, even exploratory?
7. Are the proposed QC exclusions (C/E, H, G, B7, negative and >100 RFU) likely to bias the rank association? Which sensitivities are essential?
8. Is the n < 10 stratum rule defensible? What overall minimum-estimability principle should be set before a count audit?
9. Do the four estimands and nine sensitivities create hidden multiplicity or researcher degrees of freedom?
10. Is Stage 1 statistically viable as a descriptive audit, or should it be paused?

The review would involve reading the protocol, the statistical analysis and uncertainty plan, the QC evidence and the claims matrix. We estimate 1–2 hours. There is no fee. We will not ask you to analyse data or to take on any project role. A short written response with reasons and any conditions would be sufficient.

Before accepting, please disclose any role in the Buffalo Pound or NTL-LTER datasets, the Painter/Baulch research, or the EcoSentinel project, and any current collaboration or funding relationship that could affect independence. A disclosed conflict does not automatically disqualify you; it allows us to judge the appropriate scope.

The review materials are listed below. If you are willing, I can send the package and a short review form. If you are not available, a brief decline is perfectly fine and will not be taken as an adverse judgement.

Thank you for considering this request.

Kind regards,

EcoSentinel Research Project  
Independent secondary-school research project

---

## 3. Attachments and rationale

| Attachment | Why it is provided |
|---|---|
| `STATISTICAL_REVIEWER_BRIEF.md` | One-document orientation: estimands, statistic, known problems, decision state, specific questions |
| `REVISED_PROTOCOL.md` | The current proposed protocol, especially the statistical, uncertainty and claims sections |
| `UNCERTAINTY_AND_SENSITIVITY_PLAN.md` | The proposed influence diagnostics and sensitivity list |
| `ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md` | Eligibility, matching, replicate and coverage rules |
| `INDEPENDENT_REVIEW_PROTOCOL.md` | The review process, independence rules, outcome framework and reserved decisions |
| `REVIEWER_EVIDENCE_PACKAGE_MANIFEST.csv` | The complete list of materials and what each is for |
| `REVIEWER_CONFLICT_OF_INTEREST_CHECKLIST.md` | Disclosure form to complete before review |
| `D05_QC_EVIDENCE_RESOLUTION_REPORT.md` | The rule-by-rule QC evidence assessment |
| `BUFFALO_POUND_PROVENANCE_INVESTIGATION.md` | Provenance and unresolved custodian questions |
| `STAGE1_VIABILITY_REASSESSMENT.md` | The four possible Stage 1 outcomes and the current recommendation |

Do **not** attach raw data, personal correspondence, the Müggelsee email, or unrelated project files.

---

## 4. Sending checklist

- [ ] Project owner has authorised reviewer contact.
- [ ] Email address re-checked in the ORCID record or USGS directory.
- [ ] Subject line unchanged.
- [ ] Attachments present and readable.
- [ ] No raw data or personal information beyond the reviewer’s own professional details.
- [ ] Send from the project owner’s student/professional account.
- [ ] Record the send date, recipient, subject and message ID.
- [ ] If the reviewer accepts, send the conflict-of-interest checklist before the materials.
- [ ] Do not describe the reviewer as “appointed” until they have accepted and disclosed.

**Status: NOT SENT.**
