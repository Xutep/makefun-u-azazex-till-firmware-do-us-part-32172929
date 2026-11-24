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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
