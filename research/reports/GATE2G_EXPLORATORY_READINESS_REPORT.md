# Gate 2G — Exploratory Readiness and Evidence Recovery Preparation

**Project:** EcoSentinel — Detecting Early Changes in Freshwater Ecosystems Using Multivariate Time-Series Analysis  
**Research question:** "Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?"  
**Primary dataset:** Buffalo Pound Lake, Saskatchewan, Canada (DOI: 10.20383/103.01100)  
**Date:** 2026-11-22  
**Status:** Gate 2G preparation complete within authorized scope. **Gate 2 NOT APPROVED. Classification remains Option C — Exploratory only. No labels created. No modeling performed. No Gate 4 started.**

## 1. Executive summary

Gate 2G prepared EcoSentinel to receive and validate possible future institutional biological data while making authorized exploratory/technical progress on existing evidence. The work improved evidence integrity documentation, investigated the Painter 2019-07-17 anomaly, summarized existing sensor audit artifacts, created data-intake templates/validation scripts, and documented unresolved methods decisions.

**What improved:** reproducibility/provenance scaffolding, anomaly documentation, intake readiness, and decision transparency.  
**What did not change:** no new independent biological dataset arrived; 0 independently reconstructed events; no defensible non-bloom exposure; no matched-FAR confirmatory design; Gate 2 remains blocked.

## 2. Existing evidence integrity audit

| Item | Checked | Result | Action |
|---|---|---|---|
| Painter 2022 source files | Presence in `research/evidence/gate2d/painter_2022_borealis/` | 8 files present (README, 4 phyto/biomass, 2 toxins, nutrients) | Keep as original evidence; do not modify |
| Painter checksums | Gate 2D recorded MD5s against Borealis metadata | Previously verified; no re-download needed | Preserve checksums in reports/manifests |
| Painter derived summary | `research/evidence/gate2d/derived/painter_summary.json` | Present; generated 2026-11-22 by `analyze_painter.py` | Reproducible; keep derived separate from originals |
| BPWTP annual reports | 8 PDFs in `research/evidence/gate2d/bpwtp_reports/` | Present | Originals preserved |
| BPWTP microcystin extraction | `bpwtp_microcystin_extract.txt` | Derived text present; extraction limitations documented | Treat as derived aid; verify against PDFs before use |
| Boyer 2025 evidence | Publication-level only; no SI/raw in repo | Correctly represented as inaccessible/request-only | No change |
| Gate 2D/2E/2F reports | Present in `research/reports/` | Consistent with Option C / 0 events / Gate 2 blocked | Preserved; no overwrites |
| Evidence register | `research/research_notes/GATE2_BLOOM_EVIDENCE_REGISTER.md` | Updated through 2F; 2G entry added | Preserve prior entries/correction log |
| Raw buoy data | `data/raw/buffalo_pound/FRDR_dataset_1095_download_621_202611201621/` | 8 yearly cleaned CSVs + data_flags/LICENSE/CITATION/README present | No modification |

**Provenance/reproducibility notes:**
- Derived outputs are separated (`research/evidence/gate2d/derived/`, `research/evidence/gate2g/derived/`).
- Gate 2G scripts are small/read-only and tested on synthetic fixtures.
- BPWTP extraction is text-derived from PDFs; page/section verification should be added if values are used in formal analysis.
- Painter toxin files have encoding/format complexity; no confirmed-evidence parsing pipeline yet.

## 3. Painter 2019 anomaly investigation

See `research/reports/GATE2G_PAINTER_2019_ANOMALY_INVESTIGATION.md`.

**Conclusion:** 2019-07-17 (DOY 198) remains **unresolved**. Taxonomy and group biomass agree (45.81 mg/m3 total, 41.02 mg/m3 cyano, 9 rows, all REP2, 0.8 m). Same-date toxin sample `25993` exists in three fractions, but toxin format/units/compound mapping are unverified. No correction/discard applied. Any future candidate interval spanning DOY 191–210 must carry an unresolved-anomaly flag.

## 4. Environmental sensor exploratory analysis (existing artifacts)

This section is **exploratory only**. It uses existing audit tables and does not interpret sensor patterns as independently confirmed bloom events.

### 4.1 Data availability/coverage (from `results/tables/year_summary.csv`)

| Year | Rows | First | Last | Median interval (min) | Measurement count |
|---:|---:|---|---|---:|---:|
| 2014 | 8015 | 2014-06-11 22:15:00 | 2014-09-05 01:15:00 | 15 | 30 |
| 2015 | 20438 | 2015-05-14 21:10:00 | 2015-10-06 11:50:00 | 10 | 32 |
| 2016 | 18975 | 2016-05-18 16:50:00 | 2016-09-28 15:50:00 | 10 | 32 |
| 2017 | 22023 | 2017-05-09 17:20:00 | 2017-10-11 12:40:00 | 10 | 32 |
| 2018 | 20162 | 2018-05-15 16:00:00 | 2018-10-04 11:30:00 | 10 | 32 |
| 2019 | 18026 | 2019-05-29 17:00:00 | 2019-10-03 13:20:00 | 10 | 31 |
| 2020 | 16836 | 2020-06-05 16:30:00 | 2020-10-01 13:20:00 | 10 | 33 |
| 2021 | 18285 | 2021-05-31 20:20:00 | 2021-10-07 14:30:00 | 10 | 31 |

### 4.2 Quality flags / reliability

- Raw flag definitions preserved in `data/raw/buffalo_pound/.../data_flags.csv` and `results/tables/flag_definitions.csv`.
- Existing audit artifacts: `quality_flag_summary.csv`, `quality_flag_counts.csv`, `sensor_reliability_by_year.csv`, `missing_data_periods.csv`, `flag_measurement_crosscheck.csv`.
- Gate 2G derived summary: `research/evidence/gate2g/derived/sensor_audit_summary.json` (generated from existing tables).

### 4.3 Exploratory interpretation boundaries

- Sensor patterns can inform data quality, covariation, and exploratory hypotheses only.
- No sensor-derived pattern is treated as independently confirmed biological bloom event.
- B7 pigment/turbidity spikes, M/C flags, and A4 2015 PAR shading require sensitivity-aware handling per protocol.
- 2019 deep sensors limited; cross-year comparisons must account for sensor availability/changes.

## 5. Institutional data intake readiness

Created: `research/reports/GATE2G_INSTITUTIONAL_DATA_INTAKE_SPECIFICATION.md` and `research/evidence/gate2g/data_intake/`.

**Ready:**
- Data dictionary template (`templates/biological_observation_data_dictionary.csv`)
- Provenance template (`templates/provenance_template.json`)
- Intake manifest template (`templates/intake_manifest_template.csv`)
- Read-only validator script (`research/evidence/gate2g/scripts/validate_intake.py`)
- Synthetic test fixture and validation run (`derived/validation_synthetic.json`)

**Not ready / blocked by external input:**
- No institutional datasets received.
- No data-use terms reviewed.
- No source-specific field mappings possible until files arrive.

## 6. Analytical pipeline preparation

| Component | Status | Artifact | Notes |
|---|---|---|---|
| Intake validator (CSV/XLSX schema/missingness/required fields) | Ready (basic) | `research/evidence/gate2g/scripts/validate_intake.py` | Read-only; XLSX requires openpyxl |
| Sensor audit summarizer | Ready | `research/evidence/gate2g/scripts/summarize_existing_sensor_audit.py` | Uses existing audit tables |
| Painter 2018/2019 summary extractor | Ready | `research/evidence/gate2d/derived/analyze_painter.py` | Existing, reproducible |
| Unit/timestamp/duplicate checks for incoming bio data | Partial | Specified in intake spec; implement per source schema | Do not guess units/timezones |
| Biological-environmental alignment diagnostics | Not implemented | Documented in methods register | Requires approved alignment rules and data |
| Provenance manifest workflow | Ready (template) | intake templates | Human process required |

## 7. Research methodology preparation

See `research/reports/GATE2G_METHODS_AND_DECISIONS_REGISTER.md`.

Key unresolved/blocked decisions: biological-only event definition (M1), interval-censoring rules (M3), non-bloom exposure (M5), spatial/temporal alignment (M6/M7), independent event separation (M8), matched-FAR design (M10), missed-event evaluation (M11), uncertainty estimation (M16), Gate 2 approval criteria (M18). No decisions finalized.

## 8. Institutional response readiness

No external contacts were made in Gate 2G. A tracking template is provided below for user-provided correspondence.

| Organisation/contact | Date contacted | Response status | Data availability | Access conditions | Referral | Potential scientific value | Follow-up action (human approval required) |
|---|---|---|---|---|---|---|---|
| Boyer et al. 2025 corresponding author | TBD (if user sent) | Unknown | SI/raw 2017 biological records potentially useful | Unknown/request-only | TBD | High (Tier 1 if record-level) | Only after teacher/adult review + explicit authorization |
| Buffalo Pound Water Treatment Plant | TBD | Unknown | Phyto/cell counts/biovolume/lab chl-a/toxins possible | Unknown | WSA/lab contractors? | High/Medium | Authorized request |
| Saskatchewan Water Security Agency | TBD | Unknown | Historical biological monitoring records possible | Unknown | TBD | High/Medium | Authorized request |
| USask researcher referral 1 | TBD | Unknown | Unknown | Unknown | TBD | Unknown | Human approval before contact |
| USask researcher referral 2 | TBD | Unknown | Unknown | Unknown | TBD | Unknown | Human approval before contact |

## 9. Risks and guardrails

| Risk | Status | Guardrail |
|---|---|---|
| Circular ground truth (buoy RFU used as label) | Active risk | Prohibit buoy-derived labels; biological-only independence required |
| Treating sparse samples as events | Active risk | Candidate vs approved distinction; interval censoring; 0 approved events |
| False non-bloom exposure | Active risk | No missing-as-non-bloom; defensible exposure definition required |
| Anomaly mishandling (2019-07-17) | Active risk | Keep unresolved; no silent correction |
| Data provenance loss on incoming files | Managed by templates | Checksums, manifest, provenance template, read-only validation |
| Over-interpreting technical readiness as scientific feasibility | Active communication risk | This report explicitly separates them |

## 10. Final assessment

### What genuinely improved
- Painter 2019-07-17 anomaly documented with source-level checks and explicit unresolved status.
- Data-intake templates, provenance/manifest templates, and read-only validator script created and smoke-tested on synthetic fixture.
- Existing sensor audit artifacts summarized into a reproducible derived JSON.
- Methods/decision register created; unresolved decisions made explicit.

### What remains unresolved
- Gate 2 blocked: 0 independently reconstructed biological bloom events.
- No defensible independent non-bloom exposure; matched-FAR confirmatory evaluation not defensible.
- Boyer 2017 raw/SI inaccessible; BPWTP/WSA historical biological records not obtained.
- 2019-07-17 anomaly unresolved; Painter toxin format/units unverified.

### Reproducible findings
- Painter 2018/2019 sampling counts/gaps and DOY 198 anomaly checks via `analyze_painter.py` and source CSVs.
- Sensor availability/flag table summaries via existing `results/tables/*` and `summarize_existing_sensor_audit.py`.
- Intake validator behavior on synthetic fixture via `validate_intake.py`.

### Ready for incoming institutional data
- Intake manifest/provenance/data-dictionary templates.
- Read-only validation script and validation report pattern.
- Clear rules for preserving originals, checksums, and derived outputs.

### Not ready / requires human approval
- Any external data request/contact.
- Any data-use/redistribution decision under received terms.
- Gate 2/3 approval, event definitions, non-bloom exposure, matched-FAR design, labels, or modeling.

### Option A recovery prospects
**Technically improved, scientifically unchanged.** Gate 2G improves EcoSentinel's ability to responsibly ingest and evaluate new biological evidence if it arrives. It does **not** create new biological evidence, does **not** resolve the core Gate 2 blockers, and does **not** justify upgrading from **Option C — Exploratory only**. Option A remains a long-term ambition contingent on obtaining verifiable independent biological records and human-approved Gate 2/3 methodology.