# Sprint 4L.3D Executive Report — Existing EDI Key Configuration & Acquisition

**Date:** 2026-11-24T07:10:03.729185+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status: AWAITING USER KEY INPUT — NOT COMPLETE.**

## 1. What was done

- Read `/Users/cedricbw/Documents/EcoSentinel/AGENTS.md` in full.
- Inspected the existing acquisition script (`research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py`) and the Sprint 4K/4L.3/4L.3C evidence.
- Verified the target entity and expected integrity values from EML/ORE: `f2de15b2fff6ae962a04c150c0a1c510`, 2,448,830 B, MD5 `a0363cc7fdfd6c12889750fea27bd542`.
- Prepared a secret-safe interactive key-entry helper and a separate authentication test. Neither stores the key nor prints secrets.
- Did **not** create, rotate, replace, revoke, or request a key.
- Did **not** enter or test the existing key, because the user must do that locally.

## 2. Authentication status

**Not yet tested against the existing key.** The key is not present in this agent environment, and the task requires the user to enter it locally with echo disabled. No conclusion about key validity is drawn.

A local missing-variable test of the prepared test script returns `LOCAL_CONFIGURATION_FAILURE` (exit 2); that is not an authentication result.

Previous evidence (empty request to the IAM endpoint) returned HTTP 400 "missing key"; the endpoint is reachable. Anonymous PASTA requests return 403. Those are configuration/authorisation checks, not tests of the user's key.

## 3. Secure procedure prepared

User runs in their own Terminal:

```bash
zsh research/evidence/sprint_4l3d_existing_key_authentication/scripts/acquire_88_31_with_prompt.sh
```

It:
1. Prompts for the key with echo disabled.
2. Puts the key only in the process environment.
3. Exchanges it at the official EDI IAM endpoint.
4. Tests one PASTA metadata read.
5. If successful, runs the existing acquisition script for **only** `88.31` / `f2de15b2...`.
6. Verifies size, MD5 and SHA256.
7. Unsets the key on exit.

No key is written to disk, passed as a command-line argument, or printed.

## 4. Acquisition

**No CSV acquired.** The prior attempt failed before any network request because `EDI_API_KEY` was absent. This sprint stops at the user-input boundary; the single-entity acquisition has not been run with the existing key.

## 5. Script inspection

The existing script is suitable for authentication and controlled acquisition:
- reads `EDI_API_KEY` from the environment;
- POSTs `{"key": ...}` to `https://auth.edirepository.org/auth/v1/key`;
- keeps `edi-token` in memory and sends `Cookie: edi-token=...`;
- never prints key/token; provenance excludes secrets;
- enforces PASTA data URL prefix;
- bounded retries; no retry on 401/403/404;
- resumable `.part`, no overwrite, SHA256/provenance.

**Gap identified:** its EML parser looks for `<checksum>`, while 88.31 uses `<authentication method="MD5">`, so it does **not** verify the expected MD5 itself. Size is checked when EML size is parsed. The wrapper therefore performs an independent MD5 check after acquisition. No script change was made; the evidence did not justify altering it before acquisition.

## 6. Required user action

Run the helper in a local Terminal and enter the existing key at the hidden prompt. If authentication fails, the helper prints only a safe category (authentication/authorization/network/local configuration) and does not acquire data. If it succeeds, it acquires the single entity and prints size/MD5/SHA256.

## 7. Gate 2

**Gate 2 remains PAUSED / NOT APPROVED — Option C (Exploratory Only).** No labels, event intervals, modelling, hypothesis tests, confirmatory analysis, protocol changes, external contacts, uploads, commits or pushes. No secret appears in this report.
