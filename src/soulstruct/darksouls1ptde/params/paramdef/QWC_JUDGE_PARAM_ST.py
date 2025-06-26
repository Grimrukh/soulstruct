from __future__ import annotations

__all__ = ["QWC_JUDGE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class QWC_JUDGE_PARAM_ST(ParamRow):
    PcJudgeUnderWB: int = ParamField(
        short, "pcJudgeUnderWB", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    PcJudgeTopWB: int = ParamField(
        short, "pcJudgeTopWB", default=200,
        tooltip="TOOLTIP-TODO",
    )
    PcJudgeUnderLR: int = ParamField(
        short, "pcJudgeUnderLR", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    PcJudgeTopLR: int = ParamField(
        short, "pcJudgeTopLR", default=200,
        tooltip="TOOLTIP-TODO",
    )
    AreaJudgeUnderWB: int = ParamField(
        short, "areaJudgeUnderWB", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    AreaJudgeTopWB: int = ParamField(
        short, "areaJudgeTopWB", default=200,
        tooltip="TOOLTIP-TODO",
    )
    AreaJudgeUnderLR: int = ParamField(
        short, "areaJudgeUnderLR", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    AreaJudgeTopLR: int = ParamField(
        short, "areaJudgeTopLR", default=200,
        tooltip="TOOLTIP-TODO",
    )
