from __future__ import annotations

__all__ = ["MSGBND"]

import typing as tp

from soulstruct.containers import Binder, BinderVersion, BinderFlags, BinderVersion4Info
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_DSR


class MSGBND(Binder):
    """Subclassed by games to set default binder/entry path."""

    IS_SPLIT_BXF: tp.ClassVar[bool] = False
    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{DARK_SOULS_DSR.interroot_prefix}\\Msg\\Data_ENGLISH"

    dcx_type: DCXType = DARK_SOULS_DSR.default_dcx_type
    signature: str = "07D7R6"
    flags: BinderFlags = BinderFlags(0b00101110)
    big_endian: bool = False
    bit_big_endian: bool = False
    version: BinderVersion = BinderVersion.V3
    v4_info: BinderVersion4Info | None = None
    is_split_bxf: bool = False
