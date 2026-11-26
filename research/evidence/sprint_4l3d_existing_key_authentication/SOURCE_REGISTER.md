# Source Register

**Date:** 2026-11-24T07:10:03.729185+00:00

| ID | Source | URL/path | Type | Inspected | Used for |
|---|---|---|---|---|---|
| S01 | EDI IAM guide | https://edirepository.org/user-guides/iam | Official docs | Full page | Key/token flow, security |
| S02 | EDI access-key guide | https://edirepository.org/user-guides/working-with-access-keys | Official docs | Full page | Key creation steps |
| S03 | EDI auth news | https://edirepository.org/news/news-grid | Official news | Full page | Mandatory auth since 2026-07-30 |
| S04 | IAM token API | https://auth.edirepository.org/auth/ui/api-docs/token | Official API docs | Full page | `POST /auth/v1/key` |
| S05 | PASTA API docs | https://pasta.lternet.edu/package/docs/api | Official API docs | Excerpt + tested | Data/metadata endpoints |
| S06 | PASTA+ API reference | https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html | Official docs | Excerpt | Read Data Entity |
| S07 | DataONE auth design | https://dataoneorg.github.io/api-documentation/design/Authentication.html | Official docs | Excerpt | Bearer-token model |
| S08 | edi-mcp README | https://github.com/idss-mesa/edi-mcp | Third-party docs | Full README | DataONE fallback claim |
| S09 | edi-mcp DataONE backend | raw.githubusercontent.com/idss-mesa/edi-mcp/main/src/edi_mcp/edi/backends/dataone.py | Source code | Full file | GMN URL pattern |
| S10 | Acquisition script | research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py | Project code | Full file | Auth/acquisition behavior |
| S11 | Sprint 4L.3C report | research/evidence/sprint_4l3c_edi_access_investigation/ | Project evidence | Full | Prior failure/blocker |
| S12 | EML 88.31 | research/evidence/sprint_4e1c_mendota_replica_audit/downloads/88.31/metadata_88.31.xml | Primary metadata | Full | Entity/size/MD5/schema |
| S13 | EML 88.32 | research/evidence/sprint_4l_mendota_biology_audit/downloads/metadata_88.32.xml | Primary metadata | Full | Same data entity |

## Notes

- "Excerpt" means search-result text, not the full document; this is identified explicitly.
- Official endpoint behavior was tested where safe; no secret was sent.
- No source supports bypassing authentication.
