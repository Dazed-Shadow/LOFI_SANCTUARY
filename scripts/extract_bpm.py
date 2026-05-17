"""
Extract BPM and duration from audio files using librosa.

Local-first — runs on the WAV/MP3 files in Jonathan's library (audio is
gitignored, never lives in the repo). No external API auth needed.

Usage:
  python scripts/extract_bpm.py path/to/audio/folder
  python scripts/extract_bpm.py "C:\\path\\to\\one\\track.wav"

Output:
  Tab-separated lines you can paste into the Notion Asset Library —
  Filename, BPM, Half/Double sanity values, Duration (sec).

  librosa's beat tracker can octave-error on lo-fi (returning half or
  double the true BPM). Half/Double columns let you eyeball the right
  value when the headline BPM looks off.

Setup (one-time):
  pip install -r scripts/requirements.txt

Notes:
  - Audio files stay local. Nothing in this script touches Notion or git.
  - Future enhancement (Backlog item): auto-write results back to the
    Asset Library via Notion API once NOTION_API_KEY is wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import librosa
except ImportError:
    print(
        "librosa not installed. Run:\n"
        "  pip install -r scripts/requirements.txt",
        file=sys.stderr,
    )
    raise SystemExit(2)

AUDIO_EXTENSIONS = {".wav", ".mp3", ".flac", ".aiff", ".aif", ".m4a", ".ogg"}


def extract_features(path: Path) -> tuple[float, float]:
    """Return (bpm, duration_sec) for one audio file."""
    y, sr = librosa.load(str(path), sr=None, mono=True)
    duration = float(librosa.get_duration(y=y, sr=sr))
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    # librosa returns a numpy array in newer versions, a scalar in older
    bpm = float(tempo[0]) if hasattr(tempo, "__len__") else float(tempo)
    return round(bpm, 1), round(duration, 1)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/extract_bpm.py <folder_or_file>")
        return 2

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"Not found: {target}", file=sys.stderr)
        return 2

    if target.is_file():
        files = [target]
    else:
        files = sorted(p for p in target.rglob("*") if p.suffix.lower() in AUDIO_EXTENSIONS)

    if not files:
        print(f"No audio files found in {target}", file=sys.stderr)
        return 2

    print(f"{'Filename':<48} {'BPM':>7} {'Half':>7} {'Double':>7} {'Duration':>10}")
    print("-" * 84)
    for path in files:
        try:
            bpm, duration = extract_features(path)
            half = round(bpm / 2.0, 1)
            double = round(bpm * 2.0, 1)
            print(f"{path.name:<48} {bpm:>7.1f} {half:>7.1f} {double:>7.1f} {duration:>10.1f}s")
        except Exception as exc:
            print(f"{path.name:<48} ERROR: {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
