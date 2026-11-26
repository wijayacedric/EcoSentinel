# One-Page Protocol — Narrowed Measurement/Comparability Study

**Sprint 4L.12 · PROPOSED — NOT APPROVED · Gate 2: PAUSED / Option C (Exploratory Only) · 2026-11-24**  
**No analysis may begin until this protocol is reviewed and explicitly approved.**

## Question

> In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day paired observations and analysed separately by lake and sensor era, what are the direction, strength and descriptive uncertainty of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations vary by season and depth-alignment setting?

**Descriptive measurement/comparability study — not early-warning validation, bloom detection, calibration, or toxicity assessment.**

## Design and estimands

- Unit: **lake–date**. Sensor readings and taxon rows are subsamples/components, never independent observations.
- Mendota: 0.5 m sensor vs 0–8 m microscopy composite; Turner 2006–2019 primary; YSI 2019–2020 secondary.
- Buffalo Pound: 0.82 m sensor vs 0.8 m sample; YSI 6600, 2018–2019.
- Turner and YSI are **never concatenated**. Mendota biovolume and Buffalo Pound biomass are **never pooled**.

| ID | Lake / era | Sensor | Endpoint | Max n |
|---|---|---|---|---|
| P1 | Mendota / Turner | Chlorophyll RFU | Cyanobacteria biovolume | 128 |
| P2 | Mendota / Turner | Phycocyanin RFU | Cyanobacteria biovolume | 139 |
| P3 | Buffalo Pound / YSI 6600 | Chlorophyll RFU | Cyanobacteria biomass | 42 |
| P4 | Buffalo Pound / YSI 6600 | Phycocyanin RFU | Cyanobacteria biomass | 42 |

Mendota endpoint: sum `biovolume_conc` for `division = Cyanophyta`, `depth_range = 0-8m`, µm³ mL⁻¹. Buffalo Pound endpoint: sum `Biomass_mg_m3` for `Group = Cyanophyte`, `Depth = 0.8`, mg m⁻³.

## Inclusion and matching

- Mendota: `lakeid = ME`; 0–8 m only; 2006-07-09 to 2020-12-10; broad cyanobacteria total.
- Buffalo Pound: 2018–2019; 0.8 m; broad cyanophyte total.
- Exclude: Mendota 0–2 m dates; relative total biovolume; 2006 conductance; pH/fDOM/turbidity/conductance outside 2019–2020 from primary; PAR/pCO2/weather; Buffalo Pound deep sensors, thermistors, YSI profiles, toxins, nutrients, heterocytes.
- Raw data preserved. No imputation, interpolation, zero-fill, or derived endpoint.
- **Primary matching: same calendar date only.** Date-only biology; no sample time.
- Mendota: provider daily mean of 1-minute data; no nighttime reconstruction.
- Buffalo Pound: mean of valid 10-minute values; ≥50% of expected values and both halves of the day represented.
- **Sensitivity: ±1-day window only.** No ±3/±7/±14-day windows; no lags, onset, or lead time.

## QC

- Mendota: exclude `C`, `E`, `G`, `O`; retain numeric `H` if plausible; exclude negative pigments. Strict-unflagged (`H` excluded) is a sensitivity.
- Buffalo Pound: blank flag only; exclude `M`, `C`, `B7`; B7-inclusive sensitivity.
- “Unflagged” ≠ “validated.” Flags, missingness, and anomalies are reported; included vs excluded dates compared descriptively.
- 2019-07-17 Buffalo Pound anomaly is retained and flagged; exclusion is a sensitivity, not a correction.
- No detection limits or per-record calibration; RFU is a relative signal.

## Statistics

- **Primary: Spearman’s ρ** with n and a descriptive bootstrap interval.
- Mendota: year-cluster bootstrap (2,000 replicates). Buffalo Pound: naive date-level bootstrap (2,000) plus separate 2018/2019 estimates; interval labelled anti-conservative.
- **Secondary: Pearson r on log10(1+x)** as a scale check; no p-values.
- **No p-values, hypothesis tests, models, thresholds, calibration, Bland–Altman, concordance, prediction, or matched FAR.**
- Seasonal: calendar spring/summer/autumn; no stratum ρ if n<10; no interaction test.
- All secondary/exploratory analyses labelled; all sensitivity analyses reported.

## Claims

**Permitted:** “In the included dates, [pigment] showed a [direction] rank association with [endpoint] (Spearman ρ = ..., n = ...).” “The descriptive pattern was [similar/different] across seasons/eras/settings, with [n] and [confounders].” “The two lake settings differ in depth alignment, but the comparison is confounded and cannot isolate a depth effect.”

**Prohibited:** validation; accuracy; prediction; forecast; early warning; lead time; bloom detection; bloom/non-bloom classification; toxicity; whole-water-column biomass; absolute agreement; Turner/YSI interchangeability; causal depth effect; generalisation to other lakes.

## Decisions required before analysis

1. Accept rank association (not absolute agreement) as “comparability.”
2. Accept Buffalo Pound biomass as endpoint; no derived biovolume.
3. Accept Mendota 0.5 m vs 0–8 m with no depth correction.
4. Keep Turner/YSI separate; no cross-calibration.
5. Approve primary QC rule (retain `H`; exclude `C/E/G/O`; BP blank only).
6. Approve full-day means (BP nighttime as sensitivity).
7. Approve same-day + ±1-day only.
8. Approve BP replicate mean (sum/first as sensitivity).
9. Approve retaining 2019-07-17 with exclusion sensitivity.
10. Approve bootstrap/no-p-value uncertainty.
11. Approve n<10 stratum reporting rule.
12. Approve claims matrix.
13. Decide whether a modest/negative measurement study is sufficient; if a novel early-warning result is required, **PAUSE**.
14. Complete licence/competition review.
15. Record explicit approval to begin analysis.

**If any decision is unresolved, the status remains PROPOSED — NOT APPROVED and no analysis may begin.**
