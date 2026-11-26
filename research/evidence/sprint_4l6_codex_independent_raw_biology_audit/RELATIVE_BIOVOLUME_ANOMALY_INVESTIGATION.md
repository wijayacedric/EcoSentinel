# Relative total biovolume anomaly investigation

## What the field metadata establishes

EML `knb-lter-ntl.88.31` gives `relative_total_biovolume` a definition equivalent to “relative total biovolume” and unit percent. The package abstract explains absolute biovolume: geometric cell volume × cell density; 1,000,000 µm³/mL equals 1 mm³/mL, and with the assumed cell density of water this is converted to 1 mg/L biomass. The abstract does **not** specify the relative field's denominator, inclusion/exclusion rules, aggregation key, or rounding method. Thus the field name and percent unit alone do not establish that same-date rows should sum to 100.

## Independent result

I grouped the field by `(lakeid, sampledate, sta, depth_range)`, directly summing the exported percentage rows. There are 781 observed groups: 762 total 99–101; 14 total 199–201; three total exactly zero; one totals 98.864; and one totals 283,906.853. This reproduces Sprint 4L.5. Grouping without station and/or depth results in the same empirical group membership in this dataset because observed combinations are nested, not because the intended denominator is thereby verified.

The 14 near-200 groups are not explained by a single exact-duplicate mechanism: only the MO 1999-11-22 block has exact duplicated rows, whereas the other 13 near-200 groups occur on other lake/date/depth combinations. Some same-taxon records within samples could represent variants or vegetative states, as EML explicitly permits; that permission does not show why normalized percentages sum to 200. Separate replicates/slide sets, calculation groups omitted from the export, duplicate counting, and processing defects remain possibilities—not findings.

The three zero groups are WI samples with one `Cyanophyta` row each, zero biovolume and zero relative value. These are not evidence that the full community sample had no algae: they may be cyanobacteria-only/summary rows, and the taxon field is a division-level aggregate. This is a compositional metadata concern, not a verified biological absence.

## Catastrophic sample

ME 2011-07-25, station 1, 0–8 m: 45 rows sum to 283,906.853%; recorded total absolute biovolume is 20,120,031.517 in the exported unit. The *Coelastrum reticulatum* row contributes 283,806.87 of the relative sum. If the percentages were computed as row biovolume / this group's total ×100, that row would contribute about 3.82e-10%, not 283,806.87%. But the EML never establishes that this is the denominator, so this is an arithmetic contradiction conditional on that common interpretation, plus a severe internal anomaly under any ordinary percent interpretation.

## Disposition

The field is **not safe as an analytic input** until source-owner documentation explains denominator and 200% groups and the anomalous group/row. It may be useful as a screening signal only. Do not recalculate, normalize, cap or replace it based solely on this export. Future analyses may independently derive relative shares from an adjudicated absolute-biovolume table only after deciding how repeated variants, aggregates, blank taxa, and replicate samples should be handled.
