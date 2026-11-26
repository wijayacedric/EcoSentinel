# Technical Dependency Map (Post-4D.4 Handover)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Purpose:** Map technical dependencies for future cautious work. No new integrated datasets created.

## Legend

- **Verified:** directly observed in files/manifests/code/docs inspected during Sprints 4D-4D.4.
- **Inferred:** plausible relationship based on documentation or naming; requires verification before use.

## Dependency map

| Upstream artifact | Downstream artifact/use | Relationship | Status | Notes |
|---|---|---|---|---|
| ERIC 000C2G monthly 5p0x `class_and_feat` tarballs (60) | Sprint 4D.3 `COMPLETE_60_PACKAGE_MANIFEST.csv`, SHA256 register | Acquisition manifest tracks local path, size, hash, status | Verified | `research/evidence/sprint_4d3_greifensee_complete_acquisition/manifests/` |
| 60 tarballs | Sprint 4D.4 `COMPLETE_60_PACKAGE_CONTENT_INVENTORY.csv` | Structural/content audit derived by read-only inspection | Verified | No original archives modified |
| 60 tarballs | `MONTHLY_BIOLOGICAL_CLASSIFICATION_COVERAGE.csv`, `OBSERVATION_EFFORT_AND_MISSINGNESS_AUDIT.csv` | Record/day/timestamp counts derived from tarball contents | Verified | Descriptive; effort proxies incomplete |
| Classification txt outputs within tarballs | `CYANOBACTERIA_TAXONOMIC_LABEL_REGISTER.csv` | Heuristic regex over label tokens | Verified (method) / label semantics unverified | Not a validated taxonomic mapping |
| Observed file basenames/schemas | `CLASSIFIER_AND_SCHEMA_VERSION_HISTORY.csv`, `CROSS_MONTH_COMPARABILITY_MATRIX.csv` | Schema signatures grouped by month | Verified | Classifier-version meaning partially inferred |
| 000C2G readme / Eyring 2025 data descriptor | 4D.4 validity/overlap registers | Documentation context for interpretation limits | Verified as cited/reviewed partially | SI PDF not fully parsed in audit |
| Plankiformer/Plankifier models & training taxonomy | Label meaning, confidence, per-class performance | Classification outputs depend on model/training choices | Inferred/partially verified | Requires authoritative documentation/validation artifacts |
| Camera acquisition logs/metadata (if any) | Observation effort reconstruction | Effort normalization depends on uptime/frame metadata | Inferred | Not fully reconstructed from class_and_feat tarballs alone |
| ERIC 000C8P environmental package | Potential future exploratory alignment | Environmental pairing depends on timestamps/depth/units/QC | Verified as acquired separately; pairing not audited | `research/evidence/sprint_4d_alternative_acquisition/downloads/greifensee_2018_2023/environmental/` |
| 4D.4 audit outputs | Independent Codex/Gemini scientific reviews | Reviews should read 4D.4 deliverables as primary evidence | Verified (process intent) | Reviews not created here |
| Codex + Gemini reviews | Reconciliation memo/decision record | Reconciliation depends on both independent reviews existing | Inferred | No reconciliation performed yet |
| Any future exploratory analysis | Gate 2 constraints | Must remain Option C: no event labels, no confirmatory claims, no Gate 2 change | Verified policy | `documentation/SCIENTIFIC_PROTOCOL_DRAFT.md`, Gate 2 registers |

## Explicit non-dependencies / prohibited shortcuts

- **Not verified:** Camera-derived cyano labels -> independent biological bloom ground truth.
- **Not verified:** Raw monthly class counts -> comparable biological abundance across all 60 months.
- **Prohibited:** Creating integrated analysis datasets or harmonized labels without documented crosswalk/validation and appropriate gate review.
