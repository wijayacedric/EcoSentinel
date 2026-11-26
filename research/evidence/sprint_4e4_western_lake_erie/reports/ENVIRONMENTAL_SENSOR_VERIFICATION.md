# Environmental Sensor Verification — Western Lake Erie (Sprint 4E.4)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Verification status

**Raw-file inspection: NOT COMPLETED** due NCEI 503. Below separates literature-described fields (Boegehold 2023) from verified raw-file facts.

## Literature-described measurements (NOT raw-file verified)

| Category | Variables (paper-described) | Sampling type | Raw-file verified? |
|---|---|---|---|
| CTD/physico-chemical | Conductivity, temperature, DO, beam attenuation, transmission, PAR | Discrete in situ CTD casts at sampling events | No |
| Optical/physical | Secchi depth, turbidity, CDOM, DOC, POC/PON, TSS, VSS | Discrete sampling/lab analysis | No |
| Nutrients | TP, TDP, SRP, ammonium, nitrate+nitrite, urea | Discrete sampling/lab analysis | No |
| Pigments/toxins | Chlorophyll a, phycocyanin, particulate/dissolved microcystins | Discrete sampling/lab analysis | No |
| Meteorological | Wind speed, wave height | Sourced from nearby buoys (THLO1, GLOS Toledo Intake 45165) per paper | No |

## High-frequency vs discrete

- **Discrete:** The primary GLERL/CIGLR monitoring dataset is described as weekly/biweekly ice-free-season sampling at fixed stations. It should **not** be described as high-frequency biological/environmental monitoring.
- **Potentially high-frequency:** THLO1 and GLOS 45165 are buoy platforms mentioned by the paper for wind/wave context; their actual variables, resolution, depth, coverage, and suitability for pairing were **not verified** in this sprint.

## Raw-file checks required

Exact column names, units, sampling intervals, sensor locations/depths, timestamp conventions, missingness, instrument changes, QC flags, and licence conditions.
