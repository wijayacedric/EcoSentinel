# Sprint 4 Executive Report — Comprehensive Global Biological Data Acquisition Investigation

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Sprint:** Schedule Recovery Sprint 4  
**Gate 2 status:** **PAUSED / NOT APPROVED — Option C (Exploratory only)** (unchanged)

## 1. Mission and constraints

This sprint conducted a first-pass, evidence-backed global investigation for independent biological datasets suitable for EcoSentinel. No real-data modelling, confirmatory evaluation, biological event labeling, Gate/protocol changes, raw project data modifications, external contacts, or external uploads were performed. Downloaded external files were kept in an isolated directory: `research/evidence/sprint4_global_bio/`.

This report does **not** claim exhaustive global coverage. It documents what was searched, what was verified, what remains uncertain, and what requires human approval.

## 2. Search coverage (first pass)

| Metric | Value | Notes |
|---|---:|---|
| Distinct source categories investigated | 9 | Publication/data linkage; Borealis/USask/HARVEST/GitHub; US EPA NARS; UK CEH EIDC; EEA/WISE/Waterbase; EDI/USGS catalog leads; GLEON/network leads; LAGOS; Buffalo Pound institutional/operational leads |
| Search log entries | 14 | `SEARCH_QUERY_AND_REPOSITORY_LOG.csv` |
| Unique candidate records (inventoried) | 9 | 5 Buffalo Pound + 4 global/meta-source candidates |
| Candidates verified as downloadable/inspectable | 2 | BP-001 Painter 2022 (key files downloaded/inspected); GL-001 NLA 2017 phytoplankton CSV header verified downloadable |
| Candidates with independent biological observations (verified/strongly indicated) | 4 | BP-001 (verified microscopy/biovolume/biomass/toxins); BP-002 (per project records, raw data not obtained); GL-001 (verified counts/biovolume/density); GL-002 (metadata indicates phyto/zooplankton counts; gated) |
| Candidates potentially suitable for confirmatory research (conditional) | 2 | BP-001 (B, conditional, insufficient alone); GL-002 (B, conditional, licence/pairing/inspection required) |
| Exploratory/meta-source candidates | 3 | GL-001, GL-003, GL-004 |
| Excluded/unsuitable-as-primary-confirmatory | 2 | EX-001 NLA as primary HF confirmatory; EX-002 EQR-only products as direct ground truth |

## 3. Key verified finding — Buffalo Pound

### BP-001 Painter et al. 2022 (verified, downloadable) — strongest immediate Buffalo Pound evidence
- **DOI:** 10.5683/SP3/MP6NXF (Borealis) / GitHub mirror `biogeochem/buffalopound_blooms`
- **Licence:** CC BY-NC-SA 4.0 (human review needed for intended use)
- **Content verified:** microscopy phytoplankton taxonomy, species, cell density (cells/L), biomass (mg/m3), cell volume (um3), phylum/genus/species; 25 sampling dates in 2018, 17 in 2019; toxins and nutrients/biomass files present.
- **Value:** Independent biological observations overlapping Buffalo Pound buoy period (2018-2019).
- **Limitations:** sparse/interval-censored sampling; limited years; CC BY-NC-SA; toxin CSV complex header/encoding needs careful parsing; known 2019-07-17 anomaly unresolved; not sufficient alone for Gate 2 confirmatory evaluation.

### BP-002 Boyer 2025 (high value, not publicly obtained)
- **DOI:** 10.1111/fwb.70131; Buffalo Pound 2017, ~15 biological sampling dates per project records.
- **Status:** no public raw/supplementary dataset located in Sprint 4; publisher direct fetch blocked (403). Human-authorized acquisition/contact decision required.

### BP-004/BP-005 Institutional leads
- BPWTP and WSA/provincial records remain plausible leads but no public datasets verified. Human-authorized requests required.

## 4. Strongest international alternatives (first pass)

| Rank | Candidate | Class | Why | Major blocker |
|---:|---|---|---|---|
| 1 | GL-002 CEH Cumbrian Lakes plankton (1940-2013) | B Conditional | Long-term independent phyto/zooplankton counts; rare temporal depth | EIDC licence acceptance/review; HF environmental pairing unverified; file inspection needed |
| 2 | GL-003 EDI/GLEON paired-lake meta-source | C Exploratory | Many HF sensor datasets exist; pairing possible in principle | Requires systematic per-lake inventory |
| 3 | GL-001 US EPA NLA phytoplankton | C Exploratory | Public, verified independent counts/biovolume | Single-visit survey design unsuitable for HF confirmatory EWS |

## 5. Dataset combinations assessed

| Combination | Feasibility | Assessment |
|---|---|---|
| BP buoy 2014-2021 + BP-001 Painter 2022 biological | Exploratory-promising | Temporal overlap 2018-2019 exists; biological sampling sparse/interval-censored; no defensible non-event exposure established. |
| BP buoy 2014-2021 + BP-002 Boyer 2025 biological | Conditional | High value if raw data obtained; 2017 overlap exists; access unresolved. |
| NLA phytoplankton + NLA co-sampled water quality | Exploratory only | No continuous HF predictor series; unsuitable for confirmatory HF EWS. |
| CEH Cumbrian plankton + CEH HF/monitoring environmental series | Conditional lead | Requires licence review, file inspection, and pairing verification. |

## 6. Candidates requiring permissions / human decisions

- **BP-001 Painter 2022**: CC BY-NC-SA 4.0 licence compatibility review.
- **BP-002 Boyer 2025**: human-authorized author/publisher contact or access request.
- **BP-004 BPWTP**: human-authorized institutional request.
- **BP-005 WSA**: human-authorized government/institutional request.
- **GL-002 CEH Cumbrian Lakes**: EIDC licence review/acceptance; collaboration terms review; no contact without approval.

## 7. Remaining incomplete search avenues

- Systematic EDI/GLEON per-lake paired HF+biological inventory.
- CEH file inspection after licence review.
- NLA 2007/2012/2022 full file/metadata inspection.
- EEA/WISE raw biology table inspection.
- Canada-wide (ECCC, provinces, ELA, Lake Winnipeg/Erie) biological monitoring datasets.
- Australia/NZ/Scandinavia/Asia/other regions.
- DataCite/OpenAIRE/CORE/BASE/thesis catalog systematic crawl.
- Non-English search terms and historical programme names.

## 8. Is Buffalo Pound still the strongest scientific option?

**As the primary target ecosystem, yes - provisionally.** Buffalo Pound remains scientifically strongest for EcoSentinel's *current* question because the primary HF environmental dataset is already in-project, verified, and well-documented (10.20383/103.01100), and BP-001 provides verified independent biological observations for 2018-2019. However, the current evidence base is **not sufficient for confirmatory Gate 2 evaluation**: independent biological labels and defensible non-bloom exposure remain missing/insufficient.

**No stronger alternative ecosystem has been verified** in this first pass. GL-002 (Cumbrian Lakes) is the best international lead but is conditional on licence, data inspection, and HF environmental pairing. A switch of ecosystem is **not recommended** without a human-approved protocol decision and a verified stronger paired dataset.

## 9. Human approval required

- Any author/institution/government contact or data request (BP-002/004/005, CEH collaboration).
- Any licence acceptance where terms are ambiguous or impose obligations.
- Any integration of alternative datasets into the main project.
- Any ecosystem/protocol/gate change.
- Any follow-up that would move beyond exploratory data inspection into labeling/modeling/evaluation.

## 10. Deliverables

All required Sprint 4 files were created in `research/reports/schedule_recovery_sprint_4/`:
- `SPRINT_4_EXECUTIVE_REPORT.md`
- `BUFFALO_POUND_SOURCE_INVENTORY.csv`
- `GLOBAL_DATASET_INVENTORY.csv`
- `ALTERNATIVE_LAKE_RANKING.csv`
- `BIOLOGICAL_MEASUREMENT_COMPATIBILITY.md`
- `ENVIRONMENTAL_DATA_COMPATIBILITY.md`
- `DATASET_ACCESS_AND_LICENCE_REGISTER.csv`
- `SEARCH_QUERY_AND_REPOSITORY_LOG.csv`
- `EXCLUDED_CANDIDATES_REGISTER.csv`
- `DATASET_VERIFICATION_REPORT.md`
- `REMAINING_SEARCH_GAPS.md`
- `RECOMMENDED_ACQUISITION_STRATEGY.md`

## 11. Explicit confirmation

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory only).**

No further sprint was started automatically.
