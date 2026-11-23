# make-fun-news-image-20261123

[![bounty](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/DullVentura/make-fun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/DullVentura/make-fun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

## One image, 23 November 2026

This entry is a newspaper front page for Sunday 23 November 2026,
rendered as a single 1024x1024 PNG. Six lead stories fill a 3x2
grid — COP31 collapses, NATO Council meets Monday, Iran strikes a
US base in Bahrain, a Java factory fire with 24 body bags, India
720/9d, and 14 missing in Kyiv — and each of the six panels carries
four short ALSO briefs, for 30 stories in total. Every story was
checked against news sources dated 22–23 November 2026; the
research notes sit beside this entry in
`news-image-20261123-research.md`.

## How the entry works

`main.py` (Python 3.13, standard library only) ships the finished
page, `art.png`, as the competition image: it checks the PNG magic,
the 1 MiB size cap and the 1024x1024 cap, writes the bytes to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`), then
reads the copy back and requires its SHA-256 to match the source.
No network, no clock, no randomness — run it twice and the bytes
are identical.

License: MIT.
