from __future__ import annotations

__all__ = ["ENEMY_COMMON_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class ENEMY_COMMON_PARAM_ST(ParamRow):
    _Pad0: bytes = ParamPad(8, "reserved0[8]")
    SoundTargetTryApproachTime: int = ParamField(
        int32, "soundTargetTryApproachTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SearchTargetTryApproachTime: int = ParamField(
        int32, "searchTargetTryApproachTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MemoryTargetTryApproachTime: int = ParamField(
        int32, "memoryTargetTryApproachTime", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(40, "reserved5[40]")
    ActivateChrByTimePhantomId: int = ParamField(
        int32, "activateChrByTime_PhantomId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FindUnfavorableFailedPointDist: float = ParamField(
        float32, "findUnfavorableFailedPointDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FindUnfavorableFailedPointHeight: float = ParamField(
        float32, "findUnfavorableFailedPointHeight", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(184, "reserved18[184]")
