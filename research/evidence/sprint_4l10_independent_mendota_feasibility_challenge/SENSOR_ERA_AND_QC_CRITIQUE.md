# Sensor-Era and QC Critique

**Sprint:** 4L.10  
**Gate 2:** PAUSED / NOT APPROVED — option C (Exploratory Only)

## 1. Turner versus YSI

The independent recount confirms the 2019 paired comparison:

| Proxy | Paired dates | Turner median | YSI median | Median ratio | Non-positive Turner pairs |
|---|---:|---:|---:|---:|---:|
| Chlorophyll | 156 | 1,354.74 | 0.390 | 0.000332 | 0 |
| Phycocyanin | 160 | 802.01 | 0.590 | 0.000835 | 0 |

The EML states that both output RFU but have “significant magnitude differences.” No cross-calibration equation, correction factor or conversion is present. The ratio is **descriptive only**; it excludes zero/non-positive Turner values and is not a calibration. In the 2019 paired data there were **no non-positive Turner pairs**, so the exclusion has no effect here.

**Conclusion:** Turner and YSI are demonstrably non-comparable on the raw RFU scale. Concatenating them would create an artificial ecological step.

## 2. Other sensor discontinuities

- **DO:** daily values exist from 2006, but the sensor inventory lists DO only from 2016. The 2006–2015 instrument identity is unresolved. DO flags vary strongly by year.
- **Water temperature:** `avg_do_wtemp` is labelled “YSI water temp” but exists from 2006; 2019+ is heavily `C`-flagged (1,087 `C`; 371 unflagged of 1,612). It is not a clean continuous temperature series. Ancillary 130 is documented but not acquired.
- **pCO2:** data begin 2016-03-22; inventory says 2017. 2024 has only 70 unflagged values; 2025 has 177.
- **PAR:** 11 near-zero values in 2007, then no sustained record until 2016. 2019–2020 has major outages.
- **Conductivity:** 2006 values ~0.38–0.48 µS/cm, all `H`/`O`; 2019+ ~122–596 µS/cm. Not comparable.
- **pH/fDOM/turbidity:** 2019+ only.

These transitions can produce artificial signals if treated as homogeneous. Era-specific series are mandatory.

## 3. QC findings and their materiality

- **Undefined `O`:** one value in `flag_avg_spec_cond` (2006-08-11, 0.45). Its meaning is unknown. Materiality: low for the 2019+ conductance series; it reinforces that 2006 conductance is unusable.
- **Eight flag columns use undocumented values:** `rel_hum` H (6), `wind_speed` H (124), `par_below` H (90), `do_wtemp` E (3), `ph` E (1), `fdom` E (1), `turbidity` E (1), `spec_cond` E (17) and O (1). Materiality: high for interpreting those flags; the data cannot tell us whether the undocumented code means the same thing as the generic definition.
- **`C` with numeric values:** 1,534 for `avg_do_wtemp`, 668 for PAR below, 277 for DO raw, 118 for conductance, 113 for YSI chlorophyll. `C` cannot be treated as a missingness code. The audit correctly retains these values as flagged numeric; downstream analysis must define its own rule.
- **`H`:** 928 DO saturation, 734 DO raw, 157 air temperature, 124 wind speed, 82 conductance. Some are plausible extremes (supersaturated DO); some are era artefacts (2006 conductance). Do not equate `H` with “invalid” or with “accurate”.
- **`G`:** only YSI chlorophyll/phycocyanin and PAR below. The Turner era has no `G` flags; absence of `G` is not evidence of no fouling. The EML’s 2017 DO biofouling note is not a per-record flag.
- **Unflagged but implausible:** 31 negative turbidity, 62 negative YSI phycocyanin, 1 negative YSI chlorophyll, 3 negative PAR below, 2006 conductance ~0.4 µS/cm. `valid_unflagged` is not a validation label.
- **Missingness without flags:** Turner chlorophyll 1,424 empty-unflagged; YSI chlorophyll 2,440; pH 2,434; fDOM 2,434; turbidity 2,434; conductance 2,360. Most are structural, but the file does not carry a “not deployed” code for them.

## 4. Does the audit overstate reliability?

The 4L.9 report explicitly defines `valid_unflagged` as numeric with a blank flag and says it is not proof of accuracy. That is appropriate. The risk is **label drift**: a reader may treat “valid” as “validated”. The independent challenge recommends:

- call the field **`unflagged_numeric`** in any downstream analysis;
- report flagged values alongside unflagged values in sensitivity analyses;
- do not use `C` as missing, `H` as invalid, or `G` as the only fouling indicator;
- do not treat unflagged negatives as valid.

## 5. What would change the assessment

- A documented Turner/YSI cross-calibration with uncertainty.
- Per-record calibration, maintenance, serial number and detection-limit data.
- A reconciled sensor inventory with exact deployment dates and pre-2016 DO/pre-2019 temperature provenance.
- A flag dictionary that covers every observed code for every column.

Without these, the sensor record is usable only as era-specific, flag-aware descriptive data.
