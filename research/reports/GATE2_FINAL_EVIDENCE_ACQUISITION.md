# Gate 2 Final Evidence Acquisition and Resolution (Corrected — Reconciled)

**Project:** EcoSentinel — Detecting Early Changes in Freshwater Ecosystems Using Multivariate Time-Series Analysis  
**Research question:** "Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?"  
**Primary dataset:** Buffalo Pound Lake, Saskatchewan, Canada (DOI: 10.20383/103.01100; Baulch et al. 2025, DOI: 10.1016/j.dib.2025.112290)  
**Status:** Corrected evidence-acquisition record; reconciled 2026-11-22 for consistency with `research/reports/GATE2_2017_2019_INTEGRATED_EVIDENCE_ASSESSMENT.md`. **Gate 2 is NOT approved.**  
**Date:** 2026-11-22 (corrected after Boyer 2025 full-text verification; reconciled same day)  
**Authoring agent:** OpenCode (autonomous investigation; bounded reconciliation)

> **Reconciliation note (2026-11-22):** This document preserves acquisition history and prior findings. Where this document previously used stronger feasibility language, the definitive feasibility verdict is now **Exploratory only** as documented in `research/reports/GATE2_2017_2019_INTEGRATED_EVIDENCE_ASSESSMENT.md`. Do not treat this acquisition report as Gate 2 approval or as confirmatory validation support.

## Correction log (preserved)

| Date | Item | Prior statement | Correction | Evidence |
|---|---|---|---|---|
| 2026-11-22 | Boyer et al. 2025 access/location/year | Reported as partially accessed; year/site/sampling dates/independence unverified; full text 403. | Full text accessed via in-app browser. Boyer et al. (2025) is a **2017 Buffalo Pound Lake** study. 15 discrete surface-water samples collected ~every 5 days between **10 Jul–21 Sep 2017** (DOY 190–264). Study location: Buffalo Pound Lake, Saskatchewan (50°35'10.1"N, 105°23'5"W). Independence is **mixed** (discrete biological measurements vs. buoy-informed phase boundaries). | Wiley full text: https://onlinelibrary.wiley.com/doi/full/10.1111/fwb.70131 (accessed 2026-11-22). |
| 2026-11-22 | Painter 2018–2019 date range ambiguity | Prior text could be read as a combined continuous 2018–2019 period. | Clarified: Painter 2022 contains **two separate seasons**: 2018-05-29 to 2018-09-17 (25 dates) and 2019-05-29 to 2019-10-03 (17 dates), with gaps within and between seasons. | Painter 2022 dataset DOI 10.5683/SP3/MP6NXF; `BP_PhytoTax_2018_KP.csv`, `BP_PhytoTax_2019_KP.csv`. |
| 2026-11-22 | Boyer 2025 boundary/ground-truth reconciliation | Could be read as independently reconstructed ground truth; pre-bloom start not explicitly distinguished from first biological sample. | Pre-bloom begins DOY 187, **three days before first biological sample** (DOY 190). Post-bloom ends DOY 264, last reported biological sampling date. Published phase boundaries were not established exclusively through independent biological measurements; buoy observations informed interpretation. Original biological measurements not obtained as accessible raw data; no independent reconstruction/reproduction claimed. | Boyer 2025 full text (accessed 2026-11-22); integrated assessment. |
| 2026-11-22 | Painter 2022 gap/anomaly/toxin reconciliation | Discrete sampling dates could be conflated with continuous confirmation; 2019-07-17 anomaly and toxin files risked over-interpretation. | Actual discrete sampling dates distinguished from candidate/published phase descriptions; no period between samples continuously confirmed; 2018/2019 timelines separated; 2019-07-17 anomaly unresolved; toxin records not used as confirmed evidence until formats/units/sample identities/interpretation verified. | Painter 2022 dataset/paper; escalation assessment; integrated assessment. |
| 2026-11-22 | Feasibility reconciliation | Option A described as "moderate to high for narrowly scoped claims"; report could be read as supporting restricted confirmatory evaluation. | Definitive feasibility classification is **Exploratory only** (see `GATE2_2017_2019_INTEGRATED_EVIDENCE_ASSESSMENT.md`). 0 independently reconstructed events from accessible evidence; no confirmed non-bloom exposure; matched FAR not defensible; lead-time precision insufficient; confirmatory inference not defensible. Option A may support only carefully bounded exploratory/descriptive work, not confirmatory validation. | Integrated assessment 2026-11-22. |

## 1. Executive summary

This corrected investigation completes the Gate 2 evidence-acquisition pass for Buffalo Pound Lake (2014–2021). It re-examined Painter et al. (2022), verified Boyer et al. (2025) full text, and reassessed whether 2017–2019 provide a defensible restricted confirmatory evidence base.

**What was established:**
- **Painter et al. (2022)** provides verified independent biological microscopy evidence for two separate seasons: **2018** (25 dates, 2018-05-29–2018-09-17) and **2019** (17 dates, 2019-05-29–2019-10-03), with species-level biomass/taxonomy and toxin files (Borealis DOI 10.5683/SP3/MP6NXF).
- **Boyer et al. (2025)** is a verified **2017 Buffalo Pound Lake** study (DOI 10.1111/fwb.70131). It reports 15 discrete surface-water samples (~every 5 days, 10 Jul–21 Sep 2017, DOY 190–264) with phytoplankton identification/enumeration/biovolume/heterocyte biovolume, chl-a, nutrients, N2 fixation, and ammonium uptake. It also reports pre-bloom/major-bloom/post-bloom and primary/secondary bloom periods.
- **Independence is mixed for Boyer 2025:** discrete biological measurements are independent biological methods, but the study uses the same Buffalo Pound buoy high-frequency sensors and the published bloom-phase boundaries are informed by buoy/sensor context. Phase boundaries cannot be treated as fully independent ground truth without biological-only reconstruction.
- **Painter et al. (2023)** remains **not independent** of buoy phycocyanin signals and cannot validate buoy-predictor models.
- No verified independent biological event dataset with extractable dates was identified for **2014–2016 or 2020–2021**.

**Key scientific limitation:** Full 2014–2021 confirmatory evaluation remains **not defensible**. After reconciliation, the definitive overall feasibility classification is **Exploratory only** (see `research/reports/GATE2_2017_2019_INTEGRATED_EVIDENCE_ASSESSMENT.md`). A restricted 2017–2019 evidence base may support **carefully bounded exploratory/descriptive analysis only**; it does **not** support the original confirmatory claim. Any future confirmatory use would require, at minimum, accessible raw independent biological data, biological-only event reconstruction with pre-approved criteria, interval censoring, no buoy-informed labels as ground truth, defensible non-event exposure, and matched-FAR evaluation design. These conditions are not currently met.

**No Gate 4 actions were taken. No bloom labels were generated. No modeling was performed. No raw data were modified. No research question or primary dataset was changed.**

## 2. Sources investigated and access status

| Source | Type | Access status | Evidence provided | Independent of buoy RFU predictors? | Notes |
|---|---|---|---|---|---|
| Baulch et al. 2025, *Data in Brief* 63:112290. DOI: 10.1016/j.dib.2025.112290. PMC12720111. | Dataset paper | **Accessed** | 2014–2021 buoy dataset context; RFU pigment limitations. | Contextual only. | No independent event dates. |
| Painter et al. 2022, *Environ. Sci.: Processes Impacts* 24:1212–1227. DOI: 10.1039/D2EM00078D. PubMed 35833582. | Peer-reviewed paper | **Partially accessed** (metadata/abstract/snippets; full RSC not fully extracted) | 2018 and 2019 microscopy-based cyanobacterial bloom phases; *Dolichospermum* and *Planktothrix agardhii*. | **Yes** for microscopy/taxonomy/biomass. | Two separate seasons, not a continuous 2018–2019 period. |
| Painter et al. 2022 dataset, Borealis DOI 10.5683/SP3/MP6NXF; GitHub `biogeochem/buffalopound_blooms@176ff61768f1e5e5d485b53b72c68c8f287ca83f`. | Public dataset | **Accessed** | 2018: 25 dates; 2019: 17 dates; phytoplankton taxonomy/biomass, toxins, nutrients, heterocytes, YSI. | **Yes** for microscopy/toxin lab measurements. | Examined: `BP_PhytoTax_2018_KP.csv`, `BP_PhytoTax_2019_KP.csv`, `BP_GroupsBiomass_2018_KP.csv`, `BP_GroupsBiomass_2019_KP.csv`, `BP_2018_toxins_0.8m.csv`, `BP_2019_toxins_0.8.csv`. |
| Painter et al. 2023, *Ecosphere* 14:e4472. DOI: 10.1002/ecs2.4472. | Peer-reviewed paper | **Partially accessed** | Buoy phycocyanin GAM bloom classification 2014–2020. | **No**. | Cannot be ground truth for buoy-predictor models. |
| Boyer et al. 2025, *Freshwater Biology* 70:e70131. DOI: 10.1111/fwb.70131. URL: https://onlinelibrary.wiley.com/doi/full/10.1111/fwb.70131 | Peer-reviewed paper | **Accessed** (full text via browser; SI download failed) | 2017 Buffalo Pound Lake; 15 discrete surface-water samples (DOY 190–264, 10 Jul–21 Sep 2017); phytoplankton enumeration/biovolume/taxonomy/heterocytes; chl-a; nutrients; N2 fixation; ammonium uptake; pre/major/post and primary/secondary bloom periods. | **Mixed**. Discrete biological measurements are independent methods; buoy sensors used and phase boundaries partly buoy/sensor-informed. | SI `fwb70131-sup-0001-AppendixS1.docx` download failed (0 bytes). Data available from corresponding author upon reasonable request (not obtained). |
| Boyer 2021 MES thesis, U. Saskatchewan. Handle: https://hdl.handle.net/10388/13318 | Thesis | **Metadata accessed** | N2 fixation in prairie lakes; one upstream lake intensive study. | Unknown. | Context only; not used as event evidence. |
| WSA 2015-05-29 notice. https://www.saskatchewan.ca/government/news-and-media/2015/may/29/buffalo-pound-lake | Government notice | **Accessed** | Algae bloom/treatment challenge signal. | Independent operational signal; not biological confirmation. | No species/counts/toxins/precise dates. |
| CBC 2016-07-27 beach advisory. http://cbc.ca/news/canada/saskatchewan/blue-green-algae-blooms-shut-down-buffalo-pound-lake-1.3696278 | News | **Search-identified** | Beach shutdown/advisory. | Independent public-health signal; not biological confirmation. | Secondary report. |
| WSA Buffalo Pound Water Quality Research Project page. | Agency webpage | **Accessed** | 2025–2027 tributary monitoring project. | Not relevant to 2014–2021. | No historical biological event records. |
| BPWTP annual reports (PDFs) | Operational reports | **Located, not fully parsed** | Potential operational/lab context. | Unverified. | PDF extraction tooling unavailable. |

## 3. Verified biological evidence

| ID | Period | Evidence | Source(s) | What is verified | Independence | Key limitation |
|---|---|---|---|---|---|---|
| V1 | 2017-07-10 to 2017-09-21 (DOY 190–264) | Discrete surface-water biological sampling | Boyer et al. 2025 DOI 10.1111/fwb.70131 | 15 discrete surface-water samples ~every 5 days; 0.1 m adjacent to buoy or 0.3 m at U Regina site; one archived BPWTP intake phytoplankton sample replaced missing 0.3 m sample (DOY 212). Phytoplankton ID/enumeration/biovolume/heterocyte biovolume by Plankton R Us; chl-a, nutrients, N2 fixation (ARA/15N2), ammonium uptake. | **Biological measurements: independent methods.** Phase boundaries: **mixed/partly buoy-informed**. | Sampling sparse; published phase boundaries use buoy/sensor context; underlying data not obtained; SI unavailable. |
| V2 | 2018-05-29 to 2018-09-17 | Phytoplankton microscopy/taxonomy/biomass | Painter et al. 2022 DOI 10.1039/D2EM00078D; Borealis DOI 10.5683/SP3/MP6NXF | 25 sampling dates with species-level cell density, biomass, taxonomy, group biomass. | **Independent biological measurement**. | 1–12 day gaps; no post-09-17 sample; no precise onset/duration/termination. |
| V3 | 2019-05-29 to 2019-10-03 | Phytoplankton microscopy/taxonomy/biomass | Painter et al. 2022 DOI 10.1039/D2EM00078D; Borealis DOI 10.5683/SP3/MP6NXF | 17 sampling dates with species-level cell density, biomass, taxonomy, group biomass. | **Independent biological measurement**. | 4–16 day gaps; 2019-07-17 anomaly; no precise onset/duration/termination. |
| V4 | 2018–2019 sampled dates | Cyanotoxin/cyanopeptide lab files | Painter 2022 dataset `BP_2018_toxins_0.8m.csv`, `BP_2019_toxins_0.8.csv` | Dated toxin/cyanopeptide records exist (e.g., 2019-07-17 present). | **Potentially independent lab chemical evidence**. | Messy format; not parsed into labels; not interpreted as bloom presence/absence. |

**Non-independent/non-confirming evidence:** Painter 2023 GAM phycocyanin classifications (not independent); buoy RFU (proxy); WSA 2015/CBC 2016 (signals, not biological confirmation).

## 4. Evidence that could not be verified

| Evidence | Reason not verified | Consequence |
|---|---|---|
| Boyer 2025 supplementary information (`fwb70131-sup-0001-AppendixS1.docx`) | Browser download failed (0 bytes/failed); direct download returned HTML challenge in non-browser context. | Any sampling-date table or extra biological detail in SI not extracted. |
| Boyer 2025 underlying data | Paper states "available from corresponding author upon reasonable request"; not obtained; no contact made. | Reproducible biological-only event reconstruction limited. |
| Boyer 2021 thesis full text | Metadata accessed; PDF not text-extracted. | Cannot confirm sampling-year details. |
| BPWTP/WSA internal lab records 2014–2021 | No public dataset located; agency request outside scope. | 2014–2016, 2020–2021 coverage gap remains. |
| BPWTP annual report microcystin/phytoplankton tables | PDFs not parsed in-session. | Potential operational evidence unextracted. |
| 2019-07-17 Painter anomaly explanation | No field note/replicate explanation in examined files. | Must remain uncertain. |

## 5. Independent event-period assessment (no labels created)

Boyer 2025 published periods (as reported, **not fully independent ground truth**): pre-bloom DOY 187–212 (Jul 6–31; **starts 3 days before first reported biological sample at DOY 190**); major bloom DOY 213–238 (Aug 1–26); primary bloom DOY 215–222; secondary bloom DOY 226–233; post-bloom DOY 239–264 (Aug 27–Sep 21; **ends at last reported biological sampling date**). These are publication-level phase descriptions, not independently reconstructed event evidence.

| Candidate period | Evidence basis | Independence | Interval-censored defensibility | Precise onset/termination | Required caveats |
|---|---|---|---|---|---|
| Boyer 2017 pre-bloom (DOY 187–212) | Boyer 2025 discrete samples + buoy/sensor context | **Mixed** | **Possible only if biologically reconstructed** | **Not defensible** | Starts 3 days before first reported biological sample (DOY 190); boundaries informed by buoy phycocyanin/sensor context in paper; sparse sampling; no biological-only threshold approved. |
| Boyer 2017 major bloom primary (DOY 215–222) | Boyer 2025 discrete biological samples | **Mixed** | **Possible as candidate window with reconstruction** | **Not defensible** | Transient stratification/biomass peaks; 5-day sampling; phase boundary partly buoy-informed. |
| Boyer 2017 major bloom secondary (DOY 226–233) | Boyer 2025 discrete biological samples | **Mixed** | **Possible as candidate window with reconstruction** | **Not defensible** | Taxa shift to *P. agardhii*; sparse sampling; buoy-informed phase context. |
| Boyer 2017 post-bloom (DOY 239–264) | Boyer 2025 discrete samples | **Mixed** | **Possible only if biologically reconstructed** | **Not defensible** | "Post-bloom" is relative; absence of bloom signal not equivalent to confirmed non-bloom. |
| Painter 2018 mid-summer cyanobacteria-dominant phase (sampled around 06-13–08-09) | Painter 2022 microscopy | **Independent biological** | **Potentially defensible** with approved interval-censored definition | **Not defensible** | 1–8+ day gaps; co-occurring taxa; no pre/post-season bounds. |
| Painter 2018 late-summer/autumn *Planktothrix*-dominant phase (07-12–09-17 sampled) | Painter 2022 microscopy | **Independent biological** | **Potentially defensible** with approved definition | **Not defensible** | Right-censored at last sample 09-17. |
| Painter 2019 early/mid-summer cyanobacteria-dominant samples (06-12–08-07 sampled dates) | Painter 2022 microscopy | **Independent biological** | **Potentially defensible** with caution | **Not defensible** | Large gaps; 2019-07-17 anomaly. |
| Painter 2019 autumn *Planktothrix*-dominant phase (09-03–10-03 sampled) | Painter 2022 microscopy | **Independent biological** | **Potentially defensible** with approved definition | **Not defensible** | 9–10 day gaps; right edge 10-03. |

## 6. Assessment of Painter et al. (2022)

- **Citation:** Painter, K.J.; Venkiteswaran, J.J.; Simon, D.F.; Duy, S.V.; Sauvé, S.; Baulch, H.M. (2022). *Environ. Sci.: Processes Impacts* 24:1212–1227. DOI: 10.1039/D2EM00078D.
- **Data:** Borealis DOI 10.5683/SP3/MP6NXF (CC BY-NC-SA 4.0).
- **Verified:** Two separate seasons (2018: 25 dates, 2019: 17 dates), microscopy taxonomy/biomass/cell density/biovolume, toxins, nutrients, heterocytes, YSI. Mid-summer *Dolichospermum* spp. and autumn *Planktothrix agardhii* phases reported.
- **Independence:** Independent biological measurements relative to buoy RFU.
- **Limitations:** Sparse discrete sampling (1–16 day gaps); no precise onset/duration/termination; 2019-07-17 anomaly; phase descriptions require operational definition before any event-window use.

## 7. Assessment of Boyer et al. (2025) — corrected

- **Citation:** Boyer, L.M.; Higgins, S.N.; Baulch, H.M. (2025). Cyanobacterial Bloom Development, Nitrogen Fixation and Community Change: Insights on Rapid Change From a Shallow Lake. *Freshwater Biology* 70:e70131. DOI: 10.1111/fwb.70131.
- **Access:** Full text accessed 2026-11-22 via browser at https://onlinelibrary.wiley.com/doi/full/10.1111/fwb.70131. SI link identified but download failed in-session; underlying data not obtained.
- **Verified study details:** Buffalo Pound Lake, Saskatchewan, Canada (50°35'10.1"N, 105°23'5"W). 2017 open-water season. High-frequency buoy (YSI 6600 at 0.8 m, YSI 6920 at 2.8 m, thermistors, LI-COR PAR, Vaisala weather station) May 10–Oct 11 2017 (DOY 130–284). Fifteen discrete surface-water samples collected ~every 5 days between 10 Jul–21 Sep 2017 (DOY 190–264) at 0.1 m adjacent to buoy or 0.3 m at U Regina long-term site (50°35'51"N, 105°24'29"W); one archived BPWTP intake phytoplankton sample replaced missing 0.3 m sample (DOY 212). Scums sampled at shoreline on 4 dates (DOY 222–250) with some paired littoral surface-water samples.
- **Biological measurements:** Phytoplankton identification, enumeration, biovolume, heterocyte biovolume by Plankton R Us (Lugol's preserved; 5x concentration for water samples; scums not concentrated). Chl-a, NH4+, NO3/NO2, SRP, TDP, TP. N2 fixation by 15N2-calibrated acetylene reduction assays; 15N2-tracer assays; ammonium uptake on 5 occasions.
- **Published periods:** Pre-bloom DOY 187–212 (Jul 6–31); major bloom DOY 213–238 (Aug 1–26); primary bloom DOY 215–222; secondary bloom DOY 226–233; post-bloom DOY 239–264 (Aug 27–Sep 21).
- **Biological evidence by phase:** Pre-bloom dominated by *D. flos-aquae* with low/moderate N2 fixation; primary bloom high *D. flos-aquae* biomass and peak N2 fixation (up to 3.7 μg N L−1 h−1); secondary bloom shift to *P. agardhii* dominance and lower N2 fixation; post-bloom lower biomass, *P. agardhii* then *Woronichinia compacta*.
- **Independence assessment (critical):**
  - **A. Independently collected biological measurements:** Phytoplankton taxonomy/enumeration/biovolume/heterocyte biovolume, chl-a, nutrients, 15N2-tracer/ARA N2 fixation, ammonium uptake are laboratory/assay measurements. These are **biological/chemical measurements independent of buoy RFU as a measurement method**.
  - **B. Buoy-derived measurements:** High-frequency buoy phycocyanin, chlorophyll RFU, pH, DO, turbidity, temperature, PAR, weather were used in the study. These are **not independent** of the primary dataset/buoy sensor system.
  - **C. Published bloom-phase boundaries:** The paper defines bloom phases using bloom development/biomass accrual and discusses them alongside buoy phycocyanin/sensor patterns (e.g., "phycocyanin (Figure 2)", major bloom span). Therefore phase boundaries are **partly informed by buoy/sensor context** and cannot be automatically treated as independent ground truth labels.
- **Implication:** Boyer 2025 supports 2017 biological sampling evidence, but defensible event periods must be reconstructed from independent biological observations using pre-approved criteria, not copied from buoy-informed phase labels.

## 8. Assessment of the 17 July 2019 anomaly

- **Observation:** Painter 2022 2019-07-17 (DOY 198) microscopy sample: total biomass 45.8 mg/m3, cyanophyte 41.0 mg/m3 (89.5%), 9 taxa rows, `REP2`. Neighboring dates: 2019-07-10 total 12587.1 mg/m3 (cyano 11919.8, 94.7%); 2019-07-29 total 9497.9 mg/m3 (cyano 6755.2, 71.1%).
- **Toxin file:** `BP_2019_toxins_0.8.csv` contains 2019-07-17 records (Enki ID 25993) for non-filtered/extra-/intra-cellular fractions; non-filtered row includes MC total 1045.3 ng/L (messy wide format; careful parsing required). Same-date chemical sampling exists but does not explain low microscopy biomass.
- **Status:** **Unresolved anomaly.** Possible explanations include patchiness, replicate handling, field/lab processing, data-entry/subset issue, or real short-lived change. Do not treat as bloom termination/recovery/non-bloom.

## 9. Confirmed non-bloom evidence versus unknown periods

| Period / condition | Status | Evidence | Notes |
|---|---|---|---|
| 2018-05-29, 2019-05-29 microscopy samples | Low cyanobacterial biomass on sampled dates (11.6 and 4.0 mg/m3 cyano) | Painter 2022 | Point observations only; not extrapolated. |
| Boyer 2017 discrete samples with lower cyanobacterial biomass | Point observations only | Boyer 2025 | No approved non-bloom threshold; cannot be converted to non-bloom labels. |
| Any date between discrete samples | **Unknown** | Sparse sampling | Absence of observation is not absence of bloom. |
| 2014–2016, 2020–2021 | **Unknown biological status** | No verified independent biological dataset located | Cannot be treated as non-bloom. |
| 2019-07-17 anomaly | **Uncertain** | Painter 2022 | Unresolved. |
| WSA 2015 / CBC 2016 | **Unconfirmed bloom signals** | Public notices/reports | Not biological confirmation. |

## 10. Technical problems encountered and their resolutions

| Problem | Cause | Fix applied | Verification | Status |
|---|---|---|---|---|
| Boyer 2025 previously reported as 403/unverified | Prior session used webfetch; Wiley blocked | Used in-app browser; accepted cookies; extracted `document.body.innerText` via evaluate. | Full text content extracted (60,682 chars) including methods, phases, sampling details. | **Resolved**. |
| Boyer 2025 SI download failed | Browser download failed / file download handling | Attempted click/download and `files.list`; recorded failure. | `file_d472a117...` state failed, 0 bytes. | **Unresolved access limitation**. |
| Boyer 2025 underlying data not public | Data on request only | Did not contact authors; recorded limitation. | Data Availability statement confirmed in paper. | **Documented limitation**. |
| PDF extraction tools unavailable | No pdftotext/gs/mutool/Python PDF libs | Used browser text extraction for Wiley page. | Successful for HTML article. | **Resolved by alternate method**. |
| Painter 2019 CSV malformed URL (earlier) | Typo in curl URL | Reissued correct URL. | 406-line file confirmed. | **Resolved**. |
| Toxin CSV messy format | Wide/encoded French headers | Confirmed 2019-07-17 records via grep; no label parsing. | Rows present. | **Partially resolved**. |

## 11. Remaining scientific limitations

1. **Coverage gap remains:** 2014–2016, 2020–2021 lack verified independent biological event records.
2. **Boyer 2017 mixed independence:** Biological measurements are independent methods, but published phase boundaries are partly buoy/sensor-informed; cannot be used as fully independent ground truth without reconstruction.
3. **Sparse sampling / interval censoring:** Boyer 2017 (15 dates over ~73 days) and Painter 2018/2019 (25/17 dates) cannot support precise onset/duration/termination.
4. **Data accessibility:** Boyer 2025 SI/underlying data not obtained; reproducibility of biological-only reconstruction limited.
5. **2019-07-17 anomaly unresolved.**
6. **No approved event definition:** Biomass/taxa/toxin/persistence/censoring criteria require Gate 2/3 approval.
7. **Non-event exposure:** Unknown periods cannot be treated as non-bloom; FAR denominators remain problematic.

## 12. Comparison of Options A–D (reassessed with 2017 evidence)

| Option | Description | Scientific defensibility | Feasibility now | Main risks | Recommendation |
|---|---|---|---|---|---|
| **A. Restricted 2017–2019 evaluation** | Use only independently documented biological periods from 2017, 2018, 2019 with interval-censored, biologically reconstructed windows; 2014–2016/2020–2021 exploratory/unknown. | **Low for confirmatory; moderate only for carefully bounded exploratory/descriptive work.** Not confirmatory under current evidence. | **Exploratory only now.** Confirmatory use not feasible until reconstruction/exposure/FAR conditions are met. | Boyer phase boundaries mixed independence; sparse sampling; no SI/underlying data; 2019 anomaly; 0 independently reconstructed events from accessible evidence; no confirmed non-bloom exposure. | **Exploratory only, if clearly labeled.** Not a confirmatory fallback as currently evidenced. |
| **B. Documented-event evaluation** | Evaluate around documented event windows; unlabeled periods unknown/censored. | **Moderate** with strict censoring. | Feasible for documented windows. | Selection bias; FAR/exposure undefined; may overstate performance. | **Component** of A/C. |
| **C. Additional independent evidence** | Obtain BPWTP/WSA lab records, Boyer SI/underlying data via authorized request by user, advisory archives. | **Potentially highest** if verified independent evidence obtained. | Partially feasible; some steps require user action. | Access/quality/independence uncertainty. | **Recommended first step**. |
| **D. Additional/replacement dataset** | New primary dataset. | Unknown. | **Not authorized without explicit approval**. | Scope change, transferability loss. | **Do not pursue now.** |

## 13. Final recommendation (reconciled)

**Recommend Option C; Option A only as explicitly exploratory/descriptive, not confirmatory.**

1. **Do not claim Gate 2 complete.** Full 2014–2021 confirmatory evaluation remains indefensible. Overall feasibility is **Exploratory only**.
2. **Pursue Option C:** user/authorized channels should obtain Boyer 2025 SI/underlying biological data (author request by user), BPWTP/WSA phytoplankton/toxin/chl-a records, and advisory archives. Verify any new source for independence. Agent must not initiate external contact.
3. **Option A (2017–2019 restricted):** may be considered only as **explicitly exploratory/descriptive analysis** with strict caveats. It must not be presented as confirmatory validation. Any future confirmatory claim would require accessible raw independent biological data, biological-only reconstruction, pre-approved interval-censored definitions, defensible non-event exposure, and matched-FAR evaluation design.
4. **If reconstruction/data access is insufficient:** do not make confirmatory claims; limit to descriptive/exploratory analysis clearly labeled non-confirmatory.
5. **Reject Option D** without explicit approval.

**Gate 2 readiness:** **Ready for human review; NOT approved.** The definitive verdict is **Exploratory only** per the integrated assessment. Gate 2 remains blocked pending evidence and design requirements.

## 14. Exact implications for the research question and future evaluation (reconciled)

**Research question (unchanged):** "Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?"

- **Scope:** Full 2014–2021 confirmatory claim unsupported. A 2017–2019 restricted confirmatory claim is **not currently supported**; the reconciled classification is **Exploratory only**. The research question is preserved, not redefined.
- **Independence:** Boyer 2025 biological assays are independent methods; Boyer 2025 published phase boundaries and buoy sensor measurements are not fully independent. Painter 2023 and buoy RFU are not independent ground truth.
- **Event count:** 0 independently reconstructed biological bloom events from accessible evidence.
- **Temporal precision:** All candidate windows are interval-censored; no precise onset/duration/termination; few-day lead-time claims cannot be distinguished from boundary uncertainty.
- **Non-event exposure:** Unknown periods cannot be non-bloom. FAR cannot be fairly estimated without defensible exposure.
- **Data reproducibility:** Boyer 2025 SI/underlying data not obtained; Painter 2022 raw CSVs not present in repo at reconciliation. Any reconstruction must document data availability constraints.
- **Evaluation design:** Leakage-safe temporal splits, uncertainty reporting, and separation of confirmatory vs exploratory periods remain mandatory.

## Appendix A — Key verified evidence locations

| Item | Location |
|---|---|
| Primary dataset | DOI 10.20383/103.01100; Baulch et al. 2025 DOI 10.1016/j.dib.2025.112290 |
| Painter 2022 paper | DOI 10.1039/D2EM00078D; PubMed 35833582 |
| Painter 2022 dataset | Borealis DOI 10.5683/SP3/MP6NXF; GitHub `biogeochem/buffalopound_blooms@176ff61768f1e5e5d485b53b72c68c8f287ca83f` |
| Painter 2022 files examined | `BP_PhytoTax_2018_KP.csv`, `BP_PhytoTax_2019_KP.csv`, `BP_GroupsBiomass_2018_KP.csv`, `BP_GroupsBiomass_2019_KP.csv`, `BP_2018_toxins_0.8m.csv`, `BP_2019_toxins_0.8.csv` |
| Painter 2023 | DOI 10.1002/ecs2.4472 (non-independent) |
| Boyer 2025 full text | DOI 10.1111/fwb.70131; https://onlinelibrary.wiley.com/doi/full/10.1111/fwb.70131 (accessed 2026-11-22 via browser) |
| Boyer 2025 SI | https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Ffwb.70131&file=fwb70131-sup-0001-AppendixS1.docx (download failed in-session) |
| Boyer 2025 data availability | "available from the corresponding author upon reasonable request" (not obtained) |
| WSA 2015 notice | https://www.saskatchewan.ca/government/news-and-media/2015/may/29/buffalo-pound-lake |
| CBC 2016 advisory | http://cbc.ca/news/canada/saskatchewan/blue-green-algae-blooms-shut-down-buffalo-pound-lake-1.3696278 |

## Appendix B — Compliance checklist

- [x] No observations, sources, dates, labels, or results fabricated.
- [x] Inferences distinguished from observed facts.
- [x] Independent biological evidence distinguished from sensor-derived proxies.
- [x] Unknown periods not treated as confirmed non-bloom.
- [x] Sparse sampling / interval censoring acknowledged.
- [x] No precise onset/termination claimed.
- [x] Not all cyanobacterial biomass treated as harmful bloom.
- [x] Painter 2023 not used as independent validation for buoy-predictor models.
- [x] No outcome labels generated; no predictive models trained.
- [x] Gate 4 not started.
- [x] Research question and primary dataset unchanged.
- [x] Raw data not modified (`data/raw` untouched).