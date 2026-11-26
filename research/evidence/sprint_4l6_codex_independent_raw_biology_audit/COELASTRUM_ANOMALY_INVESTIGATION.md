# Coelastrum record anomaly investigation

## Exact raw record

The only exact taxon/date match is:

`ME,2011,2011-07-25,1,0-8m,Chlorophyta,Coelastrum reticulatum,0.00018286,0,10,0,7.688e-05,84.6924,283806.87,Coelastrum`

The 15-column header identifies values as `gald`, cells per natural unit, natural units/mL, cells/mL, biovolume concentration, biomass concentration, relative biovolume percent, genus. EML defines `gald` as a length (µm); cells/mL as cells per milliliter; biovolume as µm³/mL; biomass as mg/L assuming equal density; relative total biovolume as percent. The raw row is quoted exactly, without altering or repairing it.

## Context and cross-checks

- Group is 45 records with the same lake/date/station/depth; group relative sum is 283,906.853%, dominated by this row. Group sum of absolute biovolume values is 20,120,031.517 µm³/mL.
- `cells_per_ml = 0` agrees arithmetically with `cells_per_nu=0` despite 10 natural units/mL, which by itself is a contradiction if all fields use their stated definitions.
- The row's tiny positive biovolume (0.00007688 µm³/mL) paired with biomass 84.6924 mg/L conflicts by roughly twelve orders of magnitude with the usual conversion. Conversely, 84.6924 mg/L implies about 84,692,400 µm³/mL if the stated density conversion is used. EML's conversion makes that comparison appropriate, but the file alone cannot reveal which field is corrupt.
- The `gald` value is 0.00018286 µm. This is far below the raw dataset's measurement scale; it is not credible as a cell linear dimension under the stated unit absent a unit/decimal problem.
- Relative value exceeds 100 by a factor of 2,838.0687 for this row alone. Ordinary percentage reporting cannot explain it.

## Finding

**Classification: unresolved, internally impossible as a valid row under the documented column meanings.** A transcription/decimal shift, field/column alignment issue, unit conversion error, or upstream calculation/export defect are plausible. There is no evidence to choose among these. A single unusual cell/colony cannot account for contradictory cell counts, impossible length, biomass/biovolume conflict and a percentage >100. There is no evidence it is legitimate biological extremity.

The audit does not remove or correct this observation. Exclude it from biological interpretation only under a future documented, protocol-approved quality rule; preserve the original row and record any downstream treatment.

## Evidence needed

Original count-sheet or electronic lab record, slide review, microscope measurement units, calculation/export lineage for `gald`/biovolume/biomass/relative values, and explanation whether natural units and cells were tallied from different records. No additional raw measurements or source-owner clarification were acquired in this audit.
