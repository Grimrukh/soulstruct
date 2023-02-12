from __future__ import annotations

__all__ = ["SOUND_AUTO_REVERB_EVALUATION_DIST_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SOUND_AUTO_REVERB_EVALUATION_DIST_PARAM_ST(ParamRow):
    NoHitDist: float = ParamField(
        float, "NoHitDist", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IsCollectNoHitPoint: int = ParamField(
        byte, "isCollectNoHitPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCollectOutdoorPoint: int = ParamField(
        byte, "isCollectOutdoorPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCollectFloorPoint: int = ParamField(
        byte, "isCollectFloorPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DistValCalcType: int = ParamField(
        byte, "distValCalcType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableLifeTime: float = ParamField(
        float, "enableLifeTime", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxDistRecordNum: int = ParamField(
        uint, "maxDistRecordNum", default=20,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreDistNumForMax: int = ParamField(
        uint, "ignoreDistNumForMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
