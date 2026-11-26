# External Search Log — Sprint 4L.5

**Date:** 2026-11-24T07:23:09.883291+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Source categories defined before searching

1. Original dataset/package metadata and version history.
2. NTL-LTER sampling/laboratory protocols and PhycoTech methods.
3. Cyanobacterial nomenclature/synonym authorities.
4. Biovolume/biomass/cell-density methods and long-term comparability.
5. Sampling frequency/temporal aliasing and sensor-proxy validation.
6. Mendota phytoplankton/cyanobacteria prior studies.
7. Existing project evidence (Sprints 4K, 4L.1, 4L.2, 4L.3, 4L.3C, 4L.3D).

## Queries and sources

| # | Query / route | Sources inspected | Key finding | Status |
|---:|---|---|---|---|
| 1 | EDI 88.31/88.32 metadata; DataONE CN | EML 88.31, EML 88.32, ORE, sysmeta | 88.31/88.32 share same data objectName/size/MD5; 88.32 metadata newer | Full primary metadata |
| 2 | NTL-LTER protocols page | https://lter.limnology.wisc.edu/protocols/ | Biweekly summer/monthly non-summer; phytoplankton biovolume ME/MO; archived slides | Full page |
| 3 | NSF PAR record 10493157 | https://par.nsf.gov/biblio/10493157... | 4 lakes, Mendota 0–8m composite, PhycoTech, Utermöhl, biweekly | Full record |
| 4 | Carey et al. 2016, J Plankton Res 38:27–40 | Search-index full-text excerpts; Carey PDF URL | 1995–2010, >400 natural units, same taxonomist, biovolume up to 15/species | Excerpts, not PDF parser |
| 5 | Carpenter et al. 2020, Limnol Oceanogr Lett 5:331–336 | Search-index abstract/methods; WUR record | 1-min phycocyanin/chlorophyll 2008–2018; Turner Cyclops 7 at 1m; sensor proxy | Excerpts |
| 6 | Beal et al. 2022, Lake Reserv Manage 39:37–52 | Search-index full-text excerpts; NSF PAR | 1995–2018 cyanobacteria biomass; season-ahead forecast | Excerpts |
| 7 | O'Brien et al. 2023, Nat Commun 14:7942 | Nature HTML | EWS generally poor on empirical lake data; multivariate weakly superior | Full HTML |
| 8 | "AlgaeBase Dolichospermum Anabaena synonym Cuspidothrix..." | AlgaeBase search-result records; direct AlgaeBase blocked by Cloudflare Turnstile | Cuspidothrix, Dolichospermum synonymy | Search records; direct pages inaccessible |
| 9 | "Woronichinia Coelosphaerium synonym..." | AlgaeBase records; HCB-1 Appendix A | Woronichinia naegeliana ← Coelosphaerium naegelianum; Planktothrix/Pseudanabaena crosswalk | HCB-1 full page; AlgaeBase search records |
| 10 | ITRC HCB-1 Appendix A | https://hcb-1.itrcweb.org/appendix-a/ | Full synonym crosswalk Table A-1; HCB morphology/toxin context | Full page |
| 11 | HELCOM phytoplankton guidelines | Search-result sections | Biomass preferred; abundance units/colonies not directly comparable; QC/intercalibration | Excerpts |
| 12 | CEMP phytoplankton monitoring guidelines | Search-result sections | Long-term methods must remain comparable; frequent sampling needed | Excerpt |
| 13 | Inter-lab comparison (2015) | Abstract | 2-fold differences in abundance/cell volume; carbon biomass CV 43% | Abstract |
| 14 | Taxonomic bias in freshwater phytoplankton (2022) | Abstract | Non-zero taxonomic bias; total biovolume/cell density often robust | Abstract |
| 15 | Lake Zurich long-term consistency rejoinder | Search-result summary | Taxonomic learning/detection-limit changes can create step changes | Excerpt |
| 16 | Intercalibration of freshwater phytoplankton (2024) | Abstract | CV 10–42% professionals; 4–19% same analyst | Abstract |
| 17 | "Hit or miss? Impact of time series resolution..." (2024) | Abstract | Weekly/biweekly can miss short blooms; twice-weekly better for timing | Abstract |
| 18 | Existing project evidence | Sprints 4K/4L.1/4L.2/4L.3/4L.3C/4L.3D | Sensor list, metadata, prior access/failure, no raw biology | Full reports |

## Inaccessible / incomplete

- AlgaeBase direct species pages blocked by Cloudflare Turnstile; search-result records used for synonym leads, and HCB-1 Table A-1 used as the authoritative crosswalk.
- Carey 2016, Carpenter 2020, Beal 2022 full PDFs not parsed (no PDF parser); search-index full-text excerpts inspected.
- HELCOM/CEMP full PDFs not parsed; relevant sections visible in search results.
- 129.42 daily/hourly/high-resolution sensor data not acquired; sensor compatibility remains metadata-level.
- No additional literature beyond the defined categories was pursued after saturation of the specific questions.

## Conflicting evidence

- PhycoTech self-reports high consistency/95%+ QA, while independent long-term series studies document taxonomic bias and interanalyst variation. Both are recorded; neither is treated as conclusive for this dataset.
- High-frequency sensor studies show useful pigment proxies, while O'Brien et al. show empirical EWS often fail. This cautions against assuming confirmatory early warning.
- Metadata says Mendota 0–8m and other lakes 0–2m; raw data contain exceptions in 1995/2002–2004. Recorded, not corrected.
