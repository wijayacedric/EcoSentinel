# Sprint 4L.4 Codex Handover

**Review dates:** 23–24 November 2026  
**Status:** PARTIALLY COMPLETE — literature/method review complete to accessible evidence; package-level metadata and exact-method novelty remain unresolved.  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Deliverable folder:** `research/evidence/sprint_4l_codex_mendota_literature_review/`

## Executive result

Independent verdict: **Lake Mendota remains an exploratory candidate; not yet confirmatory-ready.** This handover is **PARTIALLY COMPLETE** because this review did not verify 88.31 contents directly or close the exact-method novelty search. There is strong published evidence that Mendota combines independent species-resolved microscopy/counts/biovolume (at least in the published legacy periods) with high-frequency environmental and pigment sensors. But the biological time series is sparse relative to the sensors, no independent event rule was established here, onset is interval-censored, the 0–8m biological composite does not match a point-depth sensor, and sensors cross multiple documented generations with a major 2019 pigment magnitude discontinuity. Mendota has substantial existing prior art in high-frequency phycocyanin dynamics, environmental lag analysis, seasonal/subseasonal forecasts and hourly/daily/monthly algal prediction.

## Files produced

1. `CODEX_EXECUTIVE_ASSESSMENT.md` — verdict, strengths, limitations and readiness position.
2. `MENDOTA_BIOLOGICAL_MONITORING_REVIEW.md` — taxonomic and abundance endpoint evidence, sample design, limitations.
3. `MENDOTA_SENSOR_MONITORING_REVIEW.md` — sensor variables, coverage, depth, method changes, QC and independence.
4. `PRIOR_ART_AND_NOVELTY_ASSESSMENT.md` — direct Mendota and broader EWS literature; novelty boundary.
5. `METHODOLOGICAL_FEASIBILITY_REVIEW.md` — endpoint, censoring, exposure, fairness, leakage, validation, event-count concerns.
6. `LITERATURE_AND_SOURCE_REGISTER.csv` — source inventory and supported claims.
7. `SEARCH_LOG.md` — systematic search queries, scope, access failures and limits.
8. `GATE2_REQUIREMENTS_AND_BLOCKERS.md` — requirement status and evidence needed.
9. `CODEX_HANDOVER.md` — this file.

## Evidence and independence notes

- The required repository `AGENTS.md` instructions were read. The permanent research standards required by Sprint 4L.3 are present in that file; work followed systematic primary-source searching, source tracking, full-text/supplement review where accessible, and explicit uncertainty reporting.
- No OpenCode Sprint 4L.3 conclusion/report was opened or used. Existing project-wide Sprint 4E.1 and Codex Sprint 4L.2 artifacts were reviewed as permitted; the 4L.2 review is the prior independent sensor inventory transcription, not raw time-series analysis.
- EDI access restrictions were confirmed in NTL-LTER's public Core Datasets page and the 88.31 portal page returned 403 in the research browser. No data were downloaded and no data entities were examined.
- Some full articles and supplementary materials were accessible through publisher or institutional copies; ScienceDirect and PMC pages intermittently blocked direct open. Search snippets were not treated as sufficient to establish detailed package-level claims. Limitations are recorded in the source register and search log.

## Remaining work for completion

- Inspect the authenticated EDI `knb-lter-ntl.88.31` package schema, entity manifest, current data/method metadata and historical protocols when that separately acquired evidence is available. This review did not duplicate OpenCode acquisition.
- Obtain the exact EcoSentinel indicator specification and conduct a method-by-method citation search against the cited Mendota and lake EWS literature; the current review can only bound broad originality.
- Resolve full supplementary-material availability for key prior-art papers where publisher access was blocked.

## Recommended next authorized work

1. Reconcile this literature review with the eventual independently completed 88.31 package audit only after this review is frozen/complete; compare exact fields, years, methods and event feasibility without treating this report as a substitute for raw-data QA.
2. Verify sensor depth conflict and exact 2019 switch, calibration, QC, gap history, and coverage with public metadata already acquired or a separately authorized evidence phase.
3. Prepare a literature comparison table for the exact EcoSentinel detector and endpoint, especially against Carpenter et al. 2020, Carpenter et al. 2022, Beal et al. 2021/2022, Liu et al. 2022, and Burthe et al. 2023.
4. Only in a separately authorized stage, conduct a blinded endpoint feasibility census: candidate-independent abundance definition, sample effort/detection, interval widths, independent episode count, and non-event exposure. Do not tune endpoint criteria to observed detector performance.
5. Complete Gate 2 readiness matrix and precision/uncertainty feasibility under the same horizon, exposure and false-alarm definition before confirmatory authorization.

## Restrictions observed

No labels, onset/event intervals, modelling, hypothesis tests, confirmatory analyses, protocol changes, external contacts, uploads, commits or pushes were performed. No additional datasets were downloaded. Original data and existing evidence were not modified.
