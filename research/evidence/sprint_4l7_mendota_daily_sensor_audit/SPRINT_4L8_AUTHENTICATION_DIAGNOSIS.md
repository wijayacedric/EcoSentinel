# Sprint 4L.8 Authentication Diagnosis

**Date:** 2026-11-24T09:34:03.677381+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Exact failure

The acquisition process reported:

`LOCAL_CONFIGURATION_FAILURE: EDI_API_KEY is not set in this process`

A fresh run of the prepared authentication test produced the same result (exit 2) **before any network request**.

## What was checked (no secret values read/printed)

| Check | Result |
|---|---|
| `EDI_API_KEY` in current process | absent |
| `launchctl getenv EDI_API_KEY` | unset |
| `launchctl getenv PASTA_TOKEN` | unset |
| `launchctl getenv PASTA_API_KEY` | unset |
| macOS Keychain `ecosentinel-edi` | exit 44 (not found) |
| Keychain candidate services `EDI`, `edi`, `EDI_API_KEY`, `pasta`, `PASTA`, `edirepository` | all exit 44 |
| Shell/config files | no key value (prior 4L.3C/4L.3D targeted checks) |
| EDIutils/R config | no key |
| Agent/MCP config | no EDI key |
| Sensor-list file | already present/verified |

## Why the workflow cannot access the credential

`edi_mendota_acquire.py` reads `os.environ.get('EDI_API_KEY')`. The key was previously entered through an interactive hidden prompt in a different shell and exported only in that shell. That variable is **not inherited** by the OpenCode process or a new shell, and it was not persisted to `.zshrc`, Keychain, launchctl, EDIutils config, or an agent config.

This is a **local configuration/environment issue**, not evidence that the key is invalid. No token exchange was attempted; no 401/403 conclusion about key validity is made.

## Secure method remains available

The established secure method is user-run hidden input in a local Terminal (see `SPRINT_4L8_SECURE_KEY_RESTORE.md`). The agent cannot enter the secret on the user's behalf and must not request it in chat.

## Classification

**BLOCKED — AUTHENTICATION CONFIGURATION.** Further acquisition requires user action to restore the existing credential in the process environment.
