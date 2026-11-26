# Authentication Diagnostic Log

**Date:** 2026-11-24T00:07:54.485503+00:00  
**No secret values are recorded below.**

## Stage 1 — Local environment

| Check | Result |
|---|---|
| `EDI_API_KEY` | absent |
| `PASTA_TOKEN` / `PASTA_API_KEY` | absent |
| `DATAONE_TOKEN` / `DATAONE_AUTH_TOKEN` | absent |
| `launchctl getenv` for EDI/PASTA keys | unset |
| macOS Keychain candidate services | all exit 44 (not found) |
| 1Password CLI | not installed |
| Project `.env` / `config.txt` | no key |
| `~/.zshrc`, `~/.zprofile`, `.bash_profile`, `.profile` | no key |
| `.Renviron`, `.Rprofile`, `.netrc`, EDIutils config | no key |
| Agent/MCP configs | no EDI key |
| Shell history/sessions | only `read -s` and `export EDI_API_KEY`; no value |

**Inference (identified as inference):** the key was entered interactively in a prior shell and exported only for that session. It was not persisted to a durable store.

## Stage 2 — IAM exchange

- Endpoint: `POST https://auth.edirepository.org/auth/v1/key`
- Empty JSON probe: **HTTP 400** `Bad request: Missing field in JSON in request body: 'key'`, method `getTokenByKey`.
- Interpretation: IAM endpoint is reachable and functioning; no key to exchange.

## Stage 3 — PASTA

| Endpoint | Result |
|---|---|
| `/package/metadata/eml/knb-lter-ntl/88/31` | 403 Public Access not authorized (`readMetadata`) |
| `/package/data/eml/.../f2de15b2...` | 403 Public Access not authorized (`readDataEntity`) |
| `/package/authz?...` | 403 Public Access not authorized (`isAuthorized`) |
| `/package/download/eml/knb-lter-ntl/88/31` | 500 Internal Server Error |

Interpretation: authentication is mandatory for public reads; no key.

## Stage 4 — DataONE

- CN sysmeta for data PID: **200**; `authoritativeMemberNode=urn:node:LTER`; `replicaMemberNode=urn:node:LTER` only; size 2,448,830; format text/csv.
- CN object: **404** — no CN replica.
- LTER GMN object: **403**; `/mn/home`: **403**; `/mn/v2/node`: **403**. Apache 403, no object-specific 401.
- EDI GMN object: **403**.
- DataONE token: absent; not attempted.

Interpretation: the documented anonymous member-node route is not usable from this environment. A DataONE token would require a user account and may not resolve a host/path block.

## Stage 5 — EDI Data Portal

- `portal.edirepository.org/nis/dataviewer?...` → **200 login page**.
- `portal.edirepository.org/nis/mapbrowse?...` → login redirect.
- No login/account creation attempted.

## Stage 6 — Browser session

- **Not attempted.** Using an existing browser-authenticated EDI session would rely on the user's account/session and is not appropriate for an autonomous agent without explicit user action.

## Conclusion

No authentication or authorisation bypass was attempted. The blocker is a missing user-held EDI API key (and a host-level DataONE path block), not an incorrect entity or a broken IAM exchange.

## Additional filename sweep

A broad filename sweep for `config.txt`, `.env`, `*.env`, `.Renviron`, `*credential*`, and `*secret*` under the user home (max depth 4) found only the Python standard-library `secrets.py`; no EDI/PASTA credential file. No secret values were read or printed.
