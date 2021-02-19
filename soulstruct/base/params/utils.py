from __future__ import annotations

__all__ = [
    "BitFieldReader",
    "BitFieldWriter",
    "FieldDisplayInfo",
    "DynamicFieldDisplayInfo",
    "pad_field",
    "bit_pad_field",
]

import abc
import io
import logging
import struct

_LOGGER = logging.getLogger(__name__)


class _BitFieldBase:

    def __init__(self):
        self._field = ""
        self._fmt = ""
        self._offset = 0

    def clear(self):
        self._field = ""
        self._fmt = ""
        self._offset = 0


class BitFieldReader(_BitFieldBase):

    def read(self, buffer: io.BufferedIOBase, bit_count: int, fmt: str):
        max_bit_count = 8 * struct.calcsize(fmt)
        if self._field == "" or fmt != self._fmt or self._offset + bit_count > max_bit_count:
            # Consume (and reverse) new bit field. Any previous bit field is discarded.
            (integer,) = struct.unpack(fmt, buffer.read(struct.calcsize(fmt)))
            self._field = format(integer, f"0{max_bit_count}b")[::-1]
            self._fmt = fmt
        binary_str = self._field[self._offset:self._offset + bit_count][::-1]
        self._offset += bit_count
        if self._offset % max_bit_count == 0:  # read new field next time
            self._field = ""
            self._offset = 0
        return int(binary_str, 2)


class BitFieldWriter(_BitFieldBase):

    def write(self, value, bit_count, fmt: str) -> bytes:
        """Appends `value` to bit field and returns packed data whenever a field is completed.

        Note that a field is completed if the given `fmt` is different to the type of the current bit field.
        """
        if value >= 2 ** bit_count:
            raise ValueError(
                f"Value {value} of new bit field value is too large for given bit count ({bit_count})."
            )
        packed = b""
        if fmt != self._fmt:
            if self._fmt:
                # Pad and return last bit field (of different type to new one) while starting new bit field.
                packed = self.finish_field()
            self._fmt = fmt
        max_bit_count = 8 * struct.calcsize(fmt)
        self._field += format(value, f"0{bit_count}b")[::-1]
        if len(self._field) >= max_bit_count:
            if packed:
                # This shouldn't happen for new `fmt` because `bit_count < max_size`, but just in case.
                raise ValueError(f"New bit field was exceeded before previous bit field could be written.")
            # Leftover bytes go into next lot (though this should never happen due to pad fields).
            completed_bit_field = self._field[:max_bit_count]
            integer = int(completed_bit_field[::-1], 2)  # reversed
            packed = struct.pack(self._fmt, integer)
            self._field = self._field[max_bit_count:] if len(self._field) > max_bit_count else ""
        return packed

    def finish_field(self) -> bytes:
        """Pad existing bit field to its maximum size, clear it, and return packed data.

        Returns empty bytes if field is empty.
        """
        if not self._field:
            return b""
        size = struct.calcsize(self._fmt)
        self._field = format(self._field, f"0<{size}")
        packed = struct.pack(self._fmt, int(self._field[::-1], 2))  # note string reversal
        self.clear()
        return packed


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

    @property
    def docstring(self):
        return f"[{self.name}] {self.description}"


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


def bit_pad_field(n):
    return f"<BitPad:{n}>"
