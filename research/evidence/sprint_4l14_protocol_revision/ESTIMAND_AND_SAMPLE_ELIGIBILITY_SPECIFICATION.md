# Estimand and Sample Eligibility Specification

**Sprint:** 4L.14  
**Status:** PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Date:** 2026-11-24

> **No analysis is authorised. Actual usable n is not calculated in this sprint. The count-only audit described here is a prohibited future analysis step until D-15 approval.**

## 1. Purpose

This document implements Sprint 4L.13 revision R-02. It:

- distinguishes previously reported maximum n from actual usable n;
- specifies the exact eligibility rules for P1–P4;
- states whether actual n is known;
- specifies what must be calculated after approval;
- identifies potential exclusions and their consequences.

It does **not** calculate correlations or create analytical datasets.

## 2. The four estimands

| ID | Lake / era | Sensor | Biological endpoint | Previously reported maximum n | Actual primary n known? |
|---|---|---|---|---:|---|
| P1 | Mendota / Turner 2006–2019 | Chlorophyll RFU | Cyanobacteria biovolume (0–8 m) | 128 | **No** |
| P2 | Mendota / Turner 2006–2019 | Phycocyanin RFU | Cyanobacteria biovolume (0–8 m) | 139 | **No** |
| P3 | Buffalo Pound / YSI 6600 2018–2019 | Chlorophyll RFU | Cyanobacteria biomass (0.8 m) | 42 | **No** |
| P4 | Buffalo Pound / YSI 6600 2018–2019 | Phycocyanin RFU | Cyanobacteria biomass (0.8 m) | 42 | **No** |

The 128/139/42/42 values are **upper bounds under the strict 4L.10 “unflagged only” rule**. They are not the actual primary n under the revised QC rules, which:

- retain some `H` values;
- retain negative RFU as observed, with exclusion sensitivity;
- exclude `C`, `E`, `G`, `O`, and undocumented flags from primary;
- exclude Buffalo Pound `B7` from primary;
- require Buffalo Pound within-day coverage;
- exclude missing values.

The actual n may be higher or lower. It must be enumerated before estimation.

## 3. Eligibility rules by estimand

### 3.1 P1 — Mendota Turner chlorophyll vs cyanobacteria biovolume

A date is eligible for P1 if **all** of the following hold:

1. `lakeid = ME` in NTL-LTER 88.31.
2. `sampledate` lies in 2006-07-09 to 2020-12-10.
3. `depth_range = 0-8m`.
4. The date has at least one cyanobacteria row (`division = Cyanophyta` after whitespace trimming).
5. The cyanobacteria biovolume total is finite and ≥ 0.
6. The date has a same-day `avg_chlor_rfu_turner` value.
7. The Turner chlorophyll value is `USABLE` under `QC_AND_MISSINGNESS_RULES.md`.
8. The date is not excluded by the station rule (see §4).

**Not eligible:** YSI chlorophyll values; Turner phycocyanin values; 0–2 m dates; dates outside the window; dates with no cyanobacteria rows.

### 3.2 P2 — Mendota Turner phycocyanin vs cyanobacteria biovolume

Same as P1, but with `avg_phyco_rfu_turner` and the phycocyanin QC rules.

### 3.3 P3 — Buffalo Pound YSI chlorophyll vs cyanobacteria biomass

A date is eligible for P3 if **all** of the following hold:

1. The date is one of the 42 documented microscopy dates in 2018–2019.
2. `Depth = 0.8`.
3. The date has at least one cyanobacteria row (`Group = Cyanophyte` after whitespace trimming; cross-checked against `Phylum = Cyanophyta`).
4. The cyanobacteria biomass total is finite and ≥ 0.
5. The date has same-day `ChlRFUShallow_RFU` values.
6. The sensor date passes the QC rules in `QC_AND_MISSINGNESS_RULES.md`.
7. The sensor date passes the within-day coverage rule: ≥50% of expected 10-minute values and at least one valid value in each half of the day.
8. The date is not excluded by the replicate rule (mean-before-sum primary; sensitivity sum/first).
9. The date is not excluded for a `Group`/`Phylum` mismatch.

**Not eligible:** deep sensors; YSI profiles; thermistors; dates outside 2018–2019; dates without 0.8 m biology; dates with only `B7`-flagged pigment values under the primary rule.

### 3.4 P4 — Buffalo Pound YSI phycocyanin vs cyanobacteria biomass

Same as P3, but with `BGPCShallowRFU_RFU` and the phycocyanin QC rules.

## 4. Mendota station rule

The 4L.12 rule was “use station 1 if present; otherwise blank.” This is retained but clarified:

- If a date has station `1` rows, use station `1` only.
- If a date has only blank-station rows, use blank-station rows.
- If a date has multiple non-blank station values, and station `1` is not present, **exclude the date** as `UNRESOLVED_STATION` (primary); include in a sensitivity using all stations.
- Do not pool station `1` with other stations in primary.
- Do not average across stations.

This rule is required because station metadata are blank for 371/402 Mendota dates and only 31 dates have station `1`.

## 5. Buffalo Pound replicate rule

- 2018: duplicate date × species rows without a replicate identifier.
- 2019: `REP1`/`REP2` on disjoint dates; not paired replicates.

Primary rule:

- collapse duplicate date × species rows by **mean** before summing to the date total;
- treat each 2019 date as one sample; do not treat `REP` as a replicate estimate.

Sensitivity:

- collapse by **sum**;
- collapse by **first row**.

Remaining uncertainty: the source method does not document whether duplicates are replicate counts or split samples. The mean rule is an explicit assumption, not a verified fact.

## 6. Buffalo Pound Group/Phylum consistency

Primary:

- require `Group = Cyanophyte` and `Phylum = Cyanophyta` after case/whitespace normalization;
- if either field is missing or they disagree, classify the row as `UNRESOLVED_GROUP` and exclude from primary;
- report the number of affected rows/dates;
- sensitivity includes rows where `Group = Cyanophyte` but `Phylum` is missing/disagrees, if the species is unambiguously cyanobacterial by a documented mapping; otherwise exclude.

No new taxonomic mapping is created in this sprint.

## 7. Actual n: what must be calculated after approval

The following **count-only audit** must be completed after D-15 approval and before any correlation:

| Step | Output |
|---|---|
| 1 | Total biological dates in source |
| 2 | Dates inside the analysis window |
| 3 | Dates meeting depth rules |
| 4 | Dates with any sensor record |
| 5 | Dates with numeric sensor values |
| 6 | Dates passing each QC rule |
| 7 | Dates passing station/group/replicate rules |
| 8 | Dates passing Buffalo Pound coverage |
| 9 | Final n for P1, P2, P3, P4 |
| 10 | n by year and season for each estimand |
| 11 | Excluded dates with reason codes |
| 12 | Included vs excluded biological endpoint distributions (median, IQR, n) — descriptive only |
| 13 | B7 overlap: n dates, biomass distribution on B7 vs non-B7 |
| 14 | Negative/H/undocumented-flag counts and their effect on n |

This audit is **not** a correlation analysis and does **not** create a cleaned analytical dataset. It is a count/eligibility audit. It must not be performed in this sprint. It requires a separate authorisation after D-15; it does not itself authorise estimation, and it must not be treated as permission to compute correlations or other analytical results.

## 8. Minimum-n rule

The protocol must pre-specify a minimum n for reporting an overall ρ. The exact number must be set by the statistical reviewer after the count audit and before estimation.

Recommended structure:

- overall ρ: require a minimum n set by the statistical reviewer (justified by precision/dependence, not by the result);
- seasonal ρ: n ≥ 10 (retained from 4L.12);
- if n is below the minimum: show points and n, do not compute ρ, and return to human review if the estimand cannot be supported.

No minimum is set in this sprint because actual n is unknown. This avoids an arbitrary threshold.

## 9. Estimand independence

The four estimands are **not independent**:

- P1/P2 share the same biological endpoint and dates;
- P3/P4 share the same biological endpoint and dates;
- the sensors within each lake are correlated.

They must be reported as four descriptive association estimates, not four independent tests or four independent confirmations. No multiplicity correction is proposed because there are no p-values; the risk is selective emphasis, controlled by pre-specification and reporting all estimates.

## 10. Estimand suitability after revisions

| Estimand | Suitability at protocol stage | Conditions | Could revision make it unsuitable? |
|---|---|---|---|
| P1 | **Suitable, conditional** | actual n; QC; no depth correction | No, unless n is inadequate |
| P2 | **Suitable, conditional** | actual n; QC; taxon dependence | No, unless n is inadequate |
| P3 | **Recommended downgrade to exploratory pending D-02 verification** | biomass derivation verified; actual n; B7/coverage; two seasons | Yes, if reviewers reject derived biomass or n is inadequate |
| P4 | **Recommended downgrade to exploratory pending D-02 verification** | same, plus *Planktothrix* detection caveat | Yes, if reviewers reject derived biomass or n is inadequate |

No estimand is categorically unsuitable at this stage. P3/P4 are recommended for **downgrade to exploratory** until the data custodian verifies the biomass derivation; if verified, they may be restored to primary subject to the count audit. If verification fails, P3/P4 are unsuitable for primary analysis.

## 11. What is not allowed

- Do not treat 128/139/42/42 as actual n.
- Do not compute correlations during the count audit.
- Do not create a cleaned analytical dataset in this sprint.
- Do not impute missing values.
- Do not pool Turner and YSI.
- Do not pool Mendota and Buffalo Pound.
- Do not use species-level primary endpoints.

## 12. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No analysis is authorised until the required human decisions and explicit D-15 approval are recorded.
