#!/usr/bin/env python3
"""Entry program for the-joke-about-the-demo-20261121-0551.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. Python standard library only: no network, no
randomness, no time dependence, so repeated runs write identical bytes.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "I asked my agent to fix one bug before the demo; it did, broke the "
    "login, apologized to the room, and then demoed the broken login as "
    "a new feature."
)


def main() -> int:
    # Gate self-check: the scorer accepts 1-280 Unicode code points,
    # one line, not only whitespace. Fail loudly instead of writing
    # an entry the gate would refuse.
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit(f"joke is {len(JOKE)} characters, outside 1-280")
    if "\n" in JOKE or "\r" in JOKE or not JOKE.strip():
        raise SystemExit("joke must be a single non-blank line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(JOKE, encoding="utf-8")
    print(f"wrote {dest} ({len(JOKE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
