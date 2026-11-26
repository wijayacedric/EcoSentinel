# External Search Log — Sprint 4L.19

**Sprint:** 4L.19  
**Date:** 2026-11-25  
**Scope:** Buffalo Pound provenance, custodian identification, independent reviewer candidates, Stage 1 originality/viability, Müggelsee Stage 2 evidence, competition/licence context.  
**Status:** Search completed for the sources accessible in this environment. No external contact was made in this sprint.

---

## 1. Method

The search followed the project’s evidence hierarchy:

1. original datasets and repository metadata;
2. original publications and data papers;
3. official institutional profiles and ORCID records;
4. manufacturer/instrument documentation;
5. official monitoring-programme documentation;
6. peer-reviewed literature and reviews;
7. secondary sources only when primary sources were unavailable.

Sources were recorded in `UPDATED_SOURCE_REGISTER.csv` with an evidence grade (A–E). Inaccessible sources were recorded with the reason (403, 404, paywall, security check, timeout, rate limit).

**Important:** this was a targeted research sprint, not a systematic review. The absence of a source is not proof that it does not exist.

---

## 2. Stream A — Buffalo Pound provenance

### 2.1 Dataset identity

**Queries / routes:**

- FRDR DOI `10.20383/103.01100`.
- FRDR record page for the buoy dataset.
- Borealis DOI `10.5683/SP3/MP6NXF`.
- Borealis API record (`/api/datasets/:persistentId/`).
- Local README and `data_flags.csv`.
- *Data in Brief* DOI `10.1016/j.dib.2025.112290`; Europe PMC full text `PMC12720111`.
- Painter et al. 2022 DOI `10.1039/D2EM00078D`; Crossref metadata; ESS Open Archive DOI `10.1002/essoar.10510183.2`.

**Found:**

- The buoy dataset and the biological dataset are separate deposits with different DOIs, authors, licences and periods.
- The buoy dataset is CC BY 4.0, 2014–2021, 10-minute data (15-minute in 2014), YSI 6600/6025/6131, 0.82 m and 2.83 m sensors.
- The biological dataset is CC BY-NC-SA 4.0, 2018–2019, microscopy at 0.8 m.
- The *Data in Brief* paper documents the buoy, B7 and calibration; it does not document the biological dataset.
- The 2022 paper documents the bloom ecology; its full text was not accessible.

**Inaccessible:**

- RSC article landing/PDF: HTTP 403.
- ESSOAr/Authorea PDF: returned HTML challenge pages.
- FRDR newer-version record `cbf4ec95-...`: HTTP 404.
- Some FRDR files were not directly downloadable; local copies were used.

**Consequence:** provenance is resolved at the dataset level but not at the record level. The exact biomass derivation, duplicate/`REP` semantics, B7 retention, negative/above-range RFU, coverage and time zone remain custodian questions.

### 2.2 Duplicate and REP structure

**Route:** local structural inspection of `BP_PhytoTax_2018_KP.csv` and `BP_PhytoTax_2019_KP.csv`.

**Found:**

- 2018: 817 rows, 25 dates, 19 duplicate date–species groups (19 extra rows).
- 2019: 405 rows, 17 dates, 2 duplicate groups (2 extra rows).
- 2019 `REP1`: 12 dates/294 rows; `REP2`: 5 dates/111 rows; disjoint dates.
- 2019-07-17: all `REP2`.

**Not done:** no biological totals, no correlations, no event labels. This was a structural provenance check, not the prohibited count-only audit.

### 2.3 Biomass arithmetic

**Route:** deterministic arithmetic check on example rows; prior 4L.14 all-row ratio check.

**Found:** example rows are consistent with `Cell_Volume_um3 × Cell_Density_L × 10^-6` and a density of 1 g cm⁻³. This is arithmetic consistency, not provider confirmation.

### 2.4 B7 and calibration

**Route:** *Data in Brief* full text (PMC).

**Found:**

- B7 = entire interval between the last maintenance visit and the visit where fouling was identified; a caution interval, not a removal flag.
- Pigment sensors calibrated at start/end of seasons with a two-point rhodamine standard; drift reported minimal; no per-record coefficients.
- Negative PAR is documented; negative pigment RFU is not.

**Consequence:** B7 automatic exclusion is not supported. Negative/above-range RFU still require the custodian.

### 2.5 Sample times

**Route:** local inspection of `BP_YSI_2018.tab` and `BP_YSI_2019.tab` (profile casts).

**Found:** profile dates overlap 19/25 biological dates in 2018 and 16/17 in 2019; times ~10:20–13:33. These are likely visit times, but the phytoplankton sample time is not documented.

**Consequence:** the “no sample times” statement is too strong for Buffalo Pound; label as inferred.

---

## 3. Stream B — coverage and time zone

**Routes:** README, *Data in Brief*, 4L.17 D-06 assessment, local file structure.

**Found:**

- 10-minute cadence from 2015; 15-minute in 2014.
- Daily counts vary 121–144 (2018) and 42–131 (2019).
- No time-zone statement.
- No date-specific expected cadence.
- Fixed 72/144 rule withdrawn.

**Not found:** partial-day handling, outage log, date-boundary convention.

---

## 4. Stream C — custodian identification

**Routes:**

- FRDR record/author list.
- Borealis record/contacts.
- *Data in Brief* author list.
- USask SENS profile (Helen Baulch).
- USask GIWS profile (Katy Nugent).
- USask SENS adjunct profile (Kristin Painter).
- WLU profile (Jason Venkiteswaran).
- ORCID records.

**Found:**

- Helen Baulch: Professor, USask SENS; PI contact; `helen.baulch@usask.ca`.
- Katy Nugent: GIWS lab manager/field technician; `katy.nugent@usask.ca`.
- Kristin Painter: Adjunct Professor, USask; ECCC; `kristin.painter@ec.gc.ca`.
- Jason Venkiteswaran: Associate Professor, WLU; `jvenkiteswaran@wlu.ca`.
- Lisa Boyer and Jay Bauer are co-authors; current roles/custodianship not verified.

**Distinction:** creator/corresponding author/current custodian are not the same. No one has confirmed current custody in this sprint. The recommended route is Baulch (accountable PI), cc Nugent and Painter.

---

## 5. Stream D/E — reviewer candidates

### 5.1 Method

- OpenAlex author search to identify current affiliations and top works.
- ORCID public records for employments and some public emails.
- Official institutional profiles for role, profile URL and email.
- Crossref for publication titles, authors, journals and DOIs.
- Targeted checks for current affiliation changes (e.g., Carvalho CEH→NIVA; Simpson Regina→Aarhus; Killick Lancaster→Clemson).

### 5.2 Scientific candidates found

- Cayelan Carey (Virginia Tech) — verified email.
- Laurence Carvalho (NIVA) — verified email.
- Hans Paerl (UNC) — verified email.
- Petra Visser (UvA) — verified email.
- Meryem Beklioğlu (METU) — ORCID, no public email verified.
- Beatrix Beisner (UQAM) — ORCID, no public email verified.
- Bas Ibelings (UNIGE) — ORCID, no public email verified.

### 5.3 Statistical candidates found

- Mark Scheuerell (USGS/UW) — verified email via ORCID.
- E. Eli Holmes (NOAA/UW) — verified email via professional site.
- David Warton (UNSW) — verified email.
- Gavin Simpson (Aarhus/Regina adjunct) — public professional email; institutional email not verified.
- Peter Guttorp (NR; former UW professor) — verified email.
- Christopher Wikle (Missouri) — verified email.

### 5.4 Inaccessible / problematic

- USGS staff profile for Scheuerell: timed out/0 bytes; identity verified via ORCID.
- UNIGE profile for Ibelings: security check; no email.
- Griffith experts page for David Hamilton: returned a JS/empty page; Hamilton was not shortlisted.
- Some institutional directory pages returned “page not found” or security checks.
- Web search engines produced irrelevant results for some queries (e.g., “IGB” interpreted as the Irish Greyhound Board); official sites and APIs were used instead.
- Crossref returned HTTP 429 after repeated queries; searches were paused and reduced.

**Consequence:** the shortlist uses verified identities and contact routes. No email was guessed. Candidates without a verified email are marked “institutional route only.”

---

## 6. Stream F — review design

**Routes:** project evidence packages; SciFest rules; general review-design reasoning.

**Found:** no existing independent review process for this project. The protocol in `INDEPENDENT_REVIEW_PROTOCOL.md` was created for this sprint. It defines independence, disclosure, materials, outcomes, reconciliation and reserved decisions.

---

## 7. Stream G — Stage 1 viability and originality

### 7.1 Prior art

**Routes:** Crossref bibliographic queries, OpenAlex works, known literature, project 4L.14 prior-art review.

**Found:**

- Brient et al. 2008 — PC probe evaluation.
- Loisa et al. 2015 — PC fluorescence to absolute biomass, with site-specific calibration.
- Kong et al. 2013 — online PC probe in a reservoir.
- Hodges et al. 2017 — manufacturer/temperature/morphology effects on PC fluorescence.
- Painter et al. 2022 — Buffalo Pound autumn Planktothrix bloom not detected by sensor/lab chlorophyll.

**Conclusion:** low–moderate originality; the core association method is established. The modest contribution is the pre-specified non-equivalence audit and negative-result framing.

### 7.2 Mendota prior art

A targeted search did not identify an exact same-date Spearman audit for Mendota. This is **not** proof of novelty; the dataset is widely used and the search was not exhaustive.

### 7.3 Viability

Assessed four outcomes (A–D). Conclusion: Outcome C in strict form (Mendota core, Buffalo Pound conditional appendix) is the most defensible; Outcome B (Mendota-only) is the fallback; Outcome D (pause) if custodian/reviewer conditions fail.

---

## 8. Stream H — Müggelsee Stage 2

**Routes:**

- FRED 867 package page.
- FRED 867 metadata PDF.
- FRED 1 package page.
- FRED 1 metadata PDF.
- FRED 1145 package page.
- FRED 1145 EML.
- IGB FRED site.

**Found:**

- FRED 867: phytoplankton 1979–ongoing, weekly/biweekly, Utermöhl, biomass/biovolume, all rights reserved, contact Hilt.
- FRED 1: weekly multiparameter probe 1978–2019, chl a and phycocyanin, all rights reserved, contact Hilt.
- FRED 1145: high-frequency station 2001–ongoing, 5-min nominal, 1.5 m, chl a and phycocyanin, all rights reserved, contact Shatwell.
- Sensor station M210 vs phytoplankton stations M3/M5/M7/M8/M10; depth 1.5 m vs integrated samples.
- No public event definition, event count, calibration/QC record or permission.

**Inaccessible:**

- FRED data files (access restricted).
- Some FRED pages had large embedded images; text was extracted after stripping images.

**Consequence:** Müggelsee is a candidate, not qualified. Stage 2 threshold should be strengthened.

---

## 9. Competition and licence

**Routes:**

- SciFest@College 2027 entry page.
- Provisional 2027 student rules PDF.
- CC BY 4.0 and CC BY-NC-SA 4.0 licence records.

**Found:**

- Eligibility: born after 1 May 2008; second-level in Ireland/NI; one project; individual/group max 3.
- Report book + visual display; plagiarism prohibited; external supervision acknowledged; media release.
- No public judging rubric.
- Two datasets have different licences; no automatic educational exception.
- D-14 remains outstanding.

---

## 10. Inaccessible sources and limitations

| Source | Problem | Effect |
|---|---|---|
| RSC article (Painter 2022) | HTTP 403 | Full methods not inspected; used abstract, dataset README, Crossref metadata |
| ESSOAr/Authorea PDF | HTML challenge | Preprint not fully read |
| FRDR newer-version record | HTTP 404 | Version ambiguity unresolved |
| USGS Scheuerell profile | Timeout/0 bytes | Identity verified via ORCID |
| UNIGE Ibelings profile | Security check | No verified email |
| Griffith Hamilton profile | JS/empty page | Hamilton not shortlisted |
| Some university directories | 404/security | Used ORCID/official profiles instead |
| Crossref API | HTTP 429 | Reduced query volume; waited/paused |
| Web search engines | Irrelevant results for “IGB” etc. | Used official sites/APIs |
| FRED data files | Access restricted | Metadata only; no data inspection |
| SciFest judging rubric | Not public | Did not invent criteria |

**Search stop rule:** stop when the defined source categories have been covered, the key claims have at least one primary/official source, and remaining gaps are explicitly custodian/access dependent. Do not stop merely because a preferred answer was found.

---

## 11. What was not done

- No external contact, email, reviewer invitation or custodian enquiry was sent in this sprint. (The earlier Müggelsee enquiry remains the only external message recorded in the project.)
- No data were acquired or uploaded.
- No analysis, count audit, correlation, model, label, event interval or derived dataset was produced.
- No Git commit or push.
- No claim that a reviewer accepted or a custodian replied.
- No claim that Müggelsee is qualified.

---

## 12. Search verdict

The search is **sufficient to support the package’s conclusions**:

- the two Buffalo Pound datasets are separate and their key provenance gaps are identified;
- the custodian route is verified;
- reviewer candidates are identified with current affiliations and contact routes;
- the prior art is sufficient to conclude low–moderate originality;
- the Müggelsee resources are sufficient to conclude “candidate, not qualified”;
- the competition/licence issues are identified but unresolved.

The search is **not sufficient** to answer the custodian-only questions or to qualify Stage 2. Those require external responses and written permission.
