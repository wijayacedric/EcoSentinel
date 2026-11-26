# Next Required Actions (Sprint 4E.1B)

**Date:** 2026-11-23T00:09:53.866270+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

1. **User authorisation (EDI path):** If EDI API access is desired, provide an authorised EDI API key through an approved secure mechanism (not chat, not committed). After availability, retrieve metadata first, inspect entity names/sizes/checksums, then acquire only required files; record SHA256 and provenance.
2. **DataONE discrepancy resolution:** Investigate missing 130.29 member `https://pasta.lternet.edu/package/data/eml/knb-lter-ntl/130/29/c7538c460f8d0cbd90ec2892b8ce3025` (in ORE, absent from CN sysmeta/solr). Do not assume package completeness.
3. **Checksum reconciliation:** Once EDI or another authoritative source is accessible, reconcile CN sysmeta checksums/sizes against EDI PASTA metadata for the exact package revisions.
4. **Metadata-first acquisition:** If using DataONE CN public reads, download metadata/EML and small manifests first; verify checksums; only then consider large data entities, with disk-space and integrity checks.
5. **Licence/human review:** Confirm package-level licences/terms before reuse.
6. **No Gate 2 progression:** Do not create event labels, non-bloom intervals, or modelling outputs. Keep Gate 2 PAUSED / NOT APPROVED.

No external contacts, uploads, commits, or pushes.
