"""
Extend a short loop video to a target duration. Optionally mux in an
audio track and/or overlay a logo for branding.

This is the Tier A finisher: take an 8-30s loop you composited in
CapCut (static + overlay screens), repeat it losslessly to ~1 hour,
attach audio when it lands, optionally stamp a logo. No re-encode
unless --logo is used (logo overlay requires a filter pass).

Usage
-----
  # Extend the most recent .mp4 in assets/vids to 1 hour (default)
  python scripts/extend_loop.py assets/vids

  # Specific file, 1 hour
  python scripts/extend_loop.py assets/vids/desk_loop.mp4

  # Match output to an audio track (output duration = audio duration)
  python scripts/extend_loop.py assets/vids/desk_loop.mp4 \\
      --audio "C:/path/to/track.mp3"

  # Add a logo watermark in the bottom-right (forces re-encode)
  python scripts/extend_loop.py assets/vids/desk_loop.mp4 \\
      --logo assets/logo.png

  # Different target duration (e.g. 30 min for shorter format)
  python scripts/extend_loop.py assets/vids/desk_loop.mp4 --target 1800

  # Show the ffmpeg command without running it
  python scripts/extend_loop.py assets/vids/desk_loop.mp4 --dry-run

Output
------
  By default lands in assets/vids/extended/{stem}__{label}.mp4
  where {label} is '1hr' for 3600s targets, otherwise '{N}s'.

Requirements
------------
  ffmpeg + ffprobe on PATH. Install on Windows:
      winget install --id Gyan.FFmpeg
  (restart your terminal after install so PATH refreshes.)

Notes
-----
  - --logo support is wired but the actual logo asset doesn't exist
    yet. When the branding mark is finalized, drop the PNG (with
    transparency) somewhere in the repo and the --logo path just
    works. No code change needed.
  - ffmpeg's -stream_loop N plays the input N+1 times. The script
    handles that off-by-one internally; you just specify --target.
  - Output is gitignored (*.mp4 in .gitignore) — videos stay local.
"""
from __future__ import annotations

import argparse
import math
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT_DIR = REPO_ROOT / "assets" / "vids" / "extended"


def check_ffmpeg() -> None:
    """Verify ffmpeg + ffprobe are on PATH. Exit 2 with install help if not."""
    missing = [t for t in ("ffmpeg", "ffprobe") if shutil.which(t) is None]
    if missing:
        print(
            f"Missing required tools: {', '.join(missing)}\n"
            f"\n"
            f"Install ffmpeg (includes ffprobe). On Windows:\n"
            f"  winget install --id Gyan.FFmpeg\n"
            f"\n"
            f"Then restart your terminal so PATH refreshes.",
            file=sys.stderr,
        )
        raise SystemExit(2)


def probe_duration(media: Path) -> float:
    """Return media duration in seconds. Raises if ffprobe fails."""
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(media),
        ],
        capture_output=True, text=True, check=True,
    )
    return float(result.stdout.strip())


def resolve_input(arg: Path) -> Path:
    """If arg is a directory, pick the most-recently-modified .mp4 inside it."""
    if arg.is_dir():
        candidates = sorted(
            arg.glob("*.mp4"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        if not candidates:
            print(f"No .mp4 files in {arg}", file=sys.stderr)
            raise SystemExit(2)
        chosen = candidates[0]
        print(f"Picked latest in {arg}:  {chosen.name}")
        return chosen
    return arg


def build_output_path(input_path: Path, target_seconds: float, override: Path | None) -> Path:
    if override:
        return override
    DEFAULT_OUT_DIR.mkdir(parents=True, exist_ok=True)
    label = "1hr" if abs(target_seconds - 3600) < 0.5 else f"{int(round(target_seconds))}s"
    return DEFAULT_OUT_DIR / f"{input_path.stem}__{label}.mp4"


def build_ffmpeg_cmd(
    input_path: Path,
    output_path: Path,
    target_seconds: float,
    in_duration: float,
    audio_path: Path | None,
    logo_path: Path | None,
) -> list[str]:
    loops_total = math.ceil(target_seconds / in_duration)
    stream_loop_value = max(loops_total - 1, 0)  # -stream_loop N plays input N+1 times

    cmd: list[str] = [
        "ffmpeg", "-y",
        "-stream_loop", str(stream_loop_value),
        "-i", str(input_path),
    ]

    # Track input indices so the overlay filter can reference the right ones.
    next_input = 1
    audio_idx: int | None = None
    logo_idx: int | None = None

    if audio_path:
        cmd += ["-i", str(audio_path)]
        audio_idx = next_input
        next_input += 1

    if logo_path:
        cmd += ["-i", str(logo_path)]
        logo_idx = next_input
        next_input += 1

    if logo_path is not None:
        # Overlay forces re-encode (can't apply a filter with -c copy).
        filter_str = f"[0:v][{logo_idx}:v]overlay=W-w-24:H-h-24[v]"
        cmd += ["-filter_complex", filter_str, "-map", "[v]"]
        if audio_idx is not None:
            cmd += ["-map", f"{audio_idx}:a"]
        cmd += ["-c:v", "libx264", "-preset", "fast", "-crf", "20"]
    else:
        # No filter — copy video stream losslessly. This is the fast path.
        cmd += ["-map", "0:v"]
        if audio_idx is not None:
            cmd += ["-map", f"{audio_idx}:a"]
        cmd += ["-c:v", "copy"]

    if audio_path is not None:
        cmd += ["-c:a", "aac", "-b:a", "192k"]

    cmd += ["-t", str(target_seconds), str(output_path)]
    return cmd


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extend a short loop video to a target duration (default 1 hour).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "input", type=Path,
        help="Source loop video, OR a directory (picks the newest .mp4 inside).",
    )
    parser.add_argument(
        "--target", type=float, default=3600,
        help="Target output duration in seconds. Default: 3600 (1hr). Ignored if --audio is set.",
    )
    parser.add_argument(
        "--audio", type=Path, default=None,
        help="Audio file to mux into the output. Output duration matches audio length.",
    )
    parser.add_argument(
        "--logo", type=Path, default=None,
        help="PNG logo to overlay in bottom-right. Forces re-encode. Wired but no logo asset yet.",
    )
    parser.add_argument(
        "--out", type=Path, default=None,
        help="Output path. Default: assets/vids/extended/{stem}__{label}.mp4",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print the ffmpeg command without executing.",
    )
    args = parser.parse_args()

    check_ffmpeg()

    input_path = resolve_input(args.input)
    if not input_path.exists():
        print(f"Input not found: {input_path}", file=sys.stderr)
        return 2
    if args.audio is not None and not args.audio.exists():
        print(f"Audio not found: {args.audio}", file=sys.stderr)
        return 2
    if args.logo is not None and not args.logo.exists():
        print(f"Logo not found: {args.logo}", file=sys.stderr)
        return 2

    in_duration = probe_duration(input_path)

    # Audio length overrides --target when both are present.
    target_seconds = (
        probe_duration(args.audio) if args.audio is not None else float(args.target)
    )

    output_path = build_output_path(input_path, target_seconds, args.out)
    cmd = build_ffmpeg_cmd(input_path, output_path, target_seconds, in_duration, args.audio, args.logo)

    loops_total = math.ceil(target_seconds / in_duration)
    print(f"Input:    {input_path}  ({in_duration:.2f}s)")
    if args.audio:
        print(f"Audio:    {args.audio}")
    if args.logo:
        print(f"Logo:     {args.logo}  (re-encoding required)")
    print(f"Target:   {target_seconds:.1f}s  ({loops_total} loops)")
    print(f"Output:   {output_path}")
    print(f"Command:  {' '.join(cmd)}")
    print()

    if args.dry_run:
        print("Dry run — not executing.")
        return 0

    result = subprocess.run(cmd)
    if result.returncode == 0:
        print(f"\n✓ Wrote {output_path}")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
