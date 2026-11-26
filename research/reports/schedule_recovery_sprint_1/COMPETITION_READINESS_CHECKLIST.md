# Competition Readiness Checklist

**Sprint:** Schedule Recovery Sprint 1  
**Date:** 2026-11-22  
**Rule:** No fabricated deadlines, requirements, eligibility rules, or result claims. Items marked Unknown require verification from official sources.

## 1. Verified project facts (repository-grounded)

| Item | Status | Evidence | Notes |
|---|---|---|---|
| Research question documented | Verified | `README.md`, `documentation/SCIENTIFIC_PROTOCOL_DRAFT.md` | Unchanged |
| Primary dataset documented | Verified | `README.md`, data citation/license files in `data/raw/buffalo_pound/...` | Buffalo Pound 2014–2021 |
| Raw data preservation rule documented | Verified | README/protocol | No raw-data modification observed |
| Gate 2 not approved / Option C exploratory | Verified | Gate 2 reports/register | Must not be overstated |
| Quality audit script and tests exist | Verified | `src/quality_audit.py`, `tests/test_quality_audit*.py`, 9/9 pass in ecosentinel env | Reproducible in env |
| Gate 2H synthetic prototype tests pass | Verified | 51/51 pass | Synthetic-only; not ecological validation |
| Gate 2G intake validator/tests exist | Verified | `research/evidence/gate2g/scripts/validate_intake.py`, 5/5 tests pass | Readiness only |

## 2. Competition targets (require verification)

| Competition | Requirement / deadline / eligibility | Status | Source needed | Action |
|---|---|---|---|---|
| SciFest@College (assumed target from project context) | Current year deadlines, submission format, eligibility, judging criteria | **Unknown / not verified in this sprint** | Official SciFest@College 2026 rules/deadline page; local coordinator confirmation | Human verify before any submission claim |
| Any other competition | Eligibility, deadlines, ethics/data rules, submission requirements | **Unknown** | Official competition documentation | Do not assume |

## 3. Readiness checklist (safe, evidence-based)

| Area | Item | Status | Evidence / Gap |
|---|---|---|---|
| Documentation | README explains project/question/data/repro | Partial | README exists; could add Gate 2H/Gate 2G test commands |
| Documentation | Protocol draft exists | Partial | Draft exists; dependent Gate 3 decisions unresolved |
| Reproducibility | Environment file exists | Verified | `environment.yml` |
| Reproducibility | Tests runnable and documented | Partial | Tests pass in documented envs; base env lacks pytest/pandas |
| Integrity | Raw data unchanged | Verified (this sprint) | No raw data edits made |
| Integrity | No overclaiming of validation/results | Needs ongoing review | Reports must clearly state exploratory/synthetic-only where applicable |
| Evidence | Independent biological validation | **Blocked** | Gate 2 not approved |
| Evidence | Confirmatory model evaluation | **Blocked** | No real-data modeling permitted |
| Submission | Current competition requirements verified | **Unknown** | Official source required |
| Submission | Final figures/tables/slides/poster | Not assessed | Depends on verified requirements and approved scientific status |

## 4. Safe documentation improvements allowed now

- Add reproducible command sections for Gate 2H and Gate 2G tests.
- Add "current status/blockers" section to README or docs index (without overclaiming).
- Create a checklist of required submission artifacts once official requirements are verified by human.
- Ensure all reports label synthetic outputs clearly.

## 5. Do not claim

- "Validated early-warning system"
- "Confirmed research gap/originality"
- "Gate 2 approved" / "ready for confirmatory modeling"
- Any competition deadline/eligibility not verified from official source
