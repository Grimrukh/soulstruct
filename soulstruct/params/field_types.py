__all__ = [
    "base_type",
    "unsigned", "u8", "u16", "u32", "dummy8",
    "signed", "s8", "s16", "s32",
    "f32", "f64",
    "string", "fixstr", "fixstrW"]

from enum import IntEnum


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


class f32:
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


class f64:
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


class string(base_type):
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
    def read(buffer, size):
        raise NotImplementedError

    @staticmethod
    def write(value, size):
        raise NotImplementedError

    @staticmethod
    def minimum():
        return None

    @staticmethod
    def maximum():
        return None


class fixstr(string):
    @staticmethod
    def size():
        return 1

    @staticmethod
    def read(buffer, size):
        return buffer.read(size).decode("shift_jis_2004")

    @staticmethod
    def write(value, size):
        return value.encode("shift_jis_2004").ljust(size, b"\0")


class fixstrW(string):
    @staticmethod
    def size():
        return 2

    @staticmethod
    def read(buffer, size):
        return buffer.read(size).decode("utf-16-le")

    @staticmethod
    def write(value, size):
        return value.encode("utf-16-le").ljust(size, b"\0")
