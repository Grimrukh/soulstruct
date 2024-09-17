from __future__ import annotations

__all__ = [
    "byte",
    "sbyte",
    "ushort",
    "short",
    "uint",
    "ulong",
    "long",
    "double",
    "varint",
    "varuint",

    "PRIMITIVE_FIELD_TYPING",
    "PRIMITIVE_FIELD_TYPES",
    "RESERVED",

    "BinaryMetadata",
    "Binary",
    "BinaryStringMetadata",
    "BinaryString",
    "BinaryArrayMetadata",
    "BinaryArray",
    "BinaryPad",

    "BinaryStruct",
    "ByteOrder",
    "long_varints_from_reader_peek",
    "BinaryReader",
    "BinaryWriter",
    "BinaryFieldTypeError",
    "BinaryFieldValueError",

    # UTILITY
    "read_chars_from_bytes",
    "read_chars_from_buffer",
    "BitFieldReader",
    "BitFieldWriter",
]

import copy
import dataclasses
import enum
import io
import logging
import re
import struct
import typing as tp
from contextlib import contextmanager
from pathlib import Path
from types import GenericAlias

from soulstruct.utilities.maths import Vector2, Vector3, Vector4

if tp.TYPE_CHECKING:
    from soulstruct.containers.entry import BinderEntry


_LOGGER = logging.getLogger("soulstruct")


PAD_RE = re.compile(r"(\d*)x")
FMT_RE = re.compile(r"([@=<>!])?(\d*)([\w?])")


class ByteOrder(enum.Enum):
    # TODO: Use `StrEnum` once Blender supports Python 3.11.
    NativeAutoAligned = "@"
    NativeNotAutoAligned = "="  # standard size, no alignment
    LittleEndian = "<"  # default
    BigEndian = ">"
    Network = "!"  # big-endian

    def get_utf_16_encoding(self):
        if self in {ByteOrder.BigEndian, ByteOrder.Network}:
            return "utf-16-be"
        return "utf-16-le"

    @classmethod
    def big_endian_bool(cls, is_big_endian: bool):
        """Utility shortcut for switching between big/little endian based on a bool (common in game formats)."""
        return cls.BigEndian if is_big_endian else cls.LittleEndian

    @classmethod
    def from_reader_peek(
        cls, reader: BinaryReader, size: int, bytes_ahead: int, big_endian_read: bytes, little_endian_read: bytes
    ) -> ByteOrder:
        peeked = reader.peek(size, bytes_ahead)
        if peeked == big_endian_read:
            return ByteOrder.BigEndian
        elif peeked == little_endian_read:
            return ByteOrder.LittleEndian
        else:
            raise ValueError(f"Could not determine byte order from bytes: {peeked}")

    @classmethod
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


def long_varints_from_reader_peek(
    reader: BinaryReader, size: int, bytes_ahead: int, true_read: bytes, false_read: bytes
) -> bool:
    peeked = reader.peek(size, bytes_ahead)
    if peeked == true_read:
        return True
    elif peeked == false_read:
        return False
    else:
        raise ValueError(f"Could not determine `long_varints` from bytes: {peeked}")


class BinaryBase:

    # Special format characters that become 'iI' or 'qQ' depending on `var_int_size`.
    VAR_INT = "v"
    VAR_UINT = "V"
    default_byte_order: ByteOrder
    long_varints: bool  # 4 (False) or 8 (True); determines size of 'v' and 'V' format characters

    def __init__(self, byte_order=ByteOrder.LittleEndian, long_varints=True):
        self.default_byte_order = ByteOrder(byte_order)
        self.long_varints = long_varints

    def parse_fmt(self, fmt: str) -> str:
        """Insert default byte order and replace 'vV' var int characters."""
        if fmt[0] not in "@=><!":
            fmt = self.default_byte_order.value + fmt
        if self.long_varints:
            fmt = fmt.replace("v", "q").replace("V", "Q")
        else:
            fmt = fmt.replace("v", "i").replace("V", "I")
        return fmt

    def calcsize(self, fmt: str) -> int:
        """Calculate fmt struct size after parsing it."""
        return struct.calcsize(self.parse_fmt(fmt))

    def get_utf_16_encoding(self) -> str:
        return self.default_byte_order.get_utf_16_encoding()


class BinaryReader(BinaryBase):
    """Manages a buffered binary IO stream, with methods for unpacking data and moving to temporary offsets."""

    class ReaderError(Exception):
        """Exception raised when trying to unpack data."""
        pass

    buffer: tp.BinaryIO | io.BufferedIOBase | None
    path: Path | None  # optional path to file source

    def __init__(
        self,
        buffer: str | Path | bytes | bytearray | io.BufferedIOBase | BinderEntry | BinaryReader,
        default_byte_order=ByteOrder.LittleEndian,
        long_varints=True,
    ):
        super().__init__(default_byte_order, long_varints)

        self.buffer = None
        self.path = None

        if isinstance(buffer, str):
            buffer = Path(buffer)
        if isinstance(buffer, Path):
            self.buffer = buffer.open("rb")
            self.path = buffer
        elif isinstance(buffer, (bytes, bytearray)):
            self.buffer = io.BytesIO(buffer)
        elif isinstance(buffer, io.BufferedIOBase):
            self.buffer = buffer
        elif isinstance(buffer, BinaryReader):
            self.buffer = buffer.buffer
        else:
            try:
                data = bytes(buffer)
            except TypeError:
                raise TypeError(
                    f"Invalid `buffer`: {buffer}. Should be a binary IO stream, `bytes, or `Path` of a file to open."
                )
            self.buffer = io.BytesIO(data)

    def unpack(self, fmt, offset=None, relative_offset=False, asserted=None) -> tuple:
        """Unpack appropriate number of bytes from `buffer` using `fmt` string from the given (or current) `offset`.

        Args:
            fmt (str): format string for `struct.unpack()`.
            offset (int): optional offset to seek to before reading. Old offset will be restored afterward.
            relative_offset (bool): indicates that `offset` is relative to current position.
            asserted: assert that the unpacked data is equal to this, if given..

        Returns:
            (tuple) Output of `struct.unpack()`.
        """
        fmt = self.parse_fmt(fmt)

        initial_offset = self.buffer.tell() if offset is not None else None
        if offset is not None:
            self.buffer.seek(initial_offset + offset if relative_offset else offset)
        fmt_size = struct.calcsize(fmt)
        raw_data = self.buffer.read(fmt_size)
        if not raw_data and fmt_size > 0:
            raise ValueError(f"Could not unpack {fmt_size} bytes from reader for format '{fmt}'.")
        data = struct.unpack(fmt, raw_data)
        if asserted is not None and data != asserted:
            raise AssertionError(f"Unpacked data {repr(data)} does not equal asserted data {repr(asserted)}.")
        if initial_offset is not None:
            self.buffer.seek(initial_offset)
        return data

    def unpack_value(self, fmt, offset=None, relative_offset=False, asserted=None) -> bool | int | float | bytes:
        """Call `unpack()` and return the single value returned.

        If `asserted` is given, an `AssertionError` will be raised if the unpacked value is not equal to `asserted`.

        Also raises a `ValueError` if more than one value is unpacked.
        """
        data = self.unpack(fmt, offset, relative_offset)
        if len(data) > 1:
            raise ValueError(f"More than one value unpacked with `unpack_value()`: {data}")
        value = data[0]
        if asserted is not None and value != asserted:
            raise AssertionError(f"Unpacked value {repr(value)} does not equal asserted value {repr(asserted)}.")
        return data[0]

    def __getitem__(self, fmt: str | tuple[str, int]) -> bool | int | float | bytes:
        """Shortcut for `unpack_value` at current offset or `(fmt, offset)` tuple."""
        if isinstance(fmt, str):
            return self.unpack_value(fmt)
        return self.unpack_value(fmt[0], offset=fmt[1])

    def peek(self, fmt_or_size: str | int, bytes_ahead: int = 0) -> bool | int | float | bytes | tuple:
        """Unpack `fmt_or_size` (or just read bytes) and return the unpacked values without changing the offset."""
        if isinstance(fmt_or_size, int):
            return self.read(fmt_or_size, offset=self.position + bytes_ahead)
        return self.unpack(fmt_or_size, offset=self.position + bytes_ahead)

    def peek_value(self, fmt, bytes_ahead: int = 0) -> bool | int | float:
        """Unpack `fmt` and return the unpacked value without changing the offset."""
        return self.unpack_value(fmt, offset=self.position + bytes_ahead)

    def unpack_bytes(
        self,
        offset: int = None,
        length: int = None,
        reset_old_offset=True,
        strip=True,
    ) -> bytes:
        """Read bytes (null-terminated if `length` is not given) from given `offset` (defaults to current).

        See `read_chars_from_buffer()` for more.
        """
        return read_chars_from_buffer(self.buffer, offset, length, reset_old_offset, encoding=None, strip=strip)

    def unpack_string(
        self,
        offset: int = None,
        length: int = None,
        reset_old_offset=True,
        encoding="utf-8",
        strip=True,
    ) -> str:
        """Read string (null-terminated if `length` is not given) from given `offset` (defaults to current).

        Encoding defaults to "utf-8". If a "utf-16" encoding is given, two bytes will be read at a time, and a double
        null terminator is required. See `read_chars_from_buffer()` for more.
        """
        try:
            return read_chars_from_buffer(self.buffer, offset, length, reset_old_offset, encoding=encoding, strip=strip)
        except struct.error as ex:
            raise self.ReaderError(f"Could not unpack string. Error: {ex}")

    def read(self, size: int = None, offset: int = None) -> bytes:
        if offset is not None:
            with self.temp_offset(offset):
                return self.buffer.read(size)
        return self.buffer.read(size)

    def seek(self, offset: int, whence=None) -> int:
        """Returns final position.

        Reminder: `whence` is zero (or None) for absolute offset, 1 for relative to current, and 2 for relative to end.
        """
        if whence is not None:
            self.buffer.seek(offset, whence)
        else:
            self.buffer.seek(offset)
        return self.buffer.tell()

    def tell(self):
        """Also has alias property `position` for this."""
        return self.buffer.tell()

    def assert_pad(self, size: int, char=b"\0"):
        """Read and assert `size` instances of `char` (defaults to null/zero byte)."""
        padding = self.buffer.read(size)
        if padding.strip(char):
            raise ValueError(f"Reader `assert_pad({size})` found bytes other than {char}: {padding}")

    def align(self, alignment: int):
        """Align reader position to next multiple of `alignment`."""
        while self.buffer.tell() % alignment:
            self.buffer.read(1)

    def close(self):
        self.buffer.close()

    @contextmanager
    def temp_offset(self, offset: int = None):
        """Seek `buffer` to `offset` temporarily, then reset to original offset when done.

        If `offset=None` (default), resets to current offset.
        """
        initial_offset = self.buffer.tell()
        if offset is not None:
            self.buffer.seek(offset)
        yield
        self.buffer.seek(initial_offset)

    def __del__(self):
        if self.buffer:
            self.buffer.close()

    @property
    def position(self) -> int:
        return self.buffer.tell()

    @property
    def position_hex(self) -> str:
        return hex(self.buffer.tell())

    def print_labeled_position(self, label: str, as_hex=False):
        if as_hex:
            print(f"{label} position: {self.position_hex}")
        else:
            print(f"{label} position: {self.position}")


class BinaryWriter(BinaryBase):
    """Manages `bytearray` binary data, with features like reserved offsets for later writing and big endian mode."""

    class Reserved(str):
        """Indicates a reserved name that should be used, rather than a string to pack."""

        def __repr__(self):
            return "AUTO_RESERVE" if not self else super().__repr__()

    AUTO_RESERVE = Reserved()  # reserve using `id(source)` and field name

    _array: bytearray
    reserved: dict[str, tuple[int, str]]

    def __init__(self, byte_order=ByteOrder.LittleEndian, long_varints: bool = True):
        super().__init__(byte_order, long_varints)
        self._array = bytearray()
        self.reserved = {}

    def pack(self, fmt: str, *values):
        self._array += struct.pack(self.parse_fmt(fmt), *values)

    def pack_at(self, offset: int, fmt: str, *values):
        packed = struct.pack(self.parse_fmt(fmt), *values)
        self._array[offset:offset + len(packed)] = packed

    def pack_z_string(self, value: str, encoding="utf-8"):
        """Pack null-terminated string `value` with `encoding` at current position.

        Two-char null terminator will be used for UTF-16 encodings.
        """
        terminator = b"\0\0" if encoding.replace("-", "").startswith("utf16") else b"\0"
        self._array += value.encode(encoding) + terminator

    def append(self, bytes_: bytearray | bytes):
        """Manually add existing binary data (e.g. a packed `BinaryStruct`) all at once."""
        self._array += bytes_

    def pack_new_struct(self, new_binary_struct: BinaryStruct, allow_reserved=True):
        if allow_reserved:
            new_binary_struct.to_writer(self)
        else:
            self._array += bytes(new_binary_struct)

    def pad(self, size: int, char=b"\0"):
        if size > 0:
            self._array += char * size

    def pad_to_offset(self, offset: int, char=b"\0"):
        if self.position > offset:
            raise ValueError(f"Writer is already past offset {offset}: {self.position}")
        self.pad(offset - self.position, char=char)

    def pad_align(self, alignment: int, char=b"\0"):
        amount = alignment - self.position % alignment
        if amount != alignment:
            self.pad(amount, char=char)

    def reserve(self, name: str, fmt: str, obj: object = None):
        if obj is not None:
            name = f"{obj.__class__.__name__}__{id(obj)}({name})"
        if name in self.reserved:
            raise ValueError(f"Name {repr(name)} is already reserved in `BytesWriter`.")
        fmt = self.parse_fmt(fmt)
        self.reserved[name] = (len(self._array), fmt)
        self._array += b"\0" * struct.calcsize(fmt)  # reserved space is nulls

    def mark_reserved_offset(self, name: str, fmt: str, offset: int, obj: object = None):
        """Does not pad array anywhere. User must write nulls to the reserved offset themselves."""
        if obj is not None:
            name = f"{obj.__class__.__name__}__{id(obj)}({name})"
        if name in self.reserved:
            raise ValueError(f"Name {repr(name)} is already reserved in `BytesWriter`.")
        fmt = self.parse_fmt(fmt)
        self.reserved[name] = (offset, fmt)

    def fill(self, name: str, *values, obj: object = None):
        if not values:
            raise ValueError("No values given to fill.")
        if obj is not None:
            name = f"{obj.__class__.__name__}__{id(obj)}({name})"
            if name not in self.reserved:
                raise ValueError(f"Field {repr(name)} is not reserved by `{type(obj).__name__}` object.")
        elif name not in self.reserved:
            raise ValueError(f"Name {repr(name)} is not reserved in `BytesWriter`.")
        offset, fmt = self.reserved[name]  # fmt endianness already specified
        try:
            packed = struct.pack(fmt, *values)
        except struct.error:
            raise ValueError(f"Error occurred when packing values to reserved offset with fmt {repr(fmt)}: {values}")
        self._array[offset:offset + len(packed)] = packed
        self.reserved.pop(name)  # pop after successful fill only

    def fill_with_position(self, name: str, obj: object = None) -> int:
        """Fill `name` (optionally also identified by `id(obj)` with current `writer.position`.

        Also returns current `writer.position` for convenience, as it is often needed right after.
        """
        self.fill(name, self.position, obj=obj)
        return self.position

    def block_copy(self, source_offset: int, dest_offset: int, size: int):
        """Copy one block of the buffer to another."""
        self._array[dest_offset:dest_offset + size] = self._array[source_offset:source_offset + size]

    def __bytes__(self) -> bytes:
        """Just checks that no reserved offsets remain, then converts stored `bytearray` to immutable `bytes`."""
        if self.reserved:
            reserved_values = "\n    ".join(self.reserved)
            raise ValueError(f"Reserved `BytesWriter` offsets not filled:\n    {reserved_values}")
        return bytes(self.array)

    def __repr__(self):
        return f"BytesWriter({self.array})"

    @property
    def position(self):
        """Return current 'position' of writer, which is just the number of bytes written so far."""
        return len(self._array)

    @property
    def position_hex(self) -> str:
        """Return current 'position' of writer as a hex string."""
        return hex(len(self._array))

    @property
    def array(self):
        """Return immutable copy of current array, for inspection/display only."""
        return bytes(self._array)


def read_chars_from_bytes(data, offset=0, length=None, encoding=None) -> bytes | str:
    """Read characters from a bytes object (an encoded string). Use 'read_chars_from_buffer' if you are using a buffer.

    If 'length=None' (default), characters will be read until null termination from the given offset. Otherwise,
    'length' bytes will be read and all null padding bytes will be stripped from the right side.

    Use 'encoding' to automatically decode the bytes into a string before returning (e.g. 'shift_jis_2004'). Note that
    if 'utf-16-*' is specified as the encoding with no length, a double-null termination of b'\0\0' is required to
    terminate the string (as single nulls can appear in the two-byte characters).
    """
    bytes_per_char = 2 if encoding is not None and encoding.replace("-", "").startswith("utf16") else 1
    if length is not None:
        stripped_array = data[offset:offset + length].rstrip()  # remove trailing spaces
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
        array = data[offset:offset + null_termination]
        if encoding is not None:
            return array.decode(encoding)
        return array


def read_chars_from_buffer(
    buffer: io.BufferedIOBase,
    offset: int = None,
    length: int = None,
    reset_old_offset=True,
    encoding: str = None,
    strip=True,
) -> str | bytes:
    """Read characters from a buffer (type IOBase). Use 'read_chars_from_bytes' if your data is already in bytes format.

    Args:
        buffer (io.BufferedIOBase): byte-format data stream to read from.
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
        strip: remove trailing spaces and nulls (default: True).
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
    terminator = b"\0" * bytes_per_char

    if offset is not None:
        old_offset = buffer.tell()
        buffer.seek(offset)

    while 1:
        c = buffer.read(bytes_per_char)
        if not c and length is None:
            raise ValueError("Ran out of bytes to read before null termination was found.")
        if length is None and c == terminator:
            # Null termination.
            array = b"".join(chars)
            if reset_old_offset and old_offset is not None:
                buffer.seek(old_offset)
            if encoding is not None:
                return array.decode(encoding)
            return array
        else:
            chars.append(c)
            if len(chars) == length:
                if reset_old_offset and old_offset is not None:
                    buffer.seek(old_offset)
                stripped_array = b"".join(chars)  # used to strip spaces as well, but not anymore
                if strip:
                    stripped_array = stripped_array.rstrip()  # strip spaces
                    while stripped_array.endswith(terminator):
                        stripped_array = stripped_array[:-bytes_per_char]  # remove terminators
                if encoding is not None:
                    return stripped_array.decode(encoding)
                return stripped_array


# BASIC FIELD TYPES
# bool = bool
byte = type("byte", (int,), {})
sbyte = type("sbyte", (int,), {})
ushort = type("ushort", (int,), {})
short = type("short", (int,), {})
uint = type("uint", (int,), {})
# int = int
ulong = type("ulong", (int,), {})
long = type("long", (int,), {})  # actually `int`
# float = float
double = type("double", (float,), {})  # actually `float`
# bytes = bytes
varint = type("varint", (int,), {})  # either `int` or `long`
varuint = type("varuint", (int,), {})  # either `uint` or `ulong`


PRIMITIVE_FIELD_TYPING = tp.Union[
    bool, byte, sbyte, ushort, short, uint, int, ulong, long, float, double, bytes, varint, varuint
]
PRIMITIVE_FIELD_TYPES = (
    bool, byte, sbyte, ushort, short, uint, int, ulong, long, float, double, bytes, varint, varuint
)
ASSERTED_TYPING = tp.Union[
    None, bool, int, float, bytes, str,
    list[bool], list[int], list[float], list[bytes], list[str],
]


# TODO: Use this for `ParamDef` fields as well (u8, s16, f32, angle32, etc.).
_PRIMITIVE_FIELD_FMTS = {
    bool: "?",
    byte: "B",
    sbyte: "b",
    ushort: "H",
    short: "h",
    uint: "I",
    int: "i",
    ulong: "Q",
    long: "q",
    float: "f",
    double: "d",
    varint: "v",
    varuint: "V",
}


_PRIMITIVE_FMT_SIZE_MINMAX = {
    "?": (1, None),
    "B": (1, (0, 2 ** 8 - 1)),
    "b": (1, (-(2 ** 7), (2 ** 7) - 1)),
    "H": (2, (0, (2 ** 16) - 1)),
    "h": (2, (-(2 ** 15), (2 ** 15) - 1)),
    "I": (4, (0, (2 ** 32) - 1)),
    "i": (4, (-(2 ** 31), (2 ** 31) - 1)),
    "Q": (8, (0, (2 ** 64) - 1)),
    "q": (8, (-(2 ** 63), (2 ** 63) - 1)),
    "f": (4, None),
    "d": (8, None),
    "v": (None, None),  # `size` and `min_max` must be computed
    "V": (None, None),  # `size` and `min_max` must be computed
}  # type: dict[str, tuple[int, tuple[int, int] | None]]


# Valid field types for `auto_offset`.
_OFFSET_FIELD_TYPES = (
    byte, sbyte, ushort, short, uint, int, ulong, long, varint, varuint
)


FIELD_T = tp.TypeVar("FIELD_T")  # can be any type thanks to `unpack_func` option
CONDITION_T = tp.TypeVar("CONDITION_T", bool, int, str, ByteOrder)


def read_null_terminated_bytes(reader: BinaryReader, encoding: str = None) -> bytes | str:

    # TODO: Currently just checking for UTF-16 encodings to enforce double null characters.
    bytes_per_char = 2 if encoding is not None and encoding.replace("-", "").startswith("utf16") else 1
    terminator = b"\0" * bytes_per_char

    chars = []
    while 1:
        c = reader.read(bytes_per_char)
        if not c:
            raise ValueError("Ran out of bytes to read before null termination was found.")
        if c == terminator:
            # Null termination.
            array = b"".join(chars)
            if encoding is not None:
                return array.decode(encoding)
            return array
        else:
            chars.append(c)


class BinaryFieldTypeError(Exception):

    def __init__(self, field: dataclasses.Field, cls_name: str, error_msg: str):
        name = f"`{cls_name}.{field.name}`" if cls_name else f"`{field.name}`"
        super().__init__(f"Field {name}: {error_msg}")


class BinaryFieldValueError(Exception):
    pass


@dataclasses.dataclass(slots=True)
class BinaryMetadata(tp.Generic[FIELD_T]):
    """Base class for optional metadata for `BinaryStruct` dataclass fields."""
    fmt: str
    asserted: tuple[FIELD_T, ...] = dataclasses.field(default=())
    unpack_func: tp.Callable[[PRIMITIVE_FIELD_TYPING], FIELD_T] = None
    pack_func: tp.Callable[[FIELD_T], PRIMITIVE_FIELD_TYPING] = None
    bit_count: int = -1  # NOTE: Field is packed/unpacked manually if this is not -1.
    should_skip_func: tp.Callable[[bool, dict[str, tp.Any]], bool] = None

    # Constructed in `__post_init__` for efficiency.
    single_asserted: FIELD_T | None = dataclasses.field(init=False, default=None)

    # Assigned by `BinaryStruct` to allow better error logging below. (NOT used otherwise.)
    field_name: str = dataclasses.field(default=None, init=False)
    field_type: type[FIELD_T] = dataclasses.field(default=None, init=False)

    def __post_init__(self):
        if self.asserted and len(self.asserted) == 1:
            self.single_asserted = self.asserted[0]
        else:
            self.single_asserted = None

    def get_unpacker(self) -> tp.Callable[[list[tp.Any]], FIELD_T]:
        """Configures and returns a function that produces field values from `struct.unpack()` output.

        This way, the (unchanging) field metadata options only have to be checked ONCE, here at construction.

        NOTE: Yes, I'm using the dreaded `exec` to build this function dynamically, like a preprocessor macro.
        I can't find any better way to do this, and it is NOT unsafe as the `exec()` input is fully determined here.
        """
        func = "def unpack(struct_output: list[tp.Any], metadata=self) -> FIELD_T:\n"
        func += "    value = struct_output.pop()\n"
        if self.unpack_func:
            func += "    value = metadata.unpack_func(value)\n"
        if self.asserted:
            error_msg = f"Field '{self.field_name}' read value {{value}} is not an asserted value: {self.asserted}"
            func += "    if value not in metadata.asserted:\n"
            func += f"        raise BinaryFieldValueError(\"{error_msg}\".format(value=value))\n"
        func += "    return value"
        exec(func)
        return locals()["unpack"]

    def get_packer(self) -> tp.Callable[[list[tp.Any], FIELD_T], None]:
        """Pack a single value into input for `struct.pack(full_fmt)`."""

        func = "def pack(struct_input: list[tp.Any], value: FIELD_T, metadata=self):\n"
        if self.asserted:
            error_msg = f"Field '{self.field_name}' value {{value}} is not an asserted value: {self.asserted}"
            func += "    if value not in metadata.asserted:\n"
            func += f"        raise BinaryFieldValueError(\"{error_msg}\".format(value=value))\n"
        if self.pack_func:
            func += "    value = metadata.pack_func(value)\n"
        func += "    struct_input.append(value)"
        exec(func)
        return locals()["pack"]


def Binary(
    fmt: str | type[PRIMITIVE_FIELD_TYPING] = None,
    asserted: tuple[FIELD_T, ...] | FIELD_T = None,
    unpack_func: tp.Callable[[PRIMITIVE_FIELD_TYPING], FIELD_T] = None,
    pack_func: tp.Callable[[FIELD_T], PRIMITIVE_FIELD_TYPING] = None,
    bit_count: int = -1,
    should_skip_func: tp.Callable[[bool, dict[str, tp.Any]], bool] = None
):
    if fmt is str or fmt is bytes:
        raise TypeError("Cannot use `Binary()` for bytes/string fields. Use `BinaryString()` instead.")
    elif fmt in _PRIMITIVE_FIELD_FMTS:
        fmt = _PRIMITIVE_FIELD_FMTS[fmt]
    elif not isinstance(fmt, str) and fmt is not None:
        raise TypeError(f"Binary `fmt` must be a string, primitive type, or `None` (to use type hint), not: {fmt}")

    if isinstance(asserted, list):
        asserted = tuple(asserted)
    elif asserted is not None and not isinstance(asserted, tuple):
        asserted = (asserted,)

    return {"metadata": {"binary": BinaryMetadata(
        fmt, asserted, unpack_func, pack_func, bit_count, should_skip_func
    )}}


@dataclasses.dataclass(slots=True)
class BinaryStringMetadata(BinaryMetadata):
    encoding: str | None = None
    rstrip_null: bool = True

    def get_unpacker(self) -> tp.Callable[[list[tp.Any]], FIELD_T]:
        func = "def unpack(struct_output: list[tp.Any], metadata=self) -> FIELD_T:\n"
        func += "    value = struct_output.pop()\n"
        if self.encoding:
            if self.encoding == "utf16":
                # `byte_order` local will be defined when unpacker is called.
                func += "    value = value.decode(byte_order.get_utf_16_encoding())\n"
            else:
                func += "    value = value.decode(metadata.encoding)\n"
            if self.rstrip_null:
                func += "    value = value.rstrip(\"\\0\")\n"
        else:
            # Presumably safe to rstrip (no UTF-16 bytes to damage).
            if self.rstrip_null:
                func += "    value = value.rstrip(b\"\\0\")\n"
        if self.unpack_func:  # called on decoded `str` if applicable
            func += "    value = metadata.unpack_func(value)\n"
        if self.asserted:
            error_msg = f"Field '{self.field_name}' read value {{value}} is not an asserted value: {self.asserted}"
            func += "    if value not in metadata.asserted:\n"
            func += f"        raise BinaryFieldValueError(\"{error_msg}\".format(value=value))\n"
        func += "    return value\n"
        exec(func)
        return locals()["unpack"]

    def get_packer(self) -> tp.Callable[[list[tp.Any], FIELD_T], None]:
        """Pack a single value into input for `struct.pack(full_fmt)`."""
        func = "def pack(struct_input: list[tp.Any], value: FIELD_T, metadata=self):\n"
        if self.rstrip_null:  # asserted values are stripped, so value should be too
            if self.encoding is None:  # bytes
                func += "    value = value.rstrip(b\"\\0\")\n"
            else:  # str
                func += "    value = value.rstrip(\"\\0\")\n"
        if self.asserted:
            error_msg = f"Field '{self.field_name}' value {{value}} is not an asserted value: {self.asserted}"
            func += "    if value not in metadata.asserted:\n"
            func += f"        raise BinaryFieldValueError(\"{error_msg}\".format(value=value))\n"
        if self.pack_func:
            func += "    value = metadata.pack_func(value)\n"
        if self.encoding:
            if self.encoding == "utf16":
                # `byte_order` local will be defined when unpacker is called.
                func += "    value = value.encode(byte_order.get_utf_16_encoding())\n"
            else:
                func += "    value = value.encode(metadata.encoding)\n"
        # NOTE: `writer.pack()` call will automatically pad these `bytes` using `metadata.fmt`.
        func += "    struct_input.append(value)\n"
        exec(func)
        return locals()["pack"]


def BinaryString(
    fmt_or_byte_size: str | int,  # required
    asserted: tuple[FIELD_T, ...] | FIELD_T = None,
    unpack_func: tp.Callable[[PRIMITIVE_FIELD_TYPING], FIELD_T] = None,
    pack_func: tp.Callable[[FIELD_T], PRIMITIVE_FIELD_TYPING] = None,
    encoding: str = None,
    rstrip_null: bool = True,
    should_skip_func: tp.Callable[[bool, dict[str, tp.Any]], bool] = None,
):
    if isinstance(fmt_or_byte_size, int):
        fmt = f"{fmt_or_byte_size}s"
    elif isinstance(fmt_or_byte_size, str):
        fmt = fmt_or_byte_size
        if not fmt.endswith("s"):
            raise ValueError(f"BinaryString `fmt_or_byte_size` must end with 's' if it is a fmt string, not: {fmt}")
    else:
        raise TypeError(
            f"BinaryString `fmt_or_byte_size` must be a 'Ns' fmt string or byte size `N`, not: {fmt_or_byte_size}"
        )

    if isinstance(asserted, list):
        asserted = tuple(asserted)
    elif asserted is not None and not isinstance(asserted, tuple):
        asserted = (asserted,)

    if encoding and encoding.lower().replace("-", "") == "utf16":
        encoding = "utf16"

    # If `rstrip_null=True`, asserted values should be stripped too for comparison.
    if rstrip_null and asserted:
        if encoding is not None:  # asserted value are strings
            asserted = tuple(s.rstrip("\0") for s in asserted)
        else:  # asserted value are bytes
            asserted = tuple(s.rstrip(b"\0") for s in asserted)

    return {"metadata": {"binary": BinaryStringMetadata(
        fmt, asserted, unpack_func, pack_func, bit_count=-1, should_skip_func=should_skip_func,
        encoding=encoding, rstrip_null=rstrip_null,
    )}}


@dataclasses.dataclass(slots=True, init=False)
class BinaryArrayMetadata(BinaryMetadata):
    length: int = 1

    def __init__(
        self,
        length: int,
        fmt: str | None = None,
        asserted: tuple[FIELD_T, ...] = (),
        unpack_func=None,
        pack_func=None,
        should_skip_func=None,
    ):
        """Custom argument order to make `length` required."""
        self.length = length
        self.fmt = fmt
        self.asserted = asserted
        self.unpack_func = unpack_func
        self.pack_func = pack_func
        self.should_skip_func = should_skip_func
        self.bit_count = -1
        super(BinaryArrayMetadata, self).__post_init__()

    def get_unpacker(self) -> tp.Callable[[list[tp.Any]], FIELD_T]:
        func = "def unpack(struct_output: list[tp.Any], metadata=self) -> FIELD_T:\n"
        func += f"    value = [struct_output.pop() for _ in range({self.length})]\n"  # pops in suitable reverse order
        if self.unpack_func:
            func += "    value = metadata.unpack_func(value)\n"
        if self.asserted:
            error_msg = f"Field '{self.field_name}' read value {{value}} is not an asserted value: {self.asserted}"
            func += f"    if value not in metadata.asserted:\n"
            func += f"        raise BinaryFieldValueError(\"{error_msg}\".format(value=value))\n"
        func += "    return value\n"
        exec(func)
        return locals()["unpack"]

    def get_packer(self) -> tp.Callable[[list[tp.Any], FIELD_T], None]:
        """Pack multiple values into input for `struct.pack(full_fmt)`."""
        func = "def pack(struct_input: list[tp.Any], value: FIELD_T, metadata=self):\n"
        if self.asserted:
            error_msg = f"Field '{self.field_name}' value {{value}} is not an asserted value: {self.asserted}"
            func += f"    if value not in metadata.asserted:\n"
            func += f"        raise BinaryFieldValueError(\"{error_msg}\".format(value=value))\n"
        if self.pack_func:
            func += "    value = metadata.pack_func(value)\n"
        func += "    struct_input.extend(value)\n"
        exec(func)
        return locals()["pack"]


def BinaryArray(
    length: int,
    element_fmt: str | type[PRIMITIVE_FIELD_TYPING] = None,
    asserted: list[FIELD_T] | tuple[list[FIELD_T], ...] = None,
    unpack_func: tp.Callable[[PRIMITIVE_FIELD_TYPING], FIELD_T] = None,
    pack_func: tp.Callable[[FIELD_T], PRIMITIVE_FIELD_TYPING] = None,
    should_skip_func: tp.Callable[[bool, dict[str, tp.Any]], bool] = None,
):
    if element_fmt is str or element_fmt is bytes:
        raise TypeError("Cannot use `Binary()` for bytes/string fields. Use `BinaryString()` instead.")
    elif element_fmt in _PRIMITIVE_FIELD_FMTS:
        element_fmt = _PRIMITIVE_FIELD_FMTS[element_fmt]
        fmt = f"{length}{element_fmt}"
    elif isinstance(element_fmt, str):
        fmt = f"{length}{element_fmt}"
    elif element_fmt is None:
        fmt = element_fmt
    else:
        raise TypeError(
            f"BinaryArray `element_fmt` must be a string, primitive type, or `None` (to use type hint), "
            f"not: {element_fmt}"
        )

    if isinstance(asserted, list):
        if any(isinstance(element, (list, tuple)) for element in asserted):
            raise TypeError(
                "To give multiple asserted lists/tuples to `BinaryArray()`, you must contain them in a tuple."
            )
        asserted = (asserted,)

    return {"metadata": {"binary": BinaryArrayMetadata(
        length, fmt, asserted, unpack_func, pack_func, should_skip_func
    )}}


# Alias that can be used to clearly indicate when a field is being reserved.
RESERVED = None  # type: tp.Any


def BinaryPad(
    length: int,
    char=b"\0",
    bit_count: int = -1,
    should_skip_func: tp.Callable[[bool, dict[str, tp.Any]], bool] = None,
) -> dict[str, tp.Any]:
    """Will assert `length` bytes of character `char`."""
    if not isinstance(char, bytes):
        raise TypeError("Padding `char` must be `bytes`.")
    pad = char * length
    return {
        "metadata": {
            "binary": BinaryStringMetadata(
                fmt=f"{length}s",
                asserted=(pad,),
                bit_count=bit_count,
                rstrip_null=False,
                should_skip_func=should_skip_func,
            ),
        },
        "repr": False,
    }


OBJ_T = tp.TypeVar("OBJ_T")


@dataclasses.dataclass(slots=True)
class BinaryStruct:
    """Dataclass that supports automatic reading/writing from packed binary data."""

    # Caches for class binary information, each constructed on first use.
    _STRUCT_INITIALIZED: tp.ClassVar[bool] = False
    _FIELDS: tp.ClassVar[tuple[dataclasses.Field, ...] | None] = None
    _FIELD_TYPES: tp.ClassVar[tuple[type[FIELD_T], ...] | None] = None
    _FIELD_METADATA: tp.ClassVar[tuple[BinaryMetadata, ...] | None] = None
    _FIELD_PACKERS: tp.ClassVar[tuple[tp.Callable, ...] | None] = None
    _FIELD_UNPACKERS: tp.ClassVar[tuple[tp.Callable, ...] | None] = None

    # Set by `from_bytes()` class method, or can be manually set.
    # Will be auto-detected from values with `get_byte_order()` (defaulting to `LittleEndian`) if not defined, e.g.
    # by a manually-constructed instance.
    byte_order: None | ByteOrder = dataclasses.field(init=False, repr=False, default=None)
    long_varints: None | bool = dataclasses.field(init=False, repr=False, default=None)

    def __post_init__(self):
        if not self._STRUCT_INITIALIZED:
            self._initialize_struct_cls()

        # Set single-asserted fields to their default values, regardless of `init` setting.
        for field, field_metadata in zip(self._FIELDS, self._FIELD_METADATA, strict=True):
            if field_metadata.single_asserted is not None:
                setattr(self, field.name, field_metadata.single_asserted)

        if not hasattr(self, "byte_order"):
            self.byte_order = None
        if not hasattr(self, "long_varints"):
            self.long_varints = None

    @property
    def cls_name(self):
        return self.__class__.__name__

    @classmethod
    def _initialize_struct_cls(cls):
        if not dataclasses.is_dataclass(cls):
            raise TypeError(f"BinaryStruct subclass `{cls.__name__}` is missing a `dataclass` decorator.")

        cls_name = cls.__name__
        binary_fields = cls.get_binary_fields()
        if not binary_fields:
            raise TypeError(f"`BinaryStruct` subclass `{cls_name}` has no fields.")

        all_metadata = []
        all_packers = []
        all_unpackers = []

        for field, field_type in zip(binary_fields, cls.get_binary_field_types()):

            if isinstance(field_type, GenericAlias) and field_type.__origin__ is not list:
                raise BinaryFieldTypeError(
                    field, cls_name, "Binary fields types cannot be `tuple`. Use `list[type]`."
                )

            metadata = field.metadata.get("binary", None)  # type: BinaryMetadata | None
            if metadata is None:
                # NOTE: We can't add new keys to `field.metadata` now, but store it in `_FIELD_METADATA`.

                # TODO: Allow user to specify a "metadata generator" function that allows the use of custom type
                #  annotations like `Vector2` here. Then can remove the Vector classes from this utility.

                # `Vector` types can be specified without needing any field metadata.
                if field_type == Vector2:
                    metadata = BinaryArrayMetadata(2, "2f", unpack_func=Vector2)
                elif field_type == Vector3:
                    metadata = BinaryArrayMetadata(3, "3f", unpack_func=Vector3)
                elif field_type == Vector4:
                    metadata = BinaryArrayMetadata(4, "4f", unpack_func=Vector4)
                elif issubclass(field_type, BinaryStruct):
                    # Sub-struct.
                    metadata = BinaryMetadata(
                        fmt=f"{field_type.get_size()}s",
                        unpack_func=field_type.from_bytes,
                        pack_func=lambda struct_value: struct_value.to_bytes(),
                    )
                else:
                    try:
                        fmt = _PRIMITIVE_FIELD_FMTS[field_type]
                    except KeyError:
                        raise BinaryFieldTypeError(
                            field,
                            cls_name,
                            f"Field with non-primitive type `{field_type.__name__}` must have `fmt` metadata.",
                        )

                    metadata = BinaryMetadata(fmt)
                    metadata.field_type = field_type

            metadata.field_name = field.name
            metadata.field_type = field_type

            if metadata.fmt is None:
                if isinstance(metadata, BinaryArrayMetadata):
                    if (
                        not isinstance(field_type, GenericAlias)
                        or field_type.__origin__ != list
                        or len(field_type.__args__) != 1
                    ):
                        raise BinaryFieldTypeError(
                            field, cls_name, f"Type hint for binary array field must be `list[type]`."
                        )
                    element_type = field_type.__args__[0]
                    if element_type in _PRIMITIVE_FIELD_FMTS:
                        metadata.fmt = f"{metadata.length}{_PRIMITIVE_FIELD_FMTS[element_type]}"
                    else:
                        raise BinaryFieldTypeError(
                            field,
                            cls_name,
                            f"Array field with non-primitive element type `{element_type.__name__}` "
                            f"must have `fmt` metadata.",
                        )
                else:
                    if field_type in _PRIMITIVE_FIELD_FMTS:
                        metadata.fmt = _PRIMITIVE_FIELD_FMTS[field_type]
                    else:
                        raise BinaryFieldTypeError(
                            field,
                            cls_name,
                            f"Field with non-primitive, non-BinaryStruct type `{field_type.__name__}` must have `fmt` "
                            f"metadata.",
                        )

            if field_type not in _PRIMITIVE_FIELD_FMTS:
                # Use custom non-primitive type to unpack and pack (iter).
                if metadata.unpack_func is None:
                    metadata.unpack_func = field_type
                if metadata.pack_func is None:
                    # Just validate `__iter__` presence.
                    if not hasattr(field_type, "__iter__"):
                        raise BinaryFieldTypeError(
                            field,
                            cls_name,
                            f"Non-primitive field type `{field_type.__name__}` must have `unpack_func` metadata or "
                            f"implement `__iter__` to enable default handling."
                        )

            all_metadata.append(metadata)
            all_unpackers.append(metadata.get_unpacker())
            all_packers.append(metadata.get_packer())

        cls._FIELD_METADATA = tuple(all_metadata)
        cls._FIELD_UNPACKERS = tuple(all_unpackers)
        cls._FIELD_PACKERS = tuple(all_packers)
        cls._STRUCT_INITIALIZED = True

    @classmethod
    def from_bytes(
        cls,
        data: bytes | bytearray | BinaryReader | tp.BinaryIO,
        byte_order: ByteOrder | str = None,
        long_varints: bool = None,
    ) -> tp.Self:
        """Create an instance of this class from binary `data`, by parsing its fields.

        Note that field defaults do not matter here, as ALL fields must be unpacked.
        """
        if not cls._STRUCT_INITIALIZED:
            cls._initialize_struct_cls()

        if byte_order is None:
            if isinstance(data, BinaryReader):
                byte_order = data.default_byte_order
            else:  # default
                byte_order = ByteOrder.LittleEndian
        elif isinstance(byte_order, str):
            byte_order = ByteOrder(byte_order)
        elif not isinstance(byte_order, ByteOrder):
            raise ValueError(f"Invalid `byte_order`: {byte_order}")

        if long_varints is None:
            if isinstance(data, BinaryReader):
                long_varints = data.long_varints
            # Otherwise, leave as `None` and allow errors to occur if varint fields are found.

        if isinstance(data, (bytes, bytearray)):
            reader = BinaryReader(data)
        elif isinstance(data, (io.BufferedIOBase, BinaryReader)):
            reader = data  # assumes it is at the correct offset already
        else:
            raise TypeError("`data` must be `bytes`, `bytearray`, or opened `io.BufferedIOBase`.")

        cls_name = cls.__name__
        bit_reader = BitFieldReader()

        full_fmt = cls.get_full_fmt()
        careful_unpack_mode = any(metadata.should_skip_func is not None for metadata in cls._FIELD_METADATA)

        if not careful_unpack_mode:
            try:
                struct_output = list(reversed(reader.unpack(full_fmt)))
            except Exception as ex:
                _LOGGER.error(f"Could not unpack struct fmt for `{cls_name}`: {full_fmt}. Error: {ex}")
                raise
        else:
            struct_output = None

        init_values = {}
        non_init_values = {}
        all_field_values = {}

        for field, field_type, field_metadata, field_unpacker in zip(
            cls._FIELDS, cls._FIELD_TYPES, cls._FIELD_METADATA, cls._FIELD_UNPACKERS, strict=True
        ):

            if field_metadata.bit_count == -1 and not bit_reader.empty:
                # Last bit field was not finished. Discard bits.
                bit_reader.clear()

            if field_metadata.should_skip_func is not None:
                if field_metadata.should_skip_func(long_varints, all_field_values):
                    all_field_values[field.name] = None
                    if not field.init:
                        non_init_values[field.name] = None
                    else:
                        init_values[field.name] = None
                    continue

            if field_metadata.bit_count != -1:
                # Read bit field and cast to field type (e.g. `bool` for 1-bit fields).
                try:
                    if struct_output is None:
                        field_value = field_type(bit_reader.read(reader, field_metadata.bit_count, field_metadata.fmt))
                    else:
                        field_value = field_type(bit_reader.read_list_buffer(
                            struct_output, field_metadata.bit_count, field_metadata.fmt)
                        )
                except Exception as ex:
                    _LOGGER.error(f"Error occurred while trying to unpack bit field `{cls_name}.{field.name}`: {ex}")
                    raise
                if field_metadata.asserted and field_value not in field_metadata.asserted:
                    raise BinaryFieldValueError(
                        f"Bit field `{cls_name}.{field.name}` (bit count {field_metadata.bit_count}) value "
                        f"{repr(field_value)} is not an asserted value: {field_metadata.asserted}"
                    )
            else:
                # Read normal field.
                try:
                    if struct_output is None:
                        field_value = field_unpacker(list(reader.unpack(field_metadata.fmt)))
                    else:
                        field_value = field_unpacker(struct_output)
                except Exception as ex:
                    _LOGGER.error(
                        f"Error occurred while trying to unpack field `{cls_name}.{field.name}`: {ex}\n"
                        f"  Unpacked field values: {all_field_values}"
                    )
                    raise

            all_field_values[field.name] = field_value
            if not field.init:
                non_init_values[field.name] = field_value
            else:
                init_values[field.name] = field_value

        # noinspection PyArgumentList
        instance = cls(**init_values)
        instance.byte_order = byte_order
        instance.long_varints = long_varints
        for field_name, value in non_init_values.items():
            setattr(instance, field_name, value)

        return instance

    @classmethod
    def get_full_fmt(cls, long_varints: bool = None, field_values: dict[str, tp.Any] = None) -> str:
        """Constructs full `BinaryStruct` fmt string, which is complicated only by bit fields.

        If `long_varints` and/or `field_values` are given, `should_skip_func` will be checked for each field (e.g. when
        packing). This can't be done when unpacking, though, and this method is therefore not used.
        """
        if not cls._STRUCT_INITIALIZED:
            cls._initialize_struct_cls()

        full_fmt = ""
        used_bits = 0
        bit_field_max = 0
        for field, metadata in zip(cls._FIELDS, cls._FIELD_METADATA):
            if field_values is not None and metadata.should_skip_func is not None:
                if metadata.should_skip_func(long_varints, field_values):
                    continue  # skip field
            if metadata.bit_count == -1:
                full_fmt += metadata.fmt
                used_bits = 0
                bit_field_max = 0
            elif not full_fmt or bit_field_max == 0 or metadata.fmt != full_fmt[-1]:
                # New bit field (or new bit field type).
                full_fmt += metadata.fmt
                used_bits = metadata.bit_count
                bit_field_max = struct.calcsize(metadata.fmt) * 8
            elif used_bits + metadata.bit_count > bit_field_max:
                # Bit field type is correct but will be exhausted; new chunk needed.
                full_fmt += metadata.fmt
                used_bits = metadata.bit_count - (bit_field_max - used_bits)
            else:
                # Current bit field not exhausted.
                used_bits += metadata.bit_count
        return full_fmt

    @classmethod
    def from_object(
        cls,
        obj: OBJ_T,
        byte_order: ByteOrder = None,
        long_varints: bool = None,
        **field_values,
    ):
        """Create an instance by reading getting field values directly from the attributes of `obj`, with additional
        fields NOT on the object given in `**fields`. Will raise an error if the `init` signature does not match. Fields
        with `init=False` are ignored (all such fields should be asserted or auto-computed).

        Absent fields will be initialized with `None`, which will lead them to being reserved in `to_writer()`.

        Also has the advantage of bypassing type checker for the `int` size subtypes like `byte`, `short`, etc.
        """
        if not cls._STRUCT_INITIALIZED:
            cls._initialize_struct_cls()

        for field in cls._FIELDS:
            if not field.init:
                if field.name in field_values:
                    raise ValueError(f"Cannot specify non-init binary field `{cls.__name__}.{field.name}`.")
                continue
            if field.name not in field_values:
                value = getattr(obj, field.name, None)
                field_values[field.name] = value

        # noinspection PyArgumentList
        binary_struct = cls(**field_values)
        binary_struct.byte_order = byte_order
        binary_struct.long_varints = long_varints
        return binary_struct

    @classmethod
    def from_dict(cls, data: dict[str, tp.Any]):
        """Default is just usage of dictionary as `kwargs`."""
        # noinspection PyArgumentList
        return cls(**data)

    @classmethod
    def object_to_writer(
        cls,
        obj: OBJ_T,
        writer: BinaryWriter | None = None,
        byte_order: ByteOrder = None,
        long_varints: bool = None,
        **field_values,
    ) -> BinaryWriter:
        """Convenience shortcut for creating a struct instance from `obj` and `field_values`, then immediately calling
        `to_writer(writer, reserve_obj=obj)` with that struct.
        """
        if byte_order is None and writer is not None:
            byte_order = writer.default_byte_order
        if long_varints is None and writer is not None:
            long_varints = writer.long_varints
        binary_struct = cls.from_object(obj, byte_order=byte_order, long_varints=long_varints, **field_values)
        return binary_struct.to_writer(writer, reserve_obj=obj)

    def to_object(self, obj_type: type[OBJ_T], **init_kwargs) -> OBJ_T:
        """Initialize `obj_type` instance by automatically adding field names to `init_kwargs`.

        If `obj_type` is a dataclass, any of this struct's fields that match the name of one of `obj_type`'s fields
        will be used. Otherwise, only fields that do not start with an underscore will be used.
        """
        obj_fields = {f.name for f in dataclasses.fields(obj_type)} if dataclasses.is_dataclass(obj_type) else None
        for field in self._FIELDS:
            if obj_fields is not None:
                if field.name not in obj_fields or field.name in init_kwargs:
                    continue  # skip
            elif field.name.startswith("_") or field.name in init_kwargs:
                continue
            value = getattr(self, field.name, field.name)
            if value is None:
                raise ValueError(f"Field `{self.cls_name}.{field.name}` is None. Cannot set to object.")
            init_kwargs[field.name] = value

        return obj_type(**init_kwargs)

    @classmethod
    def reader_to_object(cls, reader: BinaryReader, obj_type: type[OBJ_T], **init_kwargs) -> OBJ_T:
        """Convenience method for creating a struct instance with `from_bytes(reader)`, then immediately calling
        `to_object(obj_type, **init_kwargs)` with that struct.
        """
        struct_instance = cls.from_bytes(reader)
        obj = struct_instance.to_object(obj_type, **init_kwargs)
        return obj

    def to_bytes(self, byte_order: ByteOrder = None, long_varints: bool = None):
        """Convert struct to `bytes`, but with the ability to first update `byte_order` or `long_varints`.

        You can call simply `bytes(binary_struct)` if you do not need to change the byte order or varint size.
        """
        if byte_order is not None:
            self.byte_order = byte_order
        if long_varints is not None:
            self.long_varints = long_varints
        writer = self.to_writer()
        if writer.reserved:
            raise ValueError(
                f"`{self.cls_name}` BinaryStruct cannot fill all fields on its own. Use `to_writer()`.\n"
                f"    Remaining: {writer.reserved}"
            )
        return bytes(writer)

    def __bytes__(self) -> bytes:
        """Calls `to_bytes()` without the ability to change byte order or varint size."""
        return self.to_bytes()

    def to_writer(self, writer: BinaryWriter = None, reserve_obj: OBJ_T = None) -> BinaryWriter:
        """Use fields to pack this instance into a `BinaryWriter`, which may be given or started automatically.

        Any non-auto-computed fields whose values are `None` will be left as reserved keys in the writer of format:
            '{reserve_prefix}.{field_name}'
        and must be filled with `writer.fill()` by the caller before the writer can be converted to bytes. If
        `reserve_prefix = None` (default), it will default to the name of this class. The main use of setting it
        manually is for nested structs and lists of structs, which will keep chaining their names together and include
        list/tuple indices where relevant (handled automatically).
        """
        if not self._STRUCT_INITIALIZED:
            self._initialize_struct_cls()

        if reserve_obj is None:
            reserve_obj = self

        if self.byte_order is None:
            byte_order = self.get_default_byte_order() if writer is None else writer.default_byte_order
        else:
            byte_order = self.byte_order

        if self.long_varints is None and writer is not None:
            long_varints = writer.long_varints
        else:
            # `long_varints` may be left as None (e.g. for formats that do not care about it) but an error will be
            # raised if any `varint` or `varuint` fields are encountered.
            long_varints = self.long_varints

        if writer is not None:
            if writer.default_byte_order != byte_order:
                _LOGGER.warning(
                    f"Existing writer passed to `{self.cls_name}.to_writer()` has default byte order "
                    f"{writer.default_byte_order}, but this class wants to use {byte_order}. Using this class's byte "
                    f"order.")
                writer.default_byte_order = byte_order
        else:
            writer = BinaryWriter(byte_order)  # NOTE: `BinaryWriter.long_varints` not used here

        cls_name = self.cls_name
        bit_writer = BitFieldWriter()

        # Get all field values.
        field_values = {field.name: getattr(self, field.name, None) for field in self._FIELDS}

        # Unlike when unpacking, we can use `field_values` immediately to check skips and construct `full_fmt` as we go.
        full_fmt = ""  # for reserving
        struct_input = []  # type: list[float | int | bool | bytes]
        start_offset = writer.position

        def get_fmt_size() -> int:
            nonlocal full_fmt
            if not full_fmt:
                return 0
            if long_varints is None:
                return struct.calcsize(full_fmt)
            return writer.calcsize(full_fmt)

        for field, field_type, field_metadata, field_packer, field_value in zip(
            self._FIELDS, self._FIELD_TYPES, self._FIELD_METADATA, self._FIELD_PACKERS, field_values.values()
        ):

            if field.metadata.get("NOT_BINARY", False):
                continue  # field excluded

            if field_metadata.should_skip_func is not None:
                if field_metadata.should_skip_func(long_varints, field_values):
                    # Write nothing for this field.
                    continue

            if not bit_writer.empty and field_metadata.bit_count == -1:
                # Pad out bit writer.
                full_fmt += bit_writer.finish_field_buffer(struct_input)

            if field_metadata.bit_count != -1:
                if field_metadata.asserted and field_value not in field_metadata.asserted:
                    raise ValueError(
                        f"Field `{cls_name}.{field.name}` value {repr(field_value)} is not an asserted value: "
                        f"{field_metadata.asserted}"
                    )
                full_fmt += bit_writer.write_to_buffer(
                    struct_input, field_value, field_metadata.bit_count, field_metadata.fmt
                )
                continue

            if field_value is None:
                if field_metadata.single_asserted is None:
                    # Reserved for custom external filling, as it requires data beyond this struct's scope (even just to
                    # choose one of multiple provided asserted values). Current byte order is used.
                    reserve_offset = start_offset + get_fmt_size()
                    reserve_fmt = byte_order.value + field_metadata.fmt
                    writer.mark_reserved_offset(field.name, reserve_fmt, reserve_offset, obj=reserve_obj)
                    null_size = writer.calcsize(reserve_fmt)
                    struct_input.append(b"\0" * null_size)
                    full_fmt += f"{null_size}s"
                    continue
                else:
                    # Use lone asserted value.
                    field_value = field_metadata.single_asserted

            try:
                field_packer(struct_input, field_value)
                full_fmt += field_metadata.fmt
            except Exception as ex:
                _LOGGER.error(f"Error occurred while writing binary field `{field.name}`: {ex}")
                raise

        # Single pack call.
        try:
            writer.pack(full_fmt, *struct_input)
        except Exception as ex:
            _LOGGER.error(
                f"Error while packing `{cls_name}`: {ex}\n"
                f"    Fmt: {full_fmt}\n"
                f"    Struct input: {struct_input}"
            )
            raise

        return writer  # may have remaining unfilled fields (any non-auto-computed field with value `None`)

    def fill(self, writer: BinaryWriter, field_name: str, *values: tp.Any):
        """Fill reserved `field_name` in `writer` as reserved with the ID of this instance."""
        writer.fill(field_name, *values, obj=self)

    def fill_multiple(self, writer: BinaryWriter, **field_names_values: tp.Any):
        """Fill multiple reserved fields in `writer` as reserved with the ID of this instance.

        Can only be used with single-value reserved field formats.
        """
        for field_name, value in field_names_values.items():
            writer.fill(field_name, value, obj=self)

    def assert_field_values(self, **field_values):
        for field_name, field_value in field_values.items():
            try:
                value = getattr(self, field_name)
            except AttributeError:
                raise AssertionError(f"Field '{field_name}' does not exist on `{self.cls_name}`.")
            if value != field_value:
                raise AssertionError(f"Field value assertion error: {repr(value)} != asserted {repr(field_value)}")

    def to_dict(self, ignore_underscore_prefix=True) -> dict[str, tp.Any]:
        """Get all current (non-single-asserted) binary fields.

        Ignores fields with value `None` and (by default) underscore names.
        """
        return {
            name: value
            for name, value in self.get_binary_field_values().items()
            if value is not None and (not ignore_underscore_prefix or not name.startswith("_"))
        }

    def copy(self) -> tp.Self:
        return copy.copy(self)

    def deepcopy(self) -> tp.Self:
        return copy.deepcopy(self)

    def pop(self, field_name: str) -> tp.Any:
        """Simply sets `field_name` to None, marking it as 'consumed', without triggering type checkers.

        This has the same general usage pattern as `unpack_deferred_field()` but supports external field processing of
        arbitrary complexity. The main outcome is to ensure that `field_name` is externally reserved when packing.
        """
        value = getattr(self, field_name, None)
        if value is None:
            raise BinaryFieldValueError(f"Field `{self.cls_name}.{field_name}` has no set value to consume.")
        setattr(self, field_name, None)
        return value

    @staticmethod
    def pack_z_string(writer: BinaryWriter, value: str, encoding=""):
        """Convenience function for packing an encoded, null-terminated string."""
        z = b"\0\0" if encoding.startswith("utf-16") else b"\0"
        writer.append(value.encode(encoding) + z)

    def get_default_byte_order(self) -> ByteOrder:
        """Utility for subclasses to indicate their own default `byte_order`.

        Called on pack if `self.byte_order` is not already assigned. This base method also logs a warning.
        """
        _LOGGER.warning(f"Byte order defaulting to `LittleEndian` for `{self.cls_name}`.")
        return ByteOrder.LittleEndian

    def repr_multiline(self) -> str:
        """Only includes binary fields with non-default values."""
        lines = [
            f"{self.cls_name}(",
        ]
        for field in self._FIELDS:
            if not field.repr:
                continue  # explicitly excluded
            value = getattr(self, field.name, None)
            if value is None:
                continue
            if field.default not in (None, dataclasses.MISSING) and value == field.default:
                continue
            lines.append(f"  {field.name} = {repr(value)},")
        lines.append(")")
        return "\n".join(lines)

    def get_binary_field_values(self) -> dict[str, tp.Any]:
        """Get all current binary field values, unless it has a single asserted value."""
        field_values = {}
        for field, metadata in zip(self.get_binary_fields(), self._FIELD_METADATA):
            if metadata.single_asserted is None:
                field_values[field.name] = getattr(self, field.name, None)
        return field_values

    @classmethod
    def get_binary_fields(cls) -> tuple[dataclasses.Field, ...]:
        if cls._FIELDS is not None:
            return cls._FIELDS
        cls._FIELDS = tuple(
            field for field in dataclasses.fields(cls)
            if field.name not in {"byte_order", "long_varints"}
            and not field.metadata.get("NOT_BINARY", False)
        )
        return cls._FIELDS

    @classmethod
    def get_binary_field_types(cls) -> tuple[type[FIELD_T], ...]:
        if cls._FIELD_TYPES is not None:
            return cls._FIELD_TYPES
        all_type_hints = tp.get_type_hints(cls)
        cls._FIELD_TYPES = tuple(all_type_hints[field.name] for field in cls.get_binary_fields())
        return cls._FIELD_TYPES

    @classmethod
    def get_binary_field_names(cls) -> tuple[str, ...]:
        return tuple(f.name for f in cls.get_binary_fields())

    @classmethod
    def get_binary_field_and_type(cls, field_name: str) -> tuple[dataclasses.Field, tp.Type]:
        for field, field_type in zip(cls._FIELDS, cls._FIELD_TYPES):
            if field.name == field_name:
                return field, field_type
        raise KeyError(f"Invalid field for `{cls.__name__}`: {field_name}")

    @classmethod
    def get_size(cls, byte_order: ByteOrder = ByteOrder.LittleEndian, long_varints: bool = None) -> int:
        """Get full format of this struct, then calculate its size using the given `byte_order` and `long_varints`.

        `byte_order` will default to `LittleEndian`; only a change to `NativeAutoAligned` would potentially change the
        size of the struct, which is unlikely for game formats. `long_varints` may be omitted, but an error will be
        raised if any `varint` or `varuint` fields are used in the struct.
        """
        full_fmt = byte_order.value + cls.get_full_fmt()
        if "v" in full_fmt or "V" in full_fmt:
            if long_varints is None:
                raise ValueError(f"Struct `{cls.__name__}` has varint fields. `long_varints` must be set to get size.")
            if long_varints:
                full_fmt = full_fmt.replace("v", "q").replace("V", "Q")
            else:
                full_fmt = full_fmt.replace("v", "i").replace("V", "I")
        return struct.calcsize(full_fmt)

    @staticmethod
    def join_bytes(struct_iterable: tp.Iterable[BinaryStruct]) -> bytes:
        return b"".join(bytes(s) for s in struct_iterable)


class _BitFieldBase:

    _field: str
    _fmt: str
    _offset: int

    def __init__(self):
        self._field = ""
        self._fmt = ""
        self._offset = 0

    def clear(self):
        self._field = ""
        self._fmt = ""
        self._offset = 0

    @property
    def empty(self) -> bool:
        return not self._field


class BitFieldReader(_BitFieldBase):
    """Manages partial reading of one or more bytes, by keeping unused bits from previous reads and only consuming new
    bytes from `reader` when needed."""

    def read(self, reader: BinaryReader, bit_count: int, fmt: str = "B"):
        max_bit_count = 8 * struct.calcsize(fmt)
        if self._field == "" or fmt != self._fmt or self._offset + bit_count > max_bit_count:
            # Consume (and reverse) new bit field. Any previous bit field is discarded.
            integer = reader[fmt]
            self._field = format(integer, f"0{max_bit_count}b")[::-1]
            self._fmt = fmt
        binary_str = self._field[self._offset:self._offset + bit_count][::-1]
        self._offset += bit_count
        if self._offset % max_bit_count == 0:  # read new field next time
            self._field = ""
            self._offset = 0
        return int(binary_str, 2)

    def read_list_buffer(self, buffer: list[int], bit_count: int, fmt: str = "B"):
        """Same, but instead of using a reader, pop a new integer from end of `buffer` when needed.

        NOTE: Still uses `fmt`, but assumes that `buffer` was created appropriately with the same formats.
        """
        max_bit_count = 8 * struct.calcsize(fmt)
        if self._field == "" or fmt != self._fmt or self._offset + bit_count > max_bit_count:
            # Consume (and reverse) new bit field. Any previous bit field is discarded.
            integer = buffer.pop()
            # TODO: lazy as hell
            max_size = _PRIMITIVE_FMT_SIZE_MINMAX[fmt][1][1]
            if integer > max_size:
                raise ValueError(f"BitFieldReader popped value {integer} which is too large for fmt {fmt}.")
            self._field = format(integer, f"0{max_bit_count}b")[::-1]
            self._fmt = fmt
        binary_str = self._field[self._offset:self._offset + bit_count][::-1]
        self._offset += bit_count
        if self._offset % max_bit_count == 0:  # read new field next time
            self._field = ""
            self._offset = 0
        return int(binary_str, 2)


class BitFieldWriter(_BitFieldBase):
    """Manages partial writing of one or more bytes, by keeping incomplete bits from previous writes and flushing
    them when the full `fmt` is complete."""

    def write(self, writer: BinaryWriter, value: int, bit_count: int, fmt: str = "B"):
        """Appends `value` to bit field and returns packed data whenever a field is completed.

        `fmt` specifies the size of the field that bits are being written into (almost always `byte`). When the field is
        finished,

        Note that a field is completed if the given `fmt` is different to the type of the current bit field.
        """
        if value >= 2 ** bit_count:
            raise ValueError(
                f"Value {value} of new bit field value is too large for given bit count ({bit_count})."
            )

        new_fmt = False
        if fmt != self._fmt:
            if self._fmt:
                # Pad and append last bit field (of different type to new one) while starting new bit field.
                self.finish_field(writer)
            self._fmt = fmt
            new_fmt = True

        # Append value bits to partial field.
        self._field += format(value, f"0{bit_count}b")[::-1]

        max_bit_count = 8 * struct.calcsize(self._fmt)
        if len(self._field) >= max_bit_count:
            # Bits are ready to flush to `writer`.
            if new_fmt:
                # This shouldn't happen for new `fmt` because `bit_count < max_size`, but just in case.
                raise ValueError(f"New bit field was exceeded before previous bit field could be written.")

            # Complete and write finished field.
            completed_bit_field = self._field[:max_bit_count]
            integer = int(completed_bit_field[::-1], 2)  # reversed
            writer.pack(self._fmt, integer)

            # Leftover bits (if any) go into new field (though this should never happen in `Param`s due to pad fields).
            self._field = self._field[max_bit_count:]  # will be empty if `max_bit_count` exactly reached

    def write_to_buffer(self, buffer: list[int], value: int, bit_count: int, fmt: str = "B") -> str:
        """Appends `value` to bit field and appends packed data to `buffer` whenever a field is completed.

        `fmt` specifies the size of the field that bits are being written into (almost always `byte`).

        Note that a field is completed if the given `fmt` is different to the type of the current bit field.

        Returns `fmt` of appended values
        """
        if value >= 2 ** bit_count:
            raise ValueError(
                f"Value {value} of new bit field value is too large for given bit count ({bit_count})."
            )

        new_fmt = False
        added_fmt = ""
        if fmt != self._fmt:
            if self._fmt and not self.empty:
                # Pad and append last bit field (of different type to new one) while starting new bit field.
                self.finish_field_buffer(buffer)
                added_fmt += self._fmt
            self._fmt = fmt
            new_fmt = True

        # Append value bits to partial field.
        self._field += format(value, f"0{bit_count}b")[::-1]

        max_bit_count = 8 * struct.calcsize(self._fmt)
        if len(self._field) >= max_bit_count:
            # Bits are ready to flush to `writer`.
            if new_fmt:
                # This shouldn't happen for new `fmt` because `bit_count < max_size`, but just in case.
                raise ValueError(f"New bit field was exceeded before previous bit field could be written.")

            # Complete and write finished field.
            completed_bit_field = self._field[:max_bit_count]
            field_int = int(completed_bit_field[::-1], 2)  # reversed
            buffer.append(field_int)
            added_fmt += self._fmt

            # Leftover bits (if any) go into new field (though this should never happen in `Param`s due to pad fields).
            self._field = self._field[max_bit_count:]  # will be empty if `max_bit_count` exactly reached

        return added_fmt

    def finish_field(self, writer: BinaryWriter):
        """Pad existing bit field to its maximum size from `self._fmt`, clear it, and return packed data.

        Returns empty bytes if field is empty.
        """
        if not self._field:
            return
        size = struct.calcsize(self._fmt)
        padded_field = format(self._field, f"0<{size}")  # pad field out with zeroes
        writer.pack(self._fmt, int(padded_field[::-1], 2))  # note string reversal
        self.clear()

    def finish_field_buffer(self, buffer: list[int]) -> str:
        """Pad existing bit field to its maximum size from `self._fmt`, clear it, and return packed data.

        Returns added fmt.
        """
        size = struct.calcsize(self._fmt)
        padded_field = format(self._field, f"0<{size}")  # pad field out with zeroes
        buffer.append(int(padded_field[::-1], 2))  # note string reversal
        added_fmt = self._fmt
        self.clear()
        return added_fmt


def test_bit_field():

    @dataclasses.dataclass(slots=True)
    class TestStruct(BinaryStruct):
        start: short
        bit_1: int = dataclasses.field(**Binary("B", bit_count=1))
        bit_2: bool = dataclasses.field(**Binary("B", bit_count=1))
        _bit_pad_6: int = dataclasses.field(**Binary("B", bit_count=6, asserted=0))
        end: float

    packed = struct.pack("<hBf", 1234, 0b0000_0001, 10.0)
    print(packed)
    test_struct = TestStruct.from_bytes(packed)
    print(test_struct)
    test_struct.bit_2 = True
    repacked = bytes(test_struct)
    print(repacked)
    print(TestStruct.from_bytes(repacked))


if __name__ == '__main__':
    test_bit_field()
