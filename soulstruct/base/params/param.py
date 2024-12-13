from __future__ import annotations

__all__ = ["Param", "TypedParam", "ParamDictRow", "ParamDict"]

import abc
import copy
import logging
import struct
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType

from constrata.streams.bits import BitFieldReader, BitFieldWriter

from soulstruct.base.game_file import GameFile
from soulstruct.dcx import DCXType
from soulstruct.utilities.binary import *
from soulstruct.utilities.text import pad_chars
from soulstruct.utilities.files import write_json

from .param_row import ParamRow
from .flags import ParamFlags1, ParamFlags2
from .paramdef import ParamDef, ParamDefField, ParamDefBND, field_types as ft

_LOGGER = logging.getLogger("soulstruct")


PARAM_ROW_DATA_T = tp.TypeVar("PARAM_ROW_DATA_T", bound=ParamRow)


@dataclass(slots=True)
class ParamDictRow:
    """A single entry in a `Param` table. Layout is defined by the `ParamDef` for this `Param` type.

    Supports all (known) games.

    NOTE: This class is basically deprecated, and is only used to read/write `Param` rows using actual `ParamDefs`
    rather than the Soulstruct `ParamRow` struct classes.
    """

    fields: dict[str, bool | int | float | str | bytes]
    paramdef: ParamDef  # required
    raw_name: bytes = b""
    name: str = ""  # may not be set if `raw_name` cannot be decoded

    @classmethod
    def with_field_validation(cls, fields: dict, paramdef: ParamDef, raw_name=b"", name=""):
        """Checks `fields` keys against `paramdef` before initializing."""
        fields = cls.validate_fields(fields, paramdef)
        return cls(fields, paramdef, raw_name, name)

    def __iter__(self):
        return iter(self.fields.items())

    def __getitem__(self, field_name: str):
        try:
            return self.fields[field_name]
        except KeyError:
            raise KeyError(f"No field with name '{field_name}' in row {self.name}.")

    def __setitem__(self, field_name: str, value):
        if field_name not in self.fields:
            raise KeyError(f"Field '{field_name}' does not exist in params. (You cannot create new fields.)")
        # TODO: Check value type is valid (or that it can be cast). (Already done at write time, though.)
        self.fields[field_name] = value

    def update(self, name: str = None, **kwargs):
        """Set multiple field values at once."""
        for field_name in kwargs:  # check that all field names are valid
            if field_name not in self.fields and field_name != "name":
                raise KeyError(f"Field '{field_name}' does not exist in params.")
        if name is not None:
            self.name = name
        self.fields |= kwargs

    @property
    def field_names(self) -> tuple[str, ...]:
        return tuple(self.fields.keys())

    def get_paramdef_field(self, field_name: str) -> ParamDefField:
        return self.paramdef[field_name]

    def __repr__(self):
        return f"\nName: {self.name}" + "".join([f"\n    {key} = {value}" for key, value in self.fields.items()])

    def copy(self):
        return copy.deepcopy(self)

    @classmethod
    def from_reader(cls, reader: BinaryReader, paramdef: ParamDef, raw_name: bytes, name="") -> ParamDictRow:
        """Unpack `ParamRow` from binary game data using `paramdef`."""
        bit_reader = BitFieldReader()

        fields = {}
        for paramdef_field in paramdef.fields.values():

            display_type = paramdef_field.display_type

            if paramdef_field.bit_count != -1:
                field_value = bit_reader.read(reader, paramdef_field.bit_count, paramdef_field.py_fmt)
            else:
                bit_reader.clear()
                if issubclass(display_type, ft.basestring):
                    field_value = display_type.read(reader, paramdef_field.size)
                elif display_type is ft.dummy8:
                    # These are often 'array' fields, but we don't even bother unpacking them.
                    field_value = reader.read(paramdef_field.size)
                else:
                    data = reader.read(display_type.size())
                    try:
                        field_value = struct.unpack(paramdef_field.py_fmt, data)[0]
                    except struct.error as e:
                        if paramdef_field.display_name in {"inverseToneMapMul", "sfxMultiplier"}:
                            # These fields are malformed in m99 and default ToneMapBank in Dark Souls Remastered.
                            field_value = 1.0
                        else:
                            raise ValueError(
                                f"Could not unpack data for field {paramdef_field.name} in row name '{name}'.\n"
                                f"Field type: {display_type}\n"
                                f"Raw bytes: {data}\n"
                                f"Error:\n{str(e)}"
                            )
            fields[paramdef_field.name] = bool(field_value) if paramdef_field.bit_count == 1 else field_value

        # No field validation needed (all fields present and valid).
        return cls(fields, paramdef, raw_name, name)

    @staticmethod
    def validate_fields(fields: dict, paramdef: ParamDef) -> dict[str, bool | int | float | str | bytes]:
        """Ensures that all ParamDef fields are present in dictionary, or assigns defaults."""
        fields = fields.copy()
        parsed_fields = {}
        for paramdef_field in paramdef.fields.values():
            if paramdef_field.display_type is ft.dummy8 and paramdef_field.bit_count == -1:  # padding bytes
                # TODO: The exceptions identified in `unpack()` will be overridden with nulls. Probably fine.
                fields.pop(paramdef_field.name, None)  # ignore given value
                parsed_fields[paramdef_field.name] = b"\0" * paramdef_field.size
            else:
                parsed_fields[paramdef_field.name] = fields.pop(paramdef_field.name, paramdef_field.py_default)

        if fields:
            leftover = ", ".join(fields.keys())
            _LOGGER.warning(f"Ignoring unknown fields in `ParamRow` of type {paramdef.param_type}: {leftover}")

        return parsed_fields

    def to_param_writer(self, writer: BinaryWriter):
        bit_writer = BitFieldWriter()

        for field_name, value in self.fields.items():  # These are ordered correctly already.
            paramdef_field = self.paramdef[field_name]
            paramdef_field.check_python_type(value)
            paramdef_field.check_range(value)
            if paramdef_field.bit_count != -1:
                bit_writer.write(writer, value, paramdef_field.bit_count, paramdef_field.py_fmt)
            else:
                bit_writer.finish_field(writer)
                if issubclass(paramdef_field.display_type, ft.basestring):
                    writer.append(paramdef_field.display_type.write(value, paramdef_field.size))
                elif paramdef_field.display_type is ft.dummy8:
                    writer.append(value)  # already null bytes
                else:
                    writer.append(struct.pack(paramdef_field.py_fmt, value))
        bit_writer.finish_field(writer)

    # NOTE: Cannot be loaded `from_dict()`.

    def to_dict(self, ignore_pads=True, ignore_defaults=True, ignore_sizes=False) -> dict[str, tp.Any]:
        data = {"raw_name": self.raw_name, "name": self.name, "fields": {}}
        for paramdef_field in self.paramdef.fields.values():
            if ignore_pads and paramdef_field.display_type == "dummy8":
                continue  # pad bytes not written
            if ignore_defaults and self.fields[paramdef_field.name] == paramdef_field.py_default:
                continue  # default values not written
            field_name = paramdef_field.name.split(":")[0] if ignore_sizes else paramdef_field.name
            data["fields"][field_name] = self.fields[paramdef_field.name]
        return data

    def compare(self, other_row: ParamDictRow):
        """Prints each field that differs between the given `ParamRow` and this one."""
        for field_name, paramdef_field in self.paramdef.fields.items():
            other = other_row[field_name]
            this = self[field_name]
            if other != this:
                print(f"  {field_name}: this = {this}, other = {other}")

    def __eq__(self, other_row: ParamDictRow):
        """Returns `True` if all fields have the same value, and `False` if not."""
        for field_name, paramdef_field in self.paramdef.fields.items():
            other = other_row[field_name]
            this = self[field_name]
            if other != this:
                if paramdef_field.display_type is ft.dummy8:
                    continue  # padding differences have no effect and do not count against equality
                return False
        return True


class Param(tp.Generic[PARAM_ROW_DATA_T], GameFile, abc.ABC):
    """Table of `ParamRows` (spreadsheet entries full of numbers used all over the place).

    This class supports all (known) games, but should be retrieved dynamically with `TypedParam(row_type)` to specify
    the `ParamDef`-generated Soulstruct `ParamRow` subclass it uses (e.g. `NPC_PARAM_ST`). That class will be used
    to unpack the row data.

    NOTE: Technically, the `ParamRow`s should be stored as a list, with `row_id` being a field of each individual row
    and multiple rows potentially having the same ID. This even happens in some vanilla files. However, the `Param` is
    so clearly meant to be a dictionary -- and the fact that the game only uses the first instance of an ID suggest that
    the game engine ITSELF basically treats it as such -- that I am using the dictionary structure and not even
    bothering loading duplicate IDs.
    """
    ROW_TYPE: tp.ClassVar[type[ParamRow]] = None
    PARAMDEF_MODULE: tp.ClassVar[ModuleType] = None

    EXT: tp.ClassVar[str] = ".param"

    class RowPointerStruct32(BinaryStruct):
        row_id: int
        data_offset: uint
        name_offset: uint

    class RowPointerStruct64(BinaryStruct):
        row_id: int
        unknown: int  # not zero in DS2:SOFTS "generatordbglocation" params according to TKGP
        data_offset: long
        name_offset: long

    param_type: str = ""
    big_endian: bool = False
    unknown: int = 0
    flags1: ParamFlags1 = ParamFlags1(0)
    flags2: ParamFlags2 = ParamFlags2(0)
    paramdef_data_version: int = 0
    paramdef_format_version: int = 0

    rows: dict[int, PARAM_ROW_DATA_T] = field(default_factory=dict)

    def __getitem__(self, row_id) -> PARAM_ROW_DATA_T:
        if row_id in self.rows:
            return self.rows[row_id]
        raise KeyError(f"No row with ID {row_id} in {self.param_type}.")

    def __setitem__(self, row_id: int, row: dict | PARAM_ROW_DATA_T):
        if isinstance(row, dict):
            row = ParamRow(**row)
        if isinstance(row, ParamRow):
            self.rows[row_id] = row
        else:
            raise TypeError("New row must be a `ParamRow` or a dictionary that contains all required fields.")

    def keys(self) -> tp.KeysView[int]:
        return self.rows.keys()

    def values(self) -> tp.ValuesView[PARAM_ROW_DATA_T]:
        return self.rows.values()

    def items(self) -> tp.ItemsView[int, PARAM_ROW_DATA_T]:
        return self.rows.items()

    def __iter__(self):
        return iter(self.rows)

    def __len__(self):
        return len(self.rows)

    def pop(self, row_id: int) -> PARAM_ROW_DATA_T:
        return self.rows.pop(row_id)

    @property
    def field_names(self):
        return self.ROW_TYPE.get_binary_field_names()

    # TODO: __repr__ method returns basic information about Param (but not entire row list).

    @classmethod
    def from_reader(cls, reader: BinaryReader):
        """Reads a `Param` from a `BinaryReader` loaded from a binary `.param` file."""

        # Peek at struct-affecting info:
        byte_order = ByteOrder.BigEndian if reader["b", 0x2c] == -1 else ByteOrder.LittleEndian
        reader.byte_order = byte_order
        version_info = reader.unpack("bbb", offset=0x2d)
        flags1 = ParamFlags1(version_info[0])
        flags2 = ParamFlags2(version_info[1])
        paramdef_format_version = version_info[2]

        name_data_offset = reader["I"]  # CANNOT BE TRUSTED IN VANILLA FILES! Off by +12 bytes.
        _row_data_offset = reader["H"]  # NOT USED! It's an unsigned short, but can be larger.
        if ((flags1[0] and flags1.IntDataOffset) or flags1.LongDataOffset) and _row_data_offset != 0:
            raise ValueError(f"Expected `_row_data_offset` of zero in this `Param`, not: {_row_data_offset}")
        unknown = reader["H"]
        if unknown not in {0, 1, 2}:  # TODO: Value of 2 in Elden Ring 'BaseChrSelectMenuParam'
            raise ValueError(f"Expected `unknown` of 0 or 1 in this `Param`, not: {unknown}")
        paramdef_data_version = reader["H"]
        row_count = reader["H"]

        if flags1.OffsetParam:
            reader.assert_pad(4)
            param_type_offset = reader["q"]
            param_type = reader.unpack_string(offset=param_type_offset, encoding="ASCII")  # e.g. 'NPC_PARAM_ST'
            reader.assert_pad(20)
        else:
            param_type = reader.unpack_string(length=32, encoding="ASCII")

        reader.read(4)  # big endian, flags1, flags2, paramdef_format_version

        if flags1[0] and flags1.IntDataOffset:
            _row_data_offset = reader["i"]  # not needed while unpacking
            reader.assert_pad(12)
        elif flags1.LongDataOffset:
            _row_data_offset = reader["q"]  # not needed while unpacking
            reader.assert_pad(8)
        # End of header.

        # Load row pointer data.
        row_pointer_struct_type = cls.RowPointerStruct64 if flags1.LongDataOffset else cls.RowPointerStruct32
        row_pointer_structs = [
            row_pointer_struct_type.from_bytes(reader) for _ in range(row_count)
        ]  # type: list[cls.RowPointerStruct64] | list[cls.RowPointerStruct32]

        # Reliable row data offset (unlike header one).
        row_data_offset = reader.position

        # Row size is lazily determined.
        if len(row_pointer_structs) == 0:
            return
        elif len(row_pointer_structs) == 1:
            # NOTE: The only vanilla param in Dark Souls with one row is LEVELSYNC_PARAM_ST (Remastered only),
            # for which the row size is hard-coded here. Otherwise, we can trust the repacked offset from Soulstruct
            # (and SoulsFormats, etc.).
            if param_type == "LEVELSYNC_PARAM_ST":
                row_size = 220
            else:  # best guess
                row_size = name_data_offset - row_data_offset
        else:  # most reliable: just use difference between first two row pointer data offsets
            row_size = row_pointer_structs[1].data_offset - row_pointer_structs[0].data_offset

        # Note that we no longer need to track reader offset.
        rows = {}
        name_encoding = cls.get_name_encoding(byte_order == ByteOrder.BigEndian, flags2)
        # TODO: Would be more efficient to unpack row data in sequence and assign row names afterwards.
        for row_struct in row_pointer_structs:
            reader.seek(row_struct.data_offset)
            row_data = reader.read(row_size)
            raw_name = b""
            name = ""
            if row_struct.name_offset != 0:
                reader.seek(row_struct.name_offset)
                raw_name = reader.unpack_bytes()  # null-terminated raw name
                try:
                    name = raw_name.decode(name_encoding)
                except UnicodeDecodeError:
                    # For whatever reason, some vanilla row names are junk (notably in DS1 DrawParam).
                    pass
            if row_struct.row_id in rows:
                _LOGGER.warning(f"Repeated param row ID in {param_type}: {row_struct.row_id}. Only first will be kept.")
            else:
                rows[row_struct.row_id] = cls.ROW_TYPE.from_reader(BinaryReader(row_data), raw_name, name)

        return cls(
            param_type=param_type,
            big_endian=ByteOrder == ByteOrder.BigEndian,
            unknown=unknown,
            flags1=flags1,
            flags2=flags2,
            paramdef_data_version=paramdef_data_version,
            paramdef_format_version=paramdef_format_version,
            rows=rows,
        )

    def sort(self):
        """Sort rows by ID."""
        self.rows = {row_id: self.rows[row_id] for row_id in sorted(self.rows)}

    def _get_dcx_type(self) -> DCXType:
        """Params never have DCX applied individually."""
        return DCXType.Null

    def to_writer(self, sort=True) -> BinaryWriter:
        # if len(self.entries) > 5461:
        #     raise SoulstructError(
        #         f"Param {self.param_type} has {len(self.entries)} entries, which is more than a "
        #         f"DS1 Param can store (5461). Remove some entries before packing it.")

        row_count = len(self.rows)

        self.sort()

        byte_order = ByteOrder.BigEndian if self.big_endian else ByteOrder.LittleEndian
        writer = BinaryWriter(byte_order=byte_order)  # no varints

        writer.reserve("row_names_offset", "I", obj=self)
        writer.reserve("_short_row_data_offset", "H", obj=self)  # unsigned short, but can be larger
        writer.pack("HHH", self.unknown, self.paramdef_data_version, row_count)

        if self.flags1.OffsetParam:
            writer.pad(4)
            writer.reserve("param_type_offset", "q", obj=self)
            writer.pad(20)
        else:
            writer.append(pad_chars(
                self.param_type, encoding="ASCII", null_terminate=True, alignment=32, pad=b"\x20")
            )

        writer.pack(
            "4b", -1 if self.big_endian else 0, self.flags1.pack(), self.flags2.pack(), self.paramdef_format_version
        )

        if self.flags1[0] and self.flags1.IntDataOffset:
            writer.reserve("row_data_offset", "i", obj=self)
            writer.pad(12)
            has_long_row_data_offset = True
        elif self.flags1.LongDataOffset:
            writer.reserve("row_data_offset", "q", obj=self)
            writer.pad(8)
            has_long_row_data_offset = True
        else:
            has_long_row_data_offset = False
        # End of header.

        # Pack row pointers.
        for row_id in self.rows:
            writer.pack("i", row_id)
            if self.flags1.LongDataOffset:
                writer.pad(4)
                writer.reserve(f"row_data_offset{row_id}", "q", obj=self)
                writer.reserve(f"row_name_offset{row_id}", "q", obj=self)
            else:
                writer.reserve(f"row_data_offset{row_id}", "i", obj=self)
                writer.reserve(f"row_name_offset{row_id}", "i", obj=self)

        writer.fill("_short_row_data_offset", min(writer.position, 2 ** 16 - 1), obj=self)
        if has_long_row_data_offset:
            writer.fill_with_position("row_data_offset", obj=self)

        # Pack row data.
        for row_id, row in self.rows.items():
            writer.fill_with_position(f"row_data_offset{row_id}", obj=self)
            row.to_writer(writer)

        if self.flags1.OffsetParam:
            writer.fill_with_position("param_type_offset", obj=self)
            writer.append(self.param_type.encode("ASCII") + b"\0")

        # Pack row names (if not empty).
        writer.fill_with_position("row_names_offset", obj=self)
        for row_id, row in self.rows.items():
            packed_name = row.get_packed_name(self.get_name_encoding(self.big_endian, self.flags2))
            if packed_name:
                writer.fill_with_position(f"row_name_offset{row_id}", obj=self)
                writer.append(packed_name)
            else:
                writer.fill(f"row_name_offset{row_id}", 0, obj=self)

        return writer

    @classmethod
    def from_dict(cls, data: dict) -> tp.Self:
        """Try to find `TypeParam`, and convert flags integers to `ParamFlagsX`."""
        if cls.ROW_TYPE is None:
            raise TypeError("Cannot read `Param` dictionary of unknown type. Use `TypedParam` first.")

        if data["param_type"] != cls.ROW_TYPE.__name__:
            raise ValueError(
                f"Incompatible 'param_type' in JSON: {data['param_type']}. Expected `{cls.ROW_TYPE.__name__}`."
            )
        data["flags1"] = ParamFlags1(int(data.pop("flags1", 0)))
        data["flags2"] = ParamFlags2(int(data.pop("flags2", 0)))
        rows = data.pop("rows")  # type: dict[int, dict | ParamRow]
        data["rows"] = {}
        row_name_encoding = cls.get_name_encoding(data["big_endian"], data["flags2"])
        for row_id, row in rows.items():
            row_id = int(row_id)  # JSON keys are strings
            if isinstance(row, ParamRow):
                data["rows"][row_id] = row  # direct assignment
            elif isinstance(row, dict):
                data["rows"][row_id] = cls.ROW_TYPE.from_dict(row, row_name_encoding=row_name_encoding)
            else:
                raise TypeError(
                    f"Each entry in dictionary 'rows' must be a `{cls.ROW_TYPE.__name__}` instance or dictionary "
                    f"version of one, not: {type(row).__name__} (row ID {row_id})"
                )

        return cls(**data)

    def to_dict(self, ignore_pads=True, ignore_defaults=True, use_internal_names=False) -> dict[str, tp.Any]:
        """Provides options to ignore pad fields and/or fields with default values."""
        data = {
            "param_type": self.param_type,
            # `paramdef` not added.
            "big_endian": self.big_endian,
            "unknown": self.unknown,
            "paramdef_data_version": self.paramdef_data_version,
            "flags1": self.flags1.pack(),
            "flags2": self.flags2.pack(),
            "paramdef_format_version": self.paramdef_format_version,
            "rows": {},
        }
        # Row name encoding needed to update `RawName`.
        row_name_encoding = self.get_name_encoding(self.big_endian, self.flags2)
        for i in sorted(self.rows):
            data["rows"][i] = self.rows[i].to_dict(ignore_pads, ignore_defaults, use_internal_names, row_name_encoding)
        return data

    @classmethod
    def from_json(cls, json_path: str | Path) -> tp.Self:
        if cls.ROW_TYPE is None:
            raise TypeError("Cannot call `Param.from_json()` on `Param` of unknown row type.")
        # noinspection PyTypeChecker
        return super(Param, cls).from_json(json_path)

    def write_json(
        self, file_path: Path | str = None, encoding="utf-8", indent=4, ignore_pads=True, ignore_defaults=True
    ):
        """Extra arguments passed through to `Param.to_dict()`."""
        json_dict = self.to_dict(ignore_pads=ignore_pads, ignore_defaults=ignore_defaults)
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because file default `path` has not been set.")
            file_path = self.path
        file_path = Path(file_path)
        if file_path.suffix != ".json":
            file_path = file_path.with_suffix(file_path.suffix + ".json")
        write_json(file_path, json_dict, indent=indent, encoding=encoding)

    def get_range(self, start, count):
        return [(row_id, self[row_id]) for row_id in sorted(self.rows)[start:start + count]]

    @classmethod
    def detect_param_type(cls, source: Path | str | bytes | BinaryReader) -> str:
        """Peek at `param_type` without fully unpacking (e.g. to call `TypedParam` correctly)."""
        if isinstance(source, (Path, str)):
            reader = BinaryReader(source)
        elif isinstance(source, BinaryReader):
            reader = source
        else:
            reader = BinaryReader(source)

        byte_order = ByteOrder.BigEndian if reader["b", 0x2c] == -1 else ByteOrder.LittleEndian
        reader.byte_order = byte_order
        version_info = reader.unpack("BBB", offset=0x2d)
        flags1 = ParamFlags1(version_info[0])

        _ = reader["I"]
        _row_data_offset = reader["H"]  # NOT USED! It's an unsigned short, but can be larger.
        if ((flags1[0] and flags1.IntDataOffset) or flags1.LongDataOffset) and _row_data_offset != 0:
            raise ValueError(f"Expected `_row_data_offset` of zero in this `Param`, not: {_row_data_offset}")
        unknown = reader["H"]
        if unknown not in {0, 1, 2}:  # TODO: Values of 2 found in Elden Ring.
            raise ValueError(f"Expected `unknown` of 0 or 1 in this `Param`, not: {unknown}")

        reader.unpack("HH")  # paramdef data version, row count

        if flags1.OffsetParam:
            reader.assert_pad(4)
            param_type_offset = reader["q"]
            param_type = reader.unpack_string(offset=param_type_offset, encoding="ASCII")  # e.g. 'NPC_PARAM_ST'
            reader.assert_pad(20)
        else:
            param_type = reader.unpack_string(length=32, encoding="ASCII")

        return param_type

    @staticmethod
    def get_name_encoding(big_endian: bool, flags2: ParamFlags2):
        if flags2.UnicodeRowNames:
            return "utf-16-be" if big_endian else "utf-16-le"
        return "shift_jis_2004"


class ParamDict(Param):
    """Deprecated type that unpacks `ParamRowDict`s using a `ParamDef` instead of using baked Soulstruct classes."""

    # Initially, rows are kept as just `(raw_name, name, row_bytes)` tuple, until `ParamDef` is applied.
    row_bytes: dict[int, tuple[bytes, str, bytes]] | None = None
    # Generated by manual `unpack_rows()` call with `paramdef`.
    row_dicts: dict[int, ParamDictRow] = field(default_factory=dict)
    paramdef: ParamDef = None

    @classmethod
    def from_reader(cls, reader: BinaryReader):
        """Use a `ParamDefBND` to """

        # Peek at struct-affecting info:
        byte_order = ByteOrder.BigEndian if reader["b", 0x2c] == -1 else ByteOrder.LittleEndian
        version_info = reader.unpack("bbb", offset=0x2d)
        flags1 = ParamFlags1(version_info[0])
        flags2 = ParamFlags2(version_info[1])
        paramdef_format_version = version_info[2]

        row_names_offset = reader["I"]  # CANNOT BE TRUSTED IN VANILLA FILES! Off by +12 bytes.
        _row_data_offset = reader["H"]  # NOT USED! It's an unsigned short, but can be larger.
        if ((flags1[0] and flags1.IntDataOffset) or flags1.LongDataOffset) and _row_data_offset != 0:
            raise ValueError(f"Expected `_row_data_offset` of zero in this `Param`, not: {_row_data_offset}")
        unknown = reader["H"]
        if unknown not in {0, 1}:
            raise ValueError(f"Expected `unknown` of 0 or 1 in this `Param`, not: {unknown}")
        paramdef_data_version = reader["H"]
        row_count = reader["H"]

        if flags1.OffsetParam:
            reader.assert_pad(4)
            param_type_offset = reader["q"]
            param_type = reader.unpack_string(offset=param_type_offset, encoding="ASCII")  # e.g. 'NPC_PARAM_ST'
            reader.assert_pad(20)
        else:
            param_type = reader.unpack_string(length=32, encoding="ASCII")

        reader.read(4)  # big endian, flags1, flags2, paramdef_format_version

        if flags1[0] and flags1.IntDataOffset:
            _row_data_offset = reader["i"]  # not needed while unpacking
            reader.assert_pad(12)
        elif flags1.LongDataOffset:
            _row_data_offset = reader["q"]  # not needed while unpacking
            reader.assert_pad(8)
        # End of header.

        # Load row pointer data.
        row_pointer_struct_type = cls.RowPointerStruct64 if flags1.LongDataOffset else cls.RowPointerStruct32
        row_pointer_structs = [
            row_pointer_struct_type.from_bytes(reader) for _ in range(row_count)
        ]  # type: list[cls.RowPointerStruct64] | list[cls.RowPointerStruct32]

        # Reliable row data offset (unlike header one).
        row_data_offset = reader.position  # Reliable row data offset.

        # Row size is lazily determined.
        if len(row_pointer_structs) == 0:
            return
        elif len(row_pointer_structs) == 1:
            # NOTE: The only vanilla param in Dark Souls with one row is LEVELSYNC_PARAM_ST (Remastered only),
            # for which the row size is hard-coded here. Otherwise, we can trust the repacked offset from Soulstruct
            # (and SoulsFormats, etc.).
            if param_type == "LEVELSYNC_PARAM_ST":
                row_size = 220
            else:  # best guess
                row_size = row_names_offset - row_data_offset
        else:  # most reliable: just use difference between first two row pointer data offsets
            row_size = row_pointer_structs[1].data_offset - row_pointer_structs[0].data_offset

        # Note that we no longer need to track reader offset.
        row_bytes = {}
        name_encoding = cls.get_name_encoding(byte_order == ByteOrder.BigEndian, flags2)
        # TODO: Would be more efficient to unpack row data in sequence and assign row names afterwards.
        for row_struct in row_pointer_structs:
            reader.seek(row_struct.data_offset)
            row_data = reader.read(row_size)
            raw_name = b""
            name = ""
            if row_struct.name_offset != 0:
                reader.seek(row_struct.name_offset)
                raw_name = reader.unpack_bytes()  # null-terminated raw name
                try:
                    name = raw_name.decode(name_encoding)
                except UnicodeDecodeError:
                    # For whatever reason, some vanilla row names are junk (notably in DS1 DrawParam).
                    pass
            if row_struct.row_id in row_bytes:
                _LOGGER.warning(f"Repeated param row ID in {param_type}: {row_struct.row_id}. Only first will be kept.")
            else:
                row_bytes[row_struct.row_id] = (raw_name, name, row_data)

        return cls(
            param_type=param_type,
            big_endian=ByteOrder == ByteOrder.BigEndian,
            unknown=unknown,
            flags1=flags1,
            flags2=flags2,
            paramdef_data_version=paramdef_data_version,
            paramdef_format_version=paramdef_format_version,
            row_bytes=row_bytes,
        )

    def unpack_rows(self, paramdef_or_paramdefbnd: ParamDef | ParamDefBND | None = None):
        if self.row_bytes is None:
            _LOGGER.warning(f"Rows in `Param` with type '{self.param_type}' have already been unpacked from bytes.")
            return

        if paramdef_or_paramdefbnd is None:
            paramdef_or_paramdefbnd = ParamDefBND.from_bundled(self.get_game())
        if isinstance(paramdef_or_paramdefbnd, ParamDefBND):
            try:
                paramdef = paramdef_or_paramdefbnd[self.param_type]
            except KeyError:
                raise ValueError(f"Cannot find param type `{self.param_type}` in given `paramdefbnd`.")
        elif not isinstance(paramdef_or_paramdefbnd, ParamDef):
            raise TypeError("`unpack_rows()` must be called with a `ParamDefBND` (easier) or correct `ParamDef`.")
        else:
            paramdef = paramdef_or_paramdefbnd

        if paramdef.param_type != self.param_type:
            raise ValueError(
                f"`Param.param_type` {self.param_type} does not match paramdef.param_type` {paramdef.param_type}."
            )
        if paramdef.data_version != self.paramdef_data_version:
            raise ValueError(
                f"`Param.paramdef_data_version` {self.paramdef_data_version} does not match "
                f"`paramdef.data_version` {paramdef.data_version}."
            )
        # NOTE: `format_version` in Param is not correct/used.

        # Note that we no longer need to track reader offset.
        self.row_dicts = {}
        for row_id, (raw_name, name, data) in self.row_bytes.items():
            self.row_dicts[row_id] = ParamDictRow.from_reader(BinaryReader(data), paramdef, raw_name, name)

        # Remove row bytes.
        self.row_bytes = None

    @classmethod
    def from_dict(cls, data: dict):
        raise TypeError("Cannot load a generic `ParamDict` from a dictionary (yes, ironic).")

    def to_writer(self, sort=True) -> BinaryWriter:
        # if len(self.entries) > 5461:
        #     raise SoulstructError(
        #         f"Param {self.param_type} has {len(self.entries)} entries, which is more than a "
        #         f"DS1 Param can store (5461). Remove some entries before packing it.")

        if self.row_bytes is not None and self.row_dicts:
            raise ValueError(
                "Param has both raw `row_bytes` and unpacked `row_dict`. Cannot pack. "
                "Only use `unpack_rows()` to unpack the raw data."
            )
        row_count = len(self.row_bytes) if self.row_bytes is not None else len(self.row_dicts)

        self.sort()

        byte_order = ByteOrder.BigEndian if self.big_endian else ByteOrder.LittleEndian
        writer = BinaryWriter(byte_order=byte_order)  # no varints

        writer.reserve("row_names_offset", "I", obj=self)
        writer.reserve("_short_row_data_offset", "H", obj=self)  # unsigned short, but can be larger
        writer.pack("HHH", self.unknown, self.paramdef_data_version, row_count)

        if self.flags1.OffsetParam:
            writer.pad(4)
            writer.reserve("param_type_offset", "q", obj=self)
            writer.pad(20)
        else:
            writer.append(pad_chars(self.param_type, encoding="ASCII", null_terminate=False, alignment=32))

        writer.pack(
            "4b", -1 if self.big_endian else 0, self.flags1.pack(), self.flags2.pack(), self.paramdef_format_version
        )

        if self.flags1[0] and self.flags1.IntDataOffset:
            writer.reserve("row_data_offset", "i", obj=self)
            writer.pad(12)
            has_long_row_data_offset = True
        elif self.flags1.LongDataOffset:
            writer.reserve("row_data_offset", "q", obj=self)
            writer.pad(8)
            has_long_row_data_offset = True
        else:
            has_long_row_data_offset = False
        # End of header.

        # Pack row pointers.
        for row_id in (self.row_bytes if self.row_bytes is not None else self.row_dicts):
            writer.pack("i", row_id)
            if self.flags1.LongDataOffset:
                writer.pad(4)
                writer.reserve(f"row_data_offset{row_id}", "q", obj=self)
                writer.reserve(f"row_name_offset{row_id}", "q", obj=self)
            else:
                writer.reserve(f"row_data_offset{row_id}", "i", obj=self)
                writer.reserve(f"row_name_offset{row_id}", "i", obj=self)

        writer.fill("_short_row_data_offset", min(writer.position, 2 ** 16 - 1), obj=self)
        if has_long_row_data_offset:
            writer.fill_with_position("row_data_offset", obj=self)

        if self.row_bytes is not None:  # rows have not been unpacked
            for row_id, (_, _, data) in self.row_bytes.items():
                writer.fill_with_position(f"row_data_offset{row_id}", obj=self)
                writer.append(data)
        else:
            # Pack row data.
            for row_id, row in self.row_dicts.items():
                writer.fill_with_position(f"row_data_offset{row_id}", obj=self)
                row.to_param_writer(writer)

        if self.flags1.OffsetParam:
            writer.fill_with_position("param_type_offset", obj=self)
            writer.append(self.param_type.encode("ASCII") + b"\0")

        # Pack row names.
        name_encoding = self.get_name_encoding(self.big_endian, self.flags2)
        if self.row_bytes is not None:
            for row_id, (raw_name, name, _) in self.row_bytes.items():
                writer.fill_with_position(f"row_name_offset{row_id}")
                raw_name = name.encode(name_encoding) if name else raw_name
                raw_name = raw_name.rstrip(b"\0") + (b"\0\0" if self.flags2.UnicodeRowNames else b"\0")
                writer.append(raw_name)
        else:
            for row_id, row in self.row_dicts.items():
                writer.fill_with_position(f"row_name_offset{row_id}")
                raw_name = row.name.encode(name_encoding) if row.name else row.raw_name
                raw_name = raw_name.rstrip(b"\0") + (b"\0\0" if self.flags2.UnicodeRowNames else b"\0")
                writer.append(raw_name)

        return writer


def TypedParam(row_type: type[ParamRow]):
    """Generate a `Param` subclass dynamically with the given row type (or retrieve correct existing subclass)."""
    for param_subclass in Param.__subclasses__():
        if param_subclass.__name__ == "ParamDict":
            continue
        if param_subclass.ROW_TYPE is row_type:
            return param_subclass
    new_param_subclass = type(f"Param_{row_type.__name__}", (Param,), {"ROW_TYPE": row_type})
    new_param_subclass.__module__ = row_type.__module__
    return new_param_subclass
