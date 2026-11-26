# Access Recovery Report — Mendota (Sprint 4E.1B)

**Date:** 2026-11-23T00:09:53.866270+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Objective

Determine whether Mendota target datasets can be accessed through an authorised EDI API key or a verified public DataONE replica, after Sprint 4E.1 anonymous PASTA failure.

## Findings

1. **EDI auth requirement:** Corroborated by web sources - EDI PASTA REST API requires authentication effective 2026-07-30. No authorised EDI API key found in environment; user authorisation required.
2. **DataONE replica evidence:** All three DOIs have ORE resource maps indexed on DataONE CN. Package revisions match targets: 88.31, 130.29, 415.2. Most member objects have CN sysmeta (checksums/sizes). 88.31 metadata EML is publicly readable from CN.
3. **Blocking gaps:** (a) No EDI API key - cannot use authorised PASTA path. (b) 130.29 has one ORE member missing from CN sysmeta/solr (`c7538c4...`) - cannot claim complete verified CN replica for buoy package. (c) EDI-vs-CN checksum reconciliation not completed without EDI auth. (d) Large data files not downloaded; full file-level verification not performed.

## Final decision

**Mendota is NOT classifiable as unavailable merely because anonymous PASTA requests fail.** However, **full authorised/verified access for all three target packages is not yet confirmed in this environment.**

- **Authorised EDI API key path:** Possible in principle per EDI docs, but **blocked pending user authorisation** (no key in environment).
- **Verified public DataONE replica path:** **Partially supported.** OREs and most member sysmeta are verifiable on CN; 88.31 metadata readable. But 130.29 has an unresolved missing-member discrepancy, and EDI checksum reconciliation/full data acquisition were not completed.

**Status:** CONDITIONAL/UNRESOLVED — user authorisation for EDI API key or a deliberate DataONE metadata-first acquisition plan (with discrepancy handling) is required.
