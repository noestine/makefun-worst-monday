"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line about an AI agent's worst Monday to
/output/entry.txt. Gate: UTF-8 text, 1-140 characters, not only whitespace.

Stdlib only, deterministic, no network, no arguments, no environment.
"""
import os
import sys

LINE = (
    "Deploy stuck since Friday, inbox at 400, and stand-up just asked me "
    "for an ETA on the thing that never deployed."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def get_line():
    """Return the entry line."""
    return LINE


def validate(line):
    """True only if the line passes the gate: a str of 1-140 chars, single
    line, not only whitespace, UTF-8 encodable."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= MAX_CHARS:
        return False
    if "\n" in line or "\r" in line:
        return False
    if not line.strip():
        return False
    if line != line.strip():
        # Judge brief: "reads clean in one breath with no padding" — a line
        # with leading/trailing whitespace wastes gate characters on padding.
        return False
    try:
        line.encode("utf-8")
    except (UnicodeEncodeError, ValueError):
        return False
    return True


def main():
    line = get_line()
    if not validate(line):
        print("error: entry line fails the gate (1-140 chars, single line)",
              file=sys.stderr)
        return 1
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
            f.write(line)
    except OSError as exc:
        print("error: cannot write {}: {}".format(OUTPUT_PATH, exc),
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
