# Gate 2H — Executable Evaluation Prototype

**SYNTHETIC/SOFTWARE TESTING ONLY.** Not empirical EcoSentinel findings. Not for confirmatory performance claims. Gate 2 remains NOT APPROVED.

Provisional software semantics are implemented for synthetic testing only; they do not constitute scientific protocol approval.

## Structure
- `prototype/` — modular evaluation prototype
- `tests/` — unittest suite
- `derived/` — synthetic validation outputs

## Reproducible commands

Run unit/scenario tests:

```bash
PYTHONPATH=research/evidence/gate2h python3 -m unittest discover -s research/evidence/gate2h/tests -p 'test_gate2h.py'
```

Run synthetic validation summary (non-destructive; requires explicit output path):

```bash
PYTHONPATH=research/evidence/gate2h python3 research/evidence/gate2h/prototype/run_synthetic_validation.py --out /tmp/gate2h_summary.json
# To overwrite an existing file intentionally:
# ... --out research/evidence/gate2h/derived/synthetic_validation_summary.json --force
```

## Guardrails
- No real biological labels.
- No Buffalo Pound confirmatory evaluation.
- No matched-FAR/lead-time superiority claims.
- `EvaluationConfig.allow_unverified_exposure` is forced False.
- `max_warning_horizon` is required for evaluation; no scientific default is invented.
- Unknown observations are never silently classified as non-event.
