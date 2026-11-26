# Dataset Verification Report (Sprint 4)

**Date:** 2026-11-22  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory only)

## Verified downloadable / inspected

### BP-001 Painter et al. 2022 (Borealis/GitHub)

- **DOI:** 10.5683/SP3/MP6NXF
- **Landing page:** https://borealisdata.ca/dataset.xhtml?persistentId=doi:10.5683/SP3/MP6NXF
- **Mirror:** https://github.com/biogeochem/buffalopound_blooms
- **Licence:** CC BY-NC-SA 4.0
- **Verification date:** 2026-11-22
- **Downloaded files:** 7 key files to `research/evidence/sprint4_global_bio/downloads/painter_borealis_10.5683_SP3_MPNXF/` with SHA256 manifest.
- **Verified contents:**
  - `BP_PhytoTax_2018_KP.csv`: 818 rows, 18 cols; fields include Sample_ID, Location, Depth, DOY, Species_Code, Species_Name, Cell_Density_L, Biomass_mg_m3, Length_um, Width_um, Cell_Volume_um3, Group, Phylum, Family, Genus, Species. 25 unique DOY.
  - `BP_PhytoTax_2019_KP.csv`: 17 unique DOY.
  - `Nutrients_Biomass_BP_clean.csv`: 44 rows; Year, DOY, Tot_Biomass, Dolichospermum, Planktothrix, SRP, NH3, NO3, Chla.
  - Toxin CSVs present; encoding/structure requires careful parsing (latin-1, complex header rows).
- **Assessment:** Independent biological microscopy/taxonomy/biovolume/biomass data for Buffalo Pound 2018-2019. **Class B - Conditional**. Not sufficient alone for confirmatory Gate 2 evaluation.

### GL-001 US EPA NLA phytoplankton (partial verification)

- **Landing page:** https://www.epa.gov/national-aquatic-resource-surveys/data-national-aquatic-resource-surveys
- **Verified file:** `nla_2017_phytoplankton_count-data.csv` header checked via curl 2026-11-22.
- **Observed fields:** PUBLICATION_DATE, UID, SITE_ID, DATE_COL, VISIT_NO, STATE, STUDY, SITETYPE, LAT_DD83, LON_DD83, SAMPLE_TYPE, SAMPLE_ID, TAXA_ID, ABUNDANCE, BIOVOLUME, DENSITY, ANALYST_NAME, ALGAL_GROUP, TARGET_TAXON, PHYLUM...
- **Assessment:** Public, independent biological counts/biovolume. **Class C - Exploratory** for EcoSentinel confirmatory HF EWS due survey design (single visit/lake/survey).

### GL-002 CEH Cumbrian Lakes (metadata verified, download gated)

- **DOI:** 10.5285/1de49dab-c36e-4700-8b15-93a639ae4d55
- **Landing page verified:** 2026-11-22; licence terms apply; collaboration requested.
- **Not downloaded:** licence acceptance required; human review needed before accepting terms/downloading.
- **Assessment:** **Class B - Conditional lead** pending licence review and data inspection.

## Not verified as downloadable

- **BP-002 Boyer 2025 raw data:** no public supplement/raw data located in Sprint 4 search. Paper DOI verified; content access blocked by publisher 403 during direct fetch.
- **BP-004 BPWTP records:** no public dataset located.
- **BP-005 WSA records:** no public dataset located.

## Verification limits

- No paywalls/access controls bypassed.
- No author/institution contact made.
- Downloads limited to publicly accessible files; Painter key files downloaded, full 13.1MB zip not fully extracted beyond key files.
