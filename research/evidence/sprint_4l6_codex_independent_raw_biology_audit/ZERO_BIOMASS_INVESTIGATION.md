# Zero biomass with positive biovolume

## Reproduction

I independently inspected all 61 records where `biomass_conc == 0` and `biovolume_conc > 0`. All occur in ME or MO, with biovolume from 1.4275 through 49.0049 µm³/mL. Applying the EML's stated conversion (`biomass mg/L = biovolume µm³/mL × 10⁻⁶`, under equal density) gives 0.0000014275–0.0000490049 mg/L. Every expected value is below 0.00005 mg/L. The reported zeros look consistent with rounding to 4 or fewer decimal places (or truncation at that precision). Full case list and independently computed expected values: `reproduction/ZERO_BIOMASS_CASES.csv`.

There are 64 zero biomass values total: these 61, plus three WI records whose absolute biovolume is also zero. No positive biomass/zero biovolume rows were found outside the Coelastrum row? **Correction:** the Coelastrum record is exactly such a positive-biomass/near-zero-biovolume case and was counted in that test; it is the sole `cells=0` / positive biovolume record. The more important point is it is internally anomalous, not a valid conversion example.

## Interpretation

The magnitude pattern supports low-value rounding/truncation as a plausible mechanism, but cannot prove exact formatting precision or whether zero is a code for below reporting threshold. EML defines biomass as a unit conversion and contains no detection-limit or quantization precision specification. The 61 values should be treated as censored/rounded unknown low biomass rather than evidence of biological zero; numerical conversion cannot recover lost precision.

`biomass_conc` is derived from the same geometric biovolume and an assumed density-to-mass conversion. It does not provide an independent endpoint or validation. Use it as a secondary presentation metric only after resolving precision and the Coelastrum row. For low abundance, the exported biovolume field retains more numerical information, though it too is derived and method dependent.
