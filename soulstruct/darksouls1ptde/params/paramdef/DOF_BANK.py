from __future__ import annotations

__all__ = ["DOF_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class DOF_BANK(ParamRow):
    FarBlurStartDistance: float = ParamField(
        float, "farDofBegin", default=60.0,
        tooltip="Distance (m) at which far depth of field blur begins.",
    )
    FarBlurEndDistance: float = ParamField(
        float, "farDofEnd", default=360.0,
        tooltip="Distance (m) at which far depth of field blur ends (reaches maximum).",
    )
    FarBlurMagnitude: int = ParamField(
        byte, "farDofMul", default=100,
        tooltip="Amount of far depth of field blur applied between the start and end distances.",
    )
    _Pad0: bytes = ParamPad(3, "pad_0[3]")
    NearBlurStartDistance: float = ParamField(
        float, "nearDofBegin", default=3.0,
        tooltip="Distance (m) at which near depth of field blur begins (further away than end distance).",
    )
    NearBlurEndDistance: float = ParamField(
        float, "nearDofEnd", default=0.0,
        tooltip="Distance (m) at which near depth of field blur ends (reaches maximum) (closer than start distance).",
    )
    NearBlurMagnitude: int = ParamField(
        byte, "nearDofMul", default=100,
        tooltip="Amount of near depth of field blur applied between start and end distances.",
    )
    _Pad1: bytes = ParamPad(3, "pad_1[3]")
    BlurSquaredDispersion: float = ParamField(
        float, "dispersionSq", default=5.0,
        tooltip="Squared dispersion of depth of field blur (greater value means more blur).",
    )
