# Buffalo Pound — Final Custodian Email

**Status:** Final draft. **NOT SENT.** No contact has been made.  
**Prepared:** 2026-11-25  
**Purpose:** Obtain written clarification of the two Buffalo Pound datasets used by the proposed P3/P4 estimands.

---

## 1. Verified routing

| Field | Value | Evidence |
|---|---|---|
| **To** | Professor Helen Baulch, School of Environment and Sustainability, University of Saskatchewan — `helen.baulch@usask.ca` | USask faculty profile (official); FRDR dataset PI contact; *Data in Brief* first author |
| **Cc** | Katy Nugent, Global Institute for Water Security, University of Saskatchewan — `katy.nugent@usask.ca` | USask GIWS profile (official); dataset co-investigator; lab manager/field technician |
| **Cc** | Dr Kristin Painter, School of Environment and Sustainability, University of Saskatchewan / Environment and Climate Change Canada — `kristin.painter@ec.gc.ca` | USask adjunct profile (official); Borealis dataset contact; 2022 paper corresponding author |
| **Subject** | Clarification of Buffalo Pound Lake buoy and phytoplankton datasets (2018–2019) | — |
| **Attachment** | `BUFFALO_POUND_UNRESOLVED_QUESTIONS.csv` (one-page question sheet) | Prepared in this package |

**Why this routing:** Helen Baulch is the accountable PI listed in the buoy dataset metadata. Katy Nugent is the operational co-investigator and laboratory manager most likely to hold instrument/QC records. Kristin Painter is the corresponding author and dataset contact for the microscopy data. Copying all three avoids asking one person to answer questions about a dataset they may not manage. If the project owner prefers a single recipient, send to Professor Baulch and retain the two copies.

**Do not add** Dr Jason Venkiteswaran unless the project owner specifically wants the repository contact copied; he is a co-author and Borealis contact, but the technical questions are primarily for the PI, data manager and biological lead.

---

## 2. Email body

Dear Professor Baulch,

I am writing from the EcoSentinel research project, an independent secondary-school study of whether surface chlorophyll and phycocyanin fluorescence track independent microscopy-derived cyanobacteria abundance in lakes. We are using only publicly available data and are not requesting new measurements or unpublished data. We would be grateful for clarification of the documentation for two Buffalo Pound Lake datasets so that we describe and, if appropriate, analyse them correctly.

The two datasets are:

1. **Buoy data:** Baulch et al. (2025), “A long-term water quality and meteorological data set (2014–2021) of a eutrophic prairie lake: Buffalo Pound Lake, Saskatchewan, Canada”, FRDR, https://doi.org/10.20383/103.01100. We use the shallow chlorophyll (`ChlRFUShallow_RFU`) and phycocyanin (`BGPCShallowRFU_RFU`) fields at 0.8 m.
2. **Microscopy data:** Painter et al. (2022), “Data for: Early and late cyanobacterial bloomers in a shallow, eutrophic lake”, Borealis, https://doi.org/10.5683/SP3/MP6NXF. We use the 2018–2019 taxonomy tables and the supplied `Biomass_mg_m3` field.

Our proposed comparison is a descriptive, same-calendar-date audit. We are not attempting to calibrate the sensors, validate them, predict blooms or estimate absolute agreement. The questions below concern how the supplied files should be interpreted; they are not a request for new analysis.

**Essential questions**

1. **Duplicate date–species rows.** In the 2018 taxonomy table there are 19 date–species groups with two rows in the same `Sample_ID`; in 2019 there are 2 such groups within `REP1`. Are these split counts, separate counting chambers, duplicate entries, or something else? Should they be summed, averaged, or treated as one record?

2. **`REP1`/`REP2`.** In 2019, `REP1` occurs on 12 dates and `REP2` on 5 dates, with no date containing both. What do these labels mean? Are they replicate samples, replacement counts, counting batches, or sample identifiers? Is there a documented aggregation rule?

3. **`Biomass_mg_m3` derivation.** The field is arithmetically consistent with `Cell_Volume_um3 × Cell_Density_L × 10^-6` under a density of 1 g cm^-3. Is that the actual derivation? Is the density assumption 1.0 g cm^-3? Is biomass calculated at taxon level and then summed, and is rounding applied before or after conversion? Were any corrections or transformations applied that are not visible in the supplied columns?

4. **B7.** The 2025 *Data in Brief* paper states that B7 identifies the entire interval between the last maintenance visit and the visit at which fouling was identified. Does B7 mean “caution, retain with flag”, or “invalid, remove”, in the deposited files? Were B7-flagged values retained in the data we downloaded? If retained, should users exclude them from a primary analysis or include them with a flag and test exclusion as a sensitivity?

5. **Negative chlorophyll/phycocyanin RFU.** Do negative RFU values occur in the shallow pigment fields? If so, what do they represent — baseline/zero offset, instrument noise, invalid data, or something else? How should they be treated?

6. **Values above 100 RFU.** The 6025/6131 sensors are documented as 0–100 RFU. Do values above 100 occur in the deposited data? If so, are they saturation, clipping, extrapolation, a different configuration, or a processing artefact? How were they handled?

7. **Coverage, timestamps and time zone.** What was the expected 10-minute cadence on each date, and which dates have known outages or partial-day deployment? Are the `DateTime` values local standard time (CST), UTC, or logger time? How should dates be assigned when a deployment crosses midnight?

8. **Phytoplankton sample times.** The 2018/2019 `BP_YSI` profile casts carry times of roughly 10:20–13:33 on most biological sampling dates. Were those casts collected during the same visit as the phytoplankton sample? Can you confirm the phytoplankton sample time, or state that it is not recorded?

**Supplementary questions**

9. Are calibration and maintenance records available per deployment or per date (pigment two-point rhodamine calibration, pre/post-maintenance values, drift assessments)? If not, is there a summary table?

10. Can you confirm the exact sensor configuration in 2018–2019 (models, serial numbers, firmware, wiping, depth) and whether it changed between the two seasons?

11. Were any values changed between the 2022 biological deposit and the 2025 buoy deposit? The FRDR record notes that it is a previous version of a newer record; can you confirm which version is current?

12. Are there any known corrections, errata or processing notes for either dataset that are not in the README or the data paper?

I have attached a one-page CSV containing the same questions so that they can be answered directly if that is easier. A short written response, even to a subset, would be extremely helpful. We will cite both datasets and their papers in any report and will not redistribute the data.

Thank you for considering this request.

Kind regards,

EcoSentinel Research Project  
Independent secondary-school research project

---

## 3. Attachment rationale

| Attachment | Why it is useful | What it contains |
|---|---|---|
| `BUFFALO_POUND_UNRESOLVED_QUESTIONS.csv` | Lets the custodian answer in a structured way without rewriting the email; keeps the request to one page | Question ID, theme, question, why it matters, decision affected, priority |

Do **not** attach the full provenance report or the raw data. The report is long and contains project-internal reasoning; the raw data are already public and do not need to be sent back.

---

## 4. Sending checklist

- [ ] Project owner has authorised external contact.
- [ ] Recipient addresses re-checked against the official profiles on the day of sending.
- [ ] Subject line unchanged.
- [ ] Attachment present and opens correctly.
- [ ] No raw data, no unpublished project documents, no personal information beyond the sender’s own contact details.
- [ ] Send from the project owner’s professional/student email account, not an automated account.
- [ ] Record the send date, recipients, subject and message ID in the project correspondence log.
- [ ] Do **not** send a follow-up before a reasonable response period (suggested: 15 working days).

**Status: NOT SENT.**
