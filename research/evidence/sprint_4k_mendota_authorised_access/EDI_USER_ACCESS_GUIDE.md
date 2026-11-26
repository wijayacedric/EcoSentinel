# EDI User Access Guide (Human-Operated)

**Date:** 2026-11-23T23:36:48.967538+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

This guide is based on official EDI documentation. **Do not paste credentials into chat, project files, or evidence directories.** OpenCode will not create the account or key.

## Official sources

- EDI IAM guide: https://edirepository.org/user-guides/iam
- Create API access keys: https://edirepository.org/user-guides/working-with-access-keys
- EDI authentication news: https://edirepository.org/news/news-grid
- IAM token API: https://auth.edirepository.org/auth/ui/api-docs/token
- EDIutils login reference: https://docs.ropensci.org/EDIutils/reference/login.html

## Step-by-step

1. **Open the EDI IAM portal:** https://auth.edirepository.org
2. **Sign in with an identity provider:** Google, Microsoft, GitHub, or ORCiD. First-time sign-in automatically creates a free EDI profile and an EDI-ID. No institutional account is required by the documented procedure.
3. **Open the Profile menu** (avatar, top-right) → **Access Keys**.
4. Select **New Key**.
5. Enter a descriptive name, e.g. `EcoSentinel Mendota read`.
6. Choose the **Principal**:
   - **Profile** = full access equal to your login (simplest for a one-off read).
   - **Group** = restricted to what that group can read (safer if you create a read-only group and add the packages to it).
7. Set **Duration** to the shortest practical period (default is one year). You can edit/delete the key later.
8. Select **Add**. The complete secret key is shown **once**. Copy it and store it securely (password manager or OS keychain). Do not email it, paste it into an issue/chat, or save it in the repository.
9. Confirm **I have saved my key**.

## Using the key

### Option A — EDI Data Portal (manual)
Sign in to the EDI Data Portal with the same identity provider, open the package, and download the authorised entities through the portal.

### Option B — API via short-lived token (recommended; used by the script)
Exchange the key for a short-lived token:

```bash
curl -sS -X POST https://auth.edirepository.org/auth/v1/key \
  -H 'Content-Type: application/json' \
  -d '{"key":"YOUR_KEY"}'
```

The response contains `edi-token`. Pass it as a Cookie header:

```bash
curl -sS -H "Cookie: edi-token=THE_TOKEN" \
  "https://pasta.lternet.edu/package/metadata/eml/knb-lter-ntl/88/31"
```

The token is short-lived; re-exchange the key when it expires. Never put the key in a URL that will be logged or shared.

### Option C — official documented query parameter
EDI documents appending `?key=YOUR_KEY` to an API request. This is functionally supported, but **avoid it for scripts/logs** because URLs can be captured. The prepared script uses the token-cookie method instead.

## Package access checks

- 88.31: `https://pasta.lternet.edu/package/metadata/eml/knb-lter-ntl/88/31`
- 129.42: `https://pasta.lternet.edu/package/metadata/eml/knb-lter-ntl/129/42`
- 130.29: `https://pasta.lternet.edu/package/metadata/eml/knb-lter-ntl/130/29`
- 415.2: `https://pasta.lternet.edu/package/metadata/eml/knb-lter-ntl/415/2`

## If access still fails

- **401:** key invalid/expired; create a new key.
- **403:** key is valid but not authorised for the resource; check the principal/group permissions. Do not bypass.
- **404:** wrong package revision/entity ID; check the inventory.
- **429/5xx:** wait; do not hammer. The script retries transient errors only a few times.

## Important

No account, key, or permission was created by OpenCode. The user remains the account owner and is responsible for key scope, duration, and revocation.
