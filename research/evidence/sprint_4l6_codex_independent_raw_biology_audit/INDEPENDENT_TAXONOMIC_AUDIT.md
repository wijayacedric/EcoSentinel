# Independent taxonomic audit

## Literal counts and their limits

The CSV has 11 division strings, including `Miscellaneous`; 8,581 records with `division=Cyanophyta`. It has 468 unique nonblank stripped taxon names (469 if blank is counted) and 176 nonblank genus values (177 if blank is counted). The 4L.5 totals are therefore each one high as named-value counts. The 889 genus mismatch count reproduces as a mechanical check: for nonblank `genus`, compare its string with the first token of `taxa_name` after trimming. It does not mean 889 wrong identifications. 12 rows have blank taxon and 1,632 blank genus. Thousands of trailing spaces and double spaces make normalization material.

The 204 pre-2013-only and 72 post-2013-only values reproduce using a cutoff and exact-string sets. They mix name changes, actual presence/absence, changes in resolution, and recuration; they are not direct measures of ecological turnover. EML states February 2013 updates include accepted-name changes, changes from genus to species based on PhycoTech experience, and slide revisits to resolve taxonomic uncertainty. The revised labels therefore encode both nomenclatural and retrospective identification changes.

20 “unresolved/infraspecific” names reproduce only as a regex set (`sp`, `spp`, `var`, `cf`), 1,038 records. This rule misses some unresolved labels and may overflag strings. It is not an authoritative taxonomic audit.

## Challenge to 17 proposed mappings

The Sprint 4L.5 table was explicitly candidate-only and cited an ITRC harmful-cyanobacteria crosswalk. I treat it as a lead, not a lake-specific verification. Taxonomic sources disagree, and a name mapping is not proof that the same organism was reidentified in every sample.

| 4L.5 mapping | Independent assessment |
|---|---|
| Anabaena circinalis → Dolichospermum circinale | Genus-level transfer is a candidate within the planktonic Anabaena revision, but the exact circinalis taxon concept needs direct authority/source validation. The 2024 checklist shows continuing reassessment of cyanobacterial names. Candidate, not safe one-to-one. |
| A. lemmermannii → D. lemmermannii | Consistent with Wacklin et al. (2009) transfer framework. Strong nomenclatural candidate; same-identification continuity still unverified. |
| A. planctonica → D. planctonicum | Candidate genus/species recombination; check authorship/concept. Not proof this dataset's historic morphotype was re-reviewed. |
| A. crassa → D. crassum | Candidate recombination, but exact species concepts and spelling/authorship need authority record. |
| A. spiroides → D. spiroides | Candidate recombination; mapping cannot replace slide/method history. |
| A. macrospora → D. macrosporum | Candidate; grammatical ending change is expected in genus transfer; verify authority and taxon concept before aggregation. |
| A. flos-aquae → Dolichospermum flosaquae | Broad genus-transfer candidate, but raw current counterpart absent and name usage can vary with strains/taxonomic treatment. No harmonization. |
| A. mendotae → D. mendotae | Supported as a validly published homotypic synonym/name relationship by LPSN; current counterpart absent in raw file. |
| Aphanizomenon issatschenkoi → Cuspidothrix issatschenkoi | Strong genus transfer candidate in cyanobacterial literature/checklists; distinct historical morphology/identity remains an issue. |
| Oscillatoria agardhii → Planktothrix agardhii | Widely used taxonomic transfer candidate, but no raw crosswalk applied; method-era identification continuity unknown. |
| O. limnetica → Pseudanabaena limnetica | Supported as synonym/name transfer in freshwater taxonomic references, but genus-field update alone is not independent confirmation. |
| Phormidium mucicola → Pseudanabaena mucicola | Conflicting authorities. LPSN currently presents Pseudanabaena mucicola as not validly published and directs to Phormidium mucicola; other biodiversity authorities list Pseudanabaena as accepted. Cannot use as settled one-to-one crosswalk. |
| Cylindrospermopsis raciborskii → Raphidiopsis raciborskii | Genus transfer recognized in modern cyanobacteria literature; species-level assignment may be taxonomically debated, no harmonization made. |
| Coelosphaerium naegelianum → Woronichinia naegeliana | Candidate synonym/name transfer supported by taxonomic references; underlying identifications may still change. |
| Lyngbya birgei → Limnoraphis birgei | Strong recombination candidate: 2013 polyphasic work separates planktonic Limnoraphis from Lyngbya. Does not establish retroactive species identity in these samples. |
| Anabaena aphanizomenoides → Sphaerospermopsis aphanizomenoides | Candidate transfer; original taxonomic concept and identifier's later treatment require source review. |
| Aphanizomenon ovalisporum → Chrysosporum ovalisporum | Outdated in current 2023+ treatment: genus now Umezakia ovalisporum, with Chrysosporum ovalisporum listed as a synonym in the Japanese National Museum freshwater cyanobacteria database. This illustrates moving taxonomy, not a stable canonical name. |

The 2024 Hungarian cyanobacteria checklist (primary scholarly taxonomic list, though geographically scoped) contains a table of updated cyanobacterial names and shows that even familiar Anabaena labels may be revised differently; it lists Aphanizomenon ovalisporum as Umezakia ovalisporum and discusses uncertain entities. It is useful as evidence of active nomenclature, not as an authority on Mendota identifications. Wacklin et al. (2009) validate the genus Dolichospermum based on planktonic Anabaena morphotypes. Komárek et al. (2013) polyphasically separate Limnoraphis. McGregor et al. (2023) is cited in a national museum database for Umezakia ovalisporum.

## Aggregation implications

Genus or division aggregation can reduce string instability only if a dated, explicit mapping is biologically credible. It can also hide species replacement, toxin/toxic-genotype differences, or non-cyanobacterial composition. `division=Cyanophyta` is a broad legacy group, not evidence of toxic or bloom-forming cyanobacteria. No crosswalk was applied in this audit. Species-level longitudinal analysis is not defensible from raw strings alone; broad cyanobacterial total remains an exploratory summary with a change-history caveat.
