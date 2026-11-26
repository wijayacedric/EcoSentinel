# Sprint 4K Handover

**Date:** 2026-11-23T23:36:48.967538+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Ready for the user

- `EDI_USER_ACCESS_GUIDE.md`: official IAM registration and API-key steps.
- `SECURE_CREDENTIAL_HANDLING.md`: key/token storage and incident rules.
- `scripts/edi_mendota_acquire.py`: metadata-first, explicit-entity acquisition with token-cookie auth, hashes, provenance, resume, bounded retries, no overwrite.
- `POST_ACCESS_ACQUISITION_PLAN.md`: phased acquisition and priority entities.
- `BIOLOGICAL_DATA_AUDIT_PLAN.md` and `ENVIRONMENTAL_DATA_AUDIT_PLAN.md`: separate audit procedures.
- `POST_ACCESS_VERIFICATION_CHECKLIST.md`: integrity and no-substitution checks.

## Blocked on user action

1. Create/authorise a free EDI profile and API key (OpenCode will not do this).
2. Store the key securely (Keychain/password manager); expose only as `EDI_API_KEY` for the session.
3. Then OpenCode can run metadata/inventory, audit, and explicitly approved entity downloads.

## Not done / not claimed

- No EDI account/key created.
- No EDI data bytes acquired in Sprint 4K.
- No SSEC substitution.
- No labels, event intervals, modelling, hypothesis tests, confirmatory analysis, or Gate 2 change.

## First commands after key is available

```bash
export EDI_API_KEY="$(security find-generic-password -a "$USER" -s ecosentinel-edi -w)"
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py --package all --list-only
```

Then inspect inventories and select explicit entities (129.42 sensor list first; 88.31 biological CSV next).

## Remaining scientific blockers

- Per-variable 129.42 coverage and sensor eras.
- 88.31 Mendota subset, taxonomy, units, QC, depth integration.
- Depth/station alignment between 0-8 m composite biology and buoy sensors.
- 130.29 2015 HR gap.
- Event/non-bloom adjudication (Gate 2; not authorised).

## Status

Mendota remains **CONDITIONAL (authorization-required)** and potentially the strongest candidate. Buffalo Pound remains pending researcher clarification. Gate 2 remains paused.
