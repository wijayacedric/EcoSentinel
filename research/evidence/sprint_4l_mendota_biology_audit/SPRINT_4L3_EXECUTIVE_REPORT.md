# Sprint 4L.3 Executive Report — Mendota Phytoplankton Acquisition, Structural Audit and Evidence Review

**Date:** 2026-11-23T23:58:36.852965+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Status: PARTIALLY COMPLETE — raw acquisition blocked by missing EDI API key.**

## 0. Project instruction update

- No `AGENTS.md` existed in the repository or parent directories.
- Created **`/Users/cedricbw/Documents/EcoSentinel/AGENTS.md`** with the required permanent section "Mandatory Research and Execution Standards (Permanent)" covering extensive search, strict search depth, no token-budget shortcuts, and evidence/scientific integrity.
- No other governance/protocol document was modified.

## 1. Pre-acquisition verification

- Package: `knb-lter-ntl.88.31`.
- Entity: `f2de15b2fff6ae962a04c150c0a1c510` — confirmed in EML and ORE resource map.
- Expected size: **2,448,830 bytes** — confirmed.
- EML objectName: `ntl88_v13.csv`; EML MD5: **`a0363cc7fdfd6c12889750fea27bd542`**.
- Output location: inside the EcoSentinel repository.
- **New version finding:** `knb-lter-ntl.88.32` (DOI `10.6073/pasta/19888a181707748619d28cad7ca5ff74`, published 2026-05-18) has the **same objectName/size/MD5** as 88.31. Data bytes are identical by size/MD5; metadata text differs.

## 2. Controlled acquisition attempt

Command attempted with the existing authenticated script:

```bash
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py \
  --package 88.31 --include-data \
  --entity f2de15b2fff6ae962a04c150c0a1c510 \
  --max-bytes 3000000 \
  --outdir research/evidence/sprint_4l_mendota_biology_audit/acquisition
```

Result: **exit 2**, `EDI_API_KEY is not set`; no network request, no data bytes, no secret exposure. No EDI API key in environment or documented Keychain item. **No alternative acquisition route was improvised.**

## 3. Integrity and provenance

- No raw biological file was acquired, so actual size/SHA256/MD5 of the CSV **cannot be verified**.
- Expected integrity values are known from EML: 2,448,830 B, MD5 `a0363cc7fdfd6c12889750fea27bd542`.
- Metadata files: 88.31 EML 27,408 B SHA256 `c96ddc...`; 88.32 EML 33,523 B SHA256 `a4191d...`.
- Package DOI/revision/entity identity verified; acquisition timestamp/output path exist only for the failed attempt log (no file).

## 4. Structural audit (metadata-level)

- One data table; **15 columns**: lakeid, year4, sampledate, sta, depth_range, division, taxa_name, gald, cells_per_nu, nu_per_ml, cells_per_ml, biovolume_conc, biomass_conc, relative_total_biovolume, genus.
- Coverage: 1995-01-24 to 2020-12-31; 4 lakes; Mendota 0–8 m composite; biweekly ice-free, 4-weekly late season, occasional winter.
- No raw row count, Mendota-specific count, date distribution, missingness, duplicates, or taxonomic counts could be computed.
- Methods: Utermöhl inverted microscopy; PhycoTech; 3 slides/sample; species-level; geometric biovolume; biomass conversion; February 2013 taxonomic updates; no QC flags or detection limits in schema.

## 5. External evidence review (selected)

- **Carey et al. 2016**: 1995–2010, 0–8 m composite, >400 natural units/sample, same taxonomist; biovolume up to 15 units/species. Supports methods and consistency.
- **Carpenter et al. 2020**: 1-min phycocyanin/chlorophyll 2008–2018, Turner Cyclops 7 at 1 m, single station; sensor proxy, two states. Shows Mendota already has HF cyanobacteria proxy work.
- **Beal et al. 2022**: 1995–2018 cyanobacteria biomass, season-ahead forecast; prior Mendota forecasting.
- **O'Brien et al. 2023**: EWS generally weak on empirical lake data; multivariate weakly superior; caution.
- **Taxonomic bias/Lake Zurich/intercalibration**: long-term taxonomy has non-zero bias and consistency risks; single analyst can reduce but not eliminate variation.
- **Temporal resolution**: weekly/biweekly sampling can miss short blooms; at least twice-weekly is better for precise timing.
- **PhycoTech**: Ann St. Amand sole enumerator; 95%+ in-house QA claim; died Oct 2023. Self-reported, not independent validation.

## 6. Feasibility

- Genuine independent biological endpoint: **yes** (metadata; raw unverified).
- 0–8 m composite vs 0.5 m sensor: **major depth mismatch**.
- Biweekly–monthly biology: supports **seasonal/multi-week**, not daily, warning.
- Non-bloom exposure: **plausible but undefined**; no labels.
- Method/taxonomy changes: **need harmonisation**; no QC/detection limits.
- Early-warning evaluation: **potentially feasible at seasonal/multi-week scale** over 25 years, but not established; raw data and protocol needed.

## 7. What the dataset actually establishes

- A long-term, species-level, microscopy-based phytoplankton record for four Madison lakes, with Mendota 0–8 m composite samples, cell counts, biovolume and biomass (metadata-verified; data bytes not acquired).
- It is measurement-independent of buoy pigment sensors and could serve as independent biological validation.

## 8. What it does not establish

- That the raw file contains complete, Mendota-only, consistent records.
- Detection limits, QC, missingness, duplicates, effective sample size.
- That a bloom/non-bloom exposure can be defended.
- That biweekly biology can support sub-weekly early warning.
- That the proposed method beats conventional monitoring.

## 9. Does it materially improve Mendota's suitability?

**Yes, conditionally.** It supplies the independent biological endpoint that greifensee lacks and that Lake Erie's pigments/toxins do not provide. But it does not remove the depth mismatch, biweekly resolution, taxonomy/QC, or Gate 2 protocol blockers.

## 10. Remaining Gate 2 blockers

1. No authorised raw data acquisition (EDI key).
2. No file-level audit (Mendota subset, missingness, duplicates, quality).
3. No defensible event/non-bloom definition.
4. No depth comparator for 0–8 m composite vs buoy point sensors.
5. No matched-FAR/leakage-resistant evaluation design approved.
6. Taxonomic harmonisation/QC/detection-limit documentation incomplete.
7. Licence confirmation at package level (CC BY indicated).

## 11. Final recommendation

**Continue investigating; retain as exploratory; do not reject.** The dataset is scientifically promising for seasonal/multi-week comparison with Mendota buoy data, but it is not confirmatory-ready and the raw file was not obtained. Re-run acquisition only after a user-authorised EDI key is available, then complete the raw structural audit.

**Gate 2 remains PAUSED / NOT APPROVED. No agent may independently authorise confirmatory research.**
