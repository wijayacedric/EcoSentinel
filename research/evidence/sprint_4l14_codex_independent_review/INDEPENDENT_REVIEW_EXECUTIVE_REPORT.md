# Independent Sprint 4L.14 Review — Executive Report

**Review date:** 25 November 2026  
**Scope:** Independent, read-only scientific and methodological audit of the complete Sprint 4L.14 package against 4L.12, 4L.13 and original source evidence.  
**Verdict: ACCEPT AFTER REVISIONS.**  
**Governance remains unchanged:** research direction continues as narrowed; protocol proposed, not approved; Gate 2 paused / not approved — Option C; all 15 decisions outstanding; D-15 not approved.

## Executive assessment

Sprint 4L.14 is document-complete as a proposed package, but is **not scientifically complete**: important rules remain arbitrary or unverified, some source claims need correction, actual n remains unknown, and the project has not demonstrated that its modest descriptive question has enough information to yield interpretable answers. The package should be reopened for targeted revisions before qualified human review. No analysis is justified or authorised by this audit.

The narrowed question is answerable in principle as a **descriptive comparison of same-date rank association** between fluorometer outputs and separate microscopy endpoints. It has modest scientific value if framed as a local, measurement-specific case study that can produce a useful negative result. It does not test early warning, establish proxy validity, compare sensor accuracy, or validate one lake with the other. A strong rho could still reflect seasonal co-trending, autocorrelation, restricted endpoint selection, or sensor/community effects.

### Direct answers

1. **Is 4L.14 genuinely complete?** Its requested documents and proposal-level traceability are present. It is not substantively complete for human review because the validity of several operational rules and biomass/replicate metadata remain unresolved. “Complete” in its handover overstates that distinction.
2. **Are all nine revisions adequately resolved?** R-01, R-03, R-07 and R-11 are adequately addressed in wording. R-02 and R-08 are specified but necessarily unexecuted. R-04 is improved but its optional block bootstrap is not justified as written. R-05 is explicit but not scientifically validated. R-06 is materially improved by accessible primary methods evidence, but still lacks explicit confirmation of the exact conversion factor and replicate semantics. R-09 is improved but the current independent audit found additional primary literature and a material directly relevant Buffalo Pound result.
3. **Three most serious weaknesses:** (i) the 50%-coverage/daily-summary eligibility rule and flag/negative-value decisions lack adequate validation and may select particular days; (ii) the biomass aggregation has unresolved duplicate/sample semantics and the exact biomass conversion is not fully reproducible from the paper text/data dictionary; (iii) the proposed estimand is vulnerable to seasonal/serial structure, and no actual usable-n or temporal coverage assessment establishes whether its descriptive estimate is interpretable.
4. **P1 viable?** Conditionally viable as exploratory association, with substantial depth, station, missingness, and era limitations.
5. **P2 viable?** Conditionally viable and biologically more targeted than P1, but still species/pigment-state dependent and subject to the same sampling and sensor limitations.
6. **P3 viable?** Exploratory only pending biomass exact-method and duplicate-row resolution, plus coverage/QC review. The direct primary paper supports microscope-derived wet-weight biomass generally.
7. **P4 viable?** Same conditions as P3; exploratory only. Its use has a sounder PC rationale, but existing Buffalo Pound work shows chlorophyll can miss a major Planktothrix biomass phase; that makes the relation community-specific rather than a universal signal.
8. **Is biomass sufficiently verified?** Partly. The primary article directly verifies microscopy, species identification, cell counts and shape-based cell-volume conversion to wet-weight biomass. It does **not in accessible text state** a universal 1 g cm⁻³ density factor or the precise table formula, nor explain duplicate rows in local files. 4L.14’s “inaccessible full text” claim is now outdated.
9. **Is QC scientifically defensible?** Reproducible in parts, not yet defensible as a whole. The 50% rule (72/144, both halves), broad physical ranges, retaining negative RFU, and excluding B7 without verified overlap are choices rather than validated decisions. Mendota daily records lack within-day coverage counts, so same-day full-day comparability is asymmetric.
10. **Is uncertainty meaningful?** Leave-one-year/date-out ranges are useful influence diagnostics, not uncertainty intervals. The optional 2,000-resample season-year block percentile procedure lacks justification, a defined target population, and clear handling of sparse blocks; omit it unless independently justified. Two Buffalo Pound seasons cannot support broad temporal uncertainty.
11. **Worth pursuing?** Yes only if the student values a modest, bounded sensor–microscopy case study and accepts that results may be weak/inconclusive. It no longer answers the original EcoSentinel early-warning question.
12. **Originality:** LOW–MODERATE, closer to low. The core sensor–microscopy question is established; local synthesis has some educational value, not strong methodological novelty.
13. **SciFest competitiveness?** Plausibly a sound project, but award competitiveness is uncertain and currently below a strong entry unless student ownership, careful evidence critique, transparent data limitations, and a compelling ecological interpretation are demonstrated. No result can be presumed.
14. **Student next step:** Reopen 4L.14 for targeted protocol corrections and source updates, then submit to separate scientific, statistical, data-custodian and licence reviewers. Do not count or estimate before D-15.
15. **Should count-only audit eventually be authorised?** It is a reasonable next evidentiary step only after human decisions settle the rules and a separate explicit authorization defines exactly what counts it may report. It is not authorised now.
16. **Reopen 4L.14?** Yes, for the material amendments identified in this package. Preserve 4L.14 as history; issue a versioned addendum/revision, not a silent overwrite.
17. **Further dataset hunting justified?** **No.** The bottlenecks are protocol/evidence interpretation, not absence of another dataset. Additional search should be limited to primary-source clarification of current datasets and license terms.
18. **Final recommendation:** ACCEPT AFTER REVISIONS; keep Gate 2 paused and D-15 unapproved.

## Estimand verdicts

| Estimand | Independent status | Main condition |
|---|---|---|
| P1 Mendota Turner chlorophyll–cyanobacteria biovolume | Conditional exploratory | Establish eligibility/coverage consequences; retain depth/station caveats; describe seasons carefully |
| P2 Mendota Turner phycocyanin–cyanobacteria biovolume | Conditional exploratory | Same plus taxon composition and pigment physiology caveats |
| P3 Buffalo Pound YSI chlorophyll–cyanobacteria biomass | Exploratory only | Confirm exact biomass factor and duplicate aggregation semantics; resolve B7 and coverage selection |
| P4 Buffalo Pound YSI phycocyanin–cyanobacteria biomass | Exploratory only | Same as P3, no bloom/validation claim |

These are four paired proxy/endpoint questions, not four independent confirmations. P1/P2 and P3/P4 share endpoints and likely eligible dates.

## High-priority findings

- **Major:** the threshold for a “valid day” is arbitrary and may create time-of-day selection; current Buffalo Pound raw records do not establish that each biological date has 144 expected measurements. A 50% count rule cannot by itself make a daily mean representative.
- **Major:** primary mean-before-sum for duplicate date × species rows assumes replicate observations; the source files lack paired replicate identifiers for 2018, and 2019 REP1/REP2 are on distinct dates. Mean, sum and first-row alternatives change the estimand; sensitivity does not identify which is scientifically correct.
- **Major:** same-date concurrence combines a date-only biological sample with a daily sensor summary, potentially at different times and water parcels. It is not synchronized validation.
- **Major:** R-05 labels bounds “physical/analytical” but gives no dataset-specific evidence for several bounds; Mendota flags/documentation are known incomplete. Negative RFU retention as numeric ranks has no demonstrated interpretation as a biological low value.
- **Moderate:** the phrase “how associations differ across seasons and sensor eras” is not fully estimable for Buffalo Pound: its two-year YSI era does not contain distinct documented sensor eras; seasonal estimates may be sparse and confounded by year.
- **Moderate:** 14 annual units do not remove dependence; LOYO is an influence check, and resampling year × season blocks with replacement still relies on exchangeability assumptions the design denies.
- **Moderate:** literature review misses directly relevant primary studies and one critical source correction. Painter et al. (2022) itself compared cyanobacterial biomass with laboratory chlorophyll, finding distinct relationships by taxon and an autumn Planktothrix phase poorly indicated by chlorophyll. A narrow sensor-RFU reanalysis can still add a different question, but should state this overlap.

## Governance and integrity

The 4L.14 register preserves D-01 through D-15, with each marked outstanding/not approved; D-13 and D-14 are distinct, and D-15 remains explicitly unapproved. This audit approves none. No raw records were counted, QC-filtered, correlated, plotted, modelled, or transformed. No project protocol/register was edited. The only new files are this independent review package. Its SHA-256 register records package integrity; this does not authenticate the upstream sources.

## Handover

**ACCEPT AFTER REVISIONS.** Keep the project narrowed and exploratory, but reopen the 4L.14 proposal to repair the daily coverage rule, unresolved biological row semantics, season/era wording, uncertainty plan, biomass source citation, and transparent limits. P1/P2 are conditionally usable; P3/P4 should remain exploratory. The exact next step is a documented addendum, followed by qualified human review of D-01–D-14 and a separate decision on whether to authorize a bounded count-only audit. No analysis now.

