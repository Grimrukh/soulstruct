from __future__ import annotations

__all__ = ["QWC_JUDGE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class QWC_JUDGE_PARAM_ST(ParamRow):
    PcJudgeUnderWB: int = ParamField(
        int16, "pcJudgeUnderWB", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    PcJudgeTopWB: int = ParamField(
        int16, "pcJudgeTopWB", default=200,
        tooltip="TOOLTIP-TODO",
    )
    PcJudgeUnderLR: int = ParamField(
        int16, "pcJudgeUnderLR", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    PcJudgeTopLR: int = ParamField(
        int16, "pcJudgeTopLR", default=200,
        tooltip="TOOLTIP-TODO",
    )
    AreaJudgeUnderWB: int = ParamField(
        int16, "areaJudgeUnderWB", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    AreaJudgeTopWB: int = ParamField(
        int16, "areaJudgeTopWB", default=200,
        tooltip="TOOLTIP-TODO",
    )
    AreaJudgeUnderLR: int = ParamField(
        int16, "areaJudgeUnderLR", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    AreaJudgeTopLR: int = ParamField(
        int16, "areaJudgeTopLR", default=200,
        tooltip="TOOLTIP-TODO",
    )
