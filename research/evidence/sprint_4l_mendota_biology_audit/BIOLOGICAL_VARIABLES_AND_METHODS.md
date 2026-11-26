# Biological Variables and Methods — 88.31

**Date:** 2026-11-23T23:58:36.852965+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Entity

- Package: `knb-lter-ntl.88.31` (revision 31); DOI `10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9`.
- Entity: `f2de15b2fff6ae962a04c150c0a1c510`.
- Original object: `ntl88_v13.csv`; size **2,448,830 B**; EML MD5 **`a0363cc7fdfd6c12889750fea27bd542`**.
- One data table, **15 columns** (see `DATASET_SCHEMA.csv`).
- Data bytes **not acquired**; schema and methods are metadata-verified.

## Measurement methods (EML)

- Composite whole-water sample, **0–8 m** for Mendota; tube sampler at the deep hole.
- Preserved in **glutaraldehyde**; permanent slide mounts (3/sample) by **PhycoTech, Inc.**
- Identification to species using an **inverted microscope (Utermöhl technique)**.
- Counts reported as:
  - natural units (colonies, filaments, single cells) per mL;
  - cells per mL;
  - algal biovolume per mL.
- Multiple entries for the same species/date may represent different variants or vegetative states (colonial/attached vs free cell).
- Cell biovolume: measured dimensions matched to geometric solids (cylinders, spheres, truncated cones); average cell biovolume × cell density.
- Conversion: 10^6 µm³/mL = 1 mm³/mL biovolume; assuming cell density ≈ water, 1 mm³/mL ≈ 1 mg/L biomass.

## Variables

- **Taxonomy:** `division`, `taxa_name`, `genus`.
- **Size:** `gald` (µm).
- **Abundance:** `cells_per_nu`, `nu_per_ml`, `cells_per_ml`.
- **Biovolume/biomass:** `biovolume_conc`, `biomass_conc`, `relative_total_biovolume`.
- **Design:** `lakeid`, `year4`, `sampledate`, `sta`, `depth_range`.

## Detection limits and QC

- **No detection-limit field** in the schema.
- **No QC flag field** in the schema.
- **No replicate identifier**; multiple same-species/date rows may be variants or counting replicates (EML explicitly warns about variants).
- EML contains no `qualityControl` section; only the methods text.
- EML states species may not have been determined for all slides.

## Taxonomist/consistency evidence

- Carey et al. (2016, J Plankton Res 38:27–40) state that for 1995–2010 all microscopic analyses were conducted by the **same taxonomist (A.L.S.)**; >400 natural units/sample; biovolume for up to 15 natural units/species; Hillebrand et al. geometry.
- PhycoTech's own materials identify **Ann L. St. Amand** as the sole person enumerating algal samples, claim 95%+ in-house QC precision, and note her death on **7 October 2023**.
- This supports long-term consistency through 2020, but the QA claim is **company self-report**, not independent peer-reviewed validation. The exact 2010–2020 analyst continuity is not independently verified.

## What this establishes

A genuine, species-level, microscopy-based biological endpoint with cell density, biovolume and biomass, independent of buoy pigment sensors.

## What it does not establish

Actual data completeness, Mendota-only counts, detection limits, taxonomic consistency in the delivered file, or freedom from taxonomic bias.
