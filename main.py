#!/usr/bin/env python3
"""Entry program for news-image-20261119 (Python 3.13, standard library only).

Copies the front-page image this repository holds to the output directory
the grader provides ($MAKEFUN_OUTPUT_DIR, or /output by default).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
SOURCE = os.path.join(HERE, "entry.png")

if not os.path.isfile(SOURCE):
    raise SystemExit("news-image-20261119: entry.png is missing next to main.py")

os.makedirs(OUT, exist_ok=True)
target = os.path.join(OUT, "entry.png")
shutil.copy(SOURCE, target)
print(f"wrote {target} ({os.path.getsize(target)} bytes)")
