# Gate 2 Escalation Scientific Assessment — Buffalo Pound Bloom Evidence

**Status:** Assessment for human review (NOT Gate 2 approved; NOT Gate 4)  
**Date:** 2026-11-22  
**Trigger:** Insufficient independent bloom-event evidence across 2014–2021 study period (immediate escalation condition under EcoSentinel operating policy).  
**Scope:** Evidence investigation only. No bloom labels generated. No modeling. No raw data modified. No research question or primary dataset changed.

## 1) Painter et al. 2022 microscopy dataset and metadata (examined)

**Primary sources (exact locations):**
- Paper: Painter, K.J., Venkiteswaran, J.J., Simon, D.F., Duy, S.V., Sauvé, S., Baulch, H.M. (2022). *Early and late cyanobacterial bloomers in a shallow, eutrophic lake*. Environmental Science: Processes & Impacts 24:1212–1227. DOI: 10.1039/D2EM00078D. PubMed: 35833582.
- Dataset: Painter, K. et al. (2022). *Data for: Early and late cyanobacterial bloomers in a shallow, eutrophic lake*. Borealis. DOI: 10.5683/SP3/MP6NXF. License: CC BY-NC-SA 4.0. Accessed 2026-11-22 via Borealis API `https://borealisdata.ca/api/datasets/:persistentId/?persistentId=doi:10.5683/SP3/MP6NXF`.
- Code/data mirror: GitHub `biogeochem/buffalopound_blooms`, commit `176ff61768f1e5e5d485b53b72c68c8f287ca83f` (as referenced by Borealis README). Files examined via raw GitHub URLs.

**Study metadata (from README/Borealis metadata):**
- Location: Buffalo Pound Lake, 50°35’8.8” N, 105°23’0.24” W (Saskatchewan, Canada).
- Temporal coverage: 2018-05-29 to 2019-10-03.
- Sampling: microscopy/indicator species analysis; toxins/cyanopeptides measured; YSI profiles; nutrient/biomass data. 
- Key dataset files (Borealis/GitHub paths): `data/clean_data/BP_PhytoTax_2018_KP.csv` (817 rows, 25 sampling dates), `data/clean_data/BP_PhytoTax_2019_KP.csv` (405 rows, 17 sampling dates), `data/processed_data/BP_GroupsBiomass_2018_KP.csv`, `data/processed_data/BP_GroupsBiomass_2019_KP.csv`, `data/clean_data/BP_2018_toxins_0.8m.csv`, `data/clean_data/BP_2019_toxins_0.8.csv`, `data/clean_data/Nutrients_Biomass_BP_clean.tab`, `data/processed_data/BP_heterocytes_2018_KP.*`, `data/processed_data/BP_heterocytes_2019_KP.*`.

**Observed microscopy sampling dates (DOY converted from dataset):**

| Year | n dates | Dates (YYYY-MM-DD) | Typical interval |
|---|---:|---|---|
| 2018 | 25 | 05-29,06-07,06-13,06-19,06-21,06-25,07-03,07-06,07-09,07-12,07-16,07-18,07-24,07-25,07-30,07-31,08-08,08-09,08-14,08-17,08-21,08-23,08-28,09-05,09-17 | ~1–12 days; median ~3 days during Jul-Aug clusters, larger gaps at ends |
| 2019 | 17 | 05-29,06-03,06-12,06-19,07-05,07-10,07-17,07-29,08-07,08-15,08-21,08-30,09-03,09-13,09-17,09-26,10-03 | ~4–16 days; notable gaps 06-19→07-05 (16 d), 07-17→07-29 (12 d), 08-21→08-30 (9 d) |

**Biological measurements available in examined taxonomy files:** sample/location/depth/DOY/replicate (2019), species code/name, cell density (cells/L), biomass (mg/m3), cell dimensions/volume, taxonomic group/phylum/family/genus/species. Toxin/cyanopeptide files exist in dataset but were not fully extracted in this assessment; they may provide independent chemical evidence but require careful interpretation (not bloom presence/absence labels).

**Observed cyanobacterial composition (from dataset; evidence summary, not labels):**
- **2018:** Cyanophyte biomass rises from 11.6 mg/m3 (1.6%, 05-29) to high-biomass periods dominated first by *Anabaena/Dolichospermum*-group taxa (e.g., 06-19 2718 mg/m3, 71%; 07-09 8020 mg/m3, 86%) and later by *Planktothrix agardhii* (e.g., 07-16 10899 mg/m3, 81% cyano, 87% of cyano Planktothrix; 08-28 5279 mg/m3, 79%; 09-05 10744 mg/m3, 85%; 09-17 4349 mg/m3, 66%). Composition transitions between dates; both taxa co-occur at several dates.
- **2019:** Early *Anabaena*-dominated high biomass (06-12 1030 mg/m3, 72%; 07-10 11920 mg/m3, 95%), then mixed *Aphanizomenon/Anabaena/Microcystis* in late July–Aug (07-29 6755 mg/m3, 71%; 08-07 15957 mg/m3, 89%), followed by *Planktothrix*-dominant autumn samples (09-13 10499 mg/m3, 66%; 09-17 7006 mg/m3, 70%; 09-26 13461 mg/m3, 80%; 10-03 19260 mg/m3, 91%). **Caution:** 2019-07-17 sample has very low total biomass (45.8 mg/m3, REP2, 9 taxa rows) between two high-biomass dates; this requires data-quality/sample-representativeness verification before any interpretation.

## 2) Additional independent biological observations (2014–2021 search)

| Source | Years | Evidence type | Independence from buoy RFU predictors | Finding | Limitation |
|---|---|---|---|---|---|
| Boyer et al. 2025, *Freshwater Biology* 70:e70131, DOI 10.1111/fwb.70131 (“Cyanobacterial bloom development, nitrogen fixation and community change”) | Open-water season (year not fully confirmed from accessible abstract snippet; study uses buoy + discrete sampling) | Peer-reviewed field study; includes phytoplankton community dynamics/N2 fixation/discrete sampling | **Unclear/partially independent**: buoy used for high-frequency context; discrete sampling may be independent biological measurements, but methods/overlap with buoy RFU must be verified from full text | Reports pre-bloom, bloom, and post-bloom phases; *Dolichospermum flos-aquae* and *Planktothrix agardhii* niche differentiation/surface scums. Confirms bloom dynamics in Buffalo Pound. | Full text not accessible in this session (403/paywall). Year(s), sampling dates, and independence of biological measurements not verified. Cannot be used as event-date evidence without verification. |
| Abirhire et al. 2023, *Frontiers in Environmental Science* / related Buffalo Pound phytoplankton work (search-identified, not fully retrieved) | Multi-year (needs verification) | Potential phytoplankton/taxonomy records | Unknown | May contain phytoplankton community observations. | Not retrieved/verified; inclusion would require full-text review and independence check. |
| BPWTP/WSA lab records, microcystin/toxin monitoring, phytoplankton counts | 2014–2021 unknown | Operational/lab records | Potentially independent if not RFU-derived | No direct public dataset located in this session. | Requires agency data request/access; not publicly confirmed. |

**Conclusion:** Beyond Painter 2022 (2018–2019), no publicly accessible, verified, independent biological observation dataset with extractable event dates was identified for 2014–2017, 2020–2021 in this investigation.

## 3) Other independently documented bloom records (supplementary)

| Source | Year(s) | Type | Independent? | Evidence | Caveats |
|---|---|---|---|---|---|
| Saskatchewan WSA news release, 2015-05-29 “Water Security Agency Increasing Outflow from Buffalo Pound Lake” | 2015 | Public agency operational notice | **Independent of buoy RFU as a label source**; operational context | States BPWTP “challenged by weather conditions and rapidly changing water temperature in conjunction with algae blooms.” | **Not biological confirmation**; no species, toxin, or microscopy; coarse timing (late May 2015). Cannot define onset/duration/termination. |
| CBC/other media reports (2016 beaches/advisories; 2023 odor/taste) | 2016, 2023 etc. | Media/public-health reporting | Independent signal, but secondary | 2016: beach closures/advisory reported by CBC (per prior search). 2023 odor/taste linked to cyanobacteria (outside study period). | **Not biological confirmation**. Secondary reporting; dates may reflect advisory timing, not bloom onset. |
| Painter et al. 2023, *Ecosphere* 14:e4472, DOI 10.1002/ecs2.4472 | 2014–2020 | Buoy phycocyanin GAM bloom classification | **Not independent** | Uses in situ phycocyanin to classify cyanobacterial bloom formation; managed inflow years 2016–2020 had greater phycocyanin. | Cannot be used as ground truth where buoy phycocyanin/RFU or related sensor signals are predictors/features. Useful only as non-independent context/sensitivity comparator. |
| Baulch et al. 2025, *Data in Brief* 63:112290, DOI 10.1016/j.dib.2025.112290 | 2014–2021 | Dataset paper | Contextual | Documents high-frequency buoy dataset; “clearwater conditions to extreme blooms”; phycocyanin/chlorophyll are RFU proxies with limitations. | No independent event dates. Explicitly warns pigment sensors are RFU/proxies. |

## 4) Strongest defensible evaluation design options

### Option A — Restricted primary evaluation period (2018–2019) + exploratory 2014–2021
- **Design:** Primary confirmatory evaluation only where independent microscopy exists (2018–2019), using carefully defined, Gate 2-approved outcome windows with explicit uncertainty bounds. Treat 2014–2017, 2020–2021 as exploratory/unsupervised/sensitivity analyses only, with no confirmatory performance claims.
- **Strengths:** Highest scientific defensibility; avoids circular labels; aligns with available independent biological evidence.
- **Limitations:** Severely reduced n (2 seasons, 42 microscopy dates total, sparse). Limited generalizability across hydrologic/management regimes. May be underpowered for robust predictive claims. Onset/duration/termination still uncertain within sampling gaps.
- **Impact on original question:** Narrows confirmatory scope from “2014–2021 early warning” to “2018–2019 evidence-limited evaluation with exploratory extension”; original question can remain aspirational but confirmatory claims must be restricted.

### Option B — Event-level evaluation for documented periods only, no whole-period labels
- **Design:** Define event/phase windows only around independently documented observations (Painter 2018–2019 phases; any verified BPWTP/WSA/advisory records). Evaluate detection/warning behavior around those windows; leave unlabeled periods as unknown (censored/excluded from event metrics), not non-events.
- **Strengths:** Uses all defensible evidence without fabricating negatives. Transparent about unknown periods.
- **Limitations:** Sparse/irregular events; selection bias toward documented periods; difficult to compute false-alarm rates over full time series without defining non-event exposure. Requires careful exposure-time accounting.
- **Impact on original question:** Changes evaluation from continuous early-warning performance to event-documented-period assessment; weaker claim.

### Option C — Acquire/validate additional independent labels before confirmatory evaluation
- **Design:** Pause Gate 2 sign-off and pursue BPWTP lab phytoplankton/microcystin records, WSA advisories, archived water-treatment logs, or other independent datasets for 2014–2021. Only after evidence review, define Gate 2 event table.
- **Strengths:** Best path to preserve original 2014–2021 scope if evidence exists. Scientifically strongest if successful.
- **Limitations:** Data access uncertain; records may be incomplete, non-standardized, or not independent. Time/resource cost; may still fail to cover all years.
- **Impact on original question:** Preserves question if data found; otherwise delays/blocks it.

### Option D — Replace/supplement primary dataset with another independently labeled system
- **Design:** Add another lake/reservoir with independent bloom labels, or pivot primary evaluation to that system, keeping Buffalo Pound as secondary/exploratory.
- **Strengths:** Could enable defensible event-level evaluation.
- **Limitations:** **Violates current restriction (no primary dataset replacement without approval; major scope change).** Different limnology/management/sensors; transferability not guaranteed. High risk of losing project coherence.
- **Impact on original question:** Major change; not recommended without explicit human approval.

## 5) Limitations and impact on original research question

| Option | Main limitation | Risk to scientific validity | Impact on original question |
|---|---|---|---|
| A. Restricted 2018–2019 + exploratory | Small n, sparse sampling, limited regime coverage | Low if claims restricted; high if generalized | Confirmatory claims narrowed to 2018–2019; 2014–2021 becomes exploratory |
| B. Documented events only | Unknown non-event exposure; selection bias | Medium; manageable with explicit censoring | Evaluation becomes event-window based, not full-period early warning |
| C. Acquire more labels | Access/quality unknown; may be unavailable | Low if verified; stalled if not | Preserves scope only if successful |
| D. New dataset | Scope/dataset change; transferability | Medium-high | Substantially changes project; requires approval |

**Original question (preserved):** Can EcoSentinel provide scientifically defensible early warning of harmful cyanobacterial bloom risk in Buffalo Pound Lake using the 2014–2021 high-frequency buoy dataset?  
**Escalation implication:** The question remains valid, but **confirmatory evaluation over 2014–2021 is currently not defensible** without additional independent bloom evidence. Any defensible near-term evaluation must be restricted to independently documented periods and must report uncertainty and non-generalizability.

## 6) Temporal precision of 2018–2019 microscopy evidence (onset/duration/termination)

**Assessment: Insufficient for precise onset, duration, or termination dating.**

Evidence:
- Sampling is **discrete and sparse** (25 dates/2018, 17 dates/2019), not continuous. Intervals range from 1 to 16 days.
- A bloom “onset” can only be bounded between the last pre-bloom observation and first bloom observation; “termination” similarly bounded. With multi-day/week gaps, bounds are wide.
- 2018 shows dense mid-summer sampling but still has gaps (e.g., 06-25→07-03 = 8 days; 09-05→09-17 = 12 days; no samples after 09-17).
- 2019 has larger gaps and an anomalous low-biomass sample on 2019-07-17 (45.8 mg/m3 total, REP2) between high-biomass 07-10 and 07-29 samples. This cannot be interpreted as bloom termination/recovery without verification; it may represent patchiness, sampling artifact, or data quality issue.
- Taxonomic dominance transitions (Dolichospermum/Aphanizomenon/Planktothrix) are observed at sampled dates, but phase boundaries are ambiguous between samples.
- The dataset provides **point observations of community composition/biomass**, not continuous bloom-state measurements. Therefore onset/duration/termination can be described only as **interval-censored bounds**, not precise dates.

**Required handling if used:** Any Gate 2 event definition must use interval-censored windows, explicitly report sampling gaps, avoid day-precise onset/termination claims, and include sensitivity to alternative window definitions.

## 7) Updated evidence register / exact locations

The evidence register has been updated with exact source references and evidence locations: `research/research_notes/GATE2_BLOOM_EVIDENCE_REGISTER.md`.

Key exact locations:
- Painter 2022 paper: DOI 10.1039/D2EM00078D; PubMed 35833582.
- Painter 2022 data: Borealis DOI 10.5683/SP3/MP6NXF; API record `https://borealisdata.ca/api/datasets/:persistentId/?persistentId=doi:10.5683/SP3/MP6NXF`; GitHub `biogeochem/buffalopound_blooms@176ff61768f1e5e5d485b53b72c68c8f287ca83f`; taxonomy files `data/clean_data/BP_PhytoTax_2018_KP.csv`, `data/clean_data/BP_PhytoTax_2019_KP.csv`; biomass `data/processed_data/BP_GroupsBiomass_2018_KP.csv`, `data/processed_data/BP_GroupsBiomass_2019_KP.csv`; toxins `data/clean_data/BP_2018_toxins_0.8m.csv`, `data/clean_data/BP_2019_toxins_0.8.csv`.
- Painter 2023: DOI 10.1002/ecs2.4472 (non-independent phycocyanin classification).
- Boyer 2025: DOI 10.1111/fwb.70131 (full text not verified in-session).
- Baulch 2025: DOI 10.1016/j.dib.2025.112290; PMC12720111.
- WSA 2015 operational notice: https://www.saskatchewan.ca/government/news-and-media/2015/may/29/buffalo-pound-lake.

## Recommendation (for human review; no Gate 4 action)

**Recommended path:** **Option C + A hybrid**.  
1. **Do not proceed to Gate 4.** Keep Gate 2 open.  
2. **Immediately pursue Option C:** request/locate independent BPWTP/WSA phytoplankton, toxin, chlorophyll-a lab records, and advisory logs for 2014–2021; verify Boyer 2025 full text/year/sampling dates and independence.  
3. **If additional independent evidence is insufficient:** adopt **Option A** — restrict confirmatory evaluation to 2018–2019 microscopy-documented periods with interval-censored event windows and explicit uncertainty; treat all other years as exploratory only.  
4. **Do not use Option D** (primary dataset replacement) without explicit approval.  
5. **Protocol impact:** Gate 2 outcome definition, evaluation period, and confirmatory-claim scope must be revised and re-approved before any modeling. No protocol changes made silently here.

## STOP — Human review required

This is an immediate escalation condition. I have not generated bloom labels, not started modeling, not changed the research question or primary dataset, not modified raw data, and not proceeded to Gate 4. I am stopping and awaiting human review/decision on the recommended path.