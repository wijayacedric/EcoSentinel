# Gate 2G — Institutional Data Intake Specification

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Preparation artifact only. **No external contact made. No data received. Gate 2 NOT approved.**

## 1. Purpose

Define a reusable, reproducible intake process for any biological/environmental records that may be received from University of Saskatchewan researchers, Buffalo Pound Water Treatment Plant, Saskatchewan Water Security Agency, or referred researchers/labs. This specification prepares technical readiness; it does not create labels, reconstruct events, or change scientific feasibility.

## 2. Scope and safeguards

- Accept only records obtained with explicit human authorization and appropriate data-use terms.
- Preserve original received files unchanged; all validation/derived outputs go to separate derived paths.
- Do not fabricate observations. Templates contain empty/synthetic-test-only examples clearly marked.
- Do not treat received data as approved Gate 2 evidence until human Gate 2/3 review.

## 3. Required biological measurements (priority order)

| Tier | Measurement | Required fields | Why needed |
|---|---|---|---|
| 1 | Phytoplankton taxonomy/identification | sample_date, location, depth, taxon_name, method | Species/genus composition; cyanobacteria identification |
| 1 | Cyanobacterial/cell counts or abundance | count, unit, method, detection limit | Quantitative biological evidence |
| 1 | Biomass/biovolume | value, unit, method | Bloom magnitude/dominance; event-candidate assessment |
| 2 | Laboratory chlorophyll-a | value, unit, method, QA | Independent pigment context (not buoy RFU) |
| 2 | Cyanotoxins (microcystin, others) | value, unit, qualifier, detection limit, method | Toxin context; not a substitute for taxonomy |
| 3 | Nutrients/environmental context | value, unit, method | Mechanistic/contextual interpretation only |

## 4. Preferred file formats

| Format | Preference | Notes |
|---|---|---|
| CSV (UTF-8) | Preferred | Easiest validation/reproducibility; one table per file or clear schema |
| XLSX | Acceptable | Include data dictionary/sheet descriptions; avoid merged cells/macros |
| PDF | Last resort | Only if no tabular export exists; requires extraction with provenance and manual verification |
| Database export/API | Acceptable | Provide schema, export date, query/filter used |

## 5. Required metadata

- **Sampling:** date, time, timezone, location name, coordinates (if available), depth, site ID.
- **Sample identity:** sample ID, replicate ID, lab batch ID, field notes.
- **Methods:** taxonomic method, count/biovolume method, toxin assay method, lab name, SOP/reference, detection/reporting limits.
- **Units:** explicit per field; no implicit conversions.
- **QA/QC:** flags, qualifiers (<LOD/ND/estimated), missing-value codes, replicate handling, accreditation/QA notes.
- **Provenance:** source institution, custodian, retrieval date, license/terms, authorization, checksum.

## 6. Data dictionary and provenance templates

- `research/evidence/gate2g/data_intake/templates/biological_observation_data_dictionary.csv`
- `research/evidence/gate2g/data_intake/templates/provenance_template.json`
- `research/evidence/gate2g/data_intake/templates/intake_manifest_template.csv`
- `research/evidence/gate2g/data_intake/README.md`

## 7. Validation workflow (read-only)

1. **Receive with authorization** - human confirms permission/terms; record in provenance template.
2. **Store original** - copy to source-specific folder under `research/evidence/gate2g/data_intake/received/<source>/original/` (do not modify). Compute SHA256.
3. **Validate** - run `research/evidence/gate2g/scripts/validate_intake.py <file> --kind biological --out .../validation.json`.
4. **Profile** - inspect columns, units, date ranges, missingness, qualifiers, replicates, duplicates. Record issues.
5. **Map** - create a mapping file from source fields to canonical dictionary; do not overwrite source.
6. **Derive** - write cleaned/normalized copies only in derived folders with documented transformations.
7. **Review** - human Gate 2/3 review before any use in event-candidate analysis.

## 8. Validation checks to implement/apply

| Check | Type | Action on failure |
|---|---|---|
| File checksum recorded | Provenance | Block downstream use until recorded |
| Required fields present/mappable | Schema | Report missing; request mapping or source clarification |
| Date parseable and plausible | Quality | Flag; do not coerce silently |
| Depth/location present | Quality | Flag; cannot align spatially without it |
| Units explicit | Quality | Flag; no unit conversion without documentation |
| Detection limits/qualifiers preserved | Quality | Flag if missing for censored measurements |
| Duplicate sample IDs/rows | Quality | Flag; investigate before use |
| Missing-value codes documented | Quality | Flag; do not treat arbitrary codes as zero |
| Taxon names preserved | Integrity | Keep original; optional normalized column separately |

## 9. Handling ambiguous/missing data

- Missing values remain missing. Do not impute biological observations.
- `<LOD`/`ND`/qualifiers preserved as qualifiers; numeric handling requires pre-approved rule.
- Unknown timezone/location/depth: flag as alignment uncertainty; exclude from alignment-sensitive use until resolved.
- Conflicting duplicates: preserve both, document conflict, escalate for human/data-owner clarification.

## 10. Data-use and acknowledgement

- Record license/terms/access restrictions in provenance.
- Do not redistribute restricted data.
- Acknowledge data providers per agreed terms.
- Do not claim institutional endorsement/collaboration without confirmation.

## 11. Current status

No institutional biological datasets received as of 2026-11-22. Templates and validator are ready for use when human-authorized data arrives.