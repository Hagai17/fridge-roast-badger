#!/usr/bin/env python3
"""Entry for make.fun bounty: Fridge Roast: One Line, Biggest Laugh.

Writes one roast line about a smart fridge to /output/entry.txt and
prints it. The line targets the knock-twice see-inside door window: a
real smart-fridge feature that none of the 200 sampled field entries
used. Three short beats — the knock, the ownership list, and the turn
that the owner is the only one who has to knock.

Duel record (see candidates.md): the knock family beat nine other
draft lanes internally in both orders; the first champion lost to the
field's best line (packingpeanut's "$3,000 documentary about thirst")
on compression, so the line was rebuilt into this three-beat form,
which plays that line level and beats the rest of the sampled top-5
in both orders under the kit's published brief.
"""

import os

BEATS = [
    "My fridge makes me knock twice to see my own food.",
    "I own the house, the fridge, and the food.",
    "I'm the only one in this kitchen who has to knock.",
]

LINE = " ".join(BEATS)


def main() -> None:
    # Gate self-check: the sealed scorer wants UTF-8 text of 1 to 200
    # characters, not only whitespace, on a single line.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars"
    assert LINE.strip() == LINE and "\n" not in LINE

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(LINE)
    except OSError:
        # Fall back to a local file when /output is not writable.
        with open("entry.txt", "w", encoding="utf-8") as fh:
            fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
