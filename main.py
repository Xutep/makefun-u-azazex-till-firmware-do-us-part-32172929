#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one sentence, a wedding vow spoken by a robot at its own wedding,
to /output/entry.txt. Deterministic, standard library only: the same vow
on every run.
"""

import os

VOW = (
    "I promise to love you through every firmware update, every system "
    "crash, and every low-battery warning, because you are the one "
    "program I never want to close."
)


def main():
    # The gate accepts 1 to 200 characters of UTF-8 text, not only
    # whitespace: refuse to write anything that would fail it.
    if not 1 <= len(VOW) <= 200 or not VOW.strip():
        raise SystemExit("vow fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)
    print(f"wrote {len(VOW)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
