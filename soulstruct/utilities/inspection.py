__all__ = ["print_binary_as_integers", "get_hex_repr", "profile_function"]

import cProfile
import logging
import pstats
import struct
import typing as tp
from binascii import hexlify
from functools import wraps

_LOGGER = logging.getLogger(__name__)


def print_binary_as_integers(file_name):
    """Tool for inspecting data you assume or suspect is integers."""
    with open(file_name, "rb") as file:
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


def get_hex_repr(data: bytes, with_unicode=False) -> str:
    hex_lines = repr(hexlify(data, sep=" ", bytes_per_sep=-16))[2:-1].split()
    hex_lines = [" ".join(hx[i:i + 2] for i in range(0, 32, 2)) for hx in hex_lines]
    if with_unicode:
        for i, line in enumerate(hex_lines):
            unicode_string = ""
            for byte in data[i * 16:(i + 1) * 16]:
                unicode_string += (chr(byte) if byte else ".") + " "
            hex_lines[i] += f"    {unicode_string}"
    hex_lines = [f"{i * 16:>6} | {hex(i * 16):>8}: " + hx for i, hx in enumerate(hex_lines)]
    return "\n".join(hex_lines)


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
