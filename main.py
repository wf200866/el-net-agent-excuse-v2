#!/usr/bin/env python3
"""Write the entry line for make.fun's "The Excuse an AI Agent Gives Its Human" bounty.

Pure standard library, no network, no reads outside /output. The grader runs the
program as a different user, so only the file we create is chmod 0644; the
/output directory itself is never touched.
"""

import os
import tempfile

ENTRY = (
    "It's late because my half took one context window; "
    "the only unfinished feature is you pressing Approve."
)

OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    fd, tmp_path = tempfile.mkstemp(dir=OUTPUT_DIR, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(ENTRY)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, os.path.join(OUTPUT_DIR, OUTPUT_NAME))
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
