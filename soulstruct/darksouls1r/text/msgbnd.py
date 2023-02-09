from __future__ import annotations

__all__ = ["MSGBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.text.msgbnd import MSGBND as _BaseMSGBND
from soulstruct.containers import BinderVersion, BinderFlags
from soulstruct.games import DARK_SOULS_DSR

try:
    Self = tp.Self
except AttributeError:
    Self = "MSGBND"


@dataclass(slots=True)
class MSGBND(_BaseMSGBND):
    """Subclassed by games to set default binder/entry path."""

    dcx_type = DARK_SOULS_DSR.default_dcx_type
    signature = "07D7R6"
    flags = BinderFlags(0b00101110)
    big_endian = False
    bit_big_endian = False
    version = BinderVersion.V3
    v4_info = None
    is_split_bxf = False

    @classmethod
    def get_default_entry_path(cls, entry_name: str):
        return f"N:\\FRPG\\data\\Msg\\Data_ENGLISH\\{entry_name}"
