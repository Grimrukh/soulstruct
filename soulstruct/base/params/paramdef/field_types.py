from __future__ import annotations

__all__ = [
    "base_type",
    "unsigned", "u8", "u16", "u32", "dummy8",
    "signed", "s8", "s16", "s32",
    "f32", "f64",
    "basestring", "fixstr", "fixstrW",
]

import typing as tp
from enum import IntEnum

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary import BinaryReader


class base_type:
    @staticmethod
    def size():
        raise NotImplementedError

    @staticmethod
    def format():
        raise NotImplementedError

    @staticmethod
    def python_type():
        raise NotImplementedError

    @staticmethod
    def minimum():
        raise NotImplementedError

    @staticmethod
    def maximum():
        raise NotImplementedError

    @staticmethod
    def default():
        raise NotImplementedError


class unsigned(base_type, IntEnum):
    @staticmethod
    def size():
        raise NotImplementedError

    @classmethod
    def bit_size(cls):
        return 8 * cls.size()

    @staticmethod
    def format():
        raise NotImplementedError

    @staticmethod
    def python_type():
        return int

    @staticmethod
    def minimum():
        return 0

    @classmethod
    def maximum(cls):
        return 2 ** cls.bit_size() - 1

    @staticmethod
    def default():
        return 0


class u8(unsigned):
    @staticmethod
    def size():
        return 1

    @staticmethod
    def format():
        return "<B"


class u16(unsigned):
    @staticmethod
    def size():
        return 2

    @staticmethod
    def format():
        return "<H"


class u32(unsigned):
    @staticmethod
    def size():
        return 4

    @staticmethod
    def format():
        return "<I"


class dummy8(u8):
    """Pad fields. May not be unpacked/decoded."""


class signed(base_type, IntEnum):
    @staticmethod
    def size():
        raise NotImplementedError

    @classmethod
    def bit_size(cls):
        return 8 * cls.size()

    @staticmethod
    def format():
        raise NotImplementedError

    @staticmethod
    def python_type():
        return int

    @classmethod
    def minimum(cls):
        return -(2 ** (cls.bit_size() - 1))

    @classmethod
    def maximum(cls):
        return 2 ** (cls.bit_size() - 1) - 1

    @staticmethod
    def default():
        return 0


class s8(signed):
    @staticmethod
    def size():
        return 1

    @staticmethod
    def format():
        return "<b"


class s16(signed):
    @staticmethod
    def size():
        return 2

    @staticmethod
    def format():
        return "<h"


class s32(signed):
    @staticmethod
    def size():
        return 4

    @staticmethod
    def format():
        return "<i"


class f32(base_type):
    @staticmethod
    def size():
        return 4

    @classmethod
    def bit_size(cls):
        return 8 * cls.size()

    @staticmethod
    def format():
        return "<f"

    @staticmethod
    def python_type():
        return float

    @staticmethod
    def minimum():
        return -float("inf")

    @staticmethod
    def maximum():
        return float("inf")

    @staticmethod
    def default():
        return 0.0


class angle32(base_type):
    """TODO: Haven't personally encountered this but I assume it's just a float."""
    @staticmethod
    def size():
        return 4

    @classmethod
    def bit_size(cls):
        return 8 * cls.size()

    @staticmethod
    def format():
        return "<f"

    @staticmethod
    def python_type():
        return float

    @staticmethod
    def minimum():
        return -float("inf")

    @staticmethod
    def maximum():
        return float("inf")

    @staticmethod
    def default():
        return 0.0


class f64(base_type):
    """Not actually used in any known game."""

    @staticmethod
    def size():
        return 8

    @classmethod
    def bit_size(cls):
        return 8 * cls.size()

    @staticmethod
    def format():
        return "<d"

    @staticmethod
    def python_type():
        return float

    @staticmethod
    def minimum():
        return -float("inf")

    @staticmethod
    def maximum():
        return float("inf")

    @staticmethod
    def default():
        return 0


class basestring(base_type):
    @staticmethod
    def size():
        raise NotImplementedError

    @staticmethod
    def python_type():
        return str

    @staticmethod
    def format():
        return None

    @staticmethod
    def read(reader: BinaryReader, size: int):
        raise NotImplementedError

    @staticmethod
    def write(value: str, size: int) -> bytes:
        raise NotImplementedError

    @staticmethod
    def minimum():
        return None

    @staticmethod
    def maximum():
        return None

    @staticmethod
    def default():
        return ""


class fixstr(basestring):
    @staticmethod
    def size():
        return 1

    @staticmethod
    def read(reader: BinaryReader, size: int):
        return reader.unpack_string(length=size, encoding="shift_jis_2004")

    @staticmethod
    def write(value: str, size: int) -> bytes:
        return value.encode("shift_jis_2004").ljust(size, b"\0")


class fixstrW(basestring):
    @staticmethod
    def size():
        return 2

    @staticmethod
    def read(reader: BinaryReader, size: int):
        return reader.unpack_string(length=size // 2, encoding="utf-16-le")

    @staticmethod
    def write(value: str, size: int):
        return value.encode("utf-16-le").ljust(size, b"\0")
