# Authorised Access Pathway

**Date:** 2026-11-23T23:32:06.599235+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Official procedure (documented)

1. EDI requires authentication for all REST API access since **2026-07-30**.
2. Obtain a **free EDI user profile** via the EDI Identity and Access Manager (IAM) portal: `https://auth.edirepository.org/auth/ui/`.
3. Sign in with Google, Microsoft, GitHub, or ORCiD; no institutional account is required by the documented procedure.
4. Generate/obtain an **API access key** from the IAM portal.
5. Use the key with EDIutils `login(key=...)` or the REST API auth mechanism. Do **not** store the key in the repository or chat.
6. Alternatively, sign in to the EDI Data Portal and download via the package page.

## What is required

- **Authorization:** a user-controlled EDI profile/API key. No data-use agreement is indicated by the metadata, but package-level terms should be confirmed.
- **Institutional account:** not indicated as required.
- **Researcher approval:** not indicated for these public packages; NTL data are described as CC BY. 415.2 has a named contact (Katherine McMahon) but no restriction flag in the metadata inspected.
- **Technical:** API key via environment variable or secure local secret store; network access to `pasta.lternet.edu`/`portal.edirepository.org`.

## Appropriate contacts (do not contact in this sprint)

- NTL information manager: `lter.im@limnology.wisc.edu` (129.42); `ntl.infomgr@gmail.com` (88.31/130.29).
- 415.2 contact: Katherine (Trina) McMahon, `trina.mcmahon@wisc.edu`.
- EDI support: via EDI portal/contact page (not emailed here).

## Technical access checklist

1. Create/authorise EDI profile and API key (user action).
2. Store key securely; never commit/print.
3. Test metadata retrieval for 88.31/129.42/130.29/415.2.
4. List entities/sizes/checksums; record package revisions.
5. Download metadata and smallest relevant entities first.
6. Record source URL, timestamp, size, SHA256, HTTP outcome, licence.
7. Verify CSV readability/headers; do not modify originals.
8. Audit 88.31 `lakeid`, station, depth, taxa, units, QC; audit 129.42 sensor list and per-channel coverage; audit 415.2 frequency/depths.
9. Only then assess alignment/feasibility.

## Alternative public route (not equivalent)

- SSEC/AOSS Metobs API: public, documented; 2019-2025 samples verified (2006/2018 queries returned 0 results).
- No QC flags; different product/processing; not a substitute for EDI 129.42/130.29.
- Use only as exploratory cross-check if needed.

## Prohibitions

No account creation, credential request, secret storage, access-control bypass, or external contact in this sprint.
