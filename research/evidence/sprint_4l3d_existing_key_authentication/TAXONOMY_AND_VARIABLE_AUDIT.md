# Taxonomy and Variable Audit

**Date:** 2026-11-24T07:10:03.729185+00:00  
**Status: METADATA-LEVEL ONLY — raw taxonomy not inspected.**

## Variables

| Column | Meaning | Unit/type | Audit note |
|---|---|---|---|
| `lakeid` | lake abbreviation | string | Mendota code/value not verified |
| `year4` | year | nominal year | check against sampledate |
| `sampledate` | sample date | date | no sample time |
| `sta` | station | string/integer | deep-hole station expected |
| `depth_range` | depth range | string | Mendota expected 0-8 m |
| `division` | taxonomic division | string | cyanobacteria category present? |
| `taxa_name` | taxon | string | species-level; unresolved taxa possible |
| `gald` | greatest axial dimension | µm | used in biovolume |
| `cells_per_nu` | cells/natural unit | number | colony/filament/cell |
| `nu_per_ml` | natural units/mL | number/mL | abundance |
| `cells_per_ml` | cells/mL | number/mL | independent abundance |
| `biovolume_conc` | biovolume | EML unit blank; methods mm³/mL | primary biomass proxy |
| `biomass_conc` | biomass | mg/L | conversion assumption |
| `relative_total_biovolume` | relative biovolume | percent | composition |
| `genus` | genus | string | consistency with taxa_name pending |

## Taxonomy notes

- Identification: Utermöhl inverted microscopy, species level; PhycoTech.
- Multiple same-date/species rows may be variants or vegetative states.
- February 2013 updates: name changes, genus-to-species changes, slide revisits.
- Cyanobacteria are represented within `division`/`taxa_name`; exact categories require raw inspection.
- No raw taxonomy values were inspected. No bloom/non-bloom labels created.
