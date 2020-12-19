__all__ = ["ParamDefField", "ParamDef", "ParamDefBND", "GET_BUNDLED"]

from soulstruct.games import DARK_SOULS_DSR
from soulstruct.params.base.paramdef import (
    ParamDefField as _BaseParamDefField,
    ParamDef as _BaseParamDef,
    ParamDefBND as _BaseParamDefBND,
)
from soulstruct.utilities.binary_struct import BinaryStruct

_BUNDLED = None


class ParamDefField(_BaseParamDefField):
    STRUCT = BinaryStruct(
        ("debug_name", "64j"),
        ("debug_type", "8j"),
        ("debug_format", "8j"),  # %i, %u, %d, etc.
        ("default", "f"),
        ("minimum", "f"),
        ("maximum", "f"),
        ("increment", "f"),
        ("debug_display", "i"),
        ("size", "i"),
        ("description_offset", "i"),
        ("internal_type", "32j"),  # could be an enum name (see params.enums)
        ("name", "32j"),
        ("sort_id", "i"),
    )
    USES_DEBUG_NAME_OFFSET = False


class ParamDef(_BaseParamDef):
    BYTE_ORDER = "<"
    STRUCT = BinaryStruct(
        ("size", "i"),
        ("header_size", "H", 48),
        ("data_version", "H"),
        ("field_count", "H"),
        ("field_size", "H", 176),
        ("param_name", "32j"),
        ("big_endian", "B"),
        ("unicode", "?"),
        ("format_version", "h", 104),
    )
    FIELD_CLASS = ParamDefField


class ParamDefBND(_BaseParamDefBND):
    PARAMDEF_CLASS = ParamDef
    GAME = DARK_SOULS_DSR


def GET_BUNDLED() -> ParamDefBND:
    global _BUNDLED
    if _BUNDLED is None:
        _BUNDLED = ParamDefBND()
    return _BUNDLED
