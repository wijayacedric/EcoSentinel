# DataONE Replica Verification (Sprint 4E.1B)

**Date:** 2026-11-23T00:09:53.866270+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Summary

All three target DOIs resolve to DataONE-indexed ORE resource maps on CN (urn:node:CN replica listed). Package revisions identified from ORE members:

| Target | DOI | Package revision (from ORE) | ORE on CN | CN sysmeta/read |
|---|---|---|---|---|
| Phytoplankton | 10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9 | knb-lter-ntl.88.31 | Yes (4123 B, SHA-1 cda422be...) | Metadata EML publicly readable from CN (27408 B, SHA-256 prefix c96ddc258080971d) |
| HF buoy temp | 10.6073/PASTA/8CEFF296AD68FA8DA6787076E0A5D992 | knb-lter-ntl.130.29 | Yes (19558 B, SHA-1 7ffe1ffe...) | 17/18 member sysmeta 200 on CN; 1 data member has no CN sysmeta/solr |
| Microbial Observatory | 10.6073/PASTA/7E533C197ED8EBD27777A89A2C8D7DFE | knb-lter-ntl.415.2 | Yes (6169 B, SHA-1 4347c4b5...) | All non-ORE members sysmeta 200 on CN |

## Verification details

- **88.31**: ORE members include metadata EML, 1 data CSV (`f2de15b2fff6ae962a04c150c0a1c510`, 2,448,830 B, text/csv, CN sysmeta 200), and report. Metadata object was publicly readable from CN; content confirms packageId `knb-lter-ntl.88.31`.
- **130.29**: 18 members in ORE (16 data + metadata + report). CN sysmeta returned 200 for 17 members; **missing on CN sysmeta/solr**: `https://pasta.lternet.edu/package/data/eml/knb-lter-ntl/130/29/c7538c460f8d0cbd90ec2892b8ce3025` (present in ORE, no CN sysmeta, Solr numFound=0). This is an integrity/replication discrepancy to resolve before treating 130.29 as fully CN-replicated.
- **415.2**: 5 members in ORE (3 data + metadata + report). All non-ORE members have CN sysmeta 200.

## Reconciliation with EDI

- **Package revision identity:** Confirmed from ORE/DataONE PIDs (88.31, 130.29, 415.2) - matches user-specified targets.
- **Checksum reconciliation with EDI:** **Not completed.** EDI PASTA endpoints require authentication in this environment (403 Public Access not authorized in prior 4E.1; no API key available). CN sysmeta provides checksums/sizes for most members, but I cannot compare them to live EDI PASTA checksums without authorised EDI access.
- **Public readability:** Metadata EML for 88.31 is publicly readable from CN. I did **not** download large data objects; only sysmeta checks and one small metadata read were performed.

## Caveats

- DataONE CN replica availability != confirmed full, authorised EDI-equivalent access for all entities.
- The 130.29 missing CN member is a blocking discrepancy for "complete verified public replica" claim for that package.
- Licence/rights at package level still require human/authorised review.
