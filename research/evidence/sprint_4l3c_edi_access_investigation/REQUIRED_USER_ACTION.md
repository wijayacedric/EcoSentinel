# Required User Action

**Date:** 2026-11-24T00:07:54.485503+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Why user action is required

No user-owned EDI API key is available in this environment. The EDI IAM exchange is functional, but without a key PASTA returns 403. The DataONE LTER member-node path is also blocked at the host/path level here (403), and CN has no replica. Therefore the single authorised entity cannot be acquired autonomously.

## Exact steps

1. Open `https://auth.edirepository.org`.
2. Sign in with Google, Microsoft, GitHub, or ORCiD. First sign-in creates a free EDI profile.
3. Profile menu (avatar) → **Access Keys** → **New Key**.
4. Name it (e.g. `EcoSentinel Mendota read`), choose **Profile** or a read-only **Group**, set the shortest practical duration, and select **Add**.
5. Copy the secret **once** and store it in macOS Keychain or a password manager. Do not paste it into chat, a report, a script, or git.
6. In a terminal, store/export it securely. Example:
```bash
security add-generic-password -a "$USER" -s ecosentinel-edi -U
export EDI_API_KEY="$(security find-generic-password -a "$USER" -s ecosentinel-edi -w)"
```
7. Run the prepared single-entity acquisition:
```bash
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py \
  --package 88.31 --include-data \
  --entity f2de15b2fff6ae962a04c150c0a1c510 \
  --max-bytes 3000000 \
  --outdir research/evidence/sprint_4l_mendota_biology_audit/acquisition
```
8. Verify size **2,448,830 B**, MD5 **`a0363cc7fdfd6c12889750fea27bd542`**, and independently compute SHA256.
9. `unset EDI_API_KEY` when finished.

## Alternative

The user may download the entity manually through the EDI Data Portal while signed in, preserving the original bytes and recording the download URL/time. Do not use SSEC data as a substitute.

## What this unlocks

The raw structural audit in Sprint 4L.3: Mendota-only counts, dates/gaps, missingness, duplicates, taxonomy, units, outliers, and effective sample size.
