from __future__ import annotations

__all__ = ["RIDE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class RIDE_PARAM_ST(ParamRow):
    AtkChrId: int = ParamField(
        uint32, "atkChrId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefChrId: int = ParamField(
        uint32, "defChrId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RideCamParamId: int = ParamField(
        int32, "rideCamParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AtkChrAnimId: int = ParamField(
        uint32, "atkChrAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefChrAnimId: int = ParamField(
        uint32, "defChrAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefAdjustDmyId: int = ParamField(
        int32, "defAdjustDmyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DefCheckDmyId: int = ParamField(
        int32, "defCheckDmyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMyToDef: float = ParamField(
        float32, "diffAngMyToDef", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Dist: float = ParamField(
        float32, "dist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UpperYRange: float = ParamField(
        float32, "upperYRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LowerYRange: float = ParamField(
        float32, "lowerYRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMin: float = ParamField(
        float32, "diffAngMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMax: float = ParamField(
        float32, "diffAngMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "pad[12]")
