# make-fun-news-image-20261123

[![bounty](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/DullVentura/make-fun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/DullVentura/make-fun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

# news-image-20261123 — World News front page, Sunday 23 November 2026

A 1024x1024 newspaper front page summing up the day's world news:
6 lead stories in a 3x2 grid plus 4 ALSO briefs per panel — 30 stories
in total. Leads: COP31 collapses, NATO Council meets Monday, Iran
strikes US base in Bahrain, Java factory fire (24 body bags),
India 720/9d, 14 missing in Kyiv. All stories verified against
news sources dated 22-23 November 2026 (see
`news-image-20261123-research.md` beside the entry).

`main.py` (Python 3.13, standard library only) copies `art.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`),
validating PNG magic, the 1 MiB size limit and the 1024x1024 limit,
and verifying the written file's SHA-256 matches. No network, no
clock, no randomness — two runs write identical bytes.

License: MIT.
