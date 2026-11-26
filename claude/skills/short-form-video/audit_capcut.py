#!/usr/bin/env python3
"""Pre-export checks for a CapCut project (reads draft_info.json, changes nothing).

Usage: audit_capcut.py "<project folder or name>"
A bare name is looked up in CapCut's projects folder on macOS.

Flags:
  - captions that don't share one style (font, bold, outline, size, colour, box)
  - text in the bottom 15% or top 13% of a 9:16 frame (platform UI covers it)
  - gaps on the main video track
  - CapCut's copies of the project (template-2.tmp, Timelines/*) disagreeing with draft_info.json
Exit code 1 if anything is flagged.
"""
import glob
import json
import os
import sys
from collections import defaultdict

PROJECTS = os.path.expanduser("~/Movies/CapCut/User Data/Projects/com.lveditor.draft")
US = 1_000_000
# Text centre y in CapCut units (half canvas, up is positive). Below -0.70 sits in the bottom
# ~15% of the frame, above 0.74 in the top ~13%.
SAFE_Y = (-0.70, 0.74)


def style_key(material):
    style = json.loads(material["content"])["styles"][0]
    stroke = style.get("strokes") or []
    return json.dumps({
        "font": (style.get("font") or {}).get("path", "default"),
        "bold": style.get("bold", False),
        "size": float(style.get("size", 0)),
        "colour": style["fill"]["content"]["solid"]["color"],
        "outline": bool(stroke),
        "box": material.get("background_style", 0) and material.get("background_alpha", 0) > 0,
    }, sort_keys=True)


def audit(folder):
    path = os.path.join(folder, "draft_info.json")
    draft = json.load(open(path))
    texts = {m["id"]: m for m in draft["materials"].get("texts", [])}
    problems = []

    groups = defaultdict(list)
    for track in draft["tracks"]:
        if track["type"] != "text":
            continue
        for seg in track["segments"]:
            mat = texts.get(seg["material_id"])
            if not mat:
                continue
            start = seg["target_timerange"]["start"] / US
            words = json.loads(mat["content"])["text"]
            groups[style_key(mat)].append((start, words))
            y = seg["clip"]["transform"]["y"]
            if not SAFE_Y[0] <= y <= SAFE_Y[1]:
                problems.append(f"text at {start:.2f}s is outside the safe zone (y {y:.2f}): {words!r}")
    if len(groups) > 1:
        ranked = sorted(groups.items(), key=lambda kv: -len(kv[1]))
        problems.append(f"captions use {len(groups)} styles; most common has {len(ranked[0][1])} clips")
        for key, clips in ranked[1:]:
            first = ", ".join(f"{t:.2f}s {w!r}" for t, w in clips[:3])
            problems.append(f"  odd style {key}: {len(clips)} clip(s), e.g. {first}")

    main = next((t for t in draft["tracks"] if t["type"] == "video"), None)
    if main:
        end = 0
        for seg in sorted(main["segments"], key=lambda s: s["target_timerange"]["start"]):
            start = seg["target_timerange"]["start"]
            if start - end > US // 30:
                problems.append(f"gap on the main track at {end / US:.2f}s ({(start - end) / US:.2f}s)")
            end = start + seg["target_timerange"]["duration"]

    raw = open(path, "rb").read()
    for copy in [os.path.join(folder, "template-2.tmp")] + glob.glob(os.path.join(folder, "Timelines", "*", "draft_info.json")):
        if os.path.exists(copy) and json.load(open(copy)) != json.loads(raw):
            problems.append(f"{os.path.relpath(copy, folder)} differs from draft_info.json (CapCut may load the old one)")
    return problems


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    arg = sys.argv[1]
    folder = arg if os.path.isdir(arg) else os.path.join(PROJECTS, arg)
    problems = audit(folder)
    for p in problems:
        print(p)
    print("ok" if not problems else f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
