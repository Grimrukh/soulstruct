from __future__ import annotations

__all__ = ["ParamDefField", "ParamDef", "ParamDefBND"]

import io
import logging
import typing as tp
from pathlib import Path

from soulstruct.bnd import BND, BNDEntry
from soulstruct.games import *
from soulstruct.params.shared.display_info import get_param_info, get_param_info_field
from soulstruct.utilities import BinaryStruct, unpack_from_buffer, read_chars_from_buffer, PACKAGE_PATH

if tp.TYPE_CHECKING:
    from soulstruct.params.base.param import ParamRow

_LOGGER = logging.getLogger(__name__)


class ParamDefField:
    """Information about a single field in a ParamTable."""

    @staticmethod
    def GET_FIELD_STRUCT(format_version, unicode, byte_order="<"):
        fields = [
            ("debug_name", "64u" if unicode else "64j"),
            ("debug_type", "8j"),
            ("debug_format", "8j"),  # %i, %u, %d, etc.
            ("default", "f"),
            ("minimum", "f"),
            ("maximum", "f"),
            ("increment", "f"),
            ("debug_display", "i"),
            ("size", "i"),
            ("description_offset", "q" if format_version >= 200 else "i"),
            ("internal_type", "32j"),  # could be an enum name (see params.enums)
            ("name", "32j"),
        ]
        if format_version >= 202:
            fields[0] = ("debug_name_offset", "q")
        if format_version >= 104:
            fields.append(("sort_id", "i"))
        if format_version >= 200:
            fields.append("28x")
        return BinaryStruct(*fields, byte_order=byte_order)

    def __init__(self, field_struct: dict, index: int, description: str, param_name: str):
        self.field_index = index
        self.name = field_struct["name"]
        self.description = description
        self.size = field_struct["size"]
        self.internal_type = field_struct["internal_type"]
        self.param_name = param_name

        self.debug_name = field_struct["debug_name"]
        self.debug_type = field_struct["debug_type"]
        self.debug_format = field_struct["debug_format"]

        self.default = field_struct["default"]
        self.minimum = field_struct["minimum"]
        self.maximum = field_struct["maximum"]
        self.increment = field_struct["increment"]

        self.debug_display = field_struct["debug_display"]
        self.sort_id = field_struct["sort_id"]

        self.bit_size = self.get_bit_size(self.name, self.internal_type, self.size)

    def get_display_info(self, entry: ParamRow):
        try:
            field_info = get_param_info_field(self.param_name, self.name)
        except ValueError:
            raise ValueError(f"No display information given for field '{self.name}'.")
        return field_info(entry)

    @classmethod
    def unpack_fields(
        cls,
        param_name: str,
        paramdef_buffer: io.BytesIO,
        field_count: int,
        format_version: int,
        unicode: bool,
        byte_order: str,
    ):
        """Buffer should be at the start of the packed fields (which are followed by the packed descriptions)."""
        field_structs = cls.GET_FIELD_STRUCT(format_version, unicode, byte_order).unpack_count(
            paramdef_buffer, count=field_count,
        )
        fields = []
        for field_index, field_struct in enumerate(field_structs):
            if field_struct["description_offset"] != 0:
                field_description = read_chars_from_buffer(
                    paramdef_buffer,
                    offset=field_struct["description_offset"],
                    encoding="utf-16-le" if unicode else "shift-jis",
                )
            else:
                field_description = ""
            fields.append(cls(field_struct, field_index, field_description, param_name))
        return fields

    @staticmethod
    def get_bit_size(name, internal_type, size):
        is_bits = name.find(": ")
        if is_bits == -1:
            is_bits = name.find(":")
        if is_bits != -1:
            try:
                return int(name[is_bits + 1])
            except ValueError:
                return int(name[is_bits + 2])
        elif internal_type == "dummy8":
            is_pad = name.find("[")
            if is_pad != -1:
                return int(name[is_pad + 1]) * 8
            else:
                return 8
        else:
            return size * 8


class ParamDef:
    BYTE_ORDER_OFFSET = 44
    FORMAT_VERSION_OFFSET = 46
    FIELD_SIZES = {  # maps format version to (asserted) field size
        101: 140,
        102: 172,
        103: 108,  # NOTE: asserted value is incorrect
        104: 176,
        201: 208,
        202: 104,
    }

    @classmethod
    def GET_HEADER_STRUCT(cls, format_version, byte_order="<"):
        fields = [
            ("size", "i"),
            ("header_size", "H", 255 if format_version >= 200 else 48),
            ("data_version", "H"),
            ("field_count", "H"),
            ("field_size", "H", cls.FIELD_SIZES[format_version]),
        ]
        if format_version >= 202:
            fields += [
                "4x",
                ("param_name_offset", "q"),
                "20x",
            ]
        else:
            fields.append(("param_name", "32j"))
        fields += [
            ("big_endian", "B"),
            ("unicode", "?"),
            ("format_version", "h", format_version),
        ]
        if format_version >= 200:
            fields.append(("unk1", "q", 56))
        return BinaryStruct(*fields, byte_order=byte_order)

    def __init__(self, paramdef_source, param_type=None):
        """Defines the row fields in a particular type of `Param`.

        No pack/write methods; these are essentially hard-coded definitions for each game, and therefore read-only. If
        you want to modify them, you are too powerful a modder for Soulstruct.
        """

        self.param_type = None
        self.paramdef_path = None
        self.fields = []
        self.param_info = {}
        self.byte_order = "<"
        self.data_version = 0
        self.format_version = 104  # defaults to Dark Souls 1
        self.unicode = False  # `ParamEntry` description encoding

        if isinstance(paramdef_source, list) and all(isinstance(p, ParamDefField) for p in paramdef_source):
            if param_type is None:
                raise ValueError("`param_type` must be given to `ParamDef` if a list of `ParamDefField`s is passed.")
            self.param_type = param_type
            self.fields = paramdef_source

        elif isinstance(paramdef_source, bytes):
            self.unpack(io.BytesIO(paramdef_source))

        elif isinstance(paramdef_source, str):
            self.paramdef_path = Path(paramdef_source)
            with self.paramdef_path.open("rb") as file:
                self.unpack(file)

        elif isinstance(paramdef_source, BNDEntry):
            self.unpack(io.BytesIO(paramdef_source.data))

        else:
            raise TypeError(f"Invalid `paramdef_source` type: {type(paramdef_source)}")

        try:
            self.param_info = get_param_info(self.param_type)
        except KeyError:
            # This param has no extra information.
            self.param_info = None

    def unpack(self, paramdef_buffer):
        """Convert a paramdef file to a dictionary, indexed by ID."""
        self.byte_order = ">" if unpack_from_buffer(paramdef_buffer, "B", self.BYTE_ORDER_OFFSET)[0] == 255 else "<"
        self.format_version = unpack_from_buffer(paramdef_buffer, f"{self.byte_order}h", self.FORMAT_VERSION_OFFSET)[0]
        header = self.GET_HEADER_STRUCT(self.format_version, self.byte_order).unpack(paramdef_buffer)
        try:
            self.param_type = header["param_name"]
        except KeyError:
            self.param_type = read_chars_from_buffer(
                paramdef_buffer, offset=header["param_name_offset"], encoding="shift-jis",
            )
        self.data_version = header["data_version"]
        self.unicode = header["unicode"]
        self.fields = ParamDefField.unpack_fields(
            self.param_type, paramdef_buffer, header["field_count"], self.format_version, self.unicode, self.byte_order,
        )

    def __getitem__(self, field_name) -> ParamDefField:
        hits = [field for field in self.fields if field.name == field_name]
        if len(hits) >= 2:
            raise AttributeError(
                f"Field {field_name} appears more than once in ParamDef.\n"
                "This should NOT happen unless you've edited the ParamDef for some ungodly reason."
            )
        elif not hits:
            print([f.name for f in self.fields])
            raise AttributeError(f"Field {field_name} does not exist in ParamDef.")
        return hits[0]

    def __repr__(self):
        return f"ParamDef {self.param_type}:\n  " + "\n  ".join(
            [f"{field.field_index:>3d} | {field.debug_name} | {field.description}" for field in self.fields]
        )


class ParamDefBND:
    def __init__(self, paramdef_bnd_source):
        """BND container with all the `ParamDef` definitions for a given game.

        The latest versions of these files are included with Soulstruct for some games, and can be loaded simply by
        passing the game name to this constructor. They will also be loaded automatically when needed by `Param`
        instances.

        If you want to modify a `ParamDefBND`, you are far too powerful a modder for Soulstruct, and I cannot make that
        journey with you at this time.
        """

        if isinstance(paramdef_bnd_source, str):
            try:
                paramdef_bnd_source = get_game(paramdef_bnd_source)
            except ValueError:
                # Will try to use as a path.
                pass

        if isinstance(paramdef_bnd_source, Game):
            # Load vanilla ParamDefBND bundled with Soulstruct (easiest).
            if not paramdef_bnd_source.bundled_paramdef_path:
                raise NotImplementedError(
                    f"Soulstruct does not have a bundled `paramdefbnd` file for game {paramdef_bnd_source.name}."
                )
            paramdef_bnd_source = PACKAGE_PATH(paramdef_bnd_source.bundled_paramdef_path)
            if not paramdef_bnd_source.is_file():
                raise FileNotFoundError(
                    f"Could not find bundled `paramdefbnd` file for game {paramdef_bnd_source.name} in Soulstruct.\n"
                    "Update/reinstall Soulstruct or copy the ParamDef files in yourself."
                )

        self._bnd = BND(paramdef_bnd_source)

        self.paramdefs = {}
        for entry in self.bnd.entries:
            try:
                paramdef = ParamDef(entry)
            except Exception as ex:
                raise ValueError(f"Could not load ParamDefBND entry {entry.name}. Error: {ex}")
            if paramdef.param_type in self.paramdefs:
                raise KeyError(f"ParamDef type {paramdef.param_type} was loaded more than once in ParamDefBND.")
            self.paramdefs[paramdef.param_type] = paramdef

    def __getitem__(self, param_type) -> ParamDef:
        try:
            return self.paramdefs[param_type]
        except KeyError:
            raise KeyError(
                f"No ParamDef with type {param_type}. The available types are:\n    {list(self.paramdefs)}")

    @property
    def bnd(self):
        return self._bnd
