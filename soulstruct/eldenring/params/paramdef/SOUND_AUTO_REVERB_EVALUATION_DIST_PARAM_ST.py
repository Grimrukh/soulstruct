from __future__ import annotations

__all__ = ["SOUND_AUTO_REVERB_EVALUATION_DIST_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SOUND_AUTO_REVERB_EVALUATION_DIST_PARAM_ST(ParamRow):
    NoHitDist: float = ParamField(
        float, "NoHitDist", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    IsCollectNoHitPoint: int = ParamField(
        byte, "isCollectNoHitPoint", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCollectOutdoorPoint: int = ParamField(
        byte, "isCollectOutdoorPoint", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCollectFloorPoint: int = ParamField(
        byte, "isCollectFloorPoint", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DistValCalcType: int = ParamField(
        byte, "distValCalcType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableLifeTime: float = ParamField(
        float, "enableLifeTime", default=-1.0,
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
