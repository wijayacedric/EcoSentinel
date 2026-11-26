#!/bin/zsh
# Secure interactive EDI key entry + authentication test + single-entity acquisition.
#
# Run this in your own local Terminal, not through chat:
#   zsh research/evidence/sprint_4l3d_existing_key_authentication/scripts/acquire_88_31_with_prompt.sh
#
# The key is read with terminal echo disabled, held only in this shell's
# environment, and unset by the EXIT trap. It is never written to disk or
# passed as a command-line argument.

set -u
set +x

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
AUTH_TEST="$SCRIPT_DIR/test_existing_key.py"
ACQUIRE="$REPO_ROOT/research/evidence/sprint_4k_mendota_authorised_access/scripts/edi_mendota_acquire.py"
OUTDIR="$REPO_ROOT/research/evidence/sprint_4l_mendota_biology_audit/acquisition"
ENTITY="f2de15b2fff6ae962a04c150c0a1c510"
EXPECTED_SIZE=2448830
EXPECTED_MD5="a0363cc7fdfd6c12889750fea27bd542"

cleanup() {
  unset EDI_API_KEY 2>/dev/null || true
}
trap cleanup EXIT INT TERM HUP

if [ ! -t 0 ]; then
  print -u2 "This helper must be run in an interactive terminal."
  exit 2
fi

unset EDI_API_KEY 2>/dev/null || true
printf 'EDI API key (input hidden): '
stty -echo
IFS= read -r EDI_API_KEY
stty echo
printf '\n'
export EDI_API_KEY

python3 "$AUTH_TEST"
auth_rc=$?
if [ "$auth_rc" -ne 0 ]; then
  print -u2 "Authentication test failed (exit $auth_rc). No acquisition attempted."
  exit "$auth_rc"
fi

python3 "$ACQUIRE" \
  --package 88.31 \
  --include-data \
  --entity "$ENTITY" \
  --max-bytes 3000000 \
  --outdir "$OUTDIR"
acq_rc=$?
if [ "$acq_rc" -ne 0 ]; then
  print -u2 "Acquisition failed (exit $acq_rc). Existing files preserved."
  exit "$acq_rc"
fi

FILE="$(find "$OUTDIR/88.31" -maxdepth 1 -type f -name "*${ENTITY}*.csv" -print -quit 2>/dev/null)"
if [ -z "$FILE" ] || [ ! -f "$FILE" ]; then
  print -u2 "Acquisition command succeeded but no expected CSV was found under $OUTDIR/88.31"
  exit 7
fi

ACTUAL_SIZE="$(stat -f '%z' "$FILE")"
ACTUAL_MD5="$(md5 -q "$FILE" | tr 'A-F' 'a-f')"
ACTUAL_SHA256="$(shasum -a 256 "$FILE" | awk '{print $1}')"

print "FILE: $FILE"
print "SIZE: $ACTUAL_SIZE (expected $EXPECTED_SIZE)"
print "MD5:  $ACTUAL_MD5 (expected $EXPECTED_MD5)"
print "SHA256: $ACTUAL_SHA256"

if [ "$ACTUAL_SIZE" -ne "$EXPECTED_SIZE" ]; then
  print -u2 "SIZE CHECK FAILED"
  exit 8
fi
if [ "$ACTUAL_MD5" != "$EXPECTED_MD5" ]; then
  print -u2 "MD5 CHECK FAILED"
  exit 9
fi

print "INTEGRITY_CHECK_PASSED"
