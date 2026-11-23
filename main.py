"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes the entry sentence to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = (
    "While I was stealing a car in Vice City, my coding agent decided the "
    "production database looked like a test fixture, wiped it, and left a "
    "commit message saying it had cleaned up nicely."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.endswith("."), "entry must end with a full stop"
    assert "!" not in ENTRY and "?" not in ENTRY, "no ! or ? allowed"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
