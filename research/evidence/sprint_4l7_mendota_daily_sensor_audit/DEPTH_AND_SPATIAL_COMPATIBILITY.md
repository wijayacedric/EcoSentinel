# Depth and Spatial Compatibility

**Date:** 2026-11-24T08:45:50.090661+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

| variable | documented_depth | measurement | biological_reference | classification | reason |
|---|---|---|---|---|---|
| avg_do_wtemp | 0.5 m | water temperature | 0-8 m composite | Weakly comparable | surface point vs column composite |
| avg_do_sat | 0.5 m | DO % saturation | 0-8 m composite | Weakly comparable | surface point vs column composite |
| avg_do_raw | 0.5 m | DO mg/L | 0-8 m composite | Weakly comparable | surface point vs column composite |
| avg_ph | 0.5 m | pH | 0-8 m composite | Weakly comparable | surface point vs column composite |
| avg_spec_cond | 0.5 m | specific conductance | 0-8 m composite | Weakly comparable | surface point vs column composite |
| avg_turbidity | 0.5 m | turbidity | 0-8 m composite | Weakly comparable | surface point vs column composite |
| avg_chlor_rfu_turner | 0.5 m | chlorophyll RFU | 0-8 m composite | Weakly comparable | proxy; sensor-specific; 2006-2019 |
| avg_chlor_rfu_ysi | 0.5 m | chlorophyll RFU | 0-8 m composite | Weakly comparable | proxy; sensor-specific; 2019+ |
| avg_phyco_rfu_turner | 0.5 m | phycocyanin RFU | 0-8 m composite | Weakly comparable | proxy; sensor-specific; 2006-2019 |
| avg_phyco_rfu_ysi | 0.5 m | phycocyanin RFU | 0-8 m composite | Weakly comparable | proxy; sensor-specific; 2019+ |
| avg_pco2_ppm | 1 m | pCO2 | 0-8 m composite | Weakly comparable | single depth; no biological counterpart |
| avg_par_below | 1 m | underwater PAR | 0-8 m composite | Weakly comparable | light context, not biomass |
| avg_par | 2 m above water | above-water PAR | 0-8 m composite | Not comparable | atmospheric context |
| meteorology | 2-3 m above water | air temp/RH/wind | 0-8 m composite | Not comparable | atmospheric context |

## Spatial

- Buoy and Microbial Observatory are documented at the Lake Mendota Deep Hole; coordinates in the EML are approximately 43.0995, -89.4045.
- 88.31 is sampled at the deep hole region; however, `sta` is blank for most biology records, so per-sample station linkage is weak.
- **Site-level spatial compatibility: strongly documented (metadata). Per-sample linkage: weak/conditional.**

## Depth interpretation

- Mendota biology is generally a **0–8 m composite**.
- Sensor chlorophyll/phycocyanin/DO/pH/conductance/turbidity are documented at **0.5 m**; pCO2 at 1 m; PAR above/below at 2/1 m.
- A surface point measurement is not the 0–8 m composite. A future comparison must define a comparator (surface layer, euphotic-zone integration, or whole-column biomass) and test sensitivity.
- **No claim is made that surface sensors represent the whole water column.**

## Classification summary

- Strongly documented: buoy/Deep Hole site correspondence (metadata).
- Conditionally comparable: none at variable level until raw data and comparator are defined.
- Weakly comparable: 0.5 m temperature, DO, pH, conductance, turbidity, chlorophyll/phycocyanin, pCO2; 1 m PAR-below.
- Not established: 0–8 m composite equivalence; across-era sensor comparability; station-level biology linkage.
