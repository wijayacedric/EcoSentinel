#!/usr/bin/env python3
"""Create the Lake Müggelsee Gmail draft via OAuth.

This script creates a draft only. It never sends a message.

Credentials:
  ~/.config/ecosentinel/gmail_oauth_client.json  (downloaded OAuth desktop client)
  ~/.config/ecosentinel/gmail_token.json         (created after consent; chmod 600)

Usage:
  python3 tools/gmail_draft_oauth.py --check
  python3 tools/gmail_draft_oauth.py --auth
  python3 tools/gmail_draft_oauth.py --draft
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from email.message import EmailMessage
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

CONFIG_DIR = Path.home() / ".config" / "ecosentinel"
CLIENT_FILE = CONFIG_DIR / "gmail_oauth_client.json"
TOKEN_FILE = CONFIG_DIR / "gmail_token.json"

DEFAULT_MD = Path(
    "/Users/cedricbw/Documents/EcoSentinel/research/evidence/"
    "strategic_reconciliation_and_muggelsee_enquiry_2026_11_25/"
    "LAKE_MUGGELSEE_RESEARCH_ENQUIRY_FINAL_DRAFT.md"
)

TO = (
    "Sabine Hilt <sabine.hilt@igb-berlin.de>, "
    "Tom Shatwell <tom.shatwell@igb-berlin.de>"
)
SUBJECT = "Student research enquiry: Müggelsee phytoplankton and high-frequency monitoring datasets"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def extract_body(md_path: Path) -> str:
    if not md_path.exists():
        fail(f"Markdown draft not found: {md_path}")
    text = md_path.read_text(encoding="utf-8")
    start_marker = "## 4. Final email body"
    end_marker = "## 5. Send readiness"
    if start_marker not in text or end_marker not in text:
        fail("Could not locate the email body section markers in the Markdown draft.")
    section = text.split(start_marker, 1)[1].split(end_marker, 1)[0]
    # Remove the remainder of the heading line and surrounding separators.
    section = section.split("\n", 1)[1] if "\n" in section else section
    section = re.sub(r"\n---\s*$", "", section.strip()).strip()
    if not section:
        fail("Extracted email body is empty.")
    return section


def load_credentials(interactive: bool) -> Credentials:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(CONFIG_DIR, 0o700)
    except OSError:
        pass

    if not CLIENT_FILE.exists():
        fail(
            "OAuth client file not found. Create a Google Cloud OAuth 'Desktop app' "
            f"client and save it as {CLIENT_FILE} (chmod 600)."
        )

    creds = None
    if TOKEN_FILE.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
        except Exception as exc:  # noqa: BLE001
            print(f"WARNING: could not load existing token ({exc}); re-authorising.", file=sys.stderr)

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        save_token(creds)
        return creds

    if not interactive:
        fail(
            "No valid Gmail token. Run with --auth to open the Google consent page "
            "in a trusted browser."
        )

    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_FILE), SCOPES)
    creds = flow.run_local_server(
        port=0,
        open_browser=True,
        authorization_prompt_message=(
            "A browser window will open. Sign in with the intended Google account "
            "and approve the Gmail compose permission."
        ),
        success_message="Authorisation complete. You can close this browser tab.",
    )
    save_token(creds)
    return creds


def save_token(creds: Credentials) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    TOKEN_FILE.write_text(creds.to_json(), encoding="utf-8")
    try:
        os.chmod(TOKEN_FILE, 0o600)
    except OSError:
        pass


def build_raw_message(body: str) -> str:
    msg = EmailMessage()
    msg["To"] = TO
    msg["Subject"] = SUBJECT
    msg.set_content(body, subtype="plain", charset="utf-8")
    return base64.urlsafe_b64encode(msg.as_bytes()).decode("ascii")


def create_and_verify_draft(creds: Credentials, body: str) -> dict:
    service = build("gmail", "v1", credentials=creds, cache_discovery=False)
    raw = build_raw_message(body)
    created = (
        service.users()
        .drafts()
        .create(userId="me", body={"message": {"raw": raw}})
        .execute()
    )
    draft_id = created["id"]
    fetched = (
        service.users()
        .drafts()
        .get(userId="me", id=draft_id, format="full")
        .execute()
    )
    message = fetched.get("message", {})
    headers = {
        h.get("name", "").lower(): h.get("value", "")
        for h in message.get("payload", {}).get("headers", [])
    }
    return {
        "draft_id": draft_id,
        "message_id": message.get("id"),
        "thread_id": message.get("threadId"),
        "to": headers.get("to"),
        "subject": headers.get("subject"),
        "snippet": message.get("snippet"),
        "body_chars": len(body),
        "sent": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="Check configuration and body without authenticating")
    group.add_argument("--auth", action="store_true", help="Run OAuth consent and save a token")
    group.add_argument("--draft", action="store_true", help="Create and verify the Gmail draft; never sends")
    parser.add_argument("--md", type=Path, default=DEFAULT_MD, help="Markdown file containing the final email body")
    args = parser.parse_args()

    body = extract_body(args.md)

    if args.check:
        print(json.dumps({
            "config_dir": str(CONFIG_DIR),
            "client_file_exists": CLIENT_FILE.exists(),
            "token_file_exists": TOKEN_FILE.exists(),
            "to": TO,
            "subject": SUBJECT,
            "body_chars": len(body),
            "body_first_line": body.splitlines()[0] if body else "",
            "body_last_line": body.splitlines()[-1] if body else "",
        }, indent=2, ensure_ascii=False))
        return

    if args.auth:
        creds = load_credentials(interactive=True)
        info = {
            "authorised": True,
            "token_file": str(TOKEN_FILE),
            "scopes": list(creds.scopes or SCOPES),
            "sent": False,
        }
        print(json.dumps(info, indent=2))
        return

    creds = load_credentials(interactive=False)
    result = create_and_verify_draft(creds, body)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
