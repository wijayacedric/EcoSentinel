# Repeated taxonomic records audit

## Key definition and reproduced counts

On `(lakeid, sampledate, sta, depth_range, stripped taxa_name)`, there are 1,009 repeated groups with 2,048 rows (1,039 rows beyond one per key). Of these, 966 groups have >1 `cells_per_ml` value and 976 have >1 biovolume value. With untrimmed taxon strings the count falls to 996 groups/2,021 rows, indicating whitespace splits records that appear to be the same name.

The key is an audit convenience, not proven sample identity. Station is blank for most records, sample identifiers/replicate identifiers/slide identifiers are absent, and a repeated taxon can occur at different size/shape or colony states. The EML explicitly states that multiple entries for the same species/date can represent different variants or vegetative states (e.g. colonial/attached vs free cells). Thus a repeated taxon key is not itself a duplicate or mistake.

## Exact duplicates

An independent full-row equality check finds 29 duplicate groups, 58 rows / 29 excess rows, all on Monona 1999-11-22. Exact duplicates may be a duplicated block during data transfer/export. The file does not document whether these rows were duplicate records, repeat counts, or observations intentionally retained. Treat them as likely data duplication, but preserve and flag; do not quietly collapse.

## Relative percent anomalies

The 1999-11-22 group total is approximately 200%, and exact duplicate rows are present there. Exact duplication explains why at least some duplicated relative entries can inflate that group. It does not establish that all 14 near-200% groups have the same cause: 13 occur elsewhere without exact duplicates. Nor do other different-valued rows of the same taxon prove variants caused the total. Need sample/slide/lab IDs and formulas to decide.

## Aggregation and pseudoreplication

Do not sum repeated rows by taxon or treat rows as independent observations without first knowing what the repeated units represent. Summing can be justified only if each row is a disjoint count component; averaging or retaining rows can also be wrong if they represent replicate slides or variants. 1,039 excess records are not 1,039 extra independent biological samples. Effective observational unit is likely a sample/date or count unit, but the missing sample/replicate identifiers make that assumption unverifiable. Downstream analysis must be performed at a documented sampling unit after reviewing original metadata.
