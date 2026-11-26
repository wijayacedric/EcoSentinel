# Institutional Evidence Status

**Sprint:** Schedule Recovery Sprint 2  
**Date:** 2026-11-22  
**Status:** Documentation-only reconciliation. No follow-ups sent. No external contact made.

## 1. Reported request status

| Institution / Contact | Repo-documented status (before this sprint) | User-reported status (2026-11-22 message) | Latest documented status in repo | Notes |
|---|---|---|---|---|
| Helen Baulch (University of Saskatchewan) | Gate 2E draft UNSENT; Gate 2G tracking template: `not_contacted_or_unknown` | User states request sent | **Reported sent by user; repo lacks send date/confirmation/response record** | Do not assume response/rejection. Update tracking template only with human-provided verified details. |
| Kristin Painter | No specific sent record found in repo templates; Gate 2E/2G drafts mention Boyer/Painter context | User states request sent | **Reported sent by user; repo lacks send date/confirmation/response record** | Same. |
| Blair Kardash (Buffalo Pound Water Treatment Plant context) | Gate 2G template lists BPWTP TBD `not_contacted_or_unknown` | User states request sent | **Reported sent by user; repo lacks send date/confirmation/response record** | Same. |
| Scott Higgins | Not named in Gate 2G tracking template; appears in user context | User states request sent | **Reported sent by user; repo lacks send date/confirmation/response record** | Same. |
| Saskatchewan Water Security Agency | Gate 2G template lists WSA TBD `not_contacted_or_unknown` | User states request sent | **Reported sent by user; repo lacks send date/confirmation/response record** | Same. |

**Constraint:** No response dates, commitments, or likely outcomes are invented. Silence is not treated as rejection.

## 2. Which requested records would resolve which gaps

| Record type | Could establish biological event timing? | Could establish non-event exposure? | Supporting context only? | Would not materially improve study? | Gap addressed |
|---|---:|---:|---:|---:|---|
| Boyer 2017 record-level phytoplankton/taxonomy/biovolume/raw sample table (SI/raw) | Potentially, if dated, method-documented, independent, and sufficient resolution | Possibly partially, only with explicit pre-approved criteria and gap handling; unlikely alone | No | No | 2017 event timing; reduces boundary uncertainty |
| Painter 2018-2019 raw sample metadata/field notes/toxin method/units/QA around 2019-07-17 anomaly | Partially (interval-censored only) | Unlikely; sparse sampling remains | Also contextual | No | 2019 anomaly resolution; metadata quality |
| BPWTP phytoplankton taxonomy/cell counts/biovolume/lab chl-a (2014-2021) | Potentially, if record-level, dated, method-documented | Potentially, if sampling design and QA support defensible exposure intervals under approved rules | No | No | 2014-2016/2020-2021 coverage gap; exposure denominator |
| BPWTP cyanotoxin/microcystin method details and historical records beyond annual summaries | Limited (toxin != bloom event definition by itself) | No | Yes, supporting | No | Toxin context; cannot alone define bloom/non-bloom |
| WSA phytoplankton/cyanobacteria monitoring records (if they exist for Buffalo Pound 2014-2021) | Potentially | Potentially | No | No | Coverage/independent confirmation |
| WSA chemistry-only records without phytoplankton/taxon/toxin biological measures | No | No | Yes | Mostly | Context only |
| Painter 2023 buoy/GAM derived classifications | No | No | Yes (non-independent) | As ground truth, yes | Not usable as independent biological evidence |
| General correspondence without data/metadata | No | No | Yes | Possibly | Process only |

## 3. Evidence gaps mapped to requests

| Gap | Best potential source | Minimum required metadata | Can close gap alone? |
|---|---|---|---|
| 2014-2016 biological coverage | BPWTP/WSA historical phytoplankton/lab records | Dates, location, depth, method, units, QA, taxonomy/biovolume/counts | Possibly partially |
| 2017 raw independent biological reconstruction | Boyer 2017 raw/SI | Sample IDs, dates/times, depth, location, counts/biovolume, methods, QA | Possibly partially |
| 2018-2019 anomaly/metadata uncertainty | Painter field notes/toxin metadata | 2019-07-17 sampling context, QC flags, toxin units/LOD/method | No, but improves confidence |
| 2020-2021 biological coverage | BPWTP/WSA records | Same as above | Possibly partially |
| Defensible non-event exposure | Any continuous/adequately frequent independent biological program with QA | Sampling design, detection limits, absence criteria, method consistency | Uncertain; likely requires multiple sources + approved rules |

## 4. Recommended repo hygiene (human action only)

- Update `research/evidence/gate2g/data_intake/templates/institutional_response_tracking_template.csv` with verified send dates/responses only when human provides documentation.
- Do not mark "rejected" without explicit evidence. Do not infer outcomes.
