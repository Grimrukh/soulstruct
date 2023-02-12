from __future__ import annotations

__all__ = ["TOUGHNESS_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class TOUGHNESS_PARAM_ST(ParamRowData):
    CorrectionRate: float = ParamField(
        float, "correctionRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    MinToughness: int = ParamField(
        ushort, "minToughness", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsNonEffectiveCorrectionForMin: int = ParamField(
        byte, "isNonEffectiveCorrectionForMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    SpEffectId: int = ParamField(
        int, "spEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ProCorrectionRate: float = ParamField(
        float, "proCorrectionRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(16, "pad1[16]")
