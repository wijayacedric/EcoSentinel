# Sprint 4L.9 Deliverables Index

**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

| # | Deliverable | File(s) |
|---:|---|---|
| 1 | Executive report | `SPRINT_4L9_EXECUTIVE_REPORT.md` |
| 2 | Raw-file integrity verification | `RAW_FILE_INTEGRITY_VERIFICATION.md`, `RAW_FILE_INTEGRITY.csv` |
| 3 | Complete schema audit | `SCHEMA_AUDIT.md`, `SCHEMA_AUDIT.csv` |
| 4 | Variable coverage summary | `VARIABLE_COVERAGE_AUDIT.md`, `VARIABLE_COVERAGE_SUMMARY.csv` |
| 5 | Annual variable coverage table | `ANNUAL_VARIABLE_COVERAGE.csv` |
| 6 | Seasonal variable coverage table | `SEASONAL_VARIABLE_COVERAGE.csv` |
| 7 | Sampling interval and gap analysis | `SAMPLING_INTERVALS_AND_GAPS.md`, `SAMPLING_INTERVALS_AND_GAPS.csv`, `INTERVAL_DISTRIBUTION.csv` |
| 8 | QC flag audit | `QC_FLAG_AUDIT.md`, `QC_FLAG_DISTRIBUTIONS.csv`, `QC_FLAG_TOP_YEARS.csv`, `FLAGGED_VALUE_DISTRIBUTIONS.csv`, `UNDOCUMENTED_FLAGS.csv` |
| 9 | Sensor-era comparability | `SENSOR_ERA_COMPARABILITY.md`, `SENSOR_ERA_SUMMARY.csv`, `TURNER_YSI_OVERLAP.csv`, `SENSOR_TRANSITIONS.csv` |
| 10 | Biological overlap table | `BIOLOGICAL_OVERLAP.csv`, `BIOLOGICAL_OVERLAP_WINDOWS.csv`, `BIOLOGICAL_OVERLAP_BY_YEAR.csv`, `BIOLOGICAL_OVERLAP_BY_SEASON.csv` |
| 11 | Temporal compatibility report | `TEMPORAL_COMPATIBILITY.md` |
| 12 | Depth and spatial compatibility | `DEPTH_AND_SPATIAL_COMPATIBILITY.md`, `DEPTH_COMPATIBILITY.csv` |
| 13 | Scientific feasibility assessment | `SCIENTIFIC_FEASIBILITY_ASSESSMENT.md`, `FEASIBILITY_MATRIX.csv` |
| 14 | External search log | `EXTERNAL_SEARCH_LOG.md` |
| 15 | Source register | `SOURCE_REGISTER.md`, `SOURCE_REGISTER.csv` |
| 16 | Reproducible scripts | `scripts/audit_sensor_raw.py`, `scripts/verify_audit.py`, `scripts/write_reports.py` |
| 17 | Machine-readable audit tables | `tables/`, root-level copies of key tables, `TABLES_INDEX.csv` |
| 18 | SHA-256 evidence register and sidecar | `EVIDENCE_SHA256_REGISTER.csv`, `EVIDENCE_SHA256_REGISTER.csv.sha256` |
| 19 | Complete handover | `SPRINT_4L9_HANDOVER.md` |
| — | Validation and independent QC | `VALIDATION_REPORT.md`, `VALIDATION.json`, `INDEPENDENT_VERIFICATION.md`, `INDEPENDENT_VERIFICATION.json` |
| — | Anomaly audit | `ANOMALY_AUDIT.csv` |
| — | Summary JSON | `summary.json` |

## Canonical tables

The canonical machine-readable outputs are in `tables/`. Root-level copies of the main tables are provided for convenience; both are registered by SHA-256. If they ever diverge, `tables/` is canonical.
