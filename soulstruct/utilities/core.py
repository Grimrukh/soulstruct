from __future__ import annotations

__all__ = [
    "PACKAGE_PATH",
    "find_dcx",
    "create_bak",
    "word_wrap",
    "camel_case_to_spaces",
    "floatify",
    "find_steam_common_paths",
    "traverse_path_tree",
    "AttributeDict",
    "BiDict",
    "unpack_from_buffer",
    "read_chars_from_bytes",
    "read_chars_from_buffer",
    "pad_chars",
    "get_startupinfo",
    "partialmethod",
    "Timer",
]

import ctypes
import functools
import io
import logging
import os
import re
import string
import struct
import subprocess
import sys
import textwrap
import time
import typing as tp
from pathlib import Path


_LOGGER = logging.getLogger(__name__)


def PACKAGE_PATH(*relative_parts):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(getattr(sys, "_MEIPASS"), *relative_parts)
    return Path(__file__).absolute().parent.joinpath("..", *relative_parts)


def find_dcx(file_path):
    """Returns DCX (preferred) or non-DCX version of the given file path.

    It doesn't matter if the file path already ends with '.dcx'. If neither file exists, FileNotFoundError is raised.
    """
    file_path = Path(file_path)
    if file_path.suffix == ".dcx":
        no_dcx, dcx = (file_path.parent / file_path.stem, file_path)
    else:
        no_dcx, dcx = (file_path, file_path.with_suffix(file_path.suffix + ".dcx"))
    if Path(dcx).is_file():
        return dcx
    elif Path(no_dcx).is_file():
        return no_dcx
    raise FileNotFoundError(f"Could not find DCX or non-DCX version of {file_path}.")


def create_bak(file_path):
    file_path = Path(file_path)
    if file_path.is_file() and not file_path.with_suffix(file_path.suffix + ".bak").is_file():
        backup_path = str(file_path.with_suffix(file_path.suffix + ".bak"))
        os.rename(str(file_path), backup_path)
        _LOGGER.info(f"Created {repr(backup_path)} backup file.")
        return True
    return False


def word_wrap(text, line_limit=50):
    return "\n".join(textwrap.wrap(text, line_limit))


def camel_case_to_spaces(camel_string: str) -> str:
    """Preserves consecutive capitals (e.g. JSONFileName -> JSON File Name) and non-alphabetical symbols.

    Needs two passes to handle cases of singular capital letters and numbers/symbols (which need spaces on both sides).
    """
    camel_string = re.sub(r"([A-Z])([A-Z])([a-z])|([0-9%]+)([A-Z])", r"\1\4 \2\3\5", camel_string)  # ABc -> A Bc
    camel_string = re.sub(r"([a-z])([A-Z])|([A-Za-z])([0-9%]+)", r"\1\3 \2\4", camel_string)  # aB -> a B
    return camel_string


def floatify(int32: int, signed=False) -> float:
    """Utility function that re-interprets a 32-bit unsigned (default) or signed integer as a single float.

    This could be useful if you have any old EMEVD scripts that incorrectly represent float event arguments as integers.
    """
    pack_fmt = "<i" if signed else "<I"
    return struct.unpack("<f", struct.pack(pack_fmt, int32))[0]


def find_steam_common_paths():
    """Not using anymore. Seems to cause 'WinError 87' OSErrors for some people for some drives."""
    steam_common_paths = []
    for drive in _get_drives():
        for arch in {"", " (x86)"}:
            common_path = Path(drive, f"Program Files{arch}/Steam/steamapps/common/")
            if common_path.is_dir():
                steam_common_paths.append(common_path)
    return steam_common_paths


def traverse_path_tree(tree, cur=()):
    if isinstance(tree, dict):
        for node, leaf in tree.items():
            for path in traverse_path_tree(leaf, cur + (node,)):
                yield path
    elif isinstance(tree, (list, tuple)):
        for item in tree:
            if isinstance(item, str):
                yield cur + (item,)
            else:  # dict
                for path in traverse_path_tree(item, cur):
                    yield path
    else:
        raise ValueError(f"Invalid type encountered in path tree: {type(tree)}")


class AttributeDict(dict):
    """Simple dict extension that redirects `__getattr__` to `__getitem__`, allowing dot notation field access."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self.update(*args, **kwargs)

    def update(self, *args, **kwargs):
        for d in args + (kwargs,):
            dict.update(self, d)
        return self


class BiDict(dict):
    def __init__(self, *args):
        """Initialized with pairs of values to be connected."""
        super().__init__()
        self.__keys = []
        self.__values = []
        for arg in args:
            if not isinstance(arg, tuple) or len(arg) != 2:
                raise ValueError("BiDict can only be initialized with (value_1, value_2) tuple pair args.")
            self.__setitem__(*arg)

    def __setitem__(self, value_1, value_2):
        """Removes any pre-existing connections using either value.

        Order of values determines whether they will appear in `keys()` or `values()`.
        """
        if value_1 in self:
            del self[value_1]
            try:
                self.__keys.remove(value_1)
            except ValueError:
                pass
            try:
                self.__values.remove(value_1)
            except ValueError:
                pass
        if value_2 in self:
            del self[value_2]
            try:
                self.__keys.remove(value_2)
            except ValueError:
                pass
            try:
                self.__values.remove(value_2)
            except ValueError:
                pass
        super().__setitem__(value_1, value_2)
        super().__setitem__(value_2, value_1)
        self.__keys.append(value_1)
        self.__values.append(value_2)

    def __delitem__(self, key):
        super().__delitem__(key)
        super().__delitem__(self[key])

    def __len__(self):
        return super().__len__() // 2

    def __iter__(self):
        return iter(self.__keys)

    def keys(self):
        """Returns first elements of all set pairs."""
        return self.__keys

    def values(self):
        """Returns second elements of all set pairs."""
        return self.__values

    def items(self):
        """Returns all set pairs in order."""
        return zip(self.__keys, self.__values)


def _get_drives():
    drives = []
    bit_mask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bit_mask & 1:
            drives.append(letter + ":/")
        bit_mask >>= 1
    return drives


def unpack_from_buffer(buffer: tp.Union[str, Path, bytes, io.BufferedIOBase], fmt, offset=None, relative_offset=False):
    """Unpack appropriate number of bytes from `buffer` using `fmt` string from the given (or current) `offset`.

    Args:
        buffer (str, Path, bytes, io.BufferedIOBase): source to read from.
        fmt (str): format string for `struct.unpack()`.
        offset (int): optional offset to seek to before reading. Old offset will be restored afterward.
        relative_offset (bool): indicates that `offset` is relative to current position.

    Returns:
        (tuple) Output of `struct.unpack()`.
    """
    if isinstance(buffer, (str, Path)):
        with buffer.open("rb") as f:
            if offset is not None:
                f.seek(offset)
            return struct.unpack(fmt, f.read(struct.calcsize(fmt)))
    elif isinstance(buffer, bytes):
        buffer = io.BytesIO(buffer)
    old_offset = buffer.tell() if offset is not None else None
    if offset is not None:
        buffer.seek(old_offset + offset if relative_offset else offset)
    data = struct.unpack(fmt, buffer.read(struct.calcsize(fmt)))
    if old_offset is not None:
        buffer.seek(old_offset)
    return data


def read_chars_from_bytes(data, offset=0, length=None, encoding=None):
    """Read characters from a bytes object (an encoded string). Use 'read_chars_from_buffer' if you are using a buffer.

    If 'length=None' (default), characters will be read until null termination from the given offset. Otherwise,
    'length' bytes will be read and all null padding bytes will be stripped from the right side.

    Use 'encoding' to automatically decode the bytes into a string before returning (e.g. 'shift_jis_2004'). Note that
    if 'utf-16-*' is specified as the encoding with no length, a double-null termination of b'\0\0' is required to
    terminate the string (as single nulls can appear in the two-byte characters).
    """
    bytes_per_char = 2 if encoding is not None and encoding.replace("-", "").startswith("utf16") else 1
    if length is not None:
        stripped_array = data[offset : offset + length].rstrip()  # remove trailing spaces
        while stripped_array.endswith(b"\0\0" if bytes_per_char == 2 else b"\0"):
            stripped_array = stripped_array[:-bytes_per_char]  # remove (pairs of) nulls
        if encoding is not None:
            return stripped_array.decode(encoding)
        return stripped_array
    else:
        # Find null termination.
        null_termination = data[offset:].find(b"\0" * bytes_per_char)
        if null_termination == -1:
            raise ValueError("No null termination found for characters.")
        array = data[offset : offset + null_termination]
        if encoding is not None:
            return array.decode(encoding)
        return array


def read_chars_from_buffer(buffer, offset=None, length=None, reset_old_offset=True, encoding=None):
    """Read characters from a buffer (type IOBase). Use 'read_chars_from_bytes' if your data is already in bytes format.

    Args:
        buffer: byte-format data stream to read from.
        offset: offset to `seek()` in buffer before starting to read characters. Defaults to current offset (None).
        reset_old_offset: if True, and 'offset' is not None, the buffer offset will be restored to its original position
            (at function call time) before returning. (Default: True)
        length: number of characters to read (i.e. the length of the returned string). If None (default), characters
            will be read until a null termination is encountered. Otherwise, if a length is specified, any spaces at
            the end of the string will be stripped, then any nulls at the end will be stripped.
        encoding: attempt to decode characters in this encoding before returning. If 'utf-16-*' is specified, this
            function will infer that characters are two bytes long (and null terminations will be two bytes). Otherwise,
            it assumes they are one byte long. You can decode the characters yourself if you want to use another
            multiple-bytes-per-character encoding.
    """
    if length == 0:
        if not reset_old_offset and not isinstance(buffer, bytes):
            buffer.seek(offset)
        return "" if encoding is not None else b""

    if isinstance(buffer, bytes):
        buffer = io.BytesIO(buffer)
    chars = []
    old_offset = None
    bytes_per_char = 2 if encoding is not None and encoding.replace("-", "").startswith("utf16le") else 1

    if offset is not None:
        old_offset = buffer.tell()
        buffer.seek(offset)

    while 1:
        c = buffer.read(bytes_per_char)
        if not c and length is None:
            raise ValueError("Ran out of bytes to read before null termination was found.")
        if length is None and c == b"\x00" * bytes_per_char:
            # Null termination.
            array = b"".join(chars)
            if reset_old_offset and old_offset is not None:
                buffer.seek(old_offset)
            if encoding is not None:
                return array.decode(encoding)
            return array
        elif len(chars) == length:
            if reset_old_offset and old_offset is not None:
                buffer.seek(old_offset)
            stripped_array = b"".join(chars)  # used to strip spaces as well, but not anymore
            stripped_array.rstrip()  # remove spaces
            while stripped_array.endswith(b"\0\0" if bytes_per_char == 2 else b"\0"):
                stripped_array = stripped_array[:-bytes_per_char]  # remove (pairs of) null characters
            if encoding is not None:
                return stripped_array.decode(encoding)
            return stripped_array
        else:
            chars.append(c)


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


def get_startupinfo():
    """Disables command window for PyInstaller `--noconsole` option.

    See `https://github.com/pyinstaller/pyinstaller/wiki/Recipe-subprocess`
    """
    if hasattr(subprocess, "STARTUPINFO"):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    else:
        si = None
    return si


class partialmethod(functools.partialmethod):
    """Wrapper for `partialmethod` that adds a `__call__` attribute to stop PyCharm from complaining."""

    __call__ = None


class Timer:

    def __init__(self, name: str):
        self._name = name

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, *exc):
        if any(exc):
            print(f"{self._name} FAILED after {time.time() - self._start} s.")
        else:
            print(f"{self._name} COMPLETED in {time.time() - self._start} s.")
