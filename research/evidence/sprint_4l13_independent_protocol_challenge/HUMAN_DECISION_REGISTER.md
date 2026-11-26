# Human Decision Register

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

> **This register does not approve any decision. It records the 15 decisions exactly as documented in Sprint 4L.12, reviews the evidence, and recommends options for qualified human reviewers. No decision is recorded as approved.**

## 1. How to use this register

Each entry contains:

- the original decision identifier;
- the exact decision as documented in 4L.12;
- the evidence available;
- methodological implications;
- a review recommendation (not approval);
- alternatives and trade-offs;
- the qualified reviewer(s) who must decide;
- the consequence if the decision remains unresolved.

The recommendations below are **review opinions**, not approvals. A recommendation does not become a decision until a named human reviewer records the choice, rationale, and date.

## 2. Approval separation

The following approvals are distinct and must not be inferred from one another:

| Approval | Scope | Cannot substitute for |
|---|---|---|
| Scientific reviewer approval | Question, estimands, endpoints, inclusion, claims | Statistical, data custodian, governance, licence |
| Statistical reviewer approval | Spearman, dependence, bootstrap, n rules | Scientific, data custodian, governance, licence |
| Data custodian approval | QC, missingness, anomalies, replicate handling | Scientific, statistical, governance, licence |
| Gate 2 governance approval | Option C status, no labels/models, scope | Scientific, statistical, data custodian, licence |
| Licence/competition review | CC BY-NC-SA, attribution, share-alike, competition use | Scientific, statistical, data custodian, governance |
| D-13 continuation/pause decision | Whether the study is worth doing | D-15 authorisation |
| D-15 authorisation to begin analysis | Explicit go-ahead | Any of the above |

## 3. Decision-by-decision review

### D-01 — Operational definition of “comparability”

**Exact decision:**  
> Operational definition of “comparability” | (a) rank association + relative concordance; (b) absolute agreement; (c) predictive performance

**Evidence available:**
- RFU and biovolume/biomass are different quantities on different scales.
- No Turner/YSI cross-calibration; no RFU-to-biomass conversion.
- The literature treats fluorescence as a proxy, not a calibrated measure.
- Absolute agreement and predictive performance are not estimable with these data.

**Methodological implications:**
- This decision determines every claim in the study.
- Option (b) or (c) would require a calibration/validation experiment that does not exist.
- Option (a) is feasible, but “relative concordance” is under-defined and adds little beyond Spearman ρ.

**Review recommendation (not approval):**  
**Option (a), revised:** define comparability as **rank association only** (direction and magnitude of Spearman ρ), and either remove “relative concordance” or demote it to an exploratory secondary analysis with a formal definition.

**Alternatives and trade-offs:**
- (a) original: feasible but ambiguous due to “relative concordance.”
- (a) revised: cleanest; loses a second descriptive statistic that adds little.
- (b): not estimable; would produce misleading agreement claims.
- (c): not estimable; would require held-out predictive validation.

**Qualified reviewer:** Scientific reviewer + statistical reviewer.

**Consequence if unresolved:** The primary estimand and claims remain ambiguous; the protocol cannot be approved.

---

### D-02 — Buffalo Pound endpoint

**Exact decision:**  
> Buffalo Pound endpoint | (a) supplied biomass; (b) derive biovolume from cell volume × density; (c) exclude Buffalo Pound

**Evidence available:**
- The Painter et al. 2022 files supply `Biomass_mg_m3`, `Cell_Density_L`, and `Cell_Volume_um3`, but no biovolume column.
- Biomass is likely derived from cell counts × cell volume × a conversion, but the formula is not documented in the local metadata.
- 2018 and 2019 have different schema (`Sample_ID` vs `REP`), different taxa counts, and only 39 shared taxa.
- Mendota biovolume and Buffalo Pound biomass are not numerically equivalent.

**Methodological implications:**
- Option (b) creates a new derived endpoint; this is not authorised in 4L.12 and would require a new protocol.
- Option (c) would remove the depth-aligned case and reduce the study to Mendota.
- Option (a) is the only path that uses existing supplied data, but it is conditional on documenting the biomass derivation.

**Review recommendation (not approval):**  
**Option (a), conditional on verifying the biomass formula and 2018/2019 consistency.** If the derivation cannot be documented, downgrade Buffalo Pound to exploratory or exclude it.

**Alternatives and trade-offs:**
- (a) conditional: preserves the two-case design; requires method verification.
- (b): new derived endpoint; not authorised; risks inconsistency.
- (c): loses the comparison; simplifies but weakens the study.

**Qualified reviewer:** Data custodian + scientific reviewer.

**Consequence if unresolved:** P3/P4 cannot be defined; the two-lake design collapses to Mendota.

---

### D-03 — Mendota depth comparator

**Exact decision:**  
> Mendota depth comparator | (a) 0.5 m vs 0–8 m, no correction; (b) attempt a depth correction; (c) exclude Mendota

**Evidence available:**
- Sensor variables are at 0.5 m.
- Biology is a 0–8 m tube composite (400 dates; 2 dates at 0–2 m).
- No depth-resolved paired profiles at the buoy.
- No validated depth correction.
- The sensor and sampling site are ~105.7 m apart; station metadata are mostly blank.

**Methodological implications:**
- Option (b) would require an unvalidated model; it would create a new derived endpoint and introduce assumptions.
- Option (c) would remove the long Mendota record.
- Option (a) is the only transparent choice, but it cannot support a depth correction or whole-column claim.

**Review recommendation (not approval):**  
**Option (a), with explicit reframing as a depth-mismatched case study.** Do not apply a depth correction. Do not describe the 0.5 m sensor as a 0–8 m measure.

**Alternatives and trade-offs:**
- (a): transparent; limits inference.
- (b): not defensible without paired profiles/validation.
- (c): loses Mendota; may be preferable if the team cannot accept the limitation.

**Qualified reviewer:** Scientific reviewer + data custodian.

**Consequence if unresolved:** P1/P2 interpretation remains ambiguous.

---

### D-04 — Turner/YSI handling

**Exact decision:**  
> Turner/YSI handling | (a) separate eras; (b) concatenate; (c) convert

**Evidence available:**
- Both output RFU but differ by orders of magnitude.
- 2019 paired medians: Turner chlorophyll 1,354.74 vs YSI 0.39; Turner phycocyanin 802.01 vs YSI 0.59.
- No cross-calibration equation or conversion.
- The EML states “significant magnitude differences.”

**Methodological implications:**
- Option (b) would create an artificial step and invalidate the trend.
- Option (c) would require a calibration that does not exist.
- Option (a) is the only defensible choice.

**Review recommendation (not approval):**  
**Option (a): separate eras; never concatenate.** The 2019 transition year should be analysed separately by instrument; no averaging/choosing.

**Alternatives and trade-offs:**
- (a): correct; reduces YSI n.
- (b): invalid.
- (c): not supported.

**Qualified reviewer:** Data custodian + statistical reviewer.

**Consequence if unresolved:** The sensor series cannot be used defensibly.

---

### D-05 — Primary QC rule

**Exact decision:**  
> Primary QC rule | (a) retain H, exclude C/E/G/O; (b) strict unflagged; (c) include all numeric

**Evidence available:**
- `C` often contains numeric values; `H` means outside standard range, not invalid.
- `G` is biofouling; `O` is undefined.
- Undocumented codes occur in eight columns.
- Negative pigment values exist; their meaning is ambiguous.
- Turner chlorophyll has many `C` flags in 2014–2015.
- Buffalo Pound `B7` is an interval fouling flag.

**Methodological implications:**
- Option (b) truncates high values (H) and may bias against blooms.
- Option (c) includes faulty/noisy values.
- Option (a) balances, but “retain H if plausible” is not operational.
- Negative-value exclusion is not clearly justified.
- B7 exclusion may remove high-biomass dates.

**Review recommendation (not approval):**  
**Option (a), revised:** provide an exact decision tree and numeric bounds; retain H within physical bounds; justify or reverse negative-value exclusion; quantify B7 overlap; report strict-unflagged sensitivity.

**Alternatives and trade-offs:**
- (a) revised: best balance; requires detailed rules.
- (b): transparent but truncates high values.
- (c): inclusive but contaminated.

**Qualified reviewer:** Data custodian + statistical reviewer.

**Consequence if unresolved:** Actual n and bias are unknown; results may be non-reproducible.

---

### D-06 — Primary daily summary

**Exact decision:**  
> Primary daily summary | (a) full-day mean for both lakes; (b) nighttime for BP only; (c) daytime for both

**Evidence available:**
- Mendota daily values are provider averages of 1-minute data; no nighttime reconstruction from the daily file.
- Buffalo Pound 10-minute data allow nighttime/daytime summaries.
- Light-induced quenching can reduce chlorophyll up to 79% and PC up to 59%.
- Mendota and Buffalo Pound daily summaries have different coverage/precision.

**Methodological implications:**
- Option (b) creates an asymmetry: BP nighttime vs Mendota full-day.
- Option (c) maximizes quenching bias.
- Option (a) is structurally comparable but includes quenching.

**Review recommendation (not approval):**  
**Option (a), with BP nighttime and daytime as sensitivity analyses.** State the asymmetry explicitly; do not present the BP nighttime result as directly comparable to Mendota.

**Alternatives and trade-offs:**
- (a): comparable structure; includes quenching.
- (b): reduces quenching but breaks comparability.
- (c): worst for quenching.

**Qualified reviewer:** Scientific reviewer + statistical reviewer.

**Consequence if unresolved:** Diel bias and cross-lake comparability remain unclear.

---

### D-07 — Temporal window

**Exact decision:**  
> Temporal window | (a) same-day primary + ±1-day sensitivity; (b) ±3/±7/±14; (c) same-day only, no sensitivity

**Evidence available:**
- Biology is date-only; no sample times.
- Mendota median interval 14 days; Buffalo Pound 4–16 days.
- ±1 day adds dates but changes sample composition.
- Wider windows can span bloom phases.

**Methodological implications:**
- (b) is not defensible for same-time comparability.
- (c) is cleanest but may lose dates.
- (a) is a compromise but not a clean robustness check.

**Review recommendation (not approval):**  
**Option (a) revised:** same-day primary; ±1-day as **exploratory temporal-window analysis only**, not a robustness or agreement claim. Consider dropping it if the reviewers want the cleanest design.

**Alternatives and trade-offs:**
- (a) revised: transparent; adds a secondary analysis.
- (b): wider windows increase ambiguity.
- (c): cleanest; may reduce n.

**Qualified reviewer:** Scientific reviewer + statistical reviewer.

**Consequence if unresolved:** Matching ambiguity remains; results may be overinterpreted.

---

### D-08 — Buffalo Pound replicate handling

**Exact decision:**  
> Buffalo Pound replicate handling | (a) mean before summing; (b) sum; (c) first row

**Evidence available:**
- 2018: 19 date–species groups with two rows; no replicate ID.
- 2019: REP1/REP2 on disjoint dates; not paired replicates.
- 1,222 taxon rows; 248 cyanophyte rows; not independent.
- The source method does not document whether duplicates are replicates or split samples.

**Methodological implications:**
- Mean is appropriate if duplicates are replicate counts.
- Sum is appropriate if they are split samples/variants.
- First row discards information.
- The choice changes the date total.

**Review recommendation (not approval):**  
**Option (a) as a stated replicate assumption**, with sum/first-row sensitivity. Verify the source method; if it cannot be verified, report both and do not treat either as definitive.

**Alternatives and trade-offs:**
- (a): reasonable default; assumption-dependent.
- (b): may double-count if replicates.
- (c): arbitrary; loses information.

**Qualified reviewer:** Data custodian.

**Consequence if unresolved:** P3/P4 totals are method-dependent.

---

### D-09 — 2019-07-17 anomaly

**Exact decision:**  
> 2019-07-17 anomaly | (a) retain and flag, exclude in sensitivity; (b) exclude from primary; (c) correct

**Evidence available:**
- 45.81 mg m⁻³ total; 41.02 cyanobacteria; 9 rows, all REP2.
- Neighbours 12,587.1 and 9,497.9 mg m⁻³.
- Taxonomy and group biomass agree; toxin sample exists but unverified.
- Cause unresolved.

**Methodological implications:**
- Retaining preserves a documented observation but may dominate ρ at n=42.
- Excluding avoids dominance but deletes data.
- Correcting has no basis.

**Review recommendation (not approval):**  
**Option (a), with a mandatory leverage report**: rank/leverage, ρ with/without, and whether the conclusion depends on the date. Do not interpret as bloom/non-bloom.

**Alternatives and trade-offs:**
- (a): transparent; requires leverage analysis.
- (b): conservative; risks bias.
- (c): not defensible.

**Qualified reviewer:** Data custodian + scientific reviewer.

**Consequence if unresolved:** P3/P4 may be driven by one date.

---

### D-10 — Uncertainty method

**Exact decision:**  
> Uncertainty method | (a) Mendota year-cluster bootstrap; BP naive date bootstrap + year separation; (b) p-values; (c) no intervals

**Evidence available:**
- Temporal autocorrelation and seasonal clustering.
- Mendota: 14 non-exchangeable years; few clusters.
- Buffalo Pound: two seasons; date-level bootstrap ignores dependence.
- No coverage/simulation evidence.

**Methodological implications:**
- (b) violates the no-hypothesis-test rule.
- (a) as written may produce misleading intervals, especially BP.
- (c) hides uncertainty but is more honest than a false interval.

**Review recommendation (not approval):**  
**Revised (a):** Mendota — ρ, n, leave-one-year-out range, optional season-year block bootstrap as descriptive sensitivity; no primary confidence interval. Buffalo Pound — no bootstrap interval; ρ, n, separate 2018/2019, leave-one-date-out range; state no reliable interval. No p-values.

**Alternatives and trade-offs:**
- Revised (a): honest; less “statistical” but defensible.
- (b): prohibited.
- (c): no intervals; transparent.

**Qualified reviewer:** Statistical reviewer.

**Consequence if unresolved:** Uncertainty claims may be invalid.

---

### D-11 — Small-n reporting

**Exact decision:**  
> Small-n reporting | (a) no stratum ρ if n<10; show points; (b) compute all; (c) pool strata

**Evidence available:**
- Seasonal strata often 10–20 dates; winter near zero.
- n=10 is still unstable.
- No overall-n rule.

**Methodological implications:**
- (b) produces unstable estimates.
- (c) obscures seasonal structure.
- (a) is reasonable but incomplete.

**Review recommendation (not approval):**  
**Option (a), plus an overall-n estimability rule** set by the statistical reviewer after the count audit; show points and n; no pooling.

**Alternatives and trade-offs:**
- (a): cautious; may suppress useful description.
- (b): unstable.
- (c): misleading.

**Qualified reviewer:** Statistical reviewer.

**Consequence if unresolved:** Small-stratum results may be overinterpreted.

---

### D-12 — Claims matrix

**Exact decision:**  
> Claims matrix | (a) adopt as written; (b) soften prohibitions; (c) reject

**Evidence available:**
- The matrix correctly prohibits validation, prediction, early warning, bloom detection, toxicity, whole-column, agreement, and causal depth claims.
- Some permitted wording still needs alignment with the revised question.

**Methodological implications:**
- (b) risks overclaiming.
- (c) removes the main safeguard.
- (a) is appropriate, with wording updates.

**Review recommendation (not approval):**  
**Option (a), with updates** to reflect the revised question and the removal/demotion of relative concordance.

**Alternatives and trade-offs:**
- (a): strongest safeguard.
- (b): risky.
- (c): unacceptable.

**Qualified reviewer:** Scientific reviewer + Gate 2 governance.

**Consequence if unresolved:** Overclaim risk.

---

### D-13 — Originality sufficiency

**Exact decision:**  
> Originality sufficiency | (a) proceed as a modest measurement study; (b) pause; (c) pivot

**Evidence available:**
- The measurement question is well studied.
- The two-lake depth contrast is confounded.
- The study is a modest measurement audit, not a novel method.
- The literature contains both positive and negative results.
- No new data/method is proposed.

**Methodological implications:**
- (a) is defensible only if a modest/negative measurement result is acceptable.
- (b) is honest if a novel early-warning result is required.
- (c) has no specific evidence-based alternative.

**Review recommendation (not approval):**  
**Conditional:** proceed as a modest measurement audit only if the team and competition framing accept a negative/limited result; otherwise pause. Do not pivot without a specific, evidence-based alternative and a new protocol.

**Alternatives and trade-offs:**
- (a): feasible; low novelty.
- (b): honest; ends the current direction.
- (c): unsupported without a specific alternative.

**Qualified reviewer:** Project lead + scientific reviewer + Gate 2 governance.

**Consequence if unresolved:** No go/no-go decision; analysis cannot start.

---

### D-14 — Licence/competition compliance

**Exact decision:**  
> Licence/competition compliance | (a) use Painter data under CC BY-NC-SA with attribution/share-alike; (b) exclude Painter data; (c) seek permission

**Evidence available:**
- Painter et al. 2022 Borealis data are CC BY-NC-SA 4.0.
- Mendota and Buffalo Pound buoy data are CC BY 4.0.
- Competition rules may restrict non-commercial/share-alike use or require different licensing.

**Methodological implications:**
- (b) removes Buffalo Pound.
- (c) requires external contact (not authorised in this sprint).
- (a) is feasible only with legal/competition review.

**Review recommendation (not approval):**  
**Option (a), subject to a documented licence/competition review.** If the competition cannot accommodate CC BY-NC-SA, exclude Buffalo Pound or seek permission through the proper channel.

**Alternatives and trade-offs:**
- (a): preserves two cases; legal risk if unreviewed.
- (b): safe; loses Buffalo Pound.
- (c): requires contact; not authorised now.

**Qualified reviewer:** Licence/competition reviewer (legal or institutional).

**Consequence if unresolved:** Buffalo Pound data cannot be used publicly.

---

### D-15 — Approval to begin analysis

**Exact decision:**  
> Approval to begin analysis | (a) approve; (b) approve with changes; (c) do not approve

**Evidence available:**
- Protocol is proposed, not approved.
- Essential revisions remain.
- Actual n is unknown.
- Statistical method needs revision.
- D-13 is unresolved.
- Licence review is incomplete.

**Methodological implications:**
- (a) would authorise analysis before revisions; not defensible.
- (b) could be appropriate after revisions and decisions.
- (c) is the current status.

**Review recommendation (not approval):**  
**Option (c) until D-01–D-14 are resolved and essential revisions are incorporated.** Then D-15 may be reconsidered.

**Alternatives and trade-offs:**
- (a): premature.
- (b): only after a revised protocol and recorded approvals.
- (c): correct current state.

**Qualified reviewer:** All required approvers (scientific, statistical, data custodian, Gate 2 governance, licence).

**Consequence if unresolved:** No analysis is authorised.

## 4. Decision status matrix

| ID | Topic | Review recommendation | Human decision recorded? | Blocks analysis? |
|---|---|---|---|---|
| D-01 | Comparability definition | (a) revised: rank association only | No | Yes |
| D-02 | Buffalo Pound endpoint | (a) conditional on biomass verification | No | Yes |
| D-03 | Mendota depth comparator | (a) as case-study limitation | No | Yes |
| D-04 | Turner/YSI | (a) separate | No | Yes |
| D-05 | QC rule | (a) revised, exact decision tree | No | Yes |
| D-06 | Daily summary | (a) + BP nighttime sensitivity | No | Yes |
| D-07 | Temporal window | (a) revised: ±1 exploratory | No | Yes |
| D-08 | BP replicates | (a) mean as assumption | No | Yes |
| D-09 | 2019-07-17 | (a) + leverage report | No | Yes |
| D-10 | Uncertainty | Revised: no BP interval | No | Yes |
| D-11 | Small-n | (a) + overall-n rule | No | Yes |
| D-12 | Claims matrix | (a) with updates | No | Yes |
| D-13 | Originality | Conditional proceed/pause | No | Yes |
| D-14 | Licence | (a) with legal review | No | Yes |
| D-15 | Begin analysis | (c) until resolved | No | Yes |

## 5. What must not be inferred

- A review recommendation is not an approval.
- Scientific approval does not imply statistical approval.
- Statistical approval does not imply data-custodian approval.
- Data-custodian approval does not imply Gate 2 governance approval.
- Licence review does not imply D-13 or D-15.
- D-13 proceeding does not imply D-15 authorisation.
- D-15 authorisation requires all preceding approvals and the revised protocol.

## 6. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No decision in this register is approved.
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
