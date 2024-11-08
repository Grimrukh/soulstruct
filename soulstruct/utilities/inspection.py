from __future__ import annotations

__all__ = [
    "get_dataclass_repr",
    "compare_dataclasses",
    "compare_binary_data",
    "compare_binary_files",
    "compare_lines",
    "print_binary_as_integers",
    "get_hex_repr",
    "write_hex_repr",
    "profile_function",
    "Timer",
    "find_errant_prints",
]

import contextlib
import cProfile
import dataclasses
import logging
import pstats
import struct
import time
import typing as tp
from binascii import hexlify
from functools import wraps
from pathlib import Path

import colorama
import numpy as np

from .maths import BaseVector
from .misc import IDList
from .text import indent_lines

_LOGGER = logging.getLogger("soulstruct")

colorama.just_fix_windows_console()
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
RED = colorama.Fore.RED
RESET = colorama.Fore.RESET


def get_dataclass_repr(dataclass_instance: tp.Any, _indent=0, _recursed_ids=None) -> str:
    if not dataclasses.is_dataclass(dataclass_instance):
        raise ValueError(f"Object {dataclass_instance} is not a dataclass instance.")
    indent = "    " * _indent
    if _recursed_ids is None:
        _recursed_ids = set()
    _recursed_ids.add(id(dataclass_instance))
    s = f"{indent}{dataclass_instance.__class__.__name__}(\n"
    for field in dataclasses.fields(dataclass_instance):
        value = getattr(dataclass_instance, field.name)
        if dataclasses.is_dataclass(value) and not isinstance(value, BaseVector):
            if id(value) in _recursed_ids:
                s += f"{indent}    {field.name} = <{id(value)}>,\n"
            else:
                s += f"{indent}    {field.name} =\n{get_dataclass_repr(value, _indent + 2, _recursed_ids)}\n"
        elif isinstance(value, (list, tuple, IDList)) and value and dataclasses.is_dataclass(value[0]):
            p = "[]" if isinstance(value, (IDList, list)) else "()"
            s += f"{indent}    {field.name} = {p[0]}\n"
            for item in value:
                if id(item) in _recursed_ids:
                    s += f"{indent}        <{id(item)}>,\n"
                else:
                    s += f"{get_dataclass_repr(item, _indent + 2, _recursed_ids)},\n"
            s += f"{indent}    {p[1]},\n"
        elif isinstance(value, np.ndarray):
            value_repr = repr(value)[6:].replace("\n", f"\n{indent}{' ' * value.ndim}")
            s += f"{indent}    {field.name} = array(\n{indent}        {value_repr},\n"
        else:
            s += f"{indent}    {field.name} = {repr(value)},\n"
    s += f"{indent}) <{id(dataclass_instance)}>"
    return s


def compare_dataclasses(
    obj1: tp.Any,
    obj2: tp.Any,
    ignore_fields: tp.Iterable[str] = None,
    repr_funcs: dict[type, tp.Callable[[tp.Any], str]] = None,
    is_eq_funcs: dict[type, tp.Callable[[tp.Any, tp.Any], bool]] = None,
    is_close_funcs: dict[type, tp.Callable[[tp.Any, tp.Any], bool]] = None,
    close_vector_threshold=0.001,
    close_float_threshold=0.001,
    unequal_only=False,
):
    if not dataclasses.is_dataclass(obj1):
        raise ValueError(f"First object {obj1} is not a dataclass instance.")
    if not dataclasses.is_dataclass(obj2):
        raise ValueError(f"Second object {obj2} is not a dataclass instance.")
    if type(obj1) is not type(obj2):
        print(f"{RED}Objects are not of the same type: ({type(obj1).__name__} vs. {type(obj2).__name__}){RESET}")
        return

    if repr_funcs is None:
        repr_funcs = {}

    obj_type = type(obj1)

    max_field_name_length = 1
    for field in dataclasses.fields(obj1):
        name = field.name
        if ignore_fields is not None and name in ignore_fields:
            continue
        max_field_name_length = max(max_field_name_length, len(name))

    print(f"Comparing instances of {obj_type.__name__}:")

    for field in dataclasses.fields(obj1):
        name = field.name
        if ignore_fields is not None and name in ignore_fields:
            continue

        value1 = getattr(obj1, field.name)
        value2 = getattr(obj2, field.name)

        if type(value1) is not type(value2):
            # TODO: Permitted for `None` and non-primitive instances.
            print(f"{RED}{name:>{max_field_name_length}}: "
                  f"Field types differ: {type(value1).__name__} vs. {type(value2).__name__}{RESET}")
            continue

        field_type = type(value1)

        repr1 = repr_funcs.get(field_type, repr)(value1)
        repr2 = repr_funcs.get(field_type, repr)(value2)
        if "\n" in repr1:
            repr1 = indent_lines(repr1, indent=max_field_name_length + 2)
        if "\n" in repr2:
            repr2 = indent_lines(repr2, indent=max_field_name_length + 2)

        if is_eq_funcs is not None and field_type in is_eq_funcs:
            if is_eq_funcs[field_type](value1, value2):
                if not unequal_only:
                    print(f"{GREEN}{name:>{max_field_name_length}}: {repr1} == {repr2}{RESET}")
                continue
            print(f"{RED}{name:>{max_field_name_length}}: {repr1} != {repr2}{RESET}")
            continue
        if value1 == value2:
            if not unequal_only:
                print(f"{GREEN}{name:>{max_field_name_length}}: {repr1} == {repr2}{RESET}")
            continue
        if field_type in is_close_funcs:
            if is_close_funcs[field_type](value1, value2):
                if not unequal_only:
                    print(f"{YELLOW}{name:>{max_field_name_length}}: {repr1} ~= {repr2}{RESET}")
                continue
        if isinstance(value1, BaseVector) and close_vector_threshold > 0:
            if (value1 - value2).get_magnitude() < close_vector_threshold:
                if not unequal_only:
                    print(f"{YELLOW}{name:>{max_field_name_length}}: {repr1} ~= {repr2}{RESET}")
                continue
        if isinstance(value1, float) and close_float_threshold > 0:
            if abs(value1 - value2) < close_float_threshold:
                if not unequal_only:
                    print(f"{YELLOW}{name:>{max_field_name_length}}: {repr1} ~= {repr2}{RESET}")
                continue

        print(f"{RED}{field.name}: {repr1} != {repr2}{RESET}")


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
    max_diff_count=-1,
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

    diff_count = 0
    while offset < min(len(data1), len(data2)):
        row1 = data1[offset : offset + row_size]
        row2 = data2[offset : offset + row_size]
        if row1 != row2:
            if offset != 0 and offset - last_diff_row_offset > row_size:
                print(f"...    | {'...':<{pad}}  | {'...':<{pad}} ")
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
            diff_count += 1
            if 0 < max_diff_count <= diff_count:
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
    max_diff_count=-1,
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
        max_diff_count=max_diff_count,
        header1=file1_path.name,
        header2=file2_path.name,
    )


def compare_lines(lines1: str | list[str], lines2: str | list[str], pad=False):
    """Compare two lists of strings, line by line."""
    if isinstance(lines1, str):
        lines1 = lines1.split("\n")
    if isinstance(lines2, str):
        lines2 = lines2.split("\n")
    pad_str = max(len(line) for line in lines1) if pad else 1
    for i in range(max(len(lines1), len(lines2))):
        line1 = lines1[i] if i < len(lines1) else ""
        line2 = lines2[i] if i < len(lines2) else ""
        if line1 != line2:
            print(f"{YELLOW}{str(i):>4}: {line1:<{pad_str}} -> {RED}{line2}{RESET}")
        else:
            print(f"{GREEN}{str(i):>4}: {line1}{RESET}")


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
                returned = func(*args, **kwargs)
            p = pstats.Stats(pr)
            if strip_dirs:
                p = p.strip_dirs()
            p.sort_stats(sort).print_stats(print_count)
            return returned

        return decorated

    return decorator


class Timer:

    def __init__(self, name: str):
        self._name = name

    def __enter__(self):
        self._start = time.perf_counter()

    def __exit__(self, *exc):
        if any(exc):
            _LOGGER.error(f"{self._name} FAILED after {time.perf_counter() - self._start} s.")
        else:
            _LOGGER.info(f"{self._name} COMPLETED in {time.perf_counter() - self._start} s.")


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
