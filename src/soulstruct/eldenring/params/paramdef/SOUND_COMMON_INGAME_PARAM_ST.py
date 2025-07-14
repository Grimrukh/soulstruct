from __future__ import annotations

__all__ = ["SOUND_COMMON_INGAME_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SOUND_COMMON_INGAME_PARAM_ST(ParamRow):
    ParamKeyStr: str = ParamField(
        str, "ParamKeyStr[32]", encoding="shift_jis_2004", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
    ParamValueStr: str = ParamField(
        str, "ParamValueStr[32]", encoding="shift_jis_2004", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
