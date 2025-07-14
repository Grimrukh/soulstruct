from __future__ import annotations

__all__ = ["SOUND_AUTO_REVERB_SELECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class SOUND_AUTO_REVERB_SELECT_PARAM_ST(ParamRow):
    ReverbType: int = ParamField(
        uint32, "reverbType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaNo: int = ParamField(
        int32, "AreaNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IndoorOutdoor: int = ParamField(
        int8, "IndoorOutdoor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UseDistNoA: int = ParamField(
        int8, "useDistNoA", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UseDistNoB: int = ParamField(
        int8, "useDistNoB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad0[1]")
    DistMinA: float = ParamField(
        float32, "DistMinA", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    DistMaxA: float = ParamField(
        float32, "DistMaxA", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    DistMinB: float = ParamField(
        float32, "DistMinB", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    DistMaxB: float = ParamField(
        float32, "DistMaxB", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    NoHitNumMin: int = ParamField(
        int32, "NoHitNumMin", default=-1,
        tooltip="TOOLTIP-TODO",
    )
