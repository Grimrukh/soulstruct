from __future__ import annotations

import abc
import copy
import io
import logging
import struct
import typing as tp

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import BinaryStruct, BinaryReader

from . import field_types as ft
from .utils import BitFieldReader, BitFieldWriter, FieldDisplayInfo
from .flags import ParamFlags1, ParamFlags2
from .paramdef import ParamDef, ParamDefField, ParamDefBND

_LOGGER = logging.getLogger(__name__)


class ParamRow:

    def __init__(
        self,
        row_source: tp.Union[dict, bytes, io.BufferedIOBase, BinaryReader],
        paramdef: ParamDef,
        name: tp.Union[bytes, str] = None,
    ):
        self.fields = {}  # type: dict[str, tp.Union[bool, int, float, str, bytes]]
        self.paramdef = paramdef
        self.bit_reader = BitFieldReader()
        self.bit_writer = BitFieldWriter()
        self.name = ""

        if isinstance(row_source, dict):
            if name is None:
                if "name" not in row_source:
                    raise ValueError("Name must be specified with `name` argument or in `ParamRow` source dictionary.")
                self.name = row_source["name"]
            elif isinstance(name, str):
                if "name" in row_source:
                    _LOGGER.warning(
                        f"Name '{row_source['name']}' in source dictionary of ParamRow will be overridden with `name` "
                        f"argument value '{name}'."
                    )
                self.name = name
            else:
                raise ValueError("`name` must be a string if given.")
            self.load_dict(row_source)
        elif isinstance(row_source, (bytes, io.BufferedIOBase, BinaryReader)):
            if name is None:
                raise ValueError("`name` argument must be given explictly alongside raw `ParamRow` data.")
            self.name = name
            self.unpack(BinaryReader(row_source))
        else:
            raise TypeError(f"Cannot load `ParamRow` from source type: `{type(row_source)}`")

    def __iter__(self):
        return iter(self.fields.items())

    def __getitem__(self, field):
        if isinstance(field, int):
            try:
                field = list(self.fields.keys())[field]
            except IndexError:
                raise KeyError(f"No field with index {field}.")
        if isinstance(field, str):
            try:
                return self.fields[field]
            except KeyError:
                raise KeyError(f"No field with name '{field}' in row {self.name}.")

    def __setitem__(self, field, value):
        if isinstance(field, int):
            try:
                field = list(self.fields.keys())[field]
            except IndexError:
                raise KeyError(f"No field with index {field}. (You cannot create new fields.)")
        if field not in self.fields:
            raise KeyError(f"Field '{field}' does not exist in params.")
        # TODO: Check value type is valid (or that it can be cast).
        self.fields[field] = value

    def update(self, **kwargs):
        for field in kwargs:
            if field not in self.fields and field != "name":
                raise KeyError(f"Field '{field}' does not exist in params.")
        if "name" in kwargs:
            self.name = kwargs.pop("name")
        self.fields |= kwargs

    @property
    def field_names(self) -> tuple[str, ...]:
        if self.paramdef.param_info:
            return tuple(field.name for field in self.paramdef.param_info["fields"])
        else:
            return tuple(self.fields.keys())

    def get_paramdef_field(self, field_name: str) -> ParamDefField:
        return self.paramdef[field_name]

    def get_paramdef_field_display_info(self, field_name: str) -> FieldDisplayInfo:
        return self.paramdef[field_name].get_display_info(self)

    def __repr__(self):
        return f"\nName: {self.name}" + "".join([f"\n    {key} = {value}" for key, value in self.fields.items()])

    def copy(self):
        return copy.deepcopy(self)

    def unpack(self, row_reader: BinaryReader):

        for field in self.paramdef.fields.values():

            if field.bit_count != -1:
                field_value = self.bit_reader.read(row_reader, field.bit_count, field.fmt)
            else:
                self.bit_reader.clear()
                if issubclass(field.type_class, ft.basestring):
                    field_value = field.type_class.read(row_reader, field.size)
                elif field.type_class is ft.dummy8:
                    # These are often 'array' fields, but we don't even bother unpacking them.
                    field_value = row_reader.read(field.size)
                else:
                    data = row_reader.read(field.type_class.size())
                    try:
                        field_value = struct.unpack(field.fmt, data)[0]
                    except struct.error as e:
                        if field.display_name in {"inverseToneMapMul", "sfxMultiplier"}:
                            # These fields are malformed in m99 and default ToneMapBank in Dark Souls Remastered.
                            field_value = 1.0
                        else:
                            raise ValueError(
                                f"Could not unpack data for field {field.name} in ParamRow {self.name}.\n"
                                f"Field type: {field.display_type}\n"
                                f"Raw bytes: {data}\n"
                                f"Error:\n{str(e)}"
                            )
            self.fields[field.name] = bool(field_value) if field.bit_count == 1 else field_value

    def load_dict(self, data: dict):
        for field in self.paramdef.fields.values():
            if field.type_class is ft.dummy8 and field.bit_count == -1:  # padding bytes
                # TODO: The exceptions identified in `unpack()` will be overridden with nulls. Probably fine.
                data.pop(field.name, None)  # ignore given value
                self.fields[field.name] = b"\0" * field.size
            else:
                self.fields[field.name] = data.get(field.name, field.new_default)

    def pack(self) -> bytes:
        packed_row = b""
        for field_name, value in self.fields.items():  # These are ordered correctly already.
            field = self.paramdef[field_name]
            field.check_python_type(value)
            field.check_range(value)
            if field.bit_count != -1:
                packed_row += self.bit_writer.write(value, field.bit_count, field.fmt)
            else:
                packed_row += self.bit_writer.finish_field()
                if issubclass(field.type_class, ft.basestring):
                    packed_row += field.type_class.write(value, field.size)
                elif field.type_class is ft.dummy8:
                    packed_row += value  # already bytes
                else:
                    packed_row += struct.pack(field.fmt, value)
        packed_row += self.bit_writer.finish_field()
        return packed_row

    def to_dict(self, ignore_pads=True, ignore_defaults=True, ignore_sizes=False) -> dict[str, tp.Any]:
        data = {"name": self.name}
        for field in self.paramdef.fields.values():
            if ignore_pads and field.display_type == "dummy8":
                continue  # pad bytes not written
            if ignore_defaults and self.fields[field.name] == field.new_default:
                continue  # default values not written
            field_name = field.name.split(":")[0] if ignore_sizes else field.name
            data[field_name] = self.fields[field.name]
        return data

    def compare(self, other_row: ParamRow):
        """Prints each field that differs between the given `ParamRow` and this one."""
        for field_name, field in self.paramdef.fields.items():
            other = other_row[field_name]
            this = self[field_name]
            if other != this:
                print(f"  {field_name}: this = {this}, other = {other}")

    def __eq__(self, other_row: ParamRow):
        """Returns `True` if all fields have the same value, and `False` if not."""
        for field_name, field in self.paramdef.fields.items():
            other = other_row[field_name]
            this = self[field_name]
            if other != this:
                if field.display_type == "dummy8":
                    continue  # padding differences have no effect and do not count against equality
                return False
        return True


class Param(GameFile, abc.ABC):
    """This base class supports all binary versions, but lacks information about game-specific enums, etc."""

    GET_BUNDLED_PARAMDEF: tp.Callable = None

    @staticmethod
    def GET_HEADER_STRUCT(flags1: ParamFlags1, byte_order) -> BinaryStruct:
        fields = [
            ("name_data_offset", "I"),
            "2x" if (flags1[0] and flags1.IntDataOffset) or flags1.LongDataOffset else ("row_data_offset", "H"),
            ("unknown", "H"),  # 0 or 1
            ("paramdef_data_version", "H"),
            ("row_count", "H"),
        ]
        if flags1.OffsetParam:
            fields += [
                "4x",
                ("param_type_offset", "q"),
                "20x",
            ]
        else:
            fields.append(
                ("param_type", "32j")
            )
        fields += [
            ("big_endian", "b", 255 if byte_order == ">" else 0),
            ("flags1", "b"),
            ("flags2", "b"),
            ("paramdef_format_version", "b"),
        ]
        if flags1[0] and flags1.IntDataOffset:
            fields += [
                ("row_data_offset", "i"),
                "12x",
            ]
        elif flags1.LongDataOffset:
            fields += [
                ("row_data_offset", "q"),
                "8x",
            ]
        return BinaryStruct(*fields, byte_order=byte_order)

    ROW_STRUCT_32 = BinaryStruct(
        # These are packed together, and contain offsets into packed row data and packed names.
        ("id", "i"),
        ("data_offset", "I"),
        ("name_offset", "I"),
    )

    ROW_STRUCT_64 = BinaryStruct(
        # Same as above, but with 64-bit offsets.
        ("id", "i"),
        ("unknown", "i", 0),  # not zero in DS2:SOFTS "generatordbglocation" params according to TKGP
        ("data_offset", "q"),
        ("name_offset", "q"),
    )

    rows: dict[int, ParamRow]

    def __init__(self, param_source, dcx_magic=(), paramdef_bnd=None, undecodable_row_names: tuple[bytes, ...] = ()):
        if paramdef_bnd is None:
            self._paramdef_bnd = self.GET_BUNDLED_PARAMDEF()
        elif isinstance(paramdef_bnd, ParamDefBND):
            self._paramdef_bnd = paramdef_bnd
        else:
            raise TypeError(
                f"`paramdef_bnd` must be None or an existing `ParamDefBND` instance, not {type(paramdef_bnd)}."
            )
        self.param_type = ""  # internal name (shift_jis_2004) with capitals and underscores
        self.byte_order = "<"
        self.unknown = 0
        self.flags1 = ParamFlags1(0)
        self.flags2 = ParamFlags2(0)
        self.paramdef_data_version = 0
        self.paramdef_format_version = 0
        self.undecodable_row_names = undecodable_row_names

        self.rows = {}  # type: dict[int, ParamRow]

        super().__init__(param_source, dcx_magic=dcx_magic)

    def __getitem__(self, row_id):
        if row_id in self.rows:
            return self.rows[row_id]
        raise KeyError(f"No row with ID {row_id} in {self.param_type}.")

    def __setitem__(self, row_index, row):
        if isinstance(row, dict):
            if "name" not in row:
                raise ValueError("New row must have a 'name' field.")
            row = ParamRow(row, self._paramdef_bnd[self.param_type])
        if isinstance(row, ParamRow):
            self.rows[row_index] = row
        else:
            raise TypeError("New row must be a `ParamRow` or a dictionary that contains all required fields.")

    def keys(self):
        return self.rows.keys()

    def values(self):
        return self.rows.values()

    def items(self) -> tp.ItemsView[int, ParamRow]:
        return self.rows.items()

    def __iter__(self):
        return iter(self.rows)

    def __len__(self):
        return len(self.rows)

    def pop(self, row_id):
        return self.rows.pop(row_id)

    @property
    def paramdef(self):
        return self._paramdef_bnd[self.param_type]

    @property
    def param_info(self):
        return self.paramdef.param_info

    @property
    def field_names(self):
        if self.paramdef.param_info:
            return [field.name for field in self.paramdef.param_info["fields"]]
        else:
            return list(self.rows[0].fields.keys())

    @property
    def nickname(self) -> tp.Optional[str]:
        """Could return None for ambiguous Params like 'PlayerBehaviors'. Handled externally."""
        if self.paramdef.param_info:
            return self.paramdef.param_info["nickname"]
        return None

    # TODO: __repr__ method returns basic information about Param (but not entire row list).

    def unpack(self, reader: BinaryReader, **kwargs):
        self.byte_order = reader.byte_order = ">" if reader.unpack_value("B", offset=44) == 255 else "<"
        version_info = reader.unpack("bbb", offset=45)
        self.flags1 = ParamFlags1(version_info[0])
        self.flags2 = ParamFlags2(version_info[1])
        self.paramdef_format_version = version_info[2]
        header_struct = self.GET_HEADER_STRUCT(self.flags1, self.byte_order)
        header = reader.unpack_struct(header_struct)
        try:
            self.param_type = header["param_type"]
        except KeyError:
            self.param_type = reader.unpack_string(offset=header["param_type_offset"], encoding="utf-8")
        self.paramdef_data_version = header["paramdef_data_version"]
        self.unknown = header["unknown"]
        # Row data offset in header not used. (It's an unsigned short, yet doesn't limit row count to 5461.)
        name_data_offset = header["name_data_offset"]  # CANNOT BE TRUSTED IN VANILLA FILES! Off by +12 bytes.

        # Load row pointer data.
        row_struct = self.ROW_STRUCT_64 if self.flags1.LongDataOffset else self.ROW_STRUCT_32
        row_pointers = reader.unpack_structs(row_struct, count=header["row_count"])
        row_data_offset = reader.position  # Reliable row data offset.

        # Row size is lazily determined. TODO: Unpack row data in sequence and associate with names separately.
        if len(row_pointers) == 0:
            return
        elif len(row_pointers) == 1:
            # NOTE: The only vanilla param in Dark Souls with one row is LEVELSYNC_PARAM_ST (Remastered only),
            # for which the row size is hard-coded here. Otherwise, we can trust the repacked offset from Soulstruct
            # (and SoulsFormats, etc.).
            if self.param_type == "LEVELSYNC_PARAM_ST":
                row_size = 220
            else:
                row_size = name_data_offset - row_data_offset
        else:
            row_size = row_pointers[1]["data_offset"] - row_pointers[0]["data_offset"]

        # Note that we no longer need to track reader offset.
        name_encoding = self.get_name_encoding()
        for row_struct in row_pointers:
            reader.seek(row_struct["data_offset"])
            row_data = reader.read(row_size)
            if row_struct["name_offset"] != 0:
                try:
                    name = reader.unpack_string(
                        offset=row_struct["name_offset"],
                        encoding=name_encoding,
                        reset_old_offset=False,  # no need to reset
                    )
                except UnicodeDecodeError as ex:
                    if ex.object in self.undecodable_row_names:
                        name = reader.unpack_bytes(
                            offset=row_struct["name_offset"],
                            reset_old_offset=False,  # no need to reset
                        )
                    else:
                        raise
                except ValueError:
                    reader.seek(row_struct["name_offset"])
                    _LOGGER.error(
                        f"Error encountered while parsing row name string in {self.param_type}.\n"
                        f"    Header: {header}\n"
                        f"    Row Struct: {row_struct}\n"
                        f"    30 chrs of name data: {' '.join(f'{{:02x}}'.format(x) for x in reader.read(30))}"
                    )
                    raise
            else:
                name = ""
            self.rows[row_struct["id"]] = ParamRow(row_data, self.paramdef, name=name)

    def pack(self, sort=True):
        # if len(self.entries) > 5461:
        #     raise SoulstructError(
        #         f"Param {self.param_type} has {len(self.entries)} entries, which is more than a "
        #         f"DS1 Param can store (5461). Remove some entries before packing it.")

        row_ids = sorted(self.rows) if sort else self.rows

        current_name_offset = 0
        name_offset_list = []
        data_offset = 0
        data_offset_list = []
        packed_names = b""
        packed_data = b""
        name_encoding = self.get_name_encoding()

        for row_id in row_ids:
            row = self.rows[row_id]

            # Pack names with relative offsets (to be globally offset later).
            if row.name in self.undecodable_row_names:
                name_z_str = row.name + (b"\0\0" if self.flags2.UnicodeRowNames else b"\0")  # name was never decoded
            else:
                name_z_str = row.name.encode(name_encoding) + (b"\0\0" if self.flags2.UnicodeRowNames else b"\0")
            packed_names += name_z_str
            name_offset_list.append(current_name_offset)
            current_name_offset += len(name_z_str)

            # Pack row data.
            packed_row = row.pack()
            packed_data += packed_row
            data_offset_list.append(data_offset)
            data_offset += len(packed_row)

        header_struct = self.GET_HEADER_STRUCT(self.flags1, self.byte_order)
        if "param_type_offset" in header_struct.field_names:
            raise NotImplementedError("Soulstruct cannot yet pack/write this 2016+ version of `Param`.")
        row_pointer_struct = self.ROW_STRUCT_64 if self.flags1.LongDataOffset else self.ROW_STRUCT_32
        row_pointers_offset = header_struct.size
        row_data_offset = row_pointers_offset + row_pointer_struct.size * len(self.rows)
        name_data_offset = row_data_offset + len(packed_data)

        # Entries.
        row_pointer_data = b""
        for i, row_id in enumerate(row_ids):
            row_pointer_data += row_pointer_struct.pack(
                id=row_id,
                data_offset=row_data_offset + data_offset_list[i],
                name_offset=name_data_offset + name_offset_list[i],
            )

        # Header.
        header_fields = dict(
            name_data_offset=name_data_offset,
            unknown=self.unknown,
            paramdef_data_version=self.paramdef_data_version,
            row_count=len(self.rows),
            param_type=self.param_type,
            flags1=self.flags1.pack(),
            flags2=self.flags2.pack(),
            paramdef_format_version=self.paramdef_format_version,
        )
        if (self.flags1[0] and self.flags1.IntDataOffset) or self.flags1.LongDataOffset:
            header_fields["row_data_offset"] = row_data_offset
        else:
            # Clamp to maximum ushort value. (Not used anyway.)
            header_fields["row_data_offset"] = min(row_data_offset, 2 ** 16 - 1)  # not actually used anyway
        header = header_struct.pack(header_fields)
        return header + row_pointer_data + packed_data + packed_names

    def load_dict(self, data: dict):
        if "rows" not in data:
            raise KeyError(f"Field `rows` not specified in `Param` dict.")
        try:
            self.byte_order = ">" if data.pop("big_endian") else "<"
        except KeyError:
            raise KeyError(f"Field `big_endian` not specified in `Param` dict.")
        for field in (
            "param_type",
            "unknown",
            "paramdef_data_version",
            "paramdef_format_version",
            "undecodable_row_names",
        ):
            try:
                value = data.pop(field)
            except KeyError:
                raise KeyError(f"Field `{field}` not specified in `Param` dict.")
            setattr(self, field, value)

        try:
            self.flags1 = ParamFlags1(data.pop("flags1"))
        except KeyError:
            raise KeyError("Field `flags1` not specified in `Param` dict.")
        try:
            self.flags2 = ParamFlags2(data.pop("flags2"))
        except KeyError:
            raise KeyError("Field `flags2` not specified in `Param` dict.")

        self.rows = {}
        for i, row in data["rows"].items():
            try:
                i = int(i)
            except (ValueError, TypeError):
                raise KeyError(f"All keys of `Param` dict must be integers, not {i}.")
            if isinstance(row, ParamRow):
                self.rows[i] = row
            else:
                try:
                    self.rows[i] = ParamRow(row, paramdef=self._paramdef_bnd[self.param_type])
                except Exception as ex:
                    raise ValueError(f"Could not interpret value of `rows[{i}]` as a `ParamRow`. Error: {ex}")

    def to_dict(self, ignore_pads=True, ignore_defaults=True):
        data = {
            "param_type": self.param_type,
            "big_endian": True if self.byte_order == ">" else False,
            "unknown": self.unknown,
            "paramdef_data_version": self.paramdef_data_version,
            "flags1": self.flags1.pack(),
            "flags2": self.flags2.pack(),
            "paramdef_format_version": self.paramdef_format_version,
            "undecodable_row_names": self.undecodable_row_names,
            "rows": {},
        }
        for i in sorted(self.rows):
            data["rows"][i] = self.rows[i].to_dict(ignore_pads=ignore_pads, ignore_defaults=ignore_defaults)
        return data

    def get_range(self, start, count):
        return [(param_id, self[param_id]) for param_id in sorted(self.rows)[start: start + count]]

    def get_name_encoding(self):
        if self.flags2.UnicodeRowNames:
            return "utf-16-be" if self.byte_order == ">" else "utf-16-le"
        else:
            return "shift_jis_2004"
