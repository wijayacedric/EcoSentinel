# Sprint 4K Executive Report — Mendota Authorised Access Preparation

**Date:** 2026-11-23T23:36:48.967538+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Purpose

Prepare a safe, documented path for the user to obtain legitimate EDI access and for OpenCode to run a rigorous post-access audit, without creating accounts, handling secrets, or acquiring data in this sprint.

## What is ready

1. **Verified access pathway** against official EDI documentation: free IAM profile via Google/Microsoft/GitHub/ORCiD; API Access Key from the IAM profile menu; key exchanged for a short-lived `edi-token` (or appended as `?key=` per official docs). No institutional account or DUA is indicated for these public packages; package-level terms still require confirmation.
2. **Human-operated setup guide** (`EDI_USER_ACCESS_GUIDE.md`) with exact steps and official source links.
3. **Secure credential handling** (`SECURE_CREDENTIAL_HANDLING.md`): no chat, no repo, no evidence, no URLs with keys, environment/Keychain/password-manager options, rotation/revocation.
4. **Executable acquisition helper** (`scripts/edi_mendota_acquire.py`): metadata-first; explicit `--entity` required for data; key never printed/stored; token-cookie auth; SHA256/provenance; resumable `.part`; bounded retries; refuses non-PASTA URLs; never overwrites.
5. **Separate audit plans** for 88.31 biology and 129.42/130.29/415.2 environment, with explicit checks for Mendota-only records, per-variable coverage, cadence/missingness, sensor deployments/depths/coordinates, biological dates/depth integration, method changes and QC.
6. **Verification checklist** and **handover**.

## What is not done

- No EDI account or API key was created.
- No secret was requested, printed, stored or committed.
- No EDI data bytes were acquired in this sprint.
- SSEC/AOSS Metobs data were **not** substituted for EDI observations; the acquisition script only targets `pasta.lternet.edu/package/data/`.
- No labels, event intervals, modelling, hypothesis tests, confirmatory analysis, or protocol/Gate 2 changes.

## Required next action

The user creates/authorises a free EDI profile and a scoped API key, stores it securely, and exposes it only as `EDI_API_KEY` in the environment. OpenCode then runs:

```bash
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py \
  --package all --list-only
```

Then selects explicit entities for 88.31, 129.42 (sensor list first), 415.2 and, if needed, 130.29.

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).**
