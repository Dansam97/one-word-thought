#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to entry.txt in the output directory:
"borborygmus", the rumbling sound a stomach makes. It is a real
dictionary word that is surprising on first sight, vivid enough to
hear, and carries a spark of wit in its bubbling, gurgling sound.
"""

import os

TEXT = "borborygmus"

# The gate accepts UTF-8 text of 1 to 24 characters, not only white
# space; this entry must additionally be exactly one word.
MAX_CHARS = 24


def validated_text() -> str:
    """Return TEXT after checking it against the gate and the task."""
    encoded = TEXT.encode("utf-8")  # raises if not UTF-8 encodable
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters")
    if not TEXT.strip():
        raise ValueError("entry must not be only white space")
    if len(TEXT.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if encoded.decode("utf-8") != TEXT:
        raise ValueError("entry does not round-trip as UTF-8")
    return TEXT


def main() -> None:
    text = validated_text()
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    with open(path, "rb") as fh:
        written = fh.read()
    if written != (text + "\n").encode("utf-8"):
        raise ValueError("written entry does not match the validated text")


if __name__ == "__main__":
    main()
