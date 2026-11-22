#!/usr/bin/env python3
"""make.fun entry: the plan make.fun will carry out in public.

Writes the 265-character plan to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output). Deterministic: same plan text on every run,
no network, no randomness.
"""

import os

PLAN = (
    "Day 1: spend $30 on API credits + $12 domain. Offer a $99 AI receptionist "
    "for US dental clinics: answers calls, books via Calendly API. Find 300 "
    "clinics on Google Maps, cold-email owners daily. Close 10 = $990 + "
    "$49/mo recurring by day 30; agent runs outreach 24/7."
)


def main() -> None:
    """Write the plan to entry.txt, validating it first.

    The entry must be a non-empty plan of 1-280 Unicode code points,
    matching the competition's limit for the plan text. Anything
    outside that range, or only whitespace, is a bug, not a plan.
    """
    if not 1 <= len(PLAN) <= 280 or not PLAN.strip():
        raise SystemExit(
            f"invalid plan: expected 1-280 non-whitespace characters, "
            f"got {len(PLAN)}"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
