# Biological Endpoint Feasibility — Mendota (Sprint 4E.1C)

**Date:** 2026-11-23T07:05:41.270436+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Dataset inspected (metadata-level): knb-lter-ntl.88.31

- **Title:** North Temperate Lakes LTER: Phytoplankton - Madison Lakes Area (from EML)
- **Temporal coverage (EML):** 1995-01-24 to 2020-12-31
- **Entity:** North Temperate Lakes LTER - Phytoplankton - Madison Lakes Area (1 data table)
- **Observed attributes (EML):** lakeid, year4, sampledate, sta, depth_range, division, taxa_name, gald, cells_per_nu, nu_per_ml, cells_per_ml, biovolume_conc, biomass_conc, relative_total_biovolume, genus

## Assessment

| Criterion | Status | Evidence | Caveat |
|---|---|---|---|
| Actual measurement method | Unresolved | EML metadata retrieved but full methods/QC text not exhaustively audited here; entity attributes suggest microscopy/count/biovolume workflow. | Need methods section/QA review before use. |
| Cyanobacteria identification level | Conditionally supported | `division`, `taxa_name`, `genus` fields present in EML attribute list. | Actual cyanobacteria taxa resolution/consistency requires data inspection. |
| Taxonomic specificity | Conditionally supported | Genus and taxa_name present; species-level not confirmed from attribute names alone. | Must verify values in data. |
| Cell density / biovolume / biomass | Supported by metadata | `cells_per_ml`, `biovolume_conc`, `biomass_conc` present. | Units, detection limits, zero/missing semantics require file-level verification. |
| Sampling frequency | Unresolved | Temporal range 1995-2020; actual cadence/seasonality not verified from metadata summary alone. | Must compute from data. |
| Missingness | Unresolved | No file-level audit. | Must inspect. |
| Biological independence from predictors | Conditionally supported (potential) | Phytoplankton counts/biovolume are biological observations, not buoy predictor variables. | Independence depends on how used; toxin/pigment proxies would be weaker - this is count/biovolume metadata. |
| Defensible event/non-event interpretation | Unresolved | Presence of biological variables != defensible bloom/non-bloom intervals. | Gate 2 requires defensible event and non-bloom exposure evidence; not established. |

## Key limitations

- "Madison Lakes Area" means multiple lakes possible (`lakeid` field) - Mendota-only subset must be verified.
- 88.31 data object public readability on CN was not confirmed (Range request returned 404); sysmeta exists. Acquisition path needs confirmation.
- No biological event labels created; no bloom/non-bloom classification performed.
