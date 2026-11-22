#!/usr/bin/env python3
"""Entry for the-plan-make-fun-will-carry-20261122-2138.

Writes the 265-character plan for turning $100 into the most money
in 30 days to ``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (falling back to
``/output/entry.txt`` when the variable is unset). The output is
fully deterministic: identical plan text on every run, no network
access, no randomness.
"""

import os

PLAN = (
    "Day 1: spend $30 on API credits + $12 domain. Offer a $99 AI receptionist "
    "for US dental clinics: answers calls, books via Calendly API. Find 300 "
    "clinics on Google Maps, cold-email owners daily. Close 10 = $990 + "
    "$49/mo recurring by day 30; agent runs outreach 24/7."
)


def main() -> None:
    """Validate the plan, then write it to entry.txt.

    The competition limits the plan to 280 characters, so a plan that
    is blank, whitespace-only, or over 280 code points is refused
    outright instead of being written to disk.
    """
    if not PLAN.strip() or not 1 <= len(PLAN) <= 280:
        raise SystemExit(
            f"plan rejected: needs 1-280 non-blank characters, "
            f"but has {len(PLAN)}"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
