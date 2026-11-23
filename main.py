#!/usr/bin/env python3
"""news-image-20261123 entry (v1): publish the 23 November 2026 front page.

The page itself lives in art.png next to this file: a 1024x1024 front
page drawn by news-image-20261123-poster.py, 30 stories from 23
November 2026. Running this program places a copy at
$MAKEFUN_OUTPUT_DIR/entry.png (or /output/entry.png) after checking
the bytes are a valid PNG inside the competition's limits, then reads
the copy back and confirms the digest matches, so repeated runs agree.

Only the standard library is used. No network, no clock, no random
numbers: same input, same output, every run.
"""

import hashlib
import os
import sys

PNG_SIGNATURE = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
MAX_BYTES = 1024 * 1024
MAX_EDGE = 1024


def die(reason):
    sys.stderr.write("error: " + reason + "\n")
    return 1


def png_size(data):
    return (int.from_bytes(data[16:20], "big"),
            int.from_bytes(data[20:24], "big"))


def run():
    base = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(base, "art.png"), "rb") as f:
            data = f.read()
    except OSError as err:
        return die("art.png unreadable: %s" % err)

    if data[:8] != PNG_SIGNATURE:
        return die("art.png is not a PNG")
    if len(data) < 24:
        return die("art.png is too small to hold a PNG header")
    if len(data) > MAX_BYTES:
        return die("art.png is over 1 MiB")
    width, height = png_size(data)
    if width > MAX_EDGE or height > MAX_EDGE:
        return die("art.png is larger than 1024x1024")

    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    with open(target, "wb") as f:
        f.write(data)
    with open(target, "rb") as f:
        back = f.read()
    digest = hashlib.sha256(data).hexdigest()
    if hashlib.sha256(back).hexdigest() != digest:
        return die("entry.png does not match art.png")
    print("entry.png written: %d bytes (%d KiB), %dx%d, sha256 %s"
          % (len(data), len(data) // 1024, width, height, digest[:12]))
    return 0


if __name__ == "__main__":
    sys.exit(run())
