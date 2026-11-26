# Biological Dataset Verification — Lake Mendota (Sprint 4E.1)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Candidate

- **Package:** North Temperate Lakes LTER: Phytoplankton - Madison Lakes Area (package family `knb-lter-ntl.88`, target `knb-lter-ntl.88.31`)
- **DOI:** `10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9`

## Verification status

| Check | Status | Evidence | Limitation |
|---|---|---|---|
| Repository/package identity | **Partially verified** | DOI/package ID known from prior sprints; DOI resolves to EDI in browser context but returned EDI login page HTML in this environment. DataONE indexed older revisions (88.9, 88.11) with title "North Temperate Lakes LTER: Phytoplankton - Madison Lakes Area 1995 - current", but not 88.31. | 88.31-specific metadata not retrieved. |
| Actual downloadable files/file sizes | **Not verified** | PASTA `readDataPackage`/`listDataEntities` returned 403 Public Access not authorized in this environment. | No files downloaded; no sizes/hashes. |
| Taxonomic identification fields | **Not verified** | No metadata/data entity inspected. | Unknown. |
| Cyanobacteria-specific observations | **Not verified** | Not file-inspected. | Cannot confirm taxa resolution or cyanobacteria presence/fields. |
| Cell density / biovolume / biomass | **Not verified** | Not file-inspected. | Cannot confirm units/availability. |
| Sampling dates/frequency/seasonal coverage | **Not verified** | Prior family title suggests 1995-current; 88.31 actual coverage not verified. | No temporal audit possible. |
| Sampling locations/depth integration | **Not verified** | Not file-inspected. | Unknown. |
| Missingness/detection limits/method changes | **Not verified** | Not file-inspected. | Unknown. |
| Licence/reuse | **Not verified** | Package-level licence not retrieved; EDI data policy may apply but must be confirmed at package level. | Human review required. |

## Conclusion

**Biological dataset is not file-verified in this sprint.** Access blocked in this environment (PASTA 403 / EDI login redirect). No Gate 2 biological ground truth can be claimed from this audit.
