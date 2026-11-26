"""Frost Alien Food Review — one-star alien review of Earth, food compliment included.

Writes one sentence (<=200 chars) to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

LINE = (
    "One star: your gravity shattered my luggage, your queues defy physics, "
    "but the noodle soup was so good I nearly forgave your entire solar system."
)


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what landed on disk must be exactly the line.
    with open(os.path.join(out_dir, "entry.txt"), "r", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
