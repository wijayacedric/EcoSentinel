# Independent Review Handover — Sprint 4D.4

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Prepared by:** OpenCode (technical custodian/handover task only; no new scientific investigation)

## 1. Sprint 4D.4 scope

Sprint 4D.4 performed a descriptive file-level scientific/technical audit of all 60 Greifensee 2018–2023 5p0x `class_and_feat` monthly packages. It assessed structural usability, schema/classifier consistency, cyanobacteria label presence/ambiguity, observation effort/missingness, endpoint validity, prior publication overlap, and comparability. It explicitly did **not** perform biological event labeling, modelling, confirmatory analysis, or protocol/Gate 2 changes.

## 2. Deliverables (12)

Location: `research/evidence/sprint_4d4_greifensee_content_audit/`

1. `SPRINT_4D4_EXECUTIVE_REPORT.md`
2. `COMPLETE_60_PACKAGE_CONTENT_INVENTORY.csv`
3. `MONTHLY_BIOLOGICAL_CLASSIFICATION_COVERAGE.csv`
4. `CYANOBACTERIA_TAXONOMIC_LABEL_REGISTER.csv`
5. `CLASSIFIER_AND_SCHEMA_VERSION_HISTORY.csv`
6. `OBSERVATION_EFFORT_AND_MISSINGNESS_AUDIT.csv`
7. `BIOLOGICAL_ENDPOINT_VALIDITY_ASSESSMENT.md`
8. `INDEPENDENT_VALIDATION_EVIDENCE_REGISTER.csv`
9. `PRIOR_PUBLICATION_OVERLAP_REGISTER.csv`
10. `CROSS_MONTH_COMPARABILITY_MATRIX.csv`
11. `UNRESOLVED_QUESTIONS_AND_DATA_LIMITATIONS.md`
12. `RECOMMENDED_NEXT_STEPS.md`

## 3. Main reported conclusions (from 4D.4, not re-adjudicated here)

- All 60 packages structurally present/readable; 60/60 manifest/hash reconciliation OK.
- Four schema signatures observed across May 2018–June 2023; 2023 months have Plankiformer-only 2-file signature.
- 7 cyano-pattern labels observed by heuristic regex; labels ambiguous/partially specific and not independently validated.
- Raw monthly detection frequencies not fairly comparable without effort normalization, schema/classifier harmonization, label crosswalk, and validation.
- No sufficient independent biological validation for Gate 2 confirmatory endpoint validity in inspected packages.
- Dataset may support exploratory camera-signal description only; not suitable as-is for Gate 2 confirmatory biological event evaluation.
- Single most important barrier reported: lack of independently validated, calibrated cyanobacteria biological endpoint/event ground truth compatible with EcoSentinel confirmatory design.

## 4. Known limitations / custody notes

- 4D.4 audit was structural/content-descriptive; not exhaustive semantic validation of every record.
- Cyano identification used heuristic regex over output labels.
- Eyring 2025 SI PDF was not fully parsed in this environment; SI-dependent claims should be verified.
- Empty subdirs exist in 4D.4 folder (`manifests/`, `reports/`, `tmp_extract/`, `workspace/`) — empty, no action taken.
- Executive report contains cross-dir reference to `COMPLETE_60_PACKAGE_MANIFEST.csv` (lives in 4D.3 manifests) and schema-signature backtick strings; these are not 4D.4-local file defects.

## 5. Where independent reviews should be saved

- **Codex review:** `research/evidence/sprint_4d5c_handover/reviews/CODEX_SPRINT_4D4_INDEPENDENT_REVIEW.md`
- **Gemini review:** `research/evidence/sprint_4d5c_handover/reviews/GEMINI_SPRINT_4D4_INDEPENDENT_REVIEW.md`
- **Post-review reconciliation (only after both exist):** `research/evidence/sprint_4d5c_handover/reviews/SPRINT_4D4_REVIEW_RECONCILIATION.md`

Create `reviews/` only when saving reviews; do not pre-populate with invented content.

## 6. Findings requiring reconciliation after both reviews

- Whether heuristic cyano-label matching is adequate for the audit's limited claims, and which labels are scientifically ambiguous/unusable.
- Whether 4D.4 correctly characterized schema/classifier-version incompatibilities and cross-month comparability limits.
- Whether endpoint-validity conclusion is appropriately cautious (camera-derived signal vs independent biological ground truth).
- Whether prior-publication overlap risks (especially Eyring 2025, Ntetsika 2026) are fully/accurately captured.
- Whether any 4D.4 claim overreaches available evidence or omits a critical limitation.
- Whether additional evidence could plausibly change the "exploratory only / not Gate 2 confirmatory" conclusion, and what evidence that would be.

## 7. Absolute constraints

No event labels, no modelling, no confirmatory analysis, no raw-data modification/integration, no Gate 2/protocol/research-question changes, no external contacts/uploads, no commits/pushes. Keep Gate 2 PAUSED / NOT APPROVED — Option C.
