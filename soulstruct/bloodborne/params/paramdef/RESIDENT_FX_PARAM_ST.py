from __future__ import annotations

__all__ = ["RESIDENT_FX_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class RESIDENT_FX_PARAM_ST(ParamRowData):
    VisualEffectID: int = ParamField(
        int, "sfxId", default=-1,
        tooltip="TODO",
    )
    ModelPoint: int = ParamField(
        int, "dmypolyId", default=-1,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad_0[8]")
