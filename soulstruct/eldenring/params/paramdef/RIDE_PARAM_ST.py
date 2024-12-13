from __future__ import annotations

__all__ = ["RIDE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class RIDE_PARAM_ST(ParamRow):
    AtkChrId: int = ParamField(
        uint, "atkChrId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefChrId: int = ParamField(
        uint, "defChrId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RideCamParamId: int = ParamField(
        int, "rideCamParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AtkChrAnimId: int = ParamField(
        uint, "atkChrAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefChrAnimId: int = ParamField(
        uint, "defChrAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefAdjustDmyId: int = ParamField(
        int, "defAdjustDmyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DefCheckDmyId: int = ParamField(
        int, "defCheckDmyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMyToDef: float = ParamField(
        float, "diffAngMyToDef", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Dist: float = ParamField(
        float, "dist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    UpperYRange: float = ParamField(
        float, "upperYRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LowerYRange: float = ParamField(
        float, "lowerYRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMin: float = ParamField(
        float, "diffAngMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DiffAngMax: float = ParamField(
        float, "diffAngMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(12, "pad[12]")
