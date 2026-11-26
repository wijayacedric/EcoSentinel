# Raw Schema and Parsing Audit

**Date:** 2026-11-24T07:22:12.805937+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Header

Exact expected header (`header_match=True`):

`lakeid, year4, sampledate, sta, depth_range, division, taxa_name, gald, cells_per_nu, nu_per_ml, cells_per_ml, biovolume_conc, biomass_conc, relative_total_biovolume, genus`

All rows have 15 fields; no malformed records, blank lines, or parse failures.

## Schema comparison

| expected_column | actual_column | match |
|---|---|---|
| lakeid | lakeid | True |
| year4 | year4 | True |
| sampledate | sampledate | True |
| sta | sta | True |
| depth_range | depth_range | True |
| division | division | True |
| taxa_name | taxa_name | True |
| gald | gald | True |
| cells_per_nu | cells_per_nu | True |
| nu_per_ml | nu_per_ml | True |
| cells_per_ml | cells_per_ml | True |
| biovolume_conc | biovolume_conc | True |
| biomass_conc | biomass_conc | True |
| relative_total_biovolume | relative_total_biovolume | True |
| genus | genus | True |

## Observed domains

- **lakeid:** 4 values — ME (9,401 records), MO (8,696), WI (532), FI (25).
- **depth_range:** 2 values — `0-8m` (9,671 records) and `0-2m` (8,983 records).
- **sta:** mostly blank; `1` appears only in 2011–2012 ME and 2011 MO.
- **division:** 11 values; Cyanophyta is the largest by records.
- **sampledate:** all parse as `YYYY-MM-DD`; no sample time field.
- **numeric fields:** all parse as finite floats; no blank/NA values. Zeros are present and must be interpreted with metadata (see variable report).

## Type observations

- `year4` is integer; `sampledate` is date; `lakeid`, `sta`, `depth_range`, `division`, `taxa_name`, `genus` are text.
- All seven biological numeric columns are numeric; no non-finite values.
- Values are ASCII; no hidden encoding substitution.

## Discrepancies with metadata

- Metadata says Mendota is 0–8 m and other lakes 0–2 m. Raw has **40 ME records at 0–2m** (2002-09-23, 2002-10-21) and **310 MO records at 0–8m** (11 dates in 1995, 2002–2004). These are documented, not corrected.
- `sta` is blank for 17,518 of 18,654 records; station identity cannot be reconstructed from this field alone.
- No QC-flag or detection-limit columns exist in the actual schema.
