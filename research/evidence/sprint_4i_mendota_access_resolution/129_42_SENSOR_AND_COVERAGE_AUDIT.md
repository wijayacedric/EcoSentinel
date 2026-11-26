# 129.42 Sensor and Coverage Audit

**Date:** 2026-11-23T23:32:06.599235+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Package identity

- Package: `knb-lter-ntl.129.42` (current metadata revision; supersedes 129.9).
- Title: North Temperate Lakes LTER: High Frequency Data: Meteorological, Dissolved Oxygen, Chlorophyll, Phycocyanin - Lake Mendota Buoy 2006 - current.
- Repository/custodian: EDI / NTL-LTER, UW-Madison.
- Metadata: public DataONE CN object, 146,471 B, SHA256 `c853f0df32f67c49ac47084d4c6f656100b9d014f90da869f0f47ef0db7ebb97`.
- Data bytes: **not obtained** (CN 404; PASTA 403).

## Temporal coverage and resolution

- EML temporal coverage: **2006-06-26 to 2025-12-31**.
- Data collected every **minute**; daily and hourly averages derived.
- Buoy removed under ice (typically Dec-Apr); ice-free deployment.
- **Important:** 2006-2025 is package-level. Not all sensors deployed each season; per-variable coverage is **not resolved** from metadata alone.

## Entities (4)

1. Daily meteorological and metabolism data — 38 attributes.
2. Hourly meteorological and metabolism data — 39 attributes.
3. High-resolution (1-minute) meteorological and metabolism data — 39 attributes.
4. **List of sensors used since 2006** — attributes: `parameter, sensor_mfg, sensor_model, date_began, date_ended` (5). Rows are **not accessible** without authorization.

## Available channels (EML)

- Meteorology: air temp, relative humidity, wind speed/direction, PAR above/below.
- Biology-relevant: chlorophyll RFU (Turner and YSI), phycocyanin RFU (Turner and YSI), DO raw/saturation/water temp, pCO2.
- Flags accompany variables; sensor eras differ (Turner vs YSI; 2019+ additions include YSI chlorophyll/phycocyanin, specific conductivity, pH, turbidity, fDOM per SSEC documentation).
- This is **sensor-proxy** biological information, not independent cell counts/biomass.

## Coverage interpretation

- The title "2006-current" describes the package, not every channel.
- Old Turner chlorophyll/phycocyanin channels may span earlier years; YSI-era channels are newer.
- The sensor-list table is the authoritative way to resolve per-channel start/end, but its rows require EDI data access.
- Therefore: **2006-2025 coverage is metadata-verified at package level; per-variable coverage remains unresolved.**

## Relation to other packages

- 129.9 = older revision of the same buoy meteo/DO/chlorophyll/phycocyanin package (EML coverage 2006-2012).
- 130.29 = separate high-frequency water-temperature profile package (2006-2019), same buoy site.
- 415.2 = Microbial Observatory handheld profiles at the same Deep Hole (2006-2019), not the buoy.
- 88.31 = independent phytoplankton microscopy (1995-2020), not a sensor package.

## Access implication

Authorized EDI access is required for the sensor list and observations. SSEC's public Metobs API provides 2019-2025 buoy data (no QC flags, different product), not a substitute for the EDI package or its 2006-2018 record.
