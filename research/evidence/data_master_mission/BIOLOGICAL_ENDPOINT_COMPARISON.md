# Biological Endpoint Comparison

**Date:** 2026-11-23T23:18:29.122618+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

Legend: **Verified** = inspected in local original files this mission. **Corroborated** = documented by primary source/EML but data bytes not inspected. **Unresolved** = not established.

## Buffalo Pound Lake — VERIFIED

- **Source:** Painter et al. 2022, Borealis `10.5683/SP3/MP6NXF`; files locally preserved under `research/evidence/sprint4_global_bio/downloads/painter_borealis_10.5683_SP3_MPNXF/`.
- **Method:** microscopy taxonomy counts (README: "used microscopy to identify and describe the evolution of cyanobacterial species").
- **Taxonomy:** species-level; `Phylum=Cyanophyta`, `Genus`, `Species`, `Species_Name`; includes *Dolichospermum*, *Planktothrix*, *Woronichinia*, *Anabaena*, *Merismopedia*.
- **Density/biomass:** `Cell_Density_L` (cells/L), `Biomass_mg_m3` (mg/m³), `Cell_Volume_um3`, `Length_um`, `Width_um`.
- **Coverage:** 2018 = 25 sample dates (29 May–17 Sep); 2019 = 17 sample dates (29 May–3 Oct); depth 0.8 m; single location "Buffalo Pound".
- **Quantitative content:** 2018 = 817 taxon rows, 170 cyanophyte rows, cyanophyte ≈71.2% of summed biomass; 2019 = 405 rows, 78 cyanophyte rows, ≈70.9% of summed biomass.
- **Independence:** direct microscopy, independent of buoy sensors. **This is the only candidate with verified independent species-level biological counts/biomass locally.**
- **Limitations:** only two seasons; sampling dates sparse relative to 10-min predictors; taxonomy may include identification uncertainty not encoded as a QC flag; no formal detection-limit field observed in the clean data; toxins files have complex multi-row headers and were not used as endpoints.

## Lake Mendota — CORROBORATED (metadata), DATA BLOCKED

- **Source:** `knb-lter-ntl.88.31` EML (public), data bytes auth-blocked.
- **Fields:** `lakeid, sampledate, sta, depth_range, division, taxa_name, genus, gald, cells_per_nu, nu_per_ml, cells_per_ml, biovolume_conc, biomass_conc, relative_total_biovolume`.
- **Coverage:** 1995-01-24 to 2020-12-31 (EML).
- **Assessment:** metadata suggests a genuine microscopy-based phytoplankton endpoint with cell density, biovolume and biomass. **Not verified** at file level: Madison Lakes subset, cyanobacteria consistency, units, detection limits, QC, cadence.
- **Potential:** strongest long-term biological candidate if access is granted, but extensive prior Mendota forecasting work reduces novelty.

## Western Lake Erie — CORROBORATED (literature), NO FILES

- **Source:** Boegehold et al. 2023 ESSD (`10.5194/essd-15-3853-2023`); NOAA DOI `10.25921/11da-3x54`.
- **Measurements described:** chlorophyll-a, phycocyanin, particulate/dissolved microcystins (ELISA), nutrients, CTD, optics. **No cell counts, biovolume, biomass, microscopy taxonomy table or PCR** described as dataset fields.
- **Assessment:** pigments and toxins are proxies/symptoms, not independent cyanobacterial cell or biomass ground truth. Unsuitable as the primary biological endpoint for EcoSentinel without additional data.

## Greifensee — VERIFIED (content audit prior sprint), NOT INDEPENDENT

- **Source:** Eawag Aquascope 5p0x 2018-2023, 60/60 monthly packages local.
- **Measurements:** ROI/image-level classifier outputs (Plankifier/Plankiformer) plus image features. No calibrated cell density/biovolume/biomass; no independent microscopy validation in packages.
- **Assessment:** model-generated biological proxy, not independent ground truth. Exploratory only.

## Bottom line

| Candidate | Independent biological endpoint | Status |
|---|---|---|
| Buffalo Pound 2018-2019 | Yes — microscopy counts + biomass, species level | **Verified** |
| Lake Mendota 1995-2020 | Likely yes (metadata) | **Blocked, unresolved** |
| Western Lake Erie 2012-2021 | No (pigments/toxins only described) | **Weak/unsuitable as endpoint** |
| Greifensee 2018-2023 | No (classifier-derived) | **Not independent** |
