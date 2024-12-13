from __future__ import annotations

__all__ = ["ENEMY_COMMON_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class ENEMY_COMMON_PARAM_ST(ParamRow):
    _Pad0: bytes = ParamPad(8, "reserved0[8]")
    SoundTargetTryApproachTime: int = ParamField(
        int, "soundTargetTryApproachTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SearchTargetTryApproachTime: int = ParamField(
        int, "searchTargetTryApproachTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MemoryTargetTryApproachTime: int = ParamField(
        int, "memoryTargetTryApproachTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(40, "reserved5[40]")
    ActivateChrByTimePhantomId: int = ParamField(
        int, "activateChrByTime_PhantomId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FindUnfavorableFailedPointDist: float = ParamField(
        float, "findUnfavorableFailedPointDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FindUnfavorableFailedPointHeight: float = ParamField(
        float, "findUnfavorableFailedPointHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(184, "reserved18[184]")
