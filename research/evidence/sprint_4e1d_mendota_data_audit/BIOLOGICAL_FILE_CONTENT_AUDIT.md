# Biological File Content Audit (Sprint 4E.1D)

**Date:** 2026-11-23T07:09:51.635546+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Status: BLOCKED at file-byte access

- Target: `knb-lter-ntl.88.31` phytoplankton data entity `.../f2de15b2fff6ae962a04c150c0a1c510` (sysmeta: 2,448,830 B, text/csv, SHA-1 f2de15b2fff6ae962a04c150c0a1c510 as entity id hash; CN sysmeta 200).
- **CN object GET:** 404 NotFound.
- **CN resolve:** 403 from gmn.lternet.edu (authoritative MN).
- **Direct PASTA readDataEntity:** 403 "Public Access not authorized".

## Metadata-verified fields (EML only)

lakeid, year4, sampledate, sta, depth_range, division, taxa_name, gald, cells_per_nu, nu_per_ml, cells_per_ml, biovolume_conc, biomass_conc, relative_total_biovolume, genus.

## Not verified (file-level)

Mendota-only rows, actual cyanobacteria taxa values, taxonomic consistency, units, detection limits, QC flags, missingness, sampling cadence, depth/station semantics in data.
