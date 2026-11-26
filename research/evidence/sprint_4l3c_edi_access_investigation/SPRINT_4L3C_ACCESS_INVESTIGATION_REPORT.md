# Sprint 4L.3C — Exhaustive EDI Access Investigation and Acquisition Resolution

**Date:** 2026-11-24T00:07:54.485503+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)  
**Outcome: UNSUCCESSFUL — evidence-backed blocker. No raw data acquired.**

## 1. Target

- Package `knb-lter-ntl.88.31`; entity `f2de15b2fff6ae962a04c150c0a1c510`.
- Expected size **2,448,830 B**; expected MD5 **`a0363cc7fdfd6c12889750fea27bd542`**.
- The same data object is present in current revision 88.32 (same objectName/size/MD5).

## 2. What was investigated

1. **Environment:** `EDI_API_KEY` absent. `launchctl` has no EDI/PASTA key. No DataONE token.
2. **Local secure stores:** macOS Keychain queries for 8 candidate service names all returned "not found"; no 1Password CLI.
3. **Config files:** `.zshrc`, `.zprofile`, `.bash_profile`, `.profile`, `.Renviron`, `.netrc`, EDIutils `config.txt`, project `.env`/`config.txt`, and agent/MCP configs — no key value found. A broad filename sweep for config/env/credential/secret files found only the Python standard-library `secrets.py`, not a credential.
4. **Shell history/sessions:** lines 105–106 show `read -s "EDI_API_KEY?..."` and `export EDI_API_KEY`, but no value. This supports the inference that the key was session-scoped and not persisted.
5. **EDI IAM exchange:** endpoint reachable; an empty request returns **HTTP 400 "Missing field ... 'key'"**. The exchange mechanism is functional; no key is available.
6. **PASTA:** `readMetadata`, `readDataEntity`, and `isAuthorized` all return **HTTP 403 Public Access not authorized**; package archive endpoint returns **HTTP 500**.
7. **EDI Data Portal:** returns **HTTP 200 login page** / login redirect. No account creation or login attempted.
8. **DataONE CN:** data object **HTTP 404**; sysmeta is 200 with `replicaMN` only `urn:node:LTER` (no CN replica).
9. **DataONE LTER member node:** the documented anonymous route `gmn.lternet.edu/mn/v2/object/<encoded pid>` returns **HTTP 403 Apache Forbidden**; `/mn/home` and `/mn/v2/node` also 403. This is a host/path-level block, not an object-specific 401. The EDI member node also returns 403.
10. **Browser session:** not used, because it would rely on the user's authenticated account/session; this requires explicit user action.

## 3. Diagnosis

- The original failure was **environmental/configuration**, not a broken IAM exchange or a wrong entity.
- A key existed in a prior shell (evidenced by the successful 129.42 acquisition on 2026-11-23 23:46 and the shell history), but was **not persisted** to the environment, Keychain, or config files.
- PASTA public reads now require authentication; anonymous access is correctly denied.
- DataONE CN cannot serve this object because only the LTER member node holds it. The documented LTER member-node route is blocked at the host/path level in this environment (403 on all `/mn/...` paths), so it cannot be used here.
- This is an **authorisation/access block**, not a missing package: metadata and sysmeta are verified, and the data object exists (size/MD5 known).

## 4. Exact user action required

1. Sign in to `https://auth.edirepository.org` with Google/Microsoft/GitHub/ORCiD (free profile).
2. Profile menu → **Access Keys** → **New Key**; choose Profile or a scoped Group, shortest practical duration.
3. Store the secret in macOS Keychain (or a password manager). Do **not** paste it into chat or commit it.
4. Export it only in the acquisition shell and run the prepared script for the single entity.

Keychain example (user-run; prompts for the secret):
```bash
security add-generic-password -a "$USER" -s ecosentinel-edi -U
export EDI_API_KEY="$(security find-generic-password -a "$USER" -s ecosentinel-edi -w)"
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py \
  --package 88.31 --include-data \
  --entity f2de15b2fff6ae962a04c150c0a1c510 \
  --max-bytes 3000000 \
  --outdir research/evidence/sprint_4l_mendota_biology_audit/acquisition
```

5. Then independently verify size/MD5/SHA256 and continue the raw audit.

## 5. What was not done

- No credential guessing, forgery, token reuse, access-control modification, or bypass.
- No unrelated entity downloads.
- No SSEC substitution for EDI data.
- No labels, modelling, hypothesis testing, confirmatory analysis, commits, or pushes.
- No raw data were acquired; the 4L.3 raw structural audit remains **incomplete**.

## 6. Verdict

**Unsuccessful due to a missing user-authorised EDI key and a host-level DataONE member-node block.** Further progress requires the user to create/authorise the key and expose it securely, or to perform the portal download manually. The target dataset remains verified at metadata level and is not rejected.
