# Sprint 4I Executive Report — Mendota Access Resolution & Raw-Data Feasibility

**Date:** 2026-11-23T23:32:06.599235+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Bottom line

**No EDI raw data bytes were obtained.** The EDI data packages remain behind mandatory authenticated access. Metadata (including 129.42) is publicly available through DataONE CN and resolves much of the package design, but not the actual observations. A public **SSEC/AOSS Mendota buoy API** provides 2019-2025 environmental data (no QC flags; not equivalent to EDI 129.42/130.29) and was verified with small samples. It cannot replace the EDI packages or cover 2006-2018.

## Verified vs metadata-only vs authorization-required

| Category | What we have |
|---|---|
| **Publicly verified (bytes)** | EML metadata for 88.31, 129.42, 130.29, 415.2; DataONE CN sysmeta/ORE; SSEC sample responses (2019/2021/2020/2022-2025 probes); SSEC API docs |
| **Metadata-only** | Package variables, coverage, sampling frequency, entity counts, sensor-list table structure; not raw observations |
| **Authorization-required** | All EDI data entities (CN 404; PASTA 403; portal login) |
| **Scientifically uncertain** | Per-variable coverage; raw Mendota subset; depth/station alignment; QC; event/non-bloom feasibility |

## Key findings

- **88.31:** four Madison lakes; Mendota 0-8 m composite; **biweekly** ice-free late Mar/Apr-early Sep, 4-weekly to late Nov; 1995-2020; PhycoTech microscopy; taxonomic updates 2013. One CSV entity (2,448,830 B). Raw access blocked.
- **129.42:** current HF package, **2006-2025 metadata**, 1-minute data; daily/hourly/HR + **sensor-list table**; channels include air temp, RH, wind, PAR, chlorophyll (Turner/YSI), phycocyanin (Turner/YSI), DO, pCO2. Package-level coverage does **not** imply every channel spans 2006-2025 (not all sensors deployed each season; YSI-era channels are newer). Data blocked.
- **130.29:** temperature-only, 2006-2019, 16 tables; 2015 HR entity missing on CN.
- **415.2:** handheld YSI Pro Plus at Deep Hole; 2006-2014 temp/DO; 2014-2019 temp/DO/pH/conductance; frequency not stated.
- **Spatial:** buoy and Microbial Observatory are both at the Deep Hole (43.0995, -89.4045; 43°05'58.2"N 89°24'16.2"W); 88.31 samples the deep-hole region. Alignment is plausible but raw verification is absent.
- **Temporal overlap (metadata):** 88.31 × 129.42 = **2006-2020**; 88.31 × 130.29/415.2 = **2006-2019**. This is potentially strong (14-15 years), but conditional on raw data and Mendota-only subset.

## Access pathway

Free EDI IAM profile (Google/Microsoft/GitHub/ORCiD) → API key → authenticated REST/API or portal download. No institutional account or DUA is indicated by metadata; package-level licence/terms should be confirmed. Contacts are in EML (NTL information manager; Trina McMahon for 415). **No contact or account creation was performed.**

## Scientific feasibility

Potentially strong, but **unverified**. Biweekly biology over 14-15 years could support interval-censored onset evaluation and held-out temporal validation if raw data are complete and comparable. Conventional baselines (chlorophyll/phycocyanin sensor thresholds, temperature, DO) are available in principle. Depth mismatch (0-8 m composite vs surface sensors) and event/non-bloom adjudication remain unresolved. No labels or modelling performed.

## Status

**Mendota: CONDITIONAL — authorization-required, not selected, potentially strongest.**  
**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
