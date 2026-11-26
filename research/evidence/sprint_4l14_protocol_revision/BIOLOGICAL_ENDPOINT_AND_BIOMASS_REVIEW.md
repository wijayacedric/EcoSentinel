# Biological Endpoint and Biomass Review

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis is authorised. The arithmetic consistency check below is a metadata/derivation verification, not a statistical analysis or a derived analytical dataset.**

## 1. Purpose

This document implements Sprint 4L.13 revision R-06. It establishes:

- what the Mendota biovolume endpoint represents;
- what the Buffalo Pound biomass endpoint represents;
- its units and derivation;
- whether the derivation is sufficiently documented for reproducibility;
- whether P3/P4 remain suitable.

## 2. Mendota cyanobacteria biovolume

### 2.1 Source and derivation

- Source: NTL-LTER phytoplankton, `knb-lter-ntl.88.31`.
- Method: 0–8 m tube composite; inverted microscopy (Utermöhl); cell counts and dimensions; geometry-based cell biovolume.
- `biovolume_conc` is computed from average cell biovolume × cell density.
- `biomass_conc` is a derived conversion (approximately biovolume × 10⁻⁶), not an independent measurement.

### 2.2 Units

`biovolume_conc` is in µm³ mL⁻¹ (equivalent to 10⁻³ mm³ m⁻³; the EML defines 10⁶ µm³ mL⁻¹ = 1 mm³ mL⁻¹).

### 2.3 Independence

The endpoint is measurement-independent of the buoy sensor: different method, instrument, and analyst pipeline. It is not independent of the same lake processes.

### 2.4 Limitations

- taxonomic non-stationarity (468 names; 204 pre-2013-only; 72 post-2013-only; 2013 update);
- 1,009 same-key groups / 2,048 rows (variants/vegetative states; not independent);
- 61 biomass zeros with positive biovolume;
- Coelastrum 2011-07-25 anomaly (non-cyanobacteria);
- relative total biovolume inconsistent (not used);
- no detection limits/field blanks;
- 0.5 m sensor vs 0–8 m composite;
- station blank for 371/402 dates;
- date-only biology.

### 2.5 Suitability

**Suitable for a broad cyanobacteria biovolume endpoint with caveats.** Broad `Cyanophyta` total is defensible; species-level primary is not.

## 3. Buffalo Pound cyanobacteria biomass

### 3.1 Source columns

The Painter et al. 2022 taxonomy files provide:

- `Cell_Density_L` (cells L⁻¹);
- `Biomass_mg_m3` (mg m⁻³);
- `Length_um`, `Width_um`, `Cell_Volume_um3`;
- `Group`, `Phylum`, `Family`, `Genus`, `Species`.

There is no `Biovolume` column.

### 3.2 What the biomass variable represents

`Biomass_mg_m3` is a **derived microscopy quantity**, not a direct measurement. It is consistent with:

\[
\text{Biomass}_{mg\,m^{-3}} \approx \text{Cell\_Volume}_{\mu m^3} \times \text{Cell\_Density}_{L^{-1}} \times 10^{-6}
\]

This is a **volume-derived, wet-weight-equivalent biomass proxy**, not dry weight, carbon biomass, or a direct gravimetric measurement.

The factor \(10^{-6}\) converts µm³ L⁻¹ to mg m⁻³ under the standard assumption of a cell density of approximately 1 g cm⁻³:

- µm³ cell⁻¹ × cells L⁻¹ = µm³ L⁻¹;
- 1 mg biomass ≈ 1 mm³ cell volume;
- 1 mm³ = 10⁹ µm³;
- 1 mg L⁻¹ = 10⁹ µm³ L⁻¹;
- 1 mg m⁻³ = 10⁶ µm³ L⁻¹;
- therefore mg m⁻³ = µm³ L⁻¹ × 10⁻⁶.

### 3.3 Verification check

A metadata/derivation check was performed on the existing local files:

- 2018: all 817 positive `Biomass_mg_m3` rows; ratio `Biomass / (Cell_Volume × Cell_Density)` median = 1.000 × 10⁻⁶; range = 9.87 × 10⁻⁷ to 1.0366 × 10⁻⁶.
- 2019: all 405 positive rows; median = 1.000 × 10⁻⁶; range = 9.55 × 10⁻⁷ to 1.0227 × 10⁻⁶.

The ratios are consistent with the formula above; the small variation is consistent with rounding of `Biomass_mg_m3` to two decimals and cell-volume precision.

These are **taxon-row counts**, not eligible date counts. They do not establish actual usable n for P3/P4; that remains unknown until the separately authorised count-only audit.

This is a **derivation/metadata consistency check**, not a statistical analysis. It does not create a derived dataset.

### 3.4 Is the derivation documented sufficiently?

**Partially.**

- The data structure and arithmetic are consistent with the formula.
- The 2018 and 2019 files use the same relationship.
- The source paper/supplement is the authoritative method description, but the full text could not be retrieved in this environment (RSC 403; ESSOAr 403). The RSC supplementary metadata identifies biomass in mg/m³ for cyanobacterial species at 0.8 m, but the exact formula was not directly inspected in the paper text.
- The local data dictionary does not state the density assumption or rounding.

**Conclusion:** The derivation is sufficiently consistent for reproducible use **if** the protocol states the inferred formula and the 1 g cm⁻³ density assumption, and if the human data custodian accepts the inference. It is not documented to the standard of a formal methods statement in the local metadata.

The protocol does **not** compute biomass from this formula. It uses the supplied `Biomass_mg_m3` variable. The formula is documented only to interpret the supplied endpoint and to assess whether it is a derived microscopy quantity. This avoids substituting an assumed formula for the provided data.

### 3.5 What the endpoint is not

- It is not a direct measurement.
- It is not biovolume.
- It is not numerically equivalent to Mendota `biovolume_conc`.
- It is not independent of cell-volume measurement assumptions.
- It is not a bloom, toxicity, or whole-column endpoint.

### 3.6 2018/2019 consistency

- Same formula is consistent across both years.
- But the 2018/2019 schema and taxonomy differ (`Sample_ID` vs `REP`; 73 vs 56 taxa; 39 shared).
- Replicate structure differs and is unresolved.
- The 2019-07-17 anomaly remains.

### 3.7 Suitability

**The review recommends downgrading P3/P4 to exploratory** until the data custodian verifies the biomass derivation against the original publication/supplement. The reason is that the formula is inferred from arithmetic consistency, not quoted from the methods text.

If verification succeeds:

- P3/P4 may be restored to primary, subject to the replicate rule, count audit, B7/coverage, and two-season limitations.

If verification fails or the reviewers require a directly measured biovolume endpoint:

- P3/P4 become **unsuitable** and Buffalo Pound should be excluded from primary analysis.

Until D-02 is resolved, P3/P4 are **not approved as primary estimands**; they remain conditional/exploratory.

## 4. Cross-lake comparability

| Feature | Mendota | Buffalo Pound |
|---|---|---|
| Quantity | Biovolume | Biomass |
| Unit | µm³ mL⁻¹ | mg m⁻³ |
| Derivation | Geometry-based cell volume × density | Cell volume × density × 10⁻⁶; inferred/verified |
| Direct measurement? | No (derived from microscopy) | No (derived from microscopy) |
| Independent of sensor? | Yes | Yes |
| Depth | 0–8 m composite | 0.8 m point |
| Taxonomy | 468 names; division total | 73/56 taxa; group total |
| Period | 2006–2020 | 2018–2019 |
| Cadence | ~14 days | 4–16 days |
| Detection limits | None | None |

The endpoints are not numerically comparable. They are two different microscopy-derived abundance measures. The protocol must not pool them or treat one as a conversion of the other.

## 5. Estimand impact

| Estimand | Impact |
|---|---|
| P1/P2 | Mendota biovolume remains suitable with caveats |
| P3/P4 | Conditional on accepting the inferred biomass derivation and the replicate/coverage rules; otherwise unsuitable |

No revision makes P1/P2 unsuitable. P3/P4 remain conditional/exploratory, not automatically unsuitable; the review recommends downgrading them pending D-02 verification.

## 6. Residual uncertainty

- The exact formula is inferred from arithmetic consistency, not directly quoted from the paper text.
- The 1 g cm⁻³ density assumption is standard but not stated in the local data dictionary.
- The full Painter et al. methods text was not accessible.
- Detection limits and replicate design are undocumented.
- The 2019-07-17 anomaly is unresolved.

These are stated, not hidden.

## 7. Required protocol text

The revised protocol must say:

> Buffalo Pound `Biomass_mg_m3` is a derived microscopy quantity, consistent with `Cell_Volume_um3 × Cell_Density_L × 10^-6` under a 1 g cm^-3 density assumption. It is not a direct measurement and is not numerically equivalent to Mendota biovolume. The derivation check is a metadata consistency check, not a statistical analysis. If the data custodian does not accept the inference, P3/P4 are unsuitable.

## 8. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
