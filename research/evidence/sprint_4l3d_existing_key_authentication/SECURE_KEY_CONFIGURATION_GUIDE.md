# Secure Key Configuration Guide (No Secrets)

**Date:** 2026-11-24T07:10:03.729185+00:00  
**Gate 2:** PAUSED / NOT APPROVED — Option C (Exploratory Only)

## Preferred method: local hidden terminal input

Run in **your own Terminal**, not through chat:

```bash
zsh research/evidence/sprint_4l3d_existing_key_authentication/scripts/acquire_88_31_with_prompt.sh
```

The script:
- prompts `EDI API key (input hidden):`;
- disables terminal echo with `stty -echo`;
- reads the key into `EDI_API_KEY` in that shell only;
- runs the authentication test;
- if successful, runs the single-entity acquisition;
- verifies size/MD5/SHA256;
- unsets `EDI_API_KEY` via an `EXIT` trap.

Nothing is written to shell history, a file, a log, or a command-line argument. The key is not printed.

## Manual equivalent (if you prefer)

```bash
unset EDI_API_KEY
printf 'EDI API key (input hidden): '
stty -echo
IFS= read -r EDI_API_KEY
stty echo
printf '
'
export EDI_API_KEY
trap 'unset EDI_API_KEY' EXIT INT TERM
python3 research/evidence/sprint_4l3d_existing_key_authentication/scripts/test_existing_key.py
# only if the test passes:
python3 research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py \
  --package 88.31 --include-data \
  --entity f2de15b2fff6ae962a04c150c0a1c510 \
  --max-bytes 3000000 \
  --outdir research/evidence/sprint_4l_mendota_biology_audit/acquisition
unset EDI_API_KEY
```

## Optional Keychain storage (only for repeatability)

```bash
security add-generic-password -a "$USER" -s ecosentinel-edi -U
export EDI_API_KEY="$(security find-generic-password -a "$USER" -s ecosentinel-edi -w)"
# run the acquisition; then:
unset EDI_API_KEY
```

Keychain is optional. If you use it, the secret is stored by macOS, not by the project. Do not commit a Keychain dump or export.

## Do not

- Do not paste the key into chat, an issue, a report, a screenshot, or an agent prompt.
- Do not put it in `.env`, `config.txt`, source code, logs, or git.
- Do not `echo` it or run `env`/`set` with it in scope.
- Do not pass it as a command-line argument (visible in process lists/history).
- Do not send it to any service other than `https://auth.edirepository.org`.
- Do not reuse another person's key.
- Do not create/rotate/revoke a key unless you decide to and do it yourself.

## Cleanup

`unset EDI_API_KEY` after the process; close the shell if in doubt. If the key may have been exposed, revoke it in EDI IAM and create a replacement yourself.
