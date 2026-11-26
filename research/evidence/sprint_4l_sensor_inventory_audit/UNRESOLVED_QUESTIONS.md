# Unresolved Questions — Sensor Inventory

**Date:** 2026-11-23T23:48:59.424593+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

1. **Exact within-year transition dates.** The file gives years only. When in 2017 (Temp/RH), 2018 (DO), 2019 (DO/Chlor-Phyco/pH/conductivity/fDOM/turbidity), 2013 (wind/IR), 2016 (DO/PAR), and 2007 (water temp) did switches occur?
2. **Meaning of "present."** Is it still operational at EML publication (pubDate 2026-11-19), or merely "through the latest data revision"?
3. **Depths per sensor.** The file has no depth column. What depth is the RBR Concerto water temperature? Are YSI pH/conductivity/turbidity/fDOM at 0.5 m like chlorophyll? What is the IR skin temp field of view?
4. **Serial numbers / calibration.** No serials, calibration dates, coefficients, accuracy, or drift information. Can these be recovered from NTL documentation or raw data flags?
5. **Overlapping sensors.** In 2018 (D-Opto/miniDOT) and 2019 (Turner/YSI Chlor-Phyco), were sensors co-deployed for intercomparison or swapped mid-season?
6. **Turner vs YSI comparability.** Are chlorophyll/phycocyanin RFU from the two vendors directly comparable, or is a cross-calibration needed?
7. **Conductivity gap.** Why is there no buoy conductivity 2007-2018, and what model was the 2006 YSI sensor? Can 415.2 handheld conductivity fill the gap?
8. **Mapping to 129.42 columns.** Which daily/hourly/HR columns correspond to each sensor row (e.g., `avg_chlor_rfu_turner` vs `avg_chlor_rfu_ysi`; `avg_do_*`; `avg_phyco_*`)? The EML lists columns but the mapping to transition years needs verification.
9. **130.29 relationship.** Is the RBR Concerto water temperature a single sensor or part of the thermistor chain? How does it relate to the separate 130.29 temperature profiles?
10. **415.2 cross-calibration.** Can the handheld YSI Pro Plus (2014-2019) be used to cross-check buoy sensors? Depth/time matching is needed.
11. **QC flags and failures.** Which sensor rows correspond to `C` (sensor off), `E` (noisy/malfunctioning), or `H` (outside range) flags in the data? The sensor file alone does not say.
12. **Completeness of this list.** Does the file list all buoy sensors (e.g., thermistor chain, battery, additional PAR) or only selected ones? The EML says "not all sensors are deployed each season."

## What would resolve these

- Raw 129.42 daily/hourly/HR data + EML methods/QA documentation.
- NTL sensor/calibration logs or data-provider documentation.
- 130.29 temperature metadata/data.
- 415.2 handheld data for cross-checks.
- Authorised access only; no contact/credentials in this sprint.
