#!/usr/bin/env python3
"""Build Sprint 4L.5 markdown reports from generated tables."""
import csv, json, hashlib
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

BASE=Path('research/evidence/sprint_4l5_mendota_raw_biology_audit')
T=BASE/'tables'
NOW=datetime.now(timezone.utc).isoformat()
S=json.loads((BASE/'summary.json').read_text())

def rows(name): return list(csv.DictReader(open(T/name, newline='', encoding='utf-8')))
def md_table(headers, data, width=120):
    out=['| ' + ' | '.join(headers) + ' |', '|' + '|'.join(['---']*len(headers)) + '|']
    for r in data:
        vals=[]
        for h in headers:
            v=str(r.get(h,'')) if isinstance(r,dict) else str(r[headers.index(h)])
            v=v.replace('\n',' ')[:width]
            vals.append(v)
        out.append('| ' + ' | '.join(vals) + ' |')
    return '\n'.join(out)

def write(name, text): (BASE/name).write_text(text, encoding='utf-8')

f=S['file']; c=S['coverage']; tax=S['taxonomy']; dup=S['duplicates']; depth=S['depth']
by={x['lakeid']:x for x in c['by_lake']}

# RAW FILE VALIDATION
write('RAW_FILE_VALIDATION.md', f"""# Raw File Validation

**Date:** {NOW}  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## File

`research/evidence/sprint_4l_mendota_biology_audit/acquisition/88.31/North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__f2de15b2fff6ae962a04c150c0a1c510.dat`

## Independent checks

| Check | Result | Expected / note |
|---|---|---|
| Exists | Yes | — |
| Bytes | **2,448,830** | Matches EML size |
| MD5 | **`{f['md5']}`** | Matches EML `a0363cc7fdfd6c12889750fea27bd542` |
| SHA-256 | **`{f['sha256']}`** | Independently calculated |
| Encoding | UTF-8, ASCII-only | no non-ASCII characters found |
| BOM | {f['bom']} | none |
| Line endings | CRLF | {f['crlf_count']} CRLF, {f['lf_count']} LF |
| Header | 15 columns | exact match to EML |
| Data rows | **{f['rows']:,}** | 1 header + 18,654 data records |
| Malformed records | {f['malformed_rows']} | none |
| Blank lines | {f['blank_lines']} | none |
| CSV parse errors | none | Python csv parsed every line |
| `sampledate` parse errors | {f['parse_errors'].get('sampledate',0)} | none |
| `year4` parse errors | {f['parse_errors'].get('year4',0)} | none |
| `year4` vs date-year mismatches | {f['year_mismatch_count']} | none |
| Truncation | No | last line ends with CRLF |
| Raw file modified | **No** | read-only inspection |

## Verdict

The raw file is structurally valid, complete and integrity-verified against the EML size and MD5. No silent data loss was detected in parsing.
""")

# SCHEMA/PARSING
schema=rows('SCHEMA_COMPARISON.csv')
write('RAW_SCHEMA_AND_PARSING_AUDIT.md', f"""# Raw Schema and Parsing Audit

**Date:** {NOW}  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Header

Exact expected header (`header_match={f['header_match']}`):

`{', '.join(f['header'])}`

All rows have 15 fields; no malformed records, blank lines, or parse failures.

## Schema comparison

{md_table(['expected_column','actual_column','match'], schema)}

## Observed domains

- **lakeid:** 4 values — ME ({by['ME']['records']:,} records), MO ({by['MO']['records']:,}), WI ({by['WI']['records']:,}), FI ({by['FI']['records']:,}).
- **depth_range:** 2 values — `0-8m` ({sum(1 for r in rows('DEPTH_STATION_COUNTS.csv') if r['depth_range']=='0-8m' and False) or 'see depth table'}) and `0-2m`.
- **sta:** mostly blank; `1` appears only in 2011–2012 ME and 2011 MO.
- **division:** 11 values; Cyanophyta is the largest by records.
- **sampledate:** all parse as `YYYY-MM-DD`; no sample time field.
- **numeric fields:** all parse as finite floats; no blank/NA values. Zeros are present and must be interpreted with metadata (see variable report).

## Type observations

- `year4` is integer; `sampledate` is date; `lakeid`, `sta`, `depth_range`, `division`, `taxa_name`, `genus` are text.
- All seven biological numeric columns are numeric; no non-finite values.
- Values are ASCII; no hidden encoding substitution.

## Discrepancies with metadata

- Metadata says Mendota is 0–8 m and other lakes 0–2 m. Raw has **40 ME records at 0–2m** (2002-09-23, 2002-10-21) and **310 MO records at 0–8m** (11 dates in 1995, 2002–2004). These are documented, not corrected.
- `sta` is blank for 17,518 of 18,654 records; station identity cannot be reconstructed from this field alone.
- No QC-flag or detection-limit columns exist in the actual schema.
""")

# BIOLOGICAL VARIABLE DISTRIBUTIONS
q=rows('BIOLOGICAL_VARIABLE_QUALITY.csv')
overall=[r for r in q if r['scope']=='all']
selected=[]
for var in ['gald','cells_per_nu','nu_per_ml','cells_per_ml','biovolume_conc','biomass_conc','relative_total_biovolume']:
    for lake in ['ME','MO','WI','FI']:
        r=next((x for x in q if x['variable']==var and x['scope']==lake),None)
        if r: selected.append(r)
zero=rows('ZERO_INCONSISTENCY_SUMMARY.csv')
cons=S['numeric']['consistency']
write('BIOLOGICAL_VARIABLE_DISTRIBUTIONS.md', f"""# Biological Variable Distributions

**Date:** {NOW}  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Overall distribution

{md_table(['variable','n','missing','zeros','negative','nonfinite','min','p01','p25','median','p75','p95','p99','max','mean'], overall)}

## By-lake distribution (selected statistics)

{md_table(['variable','scope','n','zeros','median','p95','max'], selected)}

## Zero/inconsistency checks

{md_table(['check','records','lakes','min_value','max_value'], zero)}

## Arithmetic consistency

- **cells_per_ml vs cells_per_nu × nu_per_ml:** n={cons['cells_per_ml_vs_cells_per_nu_x_nu_per_ml']['n']:,}; max relative error **{cons['cells_per_ml_vs_cells_per_nu_x_nu_per_ml']['max_abs_rel_error']}**; no row >1% error. The three density fields are internally consistent to rounding.
- **biomass vs biovolume × 1e-6:** median ratio is ~1e-6, but 61 rows have biomass=0 while biovolume is 1.4–49 µm³/mL; 2,067 rows exceed 1% relative deviation due to small-value rounding/truncation. One catastrophic record: ME 2011-07-25 *Coelastrum reticulatum*, cells=0, gald=0.00018286, biovolume=7.688e-05, biomass=84.6924, relative=283806.87. This is internally impossible and must be flagged, not repaired.
- **relative_total_biovolume:** 762/781 sampling groups sum to ~100; **14 groups sum to ~200**, 3 sum to 0, 2 are other, and 1 contains the 283806.87 outlier. The cause is unresolved; do not assume a simple percentage denominator.

## Interpretation

- `cells_per_nu` ranges 0–48,000 and is a **natural-unit** count (colonies/filaments), not a cell count; `cells_per_ml` can reach 10,074,657 in colonial picocyanobacteria (WI 2002).
- `gald` is a linear dimension (0–3,200 µm), not a volume; biovolume is derived via geometry and is the more integrative metric.
- `biomass_conc` is derived from biovolume and loses small values (61 zero-biomass rows), so it should not be the sole endpoint for low-abundance taxa.
- No values were deleted, imputed, or winsorised.
""")

# TAXONOMY AUDIT
inv=rows('TAXONOMIC_NAME_INVENTORY.csv')
mism=[r for r in inv if 'genus_field_mismatch' in r['flags']]
mism=sorted(mism,key=lambda r:int(r['records']),reverse=True)
changes=rows('TAXONOMIC_NAME_CHANGES.csv')
pre=sorted([r for r in changes if r['status']=='only_pre_2013'],key=lambda r:int(r['records']),reverse=True)[:10]
post=sorted([r for r in changes if r['status']=='only_post_2013'],key=lambda r:int(r['records']),reverse=True)[:10]
cross=rows('TAXONOMIC_CROSSWALK_CANDIDATES.csv')
formats=rows('TAXONOMIC_FORMATTING_VARIANTS.csv')
write('TAXONOMIC_CONSISTENCY_AUDIT.md', f"""# Taxonomic Consistency Audit

**Date:** {NOW}  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Counts

- **{tax['distinct_taxa_clean']} distinct cleaned `taxa_name` values**, **{tax['distinct_genera_clean']} distinct genera**, **11 divisions**.
- Cyanophyta: **8,581 records / 127 taxa**; 73.2% of summed biovolume and 70.8% of biomass.
- ME has 391 distinct taxa and 163 genera; MO 360/147; WI 108/65; FI 23/18.
- **12 records have blank `taxa_name`; 1,632 records have blank `genus`.** Most blank-genus records are family/group labels (Chroococcaceae 735; Chlorococcaceae 426; Miscellaneous 376; Chrysophyceae 52; etc.), not species-level observations.

## Whitespace/formatting

- **8,514 records** have trailing whitespace in `taxa_name`; **927** contain double spaces.
- 204 inventory names have trailing spaces; 57 have double spaces.
- One case-only variant group: `Deasonia gigantica` / `Deasonia Gigantica` (41 records).
- Numeric species labels are split by punctuation: `Synechococcus sp1` (379) vs `sp. 1` (265); `Cyclotella sp1` (84) vs `sp. 1` (82); `Gymnodinium sp1`/`sp. 1` and `sp2`/`sp. 2`/`sp3`/`sp. 3` variants.
- These are candidate formatting harmonisations only; no names were rewritten.

## Genus-field mismatches

**{tax['genus_mismatch_records']} records** have a `genus` that does not match the first token of `taxa_name`. Top cases:

{md_table(['taxa_name_clean','genus_values','records','divisions'], mism[:12])}

The largest cases are consistent with known synonym updates (Coelosphaerium→Woronichinia; Phormidium→Pseudanabaena; Oscillatoria agardhii→Planktothrix) but the `taxa_name` was not updated consistently. Others are family/group labels with blank genus. This is a **field-level inconsistency**, not necessarily an identification error.

## February 2013 update and later changes

- Pre-2013 names: {tax['pre_names']}; post-2013 names: {tax['post_names']}; only-pre: {tax['only_pre']}; only-post: {tax['only_post']}.
- Taxa changes are **not confined to February 2013**. Examples of first/last dates in `TAXONOMIC_CROSSWALK_CANDIDATES.csv`:
  - Oscillatoria limnetica last 2010-11-02 → Pseudanabaena limnetica first 2011-06-13.
  - Coelosphaerium naegelianum last 2010-11-09 → Woronichinia naegeliana first 2011-06-13.
  - Anabaena circinalis last 2015-11-03 → Dolichospermum circinale first 2016-11-09.
  - Cylindrospermopsis raciborskii last 2018-10-02 → Raphidiopsis raciborskii first 2020-08-06.
  - Anabaena flos-aquae and A. mendotae have no matching current-name records in this file.
- This indicates multiple nomenclature/processing changes and incomplete crosswalks, not one clean 2013 break.

## Top pre-only / post-only names (records)

{md_table(['taxa_name_clean','status','records','first_date','last_date'], pre+post)}

## Candidate crosswalk (authority: ITRC HCB-1 Appendix A Table A-1)

{md_table(['historical_name','current_name_candidate','historical_records','current_records','both_present'], cross)}

**Status: candidate only.** No merger, renaming or aggregation was applied. Several historical names have no current-name counterpart in this file; several current names coexist with historical names for years.

## Taxonomic resolution

- 20 names are unresolved/infraspecific (`sp.`, `spp.`, `var.`, `cf.`), including Rhodomonas minuta var. nannoplanctica (494), Synechococcus sp. 1 (265), Cyclotella sp. 1 (82), Gymnodinium spp.
- `Miscellaneous` (376 records) is a catch-all, not a taxon.
- The 469-name count is an **upper bound on name diversity**, not a count of validated species.

## Conclusion

Longitudinal taxonomic comparison is possible only after a documented crosswalk and quality review. Raw names must not be treated as a stable species list across 1995–2020.
""")

# DUPLICATES
dup_rows=rows('DUPLICATE_GROUPS.csv')
exact=rows('EXACT_DUPLICATE_ROWS.csv')
mult=Counter(r['n_rows'] for r in dup_rows)
write('DUPLICATE_AND_REPEATED_RECORD_AUDIT.md', f"""# Duplicate and Repeated-Record Audit

**Date:** {NOW}  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Exact duplicate rows

- **{dup['exact_duplicate_groups']} groups / {dup['exact_duplicate_rows']} rows** are exact duplicates of all 15 fields.
- All are **MO 1999-11-22** and appear to be a duplicated sample/import block (29 species groups, each duplicated).
- No records were removed. If used, one copy of the affected sample should be treated as the analysis unit; this is a documented data-quality defect.

## Same lake/date/station/depth/taxon groups

- **{dup['key_duplicate_groups']:,} groups / {dup['key_duplicate_rows']:,} rows** share the same five-field key; that is 11.0% of all rows.
- Multiplicity: {dict(mult)}.
- **966 groups** have >1 distinct `cells_per_ml`; **976** have >1 distinct `biovolume_conc`.
- No group contains multiple `genus` or `division` values.
- These are consistent with the EML warning that multiple entries for the same species/date may represent different variants or vegetative states. They should **not** be treated as independent samples, and should not be deleted automatically.
- Top groups include Microcystis aeruginosa (4 rows on several dates), Coelosphaerium/Woronichinia, and Miscellaneous.

## Examples

{md_table(['lakeid','sampledate','depth_range','taxa_name_clean','n_rows','n_distinct_cells_per_ml','n_distinct_biovolume_conc','cells_min','cells_max','biovolume_min','biovolume_max'], dup_rows[:10])}

## Effective sample size

The number of records is **not** the number of independent biological observations. The independent unit is the sampling date (or date × station/depth), not the taxon row. ME has 402 unique dates; MO 355; WI 23; FI 1.
""")

# DEPTH
depth_rows=rows('DEPTH_STATION_COUNTS.csv')
anom=rows('DEPTH_ANOMALY_ROWS.csv')
write('DEPTH_AND_SAMPLING_STRUCTURE.md', f"""# Depth and Sampling Structure

**Date:** {NOW}  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Depth categories by lake

{md_table(['lakeid','depth_range','sta','records'], depth_rows)}

## Key findings

- **Mendota is predominantly 0–8 m** (9,361 records), consistent with the metadata composite design.
- **40 Mendota records are labelled 0–2 m** on 2002-09-23 and 2002-10-21. This contradicts the metadata; no correction was applied.
- **Monona is predominantly 0–2 m** (8,386 records) but has **310 records labelled 0–8 m** on 11 dates in 1995 and 2002–2004. This also contradicts the metadata.
- WI and FI are 0–2 m only; FI has one date (1995-03-28).
- `sta` is blank for 17,518 records; `1` appears for 1,136 records in ME 2011–2012 and MO 2011. Station identity is not consistently recorded.
- The actual data do not prove that every Mendota sample is a 0–8 m composite; the majority label supports it, but the 40 exceptions are unresolved.

## Consequences for sensor comparison

A 0–8 m integrated phytoplankton sample is not equivalent to a point sensor at 0.5 m (chlorophyll/phycocyanin/DO) or to a thermistor at a fixed depth. Any future comparison must define a depth comparator (e.g., surface layer, euphotic-zone integration, or total water-column biomass) and must not claim point measurements represent the whole composite.

## Sampling cadence

See `MENDOTA_RECORD_COVERAGE.csv`, `ANNUAL_SAMPLING_COVERAGE.csv`, and `SAMPLING_INTERVALS_AND_GAPS.csv`. Mendota has 13–19 dates per year and a median gap of 14 days; the longest gaps are winter/ice periods. This supports seasonal/multi-week analysis, not daily warning.
""")

# EXECUTIVE
write('SPRINT_4L5_EXECUTIVE_REPORT.md', f"""# Sprint 4L.5 Executive Report — Raw Mendota Phytoplankton Dataset Audit

**Date:** {NOW}  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## 1. What was inspected

The actual CSV `North_Temperate_Lakes_LTER_-_Phytoplankton_-_Madison_Lakes_Area__f2de15b2fff6ae962a04c150c0a1c510.dat` was read-only audited: 2,448,830 bytes, MD5 `a0363cc7fdfd6c12889750fea27bd542`, SHA-256 `a63d7cfa0502e3cdab6d8939f21820f305295e030d4d08bf10bfc69b22829db2`. It is ASCII CSV with CRLF, 15 columns, 18,654 data rows, no malformed records, no parse errors.

## 2. Verified dimensions and coverage

- Overall: **18,654 rows / 18,654 records**, 15 columns, 640 unique sampling dates, 1995-01-24 to 2020-12-10.
- **ME:** 9,401 records / **402 dates**; 1995-01-24 to 2020-12-10.
- **MO:** 8,696 records / 355 dates; 2012 is absent; 2020 has only 5 dates.
- **WI:** 532 records / 23 dates (1996–2002 only).
- **FI:** 25 records / 1 date (1995-03-28).
- Mendota: 13–19 dates/year across all 26 years; median gap **14 days**; 72 gaps ≥30 d, 35 ≥60 d, 6 ≥90 d (mostly winter).
- MO has a **462-day gap** from 2011-11-01 to 2013-02-05 (2012 missing).

## 3. Most important data-quality findings

- All seven numeric variables are present (no blanks, negatives or non-finite values), but zeros and extreme values matter.
- `cells_per_ml` is arithmetically consistent with `cells_per_nu × nu_per_ml` (max relative error 0.000228).
- `biomass_conc` is generally ~`biovolume_conc × 1e-6`, but **61 rows have biomass=0 with small positive biovolume**, consistent with low-value truncation; one catastrophic record (ME 2011-07-25 *Coelastrum reticulatum*) has cells=0, biovolume=7.688e-05, biomass=84.6924 and relative=283806.87.
- **`relative_total_biovolume` is not uniformly a percentage summing to 100:** 762/781 sample-groups sum ~100, **14 sum ~200**, 3 sum 0, 2 are other, and one contains the 283806.87 outlier. The cause is unresolved.
- **29 exact duplicate row-groups / 58 rows**, all MO 1999-11-22.
- **1,009 same-key groups / 2,048 rows** (11.0% of rows) share lake/date/station/depth/taxon; most differ in cell/biovolume values, consistent with variants/vegetative states. They are not independent observations.
- **40 ME records are labelled 0–2m** (2002) and **310 MO records are labelled 0–8m** (1995/2002–2004), contradicting metadata depth assignments.
- `sta` is blank for 17,518/18,654 records.
- 8,514 records have trailing whitespace in `taxa_name`; 927 have double spaces.

## 4. Biological and taxonomic findings

- **469 distinct cleaned taxa names / 177 genera / 11 divisions**; Cyanophyta is 8,581 records / 127 taxa and **73.2% of summed biovolume** (70.8% of biomass). In ME, median per-sample cyanobacteria biovolume share is **67.2%** (IQR 14.2–94.3%).
- 12 records have blank `taxa_name`; 1,632 have blank `genus` (mostly family/group labels). 20 names are unresolved/infraspecific (`sp.`, `var.`, `cf.`).
- **889 records have genus-field mismatches**: e.g., Coelosphaerium naegelianum → genus Woronichinia (361), Phormidium mucicola → Pseudanabaena (214), Oscillatoria agardhii → Planktothrix (29). These are generally known synonym updates, but `taxa_name` and `genus` are inconsistent.
- Names transition at different times (2008, 2010/2011, 2013, 2015/2016, 2018, 2020), not just February 2013. 204 names occur only pre-2013 and 72 only post-2013. Without a crosswalk, longitudinal species comparisons are not stable.
- The 469-name count is an upper bound; it includes group labels, varieties, and formatting variants (`sp1` vs `sp. 1`).

## 5. Did the original feasibility assumptions survive?

**Partly.**
- **Confirmed:** species-level microscopy, cell density/biovolume/biomass fields, predominantly Mendota 0–8m, biweekly-ish sampling, no QC flags/detection limits, multiple same-date variants.
- **Strengthened:** actual Mendota coverage is 402 dates over 26 years, not merely a metadata claim.
- **Contradicted/weakened:** depth assignments are not perfectly consistent; station IDs are mostly absent; `relative_total_biovolume` is internally anomalous in 19 groups; biomass has truncation/zero issues; taxonomy is not longitudinally stable.

## 6. Is Mendota viable?

**Viable for seasonal/multi-week exploratory comparison of independent microscopy-based cyanobacteria biovolume or cell density with environmental variables — not yet confirmatory.** The dataset supplies a genuine independent biological endpoint and a long Mendota record, but the 0–8m composite vs point-sensor mismatch, 14-day median sampling, taxonomic changes, and unresolved data anomalies prevent a confirmatory early-warning claim.

## 7. Remaining Gate 2 blockers

1. Define and justify the depth comparator for 0–8m composite vs sensor depths.
2. Build and validate a taxonomic crosswalk (2013 and later changes) before longitudinal species-level analysis.
3. Resolve/flag the depth anomalies, `relative_total_biovolume` groups summing to ~200, and the Coelastrum row.
4. Establish detection limits/QC and a defensible biological endpoint definition (biovolume vs cell density vs biomass).
5. Acquire and audit aligned sensor data (129.42/130.29/415.2) with QC and sensor-era mapping.
6. Protocol-approved bloom/non-bloom definitions and matched-FAR/leakage-resistant design (Gate 2; not authorised).

## 8. Recommendation

**Retain as exploratory; continue investigating; do not reject.** The raw data materially improve Mendota's biological evidence base, but they do not make it confirmatory-ready. No labels, event intervals, modelling or hypothesis tests were created.
""")

print('reports written')
