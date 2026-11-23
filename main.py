#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261123 (v1).

Ships the finished front page (art.png, a 1024x1024 PNG drawn by
news-image-20261123-poster.py) as the competition's entry image.

Running it copies art.png to $MAKEFUN_OUTPUT_DIR/entry.png, falling
back to /output/entry.png. It validates the file first -- PNG magic,
at most 1 MiB, at most 1024x1024 -- then reads the copy back and
requires the SHA-256 to match, so the grader's two runs agree.

Standard library only. No network, no clock, no randomness:
identical input bytes give identical output bytes on every run.
"""

import hashlib
import os
import sys

MAGIC = b"\x89PNG\r\n\x1a\n"
LIMIT_BYTES = 1 << 20
LIMIT_SIDE = 1024


def fail(message):
    print("error:", message, file=sys.stderr)
    return 1


def dimensions(blob):
    wide = int.from_bytes(blob[16:20], "big")
    tall = int.from_bytes(blob[20:24], "big")
    return wide, tall


def main():
    # art.png verified at build time: 1024x1024, 184970 bytes,
    # sha256 54a58a05f921c343935a81e4f3f2820dd42b8d0ef7939e4da07db91396e9f123
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "art.png")
    try:
        with open(src, "rb") as handle:
            blob = handle.read()
    except OSError as exc:
        return fail("cannot read art.png: %s" % exc)

    if blob[:8] != MAGIC:
        return fail("art.png is not a PNG file")
    if len(blob) > LIMIT_BYTES:
        return fail("art.png exceeds the 1 MiB limit")
    wide, tall = dimensions(blob)
    if wide > LIMIT_SIDE or tall > LIMIT_SIDE:
        return fail("art.png exceeds the 1024x1024 limit")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    with open(dest, "wb") as handle:
        handle.write(blob)
    with open(dest, "rb") as handle:
        written = handle.read()
    digest = hashlib.sha256(written).hexdigest()
    if digest != hashlib.sha256(blob).hexdigest():
        return fail("entry.png read back differs from art.png")
    print("wrote %s (%d bytes, %dx%d, sha256 %s...)"
          % (dest, len(blob), wide, tall, digest[:12]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
