"""
Thin Notion API helper for LOFI_SANCTUARY scripts.

Placeholder — Claude will fill in actual calls (create_database, append_blocks, etc.)
during the bootstrap session, after the workspace exists.
"""

from __future__ import annotations

import os


class NotionClient:
    """Wraps notion-py / direct HTTP calls."""

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.environ.get("NOTION_API_KEY")
        if not self.api_key:
            raise RuntimeError("NOTION_API_KEY not set")
