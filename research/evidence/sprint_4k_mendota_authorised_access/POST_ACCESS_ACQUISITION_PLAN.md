# Post-Access Acquisition Plan

**Date:** 2026-11-23T23:36:48.967538+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Principle

**Metadata first, explicit entities second, raw files preserved, provenance always.** No bulk crawling, no repeated failed requests, no silent substitution.

## Prepared script

`scripts/edi_mendota_acquire.py` (stdlib only; not executed in Sprint 4K).

### Safety features
- Requires `EDI_API_KEY`; never prints/stores it.
- Exchanges the key for a short-lived token via the official IAM endpoint; sends `Cookie: edi-token`.
- Metadata + entity inventory by default.
- Data only with **both** `--include-data` and an explicit `--entity`.
- Refuses any data URL outside `https://pasta.lternet.edu/package/data/`.
- Resumable `.part` files via HTTP Range; restarts cleanly if Range is unsupported.
- Bounded retries for 429/5xx/network only; no retry for 401/403/404.
- SHA256 + size + EML checksum verification; mismatches preserved as `.mismatch`, never silently repaired.
- Never overwrites an existing complete file.
- `provenance.csv` records source URL (no key), timestamps, bytes, SHA256, EML checksum, HTTP status, resume flag, and outcome.

## Step 1 — Metadata and inventory only

```bash
export EDI_API_KEY="$(security find-generic-password -a "$USER" -s ecosentinel-edi -w)"
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py \
  --package all --list-only
```

Outputs under `acquisition/<package>/`:
- `metadata_<package>.xml`
- `entity_inventory_<package>.csv`
- `provenance.csv`

Inspect inventory sizes/checksums before any data request.

## Step 2 — Priority entities

1. **129.42 sensor list** (small, resolves per-variable coverage):
   `edddc490dfd553c4c4b9e5d4b86eb2eb`
2. **88.31 biological CSV**:
   `f2de15b2fff6ae962a04c150c0a1c510` (~2.45 MB)
3. **415.2** three small tables (inventory IDs):
   `22da50a9bf813999c3e2987af86ca8e7`, `d748c9a0f9ca5c25fd631f24073fba5c`, `4c0fa94c12d7000aa8f7224882bd095e`
4. **129.42 daily** `cba9ed12834b8f315d6b10675bb60c5a` (start here; hourly/HR later if needed)
5. **130.29** daily/hourly first; avoid all 16 entities until the inventory confirms size/need; 2015 HR is expected missing.

Example (88.31 only):
```bash
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py \
  --package 88.31 --include-data --entity f2de15b2fff6ae962a04c150c0a1c510
```

Add `--max-bytes 0` only for a deliberately approved large entity.

## Step 3 — Interrupted downloads

- Re-run the same command. The script resumes `.part` if the server supports Range; otherwise it restarts that entity.
- If an entity finishes but fails size/checksum, it is preserved as `.mismatch`; do not delete or "fix" it. Investigate before retrying.
- Do not run two acquisition processes for the same output directory.

## Step 4 — Storage and separation

- Raw downloads: `acquisition/<package>/...` (original bytes; never edit).
- Derived audit tables/plots: separate `audit/` directory; transformations only on copies.
- Do not place keys, tokens, or config files in the acquisition tree.
- Monitor disk; stop before large downloads if free space is insufficient.

## Step 5 — No substitution

The script has no SSEC/Metobs code path. SSEC data may only be used, if at all, as a clearly labelled exploratory cross-check in a separate directory; it must never be written into EDI package directories or treated as EDI observations.
