# Package Metadata and Version Reconciliation (Sprint 4E.1C)

**Date:** 2026-11-23T07:05:41.270436+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Targets

| Target | DOI | Package revision (ORE/EML) | ORE on CN | Metadata on CN | EDI checksum reconciliation |
|---|---|---|---|---|---|
| Phytoplankton | 10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9 | knb-lter-ntl.88.31 | Yes | Yes (public read OK) | Not completed (no authorised EDI access) |
| HF buoy temperature | 10.6073/PASTA/8CEFF296AD68FA8DA6787076E0A5D992 | knb-lter-ntl.130.29 | Yes | Yes (public read OK) | Not completed |
| Microbial Observatory | 10.6073/PASTA/7E533C197ED8EBD27777A89A2C8D7DFE | knb-lter-ntl.415.2 | Yes | Yes (public read OK) | Not completed |

## Evidence

- ORE resource maps retrieved from DataONE CN object store and stored in `downloads/<pkg>/ore_*.rdf`. Member PIDs confirm package revisions 88.31, 130.29, 415.2.
- Metadata EMLs retrieved from CN and stored in `downloads/<pkg>/metadata_*.xml`.
- CN sysmeta checks (Sprint 4E.1B/4E.1C) provide checksums/sizes for most members. No live EDI PASTA checksum comparison possible without authorised API key.

## Discrepancies

- **130.29 missing CN member:** `https://pasta.lternet.edu/package/data/eml/knb-lter-ntl/130/29/c7538c460f8d0cbd90ec2892b8ce3025` (High Resolution Water Temperature - Lake Mendota - 2015, 2015-06-25 to 2015-09-01) is in ORE and EML distribution URL but CN resolve/sysmeta/solr return 404/not found. CN replica completeness for 130.29 is **not confirmed**.
- **Data object CN readability:** 88.31 metadata was publicly readable; a CN Range request for the 88.31 data object returned 404. This suggests sysmeta presence does not guarantee public object-byte readability on CN for all objects. Full data-access testing was deferred to avoid unnecessary large downloads.
