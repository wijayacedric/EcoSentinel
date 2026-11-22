# EcoSentinel

EcoSentinel is a SciFest@College environmental science research project investigating whether persistent changes in relationships between freshwater environmental variables can provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates.

## Research question

> Can persistent changes in relationships between freshwater environmental variables provide earlier warning of cyanobacterial blooms than conventional monitoring, at comparable false-alarm rates?

Negative or inconclusive results are scientifically valuable and must be reported honestly.

## Repository structure

```text
EcoSentinel/
  data/
    raw/                  # Original source data (never modified)
    external/             # External reference data (if added)
    processed/            # Derived analysis-ready data (generated)
  documentation/          # Protocols, methods, audit notes
  notebooks/              # Exploratory notebooks
  research/
    literature/           # Literature notes/references
    research_notes/       # Working research notes
  results/
    figures/
    tables/               # Generated audit/report tables
  src/                    # Canonical scripts/modules
  tests/                  # Validation tests
  archive/                # Archived/backups (not canonical)
  environment.yml
```

## Data

Current dataset: **Buffalo Pound Lake buoy/meteorological dataset (2014–2021)** from FRDR.

- Citation: `data/raw/buffalo_pound/FRDR_dataset_1095_download_621_202611201621/CITATION.txt`
- License: CC BY 4.0 (`LICENSE.txt`)
- README: `README.txt`
- Flags: `data_flags.csv`

Raw data must never be modified.

## Environment

```bash
conda env create -f environment.yml
conda activate ecosentinel
```

Or use an existing local env with pandas/numpy/scipy/scikit-learn/statsmodels/matplotlib.

## Reproduce quality audit

```bash
conda activate ecosentinel
python src/quality_audit.py
```

Outputs are written to `results/tables/`.

## Tests

```bash
conda activate ecosentinel
python -m pytest -q
```

## Scientific standards

- No fabricated observations or manufactured bloom events.
- No temporal leakage; no tuning on test events.
- Compare methods at comparable false-alarm rates.
- Distinguish correlation from causation.
- Document limitations, missingness, and quality flags.

See `documentation/SCIENTIFIC_PROTOCOL_DRAFT.md` for the current protocol draft.