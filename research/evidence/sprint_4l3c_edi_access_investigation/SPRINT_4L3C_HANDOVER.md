# Sprint 4L.3C Handover

**Date:** 2026-11-24T00:07:54.485503+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status: UNSUCCESSFUL — blocker documented; no raw data acquired.**

## What was exhausted

- Environment variables, `launchctl`, macOS Keychain, shell profiles/history, EDIutils/R configs, project `.env`, agent/MCP configs.
- EDI IAM key-to-token endpoint (reachable; 400 missing key).
- PASTA metadata/data/authz/archive endpoints (403/500).
- EDI Data Portal (login redirect).
- DataONE CN (404; no replica), LTER GMN (403 across `/mn/...`), EDI GMN (403).
- DataONE token (none available; not attempted).
- Browser session (not used; would rely on user's authenticated account).

## Exact blocker

**No user-authorised EDI API key exists in this environment, and the documented keyless DataONE LTER member-node path is blocked at the host/path level (403).**

## What the user must do

Create/authorise a free EDI profile and API key, store it in Keychain/password manager, export it only in the acquisition shell, and run the prepared single-entity command (see `REQUIRED_USER_ACTION.md`). Alternatively, download manually via the EDI Data Portal.

## After acquisition

1. Verify size/MD5/SHA256.
2. Complete the raw audit in Sprint 4L.3: Mendota-only rows, dates/gaps, missingness, duplicates, taxonomy, units, outliers, effective N.
3. Do not label, model, or change Gate 2.

## Preserved evidence

All prior Sprint 4L.3 and 4K files remain unchanged. No commits/pushes. No unrelated downloads. No secrets logged.
