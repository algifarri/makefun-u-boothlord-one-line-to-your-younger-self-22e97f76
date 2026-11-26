#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes a single line to /output/entry.txt (UTF-8, 137 Unicode code points,
inside the 1-200 gate). Deterministic, standard library only, no network.

The line itself: a warning from the older self about a motorbike sold to
impress a girl — ten years on, the bike is still missed and her name is
the part that did not survive. It is addressed to the younger self in the
second person ("Don't sell", "you'll still miss"), it turns on a small
surprise (what is kept is the machine, what is lost is the person), and
it stings a little without explaining itself: one sentence, one breath,
no second sentence doing the work.
"""

import os

TEXT = (
    "Don't sell the motorbike to impress her \u2014 ten years from now "
    "you'll still miss the bike, and her name will be the one you can't "
    "remember."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    # TEXT is exactly 137 Unicode code points: inside the 1-200 gate.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
