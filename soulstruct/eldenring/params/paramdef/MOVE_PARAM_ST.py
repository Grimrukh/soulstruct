from __future__ import annotations

__all__ = ["MOVE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MOVE_PARAM_ST(ParamRowData):
    StillAnimation: int = ParamField(
        int, "stayId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WalkForwardAnimatiom: int = ParamField(
        int, "walkF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WalkBackwardAnimation: int = ParamField(
        int, "walkB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    StrafeLeftAnimation: int = ParamField(
        int, "walkL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    StrafeRightAnimation: int = ParamField(
        int, "walkR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RunForwardAnimation: int = ParamField(
        int, "dashF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RunBackwardAnimation: int = ParamField(
        int, "dashB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    StrafeRunLeftAnimation: int = ParamField(
        int, "dashL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    StrafeRunRightAnimation: int = ParamField(
        int, "dashR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SprintForwardAnimation: int = ParamField(
        int, "superDash", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RollForwardAnimation: int = ParamField(
        int, "escapeF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RollBackwardAnimation: int = ParamField(
        int, "escapeB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RollLeftAnimation: int = ParamField(
        int, "escapeL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RollRightAnimation: int = ParamField(
        int, "escapeR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TurnLeftAnimation: int = ParamField(
        int, "turnL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TurnRightAnimation: int = ParamField(
        int, "trunR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LargeTurnLeftAnimation: int = ParamField(
        int, "largeTurnL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    LargeTurnRightAnimation: int = ParamField(
        int, "largeTurnR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BackstepAnimation: int = ParamField(
        int, "stepMove", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HoverAnimation: int = ParamField(
        int, "flyStay", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyForwardAnimation: int = ParamField(
        int, "flyWalkF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyForwardLeftAnimation: int = ParamField(
        int, "flyWalkFL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyForwardRightAnimation: int = ParamField(
        int, "flyWalkFR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyForwardLeft2Animation: int = ParamField(
        int, "flyWalkFL2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyForwardRight2Animation: int = ParamField(
        int, "flyWalkFR2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyForwardFastAnimation: int = ParamField(
        int, "flyDashF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyForwardLeftFastAnimation: int = ParamField(
        int, "flyDashFL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyForwardRightFastAnimation: int = ParamField(
        int, "flyDashFR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyForwardLeftFast2Animation: int = ParamField(
        int, "flyDashFL2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FlyForwardRightFast2Animation: int = ParamField(
        int, "flyDashFR2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RunningRollForwardAnimation: int = ParamField(
        int, "dashEscapeF", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RunningRollBackwardAnimation: int = ParamField(
        int, "dashEscapeB", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RunningRollLeftAnimation: int = ParamField(
        int, "dashEscapeL", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RunningRollRightAnimation: int = ParamField(
        int, "dashEscapeR", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AnalogMovement: int = ParamField(
        int, "analogMoveParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TurnNoAnimationAngle: int = ParamField(
        byte, "turnNoAnimAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Turn45DegreeAngle: int = ParamField(
        byte, "turn45Angle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Turn90DegreeAngle: int = ParamField(
        byte, "turn90Angle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TurnWaitNoAnimationAngle: int = ParamField(
        byte, "turnWaitNoAnimAngle", default=0,
        tooltip="TOOLTIP-TODO",
    )
