from __future__ import annotations

__all__ = ["SOUND_COMMON_INGAME_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SOUND_COMMON_INGAME_PARAM_ST(ParamRow):
    ParamKeyStr: bytes = ParamField(
        bytes, "ParamKeyStr[32]", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
    ParamValueStr: bytes = ParamField(
        bytes, "ParamValueStr[32]", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
