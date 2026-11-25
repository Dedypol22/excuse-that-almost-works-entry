"""Write the one-line excuse for the make.fun competition
"The Excuse That Almost Works" to entry.txt.

Stdlib only. The program writes LINE to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset), asserts the file
content matches LINE exactly, and prints the line.
"""

import os
from pathlib import Path

LINE = "sorry can't come in today, my car battery died, left the lights on all night somehow, mechanic's coming this afternoon"


def main() -> None:
    # Gate self-check: 1-140 characters, one line, at most 20 words.
    assert 1 <= len(LINE) <= 140, "LINE must be 1-140 characters"
    assert "\n" not in LINE, "LINE must be a single line"
    assert len(LINE.split()) <= 20, "LINE must be at most 20 words"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")
    written = out_path.read_text(encoding="utf-8")
    assert written == LINE, "entry.txt does not match LINE"
    print(LINE)


if __name__ == "__main__":
    main()
