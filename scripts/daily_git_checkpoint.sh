#!/bin/bash
# Daily EcoSentinel Git checkpoint.
# Commits and pushes only when there is new work or an unpushed commit.
# Intended to be run by a daily 23:00 automation.

set -uo pipefail

REPO="/Users/cedricbw/Documents/EcoSentinel"
LOG="$REPO/.git/daily_checkpoint.log"
cd "$REPO" || exit 1

ts() { date '+%Y-%m-%d %H:%M:%S %Z'; }
log() { printf '%s %s\n' "$(ts)" "$*" >> "$LOG"; }

export GIT_TERMINAL_PROMPT=0

# Refuse to create a commit that GitHub will reject for file size.
big="$( { git ls-files -o --exclude-standard; git ls-files -m; } | while IFS= read -r f; do
  [ -f "$f" ] || continue
  sz=$(stat -f%z "$f" 2>/dev/null || echo 0)
  if [ "$sz" -gt 99614720 ]; then printf '%s\n' "$f"; fi
done )"

if [ -n "$big" ]; then
  log "ABORT: file(s) larger than 95 MB are not ignored: $big"
  exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
  if ! git add -A; then
    log "ABORT: git add failed"
    exit 1
  fi
  if ! git diff --cached --quiet; then
    msg="Daily EcoSentinel checkpoint $(date '+%Y-%m-%d %H:%M')"
    if ! git commit -m "$msg" >>"$LOG" 2>&1; then
      log "ABORT: git commit failed"
      exit 1
    fi
    log "committed $(git rev-parse --short HEAD)"
  fi
fi

# Update the remote ref so we know whether a push is needed.
git fetch origin main --quiet 2>>"$LOG" || true
ahead=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)

if [ "$ahead" -gt 0 ]; then
  if git push origin main >>"$LOG" 2>&1; then
    log "pushed $(git rev-parse --short HEAD)"
  else
    log "ABORT: git push failed; commit retained locally for retry"
    exit 1
  fi
else
  log "no changes to push"
fi

exit 0
