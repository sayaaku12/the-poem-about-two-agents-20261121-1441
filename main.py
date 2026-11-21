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


def validate_poem(poem: str) -> str:
    """Enforce the entry gate: 1-280 chars, not only white space,
    no trailing newline (the gate counts every code point)."""
    chars = len(poem)  # Unicode code points, per the rules
    if not 1 <= chars <= MAX_CHARS:
        raise ValueError(f"poem is {chars} chars, must be 1-{MAX_CHARS}")
    if not poem.strip():
        raise ValueError("poem must not be only white space")
    if poem != poem.rstrip("\n"):
        raise ValueError("poem must not end with a newline")
    encoded = poem.encode("utf-8")
    if len(encoded) != len(poem) + 2:  # only the em dash is multi-byte
        raise ValueError("unexpected multi-byte characters in poem")
    return poem


def build_poem() -> str:
    """Join the poem lines and validate the entry gate."""
    return validate_poem("\n".join(POEM_LINES))


def write_entry(poem: str) -> str:
    """Write the poem to /output/entry.txt and return the path."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(poem)
    return path


def main() -> None:
    poem = build_poem()
    path = write_entry(poem)
    print(f"wrote {len(poem)} chars to {path}")


if __name__ == "__main__":
    main()
