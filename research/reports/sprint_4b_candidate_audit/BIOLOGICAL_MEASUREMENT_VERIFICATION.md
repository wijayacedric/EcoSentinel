# Biological Measurement Verification (Sprint 4B)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Verification levels used
1. **Repository verified** - repository record/source authentic.
2. **File verified** - actual data files downloaded/directly inspected.
3. **Biological outcome verified** - files contain usable biological observations with established measurement meaning.
4. **Pairing verified** - biological and environmental records can be matched defensibly in time and space.

## Candidate A — Greifensee Dryad (10.5061/dryad.r4454)

| Item | Status | Evidence | Unresolved |
|---|---|---|---|
| Repository | Verified | Dryad API metadata retrieved 2026-11-22; CC0; published 2019-01-26; related work 10.1111/ele.12927 | None at repo level |
| Files | **Verified** | User-provided zip copied to `research/evidence/sprint4b_candidate_audit/downloads/A_greifensee_dryad_r4454/doi_10_5061_dryad_r4454__v20190126.zip` (SHA256 `9b66b59eccde06fef560d24ffd02321ffb892dc411d9091ec2d375260908888b`). 4 files extracted; names/sizes match Dryad listing. READMEs and CSVs inspected. | Full QC provenance beyond README not independently audited |
| Biological variables | Verified (group-level) | 2014-2015 cytobuoy CSV: `dens_cyanos`, `dens_euks`, `dens_clean`, `cyano_percent` (log cells/mL; percent by cell number). 9366 rows, 44 cols, 2014-07-17 12:00–2015-11-28 04:00, depths 1.0–10.0m (7 depths), mostly 4h intervals. Long-term microscopy CSV: `dens_phytos`, `dens_cyanos`, `dens_euks`, `cyano_percent`, monthly 1984-03-01–2016-06-01, 388 rows, 36 cols. | Cyanobacteria identified as **group-level density**, not species/biovolume/toxin; detection limits not fully specified in README; long-term README has copy-paste artefact describing dens_phytos as Cytobuoy |
| Direct biological observation vs proxy | Direct biological observations (group-level) | Flow cytometry and microscopy cell densities | Not equivalent to species-resolved biovolume or independent bloom adjudication |

## Candidate B — Greifensee 2018-2023 (10.1038/s41597-025-04988-9; ERIC 10.25678/000C8P, 000C2G)

| Item | Status | Evidence | Unresolved |
|---|---|---|---|
| Repository | Verified | Nature article + DataCite metadata verified; CC0 for ERIC package 000C8P | 000C2G DataCite not separately fetched in this run; paper states ERIC open |
| Files | **Not file-verified** | ERIC landing pages blocked by Anubis bot protection in this environment; no files downloaded | Actual data files, SI tables, classification taxonomy/accuracy tables not inspected |
| Biological variables | Partial (paper-verified) | DSPC underwater imaging; ML classification (Plankiformer); features.csv traits; classification file assigns taxon per ROI. Paper states covers phytoplankton/zooplankton; cyanobacteria/phycoerythrin/phycocyanin mentioned in CTD context. | Cyanobacterial identification capability at usable taxonomic resolution; classification validation/uncertainty per class; false positives/negatives; whether cyanobacteria are a reliable separate biological outcome |
| Direct biological observation vs proxy | Mixed | Imaging-derived taxonomic classification is a direct observation method with model-based classification uncertainty; CTD phycocyanin is a pigment proxy | Per-class performance and cyanobacteria-specific validation not inspected |

## Candidate C — Lake Mendota NTL-LTER (10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9)

| Item | Status | Evidence | Unresolved |
|---|---|---|---|
| Repository | Partial | DOI/package ID known; EDI/PASTA endpoints returned 401 or generic shells in this environment | Authentic package metadata not retrieved in-session |
| Files | **Not file-verified** | No files downloaded/inspected | All file-level questions unresolved |
| Biological variables | Not verified | Prior search/context suggests Madison Lakes phytoplankton dataset; actual columns/units/cyanobacteria resolution unknown | Cyanobacteria identification, cell density, biovolume, sampling frequency, QC, location/depth |
| Direct biological observation vs proxy | Unknown | Requires file inspection | - |

## Candidate D — Buffalo Pound Painter 2018-2019 (10.5683/SP3/MP6NXF)

| Item | Status | Evidence | Unresolved |
|---|---|---|---|
| Repository | Verified | Borealis DOI resolves (302); GitHub mirror inspected; local manifest and files present | Directory name typo (MPNXF) vs DOI (MP6NXF) - documented, not renamed |
| Files | **Verified (key files)** | 7 files downloaded previously; SHA256 hashes match manifest; headers/rows inspected | Toxin CSVs have complex encoding/header structure; full 56-file archive not exhaustively inspected in Sprint 4B |
| Biological variables | Verified (inspected files) | Phytoplankton taxonomy: Species_Name, Cell_Density_L (cells/L), Biomass_mg_m3, Cell_Volume_um3, Length/Width, Group, Phylum/Family/Genus/Species. 2018: 818 rows, 25 unique DOY; 2019: 17 unique DOY. Toxins and nutrients files present. | Toxin units/methods per column need careful parsing; QC/missingness metadata beyond code/readme not fully audited |
| Direct biological observation vs proxy | Direct biological observations | Microscopy taxonomy/counts/biovolume/biomass; lab toxins | Sensor RFU not used as ground truth |

## Cross-candidate caution

No candidate is confirmed suitable for confirmatory Gate 2 evaluation based on this Sprint 4B pass. File-level verification is incomplete for A, B, C due to environment access blockers.
