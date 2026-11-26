# Taxonomic Consistency Audit

**Date:** 2026-11-24T07:22:12.805937+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Counts

- **469 distinct cleaned `taxa_name` values**, **177 distinct genera**, **11 divisions**.
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

**889 records** have a `genus` that does not match the first token of `taxa_name`. Top cases:

| taxa_name_clean | genus_values | records | divisions |
|---|---|---|---|
| Chroococcaceae |  | 735 | Cyanophyta |
| Chlorococcaceae |  | 426 | Chlorophyta |
| Miscellaneous |  | 376 | Miscellaneous |
| Coelosphaerium naegelianum | Woronichinia | 361 | Cyanophyta |
| Phormidium mucicola | Pseudanabaena | 214 | Cyanophyta |
| Chrysophyceae |  | 52 | Chrysophyta |
| Oscillatoria agardhii | Planktothrix | 29 | Cyanophyta |
| Chlorophyta |  | 16 | Chlorophyta |
| Chrysocapsaceae |  | 6 | Chrysophyta |
| Pyrrhophyta |  | 4 | Pyrrhophyta |
| Cyanophyta |  | 3 | Cyanophyta |
| Dinophyceae | Dinoflagellate | 1 | Pyrrhophyta |

The largest cases are consistent with known synonym updates (Coelosphaerium→Woronichinia; Phormidium→Pseudanabaena; Oscillatoria agardhii→Planktothrix) but the `taxa_name` was not updated consistently. Others are family/group labels with blank genus. This is a **field-level inconsistency**, not necessarily an identification error.

## February 2013 update and later changes

- Pre-2013 names: 397; post-2013 names: 265; only-pre: 204; only-post: 72.
- Taxa changes are **not confined to February 2013**. Examples of first/last dates in `TAXONOMIC_CROSSWALK_CANDIDATES.csv`:
  - Oscillatoria limnetica last 2010-11-02 → Pseudanabaena limnetica first 2011-06-13.
  - Coelosphaerium naegelianum last 2010-11-09 → Woronichinia naegeliana first 2011-06-13.
  - Anabaena circinalis last 2015-11-03 → Dolichospermum circinale first 2016-11-09.
  - Cylindrospermopsis raciborskii last 2018-10-02 → Raphidiopsis raciborskii first 2020-08-06.
  - Anabaena flos-aquae and A. mendotae have no matching current-name records in this file.
- This indicates multiple nomenclature/processing changes and incomplete crosswalks, not one clean 2013 break.

## Top pre-only / post-only names (records)

| taxa_name_clean | status | records | first_date | last_date |
|---|---|---|---|---|
| Rhodomonas minuta var. nannoplanctica | only_pre_2013 | 494 | 1995-01-24 | 2010-11-09 |
| Synechococcus sp1 | only_pre_2013 | 379 | 1999-02-22 | 2010-11-09 |
| Coelosphaerium naegelianum | only_pre_2013 | 361 | 1995-07-06 | 2010-11-09 |
| Oscillatoria limnetica | only_pre_2013 | 284 | 1995-01-24 | 2010-11-02 |
| Erkenia subaequiciliata | only_pre_2013 | 274 | 1995-01-24 | 2012-10-29 |
| Phormidium mucicola | only_pre_2013 | 214 | 1995-05-23 | 2010-11-02 |
| Anabaena flos-aquae | only_pre_2013 | 145 | 1995-01-24 | 2004-08-03 |
| Chlamydomonas globosa | only_pre_2013 | 116 | 1995-01-24 | 2008-04-14 |
| Aphanothece | only_pre_2013 | 97 | 1995-08-02 | 2008-05-28 |
| Gymnodinium sp3 | only_pre_2013 | 95 | 1995-01-24 | 2010-05-10 |
| Planktolyngbya limnetica | only_post_2013 | 70 | 2015-04-02 | 2020-12-10 |
| Plagioselmis minuta | only_post_2013 | 51 | 2019-02-21 | 2020-12-10 |
| Dolichospermum circinale | only_post_2013 | 49 | 2016-07-19 | 2020-11-05 |
| Cuspidothrix issatschenkoi | only_post_2013 | 45 | 2013-07-22 | 2020-10-08 |
| Dolichospermum lemmermannii | only_post_2013 | 36 | 2016-06-20 | 2020-12-10 |
| Planktolyngbya microspira | only_post_2013 | 33 | 2016-07-06 | 2020-10-08 |
| Mucidosphaerium pulchellum | only_post_2013 | 29 | 2017-05-03 | 2020-11-05 |
| Dolichospermum planctonicum | only_post_2013 | 19 | 2016-10-03 | 2020-09-18 |
| Fragilaria filiformis | only_post_2013 | 17 | 2017-04-19 | 2020-11-05 |
| Limnoraphis birgei | only_post_2013 | 16 | 2018-07-23 | 2020-10-08 |

## Candidate crosswalk (authority: ITRC HCB-1 Appendix A Table A-1)

| historical_name | current_name_candidate | historical_records | current_records | both_present |
|---|---|---|---|---|
| Anabaena circinalis | Dolichospermum circinale | 96 | 49 | yes |
| Anabaena lemmermannii | Dolichospermum lemmermannii | 44 | 36 | yes |
| Anabaena planctonica | Dolichospermum planctonicum | 2 | 19 | yes |
| Anabaena crassa | Dolichospermum crassum | 14 | 11 | yes |
| Anabaena spiroides | Dolichospermum spiroides | 5 | 7 | yes |
| Anabaena macrospora | Dolichospermum macrosporum | 27 | 13 | yes |
| Anabaena flos-aquae | Dolichospermum flosaquae | 145 | 0 | historical_only |
| Anabaena mendotae | Dolichospermum mendotae | 71 | 0 | historical_only |
| Aphanizomenon issatschenkoi | Cuspidothrix issatschenkoi | 77 | 45 | yes |
| Oscillatoria agardhii | Planktothrix agardhii | 29 | 67 | yes |
| Oscillatoria limnetica | Pseudanabaena limnetica | 284 | 165 | yes |
| Phormidium mucicola | Pseudanabaena mucicola | 214 | 136 | yes |
| Cylindrospermopsis raciborskii | Raphidiopsis raciborskii | 114 | 12 | yes |
| Coelosphaerium naegelianum | Woronichinia naegeliana | 361 | 159 | yes |
| Lyngbya birgei | Limnoraphis birgei | 5 | 16 | yes |
| Anabaena aphanizomenoides | Sphaerospermopsis aphanizomenoides | 30 | 14 | yes |
| Aphanizomenon ovalisporum | Chrysosporum ovalisporum | 1 | 2 | yes |

**Status: candidate only.** No merger, renaming or aggregation was applied. Several historical names have no current-name counterpart in this file; several current names coexist with historical names for years.

## Taxonomic resolution

- 20 names are unresolved/infraspecific (`sp.`, `spp.`, `var.`, `cf.`), including Rhodomonas minuta var. nannoplanctica (494), Synechococcus sp. 1 (265), Cyclotella sp. 1 (82), Gymnodinium spp.
- `Miscellaneous` (376 records) is a catch-all, not a taxon.
- The 469-name count is an **upper bound on name diversity**, not a count of validated species.

## Conclusion

Longitudinal taxonomic comparison is possible only after a documented crosswalk and quality review. Raw names must not be treated as a stable species list across 1995–2020.
