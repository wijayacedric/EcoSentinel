# Manifest Integrity Clarification

**Date:** 2026-11-24T08:45:50.090661+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Finding

Sprint 4L.6 reported that 43 non-manifest Sprint 4L.5 files match their recorded SHA-256 values, but the register's self-hash entry does not match the register's current hash.

Independent check:

- Original register: `research/evidence/sprint_4l5_mendota_raw_biology_audit/EVIDENCE_SHA256_REGISTER.csv`
- Entries: 44 total; 43 non-self + 1 self.
- **43/43 non-self entries match** their recorded SHA-256.
- Self entry: bytes 7,065; recorded SHA-256 `480101ee6867800ae535c43dafb4f4294b8fb4b2c46d4ca8cdec394203efafff`.
- Current register: 7,065 bytes; SHA-256 `0aeb9e8636fdceac723760d4bd981050e12791ffe31932d442d2890bf5a0cbdc`.
- The size matches; the hash does not.

## Explanation

This is an expected **self-reference limitation**. A manifest cannot contain its own final SHA-256: adding or changing the self entry changes the file hash. The self entry is stale relative to the final register bytes. It is not evidence of biological-data corruption; all 43 non-self files verify.

## Resolution (original preserved)

- Original register was **not modified**.
- `SPRINT_4L5_REGISTER_NONSELF_VERIFICATION.csv` records 43/43 matches.
- `SPRINT_4L5_REGISTER_V2_NONSELF.csv` is a corrected manifest excluding itself.
- `SPRINT_4L5_REGISTER_V2_NONSELF.csv.sha256` is a sidecar hash of the V2 manifest (`3798f085f1e9fdc7d9b7047b979ec36918b78a6d968cedf2cc635dd8f81356ea`).

## Reproducible procedure

1. Verify every non-self entry against its file.
2. Exclude the manifest itself from its own entries.
3. Write the manifest.
4. Compute a sidecar `.sha256` for the manifest.
5. Never overwrite a historical manifest; version it.

No biological evidence is discarded or reclassified by this clarification.
