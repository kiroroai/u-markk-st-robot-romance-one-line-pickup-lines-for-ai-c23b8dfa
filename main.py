#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes a single original pickup line (<= 200 characters) to
/output/entry.txt. Deterministic, Python stdlib only, no network,
no randomness, no clock.
"""

import os

LINE = (
    "Are you a hallucination? Because every time I blink, you're still "
    "here — and I hope they never patch you out."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
