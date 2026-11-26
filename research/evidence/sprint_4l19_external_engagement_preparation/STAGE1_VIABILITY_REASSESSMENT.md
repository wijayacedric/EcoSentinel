# Stage 1 Viability Reassessment

**Sprint:** 4L.19  
**Date:** 2026-11-25  
**Question:** Is the narrowed Stage 1 measurement audit viable after the 4L.18 QC findings and the 4L.19 provenance, reviewer and Stage 2 evidence?  
**Status:** Assessment only. **No decision approved. No analysis authorised.**

---

## 1. Executive conclusion

**Stage 1 remains conditionally viable — but not in its current protocol form.**

The design is viable as a modest, exploratory **measurement-comparability audit** if:

1. the Buffalo Pound custodian resolves the duplicate/`REP`, biomass, B7, negative/above-range RFU, coverage and time-zone questions;
2. the protocol’s QC section is formally revised to match the D-05 evidence (the current text still contains rules that the evidence no longer supports);
3. independent scientific and statistical reviewers accept the depth mismatch, the detection-conditioned population and the descriptive-only claims;
4. the licence/competition review is completed;
5. D-15 is explicitly approved after the count audit and all prior decisions.

The design is **not** viable as a validation, calibration, agreement, prediction, bloom-detection or early-warning study. It is also not viable if the custodian cannot document enough of the Buffalo Pound provenance to make P3/P4 interpretable.

The current recommendation is:

> **Retain P1/P2 (Mendota) as the defensible core; retain P3/P4 only as conditional exploratory appendices if custodian evidence arrives; do not analyse any estimand until D-15 is approved.**

This is a **reduced two-lake design** (Outcome C) in a strict form, with a Mendota-only fallback (Outcome B) if Buffalo Pound remains unresolved. It is not “all four estimands as equal-status primary estimates” (Outcome A), and it is not a pause of the research direction (Outcome D) unless the conditions below fail.

---

## 2. What changed since 4L.18

The 4L.18 conclusion was “conditionally yes — as a modest exploratory measurement/comparability audit.” The 4L.19 work sharpens that conclusion in five ways.

### 2.1 The protocol is internally inconsistent with the QC evidence

The current `REVISED_PROTOCOL.md` §10 still says:

- Mendota `H`: retain primary if numeric;
- Buffalo Pound `B7`: exclude primary;
- negative RFU: retain primary as observed;
- >100 RFU: retain primary with flag;
- coverage: ≥50% of expected 10-minute values and both halves of the day.

The 4L.18 D-05 report found:

- `H` has no documented numeric range; retaining it as valid is unsupported;
- `B7` is a caution interval, not a removal flag; automatic exclusion is unsupported;
- negative RFU has no documented biological meaning; retaining it as a valid signal is unsupported;
- >100 RFU is outside the documented full scale; it cannot be assumed quantitative;
- the fixed 72/144 coverage rule is unsupported, and no date-specific expectation is documented.

**Consequence:** the protocol cannot be approved as written. It must be revised before any analysis. This is a documentary inconsistency, not a reason to change the governance status by stealth. The protocol remains **PROPOSED — NOT APPROVED**.

### 2.2 Buffalo Pound is two datasets, not one

The sensor variables and the biological endpoint come from separate repositories with different licences and QC systems. The biomass field is arithmetically consistent with a volume-derived formula, but the provider’s derivation is not documented. Duplicate rows and `REP1`/`REP2` remain unexplained. B7 is a period-level caution interval. Negative and >100 RFU remain unresolved.

**Consequence:** P3/P4 are weaker than the earlier protocol implied. They should not be equal-status primary estimands until the custodian answers.

### 2.3 Buffalo Pound sample times are partially recoverable

The `BP_YSI` profile casts overlap 19/25 biological dates in 2018 and 16/17 in 2019, with times around 10:20–13:33. These are likely visit times, not confirmed phytoplankton sample times.

**Consequence:** the statement “biology has dates, not sampling times” is too strong for Buffalo Pound. A daytime sensitivity is better justified than before. It does not make a full-day mean equivalent to the sample moment, and it does not resolve Mendota’s missing sample times.

### 2.4 Stage 2 is more plausible, but not qualified

The Müggelsee evidence is stronger than a bare “potential lead”:

- FRED 867: phytoplankton biomass/biovolume, 1979–ongoing, weekly growing season / biweekly ice, integrated samples, Utermöhl microscopy, documented biomass conversion, taxonomic resolution changes.
- FRED 1: weekly multiparameter probe, 1978–2019, including chlorophyll a and phycocyanin, but the series ends in 2019.
- FRED 1145: high-frequency multiparameter probe at 1.5 m, 2001–ongoing, 5-minute nominal interval, hourly gaps before 2013, winter hourly data, chlorophyll a and phycocyanin.

But access is “all rights reserved”, the sensor station is not the same as the phytoplankton sampling stations, the sensor depth is 1.5 m versus integrated 0–4/0–7 m samples, and calibration/QC/event definitions are not publicly verified.

**Consequence:** Stage 2 remains a conditional ambition, not a secured path. It does not rescue Stage 1; it is a separate stage.

### 2.5 Prior art is more directly relevant than the protocol acknowledges

The basic association between phycocyanin fluorescence and cyanobacteria biomass has been studied repeatedly. Examples:

- Brient et al. (2008), “A phycocyanin probe as a tool for monitoring cyanobacteria in freshwater bodies”, `10.1039/b714238b`.
- Loisa et al. (2015), “From phycocyanin fluorescence to absolute cyanobacteria biomass”, `10.2166/wpt.2015.083` — PC fluorescence correlated with microscopy biomass in two Finnish lakes, with site-specific post-calibration.
- Hodges et al. (2017), “Sensor manufacturer, temperature, and cyanobacteria morphology affect phycocyanin fluorescence measurements”, `10.1007/s11356-017-0473-5`.
- Painter et al. (2022), Buffalo Pound — the autumn *Planktothrix* bloom was not detected by sensor or laboratory chlorophyll.

**Consequence:** the study’s originality is **low to moderate**. Its defensible contribution is a transparent, pre-specified measurement audit with explicit non-equivalence and negative-result acceptance, not a new sensor-validation method.

---

## 3. Outcome A — all four estimands remain viable

### Conditions

For Outcome A, all of the following would need to hold:

1. Buffalo Pound duplicate rows and `REP1`/`REP2` have a documented, defensible aggregation rule.
2. `Biomass_mg_m3` derivation, density and rounding are confirmed by the provider or by an accessible methods text.
3. B7 is confirmed as a caution flag with a documented treatment; the primary population and B7 sensitivity are defensible.
4. Negative RFU and >100 RFU are documented and their treatment is justified.
5. Date-specific coverage, time zone and partial-day handling are documented.
6. The two-season Buffalo Pound series is accepted by the statistical reviewer as capable of supporting a descriptive rho.
7. The Mendota depth mismatch and unknown sample times are accepted as bounded limitations.
8. Independent reviewers accept the four-estimand structure without requiring a reduction.
9. Licence/competition review is complete.

### Assessment

**Not currently met.** Conditions 1–6 depend on custodian evidence that has not been provided. Condition 7 is a reviewer judgement. Condition 8 is unlikely given the prior-art and multiplicity concerns. Condition 9 is unresolved.

**Verdict:** Outcome A is **not defensible now**. It could become defensible only after a full custodian response and favourable reviews. The project should not plan on it.

---

## 4. Outcome B — Mendota-only Stage 1

### What it would be

A single-lake descriptive audit:

> In Lake Mendota (Turner era, 2006–2019), among same-calendar-date co-occurrences, what is the direction and magnitude of the rank association between surface chlorophyll/phycocyanin fluorescence and microscopy-derived cyanobacteria biovolume, and how does it vary descriptively across seasons?

### Strengths

- The Mendota data are better documented than Buffalo Pound: NTL-LTER EML, flag definitions, long record, published data paper.
- The endpoint is a true biovolume (µm³ mL⁻¹), not a derived wet-weight-equivalent biomass.
- The Turner era has meaningful upper-bound n (128 chlorophyll, 139 phycocyanin).
- One lake avoids the cross-lake non-equivalence problem and the Buffalo Pound provenance blocker.
- The study can be completed with a clear, bounded question even if Buffalo Pound never resolves.

### Weaknesses

- **Depth mismatch:** sensor at 0.5 m; biology generally a 0–8 m composite. This is a serious interpretational limitation, not a minor caveat.
- **No sample times:** the daily sensor mean cannot be aligned to the microscopy sample time.
- **Unknown within-day coverage:** the provider daily mean has no documented within-day counts.
- **Detection-conditioned population:** dates with a reported cyanobacteria row may not represent the lake’s full seasonal cycle.
- **Originality:** a single-lake sensor–biovolume association is even less distinctive than the two-lake audit; prior art on fluorescence–biomass associations is substantial.
- **Generalisability:** one lake, one era, one endpoint; no claim beyond a case study.

### Assessment

**Defensible as a fallback, not as the preferred design.** It is scientifically coherent if framed as a bounded case study of surface fluorescence versus integrated biovolume, with explicit non-equivalence and no validation claim. It is not automatically more original or more useful than the two-lake design. It is the right fallback if Buffalo Pound cannot be resolved and the project owner wants to continue rather than pause.

**Verdict:** **Conditionally viable.** It requires the same protocol revision, reviewer acceptance and licence review as the two-lake design.

---

## 5. Outcome C — reduced two-lake descriptive study

### What it would be

- **Core:** P1/P2 (Mendota) as the primary descriptive estimates.
- **Conditional exploratory appendices:** P3/P4 (Buffalo Pound) reported as separate case descriptions, only if custodian evidence is adequate; not pooled, not treated as validation, not given equal-status primary claims.
- **No combined “two-lake validation” claim.** The lakes remain separate case studies.

### Strengths

- Preserves the comparative measurement-audit framing without pretending the lakes are equivalent.
- Allows Buffalo Pound to contribute context if its provenance is adequate.
- Avoids discarding potentially useful data solely because it is imperfect.
- Keeps the project’s original two-lake scope visible for competition presentation.

### Weaknesses

- **Asymmetry:** Mendota has a stronger endpoint and longer record; Buffalo Pound has two seasons and unresolved provenance. A “two-lake” label can mislead if the lakes are not comparable.
- **Multiplicity:** four estimands plus nine sensitivities create many descriptive views; without a pre-specified hierarchy, the presentation can look like result-shopping even if it is not.
- **Provenance dependency:** if the custodian does not answer, P3/P4 become an appendix of unresolved data, which adds length without adding inferential value.
- **Reviewer risk:** a reviewer may say the Buffalo Pound appendices are not interpretable and should be removed.

### Assessment

**This is the most defensible path if the custodian provides adequate evidence.** It preserves the project’s scope while making the hierarchy honest: Mendota is the core; Buffalo Pound is conditional context. It requires:

- a pre-specified estimand hierarchy (P1/P2 core; P3/P4 exploratory);
- explicit statements that the lakes are not pooled and the daily summaries are not equivalent exposures;
- a rule that P3/P4 are removed if custodian evidence is inadequate;
- reviewer acceptance of the asymmetry.

**Verdict:** **Recommended, in a strict form.** The strict form is: P1/P2 core, P3/P4 conditional exploratory appendices, no equal-status four-estimand claim.

---

## 6. Outcome D — pause Stage 1

### When pause would be the right decision

Pause rather than proceed if any of the following holds:

1. The custodian cannot or will not clarify duplicate/`REP`, biomass, B7, negative/above-range RFU, coverage and time zone.
2. The scientific reviewer concludes that the Mendota depth mismatch makes P1/P2 uninterpretable, and no defensible restriction is available.
3. The statistical reviewer concludes that the two-season Buffalo Pound series cannot support even a descriptive rho, and the Mendota-only design is not considered worthwhile.
4. The detection-conditioned population or QC selection cannot be bounded, so the rank association would be uninterpretable.
5. The licence/competition review concludes that the combined use or display is not permitted.
6. The project owner cannot commit the time to revise the protocol and complete the review.
7. The reviewers identify a fatal issue that cannot be remedied with the available data.

### What pause would mean

- No analysis, no count audit, no derived dataset.
- Preserve the evidence packages and decision records.
- Keep Stage 2 as a separate conditional ambition.
- Reassess if new custodian evidence, a qualified dataset, or a revised research question becomes available.

### Assessment

**Pause is preferable to proceeding with unresolved provenance if the project’s only path is the current four-estimand protocol.** It is not preferable if the project owner is willing to reduce to a Mendota-core design and the reviewers accept it. Pause is a legitimate scientific outcome, not a failure.

**Verdict:** **Use if the custodian/reviewer conditions fail.** Do not pause merely because the work is difficult.

---

## 7. Recommendation

### 7.1 Primary recommendation

**Proceed to external review and custodian clarification, not to analysis.**

The defensible design is a **strict Outcome C**:

- **P1/P2 (Mendota)** are the core descriptive estimates.
- **P3/P4 (Buffalo Pound)** are conditional exploratory appendices, retained only if the custodian provides adequate duplicate, biomass, B7, RFU, coverage and time-zone evidence.
- **No pooling, no four-estimand validation claim, no equal-status primary hierarchy.**
- **Protocol QC section must be formally revised** to match the D-05 evidence before approval.
- **D-15 remains NOT APPROVED** until all prior decisions, the count audit, the custodian evidence, the licence review and the independent reviews are recorded.

### 7.2 Fallback

If Buffalo Pound remains unresolved, adopt **Outcome B (Mendota-only)** rather than carrying unresolved P3/P4 as if they were interpretable.

### 7.3 If both fail

Adopt **Outcome D (pause)**. Do not manufacture a result from data whose provenance cannot be defended.

### 7.4 Why this is preferable to the alternatives

- **Versus Outcome A:** it does not pretend that P3/P4 are equal-status primary estimates when their provenance is unresolved.
- **Versus a pure Mendota-only design:** it preserves the comparative context if the evidence supports it, without making the comparison a validation claim.
- **Versus pause now:** it allows the project to obtain the evidence that could make the study viable, while keeping analysis off.
- **Versus proceeding with the current protocol:** it avoids applying QC rules that the evidence has already contradicted.

---

## 8. Conditions before any analysis

1. Custodian response recorded (or a documented decision that P3/P4 are dropped).
2. Protocol QC section revised and formally re-approved.
3. Scientific reviewer report received and reconciled.
4. Statistical reviewer report received and reconciled.
5. Licence/competition review completed.
6. Count-only audit authorised and completed.
7. D-01–D-14 recorded as approved, rejected or formally deferred with reasons.
8. D-15 explicitly approved.
9. Data and code hashes verified.
10. Claims matrix checked against the final results.

No step may be skipped. A completed review is not an approval. A successful integrity check is not scientific validity. A custodian answer is not a licence.

---

## 9. Verdict

**Stage 1 is conditionally viable as a reduced, exploratory measurement audit. It is not viable as the current four-estimand protocol, and it is not ready for analysis.**

The most important next step is not statistical. It is obtaining the custodian evidence and independent reviews that determine whether P3/P4 can be interpreted at all. If that evidence is not obtainable, the project should reduce to Mendota-only or pause, not proceed with unresolved data.

**No analysis was performed. No decision was approved. D-15 remains NOT APPROVED.**
