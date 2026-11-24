"""The Vacuum's Alibi: deterministically write one excuse line to /output/entry.txt."""

from pathlib import Path

LINE = "I skipped that spot on purpose: my sensors confirm something under the sofa moved first, and my warranty covers dust, not bravery."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
