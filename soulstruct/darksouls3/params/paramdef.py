__all__ = ["ParamDefField", "ParamDef", "ParamDefBND"]

from soulstruct.base.params.paramdef import (
    ParamDefField as _BaseParamDefField,
    ParamDef as _BaseParamDef,
    ParamDefBND as _BaseParamDefBND,
)
from soulstruct.utilities.binary import BinaryStruct


# TODO: Dark Souls 3 doesn't even use GameParam, right?


class ParamDefField(_BaseParamDefField):

    STRUCT = BinaryStruct(
        ("display_name_offset", "q"),
        ("display_type", "8j"),
        ("display_format", "8j"),  # %i, %u, %d, etc.
        ("default", "f"),
        ("minimum", "f"),
        ("maximum", "f"),
        ("increment", "f"),
        ("edit_type", "i"),
        ("size", "i"),
        ("description_offset", "q"),
        ("internal_type", "32j"),  # could be an enum name (see params.enums)
        ("name", "32j"),
        ("sort_id", "i"),
        "28x",
    )


class ParamDef(_BaseParamDef):
    BYTE_ORDER = "<"
    HEADER_STRUCT = BinaryStruct(
        ("size", "i"),
        ("header_size", "H", 255),
        ("data_version", "H"),
        ("field_count", "H"),
        ("field_size", "H", 104),
        "4x",
        ("param_name_offset", "q"),
        "20x",
        ("big_endian", "B"),
        ("unicode", "?"),
        ("format_version", "h", 202),
        ("unk1", "q", 56),
    )
    FIELD_CLASS = ParamDefField


class ParamDefBND(_BaseParamDefBND):
    PARAMDEF_CLASS = ParamDef
