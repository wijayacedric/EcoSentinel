# Gate 2 — 2017–2019 Integrated Evidence Assessment and Confirmatory Feasibility Review

**Project:** EcoSentinel — Detecting Early Changes in Freshwater Ecosystems Using Multivariate Time-Series Analysis  
**Research question:** "Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?"  
**Primary dataset:** Buffalo Pound Lake, Saskatchewan, Canada (DOI: 10.20383/103.01100; Baulch et al. 2025, DOI: 10.1016/j.dib.2025.112290)  
**Status:** Definitive integrated Gate 2 human-review document. **Gate 2 is NOT approved.**  
**Date:** 2026-11-22  
**Authoring agent:** OpenCode (bounded reconciliation; no new literature search; no new downloads/retrieval attempts)  
**Scope:** Reconciliation of existing repository evidence only. No outcome labels created. No modeling performed. No raw data modified. No research question or primary dataset changed. No Gate 4 activity.

---

## 1. Executive verdict

**Overall feasibility classification: Exploratory only.**

The existing evidence can support descriptive or exploratory analysis of 2017–2019 biological observations in relation to the Buffalo Pound buoy record, but it **does not support the original confirmatory claim**: earlier warning than conventional monitoring at comparable false-alarm rates.

**Key reasons:**
- **No independently reconstructed event evidence from accessible raw data.** Boyer et al. (2025) reports 2017 biological sampling and published bloom phases, but phase boundaries were partly informed by buoy observations and the original biological measurements are not accessible raw data in this project. Painter et al. (2022) provides independent microscopy measurements as publication/dataset records, but the raw CSVs are not present in the repository at reconciliation time; only dates/summaries recorded in prior assessments are available here.
- **Independent event count is not determinable as a defensible confirmatory count.** Sampling dates, taxa, candidate phases, and published phases cannot be counted as independently established bloom events. From accessible evidence in-repo, **0 independently reconstructed biological bloom events** can be confirmed.
- **Independent non-bloom exposure cannot be established.** Unsampled gaps, missing years, unverified periods, and sensor-only classifications cannot be counted as confirmed non-bloom time. Therefore matched false-alarm-rate (FAR) evaluation is not currently defensible.
- **Lead-time precision is insufficient for a confirmatory claim.** Boyer 2017 sampling is ~5-day discrete sampling; Painter 2018/2019 has 1–16 day gaps and an unresolved 2019-07-17 anomaly. A claimed lead-time improvement of a few days cannot be reliably distinguished from biological reference-timeline uncertainty.
- **Statistical precision/power is not defensible.** The number of independent events and confirmed non-bloom exposure is insufficient/undefined for confirmatory inference; no quantitative power calculation is fabricated.

**Gate 2 remains blocked.** Human review is required before any Gate 2/3 approval, any outcome definition, or any Gate 4 work.

---

## 2. Research question and scope

**Research question (unchanged):** "Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?"

**Primary dataset (unchanged):** Buffalo Pound Lake buoy/meteorological dataset, 2014–2021 (FRDR DOI 10.20383/103.01100; Baulch et al. 2025, DOI 10.1016/j.dib.2025.112290).

**Scope of this assessment:** Bounded reconciliation of existing Gate 2 materials in `/Users/cedricbw/Documents/EcoSentinel`, including `research/reports/GATE2_FINAL_EVIDENCE_ACQUISITION.md`, `research/research_notes/GATE2_BLOOM_EVIDENCE_REGISTER.md`, and `research/research_notes/GATE2_ESCALATION_ASSESSMENT_2026-11-22.md`. No broad literature search, no repeated failed downloads, no label creation, no modeling, no raw-data modification.

---

## 3. Evidence-status definitions

The following distinctions are mandatory for this reconciliation:

| Status | Definition | What it can support | What it cannot support |
|---|---|---|---|
| **Publication-level evidence** | What a published study reports observing, interpreting, or concluding. | Context, reported sampling design, reported measurements, reported phase descriptions; hypothesis generation. | Independent reconstruction without accessible data/methods; confirmed continuous event periods; raw-data reproduction claims. |
| **Accessible raw evidence** | Original biological/chemical measurements actually available for inspection in this project (files, tables, records, SI data). | Verification of dates, values, methods, units, sample identities; possible reconstruction under approved criteria. | Claims about data not present/inspected. |
| **Independently measured evidence** | Measurements obtained through methods independent of the buoy predictor variables being evaluated (e.g., microscopy, lab toxin assays, lab chl-a by independent method), even if collected near buoy. | Candidate biological observations for event reconstruction, subject to access and criteria. | Automatic event labels; independence of phase boundaries if buoy context informed them. |
| **Independently reconstructed event evidence** | Event periods established using predefined biological criteria applied to accessible independent measurements, without relying on predictor signals being evaluated. | Defensible event windows for confirmatory evaluation, if criteria pre-approved and uncertainty handled. | Any claim before criteria approval, data access, and reconstruction audit. |
| **Contextual evidence** | Public-health advisories, operational records, sensor-derived classifications, news reports, and other supporting information that cannot independently establish biological bloom status. | Context, prioritization for evidence acquisition, exploratory interpretation. | Confirmed biological bloom/non-bloom labels; FAR denominators; confirmatory event truth. |

**Additional rule:** A candidate interval is never a confirmed continuous bloom period unless the accessible evidence and pre-approved criteria support that conclusion. Unsampled gaps remain unknown/censored.

---

## 4. Reconciled source assessment

| Source | Publication-level evidence | Accessible raw evidence in project | Independently measured? | Independently reconstructed event evidence? | Status | Use |
|---|---|---|---|---|---|---|
| Baulch et al. 2025, *Data in Brief* 63:112290; DOI 10.1016/j.dib.2025.112290; PMC12720111 | Primary buoy dataset description; RFU pigment proxy limitations; 2014–2021 context. | Dataset paper metadata/content as previously accessed; raw buoy data in project not re-audited here. | Contextual; buoy sensors are predictors/proxies. | No. | Reconciled. | Context only. |
| Boyer et al. 2025, *Freshwater Biology* 70:e70131; DOI 10.1111/fwb.70131 | Reports 2017 Buffalo Pound Lake study; 15 discrete biological sampling dates DOY 190–264 (~every 5 days, 10 Jul–21 Sep 2017); phytoplankton ID/enumeration/biovolume/heterocyte biovolume, chl-a, nutrients, N2 fixation (ARA/15N2), ammonium uptake; published pre-bloom DOY 187–212, major bloom DOY 213–238 (primary 215–222, secondary 226–233), post-bloom DOY 239–264. | **No.** SI download failed in prior session; underlying biological data not obtained; no raw biological measurements available in repository. | Biological measurements are described as independent methods; buoy observations were also used and informed phase interpretation. | **No.** Published phases are not independently reconstructed ground truth. | Reconciled with mandatory corrections. | Publication-level biological/context evidence only; no event labels. |
| Painter et al. 2022, *Environ. Sci.: Processes Impacts* 24:1212–1227; DOI 10.1039/D2EM00078D | Reports 2018 and 2019 microscopy-based cyanobacterial bloom phases in Buffalo Pound Lake. | **Not present in repository at reconciliation time.** Prior assessment recorded examining Borealis/GitHub CSVs; those files are not available in-repo now. | Microscopy/taxonomy/biomass described as independent of buoy RFU predictors. | **No.** No pre-approved criteria; no in-repo raw data for reconstruction audit; sparse interval-censored sampling. | Reconciled with mandatory corrections. | Publication-level/priorly examined dataset evidence; candidate intervals only. |
| Painter et al. 2022 dataset, Borealis DOI 10.5683/SP3/MP6NXF; GitHub commit `176ff61768f1e5e5d485b53b72c68c8f287ca83f` | Dataset metadata and files previously examined per escalation assessment. | **No local copy verified in repository.** | Microscopy/toxin lab files described as independent measurements. | No. | Unavailable locally; provenance recorded from prior assessment. | Cannot be independently re-verified in this reconciliation. |
| Painter et al. 2023, *Ecosphere* 14:e4472; DOI 10.1002/ecs2.4472 | Buoy phycocyanin GAM bloom classification 2014–2020. | Not needed; classification is sensor-derived by design. | **No.** Uses buoy phycocyanin/sensor data. | No. | Reconciled. | Context/sensitivity comparator only; never ground truth. |
| WSA 2015 notice; CBC 2016 advisory | Public operational/public-health signals. | Web pages/news not stored as raw evidence package. | Not biological confirmation. | No. | Contextual. | Context only. |
| BPWTP/WSA/Boyer 2021 thesis/other records | Potentially relevant. | Not obtained/verified. | Unknown. | No. | Unverified. | Not evidence. |

---

## 5. Evidence-level timelines

### 5.1 2017 season (Boyer et al. 2025 — publication-level evidence)

| Item | Details | Evidence status | Independence from buoy predictors | Temporal resolution supported |
|---|---|---|---|---|
| Actual biological sampling dates | 15 discrete surface-water samples reported ~every 5 days between **DOY 190–264 (10 Jul–21 Sep 2017)**. One archived BPWTP intake phytoplankton sample replaced missing 0.3 m sample on **DOY 212** (reported). | Publication-level reported dates; no accessible raw sample table in repo. | Sampling/assays described as biological/chemical methods independent of buoy RFU measurement method; sample location adjacent to buoy/long-term site. | Discrete dates at ~5-day intervals; no continuous daily biological observation. |
| Measurements reported | Phytoplankton identification, enumeration, biovolume, heterocyte biovolume (Plankton R Us); chl-a; NH4+, NO3/NO2, SRP, TDP, TP; N2 fixation by 15N2-calibrated ARA and 15N2-tracer; ammonium uptake on 5 occasions. Scums sampled on 4 shoreline dates (DOY 222–250). | Publication-level. | Biological/chemical lab/assay measurements: independent of buoy RFU as measurement method. Buoy sensors also used in study: not independent. | Per-sample/assay; scums intermittent. |
| Published phase descriptions | Pre-bloom **DOY 187–212 (Jul 6–31)**; major bloom **DOY 213–238 (Aug 1–26)**; primary bloom **DOY 215–222**; secondary bloom **DOY 226–233**; post-bloom **DOY 239–264 (Aug 27–Sep 21)**. | Publication-level reported interpretation. | **Not exclusively independent biological measurements.** Buoy observations informed study interpretation; boundaries partly buoy/sensor-informed. | Phase labels as reported; boundary precision not defensible as independent ground truth. |
| Candidate event intervals | None independently reconstructed. Published phases may be *candidates for reconstruction only* if accessible raw biological data are obtained and pre-approved biological-only criteria are applied. | Not reconstructed. | Mixed. | Cannot support precise onset/termination/lead time. |
| Unknown/censored periods | DOY 187–189 before first biological sample (pre-bloom start is 3 days before first biological sample); all intervals between ~5-day samples; periods outside DOY 187–264; all other 2017 dates not biologically sampled. | Unknown/censored. | N/A. | Gaps of ~5 days or more; boundary uncertainty spans days. |
| Supported temporal resolution | Discrete ~5-day biological snapshots within DOY 190–264; published phase boundaries are interpretive and buoy-informed. | — | — | **Insufficient for precise onset, termination, duration, or few-day lead-time claims.** |

**Mandatory Boyer 2025 corrections applied:** pre-bloom starts DOY 187, three days before first biological sample (DOY 190). Post-bloom ends DOY 264, the last reported biological sampling date. Published phase boundaries were not established exclusively through independent biological measurements; buoy observations also informed interpretation. Original biological measurements have not been obtained as accessible raw data in this project. Published phases are **not** independently reconstructed ground truth; raw observations have **not** been independently reproduced.

### 5.2 2018 season (Painter et al. 2022 — publication-level/priorly examined dataset evidence)

| Item | Details | Evidence status | Independence from buoy predictors | Temporal resolution supported |
|---|---|---|---|---|
| Actual biological sampling dates | 25 microscopy sampling dates reported in prior examined dataset files (not present in repo at reconciliation): 2018-05-29, 06-07, 06-13, 06-19, 06-21, 06-25, 07-03, 07-06, 07-09, 07-12, 07-16, 07-18, 07-24, 07-25, 07-30, 07-31, 08-08, 08-09, 08-14, 08-17, 08-21, 08-23, 08-28, 09-05, 09-17. | Prior assessment from examined files; local raw CSV unavailable. | Microscopy/taxonomy/biomass described as independent method. | Discrete dates; gaps 1–12 days. |
| Measurements reported | Phytoplankton species ID, cell density, biomass (mg/m3), cell dimensions/volume, taxonomic grouping; group biomass files; toxin/cyanopeptide files; nutrients/YSI as per dataset metadata. | Publication/priorly examined dataset-level. | Microscopy independent. Toxin files potentially independent lab measurements but **unverified format/units/sample identity/interpretation**. | Per sampled date. |
| Published phase descriptions | Mid-summer diazotrophic *Dolichospermum* spp. and autumn *Planktothrix agardhii* bloom phases reported (publication-level). | Publication-level. | Descriptive biological interpretation; not an approved event reconstruction. | Interval-censored only. |
| Candidate event intervals | Possible candidate intervals only around sampled high-cyanobacterial-biomass dates, if pre-approved criteria are later applied to accessible raw data. **No continuous confirmation between samples.** | Not reconstructed. | Potentially independent if based on microscopy only. | Bounded by adjacent sample gaps; no onset/termination precision. |
| Unknown/censored periods | All days between samples; before 2018-05-29; after 2018-09-17 (right-censored); any unsampled period. | Unknown/censored. | N/A. | Gap-dependent uncertainty. |
| Supported temporal resolution | Point observations on 25 dates. | — | — | **Cannot support precise onset, termination, duration, or few-day lead-time claims.** |

### 5.3 2019 season (Painter et al. 2022 — publication-level/priorly examined dataset evidence)

| Item | Details | Evidence status | Independence from buoy predictors | Temporal resolution supported |
|---|---|---|---|---|
| Actual biological sampling dates | 17 microscopy sampling dates reported in prior examined dataset files (not present in repo at reconciliation): 2019-05-29, 06-03, 06-12, 06-19, 07-05, 07-10, 07-17, 07-29, 08-07, 08-15, 08-21, 08-30, 09-03, 09-13, 09-17, 09-26, 10-03. | Prior assessment from examined files; local raw CSV unavailable. | Microscopy/taxonomy/biomass described as independent method. | Discrete dates; gaps 4–16 days. |
| Measurements reported | Same measurement types as 2018 per dataset metadata/prior assessment. | Publication/priorly examined dataset-level. | Microscopy independent. Toxin files unverified. | Per sampled date. |
| Published phase descriptions | Early/mid-summer cyanobacteria and autumn *Planktothrix agardhii* phases reported (publication-level). | Publication-level. | Descriptive; not approved reconstruction. | Interval-censored only. |
| Candidate event intervals | Possible candidate intervals only with pre-approved criteria and accessible raw data. **No continuous confirmation between samples.** | Not reconstructed. | Potentially independent if microscopy-only. | Large gaps create wide bounds. |
| Unknown/censored periods | All days between samples; before 2019-05-29; after 2019-10-03; 2019-07-17 anomaly period unresolved. | Unknown/censored/uncertain. | N/A. | 12-day gap around anomaly (07-10 to 07-29) is especially ambiguous. |
| Supported temporal resolution | Point observations on 17 dates. | — | — | **Cannot support precise onset, termination, duration, or few-day lead-time claims.** |

**Mandatory Painter 2022 corrections applied:** actual discrete sampling dates are distinguished from broader candidate/published phase descriptions; no period between two samples is treated as continuously confirmed; 2018 and 2019 timelines are kept separate; 2019-07-17 anomaly remains unresolved; toxin records are not used as confirmed evidence.

### 5.4 2019-07-17 anomaly (unresolved)

- **Observation (priorly recorded from examined Painter 2022 files):** 2019-07-17 (DOY 198) sample: total biomass 45.8 mg/m3, cyanophyte 41.0 mg/m3 (89.5%), 9 taxa rows, `REP2`. Neighboring dates: 2019-07-10 total 12587.1 mg/m3 (cyano 11919.8, 94.7%); 2019-07-29 total 9497.9 mg/m3 (cyano 6755.2, 71.1%).
- **Toxin file note:** Prior assessment noted 2019-07-17 records in `BP_2019_toxins_0.8.csv`; format/units/sample identity/interpretation not verified in this reconciliation. **Not confirmed evidence.**
- **Status:** **Unresolved anomaly.** Possible explanations include patchiness, replicate handling, field/lab processing, data-entry/subset issue, or real short-lived change. It must not be treated as bloom termination, recovery, or non-bloom.

---

## 6. Independent evidence versus contextual evidence

| Evidence | Class | Can establish biological bloom status? | Can establish non-bloom exposure? | Can support confirmatory FAR/lead-time comparison? | Notes |
|---|---|---|---|---|---|
| Boyer 2025 biological/chemical assays (as reported) | Independently measured method, publication-level; not accessible raw in project | Potentially, only after raw data access + pre-approved biological-only reconstruction | No, not without approved criteria and complete exposure accounting | No | Phase boundaries buoy-informed; raw data inaccessible. |
| Boyer 2025 published phase boundaries | Publication-level interpretation; partly buoy-informed | No | No | No | Not independently reconstructed ground truth. |
| Painter 2022 microscopy measurements (as reported/priorly examined) | Independently measured method; local raw files unavailable at reconciliation | Potentially, only after accessible data verification + approved criteria | No | No | Sparse interval-censored point observations. |
| Painter 2022 toxin files | Potentially independent lab chemical measurements; unverified | Not until formats/units/sample identities/interpretation verified | No | No | Do not use as confirmed bloom evidence. |
| Painter 2023 GAM phycocyanin classifications | Contextual/sensor-derived | No | No | No | Not independent of buoy predictors. |
| Buoy chl-a/phycocyanin RFU | Contextual/sensor-derived predictor/proxy | No | No | No | RFU proxies; same system as predictors. |
| WSA 2015 notice / CBC 2016 advisory | Contextual public-health/operational signal | No | No | No | No species/counts/toxins/precise dates. |
| BPWTP/WSA internal records | Unverified | Unknown until obtained and verified | Unknown | Unknown | Not accessible in this reconciliation. |

---

## 7. Unresolved anomalies and limitations

1. **Boyer 2025 raw data inaccessible:** SI download failed in prior session; underlying biological measurements not obtained. Publication-level evidence cannot be independently reproduced in this project.
2. **Boyer 2025 phase-boundary independence:** Pre-bloom starts DOY 187, 3 days before first biological sample (DOY 190). Phase boundaries were informed by buoy observations and are not independently reconstructed ground truth.
3. **Painter 2022 local raw data unavailable:** CSVs previously examined are not present in repository at reconciliation time; dates/summaries are carried forward with provenance caveat.
4. **Sampling sparsity/interval censoring:** Boyer ~5-day intervals; Painter 1–16 day gaps. No continuous biological observation. Onset/termination/duration uncertain.
5. **2019-07-17 anomaly:** Unresolved; cannot be interpreted as termination/recovery/non-bloom.
6. **Toxin records unverified:** Painter toxin files not confirmed for format, units, sample identity, or interpretation.
7. **Coverage gap:** 2014–2016, 2020–2021 have no verified independent biological event records in this register.
8. **No approved event definition:** No Gate 2/3-approved biological criteria, persistence rule, censoring rule, or non-bloom exposure rule.
9. **No confirmed non-bloom exposure:** Unsampled intervals and missing years cannot be treated as non-bloom.
10. **No confirmatory evaluation design approved:** Splits, FAR targets, baselines, and matched operating points are not approved.

---

## 8. Confirmatory feasibility assessment

### A. Independent event count

**Question:** How many distinct biological bloom episodes can actually be established from the accessible evidence?

**Assessment:**
- **Boyer 2017:** 15 sampling dates are reported (publication-level). Published phases (pre/major/primary/secondary/post) are not independently reconstructed event evidence; boundaries are buoy-informed and raw data are inaccessible. Therefore, published phases cannot be counted as independently established bloom events. **Independently reconstructed events from accessible evidence: 0.**
- **Painter 2018:** 25 sampling dates reported in prior examined files; local raw files unavailable. No pre-approved biological event definition. Discrete high-biomass samples do not equal independently established events. **Independently reconstructed events from accessible evidence: 0.**
- **Painter 2019:** 17 sampling dates, including unresolved 2019-07-17 anomaly; local raw files unavailable. **Independently reconstructed events from accessible evidence: 0.**
- **Total independently established biological bloom events from accessible evidence: 0 (determinable as zero confirmed/reconstructed; candidate phases exist but are not established events).**

**Do not confuse:** sampling dates (15/25/17) ≠ samples ≠ taxa ≠ candidate phases ≠ independently established bloom events. The event count is **insufficient for a credible confirmatory evaluation**.

### B. Non-bloom exposure

**Question:** How much time can genuinely be classified as independently observed non-bloom exposure?

**Assessment:** **None can be defensibly classified as confirmed non-bloom exposure for confirmatory FAR estimation.** 
- Unsampled gaps between Boyer samples (~5 days) are unknown.
- Intervals between Painter samples (1–16 days) are unknown.
- Periods before/after seasonal sampling are unknown/censored.
- Missing years (2014–2016, 2020–2021) are unknown, not non-bloom.
- Sensor-only classifications (Painter 2023, buoy RFU) are not independent biological evidence.
- Low-biomass point observations are not approved non-bloom labels.

**Implication for FAR:** False-alarm rate requires a defensible denominator of non-event exposure or an explicitly justified exposure model. With no confirmed non-bloom exposure, matched FAR comparison cannot be estimated fairly. Any FAR computed over unlabeled/unknown periods would be scientifically invalid.

### C. Lead-time precision

**Question:** Do sampling frequency and event-boundary uncertainty allow meaningful lead-time estimates?

**Assessment:** **No, not for a confirmatory claim of a few days' improvement.**
- Boyer 2017: ~5-day sampling interval; pre-bloom boundary starts DOY 187, three days before first biological sample. Event onset/transition timing is uncertain by multiple days.
- Painter 2018: 1–12 day gaps; end-of-season right-censored at 2018-09-17.
- Painter 2019: 4–16 day gaps; 2019-07-17 anomaly creates ambiguity in a 12-day window.
- A claimed lead-time improvement of a few days (e.g., 1–3 days) is within or below boundary uncertainty. Even larger apparent lead times would require sensitivity analysis over all plausible interval-censored onset bounds.

### D. Matched false-alarm-rate comparison

**Question:** Is a fair comparison between the multivariate method and conventional monitoring currently possible?

**Assessment:** **No.** A valid matched-FAR comparison requires: (1) independently reconstructed event evidence with pre-approved definitions; (2) defensible non-event exposure/denominator; (3) pre-specified operating points or FAR targets; (4) comparable baselines evaluated on the same temporal splits and exposure; (5) leakage-safe evaluation. None of these are currently satisfied.

### E. Statistical precision and power

**Question:** Can the number of independent events and available non-bloom observations support meaningful statistical inference?

**Assessment:** **No quantitative power calculation is defensible.** The number of independently reconstructed events is 0 confirmed; candidate phases are few, interval-censored, and not reconstructed. Confirmed non-bloom exposure is undefined. Without specifying event count, exposure, effect size, variance, dependence structure, and evaluation design - all currently unavailable - any power number would be fabricated. **Required before any power calculation:** pre-approved event definition; accessible raw biological data; reconstructed event table; defensible exposure accounting; pre-specified effect size/lead-time claim; independence/dependence assumptions; evaluation design.

### F. Overall feasibility

**Classification: Exploratory only.**

The existing evidence can support descriptive/exploratory analysis (e.g., characterizing sensor dynamics around reported sampling periods, with explicit caveats), but **not the original confirmatory claim** of earlier warning than conventional monitoring at comparable false-alarm rates. A restricted 2017–2019 analysis would still be exploratory unless and until independent event reconstruction, confirmed exposure accounting, and matched-FAR evaluation design are defensibly established.

---

## 9. Evaluation of Options A–D

| Option | Reconciled assessment | Defensibility | Feasibility now | Required conditions / risks | Recommendation |
|---|---|---|---|---|---|
| **A. Restricted 2017–2019 evaluation** | Can support **restricted exploratory analysis only** under current evidence. Not confirmatory. | **Low for confirmatory; moderate for carefully bounded exploratory/descriptive work.** Prior "moderate-to-high for narrowly scoped claims" is **not supported** as stated. | Exploratory: conditionally feasible after strict caveats. Confirmatory: not feasible. | Requires accessible raw data, biological-only reconstruction, pre-approved definitions, interval censoring, no buoy-informed labels, no fabricated non-bloom exposure, and explicit uncertainty. Event count and FAR remain major blockers. | Do not present as confirmatory. If pursued, label as exploratory only. |
| **B. Documented-event evaluation** | Documented windows are publication-level/candidate only; no independently reconstructed events. | **Low-moderate for exploratory event-window characterization**; not confirmatory. | Exploratory only. | Selection bias; unknown exposure; FAR undefined; cannot use buoy-informed phase boundaries as truth. | Possible as exploratory component only, with strict censoring. |
| **C. Additional independent evidence** | Targeted acquisition of Boyer SI/underlying biological data, BPWTP/WSA phytoplankton/toxin/chl-a records, and advisory archives. | **Potentially improves feasibility** if evidence is accessible, independent, and sufficient. Not guaranteed. | Feasible to pursue via authorized user channels; outcome unknown. | Access, independence, quality, temporal coverage, and event-definition suitability must be verified. No external contact initiated by agent. | **Recommended next step** (user-authorized evidence acquisition). |
| **D. Additional/replacement dataset** | Major scope change. | Unknown; not evaluated. | Not authorized. | Loses Buffalo Pound continuity; transferability risk; changes project scope. | **Do not pursue without explicit human approval.** |

**Recommendation:** **Option C first.** Pursue user-authorized acquisition/verification of independent biological records. Do not treat Option A as confirmatory validation. Any 2017–2019 work before reconstruction should be explicitly exploratory/descriptive and must not claim earlier warning at comparable FAR.

---

## 10. Recommended next step

1. **Human review this assessment.** Gate 2 remains unapproved.
2. **Option C (authorized, user-led):** obtain Boyer 2025 SI and/or underlying biological data through corresponding-author request by user; obtain BPWTP/WSA phytoplankton/toxin/chl-a/advisory records through authorized channels. Agent must not initiate external contact.
3. **If new evidence arrives:** verify accessibility, independence, measurement method, units, sample identity, and temporal coverage before any event reconstruction. Update evidence register.
4. **If sufficient accessible independent biological data become available:** draft Gate 2/3 biological-only event criteria (interval-censored, no buoy-informed labels, no imputed non-blooms, explicit exposure rules) for human approval before any reconstruction.
5. **Until then:** only exploratory/descriptive analyses are defensible, and they must be clearly labeled non-confirmatory.

---

## 11. Explicit Gate 2 approval requirements

The project owner (human) must decide Gate 2. Gate 2 cannot be approved until the following are satisfied:

| Requirement | Current status | Required for approval |
|---|---|---|
| **Independent biological event periods can be reconstructed** | **No.** 0 independently reconstructed events from accessible evidence. Boyer phases buoy-informed/raw inaccessible; Painter raw files unavailable locally. | Accessible raw independent biological data; pre-approved biological-only criteria; interval-censored reconstruction; audit trail. |
| **Independent non-bloom exposure can be established** | **No.** Unsampled gaps/missing years/unverified periods cannot be counted as non-bloom. | Pre-approved non-event/exposure definition; defensible observation coverage; explicit censoring/unknown handling. |
| **False-alarm rates can be estimated fairly** | **No.** No confirmed exposure denominator; no approved evaluation design. | Defensible exposure denominator, matched-FAR operating points, same splits/baselines, leakage-safe evaluation. |
| **Lead-time comparisons are sufficiently precise** | **No.** 5-day and 1–16 day sampling gaps plus boundary uncertainty exceed plausible few-day effect sizes. | Event-boundary uncertainty quantified; lead-time claims exceed uncertainty or are reported with full censoring bounds. |
| **Number of independent events supports confirmatory inference** | **No.** 0 confirmed reconstructed events; candidate phases insufficient/ambiguous. | Adequate number of independently reconstructed events and exposure for pre-specified confirmatory design; defensible uncertainty/power rationale. |
| **Specific missing evidence** | Boyer SI/raw data; Painter raw files locally/accessibly verified; 2014–2016/2020–2021 independent biological records; BPWTP/WSA records; toxin verification; anomaly resolution. | Obtain and verify missing evidence or explicitly narrow scope with approved non-confirmatory framing. |
| **Conditions before approval** | Not met. | Human-approved Gate 2/3 criteria; evidence register updated; reconstructed event table audited; exposure/FAR design approved; no leakage/circularity. |

**If evidence supports only exploratory work, that must be stated clearly.** This assessment does so: **Exploratory only.** The original research question is preserved; it is not redefined as achieved or confirmatory.

---

## 12. Source references and traceable file locations

| Source / artifact | Location | Notes |
|---|---|---|
| This integrated assessment | `research/reports/GATE2_2017_2019_INTEGRATED_EVIDENCE_ASSESSMENT.md` | Definitive human-review document. |
| Prior final acquisition report | `research/reports/GATE2_FINAL_EVIDENCE_ACQUISITION.md` | Reconciled to this assessment; history preserved. |
| Evidence register | `research/research_notes/GATE2_BLOOM_EVIDENCE_REGISTER.md` | Updated to agree with this assessment. |
| Escalation assessment | `research/research_notes/GATE2_ESCALATION_ASSESSMENT_2026-11-22.md` | Prior investigation record. |
| Scientific protocol draft | `documentation/SCIENTIFIC_PROTOCOL_DRAFT.md` | Provisional; Gate 2-dependent. |
| Primary dataset DOI | 10.20383/103.01100 | Buffalo Pound 2014–2021; raw data untouched. |
| Baulch 2025 | DOI 10.1016/j.dib.2025.112290; PMC12720111 | Contextual dataset paper. |
| Boyer 2025 | DOI 10.1111/fwb.70131; https://onlinelibrary.wiley.com/doi/full/10.1111/fwb.70131 | Full text previously accessed via browser 2026-11-22; SI download failed; raw data not obtained. |
| Painter 2022 paper | DOI 10.1039/D2EM00078D; PubMed 35833582 | 2018–2019 microscopy study. |
| Painter 2022 dataset | Borealis DOI 10.5683/SP3/MP6NXF; GitHub `biogeochem/buffalopound_blooms@176ff61768f1e5e5d485b53b72c68c8f287ca83f` | Files previously examined per escalation assessment; not present in repo at reconciliation. |
| Painter 2023 | DOI 10.1002/ecs2.4472 | Non-independent buoy phycocyanin classification. |
| WSA 2015 notice | https://www.saskatchewan.ca/government/news-and-media/2015/may/29/buffalo-pound-lake | Contextual operational signal. |
| CBC 2016 advisory | http://cbc.ca/news/canada/saskatchewan/blue-green-algae-blooms-shut-down-buffalo-pound-lake-1.3696278 | Contextual public-health signal. |

---

## 13. Corrections made to earlier reports

| Date | Document(s) | Prior issue | Correction made | Rationale |
|---|---|---|---|---|
| 2026-11-22 | This assessment; register; final acquisition report | Boyer 2025 pre-bloom boundary could be misread as biologically sampled from start. | Explicitly states pre-bloom begins DOY 187, **three days before first biological sample (DOY 190)**; post-bloom ends DOY 264, last reported biological sampling date. | Prevents false precision and misinterpretation of biological coverage. |
| 2026-11-22 | This assessment; register; final acquisition report | Boyer 2025 phases could be read as independently reconstructed ground truth. | States published phase boundaries were **not established exclusively through independent biological measurements**; buoy observations informed interpretation; original biological measurements **not obtained as accessible raw data**; no independent reconstruction/reproduction claimed. | Enforces evidence-status distinction. |
| 2026-11-22 | This assessment; register; final acquisition report | Painter 2022 sampling dates vs candidate phases could be conflated; gaps could be read as continuous confirmation. | Separates actual discrete sampling dates from published/candidate phase descriptions; states no period between samples is continuously confirmed; preserves separate 2018/2019 timelines; explains gap impact on onset/termination/lead-time. | Prevents interval-censoring error. |
| 2026-11-22 | This assessment; register; final acquisition report | 2019-07-17 anomaly risked being smoothed over. | Keeps anomaly explicitly unresolved; prohibits interpretation as termination/recovery/non-bloom. | Preserves uncertainty. |
| 2026-11-22 | This assessment; register; final acquisition report | Toxin files could be over-interpreted. | Toxin records not used as confirmed evidence until formats/units/sample identities/interpretation verified. | Prevents unverified chemical evidence becoming labels. |
| 2026-11-22 | This assessment; final acquisition report | Option A described as "moderate to high for narrowly scoped claims" in prior report. | Reclassified: **Exploratory only** overall; Option A not confirmatory; low defensibility for confirmatory, moderate only for carefully bounded exploratory/descriptive work. | Aligns feasibility with actual evidence. |
| 2026-11-22 | This assessment; register | Event count ambiguity. | Explicitly states 0 independently reconstructed biological bloom events from accessible evidence; distinguishes samples/dates/taxa/phases/candidates from events. | Prevents inflated event count. |

---

## Compliance statement

- No observations, sources, dates, labels, or results fabricated.
- No outcome labels created; no modeling performed; no Gate 4 activity.
- No raw data modified.
- Research question and primary dataset unchanged.
- Independent biological evidence distinguished from sensor-derived proxies and contextual signals.
- Unknown periods not treated as confirmed non-bloom.
- Candidate intervals not presented as confirmed continuous bloom periods.
- Uncertainty, anomalies, and access limitations preserved.
- Gate 2 **not approved** by agent.