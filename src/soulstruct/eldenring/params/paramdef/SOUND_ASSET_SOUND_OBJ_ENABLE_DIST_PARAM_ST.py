from __future__ import annotations

__all__ = ["SOUND_ASSET_SOUND_OBJ_ENABLE_DIST_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class SOUND_ASSET_SOUND_OBJ_ENABLE_DIST_PARAM_ST(ParamRow):
    SoundObjEnableDist: float = ParamField(
        float32, "SoundObjEnableDist", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
