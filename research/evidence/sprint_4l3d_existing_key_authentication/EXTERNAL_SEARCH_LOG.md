# External Search Log — Sprint 4L.3D

**Date:** 2026-11-24T07:10:03.729185+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Defined source categories

1. Official EDI IAM/authentication documentation.
2. Official EDI API-key and token-exchange documentation.
3. Official PASTA data-access documentation.
4. Official DataONE authentication/member-node documentation.
5. Existing project acquisition scripts, logs and Sprint 4K/4L.3/4L.3C evidence.
6. Environment/secure-store configuration relevant to the script (read-only; no broad sweep repeated).

## Sources inspected

| # | Source | URL | Access date | What was inspected | Status |
|---:|---|---|---|---|---|
| 1 | EDI IAM guide | https://edirepository.org/user-guides/iam | 2026-11-24 | Profiles, access keys, token/cookie behavior, query-parameter key | Full page |
| 2 | EDI access-key steps | https://edirepository.org/user-guides/working-with-access-keys | 2026-11-24 | New Key steps, principal, duration, one-time secret | Full page |
| 3 | EDI authentication news | https://edirepository.org/news/news-grid | 2026-11-24 | Mandatory API auth from 2026-07-30; IdP sign-in | Full page |
| 4 | IAM token API | https://auth.edirepository.org/auth/ui/api-docs/token | 2026-11-24 | `POST /auth/v1/key`, body `{"key":...}`, `edi-token` response, refresh | Full page |
| 5 | PASTA API docs | https://pasta.lternet.edu/package/docs/api | 2026-11-24 | Read Data Entity, Read Metadata, isAuthorized; auth requirement | Search-result excerpt; endpoint behavior tested |
| 6 | PASTA+ API reference | https://pastaplus-core.readthedocs.io/en/latest/doc_tree/pasta_api/data_package_manager_api.html | 2026-11-24 | Read Data Entity URI; authz | Search-result excerpt |
| 7 | DataONE authentication | https://dataoneorg.github.io/api-documentation/design/Authentication.html | 2026-11-24 | Bearer token, portal authentication | Search-result excerpt |
| 8 | edi-mcp README | https://github.com/idss-mesa/edi-mcp | 2026-11-24 | Claim: anonymous DataONE replicas for metadata/entity downloads; keyless fallback | Full README inspected |
| 9 | edi-mcp DataONE backend | https://raw.githubusercontent.com/idss-mesa/edi-mcp/main/src/edi_mcp/edi/backends/dataone.py | 2026-11-24 | Member-node URL pattern `gmn.lternet.edu/mn/v2/object/<encoded pid>` | Source inspected |
| 10 | Existing acquisition script | research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py | 2026-11-24 | Key read, IAM POST, cookie, retries, URL guard, size/MD5 handling | Full file inspected |
| 11 | Sprint 4L.3/4L.3C evidence | research/evidence/sprint_4l_mendota_biology_audit/; sprint_4l3c_edi_access_investigation/ | 2026-11-24 | Prior failure, diagnostics, target values | Full reports inspected |

## Contradiction / discrepancy recorded

- `edi-mcp` documents anonymous DataONE member-node entity downloads. In this environment, `gmn.lternet.edu/mn/v2/object/<pid>`, `/mn/home`, and `/mn/v2/node` all return HTTP 403 Apache Forbidden. This is an environment/host-path block, not an object-specific 401. The claim was not accepted as universally true; it was tested and failed here.
- EDI documentation supports both a query-parameter key (`?key=`) and the IAM token/cookie flow. The acquisition script uses the token/cookie flow to avoid keys in URLs/logs.

## Sources identified but not fully inspected

- Full PASTA API HTML (search-result excerpt only).
- Full DataONE authentication page (search-result excerpt only).
- DataONE portal token acquisition UI (not used; would require user account).
- EDI Data Portal package page (login redirect; not inspected beyond redirect).

## Why searching stopped

The authentication flow, official endpoints, script behavior and prior failure are now documented. The remaining step is user entry of the existing key; further literature/search work cannot substitute for it. No broad credential-file sweep was repeated.
