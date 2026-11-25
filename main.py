"""One Star, Written in Sap — make.fun bounty entry
u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.

Emits a single one-line 1-star review, written by a houseplant about
the human who owns it, to /output/entry.txt. The humour comes from the
plant's own grievance: the owner waters it like a man defusing a bomb,
then punishes it for leaning toward the window by dragging it away
from the sun — treating its will to live as clutter in the view.
Setup, plant's-eye detail, punch: the complaint is real, the reason
for the single star is the owner's war on sunlight.
"""

import os

# Review: a houseplant's 1-star grievance — drowned with nervous
# watering, then dragged away from the sun for "cluttering the view".
LINE = (
    "One star. He waters me like he's defusing a bomb, then drags me "
    "away from the window every time I lean toward the sun — "
    "apparently my will to live is 'cluttering the view'."
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-279 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 279, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
