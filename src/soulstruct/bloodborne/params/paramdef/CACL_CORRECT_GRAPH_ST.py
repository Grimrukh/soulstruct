from __future__ import annotations

__all__ = ["CACL_CORRECT_GRAPH_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class CACL_CORRECT_GRAPH_ST(ParamRow):
    StageMaxIntercept0: float = ParamField(
        float, "stageMaxVal0", default=0.0,
        tooltip="Y-intercept in equation of 'stage max' line 0.",
    )
    StageMaxIntercept1: float = ParamField(
        float, "stageMaxVal1", default=0.0,
        tooltip="Y-intercept in equation of 'stage max' line 1.",
    )
    StageMaxIntercept2: float = ParamField(
        float, "stageMaxVal2", default=0.0,
        tooltip="Y-intercept in equation of 'stage max' line 2.",
    )
    StageMaxIntercept3: float = ParamField(
        float, "stageMaxVal3", default=0.0,
        tooltip="Y-intercept in equation of 'stage max' line 3.",
    )
    StageMaxIntercept4: float = ParamField(
        float, "stageMaxVal4", default=0.0,
        tooltip="Y-intercept in equation of 'stage max' line 4.",
    )
    StageMaxSlope0: float = ParamField(
        float, "stageMaxGrowVal0", default=0.0,
        tooltip="Slope in equation of 'stage max' line 0.",
    )
    StageMaxSlope1: float = ParamField(
        float, "stageMaxGrowVal1", default=0.0,
        tooltip="Slope in equation of 'stage max' line 1.",
    )
    StageMaxSlope2: float = ParamField(
        float, "stageMaxGrowVal2", default=0.0,
        tooltip="Slope in equation of 'stage max' line 2.",
    )
    StageMaxSlope3: float = ParamField(
        float, "stageMaxGrowVal3", default=0.0,
        tooltip="Slope in equation of 'stage max' line 3.",
    )
    StageMaxSlope4: float = ParamField(
        float, "stageMaxGrowVal4", default=0.0,
        tooltip="Slope in equation of 'stage max' line 4.",
    )
    AdjustmentMaxSlope0: float = ParamField(
        float, "adjPt_maxGrowVal0", default=0.0,
        tooltip="Adjustment factor for slope in equation of 'stage max' line 0.",
    )
    AdjustmentMaxSlope1: float = ParamField(
        float, "adjPt_maxGrowVal1", default=0.0,
        tooltip="Adjustment factor for slope in equation of 'stage max' line 1.",
    )
    AdjustmentMaxSlope2: float = ParamField(
        float, "adjPt_maxGrowVal2", default=0.0,
        tooltip="Adjustment factor for slope in equation of 'stage max' line 2.",
    )
    AdjustmentMaxSlope3: float = ParamField(
        float, "adjPt_maxGrowVal3", default=0.0,
        tooltip="Adjustment factor for slope in equation of 'stage max' line 3.",
    )
    AdjustmentMaxSlope4: float = ParamField(
        float, "adjPt_maxGrowVal4", default=0.0,
        tooltip="Adjustment factor for slope in equation of 'stage max' line 4.",
    )
    InitialLevellingCostSlope: float = ParamField(
        float, "init_inclination_soul", default=0.0,
        tooltip="Initial slope of equation determining levelling costs (alpha 1).",
    )
    LevellingCostEarlyAdjustment: float = ParamField(
        float, "adjustment_value", default=0.0,
        tooltip="'Early' adjustment value of equation determining levelling costs (alpha 2).",
    )
    LateLevellingCostSlope: float = ParamField(
        float, "boundry_inclination_soul", default=0.0,
        tooltip="Slope of equation determining required levelling souls after 'LateLevellingCostThreshold' value "
                "(alpha 3).",
    )
    LateLevellingCostThreshold: float = ParamField(
        float, "boundry_value", default=0.0,
        tooltip="Threshold at which 'LateLevellingCostSlope' takes over for levelling (t).",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
