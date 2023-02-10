from __future__ import annotations

__all__ = ["ParamDefField"]

import abc
import logging
import math
import re
import typing as tp
from dataclasses import dataclass

from soulstruct.utilities.binary import *

from soulstruct.base.params.paramdef import field_types
from soulstruct.base.params.exceptions import ParamError

from .exceptions import ParamDefError

try:
    Self = tp.Self
except AttributeError:
    Self = "ParamDefField"

if tp.TYPE_CHECKING:
    from soulstruct.base.params.param import ParamRow

_LOGGER = logging.getLogger(__name__)


class ParamDefEditFlags(int):

    @property
    def is_wrap(self):
        return self & 0b0000_0001  # 1

    @property
    def is_lock(self):
        return self & 0b0000_0100  # 4


@dataclass(slots=True)
class ParamDefField(abc.ABC):
    """Information about a single field in a `Param`. Stored in `ParamDef`.

    NOTE: This class supports all (known) game file formats. It only needs to be subclassed to define game module
    lookups for verbose field information and/or better field defaults.
    """

    _ARRAY_LENGTH_RE: tp.ClassVar[re.Pattern] = re.compile(r"^\s*.+\s*\[\s*(\d+)\s*]\s*$")
    _BIT_SIZE_RE: tp.ClassVar[re.Pattern] = re.compile(r"^\s*.+\s*:\s*(\d+)\s*$")
    _PARAMDEX_NAME_RE: tp.ClassVar[re.Pattern] = re.compile(r"^")

    index: int
    param_type: str  # e.g. 'NPC_PARAM_ST'
    name: str  # e.g. 'spEffectID7'
    description: str

    size: int  # in bytes
    bit_count: int  # in bits (-1 unless bit field actually used)

    internal_type: str  # format string, e.g. 'f32' or 'dummy8'
    display_name: str
    display_type: tp.Type[field_types.base_type]
    display_format: str  # C++ string format template, e.g. '%d'

    # These are always floats, even for integer fields, except `default` is "" for string fields.
    default: float | str
    minimum: float
    maximum: float
    increment: float

    edit_flags: ParamDefEditFlags
    sort_id: int

    # Unknown strings that appear in newer games.
    unk_xb8: str
    unk_xc0: str
    unk_xc8: str

    # Number of values (>1 for padding only; indicated by square brackets in name). Auto-computed.
    length: int = 1

    # Python information.
    py_fmt: str = ""
    py_type: tp.Type[bool] | tp.Type[int] | tp.Type[float] | tp.Type[str] | tp.Type[bytes] = None
    py_type_min: int | float = 0
    py_type_max: int | float = 0
    py_default: bool | int | float | str = 0

    def __post_init__(self):
        self.py_fmt = self.display_type.format()
        self.py_type = self.display_type.python_type()
        self.py_type_min = self.display_type.minimum()
        self.py_type_max = self.display_type.maximum()

        self.length = self.size // self.display_type.size()  # number of values (>1 for padding only)
        if match := self._ARRAY_LENGTH_RE.match(self.name):
            if int(match.group(1)) != self.length:
                print(self.name, self.size)
                raise ParamDefError(
                    f"Length of field '{self.name}' with type `{self.display_type}` calculated from byte size "
                    f"({self.length}) does not match length implied by name: [{match.group(1)}]."
                )

        self.py_default = self.get_py_default()

    @classmethod
    def from_paramdef_reader(
        cls,
        reader: BinaryReader,
        field_index: int,
        param_type: str,
        format_version: int,
        unicode: bool,
    ) -> ParamDefField:
        """Read a single `ParamDefField`.

        Does NOT use a `BinaryStruct`, as the header details vary too wildly with `format_version` and can even vary
        within the same game across different `ParamDef`s.
        """

        encoding = "utf-16-le" if unicode else "shift_jis_2004"
        uses_string_offsets = format_version >= 202 or (106 <= format_version < 200)
        kwargs = {"index": field_index, "param_type": param_type}

        if uses_string_offsets:
            display_name_offset = reader.unpack_value("v")
            kwargs["display_name"] = reader.unpack_string(display_name_offset, encoding="utf-16-le")
        else:
            kwargs["display_name"] = reader.unpack_string(length=64, encoding=encoding)

        display_type_str = reader.unpack_string(length=8, encoding="shift_jis_2004")
        # print(display_type_str.rstrip().encode())
        try:
            kwargs["display_type"] = getattr(field_types, display_type_str)  # type: tp.Type[field_types.base_type]
        except AttributeError:
            raise TypeError(f"Unknown `ParamDefField` display type: {display_type_str}")
        kwargs["display_format"] = reader.unpack_string(length=8, encoding="shift_jis_2004")  # %i, %u, %d, etc.

        if format_version >= 203:
            # Numeric information has moved to new section below.
            reader.assert_pad(16)
        else:
            kwargs["default"], kwargs["minimum"], kwargs["maximum"], kwargs["increment"] = reader.unpack("4f")

        kwargs["edit_flags"] = ParamDefEditFlags(reader.unpack_value("i"))
        kwargs["size"] = reader.unpack_value("i")

        description_offset = reader.unpack_value("v")
        if description_offset != 0:
            kwargs["description"] = reader.unpack_string(offset=description_offset, encoding=encoding)
        else:
            kwargs["description"] = ""

        if uses_string_offsets:
            internal_type_offset = reader.unpack_value("v")
            kwargs["internal_type"] = reader.unpack_string(offset=internal_type_offset, encoding="ASCII")
        else:
            kwargs["internal_type"] = reader.unpack_string(length=32, encoding="shift_jis_2004")

        kwargs["bit_count"] = -1  # default (does not use bit field)
        if format_version >= 102:
            if uses_string_offsets:
                name_offset = reader.unpack_value("v")
                name = kwargs["name"] = reader.unpack_string(offset=name_offset, encoding="ASCII")
            else:
                name = kwargs["name"] = reader.unpack_string(length=32, encoding="shift_jis_2004")

            if match := cls._BIT_SIZE_RE.match(name):
                kwargs["bit_count"] = int(match.group(1))

            # NOTE: `length` is set and validated in `__post_init__`, as it uses the attached Python type information.

        kwargs["sort_id"] = reader.unpack_value("i") if format_version >= 104 else -1

        kwargs["unk_xb8"] = kwargs["unk_xc0"] = kwargs["unk_xc8"] = ""
        if format_version >= 200:
            reader.assert_pad(4)
            unk_xb8_offset, unk_xc0_offset, unk_xc8_offset = reader.unpack("3q")
            if unk_xb8_offset != 0:
                kwargs["unk_xb8"] = reader.unpack_string(offset=unk_xb8_offset, encoding="ASCII")
            if unk_xc0_offset != 0:
                kwargs["unk_xc0"] = reader.unpack_string(offset=unk_xc0_offset, encoding="ASCII")
            if unk_xc8_offset != 0:
                kwargs["unk_xc8"] = reader.unpack_string(offset=unk_xc8_offset, encoding="ASCII")
        elif format_version >= 106:
            reader.assert_pad(12)

        if format_version >= 203:
            # Numeric information is now here, with variable format.
            keys = ("default", "minimum", "maximum", "increment")
            if issubclass(kwargs["display_type"], field_types.basestring):
                kwargs["default"] = ""
                for key in keys[1:]:
                    kwargs[key] = 0.0
                reader.assert_pad(32)  # four null 64-bit values
            elif issubclass(kwargs["display_type"], (field_types.f32, field_types.angle32)):
                for key in keys:
                    kwargs[key] = reader.unpack_value("f")
                    reader.assert_pad(4)
            elif issubclass(kwargs["display_type"], field_types.f64):
                for key in keys:
                    kwargs[key] = reader.unpack_value("d")
            elif kwargs["display_type"].size() <= 4:
                for key in keys:
                    kwargs[key] = reader.unpack_value("i")
                    reader.assert_pad(4)
            # NOTE: No 64-bit integer fields have been seen in any game yet.
            else:
                raise TypeError(f"Unknown numeric format for `ParamDefField` display type: {kwargs['display_type']}")

        # noinspection PyTypeChecker
        return cls(**kwargs)

    @classmethod
    def from_paramdex_xml(cls, index: int, xml_node, param_type: str) -> Self:
        """Load field information from Paramdex XML node."""
        kwargs = {
            "index": index,
            "param_type": param_type,
            "edit_flags": ParamDefEditFlags(0),
            "display_format": "%i",
            "increment": 1.0,
            "sort_id": -1,
            "description": "",
        }
        def_string = xml_node.attrib["Def"]  # e.g., "s32 spEffectId0 = -1"

        def_split = def_string.split(" ")
        type_str = def_split[0]
        display_type = kwargs["display_type"] = getattr(field_types, type_str)  # type: tp.Type[field_types.base_type]
        name = kwargs["name"] = def_split[1]

        if match := cls._ARRAY_LENGTH_RE.match(name):
            # Size is equal to array length times data size.
            kwargs["size"] = display_type.size() * int(match.group(1))
        else:
            kwargs["size"] = display_type.size()

        # Defaults.
        kwargs["internal_type"] = display_type
        kwargs["minimum"] = display_type.minimum()
        kwargs["maximum"] = display_type.maximum()
        if issubclass(display_type, (field_types.unsigned, field_types.signed)):
            kwargs["display_format"] = "%i"
        elif issubclass(display_type, (field_types.f32, field_types.f64)):
            kwargs["display_format"] = "%d"
        elif issubclass(display_type, field_types.fixstr):
            kwargs["display_format"] = "%s"
        elif issubclass(display_type, field_types.fixstrW):
            kwargs["display_format"] = "%u"

        if len(def_split) > 2:
            # Find default.
            default_str = def_split[3]  # index 2 should be "="
            kwargs["default"] = display_type.python_type()(default_str)
        else:
            # Use sensible default (0 or 0.0 or empty string).
            kwargs["default"] = display_type.default()

        for child in xml_node:
            if child.tag == "DisplayName":
                kwargs["display_name"] = child.text
            elif child.tag == "DisplayFormat":
                kwargs["display_format"] = child.text
            elif child.tag == "Enum":
                kwargs["internal_type"] = child.text
            elif child.tag == "Description":
                kwargs["description"] = child.text
            elif child.tag == "EditFlags":
                if child.text == "None":
                    kwargs["edit_flags"] = ParamDefEditFlags(0)
                elif child.text == "Wrap":
                    kwargs["edit_flags"] = ParamDefEditFlags(0b0000_0001)
                elif child.text == "Lock":
                    kwargs["edit_flags"] = ParamDefEditFlags(0b0000_0100)
                elif child.text == "Wrap, Lock":
                    kwargs["edit_flags"] = ParamDefEditFlags(0b0000_0001 | 0b0000_0100)
                else:
                    raise ValueError(f"Unsupported Paramdex 'EditFlags': {child.text}")
            elif child.tag == "Minimum":
                kwargs["minimum"] = float(child.text)
            elif child.tag == "Maximum":
                kwargs["maximum"] = float(child.text)
            elif child.tag == "Increment":
                kwargs["increment"] = float(child.text)
            elif child.tag == "SortID":
                kwargs["sort_id"] = int(child.text)
            elif child.tag == "UnkB8":
                kwargs["unk_b8"] = child.text
            elif child.tag == "UnkC0":
                kwargs["unk_c0"] = child.text
            elif child.tag == "UnkC8":
                kwargs["unk_c8"] = child.text
            elif child.tag.startswith("ParamRef"):
                # TODO: Could make use of these links from Yapped. Ignoring for now.
                pass
            else:
                raise ValueError(f"Unrecognized field tag name in Paramdex: {child.tag}")

        return cls(**kwargs)

    def check_python_type(self, value):
        """Check given `value` has the expected Python type of this field."""
        if self.display_type is field_types.dummy8 and self.bit_count == -1:
            if not isinstance(value, bytes):  # `dummy8` fields that are not bit fields are not unpacked
                raise ParamError(f"Value {value} of `dummy8` field {self.name} should be `bytes`, not {type(value)}.")
        elif not isinstance(value, self.display_type):
            raise ParamError(
                f"Value {value} of field {self.name} should have type {self.display_type}, not {type(value)}."
            )

    def check_range(self, value):
        """Some vanilla values are outside the ParamDef min/max, so we just check the range of the actual C type."""
        if self.display_type in {field_types.f32, field_types.f64} and math.isnan(value):
            return  # floats are allowed to be `nan`
        if self.display_type is field_types.dummy8 and self.bit_count == -1:
            return  # not unpacked
        if not (
            (self.py_type_min is None or self.py_type_min <= value)
            and (self.py_type_max is None or value <= self.py_type_max)
        ):
            raise ValueError(
                f"Value {value} of field {self.name} is outside range of its type ({self.display_type.__name__}): "
                f"[{self.py_type_min}, {self.py_type_max}]"
            )

    def validate(self, value: tp.Any):
        self.check_python_type(value)
        self.check_range(value)

    def __repr__(self):
        return (
            f"{self.name} ({self.display_name}) | {self.internal_type} ({self.display_type}) | "
            f"size = {self.size} | min/max/increment = {self.minimum}, {self.maximum}, {self.increment} | "
            f"default = {self.default} | {self.description}"
        )

    def get_display_info(self, row: ParamRow):
        """Get display info from game-specific `params.display_info` subpackage."""
        raise TypeError("Cannot get display info for this `ParamDefField` class.")
        # TODO: Use a 'get_game()' module lookup (from `ParamDef`).

    def get_py_default(self) -> bool | int | float | str:
        """Get default value from game-specific `defaults` module, if specified.

        Base class version here just parses the existing ParamDef default.
        """
        # TODO: Use a 'get_game()' module lookup (from `ParamDef`) and fall back to this.
        if self.bit_count == 1 and self.internal_type != "dummy8":
            return bool(self.default)
        elif self.internal_type not in {"f32", "f64"}:
            return int(self.default)
        return self.default  # float or str
