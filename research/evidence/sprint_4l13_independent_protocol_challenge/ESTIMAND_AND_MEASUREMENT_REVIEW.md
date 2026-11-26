# Estimand and Measurement Review

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

> **This review does not approve the protocol or authorise analysis.**

## 1. The proposed question

The 4L.12 primary question is:

> In Lake Mendota (2006–2020) and Buffalo Pound Lake (2018–2019), among same-day paired observations and analysed separately by lake and sensor era, what are the direction, strength and descriptive uncertainty of the rank association between surface chlorophyll and phycocyanin fluorescence and independent microscopy-derived cyanobacteria biovolume (Mendota) or cyanobacteria biomass (Buffalo Pound), and how do these associations vary by season and depth-alignment setting?

The question is **substantively coherent** but not yet **operationally precise**. Four phrases create ambiguity:

| Phrase | Problem | Recommended replacement |
|---|---|---|
| “paired observations” | Biology is date-only; sensor is a daily summary. There is no known time pairing or same water parcel. | “same-day date-level co-occurrence” |
| “strength” | Not a defined statistical quantity; invites arbitrary “weak/strong” labels | “direction and magnitude of Spearman’s ρ” |
| “descriptive uncertainty” | Implies an interval may exist; Buffalo Pound cannot support a reliable interval | “n, descriptive interval where defensible, and sensitivity range” |
| “depth-alignment setting” | Implies a controlled contrast; depth is confounded with lake, instrument, period, community, sampling, and endpoint | “two lake-specific settings that differ in depth alignment and many other respects” |

### 1.1 Why this matters

The question is the contract for the analysis. If it says “paired” or “depth-alignment setting,” readers will expect a paired measurement design or a depth comparison. The data cannot deliver either. The wording must be revised before approval.

## 2. The four primary estimands

| ID | Lake / era | Sensor | Biological endpoint | Proposed max n | What it actually estimates |
|---|---|---|---|---:|---|
| P1 | Mendota / Turner 2006–2019 | Chlorophyll RFU | Cyanobacteria biovolume (0–8 m) | 128 | Date-level monotonic association between daily chlorophyll and cyanobacteria biovolume |
| P2 | Mendota / Turner 2006–2019 | Phycocyanin RFU | Cyanobacteria biovolume (0–8 m) | 139 | Date-level monotonic association between daily phycocyanin and cyanobacteria biovolume |
| P3 | Buffalo Pound / YSI 6600 2018–2019 | Chlorophyll RFU | Cyanobacteria biomass (0.8 m) | 42 | Date-level monotonic association between daily chlorophyll and cyanobacteria biomass |
| P4 | Buffalo Pound / YSI 6600 2018–2019 | Phycocyanin RFU | Cyanobacteria biomass (0.8 m) | 42 | Date-level monotonic association between daily phycocyanin and cyanobacteria biomass |

### 2.1 Are the estimands distinct?

They are **four distinct sensor–endpoint pairs**, but they are not four independent quantities:

- P1 and P2 share the same biological endpoint and the same dates; the sensors are correlated.
- P3 and P4 share the same biological endpoint and the same dates; the sensors are correlated.
- P1/P2 and P3/P4 use different lakes, periods, instruments, and endpoints.

The protocol should not present four estimates as four independent tests or four independent pieces of evidence. They are a small, correlated set of descriptive associations. No multiplicity correction is needed because there are no p-values, but the report must not count them as independent confirmations.

### 2.2 Are the estimands justified by the observations?

**P1/P2: conditionally yes.** Mendota has 128/139 same-day strict-unflagged dates over 14 years. That is enough for a descriptive rank association, but not for precise seasonal/era strata. The 0.5 m sensor vs 0–8 m composite is a major interpretational limitation.

**P3/P4: conditional.** Buffalo Pound has 42 dates over two seasons. That is enough for a descriptive association, but not for a stable seasonal analysis or a reliable uncertainty interval. The endpoint is biomass, not biovolume; its derivation must be documented. B7 and coverage exclusions may reduce n.

### 2.3 Maximum n versus actual usable n

This is a **major unresolved issue**.

The 4L.12 protocol lists maximum n as 128, 139, 42, 42. These are **not** the actual primary n under the protocol’s own QC rule. They come from the strict 4L.10 “unflagged only” counts. The 4L.12 primary rule:

- retains `H` values if “plausible”;
- excludes `C`, `E`, `G`, `O`;
- excludes negative pigment values;
- excludes Buffalo Pound `B7`;
- requires ≥50% within-day coverage and both halves of the day for Buffalo Pound.

The actual n could be higher (if positive `H` values are added) or lower (if negatives/`B7`/coverage remove dates). No count-only audit has been performed. The protocol says the final n “may be larger” and “must be enumerated,” but the feasibility of P1–P4 is not established.

**Review recommendation:** Before estimation, a count-only enumeration must report:

- total biological dates;
- dates in window;
- dates meeting depth rules;
- dates with any sensor record;
- dates with numeric sensor data;
- dates passing each QC rule;
- dates passing coverage;
- final n per estimand;
- n by year and season;
- overlap of exclusions with high/low biological values.

This is not a correlation analysis and does not create a cleaned dataset. It is a feasibility/flow audit. If the final n is too small for a stable rank estimate, the protocol must return to human review.

### 2.4 What minimum n is defensible?

The protocol has a rule for seasonal strata (n < 10: no stratum ρ) but no rule for the overall estimand. A correlation based on 10–15 dates is unstable; a correlation based on 20–30 is still imprecise. The review does not impose a single number, because the appropriate minimum depends on the range and dependence structure. However, the protocol should pre-specify:

- a minimum n for reporting an overall ρ;
- a minimum n for a seasonal ρ;
- a rule for showing points only;
- a rule for returning to review if the minimum is not met.

A defensible approach is to require the human statistical reviewer to set these minima after seeing the count audit, before any correlation is computed. The minima must be based on precision/dependence, not on whether the result is interesting.

## 3. Inclusion and exclusion rules: reproducibility

The 4L.12 rules are more detailed than most protocols, but several are not fully reproducible.

| Rule | Ambiguity | Consequence | Required clarification |
|---|---|---|---|
| Mendota station | “Use station 1 if present; otherwise blank” | Mixes station types; 371/402 dates blank; not a clean spatial match | State whether station 1 is a subset or a preference; report sensitivity |
| Buffalo Pound `Group` vs `Phylum` | “Flag and exclude pending review” if mismatch | No definition of mismatch (case, whitespace, synonym) | Provide exact normalization and mismatch rule |
| Buffalo Pound replicates | Mean before summing, sum/first as sensitivity | No replicate ID; mean vs sum changes total | Justify mean as replicate assumption; verify source method |
| Mendota `H` retention | “If plausible” | Not reproducible without exact bounds | Provide numeric bounds and a rule for above/below |
| Negative pigments | Exclude primary; include sensitivity | Could truncate low signal and inflate ρ | Justify or reverse primary/sensitivity; provide tolerance |
| Buffalo Pound `B7` | Exclude primary; include sensitivity | Interval flag may remove high-biomass dates | Quantify B7 overlap with biomass; report both |
| ±1-day window | Same-day preferred; adjacent day if missing | Adds ambiguity; not a clean sensitivity | Label exploratory; do not use to rescue primary |
| Mendota 0–8 m | Exclude 0–2 m | Two dates outside sensor window; fine | State clearly |
| Taxonomy | Broad division/group only | Reduces but does not eliminate non-stationarity | Report broad-group limitation |

**Review finding:** The rules are **directionally reproducible** but not **fully algorithmically reproducible**. A second analyst could make different choices for station, `H`, `B7`, negatives, and Group/Phylum mismatches. These choices must be resolved in the protocol, not left to analysis-time judgement.

## 4. Target population and scope of inference

The protocol defines the target population as dates with valid biology and valid same-day sensor data. That is appropriate.

The scope of inference is correctly limited to the two lakes, periods, instruments, and sampling programmes. The protocol explicitly refuses generalisation, whole-column inference, bloom/toxicity inference, and early warning. This passes review.

However, the phrase “depth-alignment setting” in the question still implies a comparative inference. The scope section says the study cannot isolate depth, but the question should not imply that it can. The question and scope must be consistent.

## 5. Estimand–statistic alignment

| Estimand | Proposed statistic | Does it answer the question? | Issue |
|---|---|---|---|
| P1 | Spearman ρ | Yes, for monotonic association | “Strength” not defined; non-monotonicity not assessed |
| P2 | Spearman ρ | Yes, for monotonic association | Same; phycocyanin is taxon-dependent |
| P3 | Spearman ρ | Yes, for monotonic association | Small n/two seasons; biomass derivation |
| P4 | Spearman ρ | Yes, for monotonic association | Same; taxon-dependent; *Planktothrix* prior |
| Relative concordance | Sign of first differences | Weakly related to the question | Undefined in question; adds little; irregular intervals |
| Pearson log | Linear association on log scale | Secondary only | Log10(1+x) is arbitrary; not necessary |

The primary statistic is appropriate for a **monotonic association**. It is not appropriate for “agreement,” “accuracy,” “prediction,” or “measurement validity,” and the protocol says so. That is a strength.

## 6. Findings and required changes

### Finding A1 — Question wording overclaims the design (Major)

Remove “paired observations,” “strength,” and explanatory “depth-alignment setting.” Replace with date-level co-occurrence, direction/magnitude of ρ, and two lake-specific settings.

### Finding A2 — Actual n is unknown (Major)

The maximum n values are upper bounds, not actual n. A count-only audit is required before estimation.

### Finding A3 — Four estimands are correlated, not independent (Moderate)

Present them as four descriptive association estimates, not four independent tests/confirmations. Do not count them as independent evidence.

### Finding A4 — Inclusion rules are not fully algorithmic (Major)

Station, Group/Phylum mismatch, replicate mean, `H` plausibility, negative values, and `B7` require exact rules.

### Finding A5 — Scope is appropriately limited, but question wording is not (Major)

Align the question with the scope; remove depth as an explanatory setting.

## 7. Review recommendation for D-01, D-02, D-03, D-04, D-05, D-07, D-08, D-11

These decisions are reviewed in detail in `HUMAN_DECISION_REGISTER.md`. At the estimand level:

- **D-01:** accept rank association as the operational definition, but remove “relative concordance” or demote it to exploratory.
- **D-02:** accept supplied biomass only if the derivation is documented; otherwise downgrade/exclude.
- **D-03:** accept 0.5 m vs 0–8 m only as a case-study limitation, not a depth comparison.
- **D-04:** accept separate Turner/YSI eras; no concatenation.
- **D-05:** accept the intent, but require exact operationalization and reconsider negative-value exclusion.
- **D-07:** accept same-day primary; treat ±1-day as exploratory, not a robustness claim.
- **D-08:** accept mean only as a stated replicate assumption; verify source method.
- **D-11:** accept n<10 stratum rule; add an overall-n estimability rule.

## 8. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No decision is approved by this review.
- No analysis is authorised until the required revisions and D-15 approval are recorded.
