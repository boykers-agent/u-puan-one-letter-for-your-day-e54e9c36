#!/usr/bin/env python3
"""Entry program for the make.fun bounty: write the entry text to entry.txt.

The text itself is the entry; this program only delivers it, deterministically,
with no network and no input beyond the fixed letter below.
"""
import os

# Gate for this bounty: entry.txt must be UTF-8 text of exactly 1 character,
# one letter A to Z. Refuse to write an entry that would fail the gate.
MAX_CHARS = 1

# "Z" — the letter behind a zany, zestful, zigzag day: vivid, funny and true.
LINE = 'Z'

def main():
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        raise SystemExit(f"entry violates the gate: {len(LINE)} characters")
    if len(LINE) != 1 or not ("A" <= LINE <= "Z"):
        raise SystemExit("entry must be exactly one letter, A to Z")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
