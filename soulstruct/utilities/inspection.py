from __future__ import annotations

__all__ = [
    "compare_binary_data",
    "compare_binary_files",
    "print_binary_as_integers",
    "get_hex_repr",
    "write_hex_repr",
    "profile_function",
    "Timer",
    "find_errant_prints",
]

import contextlib
import cProfile
import logging
import pstats
import struct
import time
import typing as tp
from binascii import hexlify
from functools import wraps
from pathlib import Path

from colorama import init as colorama_init, Fore

_LOGGER = logging.getLogger(__name__)

colorama_init()
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET


def get_diff_indices(bytes1: bytes, bytes2: bytes) -> list[int]:
    indices = []
    for i, (b1, b2) in enumerate(zip(bytes1, bytes2)):
        if b1 != b2:
            indices.append(i)
    return indices


def try_ascii(bytes_: bytes, default=".", red_indices=()) -> str:
    """Try to decode each character in `bytes` with given encoding, returning `default` if it fails."""
    string = ""
    for i, b in enumerate(bytes_):
        string += RED if i in red_indices else GREEN
        if b <= 0x20:  # special characters
            string += default
        else:
            try:
                string += chr(b)
            except UnicodeDecodeError:
                string += default
    string += RESET
    return string


def compare_binary_data(
    data1: bytes,
    data2: bytes,
    row_size=16,
    context_rows=8,
    with_ascii=True,
    first_diff_only=False,
    header1="Data 1",
    header2="Data 2",
):
    offset = 0
    last_diff_row_offset = -1
    if with_ascii:
        pad = 4 * row_size - 1
    else:
        pad = 3 * row_size - 1

    header1 += f"({len(data1)} bytes)"
    header2 += f"({len(data2)} bytes)"

    last_rows = []  # type: list[tuple[int, bytes, bytes]]

    print(f"{YELLOW}Offset{RESET} | {YELLOW}{header1:<{pad}}{RESET} | {YELLOW}{header2:<{pad}}{RESET} ")

    while offset < min(len(data1), len(data2)):
        row1 = data1[offset : offset + row_size]
        row2 = data2[offset : offset + row_size]
        if row1 != row2:
            if offset != 0 and offset - last_diff_row_offset > row_size:
                print(f"...    | {'...':<{pad}} | {'...':<{pad}} ")
            for row_offset, r1, r2 in last_rows:
                # Print out last `context_rows` rows. All guaranteed to be identical.
                if with_ascii:
                    print(
                        f"{row_offset:06X} "
                        f"| {GREEN}{r1.hex(' ')} {try_ascii(r1)}{RESET} "
                        f"| {GREEN}{r2.hex(' ')} {try_ascii(r2)}{RESET}"
                    )
                else:
                    print(f"{row_offset:06X} | {GREEN}{r1.hex(' ')}{RESET} | {GREEN}{r2.hex(' ')}{RESET}")
            for _ in range(context_rows + 1):
                if offset >= min(len(data1), len(data2)):
                    break  # less than `context_rows` rows left
                r1 = data1[offset:offset + row_size]
                r2 = data2[offset:offset + row_size]
                red_indices = get_diff_indices(r1, r2)
                d1 = ""
                d2 = ""
                for i, h in enumerate(r1.hex(' ').split(' ')):
                    d1 += f" {RED if i in red_indices else GREEN}{h}{RESET}"
                for i, h in enumerate(r2.hex(' ').split(' ')):
                    d2 += f" {RED if i in red_indices else GREEN}{h}{RESET}"
                d1 = d1.lstrip()
                d2 = d2.lstrip()
                if with_ascii:
                    print(
                        f"{offset:06X} "
                        f"| {d1} {try_ascii(r1, red_indices=red_indices)} "
                        f"| {d2} {try_ascii(r2, red_indices=red_indices)}"
                    )
                else:
                    print(f"{offset:06X} | {d1} | {d2}")
                offset += row_size
            last_rows.clear()
            last_diff_row_offset = offset
            if first_diff_only:
                return
        else:
            last_rows.append((offset, row1, row2))
            if len(last_rows) > context_rows:
                last_rows.pop(0)
            offset += row_size

    if last_diff_row_offset == -1:
        print(f"{header1} and {header2} are identical.")


def compare_binary_files(
    file1_path: Path | str,
    file2_path: Path | str,
    row_size=16,
    context_rows=8,
    with_ascii=True,
    first_diff_only=False,
):
    """Compare two binary files, printing out any differences."""
    file1_path = Path(file1_path)
    file2_path = Path(file2_path)
    print(f"Comparing '{file1_path.name}' and '{file2_path.name}':")

    data1 = file1_path.read_bytes()
    data2 = file2_path.read_bytes()

    compare_binary_data(
        data1,
        data2,
        row_size=row_size,
        context_rows=context_rows,
        with_ascii=with_ascii,
        first_diff_only=first_diff_only,
        header1=file1_path.name,
        header2=file2_path.name,
    )


def print_binary_as_integers(file_path: Path):
    """Tool for inspecting data you assume or suspect is integers."""
    with file_path.open("rb") as file:
        offset = 0
        data = file.read(4)
        while data != -1:
            try:
                integer = struct.unpack("<i", data)
            except struct.error:
                _LOGGER.warning("Finished with less than four bytes remaining.")
                return
            print(f"{offset} | {hex(offset)} | {integer}")
            data = file.read(4)
            offset += 4


def get_hex_repr(data: bytes, with_line_numbers=True, with_unicode=False) -> str:
    hex_lines = repr(hexlify(data, sep=" ", bytes_per_sep=-16))[2:-1].split()
    hex_lines = [" ".join(hx[i:i + 2] for i in range(0, 32, 2)) for hx in hex_lines]
    if with_unicode:
        for i, line in enumerate(hex_lines):
            unicode_string = ""
            try:
                for byte in data[i * 16:(i + 1) * 16]:
                    unicode_string += (chr(byte) if byte else ".") + " "
            except UnicodeEncodeError:
                pass
            else:
                hex_lines[i] += f"    {unicode_string}"
    if with_line_numbers:
        hex_lines = [f"{i * 16:>6} | {hex(i * 16):>8}: " + hx for i, hx in enumerate(hex_lines)]
    return "\n".join(hex_lines)


def write_hex_repr(data: bytes, file_path: Path | str, with_line_numbers=True, with_unicode=False, encoding="utf-8"):
    hex_repr = get_hex_repr(data, with_line_numbers, with_unicode)
    Path(file_path).write_text(hex_repr, encoding=encoding)


def profile_function(print_count: int, sort="tottime", strip_dirs=True):
    """Decorator constructor that uses `cProfile` and prints stats."""

    def decorator(func: tp.Callable):

        @wraps(func)
        def decorated(*args, **kwargs):
            print(f"Profiling function: {func.__name__}")
            with cProfile.Profile() as pr:
                func(*args, **kwargs)
            p = pstats.Stats(pr)
            if strip_dirs:
                p = p.strip_dirs()
            p.sort_stats(sort).print_stats(print_count)

        return decorated

    return decorator


class Timer:

    def __init__(self, name: str):
        self._name = name

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, *exc):
        if any(exc):
            _LOGGER.error(f"{self._name} FAILED after {time.time() - self._start} s.")
        else:
            _LOGGER.info(f"{self._name} COMPLETED in {time.time() - self._start} s.")


@contextlib.contextmanager
def find_errant_prints():
    """Replaces builtin `print` with a version that prints the file, line, and function name of the caller."""
    import builtins
    from inspect import getframeinfo, stack

    # Enter
    original_print = print

    def new_print(*args, **kwargs):
        caller = getframeinfo(stack()[1][0])
        original_print("FN:", caller.filename, "Line:", caller.lineno, "Func:", caller.function, ":::", *args, **kwargs)

    builtins.print = new_print

    yield

    # Exit
    builtins.print = original_print
