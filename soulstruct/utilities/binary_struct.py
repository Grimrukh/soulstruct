__all__ = ["BinaryStruct", "BinaryObject"]

import abc
import enum
import inspect
import io
import logging
import re
import struct
import types
import typing as tp

from soulstruct.utilities import read_chars_from_bytes, AttributeDict, Flags8
from soulstruct.utilities.maths import Vector, Vector3

_LOGGER = logging.getLogger(__name__)


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
            elif isinstance(value, (list, tuple, Vector3)):
                return [self.parse_for_pack(v) for v in value]  # recur on each element
            else:
                return value

        def __repr__(self):
            return f"{self.name} :: {self.fmt}" + (f" (== {self.asserted})" if self.asserted is not None else "")

    PAD_RE = re.compile(r"(\d*)x")
    FMT_RE = re.compile(r"([<>@])?(\d*)([\w?])")

    def __init__(self, *fields, byte_order="<"):
        """Flexible binary unpacker/repacker."""
        self.fields = []  # type: list[BinaryStruct.BinaryField]
        self._struct_format = []  # Format chunks with different byte order are stored in sub-format strings.
        self._struct_length = []  # Number of values to be packed using each sub-format string.
        self.size = 0  # Total number of bytes in struct.
        if fields:
            self.add_fields(*fields, byte_order=byte_order)

    def add_fields(self, *fields, byte_order=None) -> tuple[list[BinaryField], str]:
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
                if self.PAD_RE.match(field_spec):
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
                    "Each field should be a single pad `'#x'` format string, a `(name, fmt)` pair, or a "
                    "`(name, fmt, asserted)` triplet."
                )

            if name == "x":
                raise ValueError("Field name 'x' is reserved for internal labeling of pad fields.")
            elif name in self.field_names:
                raise ValueError(f"Field name {repr(name)} already exists in `BinaryStruct`.")

            try:
                field_byte_order, field_length, field_type = self.FMT_RE.match(fmt).groups()
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
    ) -> AttributeDict:
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
            output = AttributeDict()
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

        output = AttributeDict()
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
            size = struct.calcsize(sub_fmt)
            try:
                unpacked += struct.unpack(sub_fmt, data[data_offset : data_offset + size])
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
        self, source, count: int, exclude_asserted=False, exclude_prefix="", offset: int = None
    ) -> list[AttributeDict]:
        """Unpack `count` identical structs from `source`. See `unpack()` for more.

        Args:
            source: bytes or open buffer to unpack from.
            count: number of contiguous structs to unpack from source.
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
            self.unpack(source, exclude_asserted=exclude_asserted, exclude_prefix=exclude_prefix)
            for _ in range(count)
        ]
        if old_offset is not None:
            source.seek(old_offset)
        return structs

    def pack(self, struct_dict: dict = None, /, **struct_kwargs) -> bytes:
        if not self.fields and struct_dict is None and not struct_kwargs:
            return b""  # null struct (error will be raised below if any input is given)
        if struct_dict is not None and struct_kwargs:
            raise ValueError("You cannot use both the `struct_dict` argument and the unpacked `**struct_kwargs`.")
        if isinstance(struct_dict, dict):
            struct_dict = struct_dict.copy()  # don't modify input dictionary
        elif struct_dict is None:
            struct_dict = struct_kwargs
        else:
            raise TypeError(f"`struct_dict` must be a dictionary, not `{type(struct_dict)}`.")

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
                output += struct.pack(sub_fmt, *to_pack[pack_index : pack_index + sub_fmt_length])
            except struct.error:
                _LOGGER.error(
                    f"Failed to pack data at offset {pack_index} with sub-format {sub_fmt} and length "
                    f"{sub_fmt_length}:\n{to_pack[pack_index:pack_index + sub_fmt_length]}"
                )
                raise
        return output

    def pack_multiple(self, struct_dicts: tp.Sequence[dict]) -> bytes:
        """Pack multiple instances of this binary struct and return them joined."""
        output = b""
        for struct_dict in struct_dicts:
            output += self.pack(struct_dict)
        return output

    def pack_from_object(self, obj, **kwargs) -> bytes:
        """Attempts to build complete struct dictionary from attributes of given object `obj`. If any `kwargs` are
        given, they will take precedence over the `obj` attributes.

        All non-constant fields must be present as attributes or `kwargs`, or an exception will be raised.
        """
        struct_dict = {}
        for field in self.non_padding_fields:
            if field.length == 0:
                continue  # padding
            if field.name in kwargs:
                struct_dict[field.name] = kwargs[field.name]
            else:
                try:
                    struct_dict[field.name] = getattr(obj, field.name)
                except AttributeError:
                    if not field.asserted:
                        raise AttributeError(
                            f"Non-asserted field {repr(field)} is not an attribute of given object {obj} and was not "
                            f"passed as a keyword argument. Cannot pack."
                        )
        try:
            return self.pack(struct_dict)
        except struct.error:
            _LOGGER.error(f"Failed to pack `BinaryStruct` from object. Dictionary:\n{struct_dict}")
            raise

    def copy(self):
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
    """

    STRUCT: BinaryStruct
    DEFAULTS: dict[str, tp.Any] = {}

    def __init__(self, source: tp.Optional[io.BufferedIOBase] = None, unpack_kwargs=None, **kwargs):
        """Instance `source` can be `None` or a bytes buffer. In either case, `kwargs` are applied afterwards, and must
        all be valid `STRUCT` field names that do not start with an underscore. They can be asserted fields, but the
        values must then match the asserted value.

        `unpack_kwargs` dictionary can also be passed, which will be unpacked as `**kwargs` for `unpack()`.

        Subclass should define its own fields (with default values) for type checking before calling `super().__init__`,
        or simply specify type hints in the class and use `DEFAULTS` to set default values.
        """
        if source is not None:
            if unpack_kwargs is None:
                unpack_kwargs = {}
            self.unpack(source, **unpack_kwargs)
        else:
            if unpack_kwargs is not None:
                raise ValueError("`unpack_kwargs` must be left as `None` if `source` is not a binary buffer.")
            for field in self.STRUCT.fields:
                if field.length > 0 and not field.name.startswith("_") and field.name not in kwargs:
                    # TODO: Mutable `DEFAULTS` members are an issue here.
                    setattr(self, field.name, self.DEFAULTS.get(field.name, self.get_field_default(field)))
            self.set(**kwargs)

    def set(self, **kwargs):
        """Set multiple fields (attributes) at once, via `__setattr__` below.

        Field names that start with "__" are ignored, which makes it easier to use an unpacked `BinaryStruct` dictionary
        as `kwargs`.
        """
        for field_name, value in kwargs.items():
            if field_name.startswith("__"):
                continue  # ignore
            setattr(self, field_name, value)

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
            if type(field_type) is types.GenericAlias:
                # TODO: Enforce other `typing` type hints?
                pass
            elif inspect.isclass(field_type):
                if issubclass(field_type, (enum.Enum, Vector, Flags8)):
                    value = field_type(value)
                elif field_type in (bytes, str, int, float, tuple, list, set):
                    value = field_type(value)

        super().__setattr__(field_name, value)

    def unpack(self, buffer: io.BufferedIOBase, **kwargs):
        self.set(**self.STRUCT.unpack(buffer, exclude_asserted=True))

    def pack(self, **kwargs) -> bytes:
        return self.STRUCT.pack_from_object(self)

    @classmethod
    def get_field_default(cls, field: BinaryStruct.BinaryField) -> tp.Union[str, bytes, bool, int, float]:
        if field.asserted:
            return field.asserted
        if field.name in (field_types := tp.get_type_hints(cls)):
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
        _, field_length, field_type = BinaryStruct.FMT_RE.match(field.fmt).groups()  # cannot fail
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

    # noinspection PyUnusedLocal
    @staticmethod
    def is_big_endian(buffer: io.BufferedIOBase) -> bool:
        """Examine given binary buffer to determine if it is big-endian. Always seeks back to initial position."""
        return False
