from __future__ import annotations

__all__ = ["SOUND_AUTO_REVERB_SELECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SOUND_AUTO_REVERB_SELECT_PARAM_ST(ParamRow):
    ReverbType: int = ParamField(
        uint, "reverbType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaNo: int = ParamField(
        int, "AreaNo", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IndoorOutdoor: int = ParamField(
        sbyte, "IndoorOutdoor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UseDistNoA: int = ParamField(
        sbyte, "useDistNoA", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UseDistNoB: int = ParamField(
        sbyte, "useDistNoB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad0[1]")
    DistMinA: float = ParamField(
        float, "DistMinA", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DistMaxA: float = ParamField(
        float, "DistMaxA", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DistMinB: float = ParamField(
        float, "DistMinB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DistMaxB: float = ParamField(
        float, "DistMaxB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NoHitNumMin: int = ParamField(
        int, "NoHitNumMin", default=-1,
        tooltip="TOOLTIP-TODO",
    )
