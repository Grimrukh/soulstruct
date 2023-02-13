from __future__ import annotations

__all__ = ["SOUND_ASSET_SOUND_OBJ_ENABLE_DIST_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SOUND_ASSET_SOUND_OBJ_ENABLE_DIST_PARAM_ST(ParamRow):
    SoundObjEnableDist: float = ParamField(
        float, "SoundObjEnableDist", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
