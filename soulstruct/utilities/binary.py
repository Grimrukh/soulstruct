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
    "BinaryCondition",
    "RESERVED",
    "FieldValue",
    "BinaryFieldMetadata",
    "Binary",
    "BinaryAutoCompute",
    "BinaryAutoOffset",
    "BinaryPad",
    "NewBinaryStruct",
    "ByteOrder",
    "BinaryReader",
    "BinaryWriter",
    "slots_equality",
    "BinaryFieldTypeError",
    "BinaryFieldValueError",

    # DEPRECATED
    "BinaryObject",
    "BinaryStruct",

    # UTILITY
    "read_chars_from_bytes",
    "get_blake2b_hash",
    "BitFieldReader",
    "BitFieldWriter",
]

import abc
import dataclasses
import enum
import hashlib
import inspect
import io
import logging
import re
import struct
import typing as tp
from contextlib import contextmanager
from pathlib import Path
from types import GenericAlias, MappingProxyType

from soulstruct.utilities.misc import Flags8
from soulstruct.utilities.maths import Vector, Vector2, Vector3, Vector4

if tp.TYPE_CHECKING:
    from soulstruct.containers.entry import BinderEntry

try:
    from typing import Self
except ImportError:  # < Python 3.11
    Self = "NewBinaryStruct"


_LOGGER = logging.getLogger(__name__)


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
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


# region DEPRECATED


class BinaryField:
    """Stores information about a field passed to `BinaryStruct`."""

    def __init__(self, name: str, fmt: str, length: int, asserted_value=None, encoding=""):
        self.name = name
        self.fmt = fmt
        self.length = length
        self.asserted = asserted_value
        self.encoding = encoding

    def parse_for_unpack(self, unpacked_values: tp.Sequence, index: int):
        """Read sequence of unpacked values and interpret them according to field."""
        if self.length == 0:
            # Ignore.
            return
        value = unpacked_values[index: index + self.length]
        if self.length == 1:
            # Unpack single values.
            value = value[0]
        else:
            # Convert tuples to lists.
            value = list(value)
        if self.encoding:
            value = read_chars_from_bytes(value, length=len(value), encoding=self.encoding)
            value = value.rstrip("\0\0" if self.encoding.startswith("utf-16") else "\0")
        if self.asserted is not None and value != self.asserted:
            raise ValueError(f"Field '{self.name}' contained {value} instead of asserted value {self.asserted}.")
        return value

    def parse_for_pack(self, value):
        if self.encoding:
            if not isinstance(value, str):
                raise TypeError(f"Expected a string in field '{self.name}', not {value}")
            return value.encode(encoding=self.encoding)
        elif isinstance(value, str):
            return value.encode()  # use default UTF-8 encoding to convert string to bytes
        elif isinstance(value, (list, tuple, Vector)):
            return [self.parse_for_pack(v) for v in value]  # recur on each element
        else:
            return value

    def __repr__(self):
        return f"{self.name} :: {self.fmt}" + (f" (== {self.asserted})" if self.asserted is not None else "")


# TODO: Deprecated. Replacing all uses with `NewBinaryStruct`, then deleting this and renaming that to `BinaryStruct`.
class BinaryStruct:

    # Optional function that indicates if the given `BinaryReader` should be set to `BigEndian` byte order, usually by
    # inspecting a particular byte or int at some early offset. Make sure it restores the reader's initial offset!
    _is_big_endian_func: tp.Callable[[BinaryReader], bool] | None = None

    def __init__(
        self, *fields, byte_order: ByteOrder = None, is_big_endian_func: tp.Callable[[BinaryReader], bool] = None
    ):
        """Flexible binary unpacker/repacker."""
        if is_big_endian_func:
            if byte_order is not None:
                raise ValueError(f"Cannot pass both `byte_order` and `is_big_endian_func` to `BinaryStruct` fields.")
            self._is_big_endian_func = is_big_endian_func
        else:
            self._is_big_endian_func = None
            if byte_order is None:
                byte_order = ByteOrder.LittleEndian  # default (sans `is_big_endian_func`)

        self.fields = []  # type: list[BinaryField]
        self._struct_format = []  # type: list[str]  # fmt chunks with different byte orders are stored here
        self._struct_length = []  # Number of values to be packed using each sub-format string.
        self.size = 0  # Total number of bytes in struct.
        if fields:
            self.add_fields(*fields, byte_order=byte_order)

    def add_fields(self, *fields, byte_order: ByteOrder = None) -> tuple[list[BinaryField], str]:
        """Add new fields to the BinaryStruct.

        Args:
             *fields: sequence of fields to add.
             byte_order (ByteOrder): byte order for the added fields to use, which can be different from the byte order
                of fields added in a separate call or `__init__`. By default, the most recent byte order is used.
                Not permitted if `is_big_endian_func` was defined at creation.

        Returns:
            field_list, struct_format
        """
        if not fields:
            raise ValueError(f"No fields were passed to `add_fields()`.")
        if byte_order is not None and self._is_big_endian_func is not None:
            raise ValueError(f"Cannot pass explicit new `byte_order` when `is_big_endian_func` was defined.")

        if byte_order is None:
            if self._struct_format:
                # Use most recent byte order.
                byte_order = ByteOrder(self._struct_format[-1][0])
                new_fmt = False
            else:
                byte_order = ByteOrder.LittleEndian  # default
                new_fmt = True
        elif not self._struct_format or byte_order != self._struct_format[-1][0]:
            # New byte order given that differs from last one.
            byte_order = ByteOrder(byte_order)
            new_fmt = True
        else:
            # Append to most recent sub-format (same byte order).
            new_fmt = False

        sub_fmt = ""
        sub_fmt_length = 0
        new_fields = []

        for field_spec in fields:
            if isinstance(field_spec, str):
                # Pad string.
                if PAD_RE.match(field_spec):
                    new_fields.append(BinaryField(name="x", fmt=field_spec, length=0))
                    sub_fmt += field_spec
                    continue
                else:
                    raise ValueError("Only pad strings, `'#x'`, are permitted outside field tuples.")

            asserted_value = None
            encoding = ""

            if isinstance(field_spec, (list, tuple)) and 2 <= len(field_spec) <= 3:
                if len(field_spec) == 3:
                    name, fmt, asserted_value = field_spec
                    if isinstance(asserted_value, tuple):
                        asserted_value = list(asserted_value)
                else:
                    name, fmt = field_spec
            else:
                raise TypeError(
                    f"Each field should be a single pad `'#x'` format string, a `(name, fmt)` pair, or a "
                    f"`(name, fmt, asserted)` triplet, not {field_spec}."
                )

            if name == "x":
                raise ValueError("Field name 'x' is reserved for internal labeling of pad fields.")
            elif name in self.field_names:
                raise ValueError(f"Field name {repr(name)} already exists in `BinaryStruct`.")

            try:
                field_byte_order, field_length, field_type = FMT_RE.match(fmt).groups()
            except AttributeError:
                raise ValueError(f"Invalid field format: '{fmt}'.")

            if field_byte_order:
                raise ValueError(
                    "Individual field format should not have its own byte order character. Use `byte_order` arg."
                )
            if field_type == "j":
                fmt = f"{field_length}s"
                encoding = "shift_jis_2004"
                length = 1
            elif field_type == "u":
                fmt = f"{field_length}s"
                encoding = byte_order.get_utf_16_encoding()
                length = 1
            elif field_type == "s":
                length = 1
            else:
                length = int(field_length) if field_length else 1

            new_fields.append(
                BinaryField(name=name, fmt=fmt, length=length, asserted_value=asserted_value, encoding=encoding)
            )
            sub_fmt += fmt
            sub_fmt_length += length

        self.fields += new_fields
        if new_fmt:
            self._struct_format.append(byte_order.value + sub_fmt)
            self._struct_length.append(sub_fmt_length)
        else:
            self._struct_format[-1] += sub_fmt
            self._struct_length[-1] += sub_fmt_length
        self.size = sum(struct.calcsize(sub_fmt) for sub_fmt in self._struct_format)

        return new_fields, byte_order.value + sub_fmt

    def unpack(
        self,
        source: bytes | io.BufferedIOBase,
        *fields,
        byte_order: ByteOrder = None,
        exclude_asserted=False,
        exclude_prefix="",
        offset: int = None,
    ) -> dict[str, tp.Any]:
        """Unpack a single struct from source data.

        If any 'fields' are specified (same allowed formats as the constructor above), only those fields will be
        unpacked, and they will then be added to the BinaryStruct. This allows you to dynamically build the BinaryStruct
        on the fly if the structure itself depends on the values read (e.g. a big-endian flag). The same BinaryStruct
        can then be used for repacking later.

        Args:
            source: bytes or open buffer to unpack from.
            fields: optional list of new fields to simultaneously add and unpack (instead of full struct).
            byte_order (ByteOrder): byte order of the new fields, or new byte order to fully override all
                previous byte orders passed along with fields, if no new fields are given.
            exclude_asserted: exclude any asserted fields in the returned dictionary.
            exclude_prefix: exclude any fields whose names start with this prefix, if given.
            offset (int): optional offset to unpack from. Old offset (for buffers) will be restored if this is given.

        Returns:
            Dictionary mapping field names to unpacked values.
        """
        old_offset = None
        if fields:
            # Unpack just the given fields after adding them to the BinaryStruct.
            struct_fields, struct_fmt = self.add_fields(*fields, byte_order=byte_order)
            size = struct.calcsize(struct_fmt)
            if isinstance(source, bytes):
                data = source if offset is None else source[offset:]
            else:
                if offset is not None:
                    old_offset = source.tell()
                    source.seek(offset)
                data = source.read(size)
            try:
                unpacked = struct.unpack(struct_fmt, data)
            except struct.error:
                _LOGGER.error(f"Failed to unpack data:", data)
                raise
            output = {}
            unpacked_index = 0
            for field in struct_fields:
                if (
                    field.length > 0
                    and not (exclude_asserted and field.asserted)
                    and not (exclude_prefix and field.name.startswith(exclude_prefix))
                ):
                    output[field.name] = field.parse_for_unpack(unpacked, unpacked_index)
                unpacked_index += field.length
            if old_offset is not None:
                source.seek(old_offset)
            return output

        output = {}
        if not self.fields:
            return output  # empty struct

        data_offset = 0
        if isinstance(source, bytes):
            data = source if offset is None else source[offset:]
        else:
            if offset is not None:
                old_offset = source.tell()
                source.seek(offset)
            data = source.read(self.size)
        unpacked = []
        for sub_fmt in self._struct_format:
            if byte_order:
                sub_fmt = byte_order.value + sub_fmt.lstrip('<>@')
            size = struct.calcsize(sub_fmt)
            try:
                unpacked += struct.unpack(sub_fmt, data[data_offset:data_offset + size])
            except struct.error:
                _LOGGER.error(
                    f"Failed to unpack data at offset {data_offset} with sub-format {sub_fmt}: "
                    f"{data[data_offset:data_offset + size]}"
                )
                raise
            data_offset += size
        unpacked_index = 0
        for field in self.fields:
            if (
                field.length > 0
                and not (exclude_asserted and field.asserted)
                and not (exclude_prefix and field.name.startswith(exclude_prefix))
            ):
                output[field.name] = field.parse_for_unpack(unpacked, unpacked_index)
            unpacked_index += field.length
        if old_offset is not None:
            source.seek(old_offset)
        return output

    def unpack_count(
        self,
        source,
        count: int,
        byte_order: ByteOrder = None,
        exclude_asserted=False,
        exclude_prefix="",
        offset: int = None,
    ) -> list[dict[str, tp.Any]]:
        """Unpack `count` identical structs from `source`. See `unpack()` for more.

        Args:
            source: bytes or open buffer to unpack from.
            count: number of contiguous structs to unpack from source.
            byte_order (ByteOrder): byte order to unpack with. Defaults to order specified by fields.
            exclude_asserted (bool): exclude asserted fields in the output dictionary. (Default: False)
            exclude_prefix (str): exclude fields whose names start with this string, if given. (Default: "")
            offset (int): optional offset to unpack from. Old offset (for buffers) will be restored if this is given.

        Returns:
            list[AttributeDict]
        """
        old_offset = None
        if isinstance(source, bytes):
            source = source if offset is None else source[offset:]
        elif offset is not None:
            old_offset = source.tell()
            source.seek(offset)
        structs = [
            self.unpack(source, byte_order=byte_order, exclude_asserted=exclude_asserted, exclude_prefix=exclude_prefix)
            for _ in range(count)
        ]
        if old_offset is not None:
            source.seek(old_offset)
        return structs

    def parse_object_source(self, source: object, **kwargs) -> dict[str, tp.Any]:
        if isinstance(source, dict):
            struct_dict = source.copy()  # don't modify input dictionary
            struct_dict.update(kwargs)
        elif source is None:
            struct_dict = kwargs
        else:
            # Try pulling field values from attributes.
            struct_dict = {}
            for field in self.non_padding_fields:
                try:
                    struct_dict[field.name] = kwargs.pop(field.name)
                except KeyError:
                    try:
                        struct_dict[field.name] = getattr(source, field.name)
                    except AttributeError:
                        if field.asserted is None:
                            raise KeyError(
                                f"Non-asserted field {repr(field)} is not an attribute of given {type(source)} and "
                                f"was not passed as a keyword argument."
                            )
            if kwargs:
                raise ValueError(f"Invalid field names in `kwargs`: {list(kwargs)}")
        return struct_dict

    def pack(
        self, source: dict | object = None, **kwargs
    ) -> tp.Optional[bytes]:
        """Pack this `BinaryStruct` with field data given in `source`, which can be a `dict` (fields as keys) or
        `object` (fields as attributes). Any field names given as `kwargs` will take precedence over the fields given by
        `source`.
        """
        if not self.fields and source is None and not kwargs:
            return b""  # null struct (error will be raised below if any input is given)

        struct_dict = self.parse_object_source(source, **kwargs)

        output = b""
        to_pack = []
        for field in self.non_padding_fields:
            if field.asserted is not None:
                # Asserted values are written automatically, but you are permitted to pass the asserted value too.
                if struct_dict.pop(field.name, field.asserted) != field.asserted:
                    raise ValueError(
                        f"Field '{field.name}' has value {struct_dict[field.name]} instead of asserted value "
                        f"{field.asserted}."
                    )
                value = field.asserted
            else:
                try:
                    value = struct_dict.pop(field.name)
                except KeyError:
                    raise KeyError(f"Field '{field.name}' missing from struct dictionary.")
            value = field.parse_for_pack(value)
            to_pack.extend(value) if isinstance(value, list) else to_pack.append(value)
        if struct_dict:
            raise ValueError(f"`BinaryStruct.pack()` input dictionary has extraneous keys: {struct_dict.keys()}")
        pack_index = 0
        for sub_fmt, sub_fmt_length in zip(self._struct_format, self._struct_length):
            try:
                output += struct.pack(sub_fmt, *to_pack[pack_index:pack_index + sub_fmt_length])
            except struct.error:
                _LOGGER.error(
                    f"Failed to pack data at offset {pack_index} with sub-format {sub_fmt} and length "
                    f"{sub_fmt_length}:\n{to_pack[pack_index:pack_index + sub_fmt_length]}"
                )
                raise
        return output

    def pack_multiple(self, sources: tp.Sequence[dict]) -> bytes:
        """Pack multiple instances of this binary struct and return them joined.

        Note that `kwargs` of `pack()` cannot be used here. All `sources` must contain all non-asserted fields.
        """
        output = b""
        for struct_dict in sources:
            output += self.pack(struct_dict)
        return output

    def copy(self) -> BinaryStruct:
        bs = BinaryStruct()
        bs.fields = self.fields
        bs._struct_format = self._struct_format
        bs._struct_length = self._struct_length
        bs.size = self.size
        return bs

    @staticmethod
    def set_repeated_fields(struct_dict, field_start, value):
        """Looks for all fields in struct_dict that start with the given string and sets their value to 'value'."""
        for key in struct_dict:
            if key.startswith(field_start):
                struct_dict[key] = value

    def __repr__(self):
        return (
            f"BinaryStruct: {' '.join(self._struct_format)}\n" +
            "\n".join(f"  {i} :: {field}" for i, field in enumerate(self.fields))
        )

    def get_field(self, field_name: str) -> BinaryField:
        """Looks up `BinaryField` instance from `field_name` string. Cannot get padding fields."""
        hits = [field for field in self.fields if field.name == field_name and field.length > 0]
        # Can't get multiple hits, by unique field name rule in constructor.
        if not hits:
            raise KeyError(f"Invalid field name: {field_name}")
        return hits[0]

    @property
    def struct_format(self):
        return self._struct_format

    @property
    def non_padding_fields(self):
        """Return only non-padding fields (including asserted fields)."""
        return [field for field in self.fields if field.length > 0]

    @property
    def field_names(self):
        """Excludes padding fields and includes asserted fields."""
        return [field.name for field in self.fields if field.length > 0]


# TODO: deprecated.
class BinaryObject(abc.ABC):
    """Class whose fields are all specified in a `BinaryStruct` class attribute, `STRUCT`, with `set()` method.

    `DEFAULTS` can be used to specify defaults for specific field names. Otherwise, defaults will be based on the format
    of that field as type-hinted, or failing that, in `STRUCT` (0 for numeric types, False for booleans, etc.).

    Any field names that are type-hinted will also be initialized as that type whenever the attribute is set.

    This class is intended to be packed using a `BinaryWriter`, as can be seen with the `default_pack(writer)` method.
    """

    STRUCT: BinaryStruct = None
    DEFAULTS: dict[str, tp.Any] = {}

    Z_STRING_RE = re.compile(r"^__(\w\w+)__z$")

    _TYPE_HINTS = None  # type: tp.Optional[dict]

    def __init__(self, reader: BinaryReader = None, **kwargs):
        """Create instance from `reader`, in which case `kwargs` are passed to `unpack()`, or use `kwargs` directly
        to override default field values if `reader` is None.

        If `reader` is None, `kwargs` must all be valid field names, but note that field names starting with a double
        underscore will be ignored (these are "internal" fields). `kwargs` can included asserted fields, but the value
        of those fields will simply be validated against `STRUCT` and discarded.

        Each subclass should define its own fields for type checking before calling `super().__init__`, or simply
        specify type hints in the class and use `DEFAULTS` to set default values.
        """
        if not self.STRUCT:
            raise AttributeError(f"`BinaryObject` subclass `{self.__class__.__name__}` has no `STRUCT`.")
        if reader is not None:
            self.unpack(reader, **kwargs)  # `kwargs` are passed to `unpack`
        else:
            self._set_defaults()
            self.set(**kwargs)  # `kwargs` are field names

    @classmethod
    def _get_type_hints(cls):
        """Generated on first use and then saved to class, as `tp.get_type_hints()` is expensive."""
        if cls._TYPE_HINTS is None:
            cls._TYPE_HINTS = tp.get_type_hints(cls)
        return cls._TYPE_HINTS

    def set(self, **kwargs):
        """Set multiple fields (attributes) at once, via `__setattr__` below.

        Field names that start with "__" are ignored, which makes it easier to use an unpacked `BinaryStruct` dictionary
        as `kwargs`.
        """
        for field_name, value in kwargs.items():
            if not field_name.startswith("__"):
                setattr(self, field_name, value)

    def _set_defaults(self):
        for field in [
            f for f in self.STRUCT.fields
            if f.length > 0 and not f.name.startswith("__") and f.asserted is None
        ]:
            if hasattr(self, field.name):
                continue  # already defined (e.g. manually in `__init__()`).
            # TODO: Mutable `DEFAULTS` members are an issue here.
            default = self.DEFAULTS.get(field.name, self.get_field_default(field))
            setattr(self, field.name, default)

    def __setattr__(self, field_name: str, value):
        """Checks `field_name` is a valid field, confirms any asserted value, and casts value to a given type."""
        try:
            field_type = self._get_type_hints()[field_name]
        except KeyError:
            # Check `STRUCT` fields if no type hint exists.
            try:
                field = self.STRUCT.get_field(field_name)
            except KeyError:
                raise AttributeError(f"Invalid field for `BinaryObject`: {repr(field_name)}")
            if field.asserted:
                if field.asserted != value:
                    raise ValueError(
                        f"Field {repr(field_name)} must have asserted value {field.asserted}, not {value}."
                    )
                return  # do nothing (asserted fields are not exposed as attributes but can still be 'set' here)
        else:
            if type(field_type) is GenericAlias:
                # TODO: Enforce other `typing` type hints?
                pass
            elif inspect.isclass(field_type):
                if issubclass(field_type, (enum.Enum, Vector, Flags8)):
                    value = field_type(value)
                elif field_type in (bytes, str, int, float, tuple, list, set):
                    value = field_type(value)

        super().__setattr__(field_name, value)

    def extract_kwargs_from_struct(
        self, reader: BinaryReader, binary_struct: BinaryStruct = None, encoding=None, byte_order: ByteOrder = None
    ) -> dict[str, tp.Any]:
        if binary_struct is None:
            binary_struct = self.STRUCT
        data = reader.unpack_struct(binary_struct, exclude_asserted=True, byte_order=byte_order)
        kwargs = {}
        for field, value in data.items():
            match = self.Z_STRING_RE.match(field)
            if match:
                field_name = match.group(1)
                if encoding is None:
                    raise ValueError(
                        f"You must pass `encoding` to read {repr(field_name)} from string offset."
                    )
                kwargs[field_name] = reader.unpack_string(offset=data[field], encoding=encoding)
            else:
                kwargs[field] = data[field]
        return kwargs

    def default_unpack(self, reader: BinaryReader, encoding=None, byte_order: ByteOrder = None):
        """`BinaryObject` unpack methods will frequently require extra arguments, so the exact signature of `unpack()
        is left to each subclass.

        Setting `unpack = BinaryObject.default_unpack` in the class definition is an easy option.

        `STRUCT` fields that match template `STRING_OFFSET_RE` will immediately be read as null-terminated strings from
        the unpacked offset, and set to the field name in the template.
        """
        kwargs = self.extract_kwargs_from_struct(reader, self.STRUCT, encoding, byte_order)
        self.set(**kwargs)

    unpack = default_unpack

    def default_pack(self, writer: BinaryWriter):
        """`BinaryObject` pack methods will frequently require extra arguments, so the exact signature of `pack()` is
        left to each subclass.

        Setting `pack = BinaryObject.default_pack` in the class definition is an easy option.

        `STRUCT` fields that match template `STRING_OFFSET_RE` will be automatically reserved for future write, e.g.
        with `fill()` below.
        """
        reserved = {}
        for field in self.STRUCT.fields:
            if self.Z_STRING_RE.match(field.name):
                reserved[field.name] = writer.AUTO_RESERVE
        writer.pack_struct(self.STRUCT, self, **reserved)

    def fill(self, writer: BinaryWriter, **kwargs):
        """Fill all auto-reserved fields in `kwargs` with the given values."""
        for field_name, value in kwargs.items():
            writer.fill(field_name, value, obj=self)

    def __repr__(self) -> str:
        output = f"{self.__class__.__name__}(\n"
        for field_name in self._get_type_hints():
            if field_name not in {"STRUCT", "DEFAULTS"}:
                output += f"    {field_name}={repr(getattr(self, field_name))},\n"
        output += ")"
        return output

    @classmethod
    def get_field_default(cls, field: BinaryField) -> str | bytes | bool | int | float:
        if field.asserted:
            return field.asserted
        field_types = cls._get_type_hints()
        if field.name in field_types:
            field_type = field_types[field.name]
            try:
                return field_type.default()
            except AttributeError:
                if field_type is str:
                    return ""
                elif field_type is bytes:
                    return b""
                elif field_type is bool:
                    return False
                elif field_type is int:
                    return 0
                elif field_type is float:
                    return 0.0

        # Fall back to `STRUCT` format.
        _, field_length, field_type = FMT_RE.match(field.fmt).groups()  # cannot fail
        if field_type == "s":
            if field.encoding:
                return ""
            return b""
        elif field_type == "?":
            return False
        elif field_type in {"f", "d"}:
            return 0.0
        elif field_type.lower() in {"b", "h", "i", "q"}:
            return 0
        raise TypeError(f"Unrecognized field type for `BinaryObject`: {repr(field_type)}")

# endregion


class BinaryBase:

    # Special format characters that become 'iI' or 'qQ' depending on `var_int_size`.
    VAR_INT = "v"
    VAR_UINT = "V"
    default_byte_order: ByteOrder
    varint_size: int  # 4 or 8 (determines size of 'v' and 'V' format characters)

    def __init__(self, byte_order=ByteOrder.LittleEndian, var_int_size=4):
        self.default_byte_order = ByteOrder(byte_order)
        if var_int_size not in {4, 8}:
            raise ValueError(f"{self.__class__.__name__} `var_int_size` must be 4 or 8, not {var_int_size}.")
        self.varint_size = var_int_size

    def parse_fmt(self, fmt: str) -> str:
        """Insert default byte order and replace 'vV' var int characters."""
        if fmt[0] not in "@=><!":
            fmt = self.default_byte_order.value + fmt
        if self.varint_size == 4:
            fmt = fmt.replace("v", "i").replace("V", "I")
        elif self.varint_size == 8:
            fmt = fmt.replace("v", "q").replace("V", "Q")
        else:
            raise ValueError(f"`BinaryWriter.var_int_size` must be 4 or 8, not {self.varint_size}.")
        if "v" in fmt or "V" in fmt:
            raise ValueError(f"Could not parse 'v' and 'V' characters in `fmt` without `varint_size`: {fmt}")
        return fmt

    def get_utf_16_encoding(self) -> str:
        return self.default_byte_order.get_utf_16_encoding()


class BinaryReader(BinaryBase):
    """Manages an buffered binary IO stream, with methods for unpacking data and moving to temporary offsets."""

    class ReaderError(Exception):
        """Exception raised when trying to unpack data."""
        pass

    buffer: tp.BinaryIO | io.BufferedIOBase | None

    def __init__(
        self,
        buffer: str | Path | bytes | bytearray | io.BufferedIOBase | BinderEntry | BinaryReader,
        default_byte_order=ByteOrder.LittleEndian,
        varint_size=8,
    ):
        super().__init__(default_byte_order, varint_size)

        self.buffer = None

        if isinstance(buffer, str):
            buffer = Path(buffer)
        if isinstance(buffer, Path):
            self.buffer = buffer.open("rb")
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

    def peek(self, fmt_or_size: str | int) -> bool | int | float | bytes | tuple:
        """Unpack `fmt_or_size` (or just read bytes) and return the unpacked values without changing the offset."""
        if isinstance(fmt_or_size, int):
            return self.read(fmt_or_size, offset=self.position)
        return self.unpack(fmt_or_size, offset=self.position)

    def peek_value(self, fmt) -> bool | int | float:
        """Unpack `fmt` and return the unpacked value without changing the offset."""
        return self.unpack_value(fmt, offset=self.position)

    def unpack_struct(
        self,
        binary_struct: BinaryStruct,
        *fields,
        byte_order: ByteOrder = None,
        exclude_asserted=False,
        exclude_prefix="",
        offset: int = None,
    ) -> dict[str, tp.Any]:
        return binary_struct.unpack(
            self.buffer,
            *fields,
            byte_order=byte_order,
            exclude_asserted=exclude_asserted,
            exclude_prefix=exclude_prefix,
            offset=offset,
        )

    def unpack_structs(
        self,
        binary_struct: BinaryStruct,
        count: int,
        byte_order: ByteOrder = None,
        exclude_asserted=False,
        exclude_prefix="",
        offset: int = None,
    ) -> list[dict[str, tp.Any]]:
        return binary_struct.unpack_count(self.buffer, count, byte_order, exclude_asserted, exclude_prefix, offset)

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
    def temp_offset(self, offset: int):
        """Seek `buffer` to `offset` temporarily, then reset to original offset when done."""
        initial_offset = self.buffer.tell()
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

    reserved: dict[str, tuple[int, str]]

    def __init__(self, byte_order=ByteOrder.LittleEndian, varint_size=8):
        super().__init__(byte_order, varint_size)
        self.reserved = {}
        self._array = bytearray()

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

    def append(self, other: bytearray | bytes):
        """Manually add existing binary data (e.g. a packed `BinaryStruct`) all at once."""
        self._array += other

    def pack_new_struct(self, new_binary_struct: NewBinaryStruct, allow_reserved=True):
        if allow_reserved:
            new_binary_struct.to_writer(self)
        else:
            self._array += bytes(new_binary_struct)

    def pack_struct(
        self,
        binary_struct: BinaryStruct,
        source: dict | object = None,
        **kwargs,
    ):
        """Pack and/or reserve all fields present in `binary_struct`.

        Use `BinaryWriter.Reserved("ReservedName")` as keyword argument values to reserve those fields.
        """
        struct_dict = binary_struct.parse_object_source(source, **kwargs)
        reserved = {
            field: struct_dict.pop(field) for field in tuple(struct_dict)
            if isinstance(struct_dict[field], self.Reserved)
        }
        for field in binary_struct.fields:
            if field.length == 0:  # padding
                if field.name in reserved:
                    raise ValueError(f"Padding field {repr(field.name)} cannot be in `reserved` dictionary.")
                self.pack(field.fmt)
            else:
                if field.asserted is not None:
                    if field.name in reserved:
                        raise ValueError(f"Asserted field {repr(field.name)} cannot be in `reserved` dictionary.")
                    if struct_dict.pop(field.name, field.asserted) != field.asserted:
                        raise ValueError(
                            f"Field '{field.name}' has value {struct_dict[field.name]} instead of asserted value "
                            f"{field.asserted}."
                        )
                    value = field.asserted
                else:
                    try:
                        value = struct_dict.pop(field.name)
                    except KeyError:
                        if field.name in reserved:
                            reserved_name = reserved.pop(field.name)
                            if not reserved_name:
                                # Auto-generate reserved name from `id(source)` and field name.
                                if source is None or type(source) is dict:
                                    raise ValueError("Cannot auto-generate reserved name from `dict` `source`.")
                                reserved_name = f"{id(source)}({field.name})"
                            self.reserve(reserved_name, field.fmt)
                            continue
                        raise KeyError(f"Field '{field.name}' not given in struct or reserved dictionary.")
                field_value = field.parse_for_pack(value)
                try:
                    if isinstance(field_value, list):
                        self.pack(field.fmt, *field_value)  # unpack
                    else:
                        self.pack(field.fmt, field_value)
                except struct.error:
                    _LOGGER.error(
                        f"Pack error: field = {field.name}, fmt = {repr(field.fmt)}, values = {repr(field_value)}"
                    )
                    raise

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
            name = f"{id(obj)}({name})"
        if name in self.reserved:
            raise ValueError(f"Name {repr(name)} is already reserved in `BytesWriter`.")
        fmt = self.parse_fmt(fmt)
        self.reserved[name] = (len(self._array), fmt)
        self._array += b"\0" * struct.calcsize(fmt)  # reserved space is nulls

    def fill(self, name: str, *values, obj: object = None):
        if obj is not None:
            name = f"{id(obj)}({name})"
            if name not in self.reserved:
                raise ValueError(f"Field {repr(name)} reserved by `{type(obj).__name__}` object not found.")
        elif name not in self.reserved:
            raise ValueError(f"Name {repr(name)} is not reserved in `BytesWriter`.")
        offset, fmt = self.reserved[name]  # fmt endianness already specified
        try:
            packed = struct.pack(fmt, *values)
        except struct.error:
            raise ValueError(f"Error occurred when packing values to reserved offset with fmt {repr(fmt)}: {values}")
        self._array[offset:offset + len(packed)] = packed
        self.reserved.pop(name)  # pop after successful fill only

    def fill_with_position(self, name: str, obj: object = None):
        """Fill `name` (optionally also identified by `id(obj)` with current `writer.position`."""
        self.fill(name, self.position, obj=obj)

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


def get_blake2b_hash(data: bytes | str | Path) -> bytes:
    if isinstance(data, (str, Path)):
        file_hash = hashlib.blake2b()
        with Path(data).open("rb") as f:
            chunk = f.read(8192)
            while chunk:
                file_hash.update(chunk)
                chunk = f.read(8192)
        return file_hash.digest()
    elif isinstance(data, bytes):
        return hashlib.blake2b(data).digest()
    raise TypeError(f"Can only get hash of `bytes` or `str`/`Path` of file, not {type(data)}.")


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
_PRIMITIVE_FIELD_INFO = {
    bool: ("?", 1, None),
    byte: ("B", 1, (0, 2 ** 8 - 1)),
    sbyte: ("b", 1, (-(2 ** 7), (2 ** 7) - 1)),
    ushort: ("H", 2, (0, (2 ** 16) - 1)),
    short: ("h", 2, (-(2 ** 15), (2 ** 15) - 1)),
    uint: ("I", 4, (0, (2 ** 32) - 1)),
    int: ("i", 4, (-(2 ** 31), (2 ** 31) - 1)),
    ulong: ("Q", 8, (0, (2 ** 64) - 1)),
    long: ("q", 8, (-(2 ** 63), (2 ** 63) - 1)),
    float: ("f", 4, None),
    double: ("d", 8, None),
    varint: ("v", None, None),  # `size` and `min_max` must be computed
    varuint: ("V", None, None),  # `size` and `min_max` must be computed
}


# Valid field types for `auto_offset`.
_OFFSET_FIELD_TYPES = (
    byte, sbyte, ushort, short, uint, int, ulong, long, varint, varuint
)


FIELD_T = tp.TypeVar("FIELD_T")
CONDITION_T = tp.TypeVar("CONDITION_T", bool, int, str, ByteOrder)


@dataclasses.dataclass(slots=True)
class BinaryCondition(tp.Generic[CONDITION_T]):
    """Pass to `BinaryStruct` arguments (including most `field` arguments, such as `length`, `encoding`, and `asserted`)
    to use different values based on the state of binary data of `size` at any absolute `offset` in the stream.

    If neither `true_value` nor `false_value` is found, an error will be raised.

    For example: most file formats are either little-endian (PC, new consoles) or big-endian (older consoles), with an
    early telltale byte or bytes indicating which. Those bytes (`size` bytes at offset `offset`) will be used to
    determine which endianness should be used.
    """
    offset_and_size: tuple[int, int]
    callback_or_conditions: tp.Callable[[tp.Any], CONDITION_T] | tp.Sequence[tuple[CONDITION_T, bytes]] = None
    relative_offset: bool = False

    def __call__(self, stream: tp.BinaryIO | BinaryReader) -> CONDITION_T | bytes:
        if isinstance(self.offset_and_size, tuple):
            initial_offset = stream.tell()
            offset, size = self.offset_and_size
            stream.seek(offset, (1 if self.relative_offset else 0))
            value = stream.read(size)
            stream.seek(initial_offset)
        else:
            raise TypeError("First argument of `BinaryCondition` must be a field name string or (offset, size) pair.")

        if callable(self.callback_or_conditions):
            return self.callback_or_conditions(value)
        elif self.callback_or_conditions:
            for result, test_value in self.callback_or_conditions:
                if value == test_value:
                    return result
            raise ValueError(f"Bytes found did not match any given conditional result: {value}")
        else:
            return value


@dataclasses.dataclass(slots=True)
class FieldValue(tp.Generic[FIELD_T]):
    """Pass to some `binary` arguments to use a prior field's unpacked value for that argument.

    If `callback` is given, the field's value will be passed through it.
    """
    field_name: str
    callback: tp.Callable[[tp.Any], FIELD_T] | None = None
    consume_prior_field: bool = True

    def __call__(self, field_values: dict[str, tp.Any]) -> FIELD_T:
        try:
            value = field_values[self.field_name]
        except KeyError:
            raise KeyError(f"Cannot get `FieldValue` from field name: {self.field_name}")
        if self.consume_prior_field:
            field_values[self.field_name] = None
        return value if self.callback is None else self.callback(value)


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
class BinaryFieldMetadata(tp.Generic[FIELD_T]):
    """Base class for objects attached to dataclass fields with `field(metadata={"binary": BinaryFieldMetadata()})`.

    Contains all attributes used, in different situations, by `BinaryStruct` unpacking and packing. Not all combinations
    of attributes are valid (e.g. `encoding` must be set for `str` fields only).

    NOTE: Use the `binary` utility function with `**` to generate the metadata dictionary as effortlessly as possible:
        `number: int = field(**binary(asserted=[1, 2], alignment=4))`
    This function also takes the normal `field` keyword arguments, like `init` and `default`, and can generate them. It
    allows for the most abbreviated usage while still using `field` explicitly (which type checkers like to see...).
    """
    # If given, this will be used instead of standard `dataclasses.Field.type` when unpacking the field (e.g. if it
    # is more useful for the field type hints to be standard Python types). Otherwise, it will be set from the `Field`
    # upon validation.
    type: tp.Type[PRIMITIVE_FIELD_TYPING] | None = None

    # Format for `struct.pack` and `struct.unpack`. Absent only for variable-length fields (notably null-terminated
    # strings) and nested `BinaryStruct` classes. Will override the annotation type if present (so that structs can
    # double as useful dataclasses without using dummy type hints like `short`).
    fmt: str | None = None

    # If field type is unhandled, it will be constructed from the `tuple` output of `struct.unpack()` using this factory
    # function. If not given, the default factory `field_type(*tuple)` will be used for unhandled field types.
    type_factory: tp.Callable[[tuple], FIELD_T] | None = None

    # If field type is unhandled, it will be converted to a `tuple` input for `struct.pack(*tuple)` using this factory
    # function. If not given, `tuple()` itself will simply be used.
    pack_factory: tp.Callable[[FIELD_T], tuple] | None = None

    # If given, field value must be in this list at unpack and pack time. Other changes to its value in between are not
    # checked and will not have any negative effect until you try to pack the struct.
    asserted: list[tp.Any] = dataclasses.field(default_factory=list)

    # If given, reader/writer will seek/pad to this offset before reading/writing this field.
    offset: int | str | FieldValue[int] | None = None

    # Alignment of binary stream will be padded up to this (modulo) position BEFORE reading/writing the field value.
    # Default of 1 has no effect. Must be 1 if `offset` is not `None`.
    alignment: int = 1

    # Can be supplied instead of `fmt` to use variables, such as a field name string, to determine the format.
    length: int | str | FieldValue[int] | None = None

    # String encoding to use for decoding read `bytes` to `str` types. Invalid for non-`str` fields.
    # If set to `utf-16` or `utf16`, endianness will be auto-detected from `ByteOrder`.
    encoding: str | None = None

    # If `True` (NOT default), null bytes will be stripped from the end of a read fixed-length `bytes` or `str` field.
    # Does not affect null-terminated strings, which will always have the terminator stripped/added. When packing, the
    # fixed-length field will always be padded out to the required size, regardless of this value.
    # NOTE: If asserting fixed-length values, make sure they take this argument into consideration.
    rstrip_null: bool = False

    # If not -1, data will be read from partial bits of data sized by `fmt`. Sequential bit fields with the same `fmt`
    # can be unpacked from the same single byte (or more). When a non-bit-field is encountered, the rest of `fmt` will
    # be consumed.
    bit_count: int = -1

    # If `True` (NOT default), this field will NOT be unpacked in `from_bytes()` and CANNOT be packed in `to_writer()`.
    # This is usually because additional information is required to unpack/pack the field, or it occurs much later in
    # a larger file (but still has a link to this struct, e.g. via header offsets). If ANY field uses this, the struct
    # cannot be cast directly to `bytes`; you must use `to_writer()` and resolve this field externally before finishing.
    deferred: bool = False

    # If given, this callback (called with `varint_size` and the `field_values` obtained thus far) will be used to
    # determine if this field should be skipped entirely. This is ideal for simple cases only, like pads that only
    # appear for a certain `varint_size`, etc. If skipped, the field value will be `None`.
    skip_callback: tp.Callable[[int, dict[str, tp.Any]], bool] | None = None

    # Assigned during validation for convenience.
    name: str = dataclasses.field(init=False, default="")

    @staticmethod
    def resolve_fmt_type(fmt_type: str | tp.Type[PRIMITIVE_FIELD_TYPING]) -> str:
        if isinstance(fmt_type, str):
            return fmt_type
        return _PRIMITIVE_FIELD_INFO[fmt_type][0]

    def check_asserted(self, value: FIELD_T) -> tp.Optional[FIELD_T]:
        """Checks that `value` is in `self.asserted`, if not empty.

        If it is, and `len(self.asserted) == 1`, `None` is returned instead to be clear that this is not a field to be
        modified (as the lone asserted value will be used at packing anyway).
        """
        if not self.asserted:
            return value  # nothing to check
        elif value not in self.asserted:
            raise BinaryFieldValueError(f"Field `{self.name}` has value {value} not in `asserted`: {self.asserted}")
        elif len(self.asserted) == 1:
            return None
        return value  # valid among multiple asserted values

    def validate(self, field: dataclasses.Field, field_type: tp.Type, cls_name: str):
        """Called by `NewBinaryStruct` metaclass on child class creation."""

        self.name = field.name
        if self.type is None:
            self.type = field_type

        if self.deferred:
            if self.alignment > 1 or self.offset is not None:
                raise BinaryFieldTypeError(
                    field, cls_name,
                    "`deferred` binary fields cannot have `offset` or `alignment > 1`.",
                )

        # Field type cannot be `list` or `tuple` with no element types given.
        if field_type is list:
            raise BinaryFieldTypeError(
                field, cls_name,
                "`list` binary fields must specify exactly one element type (e.g. `list[int]`) and `length` metadata.",
            )
        if field_type is tuple:
            raise BinaryFieldTypeError(
                field, cls_name,
                "`tuple` binary fields must specify at least one element type (e.g. `tuple[int, float, int]`)."
            )

        # TODO: Doesn't work with real int-derived types like `short`.
        # for asserted_value in self.asserted:
        #     if not isinstance(asserted_value, field_type):
        #         raise BinaryFieldTypeError(field, cls_name, f"Invalid asserted value type: {asserted_value}")

        if self.alignment > 1 and self.offset is not None:
            raise BinaryFieldTypeError(field, cls_name, "Cannot combine `offset` with `alignment > 1`.")

        if isinstance(field_type, GenericAlias):
            # Recur on tuple of primitive field types (MUST be primitive, i.e. handled in this very block).
            # Container MUST be a tuple so its exact length/contents can be defined in the type hint.
            # List types must have metadata with at least a `length` argument (tuples are also welcome to).
            if field_type.__origin__ is list:
                if self.length is None:
                    raise BinaryFieldTypeError(
                        field, cls_name, "`list` binary fields must have at least `binary(length)` metadata."
                    )
                if len(field_type.__args__) != 1:
                    raise BinaryFieldTypeError(
                        field, cls_name,
                        "`list` binary fields must specify exactly one element type (e.g. `list[int]`)."
                    )
                # Continue validation on element type.
                field_type = field_type.__args__[0]
            elif field_type.__origin__ is tuple:
                if not field_type.__args__:
                    raise BinaryFieldTypeError(
                        field, cls_name,
                        "`tuple` binary fields must specify at least one element type (e.g. `tuple[int, float, int]`)."
                    )
                if self.length is not None and self.length != len(field_type.__args__):
                    raise BinaryFieldTypeError(
                        field, cls_name,
                        "`tuple` binary field element types must match `length` metadata, if given.",
                    )
                # TODO: Need to validate tuple element types recursively...?
            else:
                raise BinaryFieldTypeError(
                    field, cls_name,
                    f"Invalid generic type: `{field_type.__origin__}`. Must be `tuple` or (if `length` given) `list`."
                )

        if self.length is not None:
            if self.fmt is not None:
                raise BinaryFieldTypeError(field, cls_name, "Cannot specify both `fmt` and `length`.")

        if field_type is str:
            if self.encoding is None:
                raise BinaryFieldTypeError(field, cls_name, "String field must have `encoding`.")
        elif self.encoding is not None:
            raise BinaryFieldTypeError(
                field, cls_name,
                "Only `str` field can use `encoding`. (Custom types initialized from strings are not yet supported.)",
            )

        if self.bit_count != -1:
            if self.fmt is None:
                raise BinaryFieldTypeError(field, cls_name, "Bit field type requires `fmt` metadata.")
            max_size = struct.calcsize(self.fmt) * 8
            if self.bit_count > max_size:
                raise BinaryFieldTypeError(
                    field, cls_name, f"Bit field with bit count {self.bit_count} is too high for `fmt` {self.fmt}."
                )

        if field_type is not bytes and field_type is not str and field_type not in PRIMITIVE_FIELD_TYPES:
            # All non-primitive types must have `fmt`.
            if self.fmt is None:
                raise BinaryFieldTypeError(field, cls_name, "Non-primitive field type requires `fmt` metadata.")

    @staticmethod
    def resolve_condition(condition: tp.Any, reader: BinaryReader | None, field_values: dict[str, tp.Any]) -> tp.Any:
        if isinstance(condition, BinaryCondition):
            return condition(reader)
        if isinstance(condition, str):  # consume field name
            return field_values.pop(condition)
        if isinstance(condition, FieldValue):
            return condition(field_values)
        return condition


def _validate_binary_field_without_metadata(field: dataclasses.Field, field_type: tp.Type, cls_name: str):
    """Called by `NewBinaryStruct` metaclass on child class creation.

    Does basic validation only, for fields with no `BinaryFieldMetadata` given to "binary" key of metadata.
    """

    # Field type cannot be `list` or `tuple` with no element types given.
    if field_type is list:
        raise BinaryFieldTypeError(
            field, cls_name,
            "`list` binary fields must specify exactly one element type (e.g. `list[int]`) and `length` metadata.",
        )
    if field_type is tuple:
        raise BinaryFieldTypeError(
            field, cls_name,
            "`tuple` binary fields must specify at least one element type (e.g. `tuple[int, float, int]`).",
        )

    if isinstance(field_type, GenericAlias):
        # Recur on tuple of primitive field types (MUST be primitive, i.e. handled in this very block).
        # Container MUST be a tuple so its exact length/contents can be defined in the type hint.
        # List types must have metadata with at least a `length` argument (tuples are also welcome to).
        if field_type.__origin__ is list:
            raise BinaryFieldTypeError(
                field, cls_name, "`list` binary fields must have at least `binary(length)` metadata.",
            )
        if field_type.__origin__ is not tuple:
            raise BinaryFieldTypeError(
                field, cls_name,
                f"Invalid binary field container type : `{field_type.__origin__}`. "
                f"Must be tuple or (if `length` given) list."
            )
        return

    if field_type not in _PRIMITIVE_FIELD_INFO and field_type not in (Vector2, Vector3, Vector4):
        raise BinaryFieldTypeError(field, cls_name, "Cannot handle this field type without `binary()` metadata.")


def _unpack_binary_field(
    metadata: BinaryFieldMetadata | None,
    reader: BinaryReader,
    field_type: tp.Type,
    byte_order: ByteOrder,
    varint_size: int,
    field_values: dict[str, tp.Any],
    **overrides,
) -> tp.Any:
    """Process metadata and field type to get the final value that will actually be assigned to the dataclass field.

    `overrides` can have 'offset' and 'encoding' keys that will replace field metadata for this call (e.g. when it is
    not possible to compute them purely from their containing struct class).
    """
    if metadata is None:
        # Primitive field with no extra metadata.
        if issubclass(field_type, NewBinaryStruct):
            # NOTE: Nested struct will inherit `byte_order` and `varint_size` from caller struct.
            return field_type.from_bytes(reader, byte_order, varint_size)

        if isinstance(field_type, GenericAlias):
            values = [
                _unpack_binary_field(None, reader, element_type, byte_order, varint_size, field_values)
                for element_type in field_type.__args__
            ]
            return tuple(values)

        if field_type is Vector2:
            return Vector2(*struct.unpack(byte_order.value + "2f", reader.read(8)))
        elif field_type is Vector3:
            return Vector3(*struct.unpack(byte_order.value + "3f", reader.read(12)))
        elif field_type is Vector4:
            return Vector4(*struct.unpack(byte_order.value + "4f", reader.read(16)))

        fmt, _, _ = _PRIMITIVE_FIELD_INFO[field_type]
        fmt = _process_fmt_varint(fmt, varint_size)
        size = struct.calcsize(fmt)
        return struct.unpack(byte_order.value + fmt, reader.read(size))[0]  # type: PRIMITIVE_FIELD_TYPING

    # Prepare stream position.
    initial_offset = None
    if "offset" in overrides:
        if metadata.offset is not None:
            raise ValueError("Cannot manually specify `offset` for unpacking this field.")
        initial_offset = reader.tell()
        reader.seek(overrides["offset"])
    else:
        if metadata.alignment > 1:
            mod_current_position = reader.tell() % metadata.alignment
            if mod_current_position > 0:  # move forward by difference (to reach mod 0)
                reader.seek(metadata.alignment - mod_current_position, 1)
        elif metadata.offset is not None:
            initial_offset = reader.tell()
            offset = metadata.resolve_condition(metadata.offset, reader, field_values)
            reader.seek(offset)

    def reset_stream():
        if initial_offset is not None:
            reader.seek(initial_offset)

    if issubclass(field_type, NewBinaryStruct):
        # NOTE: Nested struct will inherit `byte_order` and `varint_size` from caller struct.
        unpacked_struct = field_type.from_bytes(reader, byte_order, varint_size)
        reset_stream()
        return unpacked_struct

    if isinstance(field_type, GenericAlias):
        # Recur on tuple of primitive field types (MUST be primitive, i.e. handled in this very block).
        # Container MUST be a tuple so its exact length/contents can be defined in the type hint.
        # List types must have metadata with at least a `length` argument (tuples are also welcome to).
        if field_type.__origin__ is list:
            element_type = field_type.__args__[0]
            length = metadata.resolve_condition(metadata.length, reader, field_values)
            values = [
                _unpack_binary_field(None, reader, element_type, byte_order, varint_size, field_values)
                for _ in range(length)
            ]
            reset_stream()
            return metadata.check_asserted(values)

        if field_type.__origin__ is tuple:
            values = [
                _unpack_binary_field(None, reader, element_type, byte_order, varint_size, field_values)
                for element_type in field_type.__args__
            ]
            reset_stream()
            return metadata.check_asserted(tuple(values))

        # Shouldn't be reachable due to initial class validation, but shouldn't let corner cases fall through to
        # code below (and some kind of unhandled nested list type could reach this).
        raise BinaryFieldValueError(
            f"Field `{metadata.name}` has invalid generic type: {field_type.__origin__}. "
            f"Must be `tuple` or (if `length` given) `list`."
        )

    if field_type in _PRIMITIVE_FIELD_INFO:
        # Primitive type.
        fmt, _, _ = _PRIMITIVE_FIELD_INFO[field_type]  # no need to check `min_max` when unpacking
        fmt = _process_fmt_varint(fmt, varint_size)
        buffer = reader.read(struct.calcsize(fmt))
        value = struct.unpack(byte_order.value + fmt, buffer)[0]  # type: PRIMITIVE_FIELD_TYPING
        reset_stream()
        return metadata.check_asserted(value)

    # Get format or length, or otherwise resolve null-terminated string immediately.
    if metadata.length is not None:
        length = metadata.resolve_condition(metadata.length, reader, field_values)
        fmt = f"{length}s"
    elif metadata.fmt is not None:
        fmt = _process_fmt_varint(metadata.fmt, varint_size)
    elif field_type in (bytes, str):
        # Null-terminated.
        if "encoding" in overrides:
            encoding = overrides["encoding"]
        elif isinstance(metadata.encoding, BinaryCondition):
            encoding = metadata.encoding(reader)
        else:
            encoding = metadata.encoding
        value = read_null_terminated_bytes(reader, encoding)
        reset_stream()
        return metadata.check_asserted(value)
    else:
        # Shouldn't be reachable, but don't want to fall through.
        raise BinaryFieldValueError(f"Non-primitive field `{metadata.name}` must have `fmt` or `length`.")

    # TODO: Should I just assert that `stream` is a `BinaryReader`?
    raw_tuple = struct.unpack(byte_order.value + fmt, reader.read(struct.calcsize(fmt)))  # type: tuple

    if field_type is str:
        if "encoding" in overrides:
            encoding = overrides["encoding"]
        elif isinstance(metadata.encoding, BinaryCondition):
            encoding = metadata.encoding(reader)
        else:
            encoding = metadata.encoding
        if encoding is not None and encoding.replace("-", "").lower() == "utf16":
            encoding = byte_order.get_utf_16_encoding()
        raw_value = raw_tuple[0]
        if metadata.rstrip_null:
            raw_value = raw_value.rstrip(b"\0")
        value = raw_value.decode(encoding)
        reset_stream()
        return metadata.check_asserted(value)

    if field_type is bytes:
        value = raw_tuple[0]
        if metadata.rstrip_null:
            value = value.rstrip(b"\0")
        reset_stream()
        return metadata.check_asserted(value)

    # Otherwise, load tuple into custom field type.
    if metadata.type_factory is not None:
        value = metadata.type_factory(*raw_tuple)
    else:  # default is to just call field type
        value = field_type(*raw_tuple)
    reset_stream()
    return metadata.check_asserted(value)


def _process_fmt_varint(fmt: str, varint_size: int | None) -> str:
    if "v" in fmt or "V" in fmt:
        if varint_size is None:
            raise BinaryFieldValueError("`varint_size` required to handle binary field.")
        return fmt.replace("v", "i" if varint_size == 4 else "q").replace("V", "I" if varint_size == 4 else "Q")
    return fmt


def _pack_binary_field(
    metadata: BinaryFieldMetadata | None,
    writer: BinaryWriter,
    field_type: tp.Type,
    field_value: tp.Any,
    byte_order: ByteOrder,
    varint_size: int,
    field_values: dict[str, tp.Any],
    stored_encoding: str | None = None,
    **overrides,
):
    """Pack `field_value` to binary data using field type, optional metadata, and other contextual information.

    `overrides` kwargs support 'encoding' only.
    """
    if isinstance(field_value, NewBinaryStruct):
        # Nested struct will use its own `byte_order` and `varint_size` (probably inherited from this struct when
        # unpacked from bytes).
        field_value.to_writer(writer)
        return

    if metadata is None:
        # Primitive field with no extra metadata.
        if isinstance(field_type, GenericAlias):
            # Recur on tuple of primitive field types (MUST be primitive, i.e. handled in this very block).
            # Container MUST be a tuple so its exact length/contents can be defined in the type hint.
            # List types must have metadata with at least a `length` argument (tuples are also welcome to).
            if len(field_value) != len(field_type.__args__):
                # NOTE: No way to get field name here (no metadata).
                raise BinaryFieldValueError("`tuple` field value has wrong number of arguments.")
            for element_type, element_value in zip(field_type.__args__, field_value):
                _pack_binary_field(
                    None, writer, element_type, element_value, byte_order, varint_size, field_values, stored_encoding
                )
            return

        if field_type is Vector2:
            writer.pack("2f", *field_value)
            return
        elif field_type is Vector3:
            writer.pack("3f", *field_value)
            return
        elif field_type is Vector4:
            writer.pack("4f", *field_value)
            return

        fmt, _, min_max = _PRIMITIVE_FIELD_INFO[field_type]
        fmt = _process_fmt_varint(fmt, varint_size)
        if min_max is not None and (field_value < min_max[0] or min_max[1] < field_value):
            raise BinaryFieldValueError(f"Value {field_value} is out of range {min_max} for field type `{field_type}`.")
        writer.pack(fmt, field_value)
        return

    if metadata.alignment > 1:
        writer.pad_align(metadata.alignment)
    elif metadata.offset is not None:
        writer.pad_to_offset(metadata.offset)

    if isinstance(field_type, GenericAlias):
        # Recur on tuple of primitive field types (MUST be primitive, i.e. handled in this very block).
        # Container MUST be a tuple so its exact length/contents can be defined in the type hint.
        # List types must have metadata with at least a `length` argument (tuples are also welcome to).
        if field_type.__origin__ is list:
            element_type = field_type.__args__[0]
            for element_value in field_value:
                _pack_binary_field(
                    None, writer, element_type, element_value, byte_order, varint_size, field_values, stored_encoding
                )
            return

        if field_type.__origin__ is tuple:
            if len(field_value) != len(field_type.__args__):
                raise BinaryFieldValueError(f"Field `{metadata.name}` `tuple` value has wrong number of arguments.")
            for element_type, element_value in zip(field_type.__args__, field_value):
                _pack_binary_field(
                    None, writer, element_type, element_value, byte_order, varint_size, field_values, stored_encoding
                )
            return

        # Shouldn't be reachable due to initial class validation, but shouldn't let corner cases fall through to
        # code below (and some kind of unhandled nested list type could reach this).
        raise BinaryFieldValueError(
            f"Field `{metadata.name}` has invalid generic type: {field_type.__origin__}. "
            f"Must be `tuple` or (if `length` given) `list`."
        )

    if "encoding" in overrides:
        encoding = overrides["encoding"]
    elif isinstance(metadata.encoding, BinaryCondition):
        if stored_encoding is None:
            raise BinaryFieldValueError(
                f"`stored_encoding` required to pack string field `{metadata.name}` with conditional encoding."
            )
        encoding = stored_encoding
    else:
        if stored_encoding is not None:
            enc_msg = "no encoding" if metadata.encoding is None else f"fixed encoding '{metadata.encoding}'"
            raise BinaryFieldValueError(
                f"`stored_encoding` cannot be used to pack string field `{metadata.name}` with {enc_msg}."
            )
        encoding = metadata.encoding  # could be None

    if encoding is not None and encoding.replace("-", "").lower() == "utf16":
        encoding = byte_order.get_utf_16_encoding()

    # Get format or length, or otherwise resolve null-terminated string immediately.
    if metadata.length is not None:  # NOTE: `list` also uses `length`, but that was handled above already
        # TODO: `BinaryCondition` cannot be used for `length` unless it is stored.
        length = metadata.resolve_condition(metadata.length, None, field_values)
        bytes_value = field_value.encode(encoding) if encoding else field_value
        bytes_value += b"\0" * (length - len(bytes_value))  # pad out to `length`
        writer.pack(f"{byte_order.value}{length}s", bytes_value)
        return
    elif metadata.fmt is None and field_type in (bytes, str):
        # Null-terminated.
        if isinstance(metadata.encoding, BinaryCondition):
            if stored_encoding is None:
                raise BinaryFieldValueError(
                    f"`stored_encoding` required to pack null-terminated string field `{metadata.name}` with "
                    f"conditional encoding."
                )
            encoding = stored_encoding
        else:
            if stored_encoding is not None:
                enc_msg = "no encoding" if metadata.encoding is None else f"fixed encoding '{metadata.encoding}'"
                raise BinaryFieldValueError(
                    f"`stored_encoding` cannot be used to pack null-terminated string field `{metadata.name}` with "
                    f"{enc_msg}."
                )
            encoding = metadata.encoding
        if encoding is None:
            writer.append(field_value.rstrip(b"\0") + b"\0")
        else:
            bytes_per_char = 2 if encoding.replace("-", "").startswith("utf16le") else 1
            terminator = b"\0" * bytes_per_char
            writer.append(field_value.rstrip("\0").encode(encoding) + terminator)
        return

    if field_type in _PRIMITIVE_FIELD_INFO:
        # Primitive type.
        fmt, _, min_max = _PRIMITIVE_FIELD_INFO[field_type]
        fmt = _process_fmt_varint(fmt, varint_size)
        if min_max is not None and (field_value < min_max[0] or min_max[1] < field_value):
            raise BinaryFieldValueError(
                f"Value {field_value} of field `{metadata.name}` is out of range {min_max} for type `{field_type}`."
            )
        writer.pack(fmt, field_value)
        return

    if metadata.fmt is None:
        # Shouldn't be reachable, but don't want to fall through.
        raise BinaryFieldValueError(f"Field `{metadata.name}` must have `fmt` or `length`.")

    # Otherwise, get tuple from custom field type.
    fmt = _process_fmt_varint(metadata.fmt, varint_size)
    if metadata.pack_factory is not None:
        values = metadata.pack_factory(field_value)
    else:
        try:  # try to convert value to iterable
            values = tuple(field_value)
        except TypeError:  # try to use value as-is (e.g. `IntEnum`)
            values = [field_value]
    writer.pack(fmt, *values)


def _get_field_fmt(
    metadata: BinaryFieldMetadata | None,
    field_name: str,
    field_type: tp.Type | GenericAlias,
    varint_size: int | None,
) -> str:
    # TODO: simplify with new metadata class

    if isinstance(field_type, GenericAlias):
        fmt = ""
        for i, element_type in enumerate(field_type.__args__):
            fmt += _get_field_fmt(metadata, f"{field_name}[{i}]", element_type, varint_size)
        return fmt

    if metadata is not None:
        if metadata.fmt is not None:
            return metadata.fmt
        if metadata.length is not None:
            return f"{metadata.length}s"
        elif field_type in (bytes, str):
            raise ValueError(f"Cannot get format of null-terminated binary field `{field_name}`.")

    if field_type in _PRIMITIVE_FIELD_INFO:
        fmt, _, _ = _PRIMITIVE_FIELD_INFO[field_type]
        return _process_fmt_varint(fmt, varint_size)

    raise ValueError(f"Cannot get format of unhandled binary field `{field_name}`.")


# Alias that can be used to clearly indicate when a field is being reserved.
RESERVED = None  # type: tp.Any


# TODO: rename to `BinaryField` after deprecated `BinaryField` is removed/renamed.
def Binary(
    fmt: str | tp.Type[PRIMITIVE_FIELD_TYPING] | list[tp.Type[PRIMITIVE_FIELD_TYPING]] | None = None,
    type_factory: tp.Callable[[tuple], FIELD_T] | None = None,
    pack_factory: tp.Callable[[FIELD_T], tuple] | None = None,
    asserted: tp.Any = None,
    offset: int | str | FieldValue[int] | None = None,
    alignment: int | BinaryCondition[int] = 1,
    length: int | str | FieldValue[int] | None = None,
    encoding: str | BinaryCondition[str] | None = None,
    rstrip_null: bool = False,
    bit_count: int = -1,
    deferred: bool = False,
    skip_callback: tp.Callable[[int, dict[str, tp.Any]], bool] | None = None,
    type_override: tp.Type[PRIMITIVE_FIELD_TYPING] | None = None,
    **field_kwargs,
):
    asserted = _process_asserted_value(asserted)

    if fmt is str or fmt is bytes:
        fmt = None  # redundant
    if fmt in _PRIMITIVE_FIELD_INFO:
        fmt = [fmt]  # fall through to next line
    if isinstance(fmt, (list, tuple)):
        try:
            fmt = "".join(_PRIMITIVE_FIELD_INFO[numeric_type][0] for numeric_type in fmt)
        except KeyError:
            raise KeyError(f"Invalid sequence of primitive types given to `binary()`: {fmt}")
    elif isinstance(fmt, str):
        fmt = fmt
    elif fmt is not None:  # can be safely omitted alongside primitive field type hints
        raise TypeError(f"Invalid `binary(fmt)`: {fmt}")

    metadata = BinaryFieldMetadata(
        type_override,
        fmt,
        type_factory,
        pack_factory,
        asserted,
        offset,
        alignment,
        length,
        encoding,
        rstrip_null,
        bit_count,
        deferred,
        skip_callback,
    )

    return {"metadata": {"binary": metadata}, **field_kwargs}


def _process_asserted_value(asserted_value) -> None | list:
    """Put standalone asserted values into a list for consistency."""
    if asserted_value is None:
        return []
    if isinstance(asserted_value, tuple):
        return list(asserted_value)
    elif not isinstance(asserted_value, list):
        return [asserted_value]
    return asserted_value


def BinaryAutoOffset(
    field_name: str,
    offset_shift: int = 0,
    offset: int | FieldValue[int] | None = None,
    alignment: int | BinaryCondition[int] = 1,
    skip_callback: tp.Callable[[int, dict[str, tp.Any]], bool] | None = None,
    **field_kwargs,
) -> MappingProxyType[str, tp.Any]:
    """Will compute field value from offset of `field_name`, optionally passed through `offset_func` first."""
    return MappingProxyType({
        "metadata": {
            "binary": BinaryFieldMetadata(offset=offset, alignment=alignment, skip_callback=skip_callback),
            "auto_offset": (field_name, offset_shift),
        },
        **field_kwargs,
    })


def BinaryAutoCompute(
    compute_func: tp.Callable[[NewBinaryStruct], tp.Any] | str,
    asserted: tp.Any = None,
    offset: int | FieldValue[int] | None = None,
    alignment: int | BinaryCondition[int] = 1,
    skip_callback: tp.Callable[[int, dict[str, tp.Any]], bool] | None = None,
    **field_kwargs,
) -> MappingProxyType[str, tp.Any]:
    """Will compute field value from a function that takes the `BinaryStruct` instance (usually some bound instance
    method that uses other fields).

    When unpacking, callback will be run after other fields have been unpacked, and their results asserted against the
    actual unpacked values for this field.

    NOTE: On pack, callbacks are computed in REVERSE field order (because early offsets often depend on the lengths of
    other later fields, etc.).
    """
    asserted = _process_asserted_value(asserted)
    return MappingProxyType({
        "metadata": {
            "binary": BinaryFieldMetadata(
                asserted=asserted, offset=offset, alignment=alignment, skip_callback=skip_callback
            ),
            "auto_compute": compute_func,
        },
        **field_kwargs,
    })


def BinaryPad(
    length: int,
    char=b"\0",
    offset: int | FieldValue[int] | None = None,
    alignment: int | BinaryCondition[int] = 1,
    bit_count: int = -1,
    skip_callback: tp.Callable[[int, dict[str, tp.Any]], bool] | None = None,
) -> MappingProxyType[str, tp.Any]:
    """Will assert `length` bytes of character `char`.

    Also automatically sets `init=False`, and `repr=False`. `default` does not need to be set as the asserted value will
    be packed every time anyway.
    """
    if not isinstance(char, bytes):
        raise TypeError("Padding `char` must be `bytes`.")
    pad = char * length
    return MappingProxyType({
        "metadata": {
            "binary": BinaryFieldMetadata(
                offset=offset,
                alignment=alignment,
                length=length,
                asserted=[pad],
                bit_count=bit_count,
                skip_callback=skip_callback,
            ),
        },
        # "init": False,  # TODO: will frazzle type checker when instance is directly created
        "repr": False,
    })


# TODO: lp_strings (though seemingly not used in any From formats).


OBJ_T = tp.TypeVar("OBJ_T")


def slots_equality(obj1: OBJ_T, obj2: OBJ_T) -> bool:
    """NOTE: Not needed for dataclasses with `eq=True` (default)."""
    if obj1.__slots__ != obj2.__slots__:
        raise TypeError("Cannot compare equality of slots on objects with different slot names.")
    obj1_slots = [getattr(obj1, name) for name in obj1.__slots__]
    obj2_slots = [getattr(obj2, name) for name in obj2.__slots__]
    return obj1_slots == obj2_slots


@dataclasses.dataclass(slots=True)
class NewBinaryStruct:
    """Dataclass that supports automatic reading/writing from packed binary data."""

    _VALIDATED: tp.ClassVar[bool] = False
    _FIELDS: tp.ClassVar[tuple[dataclasses.Field] | None] = None
    _FIELD_TYPES: tp.ClassVar[tuple[tp.Any] | None] = ()

    # Set by `from_bytes()` class method, or can be manually set.
    # Will be auto-detected from values with `get_byte_order()` (defaulting to `LittleEndian`) if not defined, e.g.
    # by a manually-constructed instance.
    byte_order: None | ByteOrder = dataclasses.field(init=False, default=None)
    varint_size: None | int = dataclasses.field(init=False, default=None)
    # Remembers variable encodings for string fields with `encoding=BinaryCondition()`. Not used for fixed encodings.
    stored_encodings: dict[str, str] = dataclasses.field(init=False, repr=False, default_factory=dict)

    # Maps deferred field names to the names of unpacked `auto_offset` fields, and their optional `offset_shift` values,
    # waiting to be consumed (i.e. used and set to None). If multiple `auto_offset` fields are given in the dictionary
    # value, all must have the same offset.
    deferred_unpacking_offset_fields: dict[str, list[tuple[str, int]]] = dataclasses.field(
        init=False, repr=False, default_factory=dict
    )

    # Maps deferred field names to the names of `auto_offset` fields, and their optional `offset_shift` values,
    # waiting for them to be packed manually so the offset fields can be set.
    deferred_packing_offset_fields: dict[str, list[tuple[str, int]]] = dataclasses.field(
        init=False, repr=False, default_factory=dict
    )

    @classmethod
    def _validate_struct(cls):
        cls_name = cls.__name__
        deferred_found = False
        cls._FIELDS = cls.get_binary_fields()
        all_type_hints = tp.get_type_hints(cls)
        field_types = []
        for field in cls._FIELDS:
            if "binary" in field.metadata and field.metadata["binary"].type is not None:
                field_types.append(field.metadata["binary"].type)
            else:
                field_types.append(all_type_hints[field.name])
        cls._FIELD_TYPES = tuple(field_types)

        # Replace `__repr__` so subclasses don't have to specify `repr=False` every time.
        cls.__repr__ = NewBinaryStruct.__repr__

        if not cls._FIELDS:
            raise TypeError(f"`BinaryStruct` subclass `{cls_name}` has no fields.")

        for field, field_type in zip(cls._FIELDS, cls._FIELD_TYPES):

            metadata = field.metadata.get("binary", None)  # type: BinaryFieldMetadata | None

            # TODO: Also some `metadata` fields that aren't valid with these, I'm sure.
            if "auto_offset" in field.metadata:
                if "auto_compute" in field.metadata:
                    raise BinaryFieldTypeError(
                        field, cls_name, "Field cannot use both 'auto_compute' and 'auto_offset'."
                    )
                if field_type not in _OFFSET_FIELD_TYPES:
                    raise BinaryFieldTypeError(
                        field, cls_name, "Cannot use `auto_offset` with this non-integral field type."
                    )

            if metadata is not None:
                if metadata.deferred:
                    deferred_found = True
                elif deferred_found:
                    raise BinaryFieldTypeError(
                        field, cls_name, "Non-deferred fields cannot appear after any deferred fields."
                    )
                try:
                    metadata.validate(field, field_type, cls_name)
                except Exception as ex:
                    raise BinaryFieldTypeError(field, cls_name, f"Error occurred while trying to validate field: {ex}")
            else:
                _validate_binary_field_without_metadata(field, field_type, cls_name)

            if field.name.startswith("_"):
                # Underscore-prefix fields automatically have `repr=False`.
                # field.init = False  # TODO: will frazzle type checker when directly creating instances
                # field.repr = False
                pass
                # TODO: If field name starts with "__", could it represent something else?

        cls._VALIDATED = True

    @classmethod
    def from_bytes(
        cls,
        data: bytes | bytearray | BinaryReader | tp.BinaryIO,
        byte_order: ByteOrder | BinaryCondition[ByteOrder] | str = None,
        varint_size: int | BinaryCondition[int] = None,
    ) -> Self:
        """Create an instance of this class from binary `data`, by parsing its fields.

        Note that field defaults do not matter here, as ALL fields must be unpacked.
        """
        if not cls._VALIDATED:
            cls._validate_struct()

        if isinstance(data, (bytes, bytearray)):
            reader = BinaryReader(data)
        elif isinstance(data, (io.BufferedIOBase, BinaryReader)):
            reader = data  # assumes it is at the correct offset already
        else:
            raise TypeError("`data` must be `bytes`, `bytearray`, or opened `io.BufferedIOBase`.")

        if byte_order is None:
            if isinstance(data, BinaryReader):
                byte_order = data.default_byte_order
            else:  # default
                byte_order = ByteOrder.LittleEndian
        elif isinstance(byte_order, BinaryCondition):
            byte_order = byte_order(reader)
        elif isinstance(byte_order, str):
            byte_order = ByteOrder(byte_order)
        elif not isinstance(byte_order, ByteOrder):
            raise ValueError(f"Invalid `byte_order`: {byte_order}")

        if varint_size is None:
            if isinstance(data, BinaryReader):
                varint_size = data.varint_size
            else:  # default
                varint_size = 8
        elif isinstance(varint_size, BinaryCondition):
            varint_size = varint_size(reader)

        if varint_size not in {4, 8}:
            raise ValueError(f"Invalid `varint_size`: {varint_size}")

        cls_name = cls.__name__
        field_values = {}  # type: dict[str, tp.Any]  # maps field names to final values
        auto_compute_funcs = []  # type: list[tuple[str, tp.Callable[[NewBinaryStruct], tp.Any]]]  # only some fields
        auto_unpacking_offset_checks = {}  # type: dict[str, list[tuple[str, int, int]]]
        deferred_unpacking_offset_fields = {}  # type: dict[str, list[tuple[str, int]]]
        bit_reader = BitFieldReader()

        for field, field_type in zip(cls._FIELDS, cls._FIELD_TYPES):

            if field.metadata.get("NOT_BINARY", False):
                continue  # field excluded

            metadata = field.metadata.get("binary", None)  # type: BinaryFieldMetadata | None

            if (not metadata or metadata.bit_count == -1) and not bit_reader.empty:
                # Last bit field was not finished. Discard bits.
                bit_reader.clear()

            if metadata and metadata.skip_callback is not None:
                if metadata.skip_callback(varint_size, field_values):
                    field_values[field.name] = None
                    continue

            if metadata and metadata.deferred:
                field_values[field.name] = None
                continue

            if field.name in auto_unpacking_offset_checks:
                # Validate target field's offset (here) against offset read from earlier field.
                offset_field_name, offset_shift = auto_unpacking_offset_checks.pop(field.name)

                expected_offset_field_value = reader.tell() + offset_shift
                if expected_offset_field_value != field_values[offset_field_name]:
                    raise ValueError(
                        f"Field `{cls_name}.{offset_field_name}` was expected to have offset of field "
                        f"`{cls_name}.{field.name}` ({expected_offset_field_value}) but instead has value "
                        f"{field_values[offset_field_name]}."
                    )

            if metadata and metadata.bit_count != -1:
                # Read bit field and cast to field type (e.g. `bool` for 1-bit fields).
                try:
                    field_value = field_type(bit_reader.read(reader, metadata.bit_count, metadata.fmt))
                except Exception as ex:
                    _LOGGER.error(f"Error occurred while trying to unpack bit field `{cls_name}.{field.name}`: {ex}")
                    raise
                if metadata.asserted and field_value not in metadata.asserted:
                    raise BinaryFieldValueError(
                        f"Bit field `{cls_name}.{field.name}` (bit count {metadata.bit_count}) value "
                        f"{repr(field_value)} is not an asserted value: {metadata.asserted}"
                    )
            else:
                # Read normal field.
                try:
                    # print(f"Unpacking field {cls_name}.{field.name} at {reader.position}")
                    field_value = _unpack_binary_field(
                        metadata,
                        reader,
                        field_type,
                        byte_order,
                        varint_size,
                        field_values,  # for `FieldValue` arguments to inspect
                    )
                except Exception as ex:
                    _LOGGER.error(
                        f"Error occurred while trying to unpack field `{cls_name}.{field.name}`: {ex}\n"
                        f"Unpacked field values: {field_values}"
                    )
                    raise

            field_values[field.name] = field_value

            if "auto_compute" in field.metadata:
                if "auto_offset" in field.metadata:
                    raise ValueError(
                        f"Field `{cls_name}.{field.name}` has both `auto_compute` and `auto_offset` metadata."
                    )
                auto_compute_funcs.append((field.name, field.metadata["auto_compute"]))
            elif "auto_offset" in field.metadata:
                target_field_name, offset_func = field.metadata["auto_offset"]
                target_field, _ = cls.get_binary_field_and_type(target_field_name)
                target_field_metadata = target_field.metadata.get("binary", None)  # type: BinaryFieldMetadata | None
                if target_field_metadata and target_field_metadata.deferred:
                    # Offset should be used later in `unpack_deferred_field()`.
                    offset_dict = deferred_unpacking_offset_fields
                else:
                    # Will assert that offset is correct for specified field name. Should always be true if the targeted
                    # field also has `offset=BinaryCondition("offset_field")`.
                    offset_dict = auto_unpacking_offset_checks
                offset_dict.setdefault(target_field_name, []).append((field.name, offset_func))

        # Process callbacks and min/max values.
        init_values = {}
        non_init_values = {}
        for field, field_value in zip(cls._FIELDS, field_values.values()):
            if not field.init:  # assigned directly after initialization
                non_init_values[field.name] = field_value
            else:
                init_values[field.name] = field_value

        # noinspection PyArgumentList
        instance = cls(**init_values)
        instance.byte_order = byte_order
        instance.varint_size = varint_size
        instance.deferred_unpacking_offset_fields = deferred_unpacking_offset_fields
        for field_name, value in non_init_values.items():
            setattr(instance, field_name, value)

        # Assert computed callbacks.
        for field_name, auto_compute_func in auto_compute_funcs:
            # TODO: Not doing this, because it's annoying for fields computed from non-binary fields (which is common)
            #  as those fields have not been built from the binary data yet.
            # computed_value = auto_compute_func(instance)
            # value = getattr(instance, field_name)
            # if computed_value != value:
            #     raise ValueError(
            #         f"Value unpacked in auto-computed field `{cls.__name__}.{field_name}` ({value}) does not match "
            #         f"computed value: {computed_value}"
            #     )
            # Now that computed value has been confirmed, we set the actual field value to `None`, as it will be
            # computed properly on pack.
            setattr(instance, field_name, None)

        return instance

    @classmethod
    def from_object(
        cls,
        obj: OBJ_T,
        byte_order: ByteOrder = None,
        varint_size: int = None,
        **field_values,
    ):
        """Create an instance by reading getting field values directly from the attributes of `obj`, with additional
        fields NOT on the object given in `**fields`. Will raise an error if the `init` signature does not match. Fields
        with `init=False` are ignored (all such fields should be asserted or auto-computed).

        Absent fields will be initialized with `None`, which will lead them to being reserved in `to_writer()`.

        Also has the advantage of bypassing type checker for the `int` size subtypes like `byte`, `short`, etc.
        """
        if not cls._VALIDATED:
            cls._validate_struct()

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
        binary_struct.varint_size = varint_size
        return binary_struct

    @classmethod
    def object_to_writer(
        cls,
        obj: OBJ_T,
        writer: BinaryWriter | None = None,
        byte_order: ByteOrder = None,
        varint_size: int = None,
        **field_values,
    ) -> BinaryWriter:
        """Convenience shortcut for creating a struct instance from `obj` and `field_values`, then immediately calling
        `to_writer(writer, reserve_obj=obj)` with that struct.
        """
        binary_struct = cls.from_object(obj, byte_order=byte_order, varint_size=varint_size, **field_values)
        return binary_struct.to_writer(writer, reserve_obj=obj)

    def to_object(self, obj_type: tp.Type[OBJ_T], **init_kwargs) -> OBJ_T:
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
                raise ValueError(f"Field `{self.__class__.__name__}.{field.name}` is None. Cannot set to object.")
            init_kwargs[field.name] = value

        return obj_type(**init_kwargs)

    @classmethod
    def reader_to_object(cls, reader: BinaryReader, obj_type: tp.Type[OBJ_T], **init_kwargs) -> OBJ_T:
        """Convenience method for creating a struct instance with `from_bytes(reader)`, then immediately calling
        `to_object(obj_type, **init_kwargs)` with that struct.
        """
        struct_instance = cls.from_bytes(reader)
        obj = struct_instance.to_object(obj_type, **init_kwargs)
        return obj

    def __bytes__(self) -> bytes:
        writer = self.to_writer()
        if writer.reserved:
            raise ValueError(
                f"`{self.__class__.__name__}` BinaryStruct cannot fill all fields on its own. Use `to_writer()`.\n"
                f"    Remaining: {writer.reserved}"
            )
        return bytes(writer)

    def to_writer(self, writer: BinaryWriter = None, reserve_obj: OBJ_T = None) -> BinaryWriter:
        """Use fields to pack this instance into a `BinaryWriter`, which may be given or started automatically.

        Any non-auto-computed fields whose values are `None` will be left as reserved keys in the writer of format:
            '{reserve_prefix}.{field_name}'
        and must be filled with `writer.fill()` by the caller before the writer can be converted to bytes. If
        `reserve_prefix = None` (default), it will default to the name of this class. The main use of setting it
        manually is for nested structs and lists of structs, which will keep chaining their names together and include
        list/tuple indices where relevant (handled automatically.
        """
        if not self._VALIDATED:
            self._validate_struct()

        if reserve_obj is None:
            reserve_obj = self

        if self.byte_order is None:
            byte_order = self.get_default_byte_order() if writer is None else writer.default_byte_order
        else:
            byte_order = self.byte_order

        # `self.varint_size` may be left as None (e.g. for formats that do not care about it) but an error will be
        # raised if any `varint` or `varuint` fields are encountered.

        if writer is not None:
            if writer.default_byte_order != byte_order:
                _LOGGER.warning(
                    f"Existing writer passed to `{self.__class__.__name__}.to_writer()` has default byte order "
                    f"{writer.default_byte_order}, but this class wants to use {byte_order}. Using this class's byte "
                    f"order.")
                writer.default_byte_order = byte_order
        else:
            writer = BinaryWriter(byte_order)  # NOTE: `BinaryWriter.varint_size` not used here

        auto_packing_offset_fields = {}  # type: dict[str, list[tuple[str, int]]]
        bit_writer = BitFieldWriter()

        cls_name = self.__class__.__name__

        # Get all field values.
        field_values = {field.name: getattr(self, field.name, None) for field in self._FIELDS}
        # Auto-compute applicable fields in reverse order.
        for i in reversed(range(len(field_values))):
            field = self._FIELDS[i]
            auto_compute_func = field.metadata.get("auto_compute", None)
            if auto_compute_func is not None:
                if field_values[i] is not None:
                    raise ValueError(f"You cannot set a value to auto-computed field `{cls_name}.{field.name}`.")
                field_values[i] = auto_compute_func(self)

        for field, field_type, field_value in zip(self._FIELDS, self._FIELD_TYPES, field_values.values()):

            if field.metadata.get("NOT_BINARY", False):
                continue  # field excluded

            metadata = field.metadata.get("binary", None)  # type: BinaryFieldMetadata

            if metadata and metadata.skip_callback is not None:
                if metadata.skip_callback(self.varint_size, field_values):
                    # Write nothing for this field.
                    continue

            if not bit_writer.empty and (not metadata or metadata.bit_count == -1):
                # Pad out bit writer.
                bit_writer.finish_field(writer)

            if metadata and metadata.bit_count != -1:
                # NOTE: No `auto_offset` or `auto_compute` is compatible with bit fields.
                metadata.check_asserted(field_value)  # usually zero, if asserted
                bit_writer.write(writer, field_value, metadata.bit_count, metadata.fmt)
                continue

            if "auto_offset" in field.metadata:
                if field_value is not None:
                    raise BinaryFieldValueError(
                        f"Cannot set value of field `{cls_name}.{field.name}` with `auto_offset`."
                    )
                fmt, _, _ = _PRIMITIVE_FIELD_INFO[field_type]  # no need to check `min_max`
                fmt = _process_fmt_varint(fmt, self.varint_size)
                target_field_name, offset_shift = field.metadata["auto_offset"]
                target_field, _ = self.get_binary_field_and_type(target_field_name)
                target_metadata = target_field.metadata.get("binary", None)  # type: BinaryFieldMetadata | None
                if target_metadata and target_metadata.deferred:
                    offset_dict = self.deferred_packing_offset_fields
                else:
                    offset_dict = auto_packing_offset_fields
                offset_dict.setdefault(target_field_name, []).append((field.name, offset_shift))
                writer.reserve(field.name, byte_order.value + fmt, obj=reserve_obj)
                continue

            if field.name in auto_packing_offset_fields:
                # Fill this offset back to any offset fields waiting for it.
                offset = writer.position
                for offset_field_name, offset_shift in auto_packing_offset_fields.pop(field.name):
                    writer.fill(offset_field_name, offset + offset_shift, obj=reserve_obj)

            # Needed to inspect `asserted` here to get a default field value for packing function call.
            single_asserted = metadata is not None and metadata.asserted and len(metadata.asserted) == 1

            if metadata and metadata.deferred:
                # We are done packing fields (all remaining fields must be deferred).
                # Deferred fields will be packed later, and any reserved offsets filled.
                break

            if field_value is None and not single_asserted:
                # Reserved for custom external filling, as it requires data beyond this struct's scope (even just to
                # choose one of multiple provided asserted values). Must be a field with fixed size (already validated).

                if isinstance(field_type, GenericAlias):
                    # List or tuple.
                    try:
                        fmt = _get_field_fmt(metadata, field.name, field_type, self.varint_size)
                    except ValueError as ex:
                        raise BinaryFieldValueError(
                            f"Could not detect format of field `{cls_name}.{field.name}` to reserve it. "
                            f"Error: {ex}"
                        )
                elif field_type is Vector2:
                    fmt = "2f"
                elif field_type is Vector3:
                    fmt = "3f"
                elif field_type is Vector4:
                    fmt = "4f"
                elif field_type in _PRIMITIVE_FIELD_INFO:
                    fmt, _, _ = _PRIMITIVE_FIELD_INFO[field_type]
                    fmt = _process_fmt_varint(fmt, self.varint_size)
                elif metadata is not None:
                    if metadata.length is not None:
                        length = metadata.resolve_condition(metadata.length, None, field_values)
                        fmt = f"{length}s"
                    elif metadata.fmt is not None:
                        fmt = metadata.fmt
                    else:
                        raise BinaryFieldValueError(
                            f"Cannot reserve binary field `{cls_name}.{field.name}` of type `{field_type.__name__}`."
                        )
                else:
                    raise BinaryFieldValueError(
                        f"Cannot reserve binary field `{cls_name}.{field.name}` of type `{field_type.__name__}`."
                    )

                writer.reserve(field.name, byte_order.value + fmt, obj=reserve_obj)
                continue

            if metadata and metadata.asserted:
                if field_value is not None:
                    # Check that field value is a valid asserted value.
                    if field_value not in metadata.asserted:
                        raise BinaryFieldValueError(
                            f"Field `{cls_name}.{field.name}` value {repr(field_value)} is not an asserted value: "
                            f"{metadata.asserted}"
                        )
                elif field_value is None:
                    if single_asserted:
                        # Use lone asserted value.
                        field_value = metadata.asserted[0]
                    else:
                        # Cannot guess which asserted value to use.
                        raise ValueError(
                            f"Field `{cls_name}.{field.name}` has no value but multiple possible asserted values: "
                            f"{metadata.asserted}. Cannot guess which one to pack; one of them must be set."
                        )

            try:
                _pack_binary_field(
                    metadata,
                    writer,
                    field_type,
                    field_value,
                    byte_order,
                    self.varint_size,
                    field_values,
                    self.stored_encodings.get(field.name, None),
                )
            except Exception as ex:
                _LOGGER.error(f"Error occurred while writing binary field `{field.name}`: {ex}")
                raise

        if auto_packing_offset_fields:
            raise ValueError(f"Reserved auto-offset fields were not filled: {auto_packing_offset_fields}")

        return writer  # may have remaining unfilled fields (any non-auto-computed field with value `None`)

    def fill(self, writer: BinaryWriter, field_name: str, *values: tp.Any):
        """Fill reserved `field_name` in `writer` as reserved with the ID of this instance."""
        writer.fill(field_name, *values, obj=self)

    def assert_field_values(self, **field_values):
        for field_name, field_value in field_values.items():
            try:
                value = getattr(self, field_name)
            except AttributeError:
                raise AssertionError(f"Field '{field_name}' does not exist on `{self.__class__.__name__}`.")
            if value != field_value:
                raise AssertionError(f"Field value assertion error: {repr(value)} != asserted {repr(field_value)}")

    def unpack_deferred_field(
        self,
        stream: tp.BinaryIO | BinaryReader,
        deferred_field_name: str,
        **overrides,
    ):
        """Use current `stream offset, or a deferred unpacking offset if it exists, to unpack and set the value of
        field `deferred_field_name` excluded from initial unpack. The deferred field's value must currently be `None`.

        Any consumed offset field will be set to `None` afterward in preparation for its value to be automatically
        reserved and/or determined later from the same target field when packed.
        """
        deferred_field, deferred_field_type = self.get_binary_field_and_type(deferred_field_name)
        metadata = deferred_field.metadata.get("binary", None)  # type: BinaryFieldMetadata | None
        if metadata is None or not deferred_field.metadata["binary"].deferred:
            raise ValueError(f"Cannot manually pack to non-deferred field `{deferred_field_name}`.")
        existing_value = getattr(self, deferred_field_name, None)
        if existing_value is not None:
            raise BinaryFieldValueError(
                f"Deferred field `{self.__class__.__name__}.{deferred_field_name}` already has value {existing_value}."
            )

        if deferred_field_name in self.deferred_unpacking_offset_fields:
            offset = None  # type: int | None
            for offset_field_name, offset_shift in self.deferred_unpacking_offset_fields.pop(deferred_field_name):
                offset_field_value = getattr(self, offset_field_name)
                if offset is None:
                    offset = offset_field_value - offset_shift
                    stream.seek(offset)
                elif offset_field_value - offset_shift != offset:
                    raise BinaryFieldValueError(
                        f"Conflicting auto-offsets to deferred field `{self.__class__.__name__}.{deferred_field_name}`."
                    )
                setattr(self, offset_field_name, None)
            # Otherwise, use current `stream` position.

        deferred_field_value = _unpack_binary_field(
            metadata,
            stream,
            deferred_field_type,
            self.byte_order,
            self.varint_size,
            field_values=self.get_binary_field_values(),
            **overrides,
        )
        setattr(self, deferred_field_name, deferred_field_value)

    def pack_deferred_field(self, writer: BinaryWriter, field_name: str, temp_field_value: tp.Any = None, **overrides):
        """Pack a deferred field manually at current `writer` position. Cannot be used on non-deferred fields.

        If any offset fields are waiting for this deferred field to be packed, their values will be filled too.
        (Obviously, this must be the same `writer` and same struct instance for this to work.)

        `overrides` kwargs support 'encoding' only.
        """
        deferred_field, deferred_field_type = self.get_binary_field_and_type(field_name)
        field_value = temp_field_value if temp_field_value is not None else getattr(self, field_name, None)
        if field_value is None:
            raise ValueError(
                f"Cannot pack deferred field `{self.__class__.__name__}.{field_name}` when its value is None."
            )
        metadata = deferred_field.metadata.get("binary", None)  # type: BinaryFieldMetadata | None
        if metadata is None or not deferred_field.metadata["binary"].deferred:
            raise ValueError(f"Cannot manually pack non-deferred field: `{self.__class__.__name__}.{field_name}`")

        if field_name in self.deferred_packing_offset_fields:
            offset = writer.position
            for offset_field_name, offset_shift in self.deferred_packing_offset_fields.pop(field_name):
                self.fill(writer, offset_field_name, offset + offset_shift)

        _pack_binary_field(
            metadata,
            writer,
            deferred_field_type,
            field_value,
            self.byte_order,
            self.varint_size,
            self.get_binary_field_values(),
            stored_encoding=None,
            **overrides,
        )

        if temp_field_value is not None:
            # Clear deferred field value.
            setattr(self, field_name, None)

    def to_dict(self, ignore_underscore_prefix=True) -> dict[str, tp.Any]:
        """Get all current binary fields, but ignore fields with value `None` and (by default) underscore names."""
        return {
            name: value
            for name, value in self.get_binary_field_values().items()
            if value is not None and (not ignore_underscore_prefix or not name.startswith("_"))
        }

    def pop(self, field_name: str) -> tp.Any:
        """Simply sets `field_name` to None, marking it as 'consumed', without triggering type checkers.

        This has the same general usage pattern as `unpack_deferred_field()` but supports external field processing of
        arbitrary complexity. The main outcome is to ensure that `field_name` is externally reserved when packing.
        """
        value = getattr(self, field_name, None)
        if value is None:
            raise BinaryFieldValueError(f"Field `{self.__class__.__name__}.{field_name}` has no set value to consume.")
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
        _LOGGER.warning(f"Byte order defaulting to `LittleEndian` for `{self.__class__.__name__}`.")
        return ByteOrder.LittleEndian

    def __repr__(self) -> str:
        """Only includes binary fields with non-default values."""
        lines = [
            f"{self.__class__.__name__}(",
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
        """Get all current binary field values."""
        field_values = {}
        for field in self._FIELDS:
            field_values[field.name] = getattr(self, field.name, None)
        return field_values

    @classmethod
    def get_binary_fields(cls) -> tuple[dataclasses.Field, ...]:
        return tuple(
            field for field in dataclasses.fields(cls)
            if field.name not in {
                "byte_order",
                "varint_size",
                "stored_encodings",
                "deferred_unpacking_offset_fields",
                "deferred_packing_offset_fields",
            }
            and not field.metadata.get("NOT_BINARY", False)
        )

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
    def get_full_fmt(cls, byte_order: ByteOrder, varint_size: int) -> str:
        """Combines all field formats.

        Cannot be called if the field includes null-terminated strings (which have undefined size).
        """
        if not cls._VALIDATED:
            cls._validate_struct()
        fmt = f"{byte_order.value}"
        for field, field_type in zip(cls._FIELDS, cls._FIELD_TYPES):
            metadata = field.metadata.get("binary", None)
            fmt += _get_field_fmt(metadata, f"{cls.__name__}.{field.name}", field_type, varint_size)
        return fmt

    def get_size(self) -> int:
        """Get full format of this struct, then calculate its size using its set `byte_order` and `varint_size`."""
        return struct.calcsize(self.get_full_fmt(self.byte_order, self.varint_size))

    @classmethod
    def get_cls_size(cls, byte_order: ByteOrder = ByteOrder.LittleEndian, varint_size: int = None) -> int:
        """Get full format of this struct, then calculate its size using the given `byte_order` and `varint_size`.

        `byte_order` will default to `LittleEndian`; only a change to `NativeAutoAligned` would potentially change the
        size of the struct, which is unlikely for game formats. `varint_size` may be omitted, but an error will be
        raised if any `varint` or `varuint` fields are used in the struct.
        """
        return struct.calcsize(cls.get_full_fmt(byte_order, varint_size))

    @staticmethod
    def join_bytes(struct_iterable: tp.Iterable[NewBinaryStruct]) -> bytes:
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
            integer = reader.unpack_value(fmt)
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


def test_bit_field():

    @dataclasses.dataclass(slots=True)
    class TestStruct(NewBinaryStruct):
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
