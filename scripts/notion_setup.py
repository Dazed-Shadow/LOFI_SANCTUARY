"""
LOFI_SANCTUARY — one-time Notion workspace bootstrap.

Builds the command-center structure under NOTION_ROOT_PAGE_ID:
  - Command Center landing page
  - Asset Library DB
  - Content Pipeline DB (Kanban)
  - Outreach CRM DB
  - Prompt Library DB
  - Session Log DB

Run this ONCE after the Notion integration has been granted access
to the root page in the Notion UI (page ••• -> Connections -> add integration).

Environment (.env at repo root):
  NOTION_API_KEY=secret_xxxxx
  NOTION_ROOT_PAGE_ID=<root page UUID>

This script is a placeholder. Wire it after the workspace exists and
the integration has been authorized — Claude will fill in the actual
API calls in the bootstrap session.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def main() -> int:
    api_key = os.environ.get("NOTION_API_KEY")
    root_page_id = os.environ.get("NOTION_ROOT_PAGE_ID")

    if not api_key or not root_page_id:
        print(
            "Missing NOTION_API_KEY or NOTION_ROOT_PAGE_ID in environment.\n"
            "Copy .env.example to .env and fill in both values.",
            file=sys.stderr,
        )
        return 2

    print("Notion bootstrap not yet wired.")
    print("Next step: ask Claude to fill in this script after the workspace is created.")
    print(f"Root page: {root_page_id}")
    print(f"Repo root: {Path(__file__).resolve().parent.parent}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
