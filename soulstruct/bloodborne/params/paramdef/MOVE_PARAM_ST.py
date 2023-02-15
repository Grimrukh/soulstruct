from __future__ import annotations

__all__ = ["MOVE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MOVE_PARAM_ST(ParamRow):
    StillAnimation: int = ParamField(
        int, "stayId", default=-1,
        tooltip="Animation ID.",
    )
    WalkForwardAnimatiom: int = ParamField(
        int, "walkF", default=-1,
        tooltip="Animation ID.",
    )
    WalkBackwardAnimation: int = ParamField(
        int, "walkB", default=-1,
        tooltip="Animation ID.",
    )
    StrafeLeftAnimation: int = ParamField(
        int, "walkL", default=-1,
        tooltip="Animation ID.",
    )
    StrafeRightAnimation: int = ParamField(
        int, "walkR", default=-1,
        tooltip="Animation ID.",
    )
    RunForwardAnimation: int = ParamField(
        int, "dashF", default=-1,
        tooltip="Animation ID.",
    )
    RunBackwardAnimation: int = ParamField(
        int, "dashB", default=-1,
        tooltip="Animation ID.",
    )
    StrafeRunLeftAnimation: int = ParamField(
        int, "dashL", default=-1,
        tooltip="Animation ID.",
    )
    StrafeRunRightAnimation: int = ParamField(
        int, "dashR", default=-1,
        tooltip="Animation ID.",
    )
    SprintForwardAnimation: int = ParamField(
        int, "superDash", default=-1,
        tooltip="Animation ID.",
    )
    RollForwardAnimation: int = ParamField(
        int, "escapeF", default=-1,
        tooltip="Animation ID.",
    )
    RollBackwardAnimation: int = ParamField(
        int, "escapeB", default=-1,
        tooltip="Animation ID.",
    )
    RollLeftAnimation: int = ParamField(
        int, "escapeL", default=-1,
        tooltip="Animation ID.",
    )
    RollRightAnimation: int = ParamField(
        int, "escapeR", default=-1,
        tooltip="Animation ID.",
    )
    TurnLeftAnimation: int = ParamField(
        int, "turnL", default=-1,
        tooltip="Animation ID.",
    )
    TurnRightAnimation: int = ParamField(
        int, "trunR", default=-1,
        tooltip="Animation ID.",
    )
    LargeTurnLeftAnimation: int = ParamField(
        int, "largeTurnL", default=-1,
        tooltip="Animation ID.",
    )
    LargeTurnRightAnimation: int = ParamField(
        int, "largeTurnR", default=-1,
        tooltip="Animation ID.",
    )
    BackstepAnimation: int = ParamField(
        int, "stepMove", default=-1,
        tooltip="Animation ID.",
    )
    HoverAnimation: int = ParamField(
        int, "flyStay", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardAnimation: int = ParamField(
        int, "flyWalkF", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeftAnimation: int = ParamField(
        int, "flyWalkFL", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRightAnimation: int = ParamField(
        int, "flyWalkFR", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeft2Animation: int = ParamField(
        int, "flyWalkFL2", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRight2Animation: int = ParamField(
        int, "flyWalkFR2", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardFastAnimation: int = ParamField(
        int, "flyDashF", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeftFastAnimation: int = ParamField(
        int, "flyDashFL", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRightFastAnimation: int = ParamField(
        int, "flyDashFR", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeftFast2Animation: int = ParamField(
        int, "flyDashFL2", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRightFast2Animation: int = ParamField(
        int, "flyDashFR2", default=-1,
        tooltip="Animation ID.",
    )
    RunningRollForwardAnimation: int = ParamField(
        int, "dashEscapeF", default=-1,
        tooltip="Animation ID.",
    )
    RunningRollBackwardAnimation: int = ParamField(
        int, "dashEscapeB", default=-1,
        tooltip="Animation ID. (Never used.)",
    )
    RunningRollLeftAnimation: int = ParamField(
        int, "dashEscapeL", default=-1,
        tooltip="Animation ID. (Never used.)",
    )
    RunningRollRightAnimation: int = ParamField(
        int, "dashEscapeR", default=-1,
        tooltip="Animation ID. (Never used.)",
    )
    AnalogMovement: int = ParamField(
        int, "analogMoveParamId", default=-1,
        tooltip="Movement settings for analog stick version of movement. (Unknown enum.)",
    )
    TurnNoAnimationAngle: int = ParamField(
        byte, "turnNoAnimAngle", default=0,
        tooltip="TODO",
    )
    Turn45DegreeAngle: int = ParamField(
        byte, "turn45Angle", default=0,
        tooltip="TODO",
    )
    Turn90DegreeAngle: int = ParamField(
        byte, "turn90Angle", default=0,
        tooltip="TODO",
    )
    TurnWaitNoAnimationAngle: int = ParamField(
        byte, "turnWaitNoAnimAngle", default=0,
        tooltip="TODO",
    )
