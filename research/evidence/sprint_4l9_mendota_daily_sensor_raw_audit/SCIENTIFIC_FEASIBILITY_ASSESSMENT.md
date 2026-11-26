# Scientific Feasibility Assessment

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Final verdict: EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS.**

## 1. Summary judgement

The daily sensor file is real, structurally clean and extensive: **3,996** daily records from **2006-07-09** to **2025-11-18**, 18 variables, 18 flag columns, and no duplicate dates. It materially improves the environmental evidence base. It does **not** remove the core constraints: variable-specific missingness, undocumented flag semantics, sensor-era discontinuities, a 0.5 m vs 0–8 m depth mismatch, and a 14-day microscopy record with no sampling times.

## 2. The four requested uses

### A. Exploratory seasonal ecological analysis

**Verdict: SUPPORTED WITH MAJOR LIMITATIONS.**

Evidence:
- Air temperature, RH, wind, DO and (for 2006–2019) Turner chlorophyll/phycocyanin have multi-year records.
- YSI chlorophyll/phycocyanin and pH/fDOM/turbidity/conductance provide a 2019+ open-water series.
- The file supports descriptive seasonal plots and within-season summaries when the variable-specific denominator and flag rule are stated.

Limitations:
- The record is open-water (April–November), not year-round; winter has only 15 records.
- Missingness and flags are variable-specific and often concentrated in particular years.
- Sensor eras are not directly comparable; Turner/YSI must remain separate.
- A seasonal pattern is not a bloom label or a biological response estimate.

### B. Descriptive comparison with microscopy-derived cyanobacterial measurements

**Verdict: PARTIALLY SUPPORTED — EXPLORATORY ONLY.**

Evidence:
- The audited biology record supplies 402 Mendota dates and 0–8 m composite samples.
- Turner chlorophyll has **128** same-day unflagged values; Turner phycocyanin **139**; DO raw **99**; DO saturation **98**; `avg_do_wtemp` **94**.
- The strongest pairing is Turner chlorophyll/phycocyanin with cyanobacteria biovolume or cell density, 2006–2019.

Limitations:
- 0.5 m point sensor vs 0–8 m composite; no depth profile.
- RFU is a proxy, not a quantitative pigment or biovolume measurement; RFU is sensor-specific.
- The biology record is ~14-day, date-only, and taxonomically non-stationary.
- Same-day overlap is ~32–35% of all biology dates for the Turner proxies, not a complete paired time series.
- No causal, confirmatory or event-onset claim is supported.

### C. Investigation of multivariate environmental relationships over time

**Verdict: LIMITED / NOT ROBUSTLY SUPPORTED.**

Evidence:
- Several variables are co-measured on the same daily rows, enabling descriptive multivariate exploration.
- The 2019+ YSI suite provides a short multi-variable window.

Limitations:
- Strong collinearity among environmental variables (e.g., temperature, DO, season, light).
- Variable-specific missingness and flags; some variables exist only in 2019+.
- The biology response is sparse and not time-matched within days.
- Sensor-era changes create structural breaks.
- A descriptive multivariate exploration is possible; a robust inferential multivariate model is not justified by this audit.

### D. Any eventual early-warning evaluation

**Verdict: NOT SUPPORTED.**

Reasons:
- No bloom/non-bloom labels, event definitions or event intervals exist; creating them is prohibited under Gate 2.
- The biology record is ~14-day and date-only; it cannot resolve hours-to-days onset.
- The sensor is at 0.5 m; the biology is a 0–8 m composite.
- Fluorescence is a proxy affected by community composition, physiology, light history, temperature and biofouling.
- Same-day overlap is partial and concentrated in specific years.
- Daily data alone do not establish that an environmental change precedes a biological bloom.

## 3. Detecting environmental change vs detecting cyanobacterial change vs predicting a bloom

These are different claims:

1. **Detecting environmental change** — supported descriptively for several variables, with caveats about flags, gaps and era changes.
2. **Detecting cyanobacterial abundance change** — partially supported only through proxy fluorescence and sparse microscopy; not a direct abundance measurement.
3. **Identifying bloom onset** — not supported: no event definition, no sub-weekly biology, no intraday sampling time.
4. **Predicting a future bloom** — not supported: no labels, no validated precursor window, no out-of-sample design, no independent biological validation.

The daily file improves (1) and, cautiously, (2). It does not establish (3) or (4).

## 4. What the evidence establishes

- The daily entity is authentic and structurally sound.
- All 18 variables are present, but coverage is variable-specific and era-specific.
- The strongest long-run biological proxies are Turner chlorophyll/phycocyanin (2006–2019).
- The 2019+ YSI suite is too short, relative to the biology, for long-term comparison.
- Same-day biology–sensor overlap is partial and day-level only.
- Depth/spatial compatibility is weak/conditional.
- Flag metadata are incomplete/inconsistent in eight columns, including an undefined `O` code.

## 5. What remains unknown

- Per-record calibration history, coefficients, serial numbers and detection limits.
- Exact sensor change dates within years.
- The identity/provenance of pre-2016 DO and pre-2019 `avg_do_wtemp`.
- Whether flagged `H`/`E` values are erroneous, extreme-but-real, or era artefacts.
- Whether the 0.5 m sensor is representative of the 0–8 m composite at any given date.
- Whether a validated Turner–YSI crosswalk exists outside the EML.
- Whether the microscopy taxonomy can be harmonised for longitudinal species-level analysis (a separate biological task).
- Any protocol-approved bloom/non-bloom definition.

## 6. Final verdict

**EXPLORATORY FEASIBILITY SUPPORTED WITH MAJOR LIMITATIONS.**

The dataset can support descriptive, variable-specific, open-water-season exploratory work and a cautious descriptive comparison with microscopy-derived cyanobacteria. It cannot support confirmatory modelling, bloom labels, event intervals, hypothesis tests or early-warning claims. **Gate 2 remains PAUSED / NOT APPROVED.**
