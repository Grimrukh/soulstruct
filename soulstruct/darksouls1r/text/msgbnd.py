from __future__ import annotations

__all__ = ["MSGBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.text.msgbnd import MSGBND as _BaseMSGBND
from soulstruct.containers import BinderVersion, BinderFlags, BinderVersion4Info, DCXType
from soulstruct.games import DARK_SOULS_DSR

try:
    Self = tp.Self
except AttributeError:
    Self = "MSGBND"


@dataclass(slots=True)
class MSGBND(_BaseMSGBND):
    """Subclassed by games to set default binder/entry path."""

    dcx_type: DCXType = DARK_SOULS_DSR.default_dcx_type
    signature: str = "07D7R6"
    flags: BinderFlags = BinderFlags(0b00101110)
    big_endian: bool = False
    bit_big_endian: bool = False
    version: BinderVersion = BinderVersion.V3
    v4_info: BinderVersion4Info | None = None
    is_split_bxf: bool = False

    @classmethod
    def get_default_new_entry_path(cls, entry_name: str):
        return f"N:\\FRPG\\data\\Msg\\Data_ENGLISH\\{entry_name}"
