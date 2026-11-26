# Schedule Recovery Plan

**Sprint:** Schedule Recovery Sprint 1  
**Date:** 2026-11-22  
**Principle:** Recover time only through safe, scientifically independent work. No Gate 2 resumption, no real-data modeling, no fabricated labels.

## Completed during this sprint

| Item | Status | Evidence | Dependencies |
|---|---|---|---|
| Repository reconnaissance and baseline established | Completed | Git status inspected; test baselines run | None |
| Gate 2H prototype baseline verification | Completed | 51/51 tests pass (`research/evidence/gate2h/tests/test_gate2h.py`) | Python stdlib |
| Existing quality-audit tests baseline verification | Completed | 9/9 pass in ecosentinel env (`tests/`) | ecosentinel conda env |
| Gate 2G intake validator strengthened (read-only, no biological inference) | Completed | `research/evidence/gate2g/scripts/validate_intake.py` | None |
| Gate 2G intake synthetic test suite added | Completed | 5/5 pass (`research/evidence/gate2g/data_intake/tests/test_validate_intake.py`) | Python stdlib |
| Sprint reports created | Completed | `research/reports/schedule_recovery_sprint_1/*` | None |

## Ready to execute immediately (safe, no external approval)

| Priority | Task | Why safe | Dependency | Output |
|---|---|---|---|---|
| P1 | Add XLSX validation smoke test in ecosentinel env (if openpyxl present) | Synthetic fixture only; read-only | ecosentinel env/openpyxl | Test result logged |
| P1 | Create intake manifest/provenance checklist script (read-only report generator) | Operational integrity only | None | Script + tests |
| P1 | Add CI-local reproducible command doc (`make test`/script) without changing deps | Documentation/ops | None | README/docs update |
| P2 | Package literature/comparator exports for review (already done for Claude package) | Export-only | None | Verified archives |
| P2 | Run static checks/lint if configured in env | Quality only | Tool availability | Logged report |
| P2 | Prepare "data arrival checklist" runbook for first institutional response | Operational readiness | None | Runbook in sprint/docs dir |
| P2 | Add tests for Gate 2G summarize_existing_sensor_audit.py (synthetic/read-only) | No scientific decisions | None | Test file |
| P3 | Improve README with env/test commands for Gate 2H and Gate 2G intake tests | Documentation | None | README patch (human review) |

## Blocked by external evidence or human approval

| Item | Blocker | Required before action | Owner/decision |
|---|---|---|---|
| Gate 2 evidence adjudication | Independent biological event labels and defensible non-event exposure insufficient | Institutional/researcher responses; human scientific adjudication | Human/ChatGPT |
| Any real-data model training/evaluation | Gate 2 not approved; protocol/evaluation rules not approved | Gate 2 approval + human-approved protocol decisions | Human/ChatGPT |
| Sending follow-up data requests | External communication requires explicit authorization | Human authorization and review | Human |
| Accepting data licenses/agreements | Legal/access terms require human review | Human review | Human |
| Threshold/horizon/alert-rule selection for real evaluation | Scientific methodology decision | Human-approved protocol | Human/ChatGPT |
| Competition submission claims | Require verified current requirements and no overclaiming | Human review; verified competition info | Human |
| Commit/push/publish | Explicit user instruction required | Human instruction | Human |

## Avoidable-delay observations

- **Parallelizable now:** intake tooling tests, docs, export packaging, static checks, runbook prep - all independent of Gate 2.
- **Avoid repeated work:** keep one technical remediation register and one sprint report directory; do not create overlapping status docs.
- **Trigger on data arrival:** checksum -> provenance manifest -> validate_intake report -> human review -> mapping/template decision. No modeling.
- **Do not wait for Gate 2 to improve tooling:** safe software readiness can proceed now.
