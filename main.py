"""Entry for make.fun competition: u-suroto-two-sentence-horror-acea9253.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "The recording of my sleep-talking ends with me begging, 'Don't let it answer in my voice again.' "
LANDING = "Then there's a pause, and I hear myself, calm and awake, say: 'Too late, he's listening now.'"

ENTRY = OPENING + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
