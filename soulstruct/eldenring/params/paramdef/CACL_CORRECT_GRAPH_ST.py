from __future__ import annotations

__all__ = ["CACL_CORRECT_GRAPH_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CACL_CORRECT_GRAPH_ST(ParamRow):
    StageMaxVal0: float = ParamField(
        float, "stageMaxVal0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxVal1: float = ParamField(
        float, "stageMaxVal1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxVal2: float = ParamField(
        float, "stageMaxVal2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxVal3: float = ParamField(
        float, "stageMaxVal3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxVal4: float = ParamField(
        float, "stageMaxVal4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxGrowVal0: float = ParamField(
        float, "stageMaxGrowVal0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxGrowVal1: float = ParamField(
        float, "stageMaxGrowVal1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxGrowVal2: float = ParamField(
        float, "stageMaxGrowVal2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxGrowVal3: float = ParamField(
        float, "stageMaxGrowVal3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxGrowVal4: float = ParamField(
        float, "stageMaxGrowVal4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AdjPtmaxGrowVal0: float = ParamField(
        float, "adjPt_maxGrowVal0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AdjPtmaxGrowVal1: float = ParamField(
        float, "adjPt_maxGrowVal1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AdjPtmaxGrowVal2: float = ParamField(
        float, "adjPt_maxGrowVal2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AdjPtmaxGrowVal3: float = ParamField(
        float, "adjPt_maxGrowVal3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AdjPtmaxGrowVal4: float = ParamField(
        float, "adjPt_maxGrowVal4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Initinclinationsoul: float = ParamField(
        float, "init_inclination_soul", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Adjustmentvalue: float = ParamField(
        float, "adjustment_value", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Boundryinclinationsoul: float = ParamField(
        float, "boundry_inclination_soul", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Boundryvalue: float = ParamField(
        float, "boundry_value", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
