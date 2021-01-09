from __future__ import annotations

__all__ = ["ParamDefField", "ParamDef", "ParamDefBND"]

import abc
import io
import logging
import typing as tp

from soulstruct.bnd import BND, BNDEntry
from soulstruct.game_file import GameFile, InvalidGameFileTypeError
from soulstruct.games import *
from soulstruct.utilities import read_chars_from_buffer, PACKAGE_PATH
from soulstruct.utilities.binary_struct import BinaryStruct

if tp.TYPE_CHECKING:
    from soulstruct.params.base.param import ParamRow

_LOGGER = logging.getLogger(__name__)


class ParamDefField(abc.ABC):
    """Information about a single field in a ParamTable."""

    STRUCT: BinaryStruct = None

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

    def __init__(self, field_struct: dict, index: int, description: str, param_name: str, debug_name: str = None):
        self.field_index = index
        self.name = field_struct["name"]
        self.description = description
        self.size = field_struct["size"]
        self.internal_type = field_struct["internal_type"]
        self.param_name = param_name

        self.debug_name = field_struct["debug_name"] if debug_name is None else debug_name
        self.debug_type = field_struct["debug_type"]
        self.debug_format = field_struct["debug_format"]

        self.default = field_struct["default"]
        self.minimum = field_struct["minimum"]
        self.maximum = field_struct["maximum"]
        self.increment = field_struct["increment"]

        self.debug_display = bool(field_struct["debug_display"])
        self.sort_id = field_struct["sort_id"]

        self.bit_size = self.get_bit_size(self.name, self.internal_type, self.size)

        self.new_default = self.get_default_value()

    @abc.abstractmethod
    def get_display_info(self, entry: ParamRow):
        """Get display info from game-specific `params.display_info` subpackage."""

    def get_default_value(self):
        """Get default value from game-specific `defaults` module, if specified."""
        if self.bit_size == 1 and self.internal_type != "dummy8":
            return bool(self.default)
        elif self.internal_type not in {"f32", "f64"}:
            return int(self.default)
        return self.default  # float

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
                    encoding="utf-16-le" if unicode else "shift_jis_2004",
                )
            else:
                field_description = ""
            if "debug_name_offset" in field_struct:
                debug_name = read_chars_from_buffer(
                    paramdef_buffer,
                    offset=field_struct["debug_name_offset"],
                    encoding="utf-16-le",
                )
            else:
                debug_name = field_struct["debug_name"]
            fields.append(cls(field_struct, field_index, field_description, param_name, debug_name=debug_name))
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


class ParamDef(GameFile, abc.ABC):

    STRUCT: BinaryStruct = None
    BYTE_ORDER: str = None
    FIELD_CLASS: tp.Type[ParamDefField] = None

    def __init__(self, paramdef_source, dcx_magic=(), param_type=None):
        """Defines the row fields in a particular type of `Param`.

        No pack/write methods; these are essentially hard-coded definitions for each game, and therefore read-only. If
        you want to modify them, you are too powerful a modder for Soulstruct.
        """

        self.param_type = None
        self.paramdef_path = None
        self.fields = []
        self.byte_order = "<"
        self.data_version = 0
        self.format_version = 104  # defaults to Dark Souls 1
        self.unicode = False  # `ParamEntry` description encoding
        super().__init__(paramdef_source, dcx_magic, param_type=param_type)

    def _handle_other_source_types(self, file_source, param_type=None) -> tp.Optional[io.BufferedIOBase]:

        if isinstance(file_source, (tuple, list)) and all(isinstance(p, self.FIELD_CLASS) for p in file_source):
            if param_type is None:
                raise ValueError("`param_type` must be given to `ParamDef` if a list of `ParamDefField`s is passed.")
            self.param_type = param_type
            self.fields = file_source
            return

        if isinstance(file_source, BNDEntry):
            return io.BytesIO(file_source.data)

        raise InvalidGameFileTypeError("`paramdef_source` is not a list of `ParamDefField`s or a `BNDEntry`.")

    def unpack(self, paramdef_buffer, **kwargs):
        """Convert a paramdef file to a dictionary, indexed by ID."""
        header = self.STRUCT.unpack(paramdef_buffer)
        if "param_name" in header:
            self.param_type = header["param_name"]
        else:
            self.param_type = read_chars_from_buffer(
                paramdef_buffer, offset=header["param_name_offset"], encoding="shift_jis_2004",  # never unicode
            )
        self.data_version = header["data_version"]
        self.unicode = header["unicode"]
        self.fields = self.FIELD_CLASS.unpack_fields(
            self.param_type, paramdef_buffer, header["field_count"], self.format_version, self.unicode, self.byte_order,
        )

    def pack(self):
        raise AttributeError("Cannot pack `ParamDef`.")

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

    def verbose(self):
        return f"ParamDef {self.param_type}:\n  " + "\n  ".join(
            [f"{field.field_index:>3d} | {field.debug_name} | {field.description}\n"
             f"      field_index = {field.field_index}\n"
             f"      name = {field.name}\n"
             f"      description = {field.description}\n"
             f"      size = {field.size}\n"
             f"      internal_type = {field.internal_type}\n"
             f"      param_name = {field.param_name}\n"
             f"      debug_name = {field.debug_name}\n"
             f"      debug_type = {field.debug_type}\n"
             f"      debug_format = {field.debug_format}\n"
             f"      default = {field.new_default}\n"
             f"      minimum = {field.minimum}\n"
             f"      maximum = {field.maximum}\n"
             f"      increment = {field.increment}\n"
             f"      debug_display = {field.debug_display}\n"
             f"      sort_id = {field.sort_id}\n"
             f"      bit_size = {field.bit_size}\n"
             for field in self.fields]
        )

    @property
    @abc.abstractmethod
    def param_info(self) -> tp.Optional[dict]:
        """Get param info from game-specific `params.display_info` subpackage."""


class ParamDefBND(abc.ABC):

    PARAMDEF_CLASS: tp.Type[ParamDef] = None
    GAME: Game = None

    def __init__(self, paramdef_bnd_source=None):
        """BND container with all the `ParamDef` definitions for a given game.

        The latest versions of these files are included with Soulstruct for some games, and can be loaded simply by
        passing the game name to this constructor. They will also be loaded automatically when needed by `Param`
        instances.

        If you want to modify a `ParamDefBND`, you are far too powerful a modder for Soulstruct, and I cannot make that
        journey with you at this time.
        """
        if paramdef_bnd_source is None:
            paramdef_bnd_source = self.GAME
        elif isinstance(paramdef_bnd_source, str):
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

        self.paramdefs = {}  # type: dict[str, ParamDef]
        for entry in self.bnd.entries:
            try:
                paramdef = self.PARAMDEF_CLASS(entry)
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
