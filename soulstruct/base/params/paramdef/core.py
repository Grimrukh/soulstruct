from __future__ import annotations

__all__ = ["ParamDef"]

import logging
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path
from xml.etree import ElementTree

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *

from .paramdef_field import ParamDefField

try:
    Self = tp.Self
except AttributeError:
    Self = "ParamDef"

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class ParamDef(GameFile):

    # NOTE: TK notes that this value is wrong for `format_version` 103 (DeS, presumably).
    _EXPECTED_FIELD_SIZES: tp.ClassVar[dict[int, int]] = {
        101: 0x8C,  # Enchanted Arms, Chromehounds, Armored Core 4/For Answer/V/Verdict Day, Shadow Assault: Tenchu
        102: 0xAC,  # Demon's Souls
        103: 0x6C,  # Ninja Blade, Another Century's Episode: R
        104: 0xB0,  # Dark Souls, Steel Battalion: Heavy Armor
        106: 0x48,  # Elden Ring (deprecated ObjectParam)
        201: 0xD0,  # Bloodborne
        202: 0x68,  # Dark Souls 3
        203: 0x88,  # Elden Ring
    }

    EXT: tp.ClassVar[str] = ".paramdef"

    param_type: str = ""  # e.g. 'NPC_PARAM_ST'

    fields: dict[str, ParamDefField] = field(default_factory=dict)

    # Format info.
    big_endian: bool = False
    unicode: bool = False
    data_version: int = 0
    format_version: int = 104  # Dark Souls 1 default (TODO: game subclass override)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:
        """Unpack `ParamDef` from reader.

        NOTE: `ParamDef structure is just flexible enough (based on `format_version` to make `BinaryStruct difficult,
        and we don't want game subclasses for it, so this just uses old-fashioned reader logic.
        """

        byte_order = ByteOrder.BigEndian if reader.unpack_value("b", offset=0x2c) == -1 else ByteOrder.LittleEndian
        format_version = reader.unpack_value("h", offset=0x2e)
        reader.default_byte_order = byte_order
        reader.long_varints = format_version >= 200

        reader.read(4)  # file size
        header_size = reader.unpack_value("h")
        if (format_version < 200 and header_size != 0x30) or (format_version >= 200 and header_size != 0xFF):
            raise ValueError(f"Invalid `ParamDef` header size {header_size} for format version {format_version}.")
        data_version = reader.unpack_value("h")
        field_count = reader.unpack_value("h")
        field_size = reader.unpack_value("h")
        if field_size != (expected := cls._EXPECTED_FIELD_SIZES[format_version]):
            raise ValueError(f"Expected `ParamDef` field size of {hex(expected)} for format version {format_version}.")

        if format_version >= 202:
            reader.assert_pad(4)
            param_type_offset = reader.unpack_value("q")
            param_type = reader.unpack_string(offset=param_type_offset, encoding="ASCII")
            reader.assert_pad(20)
        elif 106 <= format_version < 200:
            param_type_offset = reader.unpack_value("i")
            param_type = reader.unpack_string(offset=param_type_offset, encoding="ASCII")
            reader.assert_pad(28)
        else:
            param_type = reader.unpack_string(length=32, encoding="shift_jis_2004")

        reader.read(1)  # big endian
        unicode = reader.unpack_value("?")
        reader.read(2)  # format version
        if format_version >= 200:
            if reader.unpack_value("q") != 0x38:
                raise ValueError(f"Asserted value 0x38 did not appear in`ParamDef` header ({format_version=}).")

        fields_list = [
            ParamDefField.from_paramdef_reader(reader, i, param_type, format_version, unicode)
            for i in range(field_count)
        ]
        fields = {f.name: f for f in fields_list}

        return cls(
            param_type=param_type,
            fields=fields,
            big_endian=ByteOrder == ByteOrder.BigEndian,
            unicode=unicode,
            data_version=data_version,
            format_version=format_version,
        )

    @classmethod
    def from_paramdex_xml(cls, xml_path: Path | str) -> Self:
        root = ElementTree.parse(xml_path).getroot()

        # Find `ParamType` tag first.
        for child in root:
            if child.tag == "ParamType":
                param_type = child.text
                break
        else:
            raise ValueError(f"Could not find `ParamType` tag in Paramdex XML: {xml_path}")

        kwargs = {}
        for child in root:
            if child.tag == "ParamType":
                continue  # already read
            if child.tag == "DataVersion":
                kwargs["data_version"] = int(child.text)
            elif child.tag == "BigEndian":
                kwargs["big_endian"] = bool(child.text)
            elif child.tag == "Unicode":
                kwargs["unicode"] = bool(child.text)
            elif child.tag == "FormatVersion":
                kwargs["format_version"] = int(child.text)
            elif child.tag == "Fields":
                fields = [ParamDefField.from_paramdex_xml(i, node, param_type) for i, node in enumerate(child)]
                kwargs["fields"] = {f.name: f for f in fields}
            else:
                raise ValueError(f"Unknown Paramdex XML tag: {child.tag}")
        paramdef = cls(param_type=param_type, **kwargs)
        paramdef.path = Path(xml_path)
        return paramdef

    @classmethod
    def from_field_sequence(cls, fields: tp.Sequence[ParamDefField], param_type: str) -> Self:
        """NOTE: Version fields will be set to their defaults (which should be fine for this game class)."""
        fields_dict = {f.name: f for f in fields}
        if len(fields) != len(fields_dict):
            raise ValueError("One or more fields was repeated in list of `ParamDefField`s given to `ParamDef`.")
        return cls(param_type=param_type, fields=fields_dict)

    def to_writer(self) -> BinaryWriter:
        raise TypeError("Cannot pack `ParamDef` to binary. Are you trying to make your own FromSoftware game...?")

    def __getitem__(self, field_name) -> ParamDefField:
        """Access field by name."""
        try:
            return self.fields[field_name]
        except KeyError:
            print(self)
            raise

    def __repr__(self):
        return f"ParamDef {self.param_type}:\n  " + "\n  ".join(f"{f.index:>3d}: {f}" for f in self.fields.values())

    def verbose(self):
        return f"ParamDef {self.param_type}:\n  " + "\n  ".join(
            [f"{f.index:>3d} | {f.display_name} | {f.description}\n"
             f"      index = {f.index}\n"
             f"      name = {f.name}\n"
             f"      description = {f.description}\n"
             f"      size = {f.size}\n"
             f"      internal_type = {f.internal_type_name}\n"
             f"      param_type = {f.param_type}\n"
             f"      display_name = {f.display_name}\n"
             f"      display_type = {f.display_type}\n"
             f"      display_format = {f.display_format}\n"
             f"      default = {f.py_default}\n"
             f"      minimum = {f.minimum}\n"
             f"      maximum = {f.maximum}\n"
             f"      increment = {f.increment}\n"
             f"      edit_flags = {f.edit_flags}\n"
             f"      sort_id = {f.sort_id}\n"
             f"      bit_count = {f.bit_count}\n"
             for f in self.fields.values()]
        )
