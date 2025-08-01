from __future__ import annotations

__all__ = ["CACL_CORRECT_GRAPH_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class CACL_CORRECT_GRAPH_ST(ParamRow):
    StageMaxIntercept0: float = ParamField(
        float32, "stageMaxVal0", default=0.0,
        tooltip="Y-intercept in equation of 'stage max' line 0.",
    )
    StageMaxIntercept1: float = ParamField(
        float32, "stageMaxVal1", default=0.0,
        tooltip="Y-intercept in equation of 'stage max' line 1.",
    )
    StageMaxIntercept2: float = ParamField(
        float32, "stageMaxVal2", default=0.0,
        tooltip="Y-intercept in equation of 'stage max' line 2.",
    )
    StageMaxIntercept3: float = ParamField(
        float32, "stageMaxVal3", default=0.0,
        tooltip="Y-intercept in equation of 'stage max' line 3.",
    )
    StageMaxIntercept4: float = ParamField(
        float32, "stageMaxVal4", default=0.0,
        tooltip="Y-intercept in equation of 'stage max' line 4.",
    )
    StageMaxSlope0: float = ParamField(
        float32, "stageMaxGrowVal0", default=0.0,
        tooltip="Slope in equation of 'stage max' line 0.",
    )
    StageMaxSlope1: float = ParamField(
        float32, "stageMaxGrowVal1", default=0.0,
        tooltip="Slope in equation of 'stage max' line 1.",
    )
    StageMaxSlope2: float = ParamField(
        float32, "stageMaxGrowVal2", default=0.0,
        tooltip="Slope in equation of 'stage max' line 2.",
    )
    StageMaxSlope3: float = ParamField(
        float32, "stageMaxGrowVal3", default=0.0,
        tooltip="Slope in equation of 'stage max' line 3.",
    )
    StageMaxSlope4: float = ParamField(
        float32, "stageMaxGrowVal4", default=0.0,
        tooltip="Slope in equation of 'stage max' line 4.",
    )
    AdjustmentMaxSlope0: float = ParamField(
        float32, "adjPt_maxGrowVal0", default=0.0,
        tooltip="Adjustment factor for slope in equation of 'stage max' line 0.",
    )
    AdjustmentMaxSlope1: float = ParamField(
        float32, "adjPt_maxGrowVal1", default=0.0,
        tooltip="Adjustment factor for slope in equation of 'stage max' line 1.",
    )
    AdjustmentMaxSlope2: float = ParamField(
        float32, "adjPt_maxGrowVal2", default=0.0,
        tooltip="Adjustment factor for slope in equation of 'stage max' line 2.",
    )
    AdjustmentMaxSlope3: float = ParamField(
        float32, "adjPt_maxGrowVal3", default=0.0,
        tooltip="Adjustment factor for slope in equation of 'stage max' line 3.",
    )
    AdjustmentMaxSlope4: float = ParamField(
        float32, "adjPt_maxGrowVal4", default=0.0,
        tooltip="Adjustment factor for slope in equation of 'stage max' line 4.",
    )
    InitialLevellingCostSlope: float = ParamField(
        float32, "init_inclination_soul", default=0.0,
        tooltip="Initial slope of equation determining levelling costs (alpha 1).",
    )
    LevellingCostEarlyAdjustment: float = ParamField(
        float32, "adjustment_value", default=0.0,
        tooltip="'Early' adjustment value of equation determining levelling costs (alpha 2).",
    )
    LateLevellingCostSlope: float = ParamField(
        float32, "boundry_inclination_soul", default=0.0,
        tooltip="Slope of equation determining required levelling souls after 'LateLevellingCostThreshold' value "
                "(alpha 3).",
    )
    LateLevellingCostThreshold: float = ParamField(
        float32, "boundry_value", default=0.0,
        tooltip="Threshold at which 'LateLevellingCostSlope' takes over for levelling (t).",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
