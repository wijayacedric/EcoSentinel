# Buffalo Pound Biomass Endpoint Audit

## Finding and correction to Sprint 4L.14

The 4L.14 claim that the full paper was inaccessible is **outdated**. Independent access to the publisher’s full 2022 article (DOI [10.1039/D2EM00078D](https://doi.org/10.1039/D2EM00078D)) exposed its methods section. It states that preserved phytoplankton samples were enumerated and identified to species level by inverted microscopy; cell counts were converted to wet-weight biomass by estimating individual cell volumes from measured cells using the geometric formula best fitting cell shape, following Vollenweider. The paper reports abundance as biomass in mg m⁻³ and sampling at 0.8 m. This directly supports the broad claim that the supplied endpoint is derived from microscopy and cell geometry.

The article does not, in the accessible methods text, specify the exact universal density multiplier represented by `Cell_Volume_um3 × Cell_Density_L × 10^-6`, nor does it explain the duplicate date-species rows in local data files. Therefore the arithmetic consistency checks reported by 4L.14 remain useful metadata evidence, but they are not the sole evidence and should not be described as a complete verification of the conversion.

## Dimensional interpretation

Cell volume in µm³ per cell multiplied by cells per litre yields µm³/L. Converting volume to mass requires an assumed or taxon-specific density. Under 1 g cm⁻³ (equivalent to 1 mg/mm³), the numerical conversion to mg/m³ is `×10^-6`; it is dimensionally coherent. Dimensionally coherent does not prove the biological density assumption or the exact method used for this supplied column. The paper’s term “wet-weight biomass” supports an approximate volume-to-mass estimate; it is not dry mass, carbon, or gravimetric measurement.

## What is directly established

- Species-level microscopic identification and enumeration are described in the primary paper.
- Samples were preserved with Lugol’s iodine, concentrated, and enumerated using inverted microscopy.
- Cell counts were converted to wet-weight biomass using individual cell measurements and shape-specific geometric volume formulas.
- Figures and results use biomass in mg m⁻³; paper identifies taxa contributing to cyanobacterial biomass.
- The 2018 and 2019 data are from separate ice-free seasons; article reports different community succession and explicitly warns that two years may not represent future/current conditions.
- The paper’s results show chlorophyll-a and microscopy biomass can diverge for taxa: autumn *Planktothrix agardhii* made up a large share of biomass but was not accompanied by comparable chlorophyll peaks; *Dolichospermum* biomass and chlorophyll associations differed from *Planktothrix*.

## What remains unverified

- Whether local `Biomass_mg_m3` exactly equals the proposed formula for every taxon row, rather than a closely related method.
- What density assumption is used, whether it is fixed or taxon-specific, and the rounding chain.
- Whether duplicate date × species records are technical replicates, split counts, separate subsamples or distinct sample records.
- Whether REP1/REP2 are identifiers for samples, observers, replicates or other source structure; 2019 rows fall on disjoint dates in the inspected source audits.
- Detection/counting limits and observer repeatability for the exact dataset.
- Whether “cyanobacteria total” at sample level matches the article’s aggregation choices and taxonomic groups.

## Endpoint suitability

This is an independent, microscopy-derived wet-weight estimate, appropriate for a bounded exploratory association with sensor RFU if the source aggregation semantics and exact field mapping are resolved. It is not numerically equivalent to Mendota biovolume and should not be used as a conversion target or pooled endpoint. The 2022 paper already analyzes relationships between cyanobacterial taxon biomass and extracted laboratory chlorophyll-a, including weak/absent chlorophyll response for *Planktothrix*. The proposed project can ask a distinct question about in-situ YSI RFU and total cyanobacteria, but it must acknowledge this close prior art and the species-dependence it documents.

**P3/P4 recommendation:** Keep exploratory only until the data custodian reconciles local row semantics and biomass field provenance to the paper and data release. Do not exclude Buffalo Pound solely because 4L.14 could not open a paper that is now accessible.

## Primary sources

- Painter et al. (2022), publisher full article: [DOI 10.1039/D2EM00078D](https://doi.org/10.1039/D2EM00078D).
- Supporting Information: [RSC ESI PDF](https://www.rsc.org/suppdata/d2/em/d2em00078d/d2em00078d1.pdf).
- Data deposit cited by paper: [FRDR DOI 10.5683/SP3/MP6NXF](https://doi.org/10.5683/SP3/MP6NXF).
- Vollenweider reference cited by article: [Scientific fundamentals of the eutrophication of lakes and flowing waters](https://doi.org/10.1016/j.ejrh.2016.01.034).

