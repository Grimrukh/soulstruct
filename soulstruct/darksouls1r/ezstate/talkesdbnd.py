from __future__ import annotations

__all__ = ["TalkESDBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.ezstate.talkesdbnd import TalkESDBND as _BaseTalkESDBND
from soulstruct.containers import BinderVersion, BinderFlags, BinderVersion4Info
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_DSR

from .esd import TalkESD


class TalkESDBND(_BaseTalkESDBND):

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{DARK_SOULS_DSR.interroot_prefix}\\script\\talk"
    TALK_ESD_CLASS: tp.ClassVar = TalkESD

    dcx_type: DCXType = DARK_SOULS_DSR.default_dcx_type
    signature: str = "07D7R6"
    flags: BinderFlags = BinderFlags(0b00101110)
    big_endian: bool = False
    bit_big_endian: bool = False
    version: BinderVersion = BinderVersion.V3
    v4_info: BinderVersion4Info | None = None
    is_split_bxf: bool = False
