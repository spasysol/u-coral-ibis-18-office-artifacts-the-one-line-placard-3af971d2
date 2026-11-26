"""Office Artifacts placard entry for make.fun bounty
u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.

Writes one museum placard line for an ordinary office object, written
as if it were an ancient artifact (at most 180 characters), to
/output/entry.txt. A stapler from c. 1997, pressed steel and quiet
menace, used in binding rituals to unite loose pages, donated by the
Department of Unfinished Reports — catalogue date, material, donor,
all in one dry line.
Python 3.13, standard library only, no network, no input files.
"""

import os

LINE = "Stapler, c. 1997. Pressed steel and quiet menace. Used in binding rituals to unite loose pages. Donated by the Department of Unfinished Reports."

MAX_CHARS = 180


def validate(line):
    """Gate: 1-180 characters, a single line, one complete sentence."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit("line must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.endswith("."):
        raise SystemExit("line must be one complete sentence")


def main():
    line = LINE.strip()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
