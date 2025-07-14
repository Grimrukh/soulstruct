from __future__ import annotations

__all__ = ["RESIDENT_FX_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class RESIDENT_FX_PARAM_ST(ParamRow):
    VisualEffectID: int = ParamField(
        int32, "sfxId", game_type=VisualEffect, default=-1,
        tooltip="TODO",
    )
    ModelPoint: int = ParamField(
        int32, "dmypolyId", game_type=ModelDummy, default=-1,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad_0[8]")
