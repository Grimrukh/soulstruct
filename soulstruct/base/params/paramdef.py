from __future__ import annotations

__all__ = ["ParamDefField", "ParamDef", "ParamDefBND"]

import abc
import logging
import math
import re
import typing as tp
from enum import IntEnum

from soulstruct.base.binder_entry import BinderEntry
from soulstruct.base.game_file import GameFile, InvalidGameFileTypeError
from soulstruct.containers import Binder
from soulstruct.exceptions import SoulstructError
from soulstruct.games import *
from soulstruct.utilities.binary import BinaryStruct, BinaryReader
from soulstruct.utilities.files import PACKAGE_PATH

from . import field_types
from .exceptions import ParamError

if tp.TYPE_CHECKING:
    from .param import ParamRow

_LOGGER = logging.getLogger(__name__)


class ParamDefError(SoulstructError):
    pass


class ParamDefField(abc.ABC):
    """Information about a single field in a ParamTable."""

    _ARRAY_LENGTH_RE = re.compile(r"^\s*.+\s*\[\s*(\d+)\s*]\s*$")
    _BIT_SIZE_RE = re.compile(r"^\s*.+\s*:\s*(\d+)\s*$")

    class EditType(IntEnum):
        DoesNotWrap = 0
        Wraps = 1
        Locked = 4
        Unknown = 5  # appears in Attack Param hitbox priority fields and some Item Lot Param fields

    @staticmethod
    def GET_FIELD_STRUCT(format_version, unicode, byte_order="<"):
        """Different `Param` entries in a `GameParamBND` can have different headers, so this detection method is
        better than fixed game-specific structs."""
        fields = [
            ("display_name_offset", "q") if format_version >= 202 else ("display_name", "64u" if unicode else "64j"),
            ("display_type", "8j"),
            ("display_format", "8j"),  # %i, %u, %d, etc.
            ("default", "f"),
            ("minimum", "f"),
            ("maximum", "f"),
            ("increment", "f"),
            ("edit_type", "i"),
            ("size", "i"),
            ("description_offset", "q" if format_version >= 200 else "i"),
            ("internal_type", "32j"),  # could be an enum name (see params.enums)
            ("name", "32j"),
        ]
        if format_version >= 104:
            fields.append(("sort_id", "i"))
        if format_version >= 200:
            fields.append("28x")
        return BinaryStruct(*fields, byte_order=byte_order)

    def __init__(self, field_struct: dict, index: int, description: str, param_name: str, display_name: str = None):
        self.index = index
        self.param_name = param_name

        self.name = field_struct["name"]
        self.description = description
        self.size = field_struct["size"]  # in bytes
        self.internal_type = field_struct["internal_type"]

        self.display_name = field_struct["display_name"] if display_name is None else display_name
        self.display_type = field_struct["display_type"]
        self.display_format = field_struct["display_format"]

        self.default = field_struct["default"]
        self.minimum = field_struct["minimum"]
        self.maximum = field_struct["maximum"]
        self.increment = field_struct["increment"]

        self.edit_type = self.EditType(field_struct["edit_type"])
        self.sort_id = field_struct["sort_id"]

        try:
            self.type_class = getattr(field_types, self.display_type)  # type: tp.Type[field_types.base_type]
        except AttributeError:
            raise ParamDefError(f"Unknown field type '{self.display_type}' for field '{self.name}'.")
        self.fmt = self.type_class.format()
        self.py_type = self.type_class.python_type()
        self.type_min = self.type_class.minimum()
        self.type_max = self.type_class.maximum()

        self.length = self.size // self.type_class.size()  # number of values (>1 for padding only)
        if match := self._ARRAY_LENGTH_RE.match(self.name):
            if int(match.group(1)) != self.length:
                raise ParamDefError(
                    f"Length of field '{self.name}' calculated from byte size ({self.length}) does not match length "
                    f"implied by name: [{match.group(1)}]. This should NOT happen unless you have edited the ParamDef."
                )

        if match := self._BIT_SIZE_RE.match(self.name):
            self.bit_count = int(match.group(1))
        else:
            self.bit_count = -1  # does not use bit field

        self.new_default = self.get_default_value()

    @abc.abstractmethod
    def get_display_info(self, row: ParamRow):
        """Get display info from game-specific `params.display_info` subpackage."""

    def get_default_value(self) -> tp.Union[bool, int, float]:
        """Get default value from game-specific `defaults` module, if specified.

        Base class version here just parses the existing ParamDef default.
        """
        if self.bit_count == 1 and self.internal_type != "dummy8":
            return bool(self.default)
        elif self.internal_type not in {"f32", "f64"}:
            return int(self.default)
        return self.default  # float

    @classmethod
    def unpack_fields(
        cls,
        param_name: str,
        paramdef_reader: BinaryReader,
        field_count: int,
        format_version: int,
        unicode: bool,
        byte_order: str,
    ) -> dict[str, ParamDefField]:
        """Buffer should be at the start of the packed fields (which are followed by the packed descriptions)."""
        field_structs = paramdef_reader.unpack_structs(
            cls.GET_FIELD_STRUCT(format_version, unicode, byte_order), count=field_count
        )
        fields = {}
        for field_index, field_struct in enumerate(field_structs):
            if field_struct["description_offset"] != 0:
                field_description = paramdef_reader.unpack_string(
                    offset=field_struct["description_offset"],
                    encoding="utf-16-le" if unicode else "shift_jis_2004",
                )
            else:
                field_description = ""
            if "display_name_offset" in field_struct:
                display_name = paramdef_reader.unpack_string(
                    offset=field_struct["display_name_offset"],
                    encoding="utf-16-le",
                )
            else:
                display_name = field_struct["display_name"]
            field = cls(field_struct, field_index, field_description, param_name, display_name=display_name)
            fields[field.name] = field
        return fields

    def check_python_type(self, value):
        """Check given `value` has the expected Python type of this field."""
        if self.type_class is field_types.dummy8 and self.bit_count == -1:
            if not isinstance(value, bytes):  # `dummy8` fields that are not bit fields are not unpacked
                raise ParamError(f"Value {value} of `dummy8` field {self.name} should be `bytes`, not {type(value)}.")
        elif not isinstance(value, self.py_type):
            raise ParamError(f"Value {value} of field {self.name} should have type {self.py_type}, not {type(value)}.")

    def check_range(self, value):
        """Some vanilla values are outside the ParamDef min/max, so we just check the range of the actual C type."""
        if self.type_class in {field_types.f32, field_types.f64} and math.isnan(value):
            return  # floats are allowed to be `nan`
        if self.type_class is field_types.dummy8 and self.bit_count == -1:
            return  # not unpacked
        if not (
            (self.type_min is None or self.type_min <= value)
            and (self.type_max is None or value <= self.type_max)
        ):
            raise ValueError(
                f"Value {value} of field {self.name} is outside range of its type: "
                f"[{self.type_min}, {self.type_max}]"
            )

    def validate(self, value: tp.Any):
        self.check_python_type(value)
        self.check_range(value)


class ParamDef(GameFile, abc.ABC):

    EXT = ".paramdefbnd"
    HEADER_STRUCT: BinaryStruct = None
    BYTE_ORDER: str = None
    FIELD_CLASS: tp.Type[ParamDefField] = None

    def __init__(self, paramdef_source, dcx_magic=(), param_type=None):
        """Defines the row fields in a particular type of `Param`.

        No pack/write methods; these are essentially hard-coded definitions for each game, and therefore read-only. If
        you want to modify them, you are too powerful a modder for Soulstruct.
        """

        self.param_type = None
        self.paramdef_path = None
        self.fields = {}  # type: dict[str, ParamDefField]
        self.data_version = 0
        self.format_version = 104  # defaults to Dark Souls 1
        self.unicode = False  # `ParamEntry` description encoding
        super().__init__(paramdef_source, dcx_magic, param_type=param_type)

    def _handle_other_source_types(self, file_source, param_type=None) -> tp.Optional[BinaryReader]:

        if isinstance(file_source, (tuple, list)):
            if param_type is None:
                raise ValueError("`param_type` must be given to `ParamDef` if a list of `ParamDefField`s is passed.")
            if not all(isinstance(p, self.FIELD_CLASS) for p in file_source):
                raise ValueError("At least one element in given list is not a `ParamDefField`.")
            self.param_type = param_type
            self.fields = {f.name: f for f in file_source}
            if len(self.fields) != len(file_source):
                raise ValueError("One or more fields was repeated in list of `ParamDefField`s.")
            return

        if isinstance(file_source, dict):
            if param_type is None:
                raise ValueError("`param_type` must be given to `ParamDef` if a list of `ParamDefField`s is passed.")
            if not all(isinstance(p, self.FIELD_CLASS) for p in file_source.values()):
                raise ValueError("At least one value in given dict is not a `ParamDefField`.")
            if not all(isinstance(p, str) for p in file_source.keys()):
                raise ValueError("At least one key in given dict is not a `str`.")
            for name, field in file_source.items():
                if name != field.name:
                    raise ValueError(f"Key '{name}' in dict different to `ParamDefField` value name '{field.name}'.")
            self.param_type = param_type
            self.fields = file_source.copy()
            return

        if isinstance(file_source, BinderEntry):
            return BinaryReader(file_source.get_uncompressed_data())

        raise InvalidGameFileTypeError("`paramdef_source` is not a list of `ParamDefField`s or a `BinderEntry`.")

    def unpack(self, paramdef_reader: BinaryReader, **kwargs):
        """Convert a paramdef file to a dictionary, indexed by ID."""
        header = paramdef_reader.unpack_struct(self.HEADER_STRUCT)
        if "param_name" in header:
            self.param_type = header["param_name"]
        else:
            self.param_type = paramdef_reader.unpack_string(
                offset=header["param_name_offset"], encoding="shift_jis_2004",  # never unicode
            )
        self.data_version = header["data_version"]
        self.format_version = header["format_version"]
        self.unicode = header["unicode"]
        self.fields = self.FIELD_CLASS.unpack_fields(
            self.param_type, paramdef_reader, header["field_count"], self.format_version, self.unicode, self.BYTE_ORDER,
        )

    def pack(self):
        raise AttributeError("Cannot pack `ParamDef`.")

    def __getitem__(self, field_name) -> ParamDefField:
        try:
            return self.fields[field_name]
        except KeyError:
            print(self)
            raise

    def __repr__(self):
        return f"ParamDef {self.param_type}:\n  " + "\n  ".join(
            [f"{f.index:>3d} | {f.name} ({f.display_name}) | {f.internal_type} ({f.display_type}) | "
             f"{f.description}"
             for f in self.fields.values()]
        )

    def verbose(self):
        return f"ParamDef {self.param_type}:\n  " + "\n  ".join(
            [f"{f.index:>3d} | {f.display_name} | {f.description}\n"
             f"      index = {f.index}\n"
             f"      name = {f.name}\n"
             f"      description = {f.description}\n"
             f"      size = {f.size}\n"
             f"      internal_type = {f.internal_type}\n"
             f"      param_name = {f.param_name}\n"
             f"      display_name = {f.display_name}\n"
             f"      display_type = {f.display_type}\n"
             f"      display_format = {f.display_format}\n"
             f"      default = {f.new_default}\n"
             f"      minimum = {f.minimum}\n"
             f"      maximum = {f.maximum}\n"
             f"      increment = {f.increment}\n"
             f"      edit_type = {f.edit_type}\n"
             f"      sort_id = {f.sort_id}\n"
             f"      bit_size = {f.bit_count}\n"
             for f in self.fields.values()]
        )

    @property
    @abc.abstractmethod
    def param_info(self) -> tp.Optional[dict]:
        """Get param info from game-specific `params.display_info` subpackage."""


class ParamDefBND(abc.ABC):

    PARAMDEF_CLASS: tp.Type[ParamDef] = None

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

        self._bnd = Binder(paramdef_bnd_source)

        self.paramdefs = {}  # type: dict[str, ParamDef]
        for entry in self.bnd.entries:
            try:
                paramdef = self.PARAMDEF_CLASS(entry)
            except Exception:
                _LOGGER.error(f"Could not load ParamDefBND entry {entry.name}.")
                raise
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
