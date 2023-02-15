from __future__ import annotations

__all__ = ["MOVE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MOVE_PARAM_ST(ParamRow):
    StayId: int = ParamField(
        int, "stayId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WalkF: int = ParamField(
        int, "walkF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WalkB: int = ParamField(
        int, "walkB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WalkL: int = ParamField(
        int, "walkL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WalkR: int = ParamField(
        int, "walkR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DashF: int = ParamField(
        int, "dashF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DashB: int = ParamField(
        int, "dashB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DashL: int = ParamField(
        int, "dashL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DashR: int = ParamField(
        int, "dashR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SuperDash: int = ParamField(
        int, "superDash", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EscapeF: int = ParamField(
        int, "escapeF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EscapeB: int = ParamField(
        int, "escapeB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EscapeL: int = ParamField(
        int, "escapeL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EscapeR: int = ParamField(
        int, "escapeR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TurnL: int = ParamField(
        int, "turnL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TrunR: int = ParamField(
        int, "trunR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LargeTurnL: int = ParamField(
        int, "largeTurnL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LargeTurnR: int = ParamField(
        int, "largeTurnR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    StepMove: int = ParamField(
        int, "stepMove", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyStay: int = ParamField(
        int, "flyStay", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyWalkF: int = ParamField(
        int, "flyWalkF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyWalkFL: int = ParamField(
        int, "flyWalkFL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyWalkFR: int = ParamField(
        int, "flyWalkFR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyWalkFL2: int = ParamField(
        int, "flyWalkFL2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyWalkFR2: int = ParamField(
        int, "flyWalkFR2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyDashF: int = ParamField(
        int, "flyDashF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyDashFL: int = ParamField(
        int, "flyDashFL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyDashFR: int = ParamField(
        int, "flyDashFR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyDashFL2: int = ParamField(
        int, "flyDashFL2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyDashFR2: int = ParamField(
        int, "flyDashFR2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DashEscapeF: int = ParamField(
        int, "dashEscapeF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DashEscapeB: int = ParamField(
        int, "dashEscapeB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DashEscapeL: int = ParamField(
        int, "dashEscapeL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DashEscapeR: int = ParamField(
        int, "dashEscapeR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AnalogMoveParamId: int = ParamField(
        int, "analogMoveParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TurnNoAnimAngle: int = ParamField(
        byte, "turnNoAnimAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Turn45Angle: int = ParamField(
        byte, "turn45Angle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Turn90Angle: int = ParamField(
        byte, "turn90Angle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TurnWaitNoAnimAngle: int = ParamField(
        byte, "turnWaitNoAnimAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
