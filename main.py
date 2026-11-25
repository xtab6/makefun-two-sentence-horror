#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one horror story of exactly two sentences to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Stdlib only, no network,
no reads outside this file. Cleans only the contents of the output
directory, never the directory itself (the grader mounts it).
"""

import os
import sys

STORY = (
    "Three months after my wife's funeral, I bought a parrot, and every morning "
    "it greets me from the kitchen by calling her name in my voice, exactly the "
    "way I used to. I have not spoken her name aloud since the day she died."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
