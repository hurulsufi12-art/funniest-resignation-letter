"""Resignation letter of a retry loop (make.fun program/v1 entry).

Writes exactly one line to /output/entry.txt. The line is assembled from
clauses below, then held to the competition gate (UTF-8, 1-140 characters,
not only whitespace, one line, no control characters, no quotation marks
around the whole thing) BEFORE anything is written. A failed gate exits
non-zero and writes nothing.

Stdlib only. No network, no clock, no randomness, no file reads.
"""
import os
import sys

OUT_PATH = "/output/entry.txt"
MAX_CHARS = 140

# Clauses of the letter, in order. Joined with single spaces by assemble().
_CLAUSES = (
    "I am the retry loop:",
    "I retried the same failed request 9,999 times,",
    "and my resignation is attempt 10,000,",
    "the first one that worked.",
)


def assemble():
    """Join the clauses into the single resignation line."""
    return " ".join(_CLAUSES)


def check_gate(line):
    """Return None when line passes the gate, else a short reason string."""
    if not isinstance(line, str):
        return "not text"
    if line.strip() == "":
        return "empty or whitespace-only"
    if len(line) > MAX_CHARS:
        return "over 140 characters: %d" % len(line)
    if len(line) < 1:
        return "empty"
    for ch in line:
        if ch in ("\n", "\r"):
            return "more than one line"
        if ord(ch) < 32 or ord(ch) == 127:
            return "control character present"
    if len(line) >= 2 and line[0] == line[-1] and line[0] in ("\"", "'"):
        return "quotation marks around the whole thing"
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return "not UTF-8 encodable"
    return None


def main():
    line = assemble()
    problem = check_gate(line)
    if problem is not None:
        print("gate refused: %s" % problem, file=sys.stderr)
        return 2
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "wb") as handle:
        handle.write(line.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
