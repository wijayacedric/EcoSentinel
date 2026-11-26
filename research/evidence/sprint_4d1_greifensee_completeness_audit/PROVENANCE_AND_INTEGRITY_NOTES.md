# Provenance and Integrity Notes — Sprint 4D.1

**Date:** 2026-11-22T23:05:52.063742+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Sources
- C2G landing package CKAN: `opendata.eawag.ch/api/3/action/package_show?id=aquascope-images-and-classifications-may-2018-to-june-2023` (cached at `/tmp/eric_c2g.json` during Sprint 4D).
- Sprint 4D download manifest: `research/evidence/sprint_4d_alternative_acquisition/manifests/c2g_download_manifest.csv` (copied/used read-only).
- Acquired tarballs: `research/evidence/sprint_4d_alternative_acquisition/downloads/greifensee_2018_2023/biological/monthly/`.

## Integrity checks performed
- Manifest vs filesystem: all 39 `ok` class_and_feat_5p0x entries have local files present. No unexpected files substituted.
- Tarball content listing: all 39 acquired tarballs opened successfully with Python `tarfile`; member counts and basenames recorded.
- No files modified, renamed, deleted, or overwritten.

## Limitations
- Skipped 20 tarballs were **not downloaded and not content-inspected**; classification is based on manifest metadata, C2G monthly inventory, and per-month uniqueness.
- Acquired tarball inspection was structural (member lists, basenames, sampled headers/labels), not exhaustive semantic validation of every file/row.
- Taxon/class label completeness (including cyanobacteria classes) was not exhaustively enumerated across all files; samples showed classification/feature structures.
- No biological event labels, modelling, confirmatory analysis, or Gate 2 changes performed.
