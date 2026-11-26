# Biological Measurement Compatibility (Sprint 4)

**Date:** 2026-11-22  
**Status:** Investigation artifact. Gate 2 remains **PAUSED / NOT APPROVED — Option C (Exploratory only)**.

## Principle

Never treat toxin concentrations, pigment fluorescence, microscopy counts, and biovolume as interchangeable measurements. Each has different biological meaning, uncertainty, and suitability for EcoSentinel's independent biological ground truth.

## Measurement compatibility assessment

| Measurement type | Role in EcoSentinel | Independence from buoy RFU | Suitability for confirmatory event labels | Key limitations | Notes |
|---|---|---|---|---|---|
| Microscopy phytoplankton taxonomy/cell counts | Primary biological evidence candidate | Yes (if lab/independent) | High potential, if methods/QC/temporal coverage adequate | Sparse sampling, taxonomic expertise, method changes, volume estimation | Painter 2022 BP dataset includes species, cell density, biomass, cell volume. |
| Biovolume | Primary biological evidence candidate | Yes (if lab-derived) | High potential | Biovolume estimation assumptions; species-specific shape factors; inter-lab variability | Preferred over raw counts for bloom biomass; must record method. |
| Biomass (mg/m3) | Primary/derived biological evidence | Yes if derived from independent microscopy | High potential | Depends on biovolume-to-biomass conversion assumptions | Painter 2022 provides Biomass_mg_m3. |
| Laboratory chlorophyll-a | Supporting biological/biomass proxy | Yes if lab-extracted | Moderate - proxy, not cyanobacteria-specific | Not cyanobacteria-specific; extraction method matters | Can support context, not sole bloom-species ground truth. |
| Cyanotoxins (microcystins, etc.) | Secondary bloom-impact evidence | Yes (lab) | Low-Moderate as sole event definition | Toxicity not always proportional to biomass; species/toxin variability; episodic | Useful corroboration; not interchangeable with bloom onset. |
| Independently measured phycocyanin (lab) | Supporting pigment evidence | Yes if independent | Low-Moderate | Pigment proxy; extraction/calibration differences | Better than buoy RFU as independent check, still proxy. |
| Buoy phycocyanin/chlorophyll RFU | Predictor/sensor signal only | **No** for ground truth | **Not suitable as independent ground truth** | Fouling, calibration, quenching, sensor drift, same-system circularity | Already project constraint. |
| Flow cytometry | Potential biological evidence | Yes | Moderate-High depending on taxa resolution | Taxonomic resolution limits; instrument/method differences | No BP candidate verified in Sprint 4. |
| Molecular (qPCR/metabarcoding) | Potential biological evidence | Yes | Moderate - depends on target and quantitation | Gene copy vs cell/biovolume; primer bias; not directly comparable to counts | No BP candidate verified in Sprint 4. |
| Remote sensing bloom indices | Secondary spatial/temporal evidence | Usually independent | Low-Moderate | Surface-only, cloud cover, resolution, algorithm uncertainty, not species-specific | Useful for corroboration/triage only. |

## Painter 2022 (BP-001) compatibility note

- Verified fields: `Cell_Density_L`, `Biomass_mg_m3`, `Cell_Volume_um3`, taxonomy (phylum/genus/species), DOY, depth.
- Sampling: 25 dates (2018), 17 dates (2019) - sparse and interval-censored for event onset/offset.
- Suitable for: exploratory biological context, candidate event-window triage, method development with explicit uncertainty.
- Not sufficient alone for: confirmatory Gate 2 event-based evaluation.
