# Credential Store Discovery

**Date:** 2026-11-24T00:07:54.485503+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Scope

Targeted search for an existing user-owned EDI/PASTA/DataONE credential. No values were printed, logged, copied, or committed.

## Locations checked

| Location | Result | Notes |
|---|---|---|
| `EDI_API_KEY`, `PASTA_TOKEN`, `PASTA_API_KEY`, `DATAONE_TOKEN`, `DATAONE_AUTH_TOKEN` environment variables | absent | checked by presence/length only |
| `launchctl getenv` | unset | GUI-level environment has no key |
| macOS Keychain generic passwords: `ecosentinel-edi`, `EDI`, `edi`, `EDI_API_KEY`, `pasta`, `PASTA`, `edirepository`, `EcoSentinel`, `dataone`, `DataONE` | exit 44 (not found) | no secret read |
| 1Password CLI (`op`) | not installed | no vault scan |
| `~/.zshrc`, `~/.zprofile`, `~/.bash_profile`, `~/.profile` | no key | targeted pattern scan |
| `~/.Renviron`, `~/.Rprofile`, `~/.netrc` | absent or no key | targeted scan |
| EDIutils `config.txt` / project `config.txt` | absent | no key |
| project `.env` / `.Renviron` | absent | no key |
| OpenCode/Claude/Codex/Gemini/Goose MCP configs | no EDI key/edi-mcp key | targeted scan |
| shell history/sessions | only `read -s` + `export EDI_API_KEY`; no value | key was session-scoped |

## Inference

The key appears to have been entered interactively in a prior shell using `read -s` and exported only for that session. It was not persisted to a durable store. This is consistent with the successful 129.42 acquisition on 2026-11-23 23:46 and the current absence.

## Boundary

No attempt was made to recover secrets from browser cookie stores, clipboard, unrelated private files, or another person's account. Those would exceed the authorised scope or require explicit user action.

## Resolution

User must create/authorise an EDI API key and store it in an approved secure location, or perform the portal download manually.

## Broad filesystem filename sweep

A targeted filename sweep under `/Users/cedricbw` (max depth 4) for `config.txt`, `.env`, `*.env`, `.Renviron`, `*credential*`, and `*secret*` returned only:

- `/Users/cedricbw/miniforge3/lib/python3.14/secrets.py` — the Python standard-library module, not a credential.

No project or user credential/configuration file was found. This sweep did not inspect file contents beyond the targeted scans above and did not read browser stores, clipboard, or unrelated private data.
