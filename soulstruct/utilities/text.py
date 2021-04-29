"""NOTE: This file is Python 3.7 compatible for Blender 2.9X use."""

__all__ = ["word_wrap", "camel_case_to_spaces", "pad_chars", "indent_lines"]

import re
import textwrap


def word_wrap(text, line_limit=50):
    return "\n".join(textwrap.wrap(text, line_limit))


def camel_case_to_spaces(camel_string: str) -> str:
    """Preserves consecutive capitals (e.g. JSONFileName -> JSON File Name) and non-alphabetical symbols.

    Needs two passes to handle cases of singular capital letters and numbers/symbols (which need spaces on both sides).
    """
    camel_string = re.sub(r"([A-Z])([A-Z])([a-z])|([0-9%]+)([A-Z])", r"\1\4 \2\3\5", camel_string)  # ABc -> A Bc
    camel_string = re.sub(r"([a-z])([A-Z])|([A-Za-z])([0-9%]+)", r"\1\3 \2\4", camel_string)  # aB -> a B
    return camel_string


def pad_chars(text, encoding=None, null_terminate=True, pad_to_multiple_of=4):
    """Pad text out to given multiple of byte length with null bytes. Optionally, encode it first."""
    if pad_to_multiple_of < 0 or not isinstance(pad_to_multiple_of, int):
        raise ValueError("pad must be an integer greater than zero.")
    if encoding is not None:
        encoded = text.encode(encoding) + (b"\0" if null_terminate else b"")
    else:
        encoded = text + ("\0" if null_terminate else "")
    pad = b"\0" if encoding is not None else "\0"
    while len(encoded) % pad_to_multiple_of != 0:
        encoded += pad
    return encoded


def indent_lines(text: str, indent=4):
    lines = text.split("\n")
    if isinstance(indent, int):
        indent = " " * indent
    return f"\n{indent}".join(lines)
