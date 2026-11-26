# DataONE Route Analysis

**Date:** 2026-11-24T00:07:54.485503+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## What was tested

- **CN sysmeta** for the data PID: HTTP 200. `authoritativeMemberNode=urn:node:LTER`; `replicaMemberNode=urn:node:LTER` only. Size 2,448,830; format `text/csv`.
- **CN object**: HTTP 404 — the CN has no replica bytes.
- **LTER member node** (documented by `edi-mcp` as keyless): `https://gmn.lternet.edu/mn/v2/object/<encoded PASTA URL>` → **403 Apache Forbidden**.
- **LTER `/mn/home` and `/mn/v2/node`** → also **403**, indicating a host/path-level block rather than an object-specific authentication failure.
- **EDI member node**: `https://gmn.edirepository.org/mn/v2/object/<pid>` → **403**.
- **DataONE authentication token**: none in environment or Keychain; not attempted.

## Interpretation

- DataONE **cannot** provide the object from CN because the only replica is on the LTER member node.
- The documented anonymous LTER member-node route is **not usable from this environment**. The 403 is not a 401 with an auth challenge; it is an Apache path/host denial.
- A DataONE bearer token would require a user account and would not obviously resolve a host/path block. It was not attempted without credentials.
- Therefore DataONE is **not a reliable acquisition route here**, even though the package metadata is discoverable.

## Reproducibility

If run from a network where `gmn.lternet.edu/mn/v2` is accessible, the documented keyless route may work. It must be verified against size/MD5 before use; do not assume success. If it works, preserve bytes and record provenance. If it remains 403, use authorised EDI access.

## No bypass

No attempt was made to circumvent the 403 via proxies, altered headers, undocumented paths, or credential reuse.
