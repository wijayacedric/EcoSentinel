# External Search Log — Strategic Reconstruction

**Date:** 2026-11-25  
**Scope:** Targeted external search for (a) long-term paired lake datasets, (b) early-warning literature, (c) access terms. This was not a global census of every lake programme.

## 1. Source categories defined before searching

1. Repository evidence: protocols, sprints, decision registers, data audits, correspondence.
2. Primary peer-reviewed literature on cyanobacterial early warning and sensor–biovolume relationships.
3. Public data repositories and data papers: EDI, Borealis, FRDR, NOAA NCEI, IGB FRED, Swedish research data, SITES.
4. Institutional monitoring programmes and metadata pages.
5. Competition documentation (SciFest 2027).

## 2. Queries and sources inspected

| # | Query / action | Category | Result | Use / limitation |
|---|---|---|---|---|
| 1 | Repository-wide search for `4L.15`, `4L15`, `sprint_4l15`, `pivot`, `field study` | Repository | No 4L.15 package; only incidental binary matches | Established provenance gap |
| 2 | Inspected `README.md`, `AGENTS.md`, `documentation/SCIENTIFIC_PROTOCOL_DRAFT.md` | Repository | Original question and design recovered | Basis for Section C |
| 3 | Inspected 4L.11, 4L.12, 4L.14, 4L.14 independent review | Repository | Narrowing, estimands, decisions, review verdict | Basis for Sections B, F |
| 4 | Inspected 4F, 4L.9, 4L.10, data master mission | Repository | Dataset limitations and overlap counts | Basis for Section E |
| 5 | Inspected Buffalo Pound correspondence package | Repository | Leavitt reply; no data; Heather pending | Basis for Section D |
| 6 | `long-term lake high-frequency buoy phytoplankton microscopy biovolume dataset` | Literature/data | Greifensee, Detroit Lake, Lake Kasumigaura leads | Screening |
| 7 | `Lake Erken high frequency sensor phytoplankton long-term monitoring` | Data | Erken phytoplankton 1989–2011; HF chlorophyll 2019–2025 | Candidate assessed; no overlap |
| 8 | `Lake Müggelsee high-frequency monitoring phytoplankton biovolume dataset` | Data | IGB FRED packages 3 and 1145; Recknagel 2025 forecasting | Strongest external candidate |
| 9 | `GLEON high-frequency lake buoy paired phytoplankton microscopy data` | Data | GLEON, Lake Sunapee, general leads | No specific paired dataset verified |
| 10 | `Buelo 2022 early warning signals cyanobacteria blooms true positive false positive rate` | Literature | Buelo et al. 2022, Ecol Appl, DOI 10.1002/eap.2616 | EWS evaluation prior art |
| 11 | `O'Brien 2023 early warning indicators lake phytoplankton blooms evaluation` | Literature | O'Brien et al. 2023, Nat Commun 14:7942 | EWS limited applicability |
| 12 | `Cotterill 2019 phycocyanin fluorescence cyanobacteria biovolume weak relationship` | Literature | Cotterill et al. 2019, DOI 10.1080/00288330.2019.1617322 | Sensor–biovolume prior art |
| 13 | Direct fetch: `https://fred.igb-berlin.de/data/package/1145` | Data metadata | HF station, 1.5 m, 5-min, 2001–ongoing, phycocyanin; all rights reserved | Müggelsee assessment |
| 14 | Direct fetch: `https://fred.igb-berlin.de/data/package/3` | Data metadata | Phytoplankton 1979–ongoing; biomass/biovolume; all rights reserved | Müggelsee assessment |
| 15 | Direct fetch: `https://researchdata.se/en/catalogue/dataset/ecds0217-1` | Data metadata | Erken phytoplankton 1989–2011, species-level, weekly ice-free, open | Erken assessment |
| 16 | Direct fetch: `https://researchdata.se/en/catalogue/dataset/sites-m1prtgtfmw9w1asyj3xzdqm8` | Data metadata | Erken HF chlorophyll 2019–2025 | Erken overlap gap |
| 17 | Direct fetch: `https://meta.fieldsites.se/resources/stations/Erken` | Data metadata | Erken station description; long-term monitoring and HF measurements | Context only |

## 3. Sources identified but not fully inspected

| Source | Reason |
|---|---|
| Müggelsee phytoplankton CSV and HF data files | All rights reserved; request required |
| Müggelsee HF full variable list | Page metadata partly obscured; associated literature used cautiously |
| Lake Erken HF sonde variables and older sensor periods | Not fully verified; only chlorophyll 2019–2025 confirmed |
| Lake Kasumigaura dataset | Data paper identified; co-located HF sensor pairing not verified |
| Western Lake Erie raw NCEI archive | Prior sprint reported 503; not re-tested in this session |
| Boyer 2017 underlying data | Available on request; not requested |
| WSA/U Regina/City/USask records | Pending correspondence; not obtained |

## 4. Inaccessible or restricted sources

- **Müggelsee:** data files require permission from IGB; metadata pages are public.
- **Western Lake Erie:** NCEI raw archive unavailable in prior audit; no local files.
- **Boyer 2017:** underlying data not public; paper states available on reasonable request.
- **Buffalo Pound WSA:** no data or metadata beyond the existing correspondence.

## 5. Search stopping point

The search stopped when it had:

1. established the repository's latest verified state and the absence of a 4L.15 package;
2. identified at least one credible external candidate (Müggelsee) and one partial candidate (Erken);
3. confirmed that no external dataset is currently acquired or verified;
4. confirmed that the original question's binding constraints are data structure, not missing explanatory information.

This is sufficient for the strategic decision. It is not a full global dataset census, and it does not establish that no other suitable dataset exists.

## 6. Search limitations

- No researcher or data custodian was contacted during this assessment.
- No restricted dataset was accessed.
- No data were downloaded, ingested, or analysed.
- Metadata pages can lag or omit variable-level details; all external dataset claims are marked as unverified until a file-level audit.
