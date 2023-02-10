from __future__ import annotations

__all__ = ["CACL_CORRECT_GRAPH_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field


CACL_CORRECT_GRAPH_ST = {
    "param_type": "CACL_CORRECT_GRAPH_ST",  # note typo in name
    "file_name": "CalcCorrectGraph",
    "nickname": "GrowthCurves",
    "fields": [
        ParamFieldInfo(
            "stageMaxVal0", "StageMaxIntercept0", True, float, "Y-intercept in equation of 'stage max' line 0."
        ),
        ParamFieldInfo(
            "stageMaxVal1", "StageMaxIntercept1", True, float, "Y-intercept in equation of 'stage max' line 1."
        ),
        ParamFieldInfo(
            "stageMaxVal2", "StageMaxIntercept2", True, float, "Y-intercept in equation of 'stage max' line 2."
        ),
        ParamFieldInfo(
            "stageMaxVal3", "StageMaxIntercept3", True, float, "Y-intercept in equation of 'stage max' line 3."
        ),
        ParamFieldInfo(
            "stageMaxVal4", "StageMaxIntercept4", True, float, "Y-intercept in equation of 'stage max' line 4."
        ),
        ParamFieldInfo("stageMaxGrowVal0", "StageMaxSlope0", True, float, "Slope in equation of 'stage max' line 0."),
        ParamFieldInfo("stageMaxGrowVal1", "StageMaxSlope1", True, float, "Slope in equation of 'stage max' line 1."),
        ParamFieldInfo("stageMaxGrowVal2", "StageMaxSlope2", True, float, "Slope in equation of 'stage max' line 2."),
        ParamFieldInfo("stageMaxGrowVal3", "StageMaxSlope3", True, float, "Slope in equation of 'stage max' line 3."),
        ParamFieldInfo("stageMaxGrowVal4", "StageMaxSlope4", True, float, "Slope in equation of 'stage max' line 4."),
        ParamFieldInfo(
            "adjPt_maxGrowVal0",
            "AdjustmentMaxSlope0",
            True,
            float,
            "Adjustment factor for slope in equation of 'stage max' line 0.",
        ),
        ParamFieldInfo(
            "adjPt_maxGrowVal1",
            "AdjustmentMaxSlope1",
            True,
            float,
            "Adjustment factor for slope in equation of 'stage max' line 1.",
        ),
        ParamFieldInfo(
            "adjPt_maxGrowVal2",
            "AdjustmentMaxSlope2",
            True,
            float,
            "Adjustment factor for slope in equation of 'stage max' line 2.",
        ),
        ParamFieldInfo(
            "adjPt_maxGrowVal3",
            "AdjustmentMaxSlope3",
            True,
            float,
            "Adjustment factor for slope in equation of 'stage max' line 3.",
        ),
        ParamFieldInfo(
            "adjPt_maxGrowVal4",
            "AdjustmentMaxSlope4",
            True,
            float,
            "Adjustment factor for slope in equation of 'stage max' line 4.",
        ),
        ParamFieldInfo(
            "init_inclination_soul",
            "InitialLevellingCostSlope",
            True,
            float,
            "Initial slope of equation determining levelling costs (α1).",
        ),
        ParamFieldInfo(
            "adjustment_value",
            "LevellingCostEarlyAdjustment",
            True,
            float,
            "'Early' adjustment value of equation determining levelling costs (α2).",
        ),
        ParamFieldInfo(
            "boundry_inclination_soul",  # (sic)
            "LateLevellingCostSlope",
            True,
            float,
            "Slope of equation determining required levelling souls after 'LateLevellingCostThreshold' value (α3).",
        ),
        ParamFieldInfo(
            "boundry_value",  # (sic)
            "LateLevellingCostThreshold",
            True,
            float,
            "Threshold at which 'LateLevellingCostSlope' takes over for levelling (t).",
        ),
        ParamFieldInfo("pad[4]", "Pad0", False, pad_field(4), "Null padding."),
    ],
}
