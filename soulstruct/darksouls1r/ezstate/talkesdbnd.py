from __future__ import annotations

__all__ = ["TalkESDBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.ezstate.talkesdbnd import TalkESDBND as _BaseTalkESDBND
from soulstruct.containers import BinderVersion, BinderFlags
from soulstruct.games import DARK_SOULS_DSR

from .esd import TalkESD


@dataclass(slots=True)
class TalkESDBND(_BaseTalkESDBND):
    TALK_ESD_CLASS: tp.ClassVar = TalkESD

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
        return f"N:\\FRPG\\data\\INTERROOT_x64\\script\\talk\\{entry_name}"