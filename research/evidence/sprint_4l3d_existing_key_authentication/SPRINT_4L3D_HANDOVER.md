# Sprint 4L.3D Handover

**Date:** 2026-11-24T07:10:03.729185+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status: AWAITING USER KEY INPUT — NOT COMPLETE.**

## What is ready

- Secure interactive helper:
  `research/evidence/sprint_4l3d_existing_key_authentication/scripts/acquire_88_31_with_prompt.sh`
- Secret-safe authentication test:
  `research/evidence/sprint_4l3d_existing_key_authentication/scripts/test_existing_key.py`
- Existing acquisition script inspected; **no changes made**.
- Target verified: entity `f2de15b2...`, size 2,448,830, MD5 `a0363cc7...`.
- All reports/deliverables created; raw-data sections clearly marked not performed.

## Exact user action

Run in your local Terminal:

```bash
zsh research/evidence/sprint_4l3d_existing_key_authentication/scripts/acquire_88_31_with_prompt.sh
```

Enter the existing key at the hidden prompt. Do not paste it into chat.

The helper will:
1. exchange the key at the official IAM endpoint;
2. test one PASTA metadata read;
3. acquire only `88.31` / `f2de15b2...`;
4. verify size/MD5/SHA256;
5. unset the key.

## After it runs

Provide the safe console output (no key/token) or simply say it finished. Then:

1. Confirm the acquisition directory and provenance.
2. Complete the raw structural audit in `BIOLOGICAL_DATA_STRUCTURAL_AUDIT.md` and `DATA_QUALITY_AND_MISSINGNESS.md`.
3. Populate `MENDOTA_COVERAGE_AND_SAMPLING_AUDIT.csv` with actual counts.
4. Verify taxonomy/2013 changes and variable consistency.
5. Do not label, model, or change Gate 2.

## If authentication fails

The helper prints a safe category:
- authentication failure (400/401),
- authorization failure (403),
- network/TLS failure,
- local configuration failure,
- service failure.
Do not create/replace the key until the category is understood.

## Not done

- No key entry or authentication test with the existing key.
- No CSV acquisition.
- No raw integrity/structural audit.
- No labels/modelling/commits/pushes.
