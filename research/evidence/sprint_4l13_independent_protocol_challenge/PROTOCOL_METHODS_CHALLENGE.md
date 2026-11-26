# Protocol Methods Challenge

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **This is a review, not an approval. It does not authorise analysis. The protocol remains PROPOSED — NOT APPROVED.**

## 1. Review scope

This review independently challenges the complete Sprint 4L.12 protocol and pre-analysis plan. It covers:

- research question and estimands;
- association versus agreement, including “relative concordance”;
- bootstrap uncertainty and temporal dependence;
- biological endpoints;
- matching and temporal sensitivity;
- QC and missing data;
- the two-lake comparison;
- special handling decisions;
- prior art and originality;
- all 15 human decisions.

The review inspected all Sprint 4L.12 deliverables, the index, SHA-256 register and README, the Sprint 4L.11 strategic decision, and the relevant Sprint 4L.9/4L.10 evidence. It did not compute correlations, create derived datasets, plot project data, label events, run models, or approve any decision.

## 2. Overall verdict

**READY AFTER SPECIFIC REVISIONS — HUMAN REVIEW REQUIRED.**

The protocol is methodologically coherent in its broad design:

- it correctly refuses absolute agreement and predictive/validation claims;
- it separates Turner and YSI;
- it separates Mendota and Buffalo Pound;
- it defines inclusion and matching rules;
- it has an explicit claims matrix;
- it is honest about low–moderate originality.

However, it is **not ready for approval as written**. There are material issues that could change the estimands, the sample size, the uncertainty statements, and the interpretation:

1. the four “maximum n” values are not actual usable n;
2. the primary question uses “paired observations” for date-level co-occurrence;
3. “relative concordance” is not defined in the primary question and adds little;
4. the Buffalo Pound bootstrap cannot support a defensible interval;
5. the Mendota year-cluster bootstrap is questionable with few, non-exchangeable years;
6. the QC rule (“retain H if plausible”) is not fully operationalized;
7. Buffalo Pound biomass derivation is not documented in the local metadata;
8. the two-lake “depth-alignment” contrast is confounded and cannot isolate depth;
9. the 2019-07-17 anomaly could dominate a rank correlation;
10. source metadata and access labels need correction.

None of these requires new data. All are fixable through protocol revision and human decisions. If they are not fixed, the correct outcome is **NOT READY — MATERIAL METHODOLOGICAL ISSUES**.

## 3. Area-by-area challenge

| Area | Finding | Severity | Required action |
|---|---|---|---|
| A. Question and estimands | Precise in intent, but “paired,” “strength,” and “depth-alignment setting” overstate what date-level data can support; actual n unknown | **Major** | Rewrite question; enumerate actual n; define estimands as four association estimates, not four independent quantities |
| B. Association vs agreement | Correctly refuses absolute agreement; Spearman appropriate for monotonic association; “relative concordance” is weakly defined and adds little | **Major** | Remove/demote relative concordance; define or drop; report ρ and n without strength labels |
| C. Bootstrap and dependence | Mendota year-cluster bootstrap questionable; Buffalo Pound date-level bootstrap invalid with two seasons and serial dependence | **Critical** | No BP bootstrap interval; replace Mendota interval with descriptive range/season-year block sensitivity; revise D-10 |
| D. Biological endpoints | Mendota biovolume well documented but taxonomy/detection limited; Buffalo Pound biomass derivation not documented locally | **Major** | Verify BP biomass formula; document; conditional endpoint status |
| E. Matching | Same-day is date-level co-occurrence, not paired measurement; ±1-day sensitivity adds ambiguity | **Major** | Reword; label ±1-day as exploratory; no lead/lag/onset |
| F. QC and missingness | Flag taxonomy is thoughtful, but “plausible” is not operational; negative-value exclusion may truncate low signal; B7 may remove high biomass | **Major** | Exact decision tree and bounds; negative/B7 sensitivity; quantify excluded vs included |
| G. Two-lake comparison | Severe confounding; depth alignment is one of many differences; no causal depth interpretation | **Major** | Reframe as two case studies; remove depth as explanatory variable |
| H. Special decisions | 2019-07-17 retention is defensible, but leverage not assessed; replicate and B7 decisions remain unresolved | **Moderate** | Retain + flag + leverage report; human decisions D-08/D-09 |
| Prior art/originality | Measurement question already extensively studied; mixed/contradictory results; low–moderate originality | **Major for D-13** | Reframe as modest measurement audit; pause if novelty required |
| Sources | Some metadata incomplete; some key claims abstract-only; contradictory studies not fully represented | **Minor–Moderate** | Correct metadata; add Bertone 2018/2019, Ma 2023, Rozina 2018, Haggard 2023, methodological sources |

## 4. What passes independent review

The following elements are methodologically sound or appropriately cautious:

1. **No absolute agreement claim.** The protocol correctly states that RFU and biovolume/biomass are different quantities on different scales.
2. **No predictive/validation claim.** The claims matrix prohibits validation, accuracy, prediction, and early warning.
3. **Turner/YSI separation.** No concatenation; the orders-of-magnitude difference is acknowledged.
4. **Mendota/Buffalo Pound separation.** No pooled correlation; biovolume and biomass are not treated as equivalent.
5. **Date as the unit.** Sensor readings and taxon rows are not treated as independent observations.
6. **Explicit matching rule.** Same-day primary; no interpolation; ±1-day only as sensitivity.
7. **Explicit QC taxonomy.** Missing, flagged, excluded, and usable observations are conceptually distinguished.
8. **2019-07-17 transparency.** The anomaly is documented, retained, and flagged; exclusion is a sensitivity, not a silent correction.
9. **Claims matrix.** The prohibited-phrase list is unusually strong and appropriate.
10. **Originality honesty.** The protocol does not claim novelty from matched FAR, algorithms, or dataset availability.

These are real strengths and should be preserved in revision.

## 5. Cross-cutting problems

### 5.1 “Maximum n” is not “usable n”

The protocol repeatedly presents 128, 139, 42, and 42 as maximum n. These are **upper bounds under the strict 4L.10 unflagged rule**, not the actual primary analysis n under the 4L.12 QC rule. The 4L.12 rule retains some `H` values, excludes `C/E/G/O`, excludes negative pigments, excludes B7 for Buffalo Pound, and requires within-day coverage. The actual n could be higher or lower, and no count-only audit has been performed.

This is a material feasibility gap. A protocol should not proceed to estimation with unknown n. A count-only enumeration (no correlations) must be completed after approval of the QC rule and before estimation. If the actual n is too small for a stable rank estimate, the protocol must return to review.

### 5.2 “Paired observations” overstates the design

The biological data are date-only. The sensor data are daily summaries. A same-day observation is a **date-level co-occurrence**, not a paired measurement of the same water parcel at the same time. The phrase “paired observations” should be removed or qualified everywhere.

### 5.3 “Depth-alignment setting” implies a comparison the design cannot support

Mendota and Buffalo Pound differ in lake type, morphometry, stratification, community, instrument, period, sampling frequency, sample integration method, QC, and endpoint. Depth alignment is one difference among many. The question should not present it as an explanatory setting.

### 5.4 “Relative concordance” is under-specified

The phrase appears in the operational definition of comparability and in the claims matrix, but the mathematical definition is only in the statistical specification (sign of first differences). It is not defined in the primary question document, and it is not clear that it adds information beyond Spearman ρ. It should be removed from the operational definition or formally defined and demoted to exploratory.

### 5.5 Uncertainty cannot be manufactured by resampling

The protocol treats bootstrap intervals as descriptive uncertainty. That is the right instinct, but the proposed resampling schemes do not match the dependence structure:

- Mendota years are not exchangeable; 14 clusters is few; within-year sampling is seasonal and unbalanced.
- Buffalo Pound has two seasons; date-level resampling ignores serial dependence and is anti-conservative.

A descriptive range across years/seasons and a clear statement of “no reliable interval” is more honest than a bootstrap interval that looks inferential.

## 6. Severity definitions

| Severity | Meaning |
|---|---|
| **Critical** | The current method could produce a misleading uncertainty statement or invalid estimand; must be fixed before approval |
| **Major** | The protocol is ambiguous or overclaims; must be fixed before analysis |
| **Moderate** | A defensible choice is possible, but the current text is insufficient; fix before final approval |
| **Minor** | Documentation/metadata issue; fix before release |

## 7. Required revisions summary

The essential revisions are specified in `REQUIRED_PROTOCOL_REVISIONS.md`. In brief:

1. Rewrite the question to remove “paired,” “strength,” and explanatory “depth-alignment setting.”
2. Enumerate actual usable n under the approved QC rule before estimation.
3. Remove or formally define and demote “relative concordance.”
4. Replace the Buffalo Pound bootstrap with no interval or a clearly descriptive range; revise the Mendota interval.
5. Operationalize QC with an exact decision tree and numeric bounds; reconsider negative-value exclusion.
6. Verify and document Buffalo Pound biomass derivation.
7. Reframe the two-lake comparison as two case studies.
8. Add a leverage/robustness report for 2019-07-17.
9. Correct source metadata and add contradictory evidence.
10. Fix the deliverables index status.

## 8. What would make the review outcome worse

The outcome would become **NOT READY — MATERIAL METHODOLOGICAL ISSUES** if:

- the actual n remains unenumerated;
- the Buffalo Pound bootstrap interval is retained as a primary uncertainty statement;
- “relative concordance” remains undefined in the primary question;
- the depth contrast is presented as an isolated comparison;
- the QC rule remains dependent on unstated “plausibility” judgement;
- Buffalo Pound biomass derivation remains undocumented.

The outcome would become **RECOMMEND PAUSE — INSUFFICIENT SCIENTIFIC VALUE** if:

- the team requires a genuinely novel early-warning contribution;
- the measurement audit cannot be framed as a legitimate modest contribution;
- the human reviewers conclude that reproducing known weak/variable relationships is not worth the effort.

## 9. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- This review does not approve the protocol, any of the 15 decisions, or Gate 2.
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
