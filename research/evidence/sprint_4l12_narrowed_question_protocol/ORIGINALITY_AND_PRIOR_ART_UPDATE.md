# Originality and Prior-Art Update

**Sprint:** 4L.12  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis may begin until this protocol has been reviewed and explicitly approved.**

## 1. Purpose

This document updates the Sprint 4L.11 prior-art assessment for the **narrowed measurement/comparability question**. It asks:

- What is already known about sensor–microscopy comparisons?
- What is already known about chlorophyll/phycocyanin proxy validity, depth mismatch, seasonality, and multi-lake comparability?
- Is there anything genuinely distinctive about the proposed study?
- If originality is modest, what additional contribution would be required?

The review is focused, not a systematic review. It distinguishes full-text inspection, abstract/metadata inspection, and project evidence. It does not claim that “not found” means “does not exist.”

## 2. Search scope

Sources searched:

1. Peer-reviewed sensor-validation and sensor–microscopy comparison studies.
2. Chlorophyll and phycocyanin fluorescence proxy studies.
3. Depth-integrated vs surface fluorescence studies.
4. Seasonal and community-composition effects on pigment fluorescence.
5. Multi-lake sensor comparability and intercalibration studies.
6. Mendota and Buffalo Pound site-specific studies.
7. Authoritative technical guidance (USGS).
8. Project evidence and prior sprint audits.

Queries and access status are recorded in `EXTERNAL_SEARCH_LOG.md`. Publication details are in `SOURCE_REGISTER.md`/`.csv`.

## 3. What is already established

### 3.1 Sensor–microscopy comparisons are common and inconsistent

| Study | Design | Key finding | Relevance |
|---|---|---|---|
| **Hartmann et al. 2019**, *Aquatic Sciences*, DOI 10.1007/s00027-018-0608-x | FluoroProbe spectral fluorescence vs microscopy, one season, drinking-water reservoir | Total chlorophyll vs total biovolume correlated well; agreement was best for diatoms and much lower for other groups; cyanobacteria were often underestimated, including at high *Microcystis* abundance | Directly comparable measurement question; shows group-specific bias |
| **Bowling et al. 2016**, *Water Research*, DOI 10.1016/j.watres.2016.08.051 | YSI EXO2 chlorophyll/phycocyanin vs cyanobacterial biovolume, three urban ponds, two summers | Phycocyanin correlated well with total cyanobacterial biovolume in two of three ponds; poor in the pond dominated by picoplankton; phycocyanin did not correlate well with cell counts; chlorophyll was a poor measure of cyanobacterial presence; relationship varied with dominant taxa | Directly comparable; shows taxon/depth/size dependence |
| **Hodges et al. 2018**, *Environmental Science and Pollution Research*, DOI 10.1007/s11356-017-0473-5 | Five phycocyanin sensors from three manufacturers; cultures + 30 field samples | Strong culture relationships for single-celled/filamentous taxa; weak for colonial *Microcystis*; field phycocyanin vs biovolume R² = 0.22–0.29 for two sensors and non-significant for a third; manufacturer, temperature, and morphology affected readings | Strong evidence that sensor–biovolume relationships are instrument- and morphology-dependent |
| **Thomson-Laing et al. 2020**, *Harmful Algae*, DOI 10.1016/j.hal.2020.101869 | CyanoFluor handheld vs cyanobacterial biovolume; 12 strains + four lakes weekly for 12 weeks | Strong overall relationships (r² ≥ 0.78), but lake-specific r² = 0.06–0.90; differences in phycocyanin per biovolume among strains and lakes; lysis improved repeatability | Shows that even a well-calibrated handheld sensor has lake-specific relationships |
| **Rogora et al. 2023**, *Frontiers in Environmental Science*, DOI 10.3389/fenvs.2022.1058515 | Lake Maggiore Cyclops7 vs 0–20 m microscopy, 2020–2021 | Good overall chlorophyll–biovolume relationship (R² = 0.72, n = 23); community composition mattered; cyanobacteria/picocyanobacteria were underestimated at low chlorophyll; nighttime sampling recommended to reduce quenching | Closest depth-integrated vs surface-sensor analogue; shows composition effects |
| **USGS SIR 2024-5010**, DOI 10.3133/sir20245010 | Finger Lakes, NY; high-frequency sensors vs laboratory chlorophyll and phytoplankton biovolume, 2019–2020 | Chlorophyll correlated moderately with lab chlorophyll-a; relations with total phytoplankton biovolume were weaker; phycocyanin vs cyanobacterial biovolume was **not significant**; chlorophyll from cyanobacteria (multichannel) was moderately strong; water temperature was among the strongest correlates; turbidity was more informative than dual-channel phycocyanin; models had limited explanatory power, possibly because no CyanoHABs occurred at the open-water sites | Strong negative/mixed evidence; directly relevant to the proposed phycocyanin question |
| **Kovalenko et al. 2026**, *Limnology and Oceanography: Methods*, DOI 10.1002/lom3.70033 | Laurentian Great Lakes; fluorometry vs microscopy | Chlorophyll correlated with total biovolume; stronger in spring than summer; weakest for summer deep chlorophyll layer; diatoms most consistent; cyanobacteria, green algae, and cryptophytes weak | Multi-lake evidence that group-specific relationships are weak and seasonal |
| **Cotterill et al. 2019**, *New Zealand Journal of Marine and Freshwater Research*, DOI 10.1080/00288330.2019.1617322 | Cyclops-7 vs cyanobacterial biovolume, five lakes and a river | Weak and variable relationships (<R² 0.4); species-specific detection limits | Direct prior art for the phycocyanin–biovolume question |
| **Levi et al. 2025**, *Open Research Europe*, DOI 10.12688/openreseurope.17146.3 | 24 chlorophyll and 12 phycocyanin Cyclops-7F sensors; mesocosms | Calibration, biofouling, community composition, nighttime sampling, and high-frequency events affect performance | Confirms sensor-specific, condition-dependent behavior |

**Synthesis:** The literature already establishes that:

- chlorophyll often tracks total phytoplankton biovolume better than it tracks cyanobacteria specifically;
- phycocyanin–cyanobacteria relationships are often weak, variable, and taxon/morphology-dependent;
- depth-integrated vs surface comparisons can be good for total biomass but poor for specific groups;
- season, community composition, temperature, quenching, fouling, and instrument model matter;
- negative or non-significant results are common.

The proposed study would test these known issues in two specific lakes, not discover them.

### 3.2 Depth mismatch is already recognized

- Rogora et al. 2023 compared a 1.5 m surface sensor with 0–20 m integrated microscopy and found a good total-biovolume relationship but composition-dependent deviations.
- The USGS Finger Lakes study used near-surface sensors and discrete samples at multiple depths; it found weaker relations with total biovolume and non-significant phycocyanin–cyanobacterial biovolume relations.
- The general literature on surface vs depth-integrated chlorophyll shows that surface values can diverge from column integrals, especially under stratification and deep chlorophyll maxima.
- Mendota’s 0.5 m vs 0–8 m mismatch is therefore not a novel problem; it is a well-known measurement issue.

**What is not established:** a controlled, same-lake test that isolates depth alignment from instrument, community, and period. The proposed two-lake comparison cannot provide that either, because lake identity is confounded with depth.

### 3.3 Seasonality and community composition are already recognized

- Kovalenko et al. 2026 found stronger fluorometry–microscopy relationships in spring than summer, and weakest relationships for summer deep chlorophyll layers.
- Hartmann et al. 2019 found group-specific agreement, with cyanobacteria often underestimated.
- Bowling et al. 2016 found taxon-dependent phycocyanin–biovolume relationships, with picoplankton causing poor performance.
- Hodges et al. 2018 found morphology and temperature effects.
- Rogora et al. 2023 found cyanobacteria/picocyanobacteria underestimated at low chlorophyll.
- Painter et al. 2022 reported an autumn *Planktothrix* bloom in Buffalo Pound that formed >60% of phytoplankton biomass but was not detected by sensor or laboratory chlorophyll-a.

**Implication:** A seasonal/era stratification of sensor–microscopy associations is a reasonable descriptive analysis, but it is not novel. The literature already predicts that relationships vary by season and community.

### 3.4 Turner/YSI non-comparability is already documented at Mendota

- The Mendota EML states that Turner and YSI both output RFU but have “significant magnitude differences.”
- The 2019 paired medians differ by orders of magnitude: chlorophyll 1,354.74 vs 0.39; phycocyanin 802.01 vs 0.59.
- No cross-calibration is provided.
- Carpenter et al. 2020/2022 used Mendota high-frequency phycocyanin and documented sensor/regime changes; they did not provide a Turner–YSI conversion.

**Implication:** Treating Turner and YSI separately is necessary, but it is not a novel contribution. It is a data-quality requirement.

### 3.5 Mendota and Buffalo Pound are already studied

- Mendota: NTL-LTER phytoplankton since 1995; buoy since 2006; Carpenter et al. 2020/2022 on high-frequency phycocyanin; Beal et al. 2021/2022 on forecasting.
- Buffalo Pound: Painter et al. 2022 on 2018–2019 bloom phases; Painter et al. 2023 on blooms/flows; Boyer et al. 2025 on 2017 bloom development and nitrogen fixation; Baulch et al. 2025 on the buoy dataset.
- Both lakes have prior sensor and microscopy work. Site novelty is weak.

### 3.6 Technical guidance already defines RFU as a proxy

- USGS TM1-D10 states that algal fluorometers are proxy sensors, RFU is sensor-specific, calibration checks should be routine, and biofouling/blank corrections require site-specific evidence.
- The Buffalo Pound data paper states that chlorophyll and phycocyanin are reported in RFU, limiting analyses without lab-based concentration measurements.
- The Mendota EML documents sensor changes, fouling, and maintenance but not per-record calibration.

**Implication:** The proposed study’s careful QC is good practice, not a new method.

## 4. What is genuinely distinctive, if anything

### 4.1 Candidate distinctions

| Candidate distinction | Is it distinctive? | Assessment |
|---|---|---|
| Two lakes with different depth alignment (Mendota 0.5 m vs 0–8 m; Buffalo Pound 0.82 m vs 0.8 m) | **Weak/moderate** | The contrast is interesting, but lake identity is confounded with instrument, period, community, sampling, and endpoint. It cannot isolate depth. |
| Long Mendota record (2006–2020; 128/139 Turner dates) | **Weak** | Long records exist; the same-day overlap is only 128/139, and the sensor is 0.5 m vs 0–8 m. Long record ≠ novel question. |
| Two-season Buffalo Pound record (42 dates) | **Weak** | Small; already described by Painter et al. 2022. |
| Separate Turner/YSI era analysis | **Not distinctive** | Necessary data hygiene; already documented as non-comparable. |
| Seasonal stratification | **Not distinctive** | Established in prior literature. |
| Use of Spearman/rank association | **Not distinctive** | Standard descriptive statistic. |
| Explicit refusal of absolute agreement | **Methodologically honest, not novel** | Good practice; not a scientific discovery. |
| Reproducible QC/missingness audit | **Useful, not novel** | Contributes to transparency, not new knowledge. |
| Two-lake side-by-side comparison | **Weak** | Descriptive; confounded; no generalisation. |

### 4.2 What is not distinctive

- Combining two lakes.
- Using high-frequency sensors.
- Using chlorophyll/phycocyanin fluorescence.
- Using Spearman correlation.
- Using seasonal stratification.
- Using a QC sensitivity analysis.
- Reporting a negative or weak result.
- Using public data.

These are all standard. None supports a novelty claim.

### 4.3 The strongest legitimate contribution

The strongest legitimate contribution is:

> A transparent, reproducible, two-case measurement audit showing how well surface pigment fluorescence ranks with independent microscopy-derived cyanobacteria abundance under a depth mismatch (Mendota) and a depth alignment (Buffalo Pound), with explicit QC, seasonal, era, and anomaly sensitivity — including the possibility that the answer is “weakly” or “not consistently.”

This is a **measurement/comparability** contribution, not an early-warning method. It is scientifically defensible because it can produce a negative or limited result. It is modest because the literature already predicts weakness and variability.

## 5. Originality verdict

**Originality: LOW–MODERATE.**

Reasons:

1. The core question — whether chlorophyll/phycocyanin fluorescence tracks microscopy-derived cyanobacteria abundance — has been studied repeatedly (Hartmann 2019; Bowling 2016; Hodges 2018; Thomson-Laing 2020; Rogora 2023; USGS 2024; Kovalenko 2026; Cotterill 2019; Levi 2025).
2. The expected answer is already known to be “sometimes, weakly, and taxon/season/instrument-dependent.”
3. The two-lake depth contrast is confounded and cannot isolate depth alignment.
4. The data are existing public records, not a new experiment.
5. The statistical method is standard.
6. The project cannot claim novelty from matched FAR, a new algorithm, a new sensor, or dataset availability.

**What the study can still be:** a rigorous, honest, reproducible local measurement audit that tests whether the expected weakness appears in these two specific settings, and documents the limits of using surface RFU as a cyanobacteria proxy. That is a legitimate school-level science project if framed as a measurement test, not a discovery.

**What it cannot be:** a novel early-warning method, a validated sensor, a bloom-detection system, or a generalisable multi-lake model.

## 6. What additional contribution would raise originality

To move from “modest measurement audit” to a stronger contribution, at least one of the following would be required:

1. **Depth-resolved paired sampling at the buoy.** Profiles of chlorophyll/phycocyanin and microscopy at multiple depths, same time, same station. This would allow a real depth-alignment test.
2. **Time-stamped, sub-weekly biology.** Sample times and intervals short enough to resolve onset/termination and diel cycles. This would support a temporal-matching study, though not necessarily early warning.
3. **Taxon-specific pigment-to-biovolume calibration.** Cultures and field samples across morphologies, temperatures, and colony sizes, with independent validation. This would address the known *Microcystis*/*Planktothrix* problems.
4. **Standardised multi-lake intercomparison.** Same sensors, same protocols, same calibration, multiple lakes/seasons. This would support generalisation.
5. **Independent event/non-event labels and a matched-FAR design.** This would be required for the original early-warning question, but the project does not have it.
6. **Verified toxin/community data.** This would allow a toxicity or taxon-specific detection question, but the current toxin files are not analysis-ready.

Without at least one of these, the study remains incremental.

## 7. Competition implications

The 4L.11 competition assessment found that the narrowed measurement study is feasible and defensible, with moderate originality/competition fit. This update sharpens that view:

- **SciFest / school-level:** A well-designed measurement audit with a clear question, transparent QC, and an honest negative/limited result can be competitive. Judges value reproducibility and critical thinking. The project should not claim early warning or novelty.
- **Earth Prize / GENIUS:** These competitions often value applied impact and innovation. A measurement audit may be seen as incremental unless it connects to a decision-relevant problem (e.g., “can a lake manager trust a surface sensor as a cyanobacteria proxy?”) and includes a clear management implication.
- **ISEF / EUCYS:** These are research-science competitions. A descriptive two-lake audit with modest novelty may struggle against projects with new methods, experiments, or mechanistic insight. A strong negative result and rigorous statistics can help, but the absence of a novel contribution is a risk.

**Bottom line:** The study is sufficient for a rigorous school-level measurement project, not for a top-tier novelty claim. If the competition requires a novel early-warning contribution, the project should **PAUSE** rather than stretch the measurement study into an early-warning claim.

## 8. What would change the originality verdict

The verdict would move upward only if:

- a genuinely controlled depth comparison is added;
- a taxon-specific calibration with independent validation is added;
- a multi-lake standardised dataset is added;
- a decision-relevant management application is rigorously evaluated;
- a preregistered negative result is framed as a contribution to measurement uncertainty (still modest).

The verdict would not change merely by:

- adding more years of the same data;
- adding more correlations;
- using a different statistic;
- combining the two lakes;
- claiming “first” without a systematic search.

## 9. Source access and limitations

- Full text or full data/metadata inspected: Rogora et al. 2023; USGS SIR 2024-5010 (XML); Baulch et al. 2025 (PMC); Painter et al. 2022 dataset/README and project audits (paper abstract only); Carpenter et al. 2022 (prior sprint full PMC); Levi et al. 2025 (prior sprint full PMC).
- Abstract/metadata only: Hartmann et al. 2019; Bowling et al. 2016; Hodges et al. 2018; Thomson-Laing et al. 2020; Kovalenko et al. 2026; Cotterill et al. 2019; Rousso et al. 2021.
- Publisher 403/blocked: Taylor & Francis, Wiley, MDPI, ScienceDirect in some attempts; used abstracts/search-index/project audits, not full text.
- No systematic-review claim. The absence of an exact two-lake study in the accessible literature is **not** evidence of novelty.
- No external contact, upload, commit, or push was made.

## 10. Governance

- **Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- This document does not approve the study. It informs the human decision on whether the originality is sufficient.
- No analysis may begin until the protocol is reviewed and explicitly approved.
