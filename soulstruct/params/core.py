from __future__ import annotations

__all__ = ["ParamError", "BitField", "FieldDisplayInfo", "DynamicFieldDisplayInfo", "pad_field"]

import abc
import logging
import struct

from soulstruct.core import SoulstructError

# TODO: GameParam BND indices of params tables are different in PTD/DSR. I'm guessing it may not actually matter, and
#   that all the params tables are loaded and accessed by their names (e.g. 'OBJ_ACT_PARAM_ST').

_LOGGER = logging.getLogger(__name__)


class ParamError(SoulstructError):
    pass


class BitField:
    def __init__(self):
        self.__field = ""
        self.__offset = 0

    def unpack(self, buffer, bit_count):
        if self.__field == "":
            # Consume (and reverse) new one-byte bit field.
            self.__field = format(struct.unpack("<B", buffer.read(1))[0], "08b")[::-1]
        value = int(self.__field[self.__offset : self.__offset + bit_count][::-1], 2)
        self.__offset += bit_count
        if self.__offset >= 8:
            self.__field = ""
            self.__offset = self.__offset % 8
        return value

    def pack(self, value, bit_count):
        binary_value = bin(value)[2:]
        if len(binary_value) > bit_count:
            raise ValueError(
                f"Value {value} (binary: {binary_value}) of binary field is "
                f"larger than given bit count ({bit_count})."
            )
        binary_value = "0" * (bit_count - len(binary_value)) + binary_value  # leading zeroes
        self.__field += binary_value[::-1]
        if len(self.__field) >= 8:
            completed_bit_field = self.__field[:8]
            # Leftover bytes go into next lot (though this should never happen due to pad fields).
            self.__field = self.__field[8:] if len(self.__field) > 8 else ""
            return int(completed_bit_field[::-1], 2)  # reversed
        return None

    def pad(self):
        if self.__field:
            # Pad out existing non-empty bit field and write it.
            self.__field += "0" * (8 - len(self.__field))
            completed_byte = int(self.__field[::-1], 2)  # note reversal
            self.__field = ""
            return completed_byte
        return None

    def clear(self):
        self.__field = ""
        self.__offset = 0


class FieldDisplayInfo:
    def __init__(self, name, nickname, is_enabled, field_type, description="TODO", default_value=None, dsr_only=False):
        self.name = name
        self.nickname = nickname
        self.is_enabled = is_enabled
        self.field_type = field_type
        self.description = description
        self.default_value = default_value
        self.dsr_only = dsr_only

    def __call__(self, entry):
        """No harm done if you treat this as a `DynamicFieldInfo`."""
        return self


class DynamicFieldDisplayInfo(abc.ABC):
    """Called with a `ParamEntry` instance, in which `type_field_name` is checked before returning `FieldInfo`."""

    POSSIBLE_TYPES = set()

    def __init__(self, name, type_field_name):
        self.name = name
        self.type_field_name = type_field_name

    @abc.abstractmethod
    def __call__(self, entry) -> FieldDisplayInfo:
        ...


def pad_field(n):
    return f"<Pad:{n}>"
