from __future__ import annotations

__all__ = ["TalkESDBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.base.ezstate.talkesdbnd import TalkESDBND as _BaseTalkESDBND
from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_PTDE
from .esd import TalkESD


@dataclass(slots=True)
class TalkESDBND(_BaseTalkESDBND):
    TALK_ESD_CLASS: tp.ClassVar = TalkESD

    dcx_type: DCXType = DARK_SOULS_PTDE.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info: BinderVersion4Info = None

    @classmethod
    def get_default_new_entry_path(cls, entry_name: str) -> str:
        if not entry_name.endswith(".talkesd"):
            raise ValueError(f"Expected `TalkESDBND` entry name to end with '.talkesd': {entry_name}")
        return f"N:\\FRPG\\data\\INTERROOT_win32\\script\\talk\\{entry_name}"
