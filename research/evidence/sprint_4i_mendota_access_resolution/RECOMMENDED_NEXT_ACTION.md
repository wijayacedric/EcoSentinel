# Recommended Next Action

**Date:** 2026-11-23T23:32:06.599235+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Immediate

1. **User-authorised EDI access:** create/authorise a free EDI profile and API key through the official IAM portal; store securely. This is the only route to the actual EDI data bytes.
2. **Metadata-first retrieval:** download 88.31/129.42/130.29/415.2 metadata and entity inventories; record sizes/checksums/revisions.
3. **Then smallest relevant entities:** 88.31 phytoplankton CSV; 129.42 sensor-list table + daily aggregates; 415.2 data tables; 130.29 daily/hourly before HR.
4. **File-level audit:** `lakeid`, station/depth, taxa/units/QC; sensor-list per-channel coverage; 415.2 frequency; alignment.

## Do not

- Do not claim raw-data feasibility until bytes are verified.
- Do not use SSEC 2019-2025 as a substitute for EDI 129.42/130.29 (no QC, no 2006-2018).
- Do not create labels, event intervals, models, or Gate 2 changes.
- Do not contact researchers or create accounts autonomously.

## Decision

Mendota remains **CONDITIONAL (authorization-required)** and potentially the strongest candidate. Buffalo Pound remains pending researcher clarification. No confirmatory candidate selected.
