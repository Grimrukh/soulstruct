from __future__ import annotations

__all__ = ["CACL_CORRECT_GRAPH_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CACL_CORRECT_GRAPH_ST(ParamRowData):
    StageMaxIntercept0: float = ParamField(
        float, "stageMaxVal0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxIntercept1: float = ParamField(
        float, "stageMaxVal1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxIntercept2: float = ParamField(
        float, "stageMaxVal2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxIntercept3: float = ParamField(
        float, "stageMaxVal3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxIntercept4: float = ParamField(
        float, "stageMaxVal4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxSlope0: float = ParamField(
        float, "stageMaxGrowVal0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxSlope1: float = ParamField(
        float, "stageMaxGrowVal1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxSlope2: float = ParamField(
        float, "stageMaxGrowVal2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxSlope3: float = ParamField(
        float, "stageMaxGrowVal3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    StageMaxSlope4: float = ParamField(
        float, "stageMaxGrowVal4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AdjustmentMaxSlope0: float = ParamField(
        float, "adjPt_maxGrowVal0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AdjustmentMaxSlope1: float = ParamField(
        float, "adjPt_maxGrowVal1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AdjustmentMaxSlope2: float = ParamField(
        float, "adjPt_maxGrowVal2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AdjustmentMaxSlope3: float = ParamField(
        float, "adjPt_maxGrowVal3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AdjustmentMaxSlope4: float = ParamField(
        float, "adjPt_maxGrowVal4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    InitialLevellingCostSlope: float = ParamField(
        float, "init_inclination_soul", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LevellingCostEarlyAdjustment: float = ParamField(
        float, "adjustment_value", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LateLevellingCostSlope: float = ParamField(
        float, "boundry_inclination_soul", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    LateLevellingCostThreshold: float = ParamField(
        float, "boundry_value", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
