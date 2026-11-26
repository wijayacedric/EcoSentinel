# Sprint 4L.6 handover

**Status:** Audit deliverables prepared; Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).

## Completed

- Read project `AGENTS.md` and task instructions.
- Independently hashed/read the original 88.31 CSV and inspected local EML.
- Independently reproduced structure, lake/date counts, Mendota annual and gap statistics, numerical quality, taxonomic literal counts, duplicate/repeated keys, relative group sums, depth and station counts.
- Compared material findings with Sprint 4L.5; recorded two blank-inclusion count corrections and interpretive qualifications.
- Investigated the Coelastrum row, 61 positive-biovolume/zero-biomass cases, 14 near-200% groups and exact duplicate block without altering data.
- Reviewed taxonomic candidate crosswalk and sources; no crosswalk applied.
- Created independent script and reproduction outputs under this folder.
- Did not create event labels/intervals or conduct prediction, confirmatory analysis, hypothesis test, protocol change or external contact.
- Integrity cross-check against the Sprint 4L.5 SHA-256 register: all 43 non-manifest listed source/output files match the recorded hashes. The register's own self-hash differs from the value written in its self-entry; the current workspace cannot establish when this occurred. The manifest was not repaired or edited.

## Important unresolved questions

1. What exact biological unit and denominator produced `relative_total_biovolume`?
2. Why do 14 sample groups sum near 200%, including 13 groups with no exact full-row duplicates?
3. Which column/value is wrong in the 2011-07-25 *Coelastrum* record; what happened at source?
4. Were MO 1999-11-22 rows duplicated in data transfer or intentionally retained replicates?
5. What are sample, station, slide and replicate IDs for rows with repeated taxa and blank station?
6. What explains 40 Mendota 0–2m and 310 Monona 0–8m records?
7. Which taxa/name transitions were retrospective slide re-identifications vs name-only corrections?
8. What limits of detection/quantification and reporting precision apply?
9. How will an independent, non-sensor biological endpoint adjudicate bloom onset and non-event exposure at a horizon matching warning evaluation?

## Files

All required Sprint 4L.6 Markdown/CSV files plus independent scripts, reproduction JSON/CSVs and SHA-256 register are colocated here. `scripts/independent_reproduction.py` reads the original source path and writes only under `reproduction/`. The raw dataset and Sprint 4L.5 folder were not modified.

## Safe continuation

The next research step would be read-only provenance investigation of archived sample-level lab/calculation records and versioned taxonomy/method documentation, if locally available or already publicly released. Do not contact data owners or change research protocol without fresh authorization. Continue to preserve row-level source data and Gate 2 governance.
