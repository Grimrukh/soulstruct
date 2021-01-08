import abc
import copy
import io
import logging
import struct
import typing as tp

from soulstruct.game_file import GameFile
from soulstruct.params.core import BitField, FieldDisplayInfo, ParamError
from soulstruct.params.base.paramdef import ParamDef, ParamDefField, ParamDefBND
from soulstruct.utilities import unpack_from_buffer, read_chars_from_buffer
from soulstruct.utilities.binary_struct import BinaryStruct

from .flags import ParamFlags1, ParamFlags2

_LOGGER = logging.getLogger(__name__)


class ParamRow(abc.ABC):

    def __init__(self, row_source, paramdef: ParamDef, name=None):
        self.fields = {}
        self.paramdef = paramdef
        self.bit_field = BitField()
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
        elif isinstance(row_source, (bytes, io.BufferedIOBase)):
            if name is None:
                raise ValueError("`name` argument must be given explictly alongside raw `ParamRow` data.")
            self.name = name
            self.unpack(row_source)
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

    @property
    def field_names(self):
        if self.paramdef.param_info:
            return [field.name for field in self.paramdef.param_info["fields"]]
        else:
            return list(self.fields.keys())

    @abc.abstractmethod
    def get_field_type(self, field):
        """Look for field type in game-specific appropriate `enums` module."""
        raise NotImplementedError

    def get_paramdef_field(self, field_name: str) -> ParamDefField:
        return self.paramdef[field_name]

    def get_paramdef_field_display_info(self, field_name: str) -> FieldDisplayInfo:
        return self.paramdef[field_name].get_display_info(self)

    def __repr__(self):
        return f"\nName: {self.name}" + "".join([f"\n    {key} = {value}" for key, value in self.fields.items()])

    def copy(self):
        return copy.deepcopy(self)

    def unpack(self, row_buffer):
        if isinstance(row_buffer, bytes):
            row_buffer = io.BytesIO(row_buffer)

        for field in self.paramdef.fields:

            if field.bit_size < 8:
                field_value = self.bit_field.unpack(row_buffer, field.bit_size)
                self.fields[field.name] = bool(field_value) if field.bit_size == 1 else field_value
            elif field.internal_type == "dummy8":
                self.bit_field.clear()
                field_value = row_buffer.read(field.size)
                if not field_value == b"\0" * field.size:
                    # TODO: Canonize these exceptions.
                    if self.paramdef.param_type == "CHARMAKEMENUTOP_PARAM_ST" and field.name == "reserved[11]":
                        continue  # identified exception
                    elif self.paramdef.param_type == "DECAL_PARAM_ST" and field.name == "pad_00[14]":
                        continue  # identified exception
                    elif self.paramdef.param_type == "GEM_GEN_PARAM_ST" and field.name == "pad_1[3]":
                        continue  # identified exception
                    elif self.paramdef.param_type == "SP_EFFECT_PARAM_ST" and field.name == "pad3[2]":
                        continue  # identified exception
                    else:
                        raise ValueError(
                            f"Pad value of field {field.name} in row {self.name} of Param {self.paramdef.param_type} "
                            f"is not null: {field_value}."
                        )
                self.fields[field.name] = field_value
            elif field.internal_type == "fixstr":
                self.bit_field.clear()
                self.fields[field.name] = row_buffer.read(field.size).decode("shift_jis_2004")
            elif field.internal_type == "fixstrW":
                self.bit_field.clear()
                self.fields[field.name] = row_buffer.read(field.size).decode("utf-16-le")
            else:
                self.bit_field.clear()
                try:
                    field_type = self.get_field_type(field)
                except AttributeError:
                    raise KeyError(
                        f"Field {field.name} in Param {self.paramdef.param_type} has unknown "
                        f"internal type {field.internal_type} (debug type = {field.debug_type})."
                    )
                data = row_buffer.read(field_type.size())
                try:
                    (field_value,) = struct.unpack(field_type.format(), data)
                except struct.error as e:
                    if field.debug_name in {"inverseToneMapMul", "sfxMultiplier"}:
                        # These fields are screwed up in m99 and default ToneMapBank.
                        field_value = 1.0
                    else:
                        print(data, field_type)
                        raise ValueError(
                            f"Could not unpack data for field {field}.\n"
                            f"Field type: {field_type}; Raw bytes: {data}\n"
                            f"Error:\n{str(e)}"
                        )
                self.fields[field.name] = bool(field_value) if field.bit_size == 1 else field_value

    def load_dict(self, data: dict):
        for field in self.paramdef.fields:
            if field.bit_size < 8:
                self.fields[field.name] = data.get(field.name, field.new_default)
            elif field.internal_type == "dummy8":  # null bytes
                # TODO: The exceptions identified in `unpack()` will be overridden with nulls. Probably fine.
                data.pop(field.name, None)
                self.fields[field.name] = b"\0" * field.size
            else:
                self.fields[field.name] = data.get(field.name, field.new_default)

    def pack(self):
        packed_row = b""
        for field_name, field_value in self.fields.items():  # These are ordered correctly already.
            field = self.paramdef[field_name]
            if field.bit_size < 8:
                # Add bits.
                completed_byte = self.bit_field.pack(field_value, field.bit_size)
                if completed_byte is not None:
                    packed_row += struct.pack("<B", completed_byte)
                continue
            completed_byte = self.bit_field.pad()
            if completed_byte is not None:
                packed_row += struct.pack("<B", completed_byte)
            if field.internal_type == "dummy8":
                # Write nulls.
                packed_row += b"\x00" * field.size
                continue
            try:
                field_type = self.get_field_type(field)
            except AttributeError:
                raise ParamError(
                    f"Field {field.name} in ParamTable {self.paramdef.param_type} has unknown "
                    f"internal type {field.internal_type} (debug type = {field.debug_type})."
                )
            if not isinstance(self[field.name], field_type.python_type()):
                raise ParamError(
                    f"Bad type: field {field.name} in row {repr(self.name)} of table "
                    f"{self.paramdef.param_type} has value {self[field.name]} with type "
                    f"{type(self[field.name])}, but should have type {field_type.python_type()}."
                )
            if not field_type.minimum() <= self[field.name] <= field_type.maximum():
                _LOGGER.error(f"Error in field. Field data: {field}")
                raise ParamError(
                    f"Invalid: field {field.name} in row {repr(self.name)} of table "
                    f"{self.paramdef.param_type} has out-of-range value {self[field.name]} "
                    f"(range is {field_type.minimum()} to {field_type.maximum()})."
                )
            packed_row += struct.pack(field_type.format(), field_value)

        return packed_row

    def to_dict(self) -> dict[str, tp.Any]:
        data = {"name": self.name}
        for field in self.paramdef.fields:
            if field.internal_type == "dummy8":
                continue  # pad bytes not written
            if self.fields[field.name] == field.new_default:
                continue  # default values not written
            data[field.name] = self.fields[field.name]
        return data


class Param(GameFile, abc.ABC):
    """This base class supports all binary versions, but lacks information about game-specific enums, etc."""

    ParamRow = ParamRow
    GET_BUNDLED: tp.Callable = None

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
            self._paramdef_bnd = self.GET_BUNDLED()
        elif isinstance(paramdef_bnd, ParamDefBND):
            self._paramdef_bnd = paramdef_bnd
        else:
            raise TypeError(
                f"`paramdef_bnd` must be None or an existing `ParamDefBND` instance, not {type(paramdef_bnd)}."
            )
        self.param_type = ""  # internal name (shift_jis_2004) with capitals and underscores
        self.byte_order = "<"
        self.unknown = 0
        self.paramdef_data_version = 0
        self.paramdef_format_version = 0
        self.undecodable_row_names = undecodable_row_names

        self.rows = {}

        super().__init__(param_source, dcx_magic=dcx_magic)

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

        self.rows = {}
        for i, row in data["rows"].items():
            try:
                i = int(i)
            except (ValueError, TypeError):
                raise KeyError(f"All keys of `Param` dict must be integers, not {i}.")
            if isinstance(row, self.ParamRow):
                self.rows[i] = row
            else:
                try:
                    self.rows[i] = self.ParamRow(row, paramdef=self._paramdef_bnd[self.param_type])
                except Exception as ex:
                    raise ValueError(f"Could not interpret value of `rows[{i}]` as a `ParamRow`. Error: {ex}")

    def __getitem__(self, row_id):
        if row_id in self.rows:
            return self.rows[row_id]
        raise KeyError(f"No row with ID {row_id} in {self.param_type}.")

    def __setitem__(self, row_index, row):
        if isinstance(row, dict):
            if "name" not in row:
                raise ValueError("New row must have a 'name' field.")
            row = self.ParamRow(row, self._paramdef_bnd[self.param_type])
        if isinstance(row, self.ParamRow):
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

    def unpack(self, buffer, **kwargs):
        self.byte_order = ">" if unpack_from_buffer(buffer, "B", 44)[0] == 255 else "<"
        version_info = unpack_from_buffer(buffer, f"{self.byte_order}bbb", 45)
        self.flags1 = ParamFlags1(version_info[0])
        self.flags2 = ParamFlags2(version_info[1])
        self.paramdef_format_version = version_info[2]
        header_struct = self.GET_HEADER_STRUCT(self.flags1, self.byte_order)
        header = header_struct.unpack(buffer)
        try:
            self.param_type = header["param_type"]
        except KeyError:
            self.param_type = read_chars_from_buffer(buffer, offset=header["param_type_offset"], encoding="utf-8")
        self.paramdef_data_version = header["paramdef_data_version"]
        self.unknown = header["unknown"]
        # Row data offset in header not used. (It's an unsigned short, yet doesn't limit row count to 5461.)
        name_data_offset = header["name_data_offset"]  # CANNOT BE TRUSTED IN VANILLA FILES! Off by +12 bytes.

        # Load row pointer data.
        if self.flags1.LongDataOffset:
            row_pointers = self.ROW_STRUCT_64.unpack_count(buffer, count=header["row_count"])
        else:
            row_pointers = self.ROW_STRUCT_32.unpack_count(buffer, count=header["row_count"])
        row_data_offset = buffer.tell()  # Reliable row data offset.

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

        # Note that we no longer need to track buffer offset.
        name_encoding = self.get_name_encoding()
        for row_struct in row_pointers:
            buffer.seek(row_struct["data_offset"])
            row_data = buffer.read(row_size)
            if row_struct["name_offset"] != 0:
                try:
                    name = read_chars_from_buffer(
                        buffer,
                        offset=row_struct["name_offset"],
                        encoding=name_encoding,
                        reset_old_offset=False,  # no need to reset
                    )
                except UnicodeDecodeError as ex:
                    if ex.object in self.undecodable_row_names:
                        name = read_chars_from_buffer(
                            buffer,
                            offset=row_struct["name_offset"],
                            encoding=None,
                            reset_old_offset=False,  # no need to reset
                        )
                    else:
                        raise
                except ValueError:
                    buffer.seek(row_struct["name_offset"])
                    _LOGGER.error(
                        f"Error encountered while parsing row name string in {self.param_type}.\n"
                        f"    Header: {header}\n"
                        f"    Row Struct: {row_struct}\n"
                        f"    30 chrs of name data: {' '.join(f'{{:02x}}'.format(x) for x in buffer.read(30))}"
                    )
                    raise
            else:
                name = ""
            self.rows[row_struct["id"]] = self.ParamRow(row_data, self.paramdef, name=name)

    def pack(self, sort=True):
        # if len(self.entries) > 5461:
        #     raise SoulstructError(
        #         f"Param {self.param_type} has {len(self.entries)} entries, which is more than a "
        #         f"DS1 Param can store (5461). Remove some entries before packing it.")

        sorted_entries = sorted(self.rows.items()) if sort else self.rows.items()

        current_name_offset = 0
        name_offset_list = []
        data_offset = 0
        data_offset_list = []
        packed_names = b""
        packed_data = b""
        name_encoding = self.get_name_encoding()

        for row_id, row in sorted_entries:

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
            raise NotImplementedError(f"Soulstruct cannot current pack this version of `Param`, sorry!")
        row_pointer_struct = self.ROW_STRUCT_64 if self.flags1.LongDataOffset else self.ROW_STRUCT_32
        row_pointers_offset = header_struct.size
        row_data_offset = row_pointers_offset + row_pointer_struct.size * len(sorted_entries)
        name_data_offset = row_data_offset + len(packed_data)

        # Entries.
        row_pointer_data = b""
        for i, (row_id, _) in enumerate(sorted_entries):
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
            row_count=len(sorted_entries),
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

    def to_dict(self):
        data = {
            "param_type": self.param_type,
            "big_endian": True if self.byte_order == ">" else False,
            "unknown": self.unknown,
            "paramdef_data_version": self.paramdef_data_version,
            "paramdef_format_version": self.paramdef_format_version,
            "undecodable_row_names": self.undecodable_row_names,
            "rows": {},
        }
        for i, row in self.rows.items():
            data["rows"][i] = row.to_dict()
        return data

    def get_range(self, start, count):
        return [(param_id, self[param_id]) for param_id in sorted(self.rows)[start: start + count]]

    def get_name_encoding(self):
        if self.flags2.UnicodeRowNames:
            return "utf-16-be" if self.byte_order == ">" else "utf-16-le"
        else:
            return "shift_jis_2004"
