from __future__ import annotations

__all__ = ["TOUGHNESS_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class TOUGHNESS_PARAM_ST(ParamRow):
    CorrectionRate: float = ParamField(
        float32, "correctionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    MinToughness: int = ParamField(
        uint16, "minToughness", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsNonEffectiveCorrectionForMin: int = ParamField(
        uint8, "isNonEffectiveCorrectionForMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2[1]")
    SpEffectId: int = ParamField(
        int32, "spEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ProCorrectionRate: float = ParamField(
        float32, "proCorrectionRate", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Unk1: float = ParamField(
        float32, "unk1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Unk2: float = ParamField(
        float32, "unk2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad1[8]")
