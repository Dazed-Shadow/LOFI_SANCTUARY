"""
Snapshot every LOFI_SANCTUARY Notion database to a timestamped JSON
file in scripts/backups/.

Safe to run at any time — read-only, never writes to Notion.
Run before any destructive operation or on a regular schedule.

Usage:
  python scripts/notion_backup.py

Output:
  scripts/backups/backup_YYYY-MM-DD_HH-MM-SS.json

The backup file contains every page from every known database, plus
the row count and any errors encountered. Old backups are pruned —
the 10 most recent are kept.

Setup: see scripts/notion_client.py for one-time NOTION_API_KEY setup.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

ENV_FILE = SCRIPTS_DIR.parent / ".env"
BACKUP_DIR = SCRIPTS_DIR / "backups"

# Load .env from repo root
if ENV_FILE.exists():
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

from notion_client import NotionError, database_exists, query_all_pages

# Database IDs are read from .env. After Claude bootstraps a new DB,
# the DB ID is copied here and to .env so the script knows what to back up.
DATABASES = {
    "Asset Library":    os.getenv("NOTION_ASSET_LIBRARY_DB", "cdf82b386d3b4bd28ea250ea0d4fbb05"),
    "Prompt Library":   os.getenv("NOTION_PROMPT_LIBRARY_DB", "d41b2e5f8481479e93e12d3d209ec4ec"),
    "Outreach CRM":     os.getenv("NOTION_OUTREACH_CRM_DB", "5338e679565a4caf85fdcae8dfa39f4d"),
    "Content Pipeline": os.getenv("NOTION_CONTENT_PIPELINE_DB", "019118f7c515411ab4fe38b8e2cd1b45"),
    "Session Log":      os.getenv("NOTION_SESSION_LOG_DB", "7e81ea6e91fc4d4aad6d24620eda593a"),
    "Backlog":          os.getenv("NOTION_BACKLOG_DB", "9d0a30fd4fef43c4ad788770f8fcaaa5"),
    "Owner Log":        os.getenv("NOTION_OWNER_LOG_DB", "8e7af2a7f62d41b5a67bf530472bc1be"),
    "References":       os.getenv("NOTION_REFERENCES_DB", "7ae8adbd39b04bbba01187c5801312c5"),
    "Decisions":        os.getenv("NOTION_DECISIONS_DB", "209730e36c5245fdac808ab602a1ed6d"),
}


def main() -> int:
    BACKUP_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = BACKUP_DIR / f"backup_{timestamp}.json"

    backup = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "snapshot_type": "scripted_full",
        "databases": {},
    }

    total_pages = 0
    for name, db_id in DATABASES.items():
        if not db_id:
            print(f"  {name}: no ID configured, skipping")
            continue

        db_id_clean = db_id.replace("-", "")
        print(f"Backing up '{name}' ({db_id_clean[:8]}...)...", end=" ", flush=True)

        if not database_exists(db_id_clean):
            print("NOT FOUND in Notion — skipping")
            backup["databases"][name] = {
                "id": db_id_clean,
                "error": "database not found",
                "pages": [],
            }
            continue

        try:
            pages = query_all_pages(db_id_clean)
            backup["databases"][name] = {
                "id": db_id_clean,
                "page_count": len(pages),
                "pages": pages,
            }
            total_pages += len(pages)
            print(f"{len(pages)} records")
        except NotionError as e:
            print(f"ERROR: {e}")
            backup["databases"][name] = {
                "id": db_id_clean,
                "error": str(e),
                "pages": [],
            }

    backup_path.write_text(json.dumps(backup, indent=2, default=str))

    print(f"\n✓ Backup complete")
    print(f"  File:    {backup_path}")
    print(f"  Records: {total_pages} pages across {len(DATABASES)} databases")

    # Prune to the 10 most recent scripted backups (leave session_* snapshots alone)
    scripted = sorted(BACKUP_DIR.glob("backup_*.json"))
    if len(scripted) > 10:
        for old in scripted[:-10]:
            old.unlink()
            print(f"  Pruned old backup: {old.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
