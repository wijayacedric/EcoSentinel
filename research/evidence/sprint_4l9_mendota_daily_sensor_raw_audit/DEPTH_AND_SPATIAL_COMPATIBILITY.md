# Depth and Spatial Compatibility

**Sprint:** 4L.9  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Sensor depths from the EML

- Chlorophyll, phycocyanin, DO, pH, specific conductance, turbidity and fDOM: **0.5 m**.
- pCO2: **1 m**.
- PAR above water: **2 m above the surface**.
- PAR below water: **1 m depth**.
- Meteorology: air temperature/RH **2 m above surface**; wind **3 m above surface**.

## 2. Biology depth

- **400** Mendota dates are labelled **0–8 m composite**.
- **2** dates are labelled **0–2 m**.
- The 0–8 m composite integrates over a depth range; the sensor values are point measurements at 0.5 m (or 1 m for pCO2/PAR).

## 3. Spatial setting

- EML buoy coordinates: approximately **43.0995, −89.4045**.
- NTL southern-lake sampling site coordinate for Mendota: approximately **43.09885, −89.40545**.
- These are about **106 m apart** (great-circle estimate); they are site-level neighbours, not an exact co-location.
- Per-sample station linkage is weak: station is blank for all rows on **371** of **402** dates; only **31** dates have any station value.

## 4. Compatibility table

| Variable | Sensor depth | Measurement | Biological reference | Classification | Reason |
|---|---|---|---|---|---|
| `avg_chlor_rfu_turner` | 0.5 m | chlorophyll RFU | 0-8 m composite | weak/conditional | surface point vs column composite; Turner-only era |
| `avg_chlor_rfu_ysi` | 0.5 m | chlorophyll RFU | 0-8 m composite | weak/conditional | surface point vs column composite; YSI-era only |
| `avg_phyco_rfu_turner` | 0.5 m | phycocyanin RFU | 0-8 m composite | weak/conditional | surface point vs column composite; Turner-only era |
| `avg_phyco_rfu_ysi` | 0.5 m | phycocyanin RFU | 0-8 m composite | weak/conditional | surface point vs column composite; YSI-era only |
| `avg_do_wtemp` | 0.5 m | water temperature | 0-8 m composite | weak/conditional | surface point vs column composite; pre-2019 provenance ambiguous |
| `avg_do_sat` | 0.5 m | DO % saturation | 0-8 m composite | weak/conditional | surface point vs column composite |
| `avg_do_raw` | 0.5 m | DO mg/L | 0-8 m composite | weak/conditional | surface point vs column composite |
| `avg_ph` | 0.5 m | pH | 0-8 m composite | weak/conditional | surface point vs column composite; short overlap |
| `avg_spec_cond` | 0.5 m | specific conductance | 0-8 m composite | weak/conditional | surface point vs column composite; short overlap |
| `avg_turbidity` | 0.5 m | turbidity | 0-8 m composite | weak/conditional | surface point vs column composite; short overlap |
| `avg_fdom` | 0.5 m | fDOM | 0-8 m composite | weak/conditional | surface point vs column composite; short overlap |
| `avg_pco2_ppm` | 1 m | pCO2 | 0-8 m composite | weak/conditional | single depth; no direct biological counterpart |
| `avg_par_below` | 1 m | underwater PAR | 0-8 m composite | weak/conditional | light context, not biomass; short overlap |
| `avg_par` | 2 m above water | above-water PAR | 0-8 m composite | not comparable | atmospheric context |
| `avg_air_temp` | 2 m above water | air temperature | 0-8 m composite | not comparable | atmospheric context |
| `avg_rel_hum` | 2 m above water | relative humidity | 0-8 m composite | not comparable | atmospheric context |
| `avg_wind_speed` | 3 m above water | wind speed | 0-8 m composite | not comparable | atmospheric context |
| `avg_wind_dir` | 3 m above water | wind direction | 0-8 m composite | not comparable | atmospheric context |

## 5. Interpretation

- A **0.5 m surface point** is not a **0–8 m composite**. The sensor may over- or under-represent the column depending on stratification, vertical migration, surface scums and light penetration. The data do not include a depth profile to quantify this.
- The two 0–2 m biology dates are a separate depth class and should not be pooled silently with the 0–8 m dates.
- Site-level proximity is documented, but the ~106 m offset and the mostly blank station field mean per-sample spatial coincidence is **not established**.
- Atmospheric variables (air temperature, RH, wind, above-water PAR) are contextual and are not directly comparable to the 0–8 m biological composite.
- pCO2 (1 m) and PAR below (1 m) are single-depth context variables, not biomass measures.

## 6. Conclusion

Depth/spatial compatibility is **weak/conditional** for all water-column variables and **not comparable** for atmospheric variables. A future analysis must define an explicit comparator (surface layer, euphotic-zone integration, or whole-column biomass) and test sensitivity; it cannot assume that 0.5 m sensors represent the 0–8 m composite.
