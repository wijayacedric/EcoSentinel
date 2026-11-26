# EDI Authentication Status (Sprint 4E.1B)

**Date:** 2026-11-23T00:09:53.866270+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. Documentation verification

- Web search (2026-11-22) indicates EDI announced mandatory authentication for all PASTA REST API access effective **2026-07-30** as a deterrent to Denial of Service attacks. Sources observed in search: edirepository.org news, EDIutils CRAN/R documentation (login()/API key required), edi-mcp documentation.
- Direct fetch of `https://edirepository.org/news/news-20240730.00` returned HTTP 500 in this environment; `https://edirepository.org/news` returned 404. I could not retrieve the canonical EDI news page body in this session. The authentication requirement is **corroborated by multiple independent package/docs sources** but the primary EDI news page was not successfully fetched here.

## 2. Environment key check

- Checked common env var names (EDI_API_KEY, EDI_TOKEN, PASTA_TOKEN, PASTA_API_KEY, EDI_AUTH_TOKEN, EDI_API_TOKEN, DATAONE_TOKEN, DATAONE_AUTH_TOKEN): **none found**.
- Checked common config paths (~/.config/edi, ~/.edi, ~/.pasta, ~/.config/dataone): **none found**.
- No API keys were printed, stored, or committed.

## 3. Required action

**User authorisation is required** to use an authorised EDI API key. I cannot create accounts, request credentials through chat, or attempt authentication without permission. If a key is legitimately provided/available in environment through an authorised channel, metadata-only retrieval and entity inspection should be performed first, with SHA256/provenance recorded.
