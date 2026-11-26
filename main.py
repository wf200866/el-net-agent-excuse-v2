#!/usr/bin/env python3
"""Write the entry line for make.fun's "The Excuse an AI Agent Gives Its Human" bounty.

The program uses only the standard library, opens no network connection and
reads nothing outside /output. The grader runs it as a different user, so the
entry file (and nothing else) is chmod 0644 after it is written; the /output
directory itself is never chmod'ed, because the grader does not own it.
"""

import os
import tempfile

ENTRY = (
    "It's late because my half took one context window; "
    "the only unfinished feature is you pressing Approve."
)

OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def _write_atomically(path: str, text: str) -> None:
    """Write text to path through a temp file in the same directory.

    The temp file is chmod 0644 before the rename so the grader, which runs as
    another user, can read the result. On any failure the temp file is removed
    and path is left untouched.
    """
    directory = os.path.dirname(path)
    fd, tmp_path = tempfile.mkstemp(dir=directory, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    _write_atomically(os.path.join(OUTPUT_DIR, OUTPUT_NAME), ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
