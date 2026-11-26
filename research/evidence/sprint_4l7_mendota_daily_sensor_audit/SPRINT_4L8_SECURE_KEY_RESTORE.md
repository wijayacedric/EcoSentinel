# Sprint 4L.8 Secure Key Restore Procedure

**Date:** 2026-11-24T09:34:03.677381+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## What is needed

The existing user-owned EDI API key must be made available to the acquisition process **without** being pasted into chat, a file, a report, or a command line.

## Preferred: run the hidden-input helper in your Terminal

```bash
zsh research/evidence/sprint_4l7_mendota_daily_sensor_audit/scripts/acquire_129_42_daily_with_prompt.sh
```

The helper:
1. prompts `EDI API key (input hidden):` with echo disabled;
2. puts the key only in that process environment;
3. runs the official IAM token exchange and one PASTA metadata check;
4. if successful, acquires **only** `cba9ed...` daily entity;
5. verifies 490,187 bytes, MD5 `eb7b3a...`, and SHA-256;
6. unsets `EDI_API_KEY` on exit.

Do not paste the key into chat. Do not ask the agent to enter it.

## Optional Keychain (repeatability only)

```bash
security add-generic-password -a "$USER" -s ecosentinel-edi -U
export EDI_API_KEY="$(security find-generic-password -a "$USER" -s ecosentinel-edi -w)"
# run the helper or acquisition command; then:
unset EDI_API_KEY
```

Keychain is optional; the hidden-input helper is sufficient for one acquisition. Do not commit config/Keychain exports.

## If authentication fails

The helper/test prints a safe category only:
- authentication failure (400/401),
- authorization failure (403),
- network/TLS failure,
- local configuration failure,
- service failure.

Do not create or rotate a key until the category is understood. No key validity conclusion has been made here.
