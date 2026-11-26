# 88.31 Biological Data Access Audit

**Date:** 2026-11-23T23:32:06.599235+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Package identity

- `knb-lter-ntl.88.31`; DOI `10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9`.
- Title: North Temperate Lakes LTER: Phytoplankton - Madison Lakes Area 1995 - current.
- Repository/custodian: EDI / NTL-LTER, UW-Madison.
- Metadata: public CN EML, 27,408 B, SHA256 `c96ddc258080971dd79294ad906287172bd285ae79e020921a3b0d5c70d7bfc7`.

## Exact data files

- **One data entity:** `https://pasta.lternet.edu/package/data/eml/knb-lter-ntl/88/31/f2de15b2fff6ae962a04c150c0a1c510`.
- Size: **2,448,830 B**; format text/csv; CN sysmeta 200.
- Report entity and metadata entity also exist.
- Data bytes: **not obtained** (CN 404; PASTA 403).

## Biological content (metadata)

- Attributes: `lakeid, year4, sampledate, sta, depth_range, division, taxa_name, gald, cells_per_nu, nu_per_ml, cells_per_ml, biovolume_conc, biomass_conc, relative_total_biovolume, genus`.
- **Cell density, biovolume and biomass are available in the schema.**
- Species/genus-level taxonomy; division includes cyanobacteria.
- Independent of buoy sensors (microscopy vs sensor).

## Mendota-specific coverage

- Four lakes: **Mendota, Monona, Wingra, Fish**.
- Mendota: composite whole-water **0-8 m**; tube sampler; glutaraldehyde preservation; PhycoTech slides.
- 1995-01-24 to 2020-12-31.
- Sampling: **biweekly** ice-free late March/April-early September; every 4 weeks through late November.
- Taxonomic updates Feb 2013 (name changes; some genus-to-species revisions).
- Wingra/Fish often archived but not routinely counted; Mendota/Monona routinely analyzed.
- Mendota-only subset requires `lakeid` filtering; not yet verified in data.

## Methodological caveats

- "Species may not have been determined for all available slides" (EML).
- Taxonomic changes over 25+ years require harmonisation.
- Composite 0-8 m sample is not a surface grab; depth comparator for buoy sensors must be defined.
- Units: metadata describes cells/mL, biovolume concentration; raw units/detection limits not verified.

## Legitimate route

- Authorized EDI IAM/API access (free profile + key), then download the CSV entity.
- Alternative: EDI portal after login.
- No DUA or institutional account indicated; confirm package-level terms.

## Status

**Metadata-only; authorization-required; scientifically promising but unverified.**
