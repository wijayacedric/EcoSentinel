# Two-Lake Comparability Review

**Sprint:** 4L.13  
**Status:** INDEPENDENT REVIEW — NOT APPROVAL  
**Protocol reviewed:** Sprint 4L.12, PROPOSED — NOT APPROVED  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

> **This review does not approve the protocol or authorise analysis.**

## 1. The proposed contrast

The 4L.12 protocol proposes a two-lake descriptive comparison:

- **Mendota:** 0.5 m sensor vs 0–8 m microscopy composite; Turner 2006–2019; 128/139 same-day strict-unflagged dates.
- **Buffalo Pound:** 0.82 m sensor vs 0.8 m microscopy sample; YSI 6600 2018–2019; 42 dates.

The protocol describes this as a contrast between a depth-mismatched and a depth-aligned setting. It correctly states that the comparison cannot isolate depth. The question, however, still says “how do these associations vary by ... depth-alignment setting,” which implies more than the design can support.

## 2. Does the two-lake design add value?

### 2.1 What it can add

- **Two independent case studies.** The same general question — does surface pigment fluorescence rank with microscopy-derived cyanobacteria abundance? — is asked in two contrasting lakes.
- **A depth-mismatched case and a depth-aligned case.** Mendota’s 0.5 m vs 0–8 m is a clear mismatch; Buffalo Pound’s 0.82 m vs 0.8 m is close. The contrast is illustrative.
- **Different data-quality regimes.** Mendota has a long record with flag inconsistencies and Turner/YSI transitions; Buffalo Pound has a short record with a single shallow sonde and documented maintenance/fouling flags.
- **A test of whether the expected weak/variable relationship appears in both settings.** If both are weak, that is a useful descriptive result; if one is strong, that is also informative.
- **A cautionary example.** Buffalo Pound’s prior *Planktothrix* bloom that was missed by sensor/lab chlorophyll is a concrete reason not to assume depth alignment guarantees agreement.

### 2.2 What it cannot add

- **A controlled depth comparison.** Depth is confounded with lake identity and many other factors.
- **A generalisable multi-lake relationship.** Two lakes are not a sample of lakes.
- **A validation of one lake by the other.** Buffalo Pound cannot validate Mendota, or vice versa.
- **A causal explanation of why associations differ.** The design is observational and confounded.
- **A “natural experiment.”** There is no manipulation, matching, or counterfactual.

## 3. Confounding

The two settings differ in at least the following dimensions:

| Dimension | Mendota | Buffalo Pound | Consequence |
|---|---|---|---|
| Lake type | Large, deep, dimictic eutrophic lake | Shallow, polymictic eutrophic reservoir | Different stratification, mixing, nutrient dynamics, bloom phenology |
| Morphometry | Deep; 0–8 m composite | Average depth ~3 m; 0.8 m sample | Depth integration and vertical heterogeneity differ |
| Biological period | 2006–2020 (14 Turner years + YSI) | 2018–2019 (2 seasons) | Different climate, management, trophic state, sampling programmes |
| Biological cadence | Median 14 days | Median 4/8 days | Different temporal resolution and interval censoring |
| Biological depth | 0–8 m tube composite | 0.8 m discrete sample | Different sample integration, not just depth |
| Sensor depth | 0.5 m | 0.82 m | Different surface layer |
| Sensor instrument | Turner Cyclops 7; YSI EXO2 | YSI 6600 | Different optics, calibration, RFU scale |
| Sensor output | RFU; Turner/YSI non-comparable | RFU; single instrument family | No cross-lake RFU comparison |
| Community | Mixed phytoplankton; cyanobacteria median 67.2% of biovolume | Bloom-season cyanobacteria ~71% of biomass; *Dolichospermum*/*Planktothrix* phases | Different pigment content, morphology, toxicity |
| Taxonomy | 468 names; non-stationary; 2013 update | 73/56 taxa; 39 shared; 2018/2019 schema change | Different taxonomic resolution and stability |
| QC | C/E/H/G/O flags; undocumented codes; no per-record calibration | M/C/A2–A6/B6/B7; documented; interval fouling flags | Different exclusion patterns and bias |
| Endpoint | Biovolume (µm³ mL⁻¹) | Biomass (mg m⁻³) | Different quantity and derivation |
| Spatial setting | Buoy ~106 m from NTL site; station mostly blank | Single buoy near intake; biology site not independently co-located | Different spatial mismatch |
| Sampling programme | Long-term LTER | Research/data-buoy programme | Different field logistics, sorting, and selection |

**Conclusion:** Depth alignment is one difference among many. The design cannot attribute a difference in association to depth.

## 4. The depth comparison specifically

### 4.1 Mendota

- Sensor: 0.5 m point.
- Biology: 0–8 m tube composite.
- The composite integrates biomass over the upper water column; the sensor samples one stratum.
- Under stratification, surface chlorophyll/phycocyanin may be higher or lower than the column mean; vertical migration, surface scums, light acclimation, and grazing add decoupling.
- The 0.5 m sensor is not a whole-column measurement.

### 4.2 Buffalo Pound

- Sensor: 0.82 m.
- Biology: 0.8 m discrete sample.
- The depths are close, but the sample is a point sample, not a depth-integrated composite.
- The lake is shallow and polymictic; transient stratification can still decouple surface and bottom, but the sampled depth is closer to the sensor.
- Prior work reported an autumn *Planktothrix* bloom that was not detected by sensor or laboratory chlorophyll-a, so depth alignment does not guarantee agreement.

### 4.3 What the contrast can say

- “The Mendota case, with a 0.5 m sensor and a 0–8 m composite, showed [pattern]; the Buffalo Pound case, with a 0.82 m sensor and a 0.8 m sample, showed [pattern].”
- “The difference is consistent with a depth-alignment effect, but it is also consistent with lake, instrument, period, community, and endpoint differences.”
- “The comparison is illustrative, not a test.”

### 4.4 What it cannot say

- “Depth alignment improves agreement.”
- “Depth causes the difference.”
- “Buffalo Pound validates the Mendota sensor.”
- “The two lakes show a generalisable relationship.”
- “Surface sensors represent whole-water-column biomass.”

## 5. Is the comparison worth doing?

**As two case studies: yes, modestly.** It can show whether the expected weak/variable relationship appears in both a depth-mismatched and a depth-aligned setting, and it can document data-quality differences. That is a legitimate descriptive contribution.

**As a depth comparison: no.** The design cannot isolate depth. If the primary goal is to understand depth effects, the project needs depth-resolved paired sampling at the buoy, not a two-lake contrast.

**As a novelty claim: no.** The measurement question is already studied; two lakes are not a new method.

## 6. Recommended reframing

Replace:

> “...and how do these associations vary by season and depth-alignment setting?”

with:

> “...and how do the two lake-specific associations differ descriptively across seasons and sensor eras, acknowledging that the lakes differ in depth alignment and many other respects?”

Or, more simply:

> “...and how do the two lake-specific case studies compare descriptively?”

This preserves the comparative interest without implying a controlled depth contrast.

## 7. Findings

| ID | Finding | Severity |
|---|---|---|
| G1 | The two-lake design has illustrative value as two case studies | Pass |
| G2 | The depth contrast is severely confounded | **Major** |
| G3 | The question’s “depth-alignment setting” implies a comparison the design cannot support | **Major** |
| G4 | Different endpoints (biovolume vs biomass) prevent like-for-like comparison | **Major** |
| G5 | Different instruments/periods/communities/QC prevent causal attribution | **Major** |
| G6 | The protocol correctly prohibits “depth causes” language in the claims matrix | Pass |
| G7 | The comparison should be reframed as two case studies, not a depth test | Required |

## 8. Required changes

1. Remove “depth-alignment setting” from the primary question.
2. Call the design “two lake-specific case studies.”
3. State that depth alignment is one of many differences.
4. Keep the prohibition on causal depth claims.
5. Do not use Buffalo Pound to validate Mendota.
6. Do not claim a generalisable multi-lake relationship.

## 9. Governance

- **Protocol: PROPOSED — NOT APPROVED.**
- **Gate 2: PAUSED / NOT APPROVED — Option C (Exploratory Only).**
- No decision is approved by this review.
- No analysis is authorised until the required revisions and D-15 approval are recorded.
