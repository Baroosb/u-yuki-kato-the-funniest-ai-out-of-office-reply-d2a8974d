#!/usr/bin/env python3
"""Entrypoint for make.fun bounty u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d
("The Funniest AI Out-of-Office Reply").

The entry is entry.txt, beside this file: one out-of-office auto-reply
line of at most 160 characters, in the voice of an AI agent leaving for
vacation. The grader runs this program twice, with no network, and both
runs must write the same bytes to /output/entry.txt, so the program is a
plain byte-for-byte copy using only the Python standard library.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    with open(src, "rb") as f:
        data = f.read()
    # Mirror the bounty's gate locally: fail loudly if the shipped text
    # could not pass it (UTF-8, 1 to 160 characters, one line, not only
    # white space), instead of writing an invalid entry.
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 160, "entry must be 1 to 160 characters"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text, "entry must be one line"
    with open(dst, "wb") as f:
        f.write(data)
    # The two grader runs must produce identical bytes: fail loudly if
    # what landed on disk is not exactly what the repository holds.
    assert os.path.getsize(dst) == len(data), "copied text size mismatch"


if __name__ == "__main__":
    main()
