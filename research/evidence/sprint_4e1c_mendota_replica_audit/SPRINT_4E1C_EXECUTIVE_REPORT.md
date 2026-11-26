# Sprint 4E.1C Executive Report — Mendota DataONE Replica Completion & File-Level Feasibility

**Date:** 2026-11-23T07:05:41.270436+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Verdict: **CONDITIONAL**

Mendota remains a plausible candidate but is **not PASS-ready** for formal Gate 2 readiness review. Evidence is sufficient to justify targeted follow-up, not Gate 2 advancement.

## What was verified

- All three target DOIs resolve to CN-indexed ORE resource maps with expected package revisions: 88.31, 130.29, 415.2.
- Metadata EMLs and OREs were publicly retrieved from DataONE CN and preserved with SHA256.
- CN sysmeta available for 26/27 non-ORE members previously checked; 130.29 missing member `c7538c460f8d0cbd90ec2892b8ce3025` (2015 HR temp, 2015-06-25–2015-09-01) confirmed absent from CN sysmeta/resolve/solr but present in ORE/EML.
- 88.31 metadata indicates biological fields relevant to EcoSentinel: `taxa_name`, `genus`, `division`, `cells_per_ml`, `biovolume_conc`, `biomass_conc`.
- 130.29 provides temperature (daily/hourly/high-resolution yearly) with flags; 415.2 provides temp/DO/pH/specific conductance in routine MO sampling.

## Key blockers

1. **No authorised EDI API key** in environment; EDI PASTA auth required (corroborated).
2. **130.29 CN replica gap:** 2015 HR temperature entity missing on CN.
3. **Data-byte access uncertainty:** 88.31 metadata readable on CN, but data object range request returned 404; full public data readability not established.
4. **Scientific alignment unresolved:** Madison Lakes Area scope vs Mendota-only; phytoplankton cadence unknown; environmental variables fragmented across packages; no event/non-bloom exposure design.

## Gate 2 condition summary

| Condition | Status |
|---|---|
| Independent biological ground truth | Conditionally supported (metadata-level) |
| Defensible bloom-event and non-bloom evidence | Unresolved |
| Adequate temporal resolution | Unresolved |
| Spatial and temporal alignment | Unresolved |
| Fair false-alarm / leakage-resistant validation | Unresolved |

## Final decision

**CONDITIONAL** — promising metadata-level biological signal, but unresolved access, completeness, alignment, and Gate 2 evidence requirements prevent a PASS. A PASS would only permit formal Gate 2 readiness review; it would not authorize Gate 2, event labelling, modelling, or confirmatory evaluation.
