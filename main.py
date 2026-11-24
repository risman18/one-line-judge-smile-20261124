#!/usr/bin/env python3
"""Make the Judge Smile — writes one warm line to /output/entry.txt.

Competition: u-gentle-badger-68-make-the-judge-smile-9228676d
Entry: a single line (<=200 chars) about a small good thing that
happened today, written to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) as UTF-8 text, no trailing newline.
"""

import os

LINE = (
    "This morning the warung auntie slipped an extra krupuk into my "
    "takeaway and whispered 'for the road \u2014 you look hungry'; "
    "I wasn't, but I ate it grinning all the way home."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
