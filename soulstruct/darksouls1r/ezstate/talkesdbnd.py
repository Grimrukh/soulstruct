from __future__ import annotations

__all__ = ["TalkESDBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.ezstate.talkesdbnd import TalkESDBND as _BaseTalkESDBND
from soulstruct.containers import BinderVersion, BinderFlags, DCXType, BinderVersion4Info
from soulstruct.games import DARK_SOULS_DSR

from .esd import TalkESD


@dataclass(slots=True)
class TalkESDBND(_BaseTalkESDBND):
    TALK_ESD_CLASS: tp.ClassVar = TalkESD

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
        return f"N:\\FRPG\\data\\INTERROOT_x64\\script\\talk\\{entry_name}"
