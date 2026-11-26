# Mendota Biological Monitoring Review

**Purpose:** assess the independent biological evidence potentially available for a bloom-warning evaluation. No bloom labels, event intervals, or biological-data analysis were created.

## What the sources establish

**Official NTL-LTER documentation.** The current [NTL-LTER Research Protocols page](https://lter.limnology.wisc.edu/protocols/) states that routine sampling generally occurs biweekly in summer and monthly in the non-summer season; it lists phytoplankton biovolume for Mendota (ME) and Monona (MO). It gives the Lake Mendota sampling location as 43.09885, -89.40545 and says protocols are being revised. The [archived 2023 NTL protocol](https://lter.limnology.wisc.edu/wp-content/uploads/sites/2029/2023/06/NTLProtocols_Archived2023.pdf) specifies a tube-integrated 0–8 m water sample for Mendota phytoplankton, compared with 0–2 m at most other southern lakes. It describes collection into a jug, mixing, filling sample bottles, and preservation. This is a water-column composite, not a surface grab.

**Published species- and abundance-level evidence.** Hansen and Carey (2015; [DOI 10.1371/journal.pone.0115414](https://doi.org/10.1371/journal.pone.0115414)) describe Mendota phytoplankton sampled during 1995–2011 at the deep hole, biweekly to monthly during the open-water period, using an integrated 8 m tube and immediate glutaraldehyde preservation. Their methods report >400 natural units (cells, filaments, or colonies) identified to species per sample using an inverted microscope, cell density per mL, and calculated biovolume for each natural unit. The same taxonomist performed identifications throughout the period examined; taxa not resolved to species were excluded from that study's analysis. These statements support that species-level taxonomic observations, abundance, and calculated biovolume existed for at least that historical subset. They do not prove that the exact columns and methods are unchanged in package version 88.31.

Beversdorf, Miller and McMahon (2013; [DOI 10.1371/journal.pone.0056103](https://doi.org/10.1371/journal.pone.0056103)) conducted separate weekly Mendota field campaigns in 2010–2011, pairing cyanobacterial community profiles, cell-count context, nutrients, phycocyanin/chlorophyll and microcystin. The PC-IGS assay resolved subgenus operational taxonomic units; of 100 OTUs identified, 50 exceeded its relative-fluorescence quantification limit and only eight could be assigned to genus, with some fragments ambiguous across genera. Their paper explicitly defined a toxic phase using measured microcystin concentration, illustrating that community composition, bloom abundance and toxin status are distinct biological endpoints. This is evidence from a targeted study, not proof that 88.31 contains toxin measurements or uses the same assay. It also documents that a targeted biological campaign can provide denser weekly observations than routine long-term core sampling, so its data must not be silently conflated with 88.31.

Carey et al. (2016; *Journal of Plankton Research* 38:27–40; [DOI 10.1093/plankt/fbv116](https://doi.org/10.1093/plankt/fbv116)) analyze 16 years of biweekly phytoplankton data from Mendota and report seasonal succession, variability in its periodicity, and low-biomass/drought years. The paper states that spring-after-ice-off and summer samples were generally collected at biweekly intervals (with some scheduling variation), and makes clear that discrete phytoplankton time series cannot resolve minute-to-day variation. These studies describe the historic method as suitable for seasonal and longer temporal scales.

**Current dataset identity.** NTL-LTER lists “North Temperate Lakes LTER: Phytoplankton – Madison Lakes Area 1995 – current” on its [Core Datasets page](https://lter.limnology.wisc.edu/core-datasets/), with the EDI package family `knb-lter-ntl.88`; the target DOI specified for this review is [10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9](https://doi.org/10.6073/pasta/bd03330e83fc52a5442bb39e131c95e9), version 88.31. The current NTL page says package contents and metadata require EDI sign-in. I did not inspect the 88.31 entity table or raw files. Thus “1995–current” is an institutional series description, not independent verification that each year through the package's specific version is populated or suitable.

## Endpoint validity: what can be measured and what it means

### Taxa and abundance

The published methods show genus/species-level cyanobacteria can be distinguished at least in the legacy analysis. Cell density and natural-unit density are not interchangeable: colonial/filamentous taxa have multiple cells per unit, and their counts can diverge. A reproducible endpoint would need to state whether it sums cell density, natural-unit density, calculated biovolume, or another measure. It would also need a harmonized taxonomy and rules for unresolved/changed names, zeros, missing taxa, and any changes in analyst or enumeration practice.

### Biovolume and “biomass”

Calculated biovolume is a defensible size-aware abundance measure if the version-specific data and calculation procedure are confirmed. It is **not mass biomass by itself**. Converting volume to carbon or dry mass requires a documented conversion or cell-specific density/composition assumptions, which are not established by the sources inspected here. Do not use “biomass” as an exact synonym for biovolume. Some forecasting papers call the response “cyanobacteria biomass”; the data derivation and target definition need to be read from their full methods and cannot simply be transplanted to 88.31.

### Taxonomic presence is not bloom status

Presence of *Aphanizomenon*, *Dolichospermum*, *Microcystis*, or another cyanobacterial genus is not, by itself, a bloom. A bloom definition needs a biologically or management-justified quantitative criterion, taxonomic aggregation, duration rule if persistence matters, and a stated relation to toxicity or public-health concern. The 88.31 package title and broad monitoring description do not themselves provide an independently adjudicated “bloom” label. Microscopy can establish taxon abundance and biovolume at sampling times; it does not automatically certify toxin production, surface scum, lake-wide extent, or adverse effect. Species capable of producing toxins are not necessarily toxin-producing on each occasion.

### Independent biological evidence

Microscopy and buoy pigment fluorescence are separate measurement processes. That gives a legitimate opportunity to evaluate sensor-derived or other environmental warnings against a biological endpoint without defining that endpoint from the same fluorescence signal. However, independence of instruments is not equivalent to independent event adjudication: a threshold and adjudication rule still must be chosen before looking at predictors, and the observed endpoint is sampled intermittently. If phycocyanin is included as a predictor/standard monitoring comparator, it must not also define the reference event.

## Sampling coverage, effort, and method history

- **Location and depth:** published samples are from the deep hole using a 0–8 m integrated tube. It represents a vertically mixed composite over the sampled upper water column, not the sensor's single depth and not the whole lake.
- **Cadence:** historical publications describe biweekly to monthly open-water observations, generally biweekly during spring/summer and less often later; the current NTL overview says biweekly summer and monthly non-summer. Exact intervals, sample dates, ice-covered sampling, missed visits, and dates for each target package version require its metadata/data audit.
- **Seasonality:** open-water sampling is concentrated in the biologically active season; the current overview indicates monthly sampling in non-summer periods but does not establish equal visit coverage or equivalent detection across all ice conditions. Biological visits are not continuous exposure monitoring.
- **Method consistency:** one paper reports one taxonomist across 1995–2011; this is useful but cannot certify all years in 88.31. Current protocol page says methods are actively being revised. The version-specific history of collectors, taxonomists, counting chambers/volumes, preservation, taxonomy, cell-size measurement, and biovolume equations remains unresolved. Separate targeted studies used molecular profiles and toxin assays; those measurements are not part of the 88.31 endpoint unless package metadata prove otherwise. Hansen & Carey excluded unresolved-to-species taxa for their own analysis; that analysis choice is not a mandate for the EcoSentinel endpoint.
- **Detection and uncertainty:** sources reviewed do not specify a dataset-wide limit of detection/quantification, taxon-specific counting uncertainty, replicate variance, blank rules, or a consistent reporting threshold. A zero may mean not observed within the analyzed aliquot, not lake-wide absence. These are material for classifying low/no bloom states.

## Can events and non-events be verified?

**At sample dates:** potentially, if the package includes count/biovolume values and taxonomic coverage adequate to calculate a pre-specified cyanobacterial abundance endpoint, and if sample effort and uncertainty are known. This is promising but still package-level conditional.

**Between sample dates:** no direct continuous biological verification is established. An onset is only known to occur after the last qualifying non-event observation and by the first qualifying event observation, assuming comparable samples and a defensible state threshold. The interval may be roughly fortnightly in peak season and longer in shoulder seasons; a short event can be missed completely. The interval may widen around missing visits and non-summer gaps. A non-event sample does not certify the full intervening interval as true-negative exposure.

**Winter/off-season:** if no biologically comparable sampling was done, it cannot be counted as verified negative exposure. Exposure should be limited to periods in which independent biological sampling could have detected the endpoint at the stated temporal support.

## Suitable inference scale

The record can plausibly support seasonal succession, seasonal abundance, and perhaps warnings whose horizon is longer than typical revisit intervals. It cannot independently support a claim of hour-ahead or day-ahead bloom onset detection solely because sensors are minutely sampled. A short-horizon claim would face outcome-observation uncertainty wider than the claimed lead time. A coarser multi-week target remains a possibility only after inspecting actual event intervals, event durations, sample dates, and independent-year counts; this review does not define those events.

## Outstanding biological evidence required

1. EDI-authenticated version-specific metadata, entity list, data tables, variables, units, taxonomy fields, update date, and license for 88.31.
2. Full temporal and per-variable coverage, sample dates, missingness, duplicate handling, site/depth, and sampling-effort records.
3. The applicable historical phytoplankton and biovolume protocols, including taxonomic references, counting effort, cell/natural-unit definitions, preservation and equations; document all known method transitions.
4. Detection/quantification limits, replicate or analyst uncertainty if available, and interpretation of reported zeros and unresolved taxa.
5. An independently justified endpoint rule and a blinded feasibility census of observations, possible episodes, interval widths and non-event exposure—under a separately authorized phase, not this review.

**Biological assessment:** credible independent abundance evidence exists in published Mendota monitoring. The exact 88.31 endpoint is **conditionally supported**, while continuously adjudicated bloom events and toxicity status are **not established**.
