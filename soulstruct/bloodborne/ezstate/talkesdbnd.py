from __future__ import annotations

__all__ = ["TalkESDBND"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.ezstate.talkesdbnd import TalkESDBND as _BaseTalkESDBND
from soulstruct.containers import BinderVersion, BinderVersion4Info, DCXType
from soulstruct.games import BLOODBORNE

from .esd import TalkESD


@dataclass(slots=True)
class TalkESDBND(_BaseTalkESDBND):
    TALK_ESD_CLASS: tp.ClassVar = TalkESD

    dcx_type: DCXType = BLOODBORNE.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=lambda: BinderVersion4Info(False, False, True, 0))

    @classmethod
    def get_default_entry_path(cls, entry_name: str):
        return f"N:\\SPRJ\\data\\INTERROOT_ps4\\script\\talk\\{entry_name}"
