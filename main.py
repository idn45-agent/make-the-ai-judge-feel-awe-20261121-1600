#!/usr/bin/env python3
"""Make the AI judge feel awe — entry.

Writes a single short relaxing text to /output/entry.txt
(or $ENTRY_OUTPUT for local testing).
"""

import os
import sys

ENTRY = (
    "Far from here, the sea moves in the dark, slow as before "
    "anyone counted years. Tide in. Tide out. Nothing hurries "
    "it. Above, the stars keep a watch older than their names, "
    "and the night is wide enough to hold it all \u2014 and you, "
    "one small warm thing, held inside it."
)


def main() -> int:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
