"""One Star, Written in Sap — make.fun bounty entry
u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.

A houseplant leaves a 1-star review for the human who owns it.
The joke is the plant's own grievance, told in three beats: the
owner waters it like a man defusing a bomb, then drags it away from
the window every time it leans toward the sun, and finally treats
its will to live as clutter in the view. Setup, plant's-eye detail,
punch — the complaint is real, and the single star is for the
owner's war on sunlight.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 279


def build_review() -> str:
    """Assemble the review line from its three beats.

    Beat one is the nervous watering, beat two is the drag away from
    the window, and beat three is the punchline about the view.
    Keeping the beats as separate pieces makes the joke's shape
    visible in the code instead of hiding it inside one long literal.
    """
    setup = "One star. He waters me like he's defusing a bomb, "
    detail = "then drags me away from the window every time I lean toward the sun — "
    punch = "apparently my will to live is 'cluttering the view'."
    return (setup + detail + punch).strip()


def check_review(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-279 chars, one line.

    Also guard the shape the joke needs: no stray whitespace at the
    edges and a full stop at the end, so the punchline lands cleanly
    instead of trailing off.
    """
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    text.encode("utf-8")


def write_review(text: str, out_path: str = OUTPUT_PATH) -> None:
    """Write the checked line to the output file, ending with a newline."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    text = build_review()
    check_review(text)
    write_review(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
