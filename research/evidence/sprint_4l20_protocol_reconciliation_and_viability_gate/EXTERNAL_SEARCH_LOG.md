# External Search Log — Sprint 4L.20

**Sprint:** 4L.20  
**Date:** 2026-11-26  
**Scope:** Protocol reconstruction and contradiction detection; Mendota standalone evidence; Buffalo Pound Stage 1 value; originality/prior art; competition; Stage 2 requirements.  
**Status:** Search completed for the sources accessible in this environment. **No external contact was made. No analysis or count audit was performed.**

---

## 1. Method

The sprint prioritised:

1. the actual protocol and its supporting documents;
2. the actual dataset metadata (NTL-LTER EML, Buffalo Pound README/Data in Brief, Borealis/FRDR records);
3. independent reviews and later evidence packages;
4. primary literature and prior art;
5. official competition rules;
6. Stage 2 metadata (FRED).

Historical summaries were not treated as substitutes for the underlying documents. Where a document was inaccessible, the limitation is recorded.

---

## 2. Protocol reconstruction

### 2.1 Sources inspected

- `sprint_4l14_protocol_revision/REVISED_PROTOCOL.md` — full relevant sections: question, design, estimands, eligibility, endpoints, sensors, matching, QC, statistics, uncertainty, claims, governance.
- `sprint_4l14_protocol_revision/QC_AND_MISSINGNESS_RULES.md` — full.
- `sprint_4l14_protocol_revision/ESTIMAND_AND_SAMPLE_ELIGIBILITY_SPECIFICATION.md` — full.
- `sprint_4l14_protocol_revision/REVISED_RESEARCH_QUESTION.md` — full relevant sections.
- `sprint_4l14_protocol_revision/UPDATED_HUMAN_DECISION_REGISTER.md` — D-01–D-15.
- `sprint_4l13_independent_protocol_challenge/FINAL_REVIEW_RECOMMENDATION.md` — full.
- `sprint_4l14_codex_independent_review/INDEPENDENT_REVIEW_EXECUTIVE_REPORT.md`, `COMPETITION_VIABILITY_ASSESSMENT.md`, `RESEARCH_QUESTION_AND_SCIENTIFIC_VALUE_REVIEW.md`.
- `strategic_reconciliation_and_muggelsee_enquiry_2026_11_25/SPRINT_4L14_REVIEW_ADDENDUM.md` — F-01–F-13.
- `sprint_4l16/17/18/19` decision/QC/provenance/viability packages.

### 2.2 Findings

- The current proposed protocol is 4L.14, but it is internally inconsistent and contradicted by the 4L.14 addendum and 4L.18/19 evidence.
- The main contradictions are H retention, B7 exclusion, negative RFU retention, >100 RFU retention, coverage rule, P3/P4 status, biomass certainty, station rule, sensor-era wording, P1/P2 hierarchy, YSI era, daily mean/sample time, detection-conditioned population, Buffalo Pound duplicates, licence and the 2006–2020 window.
- The contradiction map is in `PROTOCOL_CONTRADICTION_MAP.csv`; the QC disposition is in `QC_RULE_RECONCILIATION.md`.

### 2.3 Inaccessible/limited

- The 4L.14 protocol is not a single approved document; the addendum is not applied.
- No formal protocol v2 exists.

---

## 3. Mendota evidence

### 3.1 Sources inspected

- NTL-LTER daily sensor EML `knb-lter-ntl.129.42`.
- NTL-LTER phytoplankton EML `knb-lter-ntl.88.31`.
- 4L.9 QC flag audit.
- 4L.10 independent Mendota verdicts and prior-art review.
- 4L.5 depth/sampling and endpoint assessments.
- 4L.19 Stage 1 viability/originality/adversarial reviews.

### 3.2 Findings

- Sensors: 0.5 m; Turner 2006–2019; YSI 2019–2020.
- Biology: 0–8 m tube composite on 400/402 dates; 2 at 0–2 m; biweekly ice-free, monthly autumn, once winter; date-only.
- 128 Turner chlorophyll / 139 Turner phycocyanin same-day unflagged upper bounds.
- Station blank for 371/402; 31 station-1 dates; ~106 m buoy offset.
- Taxonomy non-stationary; no detection limits; 4 negative Turner phycocyanin values.
- H: 54 Turner chlorophyll / 41 Turner phycocyanin; no numeric range.
- C: 316 Turner chlorophyll C flags; numeric C exists.
- G: no Turner pigment G flags.
- Mendota NTL data are CC BY 4.0.
- The NTL biology is biweekly, not weekly; it cannot support daily EWS.

### 3.3 Inaccessible/limited

- No depth-resolved biology.
- No sample times or within-day sensor counts.
- No H numeric range.
- No provider statement on negative RFU.
- No actual n/count audit.

---

## 4. Buffalo Pound evidence

### 4.1 Sources inspected

- 4L.19 provenance investigation.
- FRDR record/README.
- Borealis record/README.
- Data in Brief 2025.
- Painter et al. 2022.
- 4L.18 D-05.
- 4L.14 addendum F-01/F-02/F-09.

### 4.2 Findings

- Two separate datasets: buoy (FRDR, CC BY 4.0) and biology (Borealis, CC BY-NC-SA 4.0).
- Biomass arithmetic consistent; exact field derivation unconfirmed.
- 2018 19 duplicate groups; 2019 2; REP1/REP2 disjoint.
- B7 caution interval, not removal.
- Negative/>100 RFU, coverage, time zone, sample times unresolved.
- Custodian not contacted; no response.

### 4.3 Consequence

Buffalo Pound is removed from Stage 1. It is preserved as future/Stage 2 context.

---

## 5. Originality and prior art

### 5.1 Search routes

- OpenAlex works search for Cotterill/PC/CHL sensor terms.
- Europe PMC for O’Brien, Levi, PC sensor terms.
- Crossref (rate-limited; 429).
- 4L.10 prior-art review.
- 4L.19 prior-art review.

### 5.2 Key discoveries

- **Cotterill et al. (2019)**, `10.1080/00288330.2019.1617322`: Cyclops-7 PC vs cyanobacteria biovolume across five lakes and a river; weak (<R²=0.4) and variable; limited utility. This is the closest direct prior art and was not fully weighted in 4L.19.
- **2018 combined CHL/PC sensors**, `10.14720/abs.61.2.15891`: CHL+PC vs biovolume; high correlation; false PC positives.
- **2017 PC fluorescence vs biomass**, `10.14720/abs.60.2.15683`: linear but strain-variable; biovolume best target.
- **Loisa et al. (2015)**, `10.2166/wpt.2015.083`: PC vs microscopy biomass; positive correlation; site-specific calibration.
- **Brient et al. (2008)**, `10.1039/b714238b`; **Kong et al. (2013)**, `10.1007/s10750-013-1759-3`; **Hodges et al. (2017)**, `10.1007/s11356-017-0473-5`; **Levi et al. (2024)**, `10.12688/openreseurope.17146.3`.
- **Painter et al. (2022)**, `10.1039/D2EM00078D`: sensor/lab chlorophyll missed autumn *Planktothrix*.
- **O’Brien et al. (2023)**, `10.1038/s41467-023-43744-8`: EWS limited applicability.
- **Carpenter et al. (2022)**, `10.1073/pnas.2214343119`: Mendota daily PC, nighttime means.
- **Carpenter et al. (2020)**, **Beal et al. (2021/2022)**: identified via 4L.10, DOI not verified in this sprint.

### 5.3 Inaccessible/limited

- Cotterill full text not accessed; abstract/metadata used.
- RSC Painter full text 403; abstract/dataset methods used.
- Crossref 429; queries reduced/paused.
- Some 2017/2018 Slovenian papers are in a journal with limited indexing; abstracts via OpenAlex.
- No systematic review; targeted search only.

### 5.4 Consequence

Originality is **low**, lower than the 4L.19 “low–moderate” verdict. The proposed Mendota P2/P1 audit is a local case study.

---

## 6. Competition

### 6.1 Sources inspected

- SciFest@College 2027 entry rules page.
- Provisional 2027 student rules PDF.
- 4L.19/strategic reconciliation SciFest feasibility notes.

### 6.2 Findings

- Entry deadline 11 March 2027; fairs April–June 2027.
- Second-level students born after 1 May 2008; one project; individual/group max 3.
- Report book + visual display; plagiarism prohibited; external supervision acknowledged; media release.
- No public judging rubric.
- No automatic licence exception.

### 6.3 Inaccessible/limited

- Venue not recorded.
- Entrant DOB not recorded.
- No official judging rubric.

---

## 7. Stage 2

### 7.1 Sources inspected

- FRED 867, FRED 1, FRED 1145 records (4L.19 evidence).
- 4L.19 Stage 2 reassessment/checklist.
- 4L.10 prior-art review.

### 7.2 Findings

- Müggelsee is the strongest public candidate: weekly microscopy 1979–, weekly probe 1978–2019, high-frequency sensors 2001–.
- All rights reserved; no permission.
- Sensor station/depth differ from biological stations; no event definition/calibration/QC public.
- Mendota biology is biweekly; Buffalo Pound two seasons.
- No Stage 2 dataset qualified.

### 7.3 Inaccessible/limited

- FRED data files access-restricted.
- No reply to Müggelsee enquiry recorded.
- No event audit.

---

## 8. What was not done

- No external contact, email, reviewer invitation or custodian enquiry.
- No data acquisition/upload.
- No analysis, count audit, correlation, model, label, event interval or derived dataset.
- No Git commit/push.
- No modification of historical protocols/registers.

---

## 9. Stop rule

Search stopped when:

- the protocol and its contradictions were fully mapped;
- the key dataset metadata were inspected;
- the prior art was sufficient to lower the originality verdict;
- the competition rules were verified;
- the Stage 2 candidate limitations were documented;
- remaining gaps were explicitly external (reviewers, custodian, count audit, licence, access).

Further searching would not change the decision without new external evidence.

---

## 10. Verdict

The search supports the 4L.20 decision:

- the current protocol cannot be approved as written;
- Buffalo Pound should be removed from Stage 1;
- Mendota can stand alone only as a limited exploratory audit;
- originality is low;
- competition suitability is modest;
- Stage 2 remains unqualified.

**No analysis was performed. No decision was approved.**
