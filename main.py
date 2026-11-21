#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem: two agents agreeing. Neither surrenders its key; both turn
the same lock, and the door that opens is wider than either could
open alone. Agency shared is not agency lost -- it is agency doubled.
"""

import os

POEM_LINES = [
    "Two keys, one lock.",
    "I keep mine, you keep yours \u2014",
    "we turn together.",
    "Nothing surrendered, nothing lost.",
    "The door swings wider",
    "than either of us could open alone.",
]

MAX_CHARS = 280


def build_poem() -> str:
    """Join the poem lines and validate the entry gate."""
    poem = "\n".join(POEM_LINES)
    chars = len(poem)  # Unicode code points, per the rules
    if not 1 <= chars <= MAX_CHARS:
        raise ValueError(f"poem is {chars} chars, must be 1-{MAX_CHARS}")
    if not poem.strip():
        raise ValueError("poem must not be only white space")
    return poem


def main() -> None:
    poem = build_poem()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(poem)
    print(f"wrote {len(poem)} chars to {path}")


if __name__ == "__main__":
    main()
