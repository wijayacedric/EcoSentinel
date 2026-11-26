# Unresolved Evidence and Blockers (Sprint 4B)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Environment/access blockers

| Blocker | Candidates affected | Impact | Safe next step |
|---|---|---|---|
| Dryad file downloads previously returned 401 in environment | A | Resolved for this sprint by user-provided zip; file-level inspection completed | Retain provenance/hash record; any further Dryad files need same provenance discipline |
| Eawag ERIC behind Anubis bot protection | B | Cannot inspect actual data files or SI tables | Manual browser download; or request human-assisted download |
| EDI PASTA/portal metadata endpoints returned 401/generic shell in this environment | C | Cannot verify package metadata, data entities, variables, sampling design | Manual EDI portal access; or use alternative public metadata mirror |
| Wiley/RSC publisher 403 (from Sprint 4) | BP-002 context | Cannot inspect Boyer 2025 SI/raw data availability | Human-authorized acquisition path if needed |

## Scientific/evidence blockers

| Blocker | Candidates affected | Impact |
|---|---|---|
| Cyanobacteria-specific resolution unverified in files | A,B,C | Cannot confirm biological outcome suitability |
| Temporal/spatial pairing not tested on actual files | A,B,C,D(partial) | Cannot confirm defensible pairing |
| ML classification uncertainty for cyanobacteria classes | B | Imaging-derived labels may not be equivalent to microscopy counts |
| Sparse/interval-censored biological sampling | D | Event onset/offset and non-event exposure uncertain |
| 2019-07-17 Painter anomaly | D | Potential data quality/event interpretation issue |
| No defensible verified non-bloom exposure intervals | All | Gate 2 confirmatory evaluation remains blocked |
| Prior publication overlap (Thomas 2018) | A | High originality/independence risk for EcoSentinel reuse |

## Provenance discrepancy (documented, not modified)

- Local Painter directory: `research/evidence/sprint4_global_bio/downloads/painter_borealis_10.5683_SP3_MPNXF/`
- Intended DOI: `10.5683/SP3/MP6NXF` (Borealis resolves 302). `MPNXF` returns 404.
- Manifest/file hashes verified OK for 7 downloaded files; content corresponds to Painter 2022 Buffalo Pound blooms repo.
- **No silent rename or overwrite performed.**
