# Sprint 4L.20 — Protocol Reconciliation and Viability Gate

**Date:** 2026-11-26  
**Status:** Decision package. **PROTOCOL NOT APPROVED. D-15 NOT APPROVED. ANALYSIS NOT AUTHORISED.**  
**Recommendation:** Reduce Stage 1 to a **Mendota-only, Turner-era, P2-primary/P1-secondary exploratory measurement audit**; remove Buffalo Pound from Stage 1.

---

## 1. What this package decides

The package answers four questions:

1. Can the current protocol be approved as written? **No.** It contains internal contradictions and QC rules contradicted by later evidence.
2. Should Buffalo Pound remain in Stage 1? **No.** Remove it; preserve it for future/Stage 2 work.
3. Is Mendota strong enough to stand alone? **Yes, conditionally**, as a limited exploratory measurement audit, not validation or early warning.
4. Is the result sufficiently original/competition-suitable? **No, not award-leading.** It is suitable only for a modest school/regional measurement audit.

---

## 2. Final recommendation

**PATH 3 — Mendota-only exploratory research.**

> **Among sampled dates in Lake Mendota during the Turner fluorometer era (2006–2019), what is the direction and magnitude of the rank association between daily mean surface phycocyanin fluorescence (0.5 m) and microscopy-derived cyanobacteria biovolume (0–8 m composite), and how does chlorophyll fluorescence compare descriptively?**

- **P2 phycocyanin:** primary.
- **P1 chlorophyll:** secondary descriptive comparator.
- **Turner only:** no YSI-era integration.
- **Mendota only:** Buffalo Pound removed.
- **Descriptive only:** Spearman rho, n, influence diagnostics, reduced sensitivities.
- **No validation, calibration, agreement, prediction, bloom detection or early warning.**

If the project owner requires an award-leading original contribution, **pause** rather than proceed with this design.

---

## 3. Key findings

### Protocol

- The current protocol is 4L.14; it is **PROPOSED — NOT APPROVED**.
- It is internally inconsistent: P3/P4 are called primary in §4.2 but recommended for downgrade in §1/§5/§7.2.
- It retains H without a documented range, retains negative RFU as valid, retains >100 RFU as quantitative, excludes B7 automatically, and uses a withdrawn coverage rule.
- The 4L.14 addendum proposed fixes, but they were **not applied**.
- The station rule and sensor-era wording also conflict with the addendum.

### Buffalo Pound

- Two separate datasets: buoy (FRDR, CC BY 4.0) and biology (Borealis, CC BY-NC-SA 4.0).
- Duplicate/`REP` semantics, biomass derivation, B7 retention, negative/>100 RFU, coverage, time zone and sample times unresolved.
- Two seasons; sensor missed an autumn *Planktothrix* bloom in the published record.
- The scientific gain (a depth-aligned contrast) does not justify the cost.
- **Remove from Stage 1.**

### Mendota

- Strongest dataset: NTL-LTER, CC BY 4.0, 0.5 m Turner sensors, 0–8 m integrated microscopy, 128/139 upper bounds.
- Critical limitation: surface point vs 0–8 m composite; no depth-resolved biology.
- Biology is biweekly, date-only, taxonomically non-stationary; detection-conditioned.
- Turner-only is coherent; YSI era too small.
- **Retain as limited exploratory audit.**

### Originality

- **Low.** Cotterill et al. (2019) already compared Cyclops-7 PC with cyanobacteria biovolume and found weak/variable relationships.
- 2017/2018 Slovenian studies compared PC/CHL sensors with biovolume.
- Loisa 2015, Brient 2008, Kong 2013, Hodges 2017, Levi 2024, Painter 2022.
- Mendota already has high-frequency PC, forecasting and EWS literature.
- The proposed audit is a local case study, not a new method.

### Competition

- SciFest@College 2027: entry deadline 11 March 2027; fairs April–June.
- **Suitable but unlikely to be award-leading.**
- If award-leading is the goal, pause or pursue a qualified Stage 2 dataset.

### Stage 2

- Original early-warning ambition remains unqualified.
- Mendota fails biweekly/depth requirements; Buffalo Pound fails two-season/provenance.
- Müggelsee is the strongest public candidate but access/event definition/calibration/co-location are unresolved.
- No Stage 2 dataset qualified.

---

## 4. File guide

| File | Purpose |
|---|---|
| `SPRINT_4L20_EXECUTIVE_DECISION.md` | Final recommendation, exact question, what survives/removed, next action |
| `CURRENT_PROTOCOL_RECONSTRUCTION.md` | Component-by-component reconstruction and ambiguities |
| `PROTOCOL_CONTRADICTION_MAP.csv` | Every protocol/evidence contradiction with recommended replacement |
| `QC_RULE_RECONCILIATION.md` | Rule-by-rule QC disposition and proposed Mendota-only QC |
| `BUFFALO_POUND_STAGE1_DECISION.md` | Why Buffalo Pound is removed |
| `MENDOTA_STANDALONE_VIABILITY.md` | Mendota scientific meaning, depth, sampling, eras, verdict |
| `ESTIMAND_HIERARCHY_RECOMMENDATION.md` | P2 primary/P1 secondary; P3/P4 removed |
| `ORIGINALITY_AND_PRIOR_ART_REASSESSMENT.md` | Direct prior art and low-originality verdict |
| `COMPETITION_STRATEGY_REASSESSMENT.md` | SciFest 2027 context and realistic verdict |
| `STAGE2_EARLY_WARNING_REQUIREMENTS_REASSESSMENT.md` | Strengthened Stage 2 requirements; Müggelsee |
| `ADVERSARIAL_REVIEW_4L20.md` | Fresh ecologist/statistician/judge critiques |
| `DECISION_DEPENDENCY_MAP.md` | D-01–D-15 dependencies and gates |
| `NEXT_ACTION_PLAN.md` | Prioritised plan, timeline, stop rules |
| `UPDATED_MISSING_EVIDENCE_REGISTER.csv` | 23 unresolved evidence items |
| `UPDATED_CONTRADICTORY_EVIDENCE_REGISTER.csv` | 18 contradictions/resolutions |
| `UPDATED_SOURCE_REGISTER.csv` | 49 sources with evidence grades |
| `EXTERNAL_SEARCH_LOG.md` | Search routes, findings, inaccessible sources |
| `EVIDENCE_SHA256_REGISTER.csv` | Hashes of every content file |
| `EVIDENCE_SHA256_REGISTER.csv.sha256` | Detached register checksum |
| `INTEGRITY_VERIFICATION.md` | Verification result and commands |

---

## 5. What is complete

- Protocol reconstruction and contradiction map.
- QC rule reconciliation.
- Buffalo Pound removal decision and rationale.
- Mendota standalone viability assessment.
- Estimand hierarchy.
- Prior-art reassessment.
- Competition reassessment.
- Stage 2 requirements reassessment.
- Fresh adversarial review.
- Decision dependency map and next-action plan.
- Missing/contradictory evidence registers.
- Source register and search log.
- Integrity files.

## 6. What is not complete

- D-13 owner decision.
- Protocol v2.
- Independent reviews.
- Count audit.
- D-01–D-14 approvals.
- D-15 approval.
- Licence/competition review.
- Student contribution statement.
- Analysis.
- Stage 2 access/qualification.

---

## 7. Governance

| Item | Status |
|---|---|
| Research direction | **CONTINUE — NARROWED RESEARCH QUESTION** |
| Protocol | **PROPOSED — NOT APPROVED** |
| Gate 2 | **PAUSED / NOT APPROVED — OPTION C** |
| D-01–D-15 | **OUTSTANDING — NOT APPROVED** |
| D-15 | **NOT APPROVED** |
| Analysis | **NOT AUTHORISED** |

No decision was approved by this package.

---

## 8. Integrity verification

From this directory:

```bash
cd /Users/cedricbw/Documents/EcoSentinel/research/evidence/sprint_4l20_protocol_reconciliation_and_viability_gate
shasum -a 256 -c EVIDENCE_SHA256_REGISTER.csv.sha256
```

Verify every registered file:

```bash
cd /Users/cedricbw/Documents/EcoSentinel
python3 - <<'PY'
import csv, hashlib
from pathlib import Path
base = Path('research/evidence/sprint_4l20_protocol_reconciliation_and_viability_gate')
bad = 0
for row in csv.DictReader(open(base/'EVIDENCE_SHA256_REGISTER.csv', newline='', encoding='utf-8')):
    p = Path(row['path'])
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
        bad += 1
        print('MISMATCH', row['path'])
print('mismatches', bad)
PY
```

Integrity verifies file identity, not scientific truth.

---

## 9. Single next action

**Record the D-13 scope decision: accept the Mendota-only P2-primary/P1-secondary exploratory audit, or pause.**

Do not start analysis. Do not run the count audit. Do not approve D-15.
