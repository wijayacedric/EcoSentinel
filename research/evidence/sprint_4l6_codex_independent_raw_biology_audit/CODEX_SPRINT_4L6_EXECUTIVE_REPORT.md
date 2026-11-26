# Sprint 4L.6 — Independent adversarial audit

**Assessment date:** 24 November 2026  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Executive verdict

The Sprint 4L.5 audit is **mostly reproducible as a descriptive data-quality audit**, but its records and derived fields do not support confirmatory bloom-warning evaluation. Core raw identity, row structure, Mendota's 402 dates, numeric distributions, depth/station counts, the relative-percentage anomaly pattern, and duplicate counts were independently reproduced. One headline taxonomy count is wrong by inclusion of the blank string: 469 distinct cleaned names becomes 468 nonblank names; 177 genera becomes 176 nonblank genera. Other material counts agree.

The strongest challenge is interpretive. `relative_total_biovolume` cannot be validated as a sample percentage from its metadata; 14 totals near 200% remain unexplained, 3 groups are all zero, and one group totals 283,906.853%. The Coelastrum row is internally incompatible with a valid observation under the published field meanings. This is a severe data-quality anomaly, but the precise failure mechanism is not identifiable from this export. Biomass is a derived field, not independent evidence, and 61 positive biovolumes map to exact zero biomass at a scale consistent with decimal rounding/truncation.

Direct microscopy is independent of buoy sensor measurement, but it is not “biological ground truth” for bloom onset: it is a preserved, depth-integrated sample with taxonomic and enumeration uncertainty. The data support descriptive seasonal and possibly multi-week exploratory work with explicit quality restrictions. They do **not** support the original confirmatory early-warning question at hours-to-days horizons, nor validated bloom/non-bloom classifications. Gate 2 should remain paused.

## Answers to the seven required questions

1. **Technically reproducible?** Yes for core parsing and summary statistics. Independent script and hash included.
2. **Calculations correct?** Most reproduced. Taxa/genus richness headlines are each one too high when blanks are excluded; note scripts intentionally counted `""` as a distinct value. Other reported counts checked here agree.
3. **Anomaly interpretations justified?** Flagging is justified; causal explanations are not. 200% totals and duplicate blocks need source records. The Coelastrum row is internally inconsistent, but cannot be conclusively classified as transcription, field shift, unit conversion or valid biology from the export alone.
4. **Cyanobacterial biovolume as primary exploratory endpoint?** Conditionally defensible as the least problematic derived abundance metric among these fields, after QC and explicit aggregation rules. Not verified bloom truth and not a stand-alone confirmatory endpoint.
5. **Seasonal/multi-week exploration?** Yes, conditionally: the record has useful long-term breadth, but irregular 14-day median cadence, depth compositing, taxonomic revision, and export anomalies constrain interpretation.
6. **Original confirmatory early-warning question?** No, based on this dataset alone. Biology is too sparse for short warning horizons, event onset is interval-censored, there is no independent event adjudication/threshold or validated non-event exposure, and sensor/predictor alignment is not resolved by this biology file.
7. **Material threats?** Unknown percentage denominator; Coelastrum anomaly; 14 near-200% groups; repeated taxon rows/replicates; taxonomic recuration; incomplete station metadata; 40 Mendota depth exceptions; coarse sampling; no time-of-day or sample-volume/detection-limit fields.

## What would change the assessment

Obtain and reconcile archived sample-level laboratory sheets/export documentation, the exact formula and grouping unit for relative total biovolume, the 2011-07-25 original microscopy/count record and unit conversions, explanation for the duplicate 1999-11-22 block and 13 remaining 200% groups, date-specific station/depth/sample-volume records, versioned taxonomic change log, and method/detection-limit information. Then independently adjudicate whether the biological endpoint can define event onset and non-event exposure at a resolution matching the planned horizon. No such adjudication was done in this audit.

## Evidence and reproducibility

Raw CSV SHA-256: `a63d7cfa0502e3cdab6d8939f21820f305295e030d4d08bf10bfc69b22829db2`; 2,448,830 bytes; 18,654 rows × 15 fields. See [independent results](INDEPENDENT_REPRODUCTION_RESULTS.md), [discrepancy register](SPRINT_4L5_DISCREPANCY_REGISTER.csv), source/search registers, and reproducible script in `scripts/`.

**Governance:** No event labels/intervals, predictive/confirmatory analysis, protocol change, contact, upload, commit, or push. Source and Sprint 4L.5 outputs were not changed.
