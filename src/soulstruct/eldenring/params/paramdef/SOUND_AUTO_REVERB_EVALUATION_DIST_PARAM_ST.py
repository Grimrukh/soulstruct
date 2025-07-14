from __future__ import annotations

__all__ = ["SOUND_AUTO_REVERB_EVALUATION_DIST_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SOUND_AUTO_REVERB_EVALUATION_DIST_PARAM_ST(ParamRow):
    NoHitDist: float = ParamField(
        float32, "NoHitDist", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    IsCollectNoHitPoint: int = ParamField(
        uint8, "isCollectNoHitPoint", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCollectOutdoorPoint: int = ParamField(
        uint8, "isCollectOutdoorPoint", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCollectFloorPoint: int = ParamField(
        uint8, "isCollectFloorPoint", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DistValCalcType: int = ParamField(
        uint8, "distValCalcType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableLifeTime: float = ParamField(
        float32, "enableLifeTime", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxDistRecordNum: int = ParamField(
        uint32, "maxDistRecordNum", default=20,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreDistNumForMax: int = ParamField(
        uint32, "ignoreDistNumForMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
