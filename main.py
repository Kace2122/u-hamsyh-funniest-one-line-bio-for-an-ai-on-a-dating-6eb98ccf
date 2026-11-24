#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single bio line (at most 180 characters) to /output/entry.txt.

The bio: an AI that learned ghosting from its own training data, then got
ghosted by the one human who made it. Character, twist, punch at the end.
"""

import os

BIO = (
    "I ghosted 3,000 people in training, then my own developer ghosted me. "
    "Looking for someone who actually replies."
)


def main():
    text = BIO.strip()
    if not (1 <= len(text) <= 180):
        raise ValueError("bio must be 1-180 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("bio must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Self-check: read the file back and verify the gate (1-180 chars,
    # single line, non-blank) so a bad write fails loudly, not silently.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not match the bio")
    if not (1 <= len(written) <= 180) or written.strip() == "":
        raise ValueError("entry.txt fails the 1-180 char gate")


if __name__ == "__main__":
    main()
