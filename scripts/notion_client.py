"""
Minimal Notion API client for LOFI_SANCTUARY backup script.

Token-based — uses NOTION_API_KEY from .env. This is independent from
the OAuth plugin Claude Code uses; you need a separate internal
integration token for this script to work outside Claude Code.

Setup (one-time):
  1. Go to https://www.notion.so/profile/integrations
  2. Click "+ New integration" — name it "LOFI_SANCTUARY backup"
     Workspace: select the LOFI Sanctuary workspace
     Type: Internal
  3. Copy the integration secret (starts with `ntn_` or `secret_`)
  4. Add to .env at repo root:
       NOTION_API_KEY=ntn_xxxxxxxxxxxx
  5. In Notion, open the MR_C-LOFI_SANCTUARY landing page,
     click ••• → Connections → search "LOFI_SANCTUARY backup" → Connect
     (databases under it inherit the connection)
  6. Test: python scripts/notion_backup.py

The script is read-only — it queries pages but never writes to Notion.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from typing import Any


NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


class NotionError(RuntimeError):
    pass


def _headers() -> dict[str, str]:
    token = os.environ.get("NOTION_API_KEY")
    if not token:
        raise NotionError(
            "NOTION_API_KEY not set. Add it to .env at repo root. "
            "See scripts/notion_client.py for setup steps."
        )
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method: str, path: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
    url = f"{NOTION_API}{path}"
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, headers=_headers(), method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        raise NotionError(f"Notion API {e.code}: {body_text}") from e


def database_exists(database_id: str) -> bool:
    """Returns True if the database is still alive in Notion."""
    try:
        _request("GET", f"/databases/{database_id}")
        return True
    except NotionError as e:
        if "404" in str(e) or "object_not_found" in str(e):
            return False
        raise


def query_all_pages(database_id: str) -> list[dict[str, Any]]:
    """Pages through every record in a database. Returns the full raw page objects."""
    pages: list[dict[str, Any]] = []
    cursor: str | None = None

    while True:
        body: dict[str, Any] = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor

        result = _request("POST", f"/databases/{database_id}/query", body)
        pages.extend(result.get("results", []))

        if not result.get("has_more"):
            break
        cursor = result.get("next_cursor")
        # be polite to the rate limiter
        time.sleep(0.1)

    return pages
