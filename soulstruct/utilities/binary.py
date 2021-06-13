"""NOTE: This file is Python 3.7 compatible for Blender 2.9X use."""

from __future__ import annotations

__all__ = ["BinaryStruct", "BinaryObject", "BinaryReader", "BinaryWriter", "read_chars_from_bytes"]

import abc
import enum
import inspect
import io
import logging
import re
import struct
import typing as tp
from contextlib import contextmanager
from pathlib import Path

from soulstruct.containers.entry import BinderEntry
from soulstruct.utilities.misc import Flags8
from soulstruct.utilities.maths import Vector

try:  # Python 3.9
    from types import GenericAlias
except ImportError:
    GenericAlias = None

_LOGGER = logging.getLogger(__name__)


PAD_RE = re.compile(r"(\d*)x")
FMT_RE = re.compile(r"([<>@])?(\d*)([\w?])")


class BinaryStruct:

    class BinaryField:
        """Stores information about a field passed to `BinaryStruct`."""

        def __init__(self, name: str, fmt: str, length: int, asserted=None, encoding=""):
            self.name = name
            self.fmt = fmt
            self.length = length
            self.asserted = asserted
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

    def __init__(self, *fields, byte_order="<"):
        """Flexible binary unpacker/repacker."""
        self.fields = []  # type: tp.List[BinaryStruct.BinaryField]
        self._struct_format = []  # type: tp.List[str]  # fmt chunks with different byte orders are stored here
        self._struct_length = []  # Number of values to be packed using each sub-format string.
        self.size = 0  # Total number of bytes in struct.
        if fields:
            self.add_fields(*fields, byte_order=byte_order)

    def add_fields(self, *fields, byte_order=None) -> tp.Tuple[tp.List[BinaryField], str]:
        """Add new fields to the BinaryStruct.

        Args:
             *fields: sequence of fields to add.
             byte_order: byte order for the added fields to use, which can be different from the byte order of other
                fields. By default, the most recent byte order is used.

        Returns:
            field_list, struct_format
        """
        if not fields:
            raise ValueError(f"No fields were passed to `add_fields()`.")
        if byte_order is None:
            if self._struct_format:
                byte_order = self._struct_format[-1][0]
                new_fmt = False
            else:
                byte_order = "<"  # default
                new_fmt = True
        elif not self._struct_format or byte_order != self._struct_format[-1][0]:
            if byte_order not in {"<", ">", "@"}:
                raise ValueError("byte_order must be '<', '>', or '@'.")
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
                    new_fields.append(self.BinaryField(name="x", fmt=field_spec, length=0))
                    sub_fmt += field_spec
                    continue
                else:
                    raise ValueError("Only pad strings, `'#x'`, are permitted outside field tuples.")

            asserted = None
            encoding = ""

            if isinstance(field_spec, (list, tuple)) and 2 <= len(field_spec) <= 3:
                if len(field_spec) == 3:
                    name, fmt, asserted = field_spec
                    if isinstance(asserted, tuple):
                        asserted = list(asserted)
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
                raise ValueError("Individual field format should not have its own byte order. Use `byte_order` arg.")
            if field_type == "j":
                fmt = f"{field_length}s"
                encoding = "shift_jis_2004"
                length = 1
            elif field_type == "u":
                fmt = f"{field_length}s"
                encoding = "utf-16-be" if byte_order == ">" else "utf-16-le"
                length = 1
            elif field_type == "s":
                length = 1
            else:
                length = int(field_length) if field_length else 1

            new_fields.append(self.BinaryField(name=name, fmt=fmt, length=length, asserted=asserted, encoding=encoding))
            sub_fmt += fmt
            sub_fmt_length += length

        self.fields += new_fields
        if new_fmt:
            self._struct_format.append(byte_order + sub_fmt)
            self._struct_length.append(sub_fmt_length)
        else:
            self._struct_format[-1] += sub_fmt
            self._struct_length[-1] += sub_fmt_length
        self.size = sum(struct.calcsize(sub_fmt) for sub_fmt in self._struct_format)

        return new_fields, byte_order + sub_fmt

    def unpack(
        self,
        source: tp.Union[bytes, io.BufferedIOBase],
        *fields,
        byte_order: str = None,
        exclude_asserted=False,
        exclude_prefix="",
        offset: int = None,
    ) -> tp.Dict[str, tp.Any]:
        """Unpack a single struct from source data.

        If any 'fields' are specified (same allowed formats as the constructor above), only those fields will be
        unpacked, and they will then be added to the BinaryStruct. This allows you to dynamically build the BinaryStruct
        on the fly if the structure itself depends on the values read (e.g. a big-endian flag). The same BinaryStruct
        can then be used for repacking later.

        Args:
            source: bytes or open buffer to unpack from.
            fields: optional list of new fields to simultaneously add and unpack (instead of full struct).
            byte_order (str): byte order ('<', '>', etc.) of the new fields, or new byte order to fully override all
                previous byte orders passed along with fields, if no new fields are given.
            exclude_asserted: exclude any asserted fields in the returned dictionary.
            exclude_prefix: exclude any fields whose names start with this prefix, if given.
            offset (int): optional offset to unpack from. Old offset (for buffers) will be restored if this is given.

        Returns:
            AttributeDict
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
                sub_fmt = f"{byte_order}{sub_fmt.lstrip('<>@')}"
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
        self, source, count: int, byte_order: str = None, exclude_asserted=False, exclude_prefix="", offset: int = None
    ) -> tp.List[tp.Dict[str, tp.Any]]:
        """Unpack `count` identical structs from `source`. See `unpack()` for more.

        Args:
            source: bytes or open buffer to unpack from.
            count: number of contiguous structs to unpack from source.
            byte_order (str): byte order to unpack with. Defaults to order specified by fields.
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

    def parse_object_source(self, source: object, **kwargs) -> tp.Dict[str, tp.Any]:
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
        self, source: tp.Union[dict, object] = None, **kwargs
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


class BinaryObject(abc.ABC):
    """Class whose fields are all specified in a `BinaryStruct` class attribute, `STRUCT`, with `set()` method.

    `DEFAULTS` can be used to specify defaults for specific field names. Otherwise, defaults will be based on the format
    of that field as type-hinted, or failing that, in `STRUCT` (0 for numeric types, False for booleans, etc.).

    Any field names that are type-hinted will also be initialized as that type whenever the attribute is set.

    This class is intended to be packed using a `BinaryWriter`, as can be seen with the `default_pack(writer)` method.
    """

    STRUCT: BinaryStruct = None
    DEFAULTS: tp.Dict[str, tp.Any] = {}

    Z_STRING_RE = re.compile(r"^__(\w[\w\d]+)__z$")

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

    def __setattr__(self, field_name, value):
        """Checks `field_name` is a valid field, confirms any asserted value, and casts value to a given type."""
        try:
            field_type = tp.get_type_hints(self.__class__)[field_name]
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
            if GenericAlias and type(field_type) is GenericAlias:
                # TODO: Enforce other `typing` type hints?
                pass
            elif inspect.isclass(field_type):
                if issubclass(field_type, (enum.Enum, Vector, Flags8)):
                    value = field_type(value)
                elif field_type in (bytes, str, int, float, tuple, list, set):
                    value = field_type(value)

        super().__setattr__(field_name, value)

    def default_unpack(self, reader: BinaryReader, encoding=None, byte_order=None):
        """`BinaryObject` unpack methods will frequently require extra arguments, so the exact signature of `unpack()
        is left to each subclass.

        Setting `unpack = BinaryObject.default_unpack` in the class definition is an easy option.

        `STRUCT` fields that match template `STRING_OFFSET_RE` will immediately be read as null-terminated strings from
        the unpacked offset, and set to the field name in the template.
        """
        data = reader.unpack_struct(self.STRUCT, exclude_asserted=True, byte_order=byte_order)
        kwargs = {}
        for field, value in data.items():
            match = self.Z_STRING_RE.match(field)
            if match:
                field_name = match.group(1)
                if encoding is None:
                    raise ValueError(
                        f"You must pass `encoding` to `default_unpack` to read {repr(field_name)} from string offset."
                    )
                kwargs[field_name] = reader.unpack_string(offset=data[field], encoding=encoding)
            else:
                kwargs[field] = data[field]
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

    def pack_zstring(self, writer: BinaryWriter, field: str, encoding=""):
        """Fill `"__{field}__z"` with current offset, then write `field` attribute with given `encoding`."""
        field_zstring = f"__{field}__z"
        if field_zstring not in self.STRUCT.field_names:
            raise ValueError(f"Invalid z-string field: {repr(field)}")
        writer.fill(field_zstring, writer.position, obj=self)
        z = b"\0\0" if encoding.startswith("utf-16") else b"\0"
        writer.append(getattr(self, field).encode(encoding) + z)

    @classmethod
    def get_field_default(cls, field: BinaryStruct.BinaryField) -> tp.Union[str, bytes, bool, int, float]:
        if field.asserted:
            return field.asserted
        field_types = tp.get_type_hints(cls)
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


class BinaryReader:
    """Manages an buffered binary IO stream, with methods for unpacking data and moving to temporary offsets."""

    def __init__(
        self,
        buffer: tp.Union[str, Path, bytes, bytearray, io.BufferedIOBase, BinderEntry, BinaryReader],
        byte_order="<",
    ):
        self.buffer = None

        if isinstance(buffer, str):
            buffer = Path(buffer)
        if isinstance(buffer, Path):
            self.buffer = buffer.open("rb")
        elif isinstance(buffer, (bytes, bytearray)):
            self.buffer = io.BytesIO(buffer)
        elif isinstance(buffer, io.BufferedIOBase):
            self.buffer = buffer
        elif isinstance(buffer, BinderEntry):
            self.buffer = io.BytesIO(buffer.get_uncompressed_data())
        elif isinstance(buffer, BinaryReader):
            self.buffer = buffer.buffer
        else:
            raise TypeError(
                f"Invalid `buffer`: {buffer}. Should be a binary IO stream, `bytes, or `Path` of a file to open."
            )
        self.byte_order = byte_order

    def unpack(self, fmt, offset=None, relative_offset=False, asserted=None):
        """Unpack appropriate number of bytes from `buffer` using `fmt` string from the given (or current) `offset`.

        Args:
            fmt (str): format string for `struct.unpack()`.
            offset (int): optional offset to seek to before reading. Old offset will be restored afterward.
            relative_offset (bool): indicates that `offset` is relative to current position.
            asserted: assert that the unpacked data is equal to this, if given.

        Returns:
            (tuple) Output of `struct.unpack()`.
        """
        if fmt[0] not in "<>@":
            fmt = self.byte_order + fmt
        initial_offset = self.position if offset is not None else None
        if offset is not None:
            self.seek(initial_offset + offset if relative_offset else offset)
        data = struct.unpack(fmt, self.buffer.read(struct.calcsize(fmt)))
        if asserted is not None and data != asserted:
            raise AssertionError(f"Unpacked data {repr(data)} does not equal asserted data {repr(asserted)}.")
        if initial_offset is not None:
            self.seek(initial_offset)
        return data

    def unpack_value(self, fmt, offset=None, relative_offset=False, asserted=None) -> tp.Union[bool, int, float, bytes]:
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

    def peek(self, fmt):
        """Unpack `fmt` and return the unpacked values without changing the offset."""
        return self.unpack(fmt, offset=self.position)

    def peek_value(self, fmt) -> tp.Union[bool, int, float]:
        """Unpack `fmt` and return the unpacked value without changing the offset."""
        return self.unpack_value(fmt, offset=self.position)

    def unpack_struct(
        self,
        binary_struct: BinaryStruct,
        *fields,
        byte_order: str = None,
        exclude_asserted=False,
        exclude_prefix="",
        offset: int = None,
    ) -> tp.Dict[str, tp.Any]:
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
        byte_order: str = None,
        exclude_asserted=False,
        exclude_prefix="",
        offset: int = None,
    ) -> tp.List[tp.Dict[str, tp.Any]]:
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
        return read_chars_from_buffer(self.buffer, offset, length, reset_old_offset, encoding=encoding, strip=strip)

    def read(self, size: int = None) -> bytes:
        return self.buffer.read(size)

    def seek(self, offset: int, whence=None):
        if whence is not None:
            self.buffer.seek(offset, whence)
        else:
            self.buffer.seek(offset)

    def tell(self):
        """Also has alias property `position` for this."""
        return self.buffer.tell()

    def assert_pad(self, size: int, char=b"\0"):
        """Read and assert `size` instances of `char` (defaults to null/zero byte)."""
        padding = self.buffer.read(size)
        if padding.strip(char):
            raise ValueError(f"Reader `pad({size})` found bytes other than {char}: {padding}")

    def align(self, alignment: int):
        """Align reader position to next multiple of `alignment`."""
        while self.buffer.tell() % alignment:
            self.buffer.read(1)

    def get_utf_16_encoding(self) -> str:
        return "utf-16-be" if self.byte_order == ">" else "utf-16-le"

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


class BinaryWriter:
    """Manages `bytearray` binary data, with features like reserved offsets for later writing and big endian mode."""

    class Reserved(str):
        """Indicates a reserved name that should be used, rather than a string to pack."""

        def __repr__(self):
            return "AUTO_RESERVE" if not self else super().__repr__()

    AUTO_RESERVE = Reserved()  # reserve using `id(source)` and field name

    big_endian: bool
    reserved: tp.Dict[str, tp.Tuple[int, str]]

    def __init__(self, big_endian=False):
        self.big_endian = big_endian
        self.reserved = {}
        self._array = bytearray()

    def parse_fmt(self, fmt: str) -> str:
        if fmt[0] not in "<>@":
            fmt = (">" if self.big_endian else "<") + fmt
        return fmt

    def pack(self, fmt: str, *values):
        self._array += struct.pack(self.parse_fmt(fmt), *values)

    def append(self, other: tp.Union[bytearray, bytes]):
        """Manually add existing binary data (e.g. a packed `BinaryStruct`) all at once."""
        self._array += other

    def pack_struct(
        self,
        binary_struct: BinaryStruct,
        source: tp.Union[dict, object] = None,
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
                raise ValueError(f"Field {repr(name)} auto-reserved by {type(obj)} {id(obj)} not found.")
        elif name not in self.reserved:
            raise ValueError(f"Name {repr(name)} is not reserved in `BytesWriter`.")
        offset, fmt = self.reserved[name]  # fmt endianness already specified
        try:
            packed = struct.pack(fmt, *values)
        except struct.error:
            raise ValueError(f"Error occurred when packing values to reserved offset with fmt {repr(fmt)}: {values}")
        self._array[offset:offset + len(packed)] = packed
        self.reserved.pop(name)  # pop after successful fill only

    def finish(self) -> bytes:
        """Just checks that no reserved offsets remain, then converts stored `bytearray` to immutable `bytes`."""
        if self.reserved:
            raise ValueError(f"Reserved `BytesWriter` offsets not filled: {list(self.reserved)}")
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


def read_chars_from_bytes(data, offset=0, length=None, encoding=None) -> tp.Union[bytes, str]:
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
) -> tp.Union[str, bytes]:
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
        else:
            chars.append(c)
            if len(chars) == length:
                if reset_old_offset and old_offset is not None:
                    buffer.seek(old_offset)
                stripped_array = b"".join(chars)  # used to strip spaces as well, but not anymore
                if strip:
                    stripped_array.rstrip()  # remove spaces
                    while stripped_array.endswith(b"\0\0" if bytes_per_char == 2 else b"\0"):
                        stripped_array = stripped_array[:-bytes_per_char]  # remove (pairs of) null characters
                if encoding is not None:
                    return stripped_array.decode(encoding)
                return stripped_array
