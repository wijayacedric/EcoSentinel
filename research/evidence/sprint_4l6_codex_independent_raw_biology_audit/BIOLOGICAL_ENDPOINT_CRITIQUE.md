# Biological endpoint critique

## What microscopy independently measures

The file contains phytoplankton microscopy counts and geometry-based cell biovolume, not buoy chlorophyll/phycocyanin sensor values. This makes it **measurement-source independent** of pigment sensors in principle. PLOS One's Mendota methods describe preserved deep-hole 0–8m integrated samples, inverted microscopy and natural units (cells, filaments, colonies), with cell densities and biovolume calculated; earlier work also warns that patchiness/small sample volume can create false negatives. Microscopy is therefore a direct biological observation, but not error-free or exhaustive “ground truth.” It cannot alone verify lakewide surface scum, toxin production, toxicity, onset between sample dates, or absence of a bloom elsewhere in the lake.

The archived 2023 NTL protocols include the integrated 0–8m Mendota phytoplankton collection instruction and a laboratory counting-method appendix attributed to PhycoTech. That appendix describes measurement of GALD and other dimensions, geometric volume approximations, counting natural units/cells, and a recount QA/QC of approximately every tenth sample with stated acceptance comparisons. This is useful evidence that the method has explicit measurement and QA procedures; it does **not** establish that this 88.31 version's particular historical rows were recounted, passed those criteria, or had their QA results retained in this export. The archive's applicability to every historical year is unresolved.

## Candidate measures

- **Cell density (`cells_per_ml`)**: direct count-derived; arithmetic check against cells-per-natural-unit × natural units/ml is good (max relative difference 0.000228 in 18,653 checked records). Yet the source has colonies/filaments and species-specific counting conventions. Cells are not equivalent to biomass; colony/filament geometry and cell sizes vary. One row has zero cells while positive units/ml.
- **Absolute biovolume (`biovolume_conc`)**: cell dimensions converted to geometric volumes, then multiplied by density according to EML. This integrates size and counts and is less sensitive than cell counts to whether an organism is counted as one colony or many cells only if geometry/count conventions are applied consistently. Geometric shape approximation, identification, dimensions, repeated variants and sampling bias remain sources of uncertainty. Contains three zeros and a maximum/extreme artifact concern (Mendota maximum less than cross-lake max), with the Coelastrum row's near-zero value tied to conflicting biomass/relative values.
- **Biomass (`biomass_conc`)**: derived from biovolume by assumed density-to-mass conversion. It is not independent. 61 values round/truncate to zero at the low end, plus the Coelastrum conflict. Lower reliability as sole low-abundance endpoint.
- **Relative total biovolume**: compositional percentage field, but denominator is unspecified and sample sums often disagree. Not defensible for analysis until explained.

## Recommendation challenge

Cyanobacterial absolute biovolume (`division=Cyanophyta`) is the most defensible of these as a **candidate exploratory abundance indicator**, conditional on row-level QC, taxonomic scope, repeated-record interpretation and a clearly defined sample aggregation. It measures cyanobacterial volume, not bloom status. Presence/abundance does not equal bloom. The dataset does not define a bloom threshold, toxin status, independent event ground truth, or verified non-event exposure. This audit created no threshold or labels.

Microscopy and sensor predictors would have distinct measurement pipelines but share dependence on the same lake processes and imperfect spatial/depth representation. Statistical independence does not follow from different instruments. An independent adjudicator/source would be needed to establish bloom labels if those are required by the research question.
