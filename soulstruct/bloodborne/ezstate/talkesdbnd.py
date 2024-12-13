from __future__ import annotations

__all__ = ["TalkESDBND"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.ezstate.talkesdbnd import TalkESDBND as _BaseTalkESDBND
from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.dcx import DCXType
from soulstruct.games import BLOODBORNE

from .esd import TalkESD


class TalkESDBND(_BaseTalkESDBND):

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{BLOODBORNE.interroot_prefix}\\script\\talk"
    TALK_ESD_CLASS: tp.ClassVar = TalkESD

    dcx_type: DCXType = BLOODBORNE.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=lambda: BinderVersion4Info(False, False, True, 0))
