# Mendota Metadata Feasibility Update

**Date:** 2026-11-23T23:27:42.541908+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Status: metadata-only; no raw-file verification

## New/updated metadata findings

### knb-lter-ntl.88.31 (phytoplankton)
- 4 Madison lakes: Mendota, Monona, Wingra, Fish.
- Mendota: composite whole-water 0-8 m; glutaraldehyde preservation; PhycoTech slides.
- Sampling: **biweekly** ice-free late March/April-early September, then every 4 weeks through late November.
- Coverage: 1995-01-24 to 2020-12-31.
- Taxonomic updates Feb 2013 (name changes, genus-to-species revisions).
- Data bytes: auth-blocked (CN object 404; PASTA 403).

### knb-lter-ntl.129.42 (HF meteo/metabolism; new metadata fetched)
- Coverage: **2006-06-26 to 2025-12-31** (metadata; not raw-verified).
- 1-minute data; daily/hourly/high-resolution tables; sensor list table.
- Variables include air temp, RH, wind, PAR, chlorophyll (Turner/YSI), phycocyanin (Turner/YSI), DO (raw/sat/wtemp), pCO2.
- Not all sensors deployed each season; sensor list is a separate entity.
- Data bytes: auth-blocked.

### knb-lter-ntl.130.29 (buoy temperature)
- 1-minute thermistor chain; 16 data tables; 2006-2019.
- 2015 high-resolution entity missing from CN (bounded gap).
- Data bytes: auth-blocked.

### knb-lter-ntl.415.2 (Microbial Observatory)
- Handheld probes at central Deep Hole (43°05'58.2"N 89°24'16.2"W).
- 2006-2014 compiled temp/DO only; 2014-2019 YSI Pro Plus temp/DO/pH/conductance.
- Sampling frequency not stated; data bytes auth-blocked.

## What metadata resolves

- Mendota has a long-term independent microscopy endpoint (88.31) and a modern 1-minute multivariate predictor dataset (129.42) with phycocyanin/DO.
- Sampling frequency for 88.31 is biweekly ice-free, 4-weekly late season.
- Sensor changes are documented via a sensor-list entity (not accessible).
- 130.29 is temperature-only; 415.2 is routine handheld physico-chemical.

## What metadata cannot resolve

- Raw counts/biovolume/biomass values, units, detection limits, QC flags, missingness.
- Actual station/depth/time alignment for paired analysis.
- Whether 88.31 Mendota subset is directly isolatable and consistent.
- 129.42 raw sensor changes/calibration and data completeness.
- 130.29 2015 gap materiality.
- Licence at package level (CC BY per NTL page, not raw-verified).

## Feasibility

Mendota is **metadata-consistent with the strongest potential design**: multi-decade biweekly independent microscopy + modern 1-minute multivariate predictors incl. phycocyanin and DO. It remains **CONDITIONAL**, not selected, because raw data are auth-blocked and no file-level audit is possible.

## Precise access barrier

EDI PASTA requires authorised authentication; no API key in environment; CN serves metadata but not public data bytes. A user-authorised EDI API key or authorised portal download is required.
