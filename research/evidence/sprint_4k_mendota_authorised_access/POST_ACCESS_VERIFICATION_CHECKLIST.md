# Post-Access Verification Checklist

**Date:** 2026-11-23T23:36:48.967538+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Before running acquisition

- [ ] User has created/authorised an EDI profile and scoped key; key is stored securely.
- [ ] `EDI_API_KEY` is set only in the current shell; not in repo/history.
- [ ] Output directory is on local SSD; free space checked.
- [ ] No other acquisition process is writing to the same directory.
- [ ] Package/revision IDs confirmed: 88.31, 129.42, 130.29, 415.2.
- [ ] Script reviewed; no key in command line or logs.

## Metadata/inventory

- [ ] `metadata_<pkg>.xml` exists, >0 B, parseable XML.
- [ ] Package ID and revision in EML match the requested package.
- [ ] `entity_inventory_<pkg>.csv` lists entities with URLs, sizes, checksums.
- [ ] No entity URL outside `pasta.lternet.edu/package/data/`.
- [ ] Provenance row exists for metadata; no key/token in provenance.

## Data entities

- [ ] Download used explicit `--entity`; no unintended entity fetched.
- [ ] File size matches EML size (or documented exception).
- [ ] SHA256 recorded; EML checksum verified where available.
- [ ] CSV/table readable; header matches EML attributes.
- [ ] Row count >0; no truncation at end; date range plausible.
- [ ] Existing files were not overwritten; `.part`/`.mismatch` preserved if any.
- [ ] Raw file stored separately from derived audit outputs.

## Content checks

- [ ] 88.31: `lakeid` values; Mendota subset; `depth_range`; 15 columns; cell density/biovolume/biomass populated; taxa/cyanobacteria; 2013 taxonomy changes.
- [ ] 129.42: sensor list 5 columns; 4 entities; per-variable coverage; flags; Turner/YSI eras; no assumption that 2006-2025 applies to all channels.
- [ ] 130.29: 16 entities; depth/year coverage; 2015 HR gap confirmed.
- [ ] 415.2: 3 tables; handheld frequency/depths; pH/conductance only 2014-2019.
- [ ] Station/depth/timestamp alignment documented; no interpolation.
- [ ] No bloom/non-bloom labels, event intervals, modelling, or confirmatory analysis.

## No-substitution check

- [ ] No SSEC/Metobs file in EDI package directories.
- [ ] Any SSEC cross-check is separate, labelled, and not treated as EDI observations.
- [ ] No EDI file modified/renamed; derived tables only.

## Provenance and licence

- [ ] Source URL, retrieval time, size, SHA256, package revision recorded.
- [ ] Package-level licence confirmed (NTL CC BY expected; verify).
- [ ] Raw data retention and citation plan documented.

## Sign-off

- [ ] Audit reviewed by a second person or independent agent.
- [ ] Unresolved issues logged; no silent repairs.
