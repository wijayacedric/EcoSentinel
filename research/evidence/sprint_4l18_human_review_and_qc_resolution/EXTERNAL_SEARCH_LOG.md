# External Search Log — Sprint 4L.18

**Date:** 2026-11-25  
**Scope:** D-05 QC evidence resolution; D-06 dependency reconciliation; D-14 licence/competition verification.  
**Standard:** Primary documentation first. No broad dataset discovery. No contact.

---

## 1. Source categories

1. Repository decision/protocol records.
2. Mendota NTL-LTER EML and 4L.9 audit tables.
3. Buffalo Pound README, data flags, and Data in Brief data paper.
4. YSI 6025/6131 manufacturer documentation and 6-Series manual.
5. USGS algal-fluorescence methods guidance.
6. Turner Cyclops documentation (Mendota context).
7. Creative Commons and SciFest official terms.
8. Existing Gmail/Müggelsee verification.

---

## 2. Mendota searches

| Action | Result |
|---|---|
| Read `metadata_129.42.xml` flag blocks | C = sensor off; E = noisy/malfunctioning (variable-specific); H = outside standard range; G = suspected biofouling (YSI chl/PC, PAR below); O absent/undefined |
| Read 4L.9 `QC_FLAG_AUDIT.md` | C can carry numeric values; H common and undefined numerically; G era-specific; eight columns have undocumented flag values; O appears once in spec cond |
| Read 4L.9 `QC_FLAG_DISTRIBUTIONS.csv` / `FLAGGED_VALUE_DISTRIBUTIONS.csv` | Flag counts and value distributions; no new counts calculated |
| Read 4L.9 `ANOMALY_AUDIT.csv` | Negative RFU/turbidity/PAR values exist; some flagged H/C, some unflagged |
| Search for numeric H range in EML | None found |
| Search for per-record calibration/coefficients | None found |

**Conclusion:** definitions are documented, but numeric bounds and some applicability remain unresolved.

---

## 3. Buffalo Pound searches

| Action | Result |
|---|---|
| Read `README.txt` | 68 variables; 10/15-min cadence; sensor models; calibration prior to deployment; no time-zone statement |
| Read `data_flags.csv` | M missing; C faulty/unrealistic; A2–A6/B6; B7 = spike plus decrease after site visit |
| Read Baulch et al. 2025 (PMC12720111) | Table 7: YSI 6025/6131, 0–100 RFU; B7 interval = between maintenance visits; calibration/maintenance practice; data screening |
| Search for time-zone statement | None in README/data paper; `DateTime` has no suffix |
| Search for B7 handling recommendation | Data paper says likely fouling/caution; not a removal instruction |
| Search for negative RFU guidance | None found in dataset documentation |

**Conclusion:** B7 is a caution interval; 0–100 RFU is a documented full-scale range; negative RFU and coverage/time zone need custodian clarification.

---

## 4. Instrument documentation

| Source | Result |
|---|---|
| YSI 6025 spec sheet | ~0–400 µg/L; 0–100 RFU; detection limit ~0.1 µg/L |
| YSI 6-Series manual Rev J | 6025 0–100 RFU; 6131 0–100 RFU; 6131 accuracy not specified; detection limit ~220 cells/mL; 1-point calibration zeros fluorescence |
| YSI 6131 reseller spec | 0–100 RFU; ~220 cells/mL |
| USGS TM 1-D10 | RFU is 0–100% of operating range; fluorescence is a proxy; quenching/interferences; validation needed |
| Turner Cyclops-7F docs | Optical ranges stated in µg/L/ppb; gain/range context; no single universal RFU upper bound |

**Conclusion:** 0–100 RFU is a genuine full-scale range for the Buffalo Pound YSI sensors. It is not a concentration threshold or bloom threshold. Mendota Turner RFU upper bound cannot be inferred from the EML.

---

## 5. Licence/competition checks

| Source | Result |
|---|---|
| CC BY-NC-SA 4.0 legal code | Attribution, non-commercial, share-alike for Adapted Material; Share includes public display/dissemination; database rights |
| SciFest 2027 rules | Report book/display; project content may be used by SciFest for exhibition/publication |
| SciFest terms | Website content restrictions; not a determination of student-project licence |

**Conclusion:** D-14 still requires a written licence/competition review; no automatic educational exception assumed.

---

## 6. Unsuccessful / blocked searches

- No custodian response or written data dictionary.
- No numeric H range for Mendota.
- No definition of O.
- No time-zone statement for Buffalo Pound.
- No B7 overlap counts (would require authorised count audit).
- No per-record calibration coefficients.
- No independent reviewer appointment or response.
- No Müggelsee reply.

These are recorded in `MISSING_EVIDENCE_REGISTER.csv`.

---

## 7. Stopping point

The search stopped when:

1. All D-05 proposed rules had been matched to primary documentation or marked unresolved.
2. Mendota and Buffalo Pound flag meanings were distinguished by instrument/context.
3. 0–100 RFU was verified as a manufacturer full-scale range.
4. B7 was verified as a caution interval, not a removal flag.
5. D-06 dependency on D-05 and coverage evidence was confirmed.
6. D-14 licence/competition texts were checked.

No further search can resolve items that require the custodian, a count audit, a named reviewer, or a licence authority.

**No analysis, count audit, data acquisition, email, or external contact was performed.**
