# Biological Endpoint Verification — Western Lake Erie (Sprint 4E.4)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Verification status

**Raw-file inspection: NOT COMPLETED.** NCEI archive/ISO/granule endpoints returned 503 Service Unavailable in this environment; no NOAA data files were downloaded. All field-level details below are either **NOT VERIFIED** or **literature-described** (Boegehold et al. 2023, 10.5194/essd-15-3853-2023) and must not be treated as raw-file facts.

## Endpoint assessment

| Measurement | Raw-file verified? | Literature-described (Boegehold 2023) | Can be independent biological ground truth? | Caveats |
|---|---|---|---|---|
| Cyanobacteria taxonomic ID | No | Not described as a primary dataset table; paper mentions dominant taxa in text (Microcystis, Anabaena, Aphanizomenon, Dolichospermum, Planktothrix) | Unresolved | No raw taxonomy table verified. Taxon mention in paper is not a verified dataset field. |
| Cell density/counts | No | Not described | Unresolved | No evidence of cell-count fields in paper. |
| Biovolume/biomass | No | Not described | Unresolved | No evidence. |
| Microscopy/direct biological measurements | No | Not described as dataset output | Unresolved | No evidence. |
| PCR/molecular detection | No | Not described | Unresolved | No evidence. |
| Microcystin measurements | No | Particulate and dissolved microcystins by ELISA (ADDA), congener-independent; method/kit changes 2012-2015 vs 2016-2021 | **Not direct cyanobacterial biomass/abundance.** Potential toxin endpoint, but not a bloom biomass ground truth by itself. | Toxin concentration != cell abundance/biovolume; method changes require harmonization check. |
| Chlorophyll-a | No | Extracted chlorophyll a by fluorometry (Speziale 1984) | **Pigment proxy, not cell count.** | Chlorophyll-a includes phytoplankton; not cyanobacteria-specific biomass. |
| Phycocyanin | No | Particulate phycocyanin by fluorometry (Horváth 2013) | **Pigment proxy, not cell count.** | More cyanobacteria-associated but still pigment proxy; not taxonomic/cell-density ground truth. |

## Required raw-file checks (not completed)

For any acquired file, verify: exact column names, units, detection limits, sampling method, sample matrix, dates/frequency, taxonomic resolution, QC flags, missingness. Distinguish pigment/toxin/proxy from direct biological abundance.
