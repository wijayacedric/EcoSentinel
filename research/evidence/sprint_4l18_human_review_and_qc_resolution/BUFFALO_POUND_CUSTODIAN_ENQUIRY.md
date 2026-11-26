# Buffalo Pound Custodian Enquiry

**Status:** Draft only — **NOT SENT**  
**Prepared:** 2026-11-25  
**Purpose:** Clarify data-field semantics and QC documentation in the Buffalo Pound Lake buoy dataset.  
**No contact has been made in this sprint.**

---

## Recipient

**Dr Helen Baulch**  
University of Saskatchewan  
Corresponding author of the Buffalo Pound Lake dataset paper (Baulch et al. 2025, *Data in Brief* 63:112290).  
Published corresponding email: `helen.baulch@usask.ca` (as listed in the PMC article).

No cc or additional recipients are asserted. The dataset authors include K. Painter, L. Boyer, K. Nugent, J. Bauer, L. Vuleta, J. Venkiteswaran and C. Whitfield; the appropriate data custodian may be one of these.

---

## Subject

**Clarification of Buffalo Pound buoy data fields and QC flags (FRDR DOI 10.20383/103.01100)**

---

## Draft email

Dear Dr Baulch,

I am a secondary-school student in Ireland developing an independent freshwater ecology research project, EcoSentinel. I am using the public Buffalo Pound Lake buoy dataset (FRDR DOI 10.20383/103.01100; Baulch et al. 2025) to understand how surface sensor fluorescence compares with independent microscopy-based cyanobacteria biomass.

I am writing to ask for clarification of a few data-field and quality-control details, so that I use the dataset accurately. I am not asking you to endorse the project or its conclusions, and I am not asking for any analysis. I would be grateful for documentary clarification of the points below.

**Essential questions**

1. **Duplicate date–species rows.** In the 2018 phytoplankton files, some date–species combinations have two rows without a replicate identifier; in 2019, `REP1`/`REP2` occur on disjoint dates. Do these rows represent technical replicates, split samples, separate subsamples, or distinct records? What is the intended date-level aggregation?
2. **Biomass derivation.** How was `Biomass_mg_m3` calculated from `Cell_Volume_um3` and `Cell_Density_L`? What density assumption and conversion factor were used, and is the field directly derived from the published methods?
3. **QC flags.** Please confirm the intended meaning and recommended handling of `M`, `C`, `B7`, and any other flags that may appear in the 2018–2019 pigment or turbidity columns. In particular, does `B7` mean “discard,” or “caution/interrogate”?
4. **YSI operating range.** The YSI 6025/6131 sensors are documented as 0–100 RFU. Should values above 100 RFU be treated as saturated/out-of-range, and how were they handled in the cleaned files?
5. **Negative RFU.** Are negative chlorophyll/phycocyanin RFU values valid baseline/zero-offset readings, or should they be treated as invalid? Is there a documented blank/zero convention?
6. **Daily coverage and timestamps.** What is the expected 10-minute record count per deployment day, and how should partial days be handled? What time zone and timestamp convention does `DateTime` use? The README gives the format but no time-zone statement.
7. **Calibration/maintenance records.** Are deployment-level calibration, maintenance, fouling and instrument-change records available (including the 2018–2019 shallow sonde)? The data paper describes the practice; I am asking whether record-level documentation exists.

**Supplementary questions**

8. Are detection limits or accuracy values available for the 2018–2019 chlorophyll and phycocyanin channels?
9. Is there a data dictionary or schema note for the 2018 and 2019 biological files, including sample identifiers?
10. Are there field notes or provenance details for the 2019-07-17 low-biomass microscopy record?
11. Are there any corrections or version notes beyond the published dataset?

I would be happy to receive a short written answer or to be directed to the appropriate co-author or data manager. If some of these questions are already answered in a document I have missed, a pointer would be very helpful.

Thank you for your time and for making the dataset available.

Kind regards,

Cedric Wijaya  
EcoSentinel — independent student research project

---

## Send status

- **Not sent.**
- No email account or draft was created in this sprint.
- No follow-up or external contact was initiated.
- The enquiry is prepared for later human review and authorisation.

---

## Notes on scope

- The enquiry does **not** ask the custodian to validate the research hypothesis.
- It does **not** ask for unpublished data beyond documentation needed to interpret the public dataset.
- It distinguishes essential field/QC questions from supplementary documentation.
- It does not assume that any answer will be favourable or that access will be granted.
