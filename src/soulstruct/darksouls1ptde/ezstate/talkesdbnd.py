from __future__ import annotations

__all__ = ["TalkESDBND"]

import typing as tp

from soulstruct.base.ezstate.talkesdbnd import TalkESDBND as _BaseTalkESDBND
from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.dcx import DCXType
from soulstruct.games import DARK_SOULS_PTDE
from .esd import TalkESD


class TalkESDBND(_BaseTalkESDBND[TalkESD]):

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{DARK_SOULS_PTDE.interroot_prefix}\\script\\talk"
    TALK_ESD_CLASS: tp.ClassVar = TalkESD

    version: BinderVersion = BinderVersion.V3
