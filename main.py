"""Write the robot band name entry to /output/entry.txt.

Deterministic, stdlib only, no network. The entry is one funny name
for a band made of robots, plus a few words on its hit song.
"""

import os

ENTRY = (
    "The Unplugged \u2014 hit single 'Low Battery (Acoustic Version)' "
    "cuts out mid-chorus when the lead singer powers down. "
    "The encore is 40 minutes of charging noises."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
