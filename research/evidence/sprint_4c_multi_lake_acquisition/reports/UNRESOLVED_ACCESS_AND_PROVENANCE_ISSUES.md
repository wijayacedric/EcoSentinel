# Unresolved Access and Provenance Issues (Sprint 4C)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Access blockers

| ID | Candidate/Package | Issue | Evidence | Bypass attempted? | Human action required |
|---|---|---|---|---|---|
| U1 | B - ERIC 000C2G biological | Anubis bot-protection page returned by opendata.eawag.ch | curl saved HTML challenge `Making sure you're not a bot!` / Anubis v1.28.2 | No | Manual browser download from official ERIC page; preserve originals and hashes |
| U2 | B - ERIC 000C8P environmental | Same Anubis bot protection | Same challenge page | No | Manual browser download from official ERIC page |
| U3 | C - NTL 88.31 phytoplankton | PASTA metadata endpoint returned 401 `Public Access not authorized` in this environment | curl to `package/metadata/eml/knb-lter-ntl/88/31` returned 401 body; mapbrowse returned generic shell | No | Manual EDI portal download or verify PASTA access from authorized network/browser |
| U4 | C - Mendota HF temp / Microbial Observatory | Not attempted after PASTA/EDI blocker; same environment likely affected | Prior EDI 401/generic shell behavior | No | Manual EDI download |
| U5 | D - BP buoy FRDR 10.20383/103.01100 | FRDR download is Globus-gated | Landing page includes Globus file-manager link with origin_id/path | No | Manual Globus/FRDR download with appropriate access |

## Provenance issues

| ID | Item | Issue | Action taken | Remaining risk |
|---|---|---|---|---|
| P1 | Painter directory naming | Sprint4_global_bio dir uses `painter_borealis_10.5683_SP3_MPNXF` but intended DOI is `10.5683/SP3/MP6NXF` (MPNXF returns 404) | Documented; no rename/overwrite; files hash-verified | Confusion in future scripts; keep manifest/provenance note |
| P2 | Painter partial package | Only 7/56 Borealis files locally present | Copied 7 into sprint4c; recorded gap | Missing files may contain QC/metadata needed for full audit |
| P3 | ERIC 000C2G licence | Paper states open; package-level licence not separately verified | Flagged for human review | Reuse terms uncertain until verified |
| P4 | FRDR buoy licence | Project records indicate CC BY 4.0 but not re-verified on current landing page in this sprint | Flagged for human review | Licence drift possible |

## Not treated as unavailable

- B ERIC and C EDI failures are **environment/access blockers**, not proof datasets are unavailable.
- D FRDR buoy is **Globus-gated**, not unavailable.
