#!/usr/bin/env python3
"""Entry program for news-image-20261119 (Python 3.13, standard library only).

Copies the front-page image this repository holds to the output directory
the grader provides ($MAKEFUN_OUTPUT_DIR, or /output by default).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT, exist_ok=True)
shutil.copy(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
