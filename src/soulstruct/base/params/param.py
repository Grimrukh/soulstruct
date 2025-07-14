from __future__ import annotations

__all__ = ["Param", "TypedParam"]

import abc
import logging
import typing as tp
from dataclasses import field
from pathlib import Path
from types import ModuleType

from soulstruct.base.game_file import GameFile
from soulstruct.dcx import DCXType
from soulstruct.utilities.binary import *
from soulstruct.utilities.text import pad_chars
from soulstruct.utilities.files import write_json

from .param_row import ParamRow
from .flags import ParamFlags1, ParamFlags2

_LOGGER = logging.getLogger(__name__)


PARAM_ROW_DATA_T = tp.TypeVar("PARAM_ROW_DATA_T", bound=ParamRow)


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

    def __iter__(self) -> tp.Iterator[tuple[int, PARAM_ROW_DATA_T]]:
        return iter(self.rows.items())

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

        # If there are no row pointer structs, return an empty `Param`.
        if len(row_pointer_structs) == 0:
            return cls(
                param_type=param_type,
                big_endian=ByteOrder == ByteOrder.BigEndian,
                unknown=unknown,
                flags1=flags1,
                flags2=flags2,
                paramdef_data_version=paramdef_data_version,
                paramdef_format_version=paramdef_format_version,
                rows={},
            )

        # Row size is lazily determined.
        if len(row_pointer_structs) == 1:
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
                try:
                    row = cls.ROW_TYPE.from_bytes(row_data)
                except Exception as ex:
                    raise ValueError(
                        f"Could not read `ParamRow` of data type `{cls.__name__}` from {len(row_data)} bytes: {ex}"
                    )
                row.RawName = raw_name
                row.Name = name
                rows[row_struct.row_id] = row

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


# noinspection PyPep8Naming
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
