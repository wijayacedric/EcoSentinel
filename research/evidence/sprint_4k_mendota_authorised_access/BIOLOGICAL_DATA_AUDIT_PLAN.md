# Biological Data Audit Plan — 88.31

**Date:** 2026-11-23T23:36:48.967538+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Input

`knb-lter-ntl.88.31` data CSV (EML size 2,448,830 B; entity `f2de15b2fff6ae962a04c150c0a1c510`). Audit only after SHA256/size verification against EML.

## 1. Structural checks

- Read header; compare exactly to EML attributes (15 expected: `lakeid, year4, sampledate, sta, depth_range, division, taxa_name, gald, cells_per_nu, nu_per_ml, cells_per_ml, biovolume_conc, biomass_conc, relative_total_biovolume, genus`).
- Row count; delimiter; encoding; duplicate header rows; blank rows.
- Parse `sampledate` (date) and `year4`; check year consistency.
- Check duplicate keys: `(lakeid, sampledate, sta, depth_range, taxa_name)`.
- Confirm units from EML / data dictionary; do not infer from column names alone.

## 2. Mendota-only records

- Count rows by `lakeid`; list unique values; identify Mendota code.
- Verify Mendota `sta` values and `depth_range` (expected 0-8 m composite).
- Produce `mendota_subset.csv` as a **derived copy** with documented filter; never overwrite raw.
- Quantify rows/dates lost by filtering; report non-Mendota lakes separately.

## 3. Temporal coverage and cadence

- Min/max `sampledate` for Mendota; counts by year and month.
- Sampling intervals: median, IQR, max gap; identify missing years/months.
- Confirm biweekly ice-free / 4-weekly late-season pattern; flag deviations.
- Count sampling dates vs rows (rows are taxa, not independent dates).
- Do not interpolate or infer states between dates.

## 4. Taxonomy and cyanobacteria

- Unique `division`, `genus`, `taxa_name`; count by year.
- Identify cyanobacteria taxa via documented taxonomy, not ad hoc string matching alone; retain original names.
- Check taxonomic changes around Feb 2013 (name changes, genus-to-species); build a name crosswalk with uncertainty.
- Check "species not determined" / unidentified categories; quantify.
- Do not claim species-level certainty where taxonomy is unresolved.

## 5. Density, biovolume, biomass

- Missingness/zeros for `cells_per_nu`, `nu_per_ml`, `cells_per_ml`, `biovolume_conc`, `biomass_conc`.
- Check arithmetic consistency where possible (cells/NU × NU/mL vs cells/mL; biovolume vs biomass conversion).
- Units: cells/mL, biovolume concentration, biomass concentration; record exact EML definitions.
- Detection limits/quantification: look for flags or method text; if absent, state unresolved.
- Do not aggregate across taxa without a documented rule.

## 6. Method/QC changes

- PhycoTech slides; glutaraldehyde; composite 0-8 m; tube sampler.
- Taxonomic updates 2013; any change in counting/analysis.
- Missing QC flags in schema (likely none); document absence.
- Independence: microscopy is measurement-independent of buoy sensors, but same lake/season; note.

## 7. Outputs

- `88_31_structure_report.md`
- `88_31_mendota_coverage.csv`
- `88_31_taxa_cyanobacteria_summary.csv`
- `88_31_density_biomass_missingness.csv`
- `88_31_qc_and_method_notes.md`
- No bloom/non-bloom labels or event intervals.
