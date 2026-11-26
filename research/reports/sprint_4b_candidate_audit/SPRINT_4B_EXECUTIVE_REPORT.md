# Sprint 4B Executive Report — Candidate File-Level Verification and Comparative Feasibility Audit

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Phase:** Sprint 4B  
**Gate 2 status:** **PAUSED / NOT APPROVED — Option C (Exploratory Only)** (unchanged)

## 1. Mission outcome

Sprint 4B performed a targeted file-level verification audit of four candidate datasets (A-D). The audit followed the required four-level model: repository verified, file verified, biological outcome verified, pairing verified. No biological event labels, real-data modelling, confirmatory evaluation, protocol/gate changes, dataset integrations, external contacts, or commits/pushes were performed.

**Key limitation:** direct file-level verification was initially blocked in this environment for A (Dryad 401), B (Eawag ERIC Anubis), and C (EDI PASTA/portal 401/generic shell). During Sprint 4B, the user provided the A Dryad zip; A is now file-verified. B and C remain file-unverified due access blockers. Candidate D was locally file-verified for previously downloaded key files.

## 2. Candidate summary

| Candidate | Repo verified | File verified | Biological outcome verified | Pairing verified | Overall status |
|---|---|---|---|---|---|
| A. Greifensee Dryad 10.5061/dryad.r4454 | Yes | Yes (user-provided zip, SHA256 verified) | Yes (group-level cyano/euk cell density) | Partial (in-file alignment possible) | **File-verified; biologically limited; high overlap risk** |
| B. Greifensee 2018-2023 10.1038/s41597-025-04988-9 | Yes | No (Anubis) | Partial paper-only | No | **Not fully verified - access blocked** |
| C. Mendota NTL-LTER 10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9 | Partial | No (401/generic shell) | No | No | **Not verified - access blocked** |
| D. Buffalo Pound Painter 10.5683/SP3/MP6NXF | Yes | Yes (7 key files, SHA256 OK) | Yes for inspected files | Partial | **Partially verified; conditionally promising but insufficient for confirmatory Gate 2** |

## 3. Key findings

### A. Greifensee Dryad (r4454) — updated with user-provided zip
- **Verified:** Dryad metadata, CC0, 4 files extracted; SHA256 `9b66b59eccde06fef560d24ffd02321ffb892dc411d9091ec2d375260908888b`. 2014-2015 cytobuoy: 9366 rows, 44 cols, 2014-07-17–2015-11-28, 7 depths 1.0–10.0m, mostly 4h intervals; columns include `dens_cyanos`, `dens_euks`, `dens_clean`, `cyano_percent` (log cells/mL; percent by cell number), plus temp/O2/pH/nutrients/PAR/thermocline/zooplankton/weather/inflow. Long-term microscopy: 388 rows, 36 cols, monthly 1984-03-01–2016-06-01; group-level cyano/euk/phyto densities.
- **Not verified / limitations:** group-level only (no species, biovolume, toxin, or independent bloom adjudication); flow cytometry vs microscopy not comparable; high missingness in inflow/nutrients/zooplankton; detection-limit substitutions/interpolations documented in README.
- **Overlap risk:** **High** - same dataset directly used in Thomas et al. 2018 predictability study; any EcoSentinel reuse requires careful differentiation and originality scoping.

### B. Greifensee 2018-2023 (Eyring et al. 2025)
- **Verified:** paper/DataCite metadata; CC0 for ERIC 000C8P; integrated HF monitoring design (DSPC at 3m, CTD 1-17m, meteo, weekly/biweekly nutrients).
- **Not verified:** actual files/SI tables, cyanobacteria class-level ML performance, classification uncertainty, pairing defensibility on data.
- **Risks:** diel vertical migration (daily aggregation recommended), fixed 3m camera misses surface blooms, acquisition/config changes, ML classification not equivalent to independent microscopy counts without validation.

### C. Lake Mendota NTL-LTER 88.31
- **Verified:** package ID/DOI known; no file-level confirmation possible in this environment.
- **Not verified:** everything at file/biological/pairing level.
- **Status:** cannot be ranked above unverified; manual EDI access required.

### D. Buffalo Pound Painter 2018-2019
- **Verified:** local files hash-match manifest; microscopy taxonomy with `Cell_Density_L`, `Biomass_mg_m3`, `Cell_Volume_um3`, phylum/genus/species; 25 dates (2018), 17 dates (2019); 0.8m depth samples.
- **Not verified/limitations:** toxin CSV complex format not fully parsed; sparse interval-censored sampling; 2019-07-17 anomaly unresolved; no defensible verified non-bloom exposure; NC-SA licence needs compatibility review.
- **Provenance discrepancy documented:** local directory named `..._MPNXF` but intended/verified DOI is `10.5683/SP3/MP6NXF` (`MPNXF` DOI resolves 404). No silent rename/overwrite performed.

## 4. Comparative assessment (evidence-bounded)

| Criterion | A Greifensee r4454 | B Greifensee 2018-2023 | C Mendota NTL 88.31 | D BP Painter |
|---|---|---|---|---|
| Biological specificity | Unknown at file level; metadata suggests cyano/euk separation | Unknown at class-performance level; imaging+ML | Unknown | Verified microscopy taxonomy/biovolume |
| Temporal resolution | Promising (4h) but unverified | High (hourly imaging) but aggregation needed; unverified files | Unknown | Sparse (25/17 dates over 2 seasons) |
| Environmental compatibility | Promising metadata; unverified | Promising by design; unverified | Unknown | Partial (BP buoy overlap exists) |
| Spatial/depth compatibility | Unverified | Fixed 3m camera vs profiles; concern | Unknown | 0.8m biological vs buoy depth needs confirmation |
| Licence/access | CC0 but file access blocked here | CC0 stated but ERIC blocked here | Unconfirmed here | CC BY-NC-SA; locally accessible |
| Prior overlap risk | High (Thomas 2018) | Medium-High (same group/system) | Medium-High (LTER) | Low-Medium (known project dataset) |
| Confirmatory readiness | Not verifiable now | Not verifiable now | Not verifiable now | Insufficient for Gate 2 |

## 5. Final recommendation

- **Strongest file-verified candidate:** **D — Buffalo Pound Painter 2018-2019** remains the strongest *project-relevant* file-verified biological candidate (independent microscopy taxonomy/biovolume/biomass; BP overlap). **A — Greifensee Dryad** is now file-verified, but it is group-level only, has high prior-use overlap (Thomas 2018), and is not a Buffalo Pound-compatible confirmatory candidate. Neither is sufficient for confirmatory Gate 2 evaluation.
- **Strongest metadata/potential candidates (unverified at file level):** **A and B (Greifensee)** have promising metadata/paper descriptions, but file-level verification was blocked. They also carry ecosystem-transfer and prior-publication-overlap risks.
- **Buffalo Pound as primary ecosystem:** **Remains provisionally recommended** as the primary ecosystem for EcoSentinel's current question, because the existing BP HF environmental dataset is in-project and D provides verified local independent biological observations for 2018-2019 overlap. This is **not** a claim of confirmatory readiness.
- **Alternative demonstrably stronger?** **No.** No alternative candidate was demonstrably stronger based on file-verified evidence in this sprint. A/B/C may become competitive only after file-level verification, pairing assessment, and overlap/licence review.
- **Potentially suitable but not yet fully verified:** A, B, C (access-blocked); D remains conditionally useful for exploratory work only.
- **Evidence still missing:** file contents for A/B/C; cyanobacteria class resolution/validation; defensible temporal/spatial pairing tests; independent event/non-event exposure; 2019-07-17 anomaly resolution; NC-SA compatibility decision for D.
- **Future Gate 2 review justified?** **Not yet.** A future Gate 2 review is justified only after independent biological evidence and defensible non-bloom exposure are obtained/verified and a human-approved evaluation design is in place. This sprint does not provide that evidence.

## 6. Required confirmation

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**  
No Gate 2 approval is granted or implied by this report.
