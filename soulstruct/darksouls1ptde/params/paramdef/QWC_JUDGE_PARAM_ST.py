from __future__ import annotations

__all__ = ["QWC_JUDGE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class QWC_JUDGE_PARAM_ST(ParamRow):
    pcJudgeUnderWB: int = ParamField(
        short, "pcJudgeUnderWB", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    pcJudgeTopWB: int = ParamField(
        short, "pcJudgeTopWB", default=200,
        tooltip="TOOLTIP-TODO",
    )
    pcJudgeUnderLR: int = ParamField(
        short, "pcJudgeUnderLR", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    pcJudgeTopLR: int = ParamField(
        short, "pcJudgeTopLR", default=200,
        tooltip="TOOLTIP-TODO",
    )
    areaJudgeUnderWB: int = ParamField(
        short, "areaJudgeUnderWB", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    areaJudgeTopWB: int = ParamField(
        short, "areaJudgeTopWB", default=200,
        tooltip="TOOLTIP-TODO",
    )
    areaJudgeUnderLR: int = ParamField(
        short, "areaJudgeUnderLR", default=-200,
        tooltip="TOOLTIP-TODO",
    )
    areaJudgeTopLR: int = ParamField(
        short, "areaJudgeTopLR", default=200,
        tooltip="TOOLTIP-TODO",
    )
