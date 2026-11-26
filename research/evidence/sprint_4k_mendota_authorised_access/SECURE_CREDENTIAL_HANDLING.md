# Secure Credential Handling

**Date:** 2026-11-23T23:36:48.967538+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Rules

1. **Never paste an EDI API key or token into chat, issue trackers, reports, logs, screenshots, or this repository.**
2. **Never commit** keys, `config.txt`, `.env`, shell history, or token caches. Ensure `.gitignore` covers local secret files.
3. **Never place the key in a URL** used in scripts or logs. Prefer the IAM token exchange and `Cookie: edi-token=...`.
4. **Never store secrets in `research/evidence/`** or any project artifact.
5. **Do not share** a profile key; it carries your full privileges. Use a scoped group key for automation where possible.
6. **Set the shortest practical duration** and revoke keys you no longer need.
7. **Treat the key like a password.** If exposed, revoke it immediately and create a new one.

## Recommended storage

### macOS Keychain (example)
```bash
# Store once (prompts for the secret; do not use -w with a literal)
security add-generic-password -a "$USER" -s ecosentinel-edi -U

# Export into the current shell only
export EDI_API_KEY="$(security find-generic-password -a "$USER" -s ecosentinel-edi -w)"
```
The script reads `EDI_API_KEY` from the environment. It never prints or writes it.

### Password manager
Store the key in 1Password/Bitwarden/etc. and copy it into the environment for the session. Close the shell when done.

### Permissions
If a local secret file is unavoidable, use `chmod 600`, keep it outside the repository, and add it to `.gitignore`. Prefer the keychain/password manager.

## Shell hygiene

- Avoid commands that echo the key (`set -x`, `env`, `printenv`, `history`).
- Do not pass the key as a command-line argument where it appears in process lists.
- Clear the variable when finished: `unset EDI_API_KEY`.
- Do not use `?key=` in scripts that log URLs.

## Token handling

- The short-lived `edi-token` is also sensitive; keep it in memory or a protected cookie jar.
- The prepared script keeps the token in memory only and re-authenticates on a 401 once.
- Do not save tokens in the acquisition directory or provenance CSV.

## Incident response

If a key may have been exposed:
1. Revoke/delete it in IAM → Access Keys.
2. Create a new key with the minimum scope/duration.
3. Review key usage/last-used information in IAM.
4. Do not attempt to "test" the exposed key.

## What OpenCode will never do

- Request the key in chat.
- Create an account or key.
- Store the key in evidence.
- Print the key or token.
- Bypass authentication or use another person's account.
