# Biological Endpoint Review

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

> **This review does not approve the protocol or authorise analysis.**

## 1. The two endpoints

| Lake | Proposed endpoint | Unit | Depth | Source |
|---|---|---|---|---|
| Mendota | Total cyanobacteria biovolume | µm³ mL⁻¹ | 0–8 m composite | NTL-LTER 88.31 |
| Buffalo Pound | Total cyanobacteria biomass | mg m⁻³ | 0.8 m | Painter et al. 2022 |

The protocol correctly refuses to treat these as numerically equivalent. That passes review.

The protocol does not sufficiently document the **derivation** of the Buffalo Pound biomass endpoint, and it does not fully confront the implications of using biomass rather than biovolume for the cross-lake question. These are material issues.

## 2. Mendota cyanobacteria biovolume

### 2.1 What the source measures

The NTL-LTER phytoplankton dataset is microscopy-based:

- samples are 0–8 m tube composites at the deep-hole station;
- phytoplankton are identified and counted by inverted microscopy (Utermöhl technique);
- cell dimensions are measured and converted to geometric biovolumes;
- `biovolume_conc` is computed from average cell biovolume × cell density;
- `biomass_conc` is a derived conversion (approximately biovolume × 10⁻⁶), not an independent measurement.

The endpoint is measurement-independent of the buoy sensor: different method, different instrument, different analyst pipeline.

### 2.2 Strengths

- Long record: 402 Mendota dates, 1995–2020; 400 dates at 0–8 m.
- Direct microscopy, not a sensor proxy.
- Species-level counts and geometry-based biovolume.
- Broad `Cyanophyta` total reduces dependence on species-level taxonomy.
- The endpoint is an abundance/biomass measure, not a bloom label.

### 2.3 Limitations

1. **Taxonomic non-stationarity.** 468 unique cleaned taxa names, 176 genera, 11 divisions; 204 names occur only pre-2013 and 72 only post-2013; 889 genus-field mismatches; the EML documents a February 2013 taxonomic update. Broad division totals reduce but do not eliminate this.
2. **Repeated records.** 1,009 same-key groups / 2,048 rows share lake/date/station/depth/taxon but differ in values; the EML says these may be variants or vegetative states. Summing biovolume is defensible for a broad total, but the rows are not independent.
3. **Anomalies.** 61 biomass zeros with positive biovolume (low-value truncation); one catastrophic Coelastrum row (non-cyanobacteria); `relative_total_biovolume` sums to ~200% in 14 groups, 0% in 3, and one extreme value; 29 exact duplicate row-groups (all Monona, not Mendota).
4. **Depth mismatch.** 0.5 m sensor vs 0–8 m composite. The composite integrates the upper water column; the sensor samples one stratum.
5. **Spatial mismatch.** Buoy and NTL sampling site are ~105.7 m apart; station metadata are blank for 371/402 dates.
6. **No sample time.** Date-only; diel vertical migration and patchiness cannot be resolved.
7. **No detection limits.** The dataset does not provide field blanks, detection limits, or identification uncertainty. Zeros may be real or below detection.
8. **Taxonomy vs function.** `Cyanophyta` includes taxa with different pigment content, morphology, and toxicity. It is not a bloom or toxin endpoint.

### 2.4 Is the endpoint sufficiently documented?

**Yes, for a broad cyanobacteria biovolume endpoint, with caveats.** The EML documents the method, units, and depth. The main unresolved issues are taxonomic non-stationarity and anomalies, which the protocol acknowledges. The broad division total is the most defensible choice.

## 3. Buffalo Pound cyanobacteria biomass

### 3.1 What the source provides

The Painter et al. 2022 taxonomy files include:

- `Cell_Density_L` (cells L⁻¹);
- `Biomass_mg_m3` (mg m⁻³);
- `Length_um`, `Width_um`, `Cell_Volume_um3`;
- `Group`, `Phylum`, `Family`, `Genus`, `Species`.

There is **no `Biovolume` column**. The protocol uses `Biomass_mg_m3` as supplied.

### 3.2 Is biomass independently measured?

No. Biomass is a **derived quantity**, almost certainly from cell counts × cell volume × an assumed density/conversion. The local metadata and the 4L.12 source register do not document the exact formula. The 4L.12 protocol treats biomass as “the provided endpoint,” which is reasonable for avoiding a new derived dataset, but it does not establish that the derivation is consistent across 2018 and 2019.

### 3.3 Why this matters

- If biomass is derived from cell volume using a density assumption, it is not independent of the cell-volume measurement; it is a transformed microscopy quantity.
- If the 2018 and 2019 conversions differ, the two seasons are not directly comparable.
- If the conversion is undocumented, the endpoint’s units and interpretation are less certain than the protocol implies.
- Biomass is not biovolume; the two cannot be pooled or compared numerically.
- A rank association with biomass may differ from a rank association with biovolume if the conversion is nonlinear or taxon-specific.

### 3.4 Other limitations

1. **Two seasons only.** 25 dates in 2018, 17 in 2019; no non-bloom baseline.
2. **Sampling cadence.** Median 4 days (2018), 8 days (2019); maximum 12/16 days.
3. **Taxonomic change.** 73 taxa in 2018, 56 in 2019; only 39 shared; 2018 uses `Sample_ID`, 2019 uses `REP`.
4. **Replicates.** 2018 has 19 date–species groups with two rows but no replicate identifier; 2019 `REP1`/`REP2` occur on disjoint dates. The protocol’s mean-before-sum rule is an assumption, not a documented replicate design.
5. **2019-07-17 anomaly.** Total biomass 45.81 mg m⁻³, cyanobacteria 41.02 mg m⁻³, between neighbours 12,587.1 and 9,497.9; all rows `REP2`; unresolved.
6. **No detection limits.** No field blanks or detection limits; zeros may be real or below detection.
7. **No sample time.** Date-only.
8. **Depth/spatial.** 0.8 m sample; buoy 0.82 m; single station; coordinates not independently re-verified.
9. **Toxin files not used.** The toxin data are not verified for quantitative use; the protocol correctly excludes them.

### 3.5 Is the endpoint sufficiently documented?

**Conditionally, not yet.** The endpoint is available and internally consistent with the taxonomy file, but the derivation of `Biomass_mg_m3` is not documented in the local metadata. Before primary analysis, the team must:

- verify the biomass formula from the Painter et al. methods or data documentation;
- confirm that 2018 and 2019 use the same conversion;
- state that biomass is a derived microscopy quantity, not a direct measurement;
- state that it is not numerically equivalent to Mendota biovolume;
- consider downgrading Buffalo Pound to exploratory if the derivation cannot be verified.

## 4. Are the endpoints comparable?

**No, not numerically.** They differ in:

| Feature | Mendota | Buffalo Pound |
|---|---|---|
| Quantity | Biovolume | Biomass |
| Unit | µm³ mL⁻¹ | mg m⁻³ |
| Derivation | Geometry-based cell volume × density | Likely cell volume × density × conversion; unverified |
| Depth | 0–8 m composite | 0.8 m point |
| Sampling | Tube composite | Discrete sample |
| Taxonomy | 468 names; division total | 73/56 taxa; group total |
| Period | 2006–2020 | 2018–2019 |
| Cadence | ~14 days | 4–16 days |
| Detection limits | None | None |

The protocol correctly says they must not be pooled. But the primary question still asks how associations vary across the two settings. A reader may infer that the two endpoints are comparable enough to contrast. They are not.

**Recommendation:** In the question and results, call them **two different biological endpoints** (biovolume vs biomass), not two versions of the same endpoint. The cross-lake comparison is a contrast of two case studies, not a like-for-like measurement comparison.

## 5. Independence from the sensor

Both endpoints are microscopy-derived and therefore measurement-independent of the optical sensor. That is a genuine strength.

However:

- they are not independent of the same lake processes;
- they are not independent of sampling design (bloom-targeted sampling, depth, season);
- they are not independent of taxonomic/trophic changes;
- they are not “ground truth” for bloom status, toxicity, or whole-lake biomass.

The protocol says this correctly.

## 6. Endpoint recommendations

| ID | Recommendation | Priority |
|---|---|---|
| D-B1 | Verify and document the Buffalo Pound biomass formula and 2018/2019 consistency | **Essential** |
| D-B2 | State explicitly that biomass is derived, not directly measured | Essential |
| D-B3 | Keep Mendota biovolume and Buffalo Pound biomass separate; no numeric comparison | Essential |
| D-B4 | Report Mendota broad-division total with taxonomy caveat; no species-level primary | Essential |
| D-B5 | Report detection-limit/zero limitations for both endpoints | Essential |
| D-B6 | Report the 2019-07-17 anomaly and its leverage | Essential |
| D-B7 | Consider downgrading Buffalo Pound to exploratory if biomass derivation is unverifiable | Conditional |

## 7. Findings

| ID | Finding | Severity |
|---|---|---|
| D1 | Mendota biovolume is documented and measurement-independent, with taxonomy/detection caveats | Pass with caveats |
| D2 | Buffalo Pound biomass derivation is not documented locally | **Major** |
| D3 | Biomass and biovolume are not numerically comparable | Pass (protocol says so) but question wording needs alignment |
| D4 | Buffalo Pound replicates are unresolved | Major |
| D5 | 2019-07-17 anomaly is unresolved and potentially influential | Major |
| D6 | No detection limits for either endpoint | Moderate |
| D7 | Broad-group endpoints are the right choice; species-level would be indefensible | Pass |

## 8. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No decision is approved by this review.
- No analysis is authorised until the required revisions and D-15 approval are recorded.
