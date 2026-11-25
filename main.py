"""Write the one-line out-of-office reply to /output/entry.txt."""

import os
from pathlib import Path


ENTRY = (
    "Out of office until Monday; "
    "the same spreadsheet is in charge, unsupervised."
)


def main() -> None:
    """Write ENTRY verbatim, with no trailing newline."""
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
