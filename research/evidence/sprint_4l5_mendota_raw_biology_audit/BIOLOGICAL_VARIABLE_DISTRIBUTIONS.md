# Biological Variable Distributions

**Date:** 2026-11-24T07:22:12.805937+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Overall distribution

| variable | n | missing | zeros | negative | nonfinite | min | p01 | p25 | median | p75 | p95 | p99 | max | mean |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gald | 18654 | 0 | 3 | 0 | 0 | 0.0 | 0.8 | 4.4 | 12.0 | 36.0 | 133.380095 | 280.0 | 3200.0 | 34.071945 |
| cells_per_nu | 18654 | 0 | 1 | 0 | 0 | 0.0 | 1.0 | 1.0 | 1.0 | 10.5 | 52.5 | 150.0 | 48000.0 | 15.57716 |
| nu_per_ml | 18654 | 0 | 0 | 0 | 0 | 0.1704 | 0.6583 | 18.1754 | 75.7308 | 520.868 | 11772.43025 | 56128.9073 | 357259.5436 | 2613.500244 |
| cells_per_ml | 18654 | 0 | 1 | 0 | 0 | 0.0 | 1.2781 | 38.9473 | 227.1924 | 2439.1405 | 37519.23905 | 157198.924202 | 10074657.1215 | 10587.725757 |
| biovolume_conc | 18654 | 0 | 3 | 0 | 0 | 0.0 | 43.061753 | 1563.276675 | 6578.0223 | 30543.52725 | 435845.369135 | 2410111.734524 | 84070000.0 | 133607.29886 |
| biomass_conc | 18654 | 0 | 64 | 0 | 0 | 0.0 | 4e-05 | 0.001573 | 0.006589 | 0.030589 | 0.437 | 2.448085 | 84.6924 | 0.138148 |
| relative_total_biovolume | 18654 | 0 | 18 | 0 | 0 | 0.0 | 0.003 | 0.091 | 0.406 | 1.98275 | 23.5249 | 72.32871 | 283806.87 | 19.459943 |

## By-lake distribution (selected statistics)

| variable | scope | n | zeros | median | p95 | max |
|---|---|---|---|---|---|---|
| gald | ME | 9401 | 0 | 12.0 | 130.4 | 3200.0 |
| gald | MO | 8696 | 0 | 13.2 | 138.616675 | 1300.0 |
| gald | WI | 532 | 3 | 12.2 | 130.45 | 800.0 |
| gald | FI | 25 | 0 | 14.667 | 145.7032 | 647.167 |
| cells_per_nu | ME | 9401 | 1 | 1.0 | 50.0 | 48000.0 |
| cells_per_nu | MO | 8696 | 0 | 1.0 | 55.0 | 2500.0 |
| cells_per_nu | WI | 532 | 0 | 1.0 | 45.45 | 181.8182 |
| cells_per_nu | FI | 25 | 0 | 1.0 | 34.1144 | 147.083 |
| nu_per_ml | ME | 9401 | 0 | 68.1577 | 10942.472 | 271714.9378 |
| nu_per_ml | MO | 8696 | 0 | 75.7308 | 11870.331 | 233445.2282 |
| nu_per_ml | WI | 532 | 0 | 136.3154 | 44417.901125 | 357259.5436 |
| nu_per_ml | FI | 25 | 0 | 52.087 | 7000.4718 | 11823.713 |
| cells_per_ml | ME | 9401 | 1 | 190.982 | 31100.1122 | 1244658.54 |
| cells_per_ml | MO | 8696 | 0 | 254.4555 | 38790.99675 | 886662.0225 |
| cells_per_ml | WI | 532 | 0 | 408.9463 | 219488.765575 | 10074657.1215 |
| cells_per_ml | FI | 25 | 0 | 59.182 | 7951.78926 | 11823.713 |
| biovolume_conc | ME | 9401 | 0 | 5518.4683 | 349300.0 | 23370568.07 |
| biovolume_conc | MO | 8696 | 0 | 7384.67735 | 488913.490225 | 84070000.0 |
| biovolume_conc | WI | 532 | 3 | 15321.7419 | 836495.3688 | 6219433.6609 |
| biovolume_conc | FI | 25 | 0 | 13020.954 | 499040.0 | 923400.0 |
| biomass_conc | ME | 9401 | 27 | 0.005516 | 0.3513 | 84.6924 |
| biomass_conc | MO | 8696 | 34 | 0.0074 | 0.488879 | 84.07 |
| biomass_conc | WI | 532 | 3 | 0.0153 | 0.8365 | 6.2194 |
| biomass_conc | FI | 25 | 0 | 0.013021 | 0.49904 | 0.9234 |
| relative_total_biovolume | ME | 9401 | 9 | 0.437 | 24.473 | 283806.87 |
| relative_total_biovolume | MO | 8696 | 6 | 0.387 | 22.88475 | 100.0 |
| relative_total_biovolume | WI | 532 | 3 | 0.2565 | 18.3779 | 100.0 |
| relative_total_biovolume | FI | 25 | 0 | 0.495 | 18.9638 | 35.091 |

## Zero/inconsistency checks

| check | records | lakes | min_value | max_value |
|---|---|---|---|---|
| biomass_zero_biovolume_positive | 61 | ME,MO | 1.4275 | 49.0049 |
| biovolume_zero_biomass_positive | 0 |  |  |  |
| cells_zero_biovolume_positive | 1 | ME | 7.688e-05 | 7.688e-05 |
| gald_zero | 3 | WI | 0.0 | 0.0 |
| relative_zero_biovolume_positive | 15 | ME,MO | 6.9285 | 272.197 |

## Arithmetic consistency

- **cells_per_ml vs cells_per_nu × nu_per_ml:** n=18,653; max relative error **0.000228**; no row >1% error. The three density fields are internally consistent to rounding.
- **biomass vs biovolume × 1e-6:** median ratio is ~1e-6, but 61 rows have biomass=0 while biovolume is 1.4–49 µm³/mL; 2,067 rows exceed 1% relative deviation due to small-value rounding/truncation. One catastrophic record: ME 2011-07-25 *Coelastrum reticulatum*, cells=0, gald=0.00018286, biovolume=7.688e-05, biomass=84.6924, relative=283806.87. This is internally impossible and must be flagged, not repaired.
- **relative_total_biovolume:** 762/781 sampling groups sum to ~100; **14 groups sum to ~200**, 3 sum to 0, and 2 are other (one at 98.864 and one catastrophic outlier at 283,906.85; 19 anomalous groups total). The cause is unresolved; do not assume a simple percentage denominator.

## Interpretation

- `cells_per_nu` ranges 0–48,000 and is a **natural-unit** count (colonies/filaments), not a cell count; `cells_per_ml` can reach 10,074,657 in colonial picocyanobacteria (WI 2002).
- `gald` is a linear dimension (0–3,200 µm), not a volume; biovolume is derived via geometry and is the more integrative metric.
- `biomass_conc` is derived from biovolume and loses small values (61 zero-biomass rows), so it should not be the sole endpoint for low-abundance taxa.
- No values were deleted, imputed, or winsorised.
