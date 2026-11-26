# Scientific Interpretation Challenge

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. Is the 4L.9 verdict too optimistic, too pessimistic, or insufficiently qualified?

**Insufficiently qualified; directionally correct.**

- For **A (seasonal descriptive)**, 4L.9 is appropriately cautious: multi-year daily series exist, but the record is open-water, variable-specific and era-specific.
- For **B (descriptive sensor–cyanobacteria comparison)**, 4L.9 says “partially supported”, which is defensible only if “comparison” means pairwise descriptive patterns. It becomes too optimistic if read as sensor validation or quantitative proxy calibration.
- For **C (multivariate)**, 4L.9 says “limited/not robustly supported”, which is directionally right, but the new joint-coverage calculation shows it is weaker than the label suggests for sensor–biology work: only **58/402 (14.4%)** biology dates support a 7-variable Turner core, and **2/402 (0.5%)** support the 11-variable YSI core.
- For **D (early-warning validation)**, 4L.9 is correct: not supported.

Thus the overall phrase “EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS” should not be used as a green light for sensor–biology validation or early-warning work. It is a green light only for limited descriptive use.

## 2. Biological endpoint

- The microscopy data are a **separate measurement pipeline** from the buoy sensors. They are not derived from the same optical signal.
- They are **not statistically independent of the lake**: both observe the same lake on the same dates, and both are affected by spatial heterogeneity, stratification and weather.
- They measure **cyanobacterial abundance/biovolume**, not bloom status, toxicity, surface scum, or onset.
- The record has no event labels, no toxin measurements, no sample time, no detection limits and no per-row QC flags.
- Cyanobacteria biovolume is the least problematic exploratory endpoint, but it is taxonomically non-stationary: 468 nonblank taxa names, 176 nonblank genera, 204 names only pre-2013 and 72 only post-2013; 889 genus-field mismatches; 8,514 trailing-space records; 12 blank taxon rows.
- It cannot establish a lead time for a bloom because a bloom is not defined and the sampling interval is ~14 days.

## 3. Temporal alignment

- Same-day overlap means **the same calendar date has both a microscopy sample and an unflagged sensor value**. It does not mean the same hour, water parcel or depth.
- **128** Turner chlorophyll and **139** Turner phycocyanin biology dates have same-day unflagged values. This is a useful availability count, not a paired time series.
- Only **165/402** biology dates have any same-day unflagged sensor variable; **165/230** within 2006–2020.
- The ±1/±3/±7/±14-day windows increase coverage modestly (e.g., Turner chlorophyll ±7 = 156/402; ±14 = 163/402). They are **not lead/lag estimates**: they mix different dates, weather and seasonal states. A ±7-day “match” could easily span a bloom onset and decline.
- A sparse biology series can make a sensor change appear to “lead” a biological change simply because the next biology sample is two weeks later. The data cannot distinguish that from a true lead.

## 4. Depth mismatch

- Sensors are at 0.5 m (chlorophyll, phycocyanin, DO, pH, conductance, turbidity, fDOM), 1 m (pCO2, PAR below) or above water (PAR, meteorology).
- Biology is 0–8 m composite on 400 dates; 2 dates are 0–2 m.
- Under stratification, surface chlorophyll/phycocyanin can be higher or lower than the column composite; vertical migration and surface scums add further decoupling.
- A 0.5 m sensor can describe **surface conditions**; it cannot establish **whole-column biomass**. No depth profile is available to quantify the offset.
- The buoy and NTL sampling site are ~**105.7 m** apart; station is blank for **371/402** dates. Site-level proximity is documented; per-sample spatial coincidence is not.

## 5. Instrument discontinuities

- Turner and YSI are different instruments. 2019 paired medians: chlorophyll **1,354.7 vs 0.39 RFU**; phycocyanin **802.0 vs 0.590 RFU**. The EML itself says “significant magnitude differences.”
- No cross-calibration equation or correction factor is present. Concatenating the eras would create an artificial step.
- Other changes: DO exists from 2006 but the inventory lists DO only from 2016; `avg_do_wtemp` is YSI-labelled but exists from 2006; pCO2 begins 2016 while the inventory says 2017; PAR has 2007 near-zero values; 2006 conductivity is ~0.4 µS/cm and all flagged.
- These transitions can produce artificial ecological signals if treated as homogeneous series.

## 6. QC and unflagged values

- `O` is undefined; eight flag columns contain values outside their daily-EML code lists.
- `C` is not equivalent to missing: 1,534 numeric `C` values for `avg_do_wtemp`, 668 for PAR below, 277 for DO raw, 118 for conductance, 113 for YSI chlorophyll.
- `H` is common (928 DO saturation, 734 DO raw, 157 air temperature, 124 wind speed, 82 conductance). Some `H` values are plausible extremes; others (2006 conductance) are not on the later scale.
- `G` is used only for YSI chlorophyll/phycocyanin and PAR below; its absence in the Turner era does not prove absence of fouling.
- Unflagged values are not automatically accurate: negative turbidity (31), negative YSI phycocyanin (62), negative YSI chlorophyll (1), negative PAR below (3), and 2006 conductance values ~0.4 µS/cm.
- The audit’s `valid_unflagged` label is defensible only with its explicit definition. It should not be read as “validated” or “ground truth”.

## 7. Multivariate analysis

- Sensor-only complete-case coverage is reasonable for era-specific descriptive work: **939** Turner-core dates and **306** YSI-core dates.
- Sensor–biology joint coverage is much smaller: **79/402 (19.7%)** for 3 Turner variables, **64/402 (15.9%)** for 4, **58/402 (14.4%)** for 7; **16/402 (4.0%)** for 3 YSI variables, **2/402 (0.5%)** for 5, **21/402 (5.2%)** for 6, **2/402 (0.5%)** for 11.
- Missingness, seasonality and sensor-era changes can dominate apparent multivariate relationships. A descriptive sensor-only analysis is possible; a biological multivariate analysis is not robust.

## 8. Prior-art constraint

- Mendota already has high-frequency phycocyanin research (Carpenter et al. 2020, 2022) and seasonal/sub-seasonal cyanobacteria forecasts (Beal et al. 2021, 2022).
- O'Brien et al. (2023) found that most early-warning indicators in empirical lake data, including Mendota, did not perform better than chance; multivariate indicators were weakly superior and machine learning performed poorly.
- Phycocyanin–biovolume validation is weak/variable (Cotterill et al. 2019; Levi et al. 2025).
- Therefore, no novelty can be claimed from Mendota’s dataset alone, and no early-warning validation is justified without new biological event data and a precise contribution.

## 9. Bottom line

The 4L.9 arithmetic is solid. Its scientific caution is mostly appropriate, but its single overall verdict **overstates the joint sensor–biology support** and should be replaced by the four separate verdicts in `VERDICTS_A_D.md`. Mendota remains useful for limited descriptive work; it is not an early-warning validation dataset.
