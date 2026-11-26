# Depth and station critique

## Independent counts

- ME/Mendota: 9,361 rows at `0-8m`, 40 at `0-2m` (all dated 2002-09-23 or 2002-10-21, spanning two samples).
- MO/Monona: 8,386 at `0-2m`, 310 at `0-8m` (11 dates, in 1995 and 2002–2004).
- WI: 532 at `0-2m`; FI: 25 at `0-2m`.
- Station is blank on 17,518 of 18,654 rows; `1` occurs on ME 780 and MO 356 records.

The EML says standard protocol is a tube sampler/composite 0–8m for Mendota and Kemmerer water at 1m increments composited to 0–2m for the other lakes. Raw exceptions are real export values, not silently corrected. They may reflect protocol changes, legacy source records, erroneous coding, or sample-specific differences. Neither raw file nor abstract explains them. PLOS methods (1995–2011) affirm the 0–8m integrated Mendota method for that study period but do not explain the 40 shallow records in 2002.

## Consequences for point-depth sensors

Even the normal Mendota composite integrates water over 0–8 m; a buoy sensor at a fixed depth (e.g. 1m) measures a point/stratum and may diverge under stratification, vertical migration, mixing, or surface scum. The 40 shallow records are a different exposure definition and cannot be pooled uncritically with 0–8m samples. Missing station identifiers prevent an exact station match for most biological rows; station=1 on later records does not establish spatial coordinates or constant position. Date-only sample precision (no time) further limits matching to high-frequency sensor data.

An observation-level compatibility crosswalk requires original date/site/depth logs and sensor deployment location/depth history; this CSV alone cannot establish it.
