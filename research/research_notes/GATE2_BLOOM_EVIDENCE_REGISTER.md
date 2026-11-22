# Gate 2 — Independent Bloom-Event Evidence Register (Reconciled Draft)

**Status:** Draft / reconciled for human review (NOT Gate 2 approved)  
**Date:** 2026-11-22 (reconciled with integrated assessment; Gate 2C/2D updates added)  
**Purpose:** Compile and reconcile candidate bloom-event evidence for Buffalo Pound Lake (2014–2021). This register distinguishes publication-level evidence, accessible raw evidence, independently measured evidence, independently reconstructed event evidence, and contextual evidence. No biological labels are invented.

## Evidence rules (per project policy)

- Distinguish independently confirmed blooms from sensor-derived pigment signals.
- Never treat missing observations as non-bloom observations.
- Do not fabricate bloom dates, labels, or citations.
- Any bloom definition used for modeling must be approved at Gate 2/3.
- Candidate intervals are never confirmed continuous bloom periods unless accessible evidence and pre-approved criteria support that conclusion.

## Evidence-status definitions

| Status | Meaning |
|---|---|
| **Publication-level evidence** | What a published study reports observing/interpreting. |
| **Accessible raw evidence** | Original biological/chemical measurements actually available for inspection in this project. |
| **Independently measured evidence** | Measurements obtained by methods independent of buoy predictor variables being evaluated. |
| **Independently reconstructed event evidence** | Event periods established using predefined biological criteria on accessible independent measurements, without predictor signals. |
| **Contextual evidence** | Advisories, operational records, sensor-derived classifications, or other supporting information that cannot independently establish biological bloom status. |

## Evidence inventory (reconciled)

| ID | Years | Evidence type | Publication-level | Accessible raw in project | Independently measured? | Independently reconstructed event evidence? | Source | What it supports | Limitations / confidence |
|---|---|---|---|---|---|---|---|---|---|
| E1 | 2014–2021 | Dataset documentation | Yes | Dataset paper accessed; buoy raw data not re-audited here | No (contextual; buoy RFU proxies) | No | Baulch et al. 2025, *Data in Brief* 63:112290; PMC12720111; DOI 10.1016/j.dib.2025.112290 | Buffalo Pound context; RFU pigment limitations; no independent event dates. | **Medium confidence for context; no event dating.** |
| E2 | 2018–2019 | Microscopy / indicator species analysis (peer-reviewed) | Yes | **No local raw CSVs present in repo at reconciliation.** Prior escalation assessment recorded examining Borealis/GitHub files. | Yes for microscopy/taxonomy/biomass (method independent of buoy RFU predictors) | **No** (no pre-approved criteria; no in-repo raw reconstruction audit) | Painter et al. 2022, *Environ. Sci.: Processes Impacts* 24:1212–1227; DOI 10.1039/D2EM00078D; PubMed 35833582; data DOI 10.5683/SP3/MP6NXF | 25 discrete 2018 sampling dates (2018-05-29–2018-09-17) and 17 discrete 2019 sampling dates (2019-05-29–2019-10-03) reported/priorly examined. Mid-summer *Dolichospermum* spp. and autumn *Planktothrix agardhii* phases reported. | **Medium confidence for presence of sampled biological observations; low for continuous event boundaries.** Sparse 1–16 day gaps; no precise onset/duration/termination; 2019-07-17 anomaly unresolved. No period between samples is continuously confirmed. |
| E3 | 2014–2020 | Sensor/phycocyanin GAM bloom classification | Yes | Not needed (sensor-derived) | **No** (uses buoy phycocyanin/sensor data) | No | Painter et al. 2023, *Ecosphere* 14:e4472; DOI 10.1002/ecs2.4472 | Context/sensitivity comparator only. | **Not usable as independent ground truth** for buoy-predictor models. |
| E4 | 2017 | Peer-reviewed bloom development/N2 fixation study with discrete biological sampling | Yes (full text previously accessed 2026-11-22) | **No.** SI download failed; underlying biological measurements not obtained; not in repo. | **Mixed.** Biological/chemical assays are independent methods; buoy observations used and phase boundaries partly buoy/sensor-informed. | **No.** Published phases are not independently reconstructed ground truth. | Boyer et al. 2025, *Freshwater Biology* 70:e70131; DOI 10.1111/fwb.70131 | Reports 15 discrete surface-water samples ~every 5 days between **DOY 190–264 (10 Jul–21 Sep 2017)**; phytoplankton ID/enumeration/biovolume/heterocyte biovolume, chl-a, nutrients, N2 fixation, ammonium uptake. Published phases: pre-bloom DOY 187–212, major bloom DOY 213–238 (primary 215–222, secondary 226–233), post-bloom DOY 239–264. | **Medium confidence for reported biological sampling; low for independent event reconstruction.** Pre-bloom starts DOY 187, **3 days before first biological sample**. Post-bloom ends DOY 264, last reported biological sampling date. Phase boundaries not exclusively independent biological measurements; buoy observations informed interpretation. Raw biological measurements not obtained/independently reproduced. |
| E5 | 2016 | Public health advisory / news | Yes (secondary report identified) | No primary record package in repo | No biological confirmation | No | CBC News, 2016-07-27 (advisory lifted Aug 4 2016 per follow-up) | Contextual public-health signal only. | **Low precision; not biological confirmation.** |
| E6 | 2014–2021 | Water treatment / operational impacts | Partial/unclear | No records obtained | Unknown until verified | No | Baulch et al. 2025; BPWTP reports referenced | Contextual operational relevance only. | **Low confidence until primary records obtained and independence verified.** |

## Reconciled timeline summary (no labels)

### 2017 (Boyer 2025, publication-level)
- **Actual biological sampling dates reported:** 15 discrete samples, DOY 190–264 (10 Jul–21 Sep 2017), ~every 5 days; one archived BPWTP intake sample replaced missing 0.3 m sample on DOY 212 (reported).
- **Measurements reported:** phytoplankton ID/enumeration/biovolume/heterocyte biovolume; chl-a; nutrients; N2 fixation (ARA/15N2); ammonium uptake; shoreline scums on 4 dates (DOY 222–250).
- **Published phase descriptions (not independently reconstructed):** pre-bloom DOY 187–212 (starts 3 days before first biological sample); major bloom DOY 213–238 (primary 215–222, secondary 226–233); post-bloom DOY 239–264 (ends at last reported biological sampling date).
- **Unknown/censored:** DOY 187–189 before first sample; intervals between samples; outside DOY 187–264.
- **Resolution supported:** discrete ~5-day snapshots; insufficient for precise onset/termination/lead-time.

### 2018 (Painter 2022, priorly examined; local raw unavailable)
- **Actual biological sampling dates reported/priorly examined:** 25 dates: 2018-05-29,06-07,06-13,06-19,06-21,06-25,07-03,07-06,07-09,07-12,07-16,07-18,07-24,07-25,07-30,07-31,08-08,08-09,08-14,08-17,08-21,08-23,08-28,09-05,09-17.
- **Measurements reported:** microscopy taxonomy/cell density/biomass/biovolume; group biomass; toxins/nutrients/YSI files in dataset (toxins unverified).
- **Candidate phases:** publication-level descriptions only; no continuous confirmation between samples.
- **Unknown/censored:** all gaps between samples; before 2018-05-29; after 2018-09-17.
- **Resolution supported:** point observations with 1–12 day gaps; insufficient for precise onset/termination/lead-time.

### 2019 (Painter 2022, priorly examined; local raw unavailable)
- **Actual biological sampling dates reported/priorly examined:** 17 dates: 2019-05-29,06-03,06-12,06-19,07-05,07-10,07-17,07-29,08-07,08-15,08-21,08-30,09-03,09-13,09-17,09-26,10-03.
- **2019-07-17 anomaly:** unresolved (low biomass between high-biomass dates; toxin records unverified). Do not interpret as termination/recovery/non-bloom.
- **Unknown/censored:** all gaps; before 2019-05-29; after 2019-10-03; anomaly window.
- **Resolution supported:** point observations with 4–16 day gaps; insufficient for precise onset/termination/lead-time.

## Independent event count (reconciled)

- **Independently reconstructed biological bloom events from accessible evidence:** **0 confirmed**.
- Sampling dates, taxa, candidate phases, and published phase labels are **not** independent event counts.
- Any event count requires accessible raw independent biological data, pre-approved biological-only criteria, and interval-censored reconstruction.

## Confirmatory feasibility (reconciled)

- **Overall:** **Exploratory only.** Existing evidence does not support the original confirmatory claim (earlier warning than conventional monitoring at comparable false-alarm rates).
- **Independent event periods:** cannot be reconstructed from accessible evidence.
- **Independent non-bloom exposure:** cannot be established; unknown gaps/years/sensor-only periods are not non-bloom.
- **Matched FAR comparison:** not currently defensible.
- **Lead-time precision:** insufficient for few-day claims due to sampling gaps and boundary uncertainty.
- **Statistical inference/power:** not defensible; no fabricated power calculation.

## Exact evidence locations

| Source | Exact location / identifier | Accessed / status | Notes |
|---|---|---|---|
| Painter et al. 2022 paper | DOI 10.1039/D2EM00078D; PubMed 35833582 | 2026-11-22 metadata/abstract level | Independent microscopy; 2018–2019. |
| Painter et al. 2022 dataset | Borealis DOI 10.5683/SP3/MP6NXF | Priorly examined 2026-11-22; local raw CSVs not present in repo at reconciliation | Temporal coverage 2018-05-29–2019-10-03. |
| Painter 2022 GitHub mirror | `biogeochem/buffalopound_blooms` commit `176ff61768f1e5e5d485b53b72c68c8f287ca83f` | Priorly examined 2026-11-22 | Files previously examined: `BP_PhytoTax_2018_KP.csv`, `BP_PhytoTax_2019_KP.csv`, `BP_GroupsBiomass_2018_KP.csv`, `BP_GroupsBiomass_2019_KP.csv`, `BP_2018_toxins_0.8m.csv`, `BP_2019_toxins_0.8.csv`. |
| Painter et al. 2023 | DOI 10.1002/ecs2.4472 | 2026-11-22 | **Not independent**: buoy phycocyanin GAM classification. |
| Boyer et al. 2025 | DOI 10.1111/fwb.70131; https://onlinelibrary.wiley.com/doi/full/10.1111/fwb.70131 | Full text accessed via browser 2026-11-22 | SI download failed; underlying data not obtained. |
| Baulch et al. 2025 | DOI 10.1016/j.dib.2025.112290; PMC12720111 | 2026-11-22 | Contextual. |
| WSA 2015 notice | https://www.saskatchewan.ca/government/news-and-media/2015/may/29/buffalo-pound-lake | 2026-11-22 | Contextual signal only. |
| CBC 2016 advisory | http://cbc.ca/news/canada/saskatchewan/blue-green-algae-blooms-shut-down-buffalo-pound-lake-1.3696278 | Search-identified | Contextual signal only. |

## Gate 2C targeted acquisition update (2026-11-22)

Bounded investigation documented in `research/reports/GATE2C_TARGETED_EVIDENCE_ACQUISITION.md`. No raw data modified; no labels created; no external contact made.

| ID | Years | Evidence type | Accessibility | Raw data actually available? | Independence | What changed | Limitations / suitability |
|---|---|---|---|---|---|---|---|
| E2 (update) | 2018–2019 | Painter 2022 microscopy dataset | Public (Borealis DOI 10.5683/SP3/MP6NXF, CC BY-NC-SA 4.0) | Yes, public files accessible; phyto tax CSVs temp-downloaded for verification 2026-11-22 then deleted | Independent biological measurements (microscopy) | Confirmed public accessibility, file inventory, 2018/2019 DOYs, and 2019-07-17 anomaly from public files. Toxin headers inspected; interpretation unverified. | Still sparse/interval-censored; 0 independently reconstructed events; toxin evidence not confirmed. Exploratory/candidate only. |
| E4 (update) | 2017 | Boyer 2025 publication/data access | Publication OA per Semantic Scholar (CC BY-NC-ND); pdfdirect/DOI webfetch 403 in-session; SI previously failed; underlying data request-only | No record-level raw data obtained | Mixed (assays independent methods; phases buoy-informed) | Confirmed OA metadata via Semantic Scholar API; no public raw-data repository identified. | Request required; no reconstructable raw evidence obtained. |
| E7 | 2014–2021 | BPWTP annual reports | Public PDF listings at https://www.buffalopoundwtp.ca/publications/annual-report | PDFs accessible; biological content unverified | Unknown until verified | Identified public annual report PDFs 2014–2021. 2019 PDF text extraction not possible in-session. | **Unverified.** Not biological ground truth; may be operational summary only. |
| E8 | 2014–2021? | WSA Surface Water Quality Data portal | Public portal/pages: https://wsask.ca/recreation-environment/lakes-and-rivers-overview/surface-water-quality-data/ ; https://waterquality.saskatchewan.ca/PrimaryStation ; https://waterquality.saskatchewan.ca/RiverBasin | Portal accessible; Buffalo Pound 2014–2021 biological records unverified | Unknown until verified | Identified public portal/access route. WSA states 1970–2011 historical data; 2012-current next phase. | **Unverified.** Variables/frequency/independence for Buffalo Pound 2014–2021 unknown. |

## Gate 2D comprehensive acquisition update (2026-11-22)

Bounded investigation documented in `research/reports/GATE2D_COMPREHENSIVE_EVIDENCE_ACQUISITION.md`. Originals downloaded to `research/evidence/gate2d/`; derived extraction clearly separated. No raw primary dataset modified; no labels created; no external contact made.

| ID | Years | Evidence type | Accessibility | Raw data actually available? | Independence | What changed | Limitations / suitability |
|---|---|---|---|---|---|---|---|
| E2 (update) | 2018–2019 | Painter 2022 microscopy dataset | Public (Borealis DOI 10.5683/SP3/MP6NXF, CC BY-NC-SA 4.0) | Yes; downloaded to `research/evidence/gate2d/painter_2022_borealis/` with checksums verified 2026-11-22 | Independent biological measurements (microscopy) | Verified in-repo evidence copy, checksums, 2018/2019 DOYs, schemas, 2019-07-17 anomaly. | Sparse/interval-censored; 0 independently reconstructed events; toxin interpretation unverified. Exploratory/candidate only. |
| E4 (update) | 2017 | Boyer 2025 / Boyer 2021 thesis | Boyer 2025 OA metadata confirmed; SI/raw request-only. Boyer 2021 thesis public (USask HARVEST 10388/13318) | Boyer 2025 raw: no. Thesis PDF publicly accessible (temp-extracted) | Mixed (methods independent; phase boundaries buoy-informed) | Thesis corroborates 2017 Buffalo Pound sampling context (DOY 191–264 described). No record-level raw dataset obtained. | Publication-level corroboration only; not reconstructable ground truth. |
| E7 (update) | 2014–2021 | BPWTP annual reports | Public PDFs downloaded to `research/evidence/gate2d/bpwtp_reports/` | PDFs accessible; microcystin sections text-extracted | Lab toxin assay method independent of buoy RFU; intake location differs from buoy | Extracted monthly raw/treated microcystin tables (2017–2021 May–Oct), 2016 narrative values, 2014–2015 limited annual screening entries. | **Toxin evidence, not phytoplankton taxonomy/biovolume.** Monthly sparse; May–Oct only; <LOD not non-bloom; no event boundaries. |
| E8 (update) | 2014–2021? | WSA/Saskatchewan water-quality portals | Primary Station portal inspected (https://waterquality.saskatchewan.ca/PrimaryStation) | Portal accessible; relevant biological records not verified | Unknown; listed params chemical/field, no phytoplankton/toxin visible | Confirmed Qu'Appelle R HWY 2 above Buffalo Pound station has chemical/field params incl. chlorophyll a but no phytoplankton taxonomy/cell counts/microcystin. | Not verified as independent biological bloom evidence. |
| E9 | 2016–2021 | BPWTP raw-water microcystin measurements | Public annual reports; extracted in `bpwtp_microcystin_extract.txt` | Yes (report-level values extracted; original PDFs preserved) | **Independent lab toxin measurement method** | New independent toxin evidence: 2016 peak 7 µg/L raw (narrative); 2017–2021 monthly May–Oct raw/treated values including 2019-08-12 4.5 µg/L raw. | Sparse monthly; intake location; method/QA details limited in report text; toxin presence ≠ full bloom reconstruction; cannot establish non-bloom exposure. |

## Gate 2 gaps (blocking)

- **No approved bloom-event table.** 0 independently reconstructed events from accessible evidence (candidate observations only).
- **Coverage gap:** 2014–2016, 2020–2021 lack verified independent phytoplankton/biovolume event records; BPWTP microcystin provides partial toxin context only.
- **Boyer 2025 limitations:** raw biological measurements not obtained; SI unavailable; published phase boundaries partly buoy-informed; pre-bloom starts DOY 187 before first biological sample DOY 190.
- **Painter 2022 limitations:** in-repo evidence copy now exists; still sparse sampling; no continuous confirmation between samples; 2019-07-17 anomaly unresolved; toxin files unverified for confirmed-evidence use.
- **BPWTP microcystin:** independent toxin method but monthly/sparse, intake-located, no taxonomy/biovolume, cannot define event boundaries or non-bloom exposure.
- **WSA:** no verified phytoplankton/toxin biological records for Buffalo Pound 2014–2021 obtained.
- **No confirmed non-bloom exposure / no defensible FAR denominator.**
- **No approved event definition/censoring/exposure rules.**

## Correction log

| Date | Correction | Prior statement | Corrected statement | Evidence |
|---|---|---|---|---|
| 2026-11-22 | Boyer 2025 access/location/year | "Full text not accessible (403); year/dates/independence unverified"; 2014–2017/2020–2021 lacked verified independent biological records | Full text accessed via browser; Boyer 2025 is a 2017 Buffalo Pound Lake study with 15 discrete surface-water samples (DOY 190–264, 10 Jul–21 Sep 2017) and discrete biological measurements; independence is mixed because buoy sensors inform context/phase boundaries | Wiley full text https://onlinelibrary.wiley.com/doi/full/10.1111/fwb.70131; in-browser text extraction 2026-11-22 |
| 2026-11-22 | Boyer 2025 boundary/ground-truth reconciliation | Phase boundaries could be read as independently reconstructed ground truth; pre-bloom start not explicitly distinguished from first biological sample | Pre-bloom begins DOY 187, three days before first biological sample (DOY 190); post-bloom ends DOY 264, last reported biological sampling date. Published phase boundaries were not established exclusively through independent biological measurements; buoy observations informed interpretation. Original biological measurements not obtained as accessible raw data; no independent reconstruction/reproduction claimed. | Boyer 2025 full text as previously accessed; integrated assessment reconciliation |
| 2026-11-22 | Painter 2022 reconciliation | Sampling dates/candidate phases and gap handling could be conflated; toxin records risked over-interpretation | Actual discrete sampling dates distinguished from candidate/published phase descriptions; no period between samples continuously confirmed; 2018/2019 timelines separated; 2019-07-17 anomaly unresolved; toxin records not used as confirmed evidence until formats/units/sample identities/interpretation verified. | Painter 2022 DOI/dataset metadata; escalation assessment; integrated assessment |
| 2026-11-22 | Feasibility reconciliation | Option A described as moderate-to-high for narrowly scoped claims in prior report | Overall feasibility **Exploratory only**. 0 independently reconstructed events from accessible evidence; no confirmed non-bloom exposure; matched FAR not defensible; lead-time precision insufficient; statistical inference not defensible. | Integrated assessment |
| 2026-11-22 | Gate 2C targeted acquisition | Accessibility of Painter/Boyer/BPWTP/WSA evidence not fully re-verified in this targeted pass | Painter 2022 Borealis files confirmed publicly accessible (temp verification; DOYs/anomaly confirmed). Boyer 2025 OA metadata confirmed; raw data/SI remain inaccessible. BPWTP annual report PDFs and WSA water quality portals identified as public access routes but biological suitability unverified. No change to 0 independently reconstructed events; classification remains **C - Exploratory only**. | `research/reports/GATE2C_TARGETED_EVIDENCE_ACQUISITION.md` |
| 2026-11-22 | Gate 2D comprehensive acquisition | Painter files not in-repo; BPWTP biological content unverified; Boyer 2021 thesis/WSA params not inspected | Painter 2022 files downloaded to `research/evidence/gate2d/painter_2022_borealis/` with checksums verified. BPWTP 2014–2021 annual reports downloaded; monthly microcystin tables extracted (2017–2021) plus 2016 narrative/2014–2015 limited entries as independent lab toxin evidence (sparse, intake-located). Boyer 2021 thesis public and corroborates 2017 context; no raw record-level data. WSA Primary Station inspected—no phytoplankton/cell count/microcystin params visible. No change to 0 independently reconstructed events; matched FAR still not defensible; classification remains **C - Exploratory only**. | `research/reports/GATE2D_COMPREHENSIVE_EVIDENCE_ACQUISITION.md` |

## Provisional handling (NOT approved)

- Do **not** create bloom labels for modeling.
- Do **not** train/evaluate predictive models.
- Do **not** proceed to Gate 4.
- Maintain this register as evidence-only until Gate 2/3 human review and decision.