from __future__ import annotations

__all__ = ["SOUND_AUTO_ENV_SOUND_GROUP_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SOUND_AUTO_ENV_SOUND_GROUP_PARAM_ST(ParamRow):
    SoundNo: int = ParamField(
        int, "SoundNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ExpandRange: float = ParamField(
        float, "ExpandRange", default=100.0,
        tooltip="TOOLTIP-TODO",
    )
    FollowSpeed: float = ParamField(
        float, "FollowSpeed", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    FollowRate: float = ParamField(
        float, "FollowRate", default=0.015,
        tooltip="TOOLTIP-TODO",
    )
