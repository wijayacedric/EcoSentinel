# Sprint 4L.19 Report — External Evidence, Custodian Identification and Review Preparation

**Sprint:** 4L.19  
**Date:** 2026-11-25  
**Status:** External-engagement preparation and evidence reassessment. **No decision approved. No analysis authorised. No external contact made in this sprint.**  
**Governance:** Protocol **PROPOSED — NOT APPROVED**; Gate 2 **PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY)**; D-01–D-15 **OUTSTANDING — NOT APPROVED**; D-15 **NOT APPROVED**; analysis **NOT AUTHORISED**.

---

## 1. Executive summary

Sprint 4L.19 resolved the external-evidence bottleneck as far as public sources allow, without contacting anyone or analysing data.

The main findings:

1. **Buffalo Pound P3/P4 depend on two separate datasets**, not one: a 2014–2021 buoy dataset (FRDR, CC BY 4.0) and a 2018–2019 microscopy dataset (Borealis, CC BY-NC-SA 4.0). The sensor variables and the biological endpoint come from different deposits with different licences, QC systems and version histories.
2. **The Buffalo Pound custodian route is identifiable**: Helen Baulch (PI), Katy Nugent (operational/data) and Kristin Painter (biological/corresponding author). Their professional emails are verified. No one has confirmed current custody.
3. **The core custodian questions remain unanswered**: duplicate rows and `REP1`/`REP2`, exact biomass derivation/density, B7 retention, negative and >100 RFU, date-specific coverage, time zone and phytoplankton sample times.
4. **B7 is definitively a caution interval**, not a removal flag. The *Data in Brief* paper defines it as the entire period between maintenance visits. Automatic exclusion is not supported.
5. **The current protocol is internally inconsistent with the D-05 evidence**. Its QC section still says to retain H, exclude B7, retain negative RFU, retain >100 RFU and use a ≥50% coverage rule. The evidence no longer supports those rules. The protocol must be formally revised before approval.
6. **The strongest scientific reviewers are Cayelan Carey (Virginia Tech), Laurence Carvalho (NIVA), Petra Visser (Amsterdam) and Hans Paerl (UNC)**. Carey is the preferred first choice because she combines lake sensors, cyanobacteria and high-frequency data with a verified contact route.
7. **The strongest statistical reviewers are Mark Scheuerell (USGS/UW), Eli Holmes (NOAA/UW), David Warton (UNSW), Gavin Simpson (Aarhus/Regina), Peter Guttorp (NR) and Christopher Wikle (Missouri)**. Scheuerell is the preferred first choice because he combines ecological time-series expertise with a verified contact route.
8. **Stage 1 remains conditionally viable only as a reduced, exploratory measurement audit.** P1/P2 (Mendota) should be the core; P3/P4 should be conditional exploratory appendices, not equal-status primary estimates. If Buffalo Pound remains unresolved, the defensible fallback is Mendota-only. If reviewers find the depth mismatch fatal, pause.
9. **Originality is low to moderate.** Phycocyanin fluorescence versus cyanobacteria biomass is well studied (Brient 2008; Loisa 2015; Kong 2013; Hodges 2017), and Painter et al. (2022) already showed that the Buffalo Pound autumn *Planktothrix* bloom was not detected by sensor chlorophyll. The modest contribution is a transparent, pre-specified non-equivalence audit, not a new sensor-validation method.
10. **Müggelsee is a credible Stage 2 lead but not a qualified dataset.** FRED 867, FRED 1 and FRED 1145 provide long-term microscopy and sensor data, but access is all rights reserved, the sensor station and phytoplankton stations differ, the depths differ, and no event definition or calibration/QC record is public.

**Single most defensible next action:** obtain human authorisation to send the prepared Buffalo Pound custodian enquiry to Professor Helen Baulch, copied to Katy Nugent and Dr Kristin Painter. Do not analyse while waiting.

---

## 2. Package

`research/evidence/sprint_4l19_external_engagement_preparation/`

### 2.1 Deliverables created

| Group | Files |
|---|---|
| Main report | `SPRINT_4L19_REPORT.md`; `ADVERSARIAL_AUDIT.md` |
| Buffalo Pound | `BUFFALO_POUND_PROVENANCE_INVESTIGATION.md`; `BUFFALO_POUND_FINAL_CUSTODIAN_EMAIL.md`; `CUSTODIAN_CONTACT_VERIFICATION.csv`; `BUFFALO_POUND_UNRESOLVED_QUESTIONS.csv` |
| Scientific reviewers | `SCIENTIFIC_REVIEWER_CANDIDATES.csv`; `SCIENTIFIC_REVIEWER_CANDIDATE_ASSESSMENTS.md`; `SCIENTIFIC_REVIEWER_FINAL_INVITATION.md` |
| Statistical reviewers | `STATISTICAL_REVIEWER_CANDIDATES.csv`; `STATISTICAL_REVIEWER_CANDIDATE_ASSESSMENTS.md`; `STATISTICAL_REVIEWER_FINAL_INVITATION.md` |
| Review framework | `INDEPENDENT_REVIEW_PROTOCOL.md`; `REVIEWER_EVIDENCE_PACKAGE_MANIFEST.csv`; `REVIEWER_CONFLICT_OF_INTEREST_CHECKLIST.md` |
| Stage 1 | `STAGE1_VIABILITY_REASSESSMENT.md`; `STAGE1_ORIGINALITY_AND_PRIOR_ART_REVIEW.md`; `STAGE1_COMPETITION_SUITABILITY_ASSESSMENT.md` |
| Stage 2 | `MUGGELSEE_STAGE2_EVIDENCE_REASSESSMENT.md`; `STAGE2_DATASET_QUALIFICATION_CHECKLIST.md` |
| Decision management | `EXTERNAL_RESPONSE_DECISION_TREE.md`; `UPDATED_DECISION_DEPENDENCY_MATRIX.csv`; `UPDATED_MISSING_EVIDENCE_REGISTER.csv`; `CONTRADICTORY_EVIDENCE_REGISTER.csv` |
| Research audit | `UPDATED_SOURCE_REGISTER.csv`; `EXTERNAL_SEARCH_LOG.md`; `README.md` |
| Integrity | `EVIDENCE_SHA256_REGISTER.csv`; `EVIDENCE_SHA256_REGISTER.csv.sha256`; `INTEGRITY_VERIFICATION.md` |

No file was created empty. No raw data were copied into the package.

---

## 3. Buffalo Pound data provenance

### 3.1 Two datasets, not one

| Feature | Buoy dataset | Biological dataset |
|---|---|---|
| Repository | FRDR | Borealis (Wilfrid Laurier) |
| DOI | `10.20383/103.01100` | `10.5683/SP3/MP6NXF` |
| Licence | CC BY 4.0 | CC BY-NC-SA 4.0 |
| Period | 2014-06-11 to 2021-10-07 | 2018-05-29 to 2019-10-03 |
| Sensor data | YSI 6600/6025/6131, 0.82 m, 10-min | YSI profile casts only; no pigment |
| Biological data | None | Microscopy, 0.8 m, `Biomass_mg_m3` |
| Data paper | Baulch et al. 2025, `10.1016/j.dib.2025.112290` | Painter et al. 2022, `10.1039/D2EM00078D` |

**Consequence:** P3/P4 are a cross-dataset linkage. A defect in either dataset affects the estimand. The two licences also create a D-14 issue for combined derived outputs.

### 3.2 Verified sensor facts

- YSI 6600 sonde; 6025 chlorophyll; 6131 phycocyanin; 6136 turbidity; 6560 temperature; 6565/6561 pH; 6150+ ROX DO.
- Shallow pigments at **0.82 m**; deep sensors at **2.83 m**.
- 15-minute data in 2014; 10-minute data from 2015 to 2021.
- 6025 chlorophyll: **0–100 RFU** (~0–400 µg/L); 6131 phycocyanin: **0–100 RFU**.
- Pigments calibrated at the start and end of seasons with a two-point rhodamine standard; drift reported minimal; no per-record coefficients.
- B7: chlorophyll/phycocyanin/turbidity spike followed by a decrease after a site visit; the *Data in Brief* paper defines the impacted period as the **entire interval between the last maintenance visit and the visit where the issue was identified**.
- No time-zone statement; no date-specific coverage statement; no negative pigment RFU documentation; no >100 RFU processing statement.

### 3.3 Verified biological facts

- 2018: 817 taxonomy rows, 25 dates, 25 `Sample_ID` values.
- 2019: 405 rows, 17 dates, `REP` column, no `Sample_ID`.
- 2019 `REP1`: 12 dates/294 rows; `REP2`: 5 dates/111 rows; disjoint dates.
- 2018: 19 duplicate date–species groups (19 extra rows); 2019: 2 duplicate groups (2 extra rows).
- `Biomass_mg_m3` is arithmetically consistent with `Cell_Volume_um3 × Cell_Density_L × 10^-6` and a density of 1 g cm⁻³; this is arithmetic consistency, not provider confirmation.
- `BP_YSI` profile casts overlap 19/25 biological dates in 2018 and 16/17 in 2019, with times ~10:20–13:33; likely visit times, but the phytoplankton sample time is not documented.

### 3.4 What is confirmed, supported and unresolved

**Confirmed:** dataset identities, authors, licences, sensor models, ranges, B7 semantics, calibration practice, sampling interval, biological dates, duplicate/REP structure, arithmetic form of biomass.

**Supported but not provider-confirmed:** the biomass formula and density; the duplicate rows as processing/counting artifacts; the profile times as visit times; the prior evidence that sensor chlorophyll missed the autumn *Planktothrix* bloom.

**Unresolved:** exact duplicate/`REP` semantics; exact biomass derivation/rounding; B7 retention in the deposited files; negative RFU; >100 RFU; date-specific coverage; time zone; sample times; current FRDR version; record-level calibration; corrections/errata.

---

## 4. Custodian identification

| Role | Person | Evidence | Recommended use |
|---|---|---|---|
| Accountable PI / dataset contact | **Helen Baulch**, Professor, USask SENS | FRDR record/README PI contact; *Data in Brief* first author; `helen.baulch@usask.ca` | Primary recipient |
| Operational data/instrument manager | **Katy Nugent**, GIWS, USask | README co-investigator; lab manager/field technician; `katy.nugent@usask.ca` | Cc |
| Biological corresponding author/contact | **Kristin Painter**, USask/ECCC | Borealis dataset contact; 2022 corresponding author; `kristin.painter@ec.gc.ca` | Cc |
| Co-author / repository contact | **Jason Venkiteswaran**, WLU | Borealis contact; co-author; `jvenkiteswaran@wlu.ca` | Alternate, not primary |
| Co-author / README curator | **Lisa Boyer**, USask | README modified 2025-10-17; co-author | Only if PI delegates |

**Recommended route:** To Helen Baulch; Cc Katy Nugent and Kristin Painter. This covers the buoy QC/instrument questions and the biological replicate/biomass questions without guessing a single custodian.

**No one has confirmed current custody. No one has been contacted.**

---

## 5. What remains unresolved

### 5.1 Buffalo Pound

- Duplicate date–species rows and `REP1`/`REP2` semantics.
- Exact `Biomass_mg_m3` derivation, density, rounding, taxon-level vs sample-level, corrections.
- B7 retention and treatment in the deposited files.
- Negative RFU meaning/treatment.
- Values >100 RFU occurrence/cause/processing.
- Date-specific expected cadence, outages, partial-day handling.
- Time zone and date-boundary convention.
- Phytoplankton sample times.
- Current FRDR version and change history.
- Calibration/maintenance records at record level.
- Corrections/errata.

### 5.2 Mendota

- Numeric H range (none documented).
- G semantics (suspected biofouling, not confirmed invalid).
- O definition (undefined).
- Within-day coverage and sample times.
- Station/depth semantics.

### 5.3 Governance and review

- No independent reviewer appointed.
- No licence/competition review.
- No count audit.
- No D-01–D-14 approvals.
- D-15 not approved.

---

## 6. Scientific reviewer candidates

### 6.1 Shortlist

| Rank | Candidate | Institution | Why | Contact |
|---:|---|---|---|---|
| 1 | **Cayelan C. Carey** | Virginia Tech | Lake sensors, high-frequency data, cyanobacteria, GLEON; can assess sensor interpretation, depth mismatch, endpoint validity, Stage 1 viability | Verified `cayelan@vt.edu` |
| 2 | **Laurence Carvalho** | NIVA | Phytoplankton metrics, eutrophication, cyanobacteria responses, early-warning indicators; strong on ecological meaning and claims | Verified `laurence.carvalho@niva.no` |
| 3 | **Petra M. Visser** | University of Amsterdam | Cyanobacteria physiology, buoyancy, vertical distribution; strong on whether surface fluorescence represents abundance | Verified `P.M.Visser@uva.nl` |
| 4 | **Hans W. Paerl** | UNC Chapel Hill | HAB ecology, nutrients, climate; strong on bloom context and pigment-proxy limits | Verified `Hans_Paerl@unc.edu` |
| 5 | **Bas W. Ibelings** | University of Geneva | Cyanobacteria ecology and automatic high-frequency monitoring | Institutional route only |
| 6 | **Meryem Beklioğlu** | METU | Shallow-lake ecology, climate, phytoplankton/water quality | Institutional route only |
| 7 | **Beatrix E. Beisner** | UQAM | Phytoplankton community ecology, vertical distribution, trophic status | Institutional route only |

### 6.2 Why Carey first

She combines four things the review needs:

1. practical experience with lake sensor networks and high-frequency data;
2. cyanobacteria/lake-ecology expertise;
3. the ability to assess both the measurement design and the ecological claims;
4. a verified professional contact route and no identified direct role in either dataset.

Carvalho is the preferred alternate; Visser is the strongest choice for a cyanobacteria-measurement focus.

**No reviewer has been contacted or appointed.**

---

## 7. Statistical reviewer candidates

### 7.1 Shortlist

| Rank | Candidate | Institution | Why | Contact |
|---:|---|---|---|---|
| 1 | **Mark D. Scheuerell** | USGS / UW | Ecological time series, state-space models, irregular sampling, forecasting; can assess dependence, small n, multiplicity and descriptive claims | Verified `mscheuerell@usgs.gov` |
| 2 | **E. Eli Holmes** | NOAA / UW | Time-series analysis, MARSS, multivariate autoregression, ecological forecasting | Verified `eli.holmes@noaa.gov` |
| 3 | **David I. Warton** | UNSW | Ecological statistics, abundance data, measurement error, zeros/transformations | Verified `david.warton@unsw.edu.au` |
| 4 | **Gavin L. Simpson** | Aarhus / Regina (adjunct) | GAMs, temporal autocorrelation, ecological time series, regime shifts | Public professional email; institutional route |
| 5 | **Peter M. Guttorp** | NR / UW (former) | Environmental statistics, space-time processes, temporal correlation | Verified `peterg@nr.no` |
| 6 | **Christopher K. Wikle** | University of Missouri | Spatio-temporal statistics, autocorrelation, Bayesian hierarchical models | Verified `WikleC@Missouri.edu` |

### 7.2 Why Scheuerell first

He combines:

1. ecological time-series and state-space expertise;
2. direct experience with irregular sampling, dependence and small-sample ecological data;
3. the ability to assess both the statistical design and the honesty of the descriptive claims;
4. a verified professional contact route and no identified direct role in either dataset.

Holmes is the preferred alternate; Warton is the strongest choice for endpoint distribution/measurement-error questions.

**No reviewer has been contacted or appointed.**

---

## 8. Independent review design

The review protocol defines:

- **independence:** no dataset authorship/custody, no current funding/employment/supervision relationship, no direct interest in the result;
- **disclosure:** a conflict-of-interest checklist before materials are sent;
- **separate reviewers:** one scientific, one statistical; a single person only if qualified in both and justified;
- **materials:** the smallest complete package, no raw data, no personal correspondence;
- **outcomes:** acceptable; acceptable with revisions; restrict estimands; exploratory only; pause; reject;
- **issue classification:** fatal, remediable, disclosable;
- **reconciliation:** record disagreements, do not average; adjudicator only for fatal disagreement;
- **reserved decisions:** reviewers advise; they do not approve D-01–D-15 or D-15.

The reviewer package manifest and conflict checklist are prepared. **No materials have been sent.**

---

## 9. Stage 1 viability

### 9.1 Outcome A — all four estimands viable

**Not met.** Requires full custodian evidence, reviewer acceptance of the four-estimand structure, and a licence review. The evidence does not support equal-status P3/P4.

### 9.2 Outcome B — Mendota-only

**Conditionally viable.** Mendota has better documentation, a true biovolume endpoint and a longer record. But the 0.5 m vs 0–8 m depth mismatch, unknown sample times and detection-conditioned population remain serious. It is the defensible fallback if Buffalo Pound cannot be resolved.

### 9.3 Outcome C — reduced two-lake descriptive study

**Recommended in strict form.** P1/P2 are the core; P3/P4 are conditional exploratory appendices. No pooling, no four-estimand validation claim, no equal-status hierarchy. This preserves the comparative context without pretending the lakes are equivalent.

### 9.4 Outcome D — pause

**Use if the custodian/reviewer conditions fail.** Pause is preferable to analysing unresolved data. It is not a failure; it is a legitimate scientific outcome.

### 9.5 Current recommendation

**Proceed to external review and custodian clarification, not to analysis.**

- Retain P1/P2 as the core.
- Retain P3/P4 only as conditional exploratory appendices if custodian evidence arrives.
- Revise the protocol QC section before approval.
- Keep D-15 unapproved until all conditions are met.

**Stage 1 is not ready for analysis. It is conditionally viable as a reduced exploratory audit.**

---

## 10. Originality and prior art

### 10.1 Direct prior art

- **Brient et al. (2008)**, PC probe evaluation, `10.1039/b714238b`.
- **Loisa et al. (2015)**, PC fluorescence to absolute biomass with site-specific calibration, `10.2166/wpt.2015.083`.
- **Kong et al. (2013)**, online PC probe in a reservoir, `10.1007/s10750-013-1759-3`.
- **Hodges et al. (2017)**, manufacturer/temperature/morphology effects on PC fluorescence, `10.1007/s11356-017-0473-5`.
- **Painter et al. (2022)**, Buffalo Pound autumn *Planktothrix* bloom not detected by sensor/lab chlorophyll, `10.1039/D2EM00078D`.

### 10.2 Conclusion

**Low to moderate originality.** The core association method is established. The defensible contribution is a pre-specified non-equivalence audit with explicit negative-result acceptance, not a new sensor-validation method.

**D-13 remains OUTSTANDING — NOT APPROVED.**

---

## 11. Competition suitability

SciFest@College 2027 provisional rules were checked:

- second-level students born after 1 May 2008 in Ireland/NI;
- one project per student; individual or group (max 3);
- report book + visual display;
- plagiarism prohibited;
- external supervision acknowledged;
- participation consent/media release.

No public judging rubric was verified; no criteria were invented.

**Assessment:** scientifically valid only as an exploratory measurement audit; originality low–moderate; technical sophistication moderate (strong provenance/QC, simple statistics); presentation potentially strong if simplified; feasibility moderate (Mendota-core feasible, Buffalo Pound depends on custodian); student contribution must be documented.

**D-14 remains OUTSTANDING — NOT APPROVED.** The two dataset licences differ, and no automatic educational exception is assumed.

---

## 12. Stage 2 and Müggelsee

### 12.1 What is publicly verifiable

- FRED 867: phytoplankton 1979–ongoing, weekly growing season / biweekly ice, Utermöhl microscopy, biomass/biovolume, documented conversion, taxonomic/processor changes, all rights reserved, contact Sabine Hilt.
- FRED 1: weekly multiparameter probe 1978–2019, chl a and phycocyanin, all rights reserved, contact Hilt.
- FRED 1145: high-frequency station 2001–ongoing, 5-min nominal, 1.5 m, chl a and phycocyanin, all rights reserved, contact Tom Shatwell.

### 12.2 Why it is not qualified

- No pre-specified, sensor-independent bloom-event definition.
- No event count or independence check.
- Sensor station M210 is not the phytoplankton stations M3/M5/M7/M8/M10.
- Sensor depth 1.5 m vs integrated 0–4/0–7 m samples.
- No public calibration/QC record.
- All rights reserved; no permission.
- Sampling times and non-bloom exposure not fully documented.

### 12.3 Stage 2 threshold

The original threshold (≥5 years, ≥10 events, weekly microscopy, co-located sensors, non-bloom periods, calibration metadata) should be **strengthened**, not lowered. Add event-definition independence, event independence, non-bloom exposure, sample times, depth matching, spatial co-location, calibration/QC, licence, version history and a negative-control analysis.

**Müggelsee remains a candidate, not a qualified dataset. No new message was sent.**

---

## 13. Adversarial audit

Three personas reviewed the design:

- **Freshwater ecologist:** the sensor is not a biomass measurement; the Mendota depth mismatch is serious; the Buffalo Pound sensor already missed an autumn bloom; the study is a measurement audit, not ecology. Fatal only if presented as validation/ecology.
- **Environmental statistician:** detection-conditioned selection, serial dependence, seasonal confounding and multiplicity are major threats; four estimands and nine sensitivities invite researcher degrees of freedom; a pooled rho alone is not enough. Fatal for inference, remediable for a descriptive audit with a pre-specified hierarchy.
- **Science-fair judge:** low originality; the governance trail is impressive but not a discovery; the student contribution must be clear; a null result is legitimate but harder to present; simplify the poster to one question and one visual.

**Consolidated verdict:** the design survives only as a reduced, exploratory measurement audit. It does not survive as validation, early warning, four equal-status primary estimands, ecological discovery or a novelty-based competition entry.

---

## 14. What changed compared with 4L.18

1. **Custodian identity and routes verified** (Baulch, Nugent, Painter, Venkiteswaran).
2. **Two-dataset provenance resolved**: buoy and biology are separate deposits with different licences and QC.
3. **Biomass arithmetic confirmed** as consistent with cell volume × cell density × 10⁻⁶ and 1 g cm⁻³; provider derivation still unconfirmed.
4. **Duplicate/REP structure quantified**: 19 duplicate groups in 2018; 2 in 2019; REP1/REP2 disjoint.
5. **B7 exact interval confirmed**: entire period between maintenance visits; caution, not removal.
6. **Calibration practice confirmed**: start/end season, two-point rhodamine; no per-record coefficients.
7. **Buffalo Pound sample times partially recovered**: BP_YSI profiles suggest midday visits on most dates; phytoplankton sample time still unconfirmed.
8. **Protocol inconsistency identified**: §10 QC rules conflict with D-05 evidence; formal revision required.
9. **Müggelsee evidence strengthened**: FRED 867/1/1145 details verified; Stage 2 candidate, not qualified.
10. **Reviewer candidates identified and verified**: 7 scientific, 6 statistical; no appointments.
11. **Prior art sharpened**: Brient 2008, Loisa 2015, Kong 2013, Hodges 2017, Painter 2022; originality low–moderate.
12. **Competition rules rechecked**: SciFest 2027 eligibility/report/display/plagiarism/supervision; no judging rubric invented.

---

## 15. What did not change

- Research direction: **CONTINUE — NARROWED RESEARCH QUESTION**.
- Protocol: **PROPOSED — NOT APPROVED**.
- Gate 2: **PAUSED / NOT APPROVED — OPTION C (EXPLORATORY ONLY)**.
- D-01–D-15: **OUTSTANDING — NOT APPROVED**.
- D-15: **NOT APPROVED**.
- Analysis: **NOT AUTHORISED**.
- No analysis, count audit, correlations, labels, event intervals, derived datasets, models, hypothesis tests or threshold optimisation.
- No data acquisition/upload.
- No emails, reviewer invitations, custodian contact or Gmail drafts were sent in this sprint. (The earlier Müggelsee enquiry remains the only external message recorded in the project.)
- No commits or pushes.
- Historical packages and decision records were read, not modified.

---

## 16. Integrity verification

The package has a SHA-256 register covering every content file, a detached checksum for the register, and a separate `INTEGRITY_VERIFICATION.md`. The exact file count and register hash are recorded there and in `EVIDENCE_SHA256_REGISTER.csv.sha256`.

Historical package checks were also re-run. The exact results are recorded in `INTEGRITY_VERIFICATION.md`.

**This verifies package integrity, not the truth of the underlying evidence.**

---

## 17. Exact verification commands

From the package directory:

```bash
cd /Users/cedricbw/Documents/EcoSentinel/research/evidence/sprint_4l19_external_engagement_preparation
shasum -a 256 -c EVIDENCE_SHA256_REGISTER.csv.sha256
```

Verify every registered file:

```bash
cd /Users/cedricbw/Documents/EcoSentinel
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
base = Path('research/evidence/sprint_4l19_external_engagement_preparation')
bad = 0
for row in csv.DictReader(open(base/'EVIDENCE_SHA256_REGISTER.csv', newline='', encoding='utf-8')):
    p = Path(row['path'])
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
        bad += 1
        print('MISMATCH', row['path'])
print('mismatches', bad)
PY
```

Verify historical packages:

```bash
cd /Users/cedricbw/Documents/EcoSentinel
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
for pkg in ['sprint_4l16_human_review_preparation','sprint_4l17_human_review_continuation','sprint_4l18_human_review_and_qc_resolution','strategic_reconstruction_original_goal_2026_11_25','strategic_reconciliation_and_muggelsee_enquiry_2026_11_25']:
    base=Path('research/evidence')/pkg
    reg=base/'EVIDENCE_SHA256_REGISTER.csv'
    if not reg.exists():
        print(pkg,'NO REGISTER'); continue
    bad=0; n=0
    for row in csv.DictReader(open(reg,newline='',encoding='utf-8')):
        p=Path(row['path']); n+=1
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:
            bad+=1; print('MISMATCH',row['path'])
    print(pkg,'rows',n,'mismatches',bad)
PY
```

---

## 18. Single most defensible next action

**Obtain written human authorisation to send the prepared Buffalo Pound custodian enquiry to Professor Helen Baulch, copied to Katy Nugent and Dr Kristin Painter.**

Why this action:

- It addresses the highest-priority blocker (D-05/D-02/D-08).
- It uses verified professional routes and a concise, answerable email.
- It does not require analysis, data acquisition or a governance change.
- It produces the evidence needed to decide whether P3/P4 can be retained or must be dropped.
- It is a prerequisite for a meaningful independent review of the two-lake design.

Do **not** finalise D-05/D-06, do **not** approve D-15 and do **not** start analysis while waiting.

---

## 19. Limitations

- The full Painter et al. (2022) methods were not accessible (RSC 403; ESSOAr/Authorea challenge pages).
- The FRDR newer-version record returned 404; the current version is ambiguous.
- Some institutional profiles were inaccessible (UNIGE, USGS, Griffith); identity was verified via ORCID where possible.
- No reviewer has been contacted; no willingness or availability is assumed.
- No custodian has replied; no custody is confirmed.
- The prior-art search was targeted, not systematic; absence of a direct Mendota study is not proof of novelty.
- The Müggelsee data files are access-restricted; only metadata were inspected.
- No analysis was performed, so all statements about associations are about the proposed design, not observed results.

**End of report.**
