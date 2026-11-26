# Gate 2G — Methods and Decisions Register

**Project:** EcoSentinel  
**Date:** 2026-11-22  
**Status:** Decision register only. **No decisions finalized. No Gate 2/3 approval. No labels/modeling.**

## 1. Purpose

Identify methodological decisions that must be specified, reviewed, and human-approved before any confirmatory Gate 2/3/4 work. This register records unresolved options, risks, and required evidence; it does not select options.

## 2. Decision status legend

- **Unresolved:** requires human review/approval.
- **Blocked by evidence:** cannot be responsibly finalized until missing biological evidence arrives.
- **Drafted:** proposal exists in protocol draft but not approved.

## 3. Unresolved decisions

| ID | Decision | Status | Options / considerations | Risks if decided poorly | Required before finalization |
|---|---|---|---|---|---|
| M1 | Biological-only event definition | Blocked by evidence | Taxonomy/biomass/biovolume thresholds; toxin criteria; composite biological criteria; expert-reviewed biological definition | Circularity, arbitrary thresholds, post-hoc tuning | Accessible record-level biological data; human Gate 2/3 review |
| M2 | Candidate vs approved event distinction | Drafted | Candidate observation, candidate interval, approved event; explicit criteria for promotion | Inflating event count; treating sparse samples as events | Approved definition; provenance/audit trail |
| M3 | Interval-censored observation handling | Drafted | Interval-censored survival/time-to-event framing; uncertainty windows; exclude ambiguous intervals | False precision in onset/termination/lead time | Sampling-gap analysis; approved censoring rules |
| M4 | 2019-07-17 Painter anomaly handling rule | Unresolved | Exclude from interval boundaries; treat as flagged uncertain observation; sensitivity analysis only after approval | Silent bias, unjustified data cleaning | Data-owner clarification or pre-approved handling rule |
| M5 | Non-bloom exposure definition | Blocked by evidence | Confirmed biological non-dominant/negative observations with max-gap rule; unknown otherwise | False negatives/denominator inflation; invalid FAR | Biological data with adequate coverage; approved exposure rule |
| M6 | Spatial alignment (buoy vs intake/lab site) | Unresolved | Same-site only; spatial tolerance with uncertainty; exclude misaligned sources | Spatial mismatch treated as temporal signal | Location metadata for all biological sources |
| M7 | Temporal alignment/window | Drafted | Nearest sample within max gap; same-day; interval overlap; no alignment across long gaps | Spurious alignment; leakage | Timestamp/timezone/depth metadata; gap policy |
| M8 | Independent event separation | Unresolved | Minimum separation gap; biological return-to-non-event; merge/split rules | Double-counting same event; pseudoreplication | Event definition; sampling frequency evidence |
| M9 | Training/validation/test split design | Drafted | Temporal split by season/year; event-grouped CV; held-out years | Leakage, optimistic estimates | Sufficient independent events/years after Gate 2 approval |
| M10 | Matched-FAR comparison design | Blocked by evidence | FAR targets; operating-point selection on validation only; event-level FAR denominator | Unfair comparison; meaningless "earlier" claim | Defensible exposure denominator; approved baseline set |
| M11 | Missed-event evaluation | Blocked by evidence | Event-level recall; severity-weighted miss; uncertainty bounds | Misleading sensitivity claims | Approved events and exposure |
| M12 | Lead-time definition and censoring | Drafted | Time from alert to event onset interval; right/left censoring; minimum lead-time | Overstated warning time; ambiguous onset | Interval-censored event bounds |
| M13 | Baseline conventional monitoring definition | Drafted | Chlorophyll/phycocyanin/turbidity/DO thresholds; operational rules; lab-confirmation proxy where available | Straw-man baseline | Baseline data availability; human review |
| M14 | Handling B7 fouling/pigment spikes | Drafted | Primary exclude/sensitivity include; flagged sensitivity analysis | Fouling-driven false alarms or missed events | Pre-approved sensitivity plan |
| M15 | Handling M/C/A2/A3/A4/A5/A6/B6 flags | Drafted | Per-flag rules in protocol; no silent mixing of raw/corrected conductivity | Data-quality leakage/bias | Implementation tests; protocol approval |
| M16 | Uncertainty estimation | Unresolved | Bootstrap by event/year where feasible; interval-censored bounds; descriptive only when n small | Overconfident claims with tiny n | Adequate event count; approved design |
| M17 | External/institutional data use terms | Unresolved | Per-source license/acknowledgement/restrictions | Unauthorized use/redistribution | Human/legal review of received terms |
| M18 | Gate 2 approval criteria | Unresolved | Minimum independent events, coverage, non-bloom exposure, independence, protocol approval | Premature Gate 2 approval | Human review with full evidence package |

## 4. Decisions explicitly not made in Gate 2G

- No bloom/non-bloom labels assigned.
- No event thresholds selected.
- No non-bloom exposure rule approved.
- No train/test split finalized.
- No FAR target selected.
- No baseline promoted as confirmatory comparator.
- No Gate 2/3 approval granted.

## 5. Recommended human review package (when evidence arrives)

1. Data provenance and license/terms review.
2. Independence assessment (method, location, time, sensor separation).
3. Event definition workshop/review (biological-only).
4. Interval-censoring and anomaly-handling rules.
5. Non-bloom exposure and FAR denominator rules.
6. Alignment and leakage-prevention checklist.
7. Evaluation protocol approval before any modeling.