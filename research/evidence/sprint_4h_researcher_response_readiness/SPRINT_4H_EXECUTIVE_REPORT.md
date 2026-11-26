# Sprint 4H Executive Report — Researcher Response Readiness & Dataset Opportunity Audit

**Date:** 2026-11-23T23:27:42.541908+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Purpose

Prepare for pending University of Saskatchewan/University of Regina referrals without assuming additional data exist, and re-check what metadata can resolve for Mendota. Buffalo Pound remains **pending researcher clarification**, not rejected.

## 2. Buffalo Pound additional-file audit (8 files)

| File | Dates | Variables | Independent biological value |
|---|---|---|---|
| `2018_phyto_matrix_KP.tab` | 25 dates (2018) | 73 species biomass columns | **Derived duplicate** — totals equal taxonomy biomass exactly |
| `2019_phyto_matrix_KP.tab` | 17 dates (2019) | 56 species biomass columns | **Derived duplicate** |
| `BP_GroupsBiomass_2018_KP.tab` | 25 dates | 7 group biomass totals | **Derived summary** |
| `BP_GroupsBiomass_2019_KP.tab` | 17 dates | 7 group biomass totals | **Derived summary** |
| `BP_YSI_2018.tab` | 20 dates (incl. 1 non-bio date) | Temp, conductivity, DO sat, DO mg/L, pH; 0.2-4.0 m | **New environmental profiles**, not biology |
| `BP_YSI_2019.tab` | 16 dates | Same | **New environmental profiles**, not biology |
| `BP_heterocytes_2018_KP.tab` | 23 dates | Dolichospermum heterocyte density/biomass | **Same-occasion additional biological variable** |
| `BP_heterocytes_2019_KP.tab` | 17 dates | Dolichospermum/Aphanizomenon heterocytes | **Same-occasion additional biological variable** |

**No additional years, no non-bloom periods, no higher-frequency biological sampling.** The eight files add vertical environmental context and N-fixation detail, but do not create new independent biological occasions. Effective biological sample size remains **42 date-level observations**.

## 3. Mendota metadata update

- **88.31:** 4 Madison lakes (Mendota, Monona, Wingra, Fish); Mendota 0-8 m composite; glutaraldehyde; PhycoTech; **biweekly** ice-free late Mar/Apr-early Sep, every 4 weeks to late Nov; 1995-2020; taxonomic updates Feb 2013.
- **129.42 (new metadata fetched):** 2006-2025; 1-minute; daily/hourly/HR tables; meteo, chlorophyll (Turner/YSI), phycocyanin (Turner/YSI), DO, PAR, pCO2; sensor list table. Modern predictor coverage confirmed at metadata level.
- **130.29:** 1-minute thermistor chain, 16 tables, 2006-2019; 2015 HR entity missing on CN.
- **415.2:** handheld YSI Pro Plus at Deep Hole; 2006-2014 compiled temp/DO; 2014-2019 temp/DO/pH/conductance; frequency not stated.

**Access remains blocked:** PASTA 403 for metadata/data; CN data objects 404. Metadata cannot substitute for raw-file verification. 129.42 is a newer CN-indexed metadata revision than 129.9, but data bytes are still inaccessible.

## 4. What would change Buffalo Pound's status

Only new **independent biological observations across additional years and non-bloom periods**, with methods/QC/taxonomy/station/depth documentation. Derived matrices/group biomass do not help; YSI profiles help environmental characterisation but not event count.

## 5. Dataset status

| Candidate | Status |
|---|---|
| Buffalo Pound | **PENDING researcher clarification**; current public evidence exploratory-only |
| Lake Mendota | **CONDITIONAL (auth-blocked)**; potentially strongest, not selected |
| Greifensee | **Exploratory only** (classifier biology) |
| Western Lake Erie | **Low-priority backup** (proxies/discrete; inaccessible) |

## 6. Final answer

**Buffalo Pound viable if:** additional independent microscopy/cell-biomass years, non-bloom season sampling, and enough temporal coverage to hold out whole years are provided, with methods/QC/taxonomy/station/depth/licence documentation.

**Mendota still missing:** authorised access to raw 88.31 biological counts/biovolume, 129.42 modern HF predictors (incl. sensor list/QC), 415.2 routine physico-chemical data, and 130.29 (with 2015 gap resolution); plus file-level alignment/QC verification.

**Most defensible next step:** keep Buffalo Pound pending, do not label/model; pursue authorised Mendota access in parallel; assess researcher responses with the framework; no candidate selection until evidence arrives.

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
