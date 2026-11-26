# Sprint 4L.18 Report — Human-Review Readiness and D-05 Evidence Resolution

**Sprint:** 4L.18  
**Date:** 2026-11-25  
**Status:** Documentation and QC evidence-resolution package. **No decision approved. No analysis authorised.**  
**Governance:** Protocol **PROPOSED — NOT APPROVED**; Gate 2 **PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY)**; D-01–D-15 **OUTSTANDING**; D-15 **NOT APPROVED**; analysis **NOT AUTHORISED**.

---

## 1. Work completed

- Read `AGENTS.md` in full.
- Inspected the 4L.16 and 4L.17 packages, the 4L.14 protocol/addendum, QC audits, raw-data documentation, source registers and decision records.
- Conducted a focused D-05 audit against primary sources:
  - NTL-LTER 129.42 EML;
  - 4L.9 Mendota QC tables;
  - Buffalo Pound README and `data_flags.csv`;
  - Baulch et al. 2025 Data in Brief paper;
  - YSI 6025/6131 documentation and 6-Series manual;
  - USGS TM 1-D10.
- Prepared a custodian clarification enquiry and evidence-requirements table.
- Prepared independent scientific and statistical reviewer briefs and enquiry drafts.
- Reassessed D-06 in light of D-05.
- Updated the decision-status matrix and missing-evidence register.
- Verified D-14 licence/competition text from official sources.

**No analysis, count audit, labels, event intervals, derived datasets, models, data acquisition, emails, external contacts, commits or pushes were performed.**

---

## 2. D-05 — what is genuinely supported

### 2.1 Supported

| Rule | Evidence | Status |
|---|---|---|
| Buffalo Pound `M` = missing; exclude | `data_flags.csv`; Data in Brief Table 2 | **Supported** |
| Buffalo Pound `C` = faulty/unrealistic; exclude | `data_flags.csv`; Data in Brief | **Supported** |
| Missing values excluded; no imputation/zero-fill | EML; README; 4L.14 rule | **Supported** |
| 0–100 RFU is the YSI 6025/6131 full-scale range | YSI 6025 spec; YSI 6-Series manual; Data in Brief Table 7; USGS RFU definition | **Verified** |
| Values >100 RFU are outside the documented full scale; cannot be assumed quantitative | Same | **Supported conditionally** — whether values occur/saturate needs custodian/count |
| Mendota `C`/`E` are removal-type flags | EML definitions | **Supported conditionally** — C can carry numeric values |

### 2.2 Not supported as written

| Rule | Why not |
|---|---|
| Fixed Buffalo Pound 72/144 coverage + both halves | Daily counts vary 121–144 (2018), 42–131 (2019); no date-specific expected cadence; rule withdrawn |
| Buffalo Pound `B7` = automatic exclusion | B7 is a **caution interval** between maintenance visits where fouling was identified; not a removal flag |
| Mendota `H` retained as valid within a documented range | EML defines H only as “outside of standard range”; no numeric range exists |
| Mendota `G` = automatic invalidity | G is “suspected biofouling,” not confirmed invalid; Turner has no G |
| Negative RFU = “below-baseline” valid low signal | No documentation supports this; USGS says RFU is 0–100% of operating range |
| Undocumented flags included in sensitivity as if equivalent | No definition; inclusion is not interpretable |

### 2.3 Requires custodian clarification

- `M`/`C`/`B7` handling in the local files;
- whether B7 means discard or caution;
- exact B7 interval and overlap with high biomass;
- negative RFU meaning;
- date-specific expected cadence and partial-day handling;
- time zone/timestamp convention;
- calibration/maintenance records;
- duplicate rows/`REP1`/`REP2`;
- exact `Biomass_mg_m3` derivation, density and field mapping;
- whether values >100 RFU occur and how they were processed.

Full rule-by-rule detail: `D05_QC_EVIDENCE_RESOLUTION_REPORT.md`.

---

## 3. D-05 conclusion

**D-05 cannot be approved on current evidence.**

A conservative interim analysis population can be described:

- unflagged numeric values only;
- C/E/O excluded;
- H excluded from primary because no numeric range exists;
- G and B7 treated as caution flags, not automatic invalidity;
- negative and >100 RFU excluded primary, reported and sensitivity-only;
- no imputation.

This is an **analysis population**, not a validated QC system. It may reduce n and may bias the sample; it must be labelled as such.

The original QC decisions were partly evidence-based and partly assumptions. The most important unsupported assumptions are:

- that B7 is a discard flag;
- that H can be retained within a documented range;
- that negative RFU is a valid below-baseline signal;
- that 72/144 defines a representative day;
- that G is invalid rather than suspect.

---

## 4. D-06 — does Option A remain defensible?

**Yes, but only as a provisional project-owner preference — not as an approved or validated summary.**

- Full-day means are the only common daily statistic available for Mendota without within-day reconstruction.
- Buffalo Pound day/night medians are computable only where coverage/time zone are documented.
- The two daily means are **not equivalent exposures**.
- Neither represents the exact sample time or same water parcel.
- Full-day averaging does not remove diel variation/quenching.

D-06 cannot be finalised while D-05 is unresolved. If the custodian cannot document coverage, the defensible fallback is to restrict Buffalo Pound to adequately covered dates, retain Mendota only as a descriptive provider mean, and exclude the affected estimand if representativeness fails — not to switch to Option B/C.

Full assessment: `D06_EVIDENCE_ASSESSMENT.md` from 4L.17, updated by the D-05 findings here.

---

## 5. Remaining decisions

| Decision | Status | What can be done now | What remains blocked |
|---|---|---|---|
| **D-09** | OUTSTANDING — NOT APPROVED | Provisional retain/flag handling; no correction; no bloom interpretation | D-05 resolution; any influence calculation requires D-15 |
| **D-11** | OUTSTANDING — NOT APPROVED | Accept n<10/no-pooling principle; overall minimum principle | Numeric threshold requires a separately authorised count audit |
| **D-14** | OUTSTANDING — NOT APPROVED | Document CC BY-NC-SA obligations; prepare attribution/share-alike plan | Written licence/competition review; no automatic educational exception |
| **D-15** | NOT APPROVED | None | D-01–D-14 recorded; custodian/licence resolved; count audit completed; reviews done; explicit approval |

---

## 6. What independent reviewers need to decide

### Scientific reviewer

- Is the measurement question scientifically meaningful and bounded?
- Are P1–P4 appropriately exploratory, or should any be dropped?
- Is the detection-conditioned population acceptable?
- Is the Mendota depth mismatch handled honestly?
- Are the QC exclusions conservative and defensible (especially H, G, B7, negative RFU)?
- Are the claims limited to rank association/non-equivalence?
- Is Stage 1 viable or should it be paused?

### Statistical reviewer

- Is Spearman’s rho defensible for date-level co-occurrence?
- Are descriptive sensitivity ranges honestly labelled?
- Are leave-one-year/date-out diagnostics sufficient?
- What overall minimum-estimability rule should be set?
- Do the QC exclusions/detection-conditioned population bias rho?
- Are the four estimates and nine sensitivities a multiplicity/selection problem?
- Is Stage 1 statistically viable?

**No reviewer has been appointed or contacted.**

---

## 7. Does Stage 1 remain scientifically viable?

**Conditionally yes — as a modest exploratory measurement/comparability audit, not as confirmation or early warning.**

It remains viable if:

- a conservative, explicit analysis population is accepted;
- P3/P4 remain exploratory;
- H/G/B7/negative rules are reported with sensitivities, not treated as validated;
- D-06 remains provisional;
- no calibration, validation or EWS claims are made.

It is **not** viable as a confirmatory study. It may become non-viable if independent reviewers require a validated QC system that the custodian cannot provide.

---

## 8. Most important unresolved blocker

**The Buffalo Pound custodian clarification.** Without it:

- D-05 cannot be finalized;
- D-06 cannot move beyond provisional;
- D-08/D-02/D-09 cannot be resolved;
- P3/P4 cannot be interpreted;
- D-15 cannot be considered.

The missing independent reviewers are a close second, but the custodian evidence is the gating scientific blocker.

---

## 9. Single most defensible next action

**Obtain written custodian clarification on the D-05 items — especially duplicate/REP semantics, biomass derivation/density, B7 handling, negative RFU, and date-specific coverage/time zone — using the prepared enquiry after human authorisation.**

Do not finalise D-05/D-06 and do not start analysis.

---

## 10. Verification

- All required 4L.18 deliverables created.
- CSVs parse with consistent column counts.
- SHA-256 register and sidecar generated; independent re-hash returned 0 mismatches.
- Historical packages checked: 4L.16 and strategic/Müggelsee registers still 0 mismatches.
- No analysis/count audit/labels/derived datasets/models.
- No emails/contacts/data acquisition/commits/pushes.
- D-15 remains NOT APPROVED; Gate 2 remains PAUSED.

See `INTEGRITY_VERIFICATION.md`.

---

## 11. Governance statement

**Research direction: CONTINUE — NARROWED RESEARCH QUESTION.**

**Protocol: PROPOSED — NOT APPROVED.**

**Gate 2: PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY).**

**D-01–D-15: OUTSTANDING — NOT APPROVED.**

**D-15: NOT APPROVED.**

**Analysis: NOT AUTHORISED.**
