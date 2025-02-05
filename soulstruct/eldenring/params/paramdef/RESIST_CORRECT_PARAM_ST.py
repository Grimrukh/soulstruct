from __future__ import annotations

__all__ = ["RESIST_CORRECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class RESIST_CORRECT_PARAM_ST(ParamRow):
    AddPoint1: float = ParamField(
        float, "addPoint1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AddPoint2: float = ParamField(
        float, "addPoint2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AddPoint3: float = ParamField(
        float, "addPoint3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AddPoint4: float = ParamField(
        float, "addPoint4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AddPoint5: float = ParamField(
        float, "addPoint5", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AddRate1: float = ParamField(
        float, "addRate1", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AddRate2: float = ParamField(
        float, "addRate2", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AddRate3: float = ParamField(
        float, "addRate3", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AddRate4: float = ParamField(
        float, "addRate4", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    AddRate5: float = ParamField(
        float, "addRate5", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
