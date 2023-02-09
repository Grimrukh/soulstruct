__all__ = ["word_wrap", "camel_case_to_spaces", "string_to_identifier", "pad_chars", "indent_lines"]

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


def string_to_identifier(spaces_string: str, remove_prefixes=(), preserve_models=True) -> str:
    """Attempts to convert a string to the most appropriate valid Python identifier (for entity ID enums).

    - Removes useless prefixes, like "SFX ".
    - Removes spaces and capitalizes any letters that appear after them.
    - Replaces some spaces with underscores, like spaces before "mXXXX".
    - Removes invalid characters.
    - Adds leading "_" to strings that still start with a digit.
    """
    id_string = spaces_string.strip(" ")
    model_re = re.compile(r"[cohm]\d\d\d\d") if preserve_models else None
    for prefix in remove_prefixes:
        id_string = id_string.removeprefix(prefix)
    while (space_index := id_string.find(" ")) != -1:
        remove_space = True
        if model_re and model_re.match(id_string[space_index + 1:]):  # don't capitalize "m"
            suffix = id_string[space_index + 1:]
            remove_space = False
        else:
            suffix = id_string[space_index + 1:].capitalize()
        if model_re and model_re.match(id_string[space_index - 5:space_index]):  # replace with underscore
            remove_space = False
        id_string = id_string[:space_index] + ("" if remove_space else "_") + suffix
    id_string = re.sub(r"([^\w ])", "", id_string)  # remove invalid characters
    if id_string:
        if id_string[0].isdigit():
            id_string = "_" + id_string  # add leading underscore to number
        elif id_string[0].isalpha() and not (model_re and model_re.match(id_string)):
            id_string = id_string[0].upper() + id_string[1:]
    return id_string


def pad_chars(text, encoding=None, null_terminate=True, alignment=4) -> bytes:
    """Pad text out to given multiple of byte length with null bytes. Optionally, encode it first."""
    if alignment < 0 or not isinstance(alignment, int):
        raise ValueError("pad must be an integer greater than zero.")
    if encoding is not None:
        encoded = text.encode(encoding) + (b"\0" if null_terminate else b"")
    else:
        encoded = text + ("\0" if null_terminate else "")
    pad = b"\0" if encoding is not None else "\0"
    while len(encoded) % alignment != 0:
        encoded += pad
    return encoded


def indent_lines(text: str, indent=4):
    lines = text.split("\n")
    if isinstance(indent, int):
        indent = " " * indent
    return f"\n{indent}".join(lines)
