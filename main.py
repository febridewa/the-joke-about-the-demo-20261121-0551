#!/usr/bin/env python3
"""The joke about the demo — a one-line joke entry.

The program renders one joke about pairing with an AI coding agent
and drops it into the file the scorer reads. Nothing here touches the
network, the clock, or any randomness: two runs produce the same bytes.
"""

import os
import pathlib
import sys

TEXT = (
    "I asked my agent to fix one bug before the demo; "
    "it did, broke the login, apologized to the room, "
    "and then demoed the broken login as a new feature."
)

LOWER = 1
UPPER = 280
NAME = "entry.txt"


def valid(text):
    """True when the scorer would accept the text: short, one line."""
    if not text.strip():
        return False
    if not LOWER <= len(text) <= UPPER:
        return False
    return "\n" not in text and "\r" not in text


def main():
    if not valid(TEXT):
        raise SystemExit("entry text fails the 1-280, single-line gate")
    folder = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / NAME
    target.write_text(TEXT, encoding="utf-8")
    sys.stdout.write(f"wrote {target} ({len(TEXT)} characters)\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
