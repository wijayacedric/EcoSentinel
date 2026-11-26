# External Search Log — Mendota Phytoplankton 88.31

**Date:** 2026-11-23T23:58:36.852965+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Scope defined before searching

1. Dataset/package metadata and versioning (EDI, DataONE/PASTA, NTL, NSF PAR).
2. Sampling design and laboratory methods (NTL protocols, Utermöhl, PhycoTech).
3. Taxonomic identification/enumeration and long-term consistency.
4. Biovolume/biomass calculation and QC.
5. Temporal representativeness of discrete biological sampling vs high-frequency sensors.
6. Mendota cyanobacteria/early-warning prior art.
7. Conflicting evidence and limitations.

## Queries and sources inspected

| # | Query / route | Category | Sources inspected | Key finding | Status |
|---:|---|---|---|---|---|
| 1 | DataONE CN solr/sysmeta/ORE for `knb-lter-ntl.88.31` and `.32` | metadata/version | CN sysmeta; ORE; EML 88.31; EML 88.32 | 88.31 (2022) and 88.32 (2026) share the same objectName/size/MD5; 88.32 metadata differs | Verified metadata |
| 2 | DOI `10.6073/pasta/19888a181707748619d28cad7ca5ff74` redirect | version | DOI resolver | Redirects to `knb-lter-ntl.88.32` | Verified redirect |
| 3 | EDI/PASTA metadata/data endpoints | access | PASTA | Data/auth blocked; no key in environment | Access blocked |
| 4 | "North Temperate Lakes LTER phytoplankton sampling protocol Utermohl PhycoTech biovolume" | methods | NTL Protocols page; NSF PAR record 10493157 | Biweekly summer/monthly non-summer; biovolume for ME/MO; archived slides | Inspected |
| 5 | "Lake Mendota phytoplankton long-term dataset 1995 PhycoTech microscopy species biovolume" | methods | NSF PAR; HELCOM; NERC guidance | Species-level Utermöhl; 0–8 m composite; biovolume methods | Inspected (HTML/snippets) |
| 6 | "Utermöhl method phytoplankton biovolume biomass conversion Hillebrand 1999" | methods | Hillebrand et al. 1999 refs; HELCOM; NERC | Geometric biovolume; biomass conversion assumptions | Inspected (abstracts/guidance) |
| 7 | Carey et al. 2016 wavelet paper (DOI 10.1093/plankt/fbv116) | methods/prior use | Full-text excerpts via search index; Carey PDF URL | Biweekly–monthly 1995–2010; 0–8 m composite; same taxonomist; >400 units; biovolume up to 15/species; data interpolated for wavelet only | Inspected excerpts |
| 8 | "Carpenter 2020 Stochastic dynamics of Cyanobacteria..." | prior art | Search-result abstract/methods excerpts; WUR record | 1-min phycocyanin/chlorophyll 2008–2018; Turner Cyclops 7 at 1 m; two states; single station; sensor proxy | Inspected abstract/methods |
| 9 | "Beal 2022 Variability of summer cyanobacteria abundance..." | prior art | Search-result full-text excerpts; NSF PAR abstract | 1995–2018; biovolume→biomass; season-ahead forecast; prior Mendota models | Inspected full HTML |
| 10 | O'Brien et al. 2023 Nature Communications | prior art/caution | Full HTML | EWS generally poor on empirical lake data; multivariate weakly superior; Mendota included | Inspected |
| 11 | "long-term phytoplankton monitoring taxonomic consistency..." | QC | Taxonomic bias 2022 abstract; Lake Zurich rejoinder; intercalibration 2024 | Taxonomic bias affects some metrics; total biovolume/cell density often robust; long-term consistency difficult; intercalibration CV 10–42% professionals, 4–19% same analyst | Inspected abstracts |
| 12 | "discrete phytoplankton sampling temporal resolution..." | temporal | "Hit or miss?" 2024 abstract; sensor validation 2023; sensor-based detection 2021 | Weekly/biweekly can resolve general composition but miss short blooms; twice-weekly better for bloom timing; sensors need lab validation | Inspected abstracts |
| 13 | "St. Amand PhycoTech Lake Mendota" | methods/QC | Search-result excerpts from PhycoTech info packet, staff page and Standard Methods memorial | Ann St. Amand was sole enumerator; 95%+ in-house QA claim; died 7 Oct 2023 | Inspected |
| 14 | "Lake Mendota phytoplankton species composition long-term changes..." | prior art | Carey 2016; PNAS invasions 2023; nitrogen fixation 2013 | Long-term seasonal succession; cyanobacteria ~70% biovolume 1995–2010; invasions shifted phenology | Inspected abstracts/excerpts |
| 15 | NTL protocols page | methods | https://lter.limnology.wisc.edu/protocols/ | Biweekly summer/monthly non-summer; phytoplankton biovolume ME/MO; protocol PDFs being revised | Inspected |

## Inaccessible / incomplete sources

- **EDI data bytes:** PASTA 403; DataONE CN data object 404; EDI portal login. No key.
- **Carpenter 2020 / Beal 2022 PDFs:** PDF parsing unavailable; HTML/full-text excerpts inspected instead.
- **NTL archived protocol PDF:** URL returned 404; current protocol page says protocols are being revised.
- **PhycoTech QA details:** company self-report; no independent audit report retrieved.
- **88.32 metadata:** retrieved; 88.32 data bytes not acquired.
- **Exact row counts / Mendota subset:** cannot be obtained without raw data.

## Conflicting evidence

- PhycoTech claims high consistency and 95%+ QA precision; independent literature on long-term phytoplankton series documents taxonomic consistency problems and interanalyst variability. Both are recorded; neither is treated as conclusive for this dataset.
- Carpenter 2020 finds high-frequency phycocyanin dynamics with two states; O'Brien 2023 finds EWS generally weak on empirical lake data. This cautions against assuming the proposed early-warning method will work.

## Why the search stopped

The defined categories were covered to the extent accessible: package metadata/versioning, sampling/lab methods, taxonomy/QC, biovolume/biomass, temporal resolution, prior art, and conflicting evidence. Further progress requires raw data and/or full-text PDF access, not more broad searching. This is not claimed as exhaustive literature coverage beyond the queries above.
