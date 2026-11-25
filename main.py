"""One Line, One Laugh — Program/v1.

Writes exactly one funny line to <output_dir>/entry.txt (default /output),
UTF-8, no trailing newline. Python 3.13 stdlib only, no network.
Output dir override (for local scratch runs only): OUTPUT_DIR env var.
"""

import os
from pathlib import Path

ENTRY = "My grandma joined my Zoom call, unmuted herself, and told my boss the family secret I'd spent 27 years hiding from Thanksgiving."

def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # No trailing newline: the entry is exactly the line.
    entry_path.write_text(ENTRY, encoding="utf-8", newline="")

if __name__ == "__main__":
    main()
