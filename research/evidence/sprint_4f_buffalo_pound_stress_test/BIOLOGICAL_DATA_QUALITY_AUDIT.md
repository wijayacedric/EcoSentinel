# Biological Data Quality Audit — Buffalo Pound

**Date:** 2026-11-23T23:22:37.724583+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Verified content

| Year | Dates | Range | Median gap | Max gap | Taxon rows | Taxa | Cyano rows | Depth |
|---|---:|---|---:|---:|---:|---:|---:|---|
| 2018 | 25 | 2018-05-29 to 2018-09-17 | 4 d | 12 d | 817 | 73 | 170 | 0.8 m |
| 2019 | 17 | 2019-05-29 to 2019-10-03 | 8 d | 16 d | 405 | 56 | 78 | 0.8 m |

- **Measurement:** microscopy, species-level, `Cell_Density_L` (cells/L), `Biomass_mg_m3` (mg/m³), cell volume/dimensions.
- **Cyanobacteria genera:** 2018 includes Merismopedia, Planktolyngbya, Woronichinia, Planktothrix, Anabaena, Chroococcus, Microcystis, Aphanothece; 2019 includes Planktothrix, Anabaena, Woronichinia, Aphanizomenon, Microcystis, Merismopedia, Rhabdogloea.
- **Additional files acquired this sprint:** `BP_GroupsBiomass_2018/2019`, `BP_heterocytes_2018/2019`, `BP_YSI_2018/2019`, `2018/2019_phyto_matrix` (Borealis public files, SHA256 recorded).
- **Heterocytes:** Dolichospermum (2018/2019) and Aphanizomenon (2019); 23/17 dates; nonzero counts on 37/41 rows.
- **Group biomass:** 7 groups × 25 dates (2018), 7 × 17 (2019).
- **YSI profiles:** 20 dates (2018), 16 (2019), 0.2-4.0 m, temperature/conductivity/DO/pH.

## 2. Replicates and duplicates

- **2018:** no `REP` field; 25 unique `Sample_ID` values. 19 date-species groups have two rows with different densities/biomass (e.g., Woronichinia, Microcystis), consistent with counting replicates, but **no replicate identifier**; they are not independent dates.
- **2019:** `REP1` (12 dates) and `REP2` (5 dates) occur on **disjoint dates**, not paired replicates (17 dates total). The label does not provide a replicate estimate.
- Treating 1,222 taxon rows or 248 cyanophyte rows as independent observations would overstate effective sample size.

## 3. Method/schema changes

- 2018 header includes `Sample_ID`; 2019 header includes `REP` (and no `Sample_ID`).
- 73 taxa in 2018 vs 56 in 2019; only **39 shared**, 34 only 2018, 17 only 2019. This could reflect real community change, taxonomic-list changes, or both. Harmonisation is unresolved.
- No explicit detection-limit or identification-uncertainty field observed in the clean data.

## 4. Zeros/missing

- No empty cell-density/biomass values in the taxonomy rows; zeros are explicit. Some rows have zero length/width (e.g., colonial taxa), but biomass is populated.
- Toxins files have multi-row LOD/LOQ headers and are not analysis-ready without careful parsing; not used as an endpoint here.

## 5. Independence

The microscopy counts are **measurement-independent** of the buoy sensors (different method/instrument). They are not statistically independent of the same lake/season, and sampling dates may be influenced by field logistics. Independence does not solve the two-season limitation.

## 6. Conclusion

Biological data are genuine and scientifically valuable for exploratory work, but they are **not sufficient for confirmatory event/false-alarm evaluation**: too few seasons, inconsistent replicate encoding, taxonomic harmonisation unresolved, and no non-bloom baseline.
