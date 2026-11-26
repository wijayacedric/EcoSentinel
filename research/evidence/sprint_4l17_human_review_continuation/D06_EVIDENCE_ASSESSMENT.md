# D-06 Evidence Assessment — Primary Daily Summary

**Decision:** D-06 — Primary daily summary  
**Original wording:** (a) full-day mean for both lakes; (b) nighttime for BP only; (c) daytime for both  
**Current status:** **OUTSTANDING — NOT APPROVED**  
**Project-owner preference:** **Provisional Option A only** — full-day means for both lakes, with Buffalo Pound daytime/nighttime medians as sensitivity and an explicit non-equivalence statement.  
**Formal approval:** **None.** Independent scientific and statistical sign-off is still required.

---

## 1. The options

| Option | Definition | Immediate problem |
|---|---|---|
| **A** | Full-day mean for both lakes | The two daily means are built from different within-day coverage and instruments; they are not equivalent exposures |
| **B** | Nighttime summary for Buffalo Pound only | Not comparable to Mendota full-day means; introduces a different statistic and exposure for one lake |
| **C** | Daytime summary for both lakes | Mendota’s provider daily mean has no documented within-day counts; a daytime mean cannot be reconstructed from the current package |

---

## 2. Evidence for and against Option A

### 2.1 Mendota

**Verified:**

- The daily sensor file contains provider daily averages of 1-minute data.
- The file does **not** contain within-day observation counts or a documented within-day completeness measure.
- The biology record has **dates, not sampling times**.
- Turner chlorophyll has 128 same-day unflagged values; Turner phycocyanin 139; YSI chlorophyll 21; YSI phycocyanin 22.
- Mendota biology is generally a **0–8 m composite**; sensors are at **0.5 m** (pCO2 1 m; PAR 1–2 m).
- Diel quenching can reduce chlorophyll and phycocyanin signals; the exact sampling time is unknown.

**Supports Option A:** It is the only daily summary available for Mendota without reconstructing raw within-day data. It is a consistent, provider-defined statistic across the Mendota record.

**Argues against:** The daily mean’s within-day coverage and representativeness are unknown. It cannot be shown to represent the microscopy sample time or the 0–8 m composite. A full-day mean may average across diel cycles and quenching.

### 2.2 Buffalo Pound

**Verified:**

- Sensors are 10-minute records (15-minute in 2014).
- Biological dates: 25 in 2018, 17 in 2019.
- Daily record counts: 121–144 in 2018; 42–131 in 2019.
- The fixed “≥72 of 144 and both halves” coverage rule has been **withdrawn** in the 4L.14 addendum because 144 is not a documented date-specific expectation.
- B7 fouling intervals, negative/above-range RFU, and instrument/calibration issues remain unresolved.
- The raw 10-minute data allow daytime/nighttime medians **in principle**, but only where within-day coverage is adequate and the time zone is documented.

**Supports Option A:** A full-day mean uses all valid records and is the closest available analogue to the Mendota provider daily mean. It avoids choosing a nighttime window without evidence.

**Argues against:** A 42-record day and a 144-record day do not represent the same exposure. A 50% day can be mostly one interval. Coverage may correlate with maintenance, fouling, weather, or high biomass. The daily mean may not represent the biological sample day.

### 2.3 Cross-lake comparability

| Feature | Mendota | Buffalo Pound | Consequence |
|---|---|---|---|
| Daily summary | Provider daily mean of 1-minute data | Mean of valid 10-minute records | Different construction |
| Within-day counts | Unknown | Known per date but variable | Different uncertainty |
| Sample time | Unknown | Unknown | No time-of-day alignment |
| Sensor depth | 0.5 m | 0.82 m | Similar shallow point, not identical |
| Biology depth | 0–8 m composite | 0.8 m point | Depth mismatch at Mendota |
| Instruments | Turner / YSI | YSI 6600 | Different sensors and eras |
| Missingness | Variable by year/variable | Variable by date/year | Different selection |

**Conclusion:** The same label “daily mean” does **not** mean the same exposure, precision, or biological support. Option A is a common descriptive statistic, not a common measurement.

---

## 3. Evidence for and against Options B and C

### Option B — nighttime Buffalo Pound only

**Potential advantage:** Reduces daytime quenching and may better match a stable dark-period signal.

**Problems:**

- Mendota has no nighttime reconstruction, so the lakes would use different statistics.
- The biological samples have no sampling times; there is no evidence they were collected at night.
- Buffalo Pound nighttime coverage may be worse than full-day coverage.
- A nighttime-only summary would introduce a lake-specific exposure difference that the design cannot interpret.
- No current evidence shows nighttime is more representative of the microscopy sample.

**Assessment:** Not defensible as a primary summary. At most a sensitivity, and only if coverage supports it.

### Option C — daytime both lakes

**Potential advantage:** Better match to daytime sampling and reduce nighttime baseline effects.

**Problems:**

- Mendota’s provider daily mean cannot be decomposed into daytime without raw within-day data or documented counts.
- Buffalo Pound daytime can be computed, but Mendota cannot; the comparison would be asymmetric.
- “Daytime” is not defined in the current documentation (fixed hours? sunrise/sunset?).
- No sample times exist to justify a particular window.

**Assessment:** Not currently implementable for both lakes. Reject as a primary option.

---

## 4. Recommendation

### Provisional project-owner preference: **Option A**

Retain full-day means for both lakes as the proposed primary daily summaries, subject to independent scientific and statistical review, because:

1. It is the only daily summary available for Mendota without new within-day data.
2. It avoids inventing a nighttime/daytime window unsupported by sample times.
3. It can be paired with Buffalo Pound daytime/nighttime medians as **sensitivity summaries**, not as alternative primary datasets.
4. It preserves a consistent descriptive statistic while explicitly denying biological equivalence.

**This is a project-owner preference, not D-06 approval.**

### Mandatory qualifications

- The daily summaries are **not equivalent exposures**.
- Neither summary represents the exact biological sample time or the same water parcel.
- Full-day averaging does **not** remove diel variation or quenching.
- Using the same summary statistic does **not** imply biological equivalence.
- Buffalo Pound sensitivity summaries are valid only where date-specific coverage and time zone are documented.
- If coverage cannot be documented, affected Buffalo Pound dates are excluded from primary analysis; the study does not substitute a nighttime mean to rescue them.

### Proposed protocol wording

> **Primary daily summary (proposed).** The primary sensor exposure is the full-day mean: the provider daily mean for Mendota and the mean of valid 10-minute records for Buffalo Pound. These summaries are not equivalent exposures. Mendota’s within-day coverage is undocumented; Buffalo Pound’s within-day coverage varies by date. Neither summary represents the biological sample time or the same water parcel. Buffalo Pound daytime and nighttime medians are reported as sensitivity summaries only where date-specific coverage and time zone are documented; they are not alternative primary datasets. No claim of biological equivalence, quenching removal, or exact temporal alignment is permitted.

---

## 5. What would change the recommendation

Option A would become **unsupported** if:

- the data custodian cannot document Buffalo Pound date-specific coverage;
- the independent statistical reviewer concludes that a full-day mean is not a meaningful date-level exposure;
- the independent scientific reviewer concludes that the Mendota provider mean is too unrepresentative to compare;
- the daytime/nighttime sensitivity cannot be computed with adequate coverage;
- the daily means select dates non-randomly by season, maintenance, or fouling.

In that case, the most defensible alternative is **not** Option B or C. It is:

- restrict Buffalo Pound to dates with documented adequate coverage;
- retain Mendota’s provider mean only as a descriptive date-level exposure;
- report points/n and no pooled daily-mean claim if representativeness fails;
- exclude the affected lake/estimand rather than switch to an unvalidated window.

---

## 6. Required sign-offs

| Sign-off | What they must confirm |
|---|---|
| Independent scientific reviewer | The daily-mean interpretation is biologically defensible with the stated limitations |
| Independent statistical reviewer | The full-day mean is a defensible date-level summary; sensitivity summaries are not over-interpreted |
| Data custodian | Buffalo Pound date-specific cadence/coverage and time zone; Mendota within-day coverage if available |

**D-06 remains OUTSTANDING — NOT APPROVED until these are recorded.**
