# Recommended Next Step (Sprint 4E.1C)

**Date:** 2026-11-23T07:05:41.270436+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Verdict: **CONDITIONAL**

Mendota is **not unavailable** and **not yet PASS-ready** for formal Gate 2 readiness review.

## Why conditional

- **Positive:** All three target package revisions (88.31, 130.29, 415.2) are identified in CN OREs; metadata EMLs are publicly readable from CN. 88.31 metadata indicates potentially useful biological fields (taxa, genus, division, cells_per_ml, biovolume_conc, biomass_conc).
- **Blocking/unresolved:** 130.29 has a missing CN data member (2015 HR temp). 88.31 data-byte public readability on CN was not confirmed by a range test (404). Full file-level verification not done. "Madison Lakes Area" scope requires Mendota-only subset verification. Environmental variables are fragmented (temp-only HF; routine physico-chemical). No defensible bloom/non-bloom exposure design. No Gate 2 evidence for fair matched-FAR/leakage-resistant evaluation.

## Next steps (priority order)

1. **Resolve access path:** Obtain authorised EDI API key (user-approved) or confirm CN/public download path for required data bytes; document provenance/SHA256.
2. **Resolve 130.29 gap:** Determine whether 2015 HR temp entity is essential; if so, acquire via authorised path.
3. **Metadata-first file audit:** Before full download, inspect entity sizes/checksums/licences; download smallest scientifically necessary files first.
4. **Mendota subset verification:** Confirm `lakeid`/station/depth semantics in 88.31 and isolate Mendota records with documented rules.
5. **Alignment feasibility memo:** Only after file-level verification, assess temporal/spatial overlap and whether environmental predictors are sufficient for EcoSentinel question.
6. **Gate 2 readiness review:** Only if above evidence is sufficient; PASS here would not authorize Gate 2.

## Do not do now

No event labels, no non-bloom labels, no modelling, no confirmatory analysis, no protocol/Gate 2 changes.
