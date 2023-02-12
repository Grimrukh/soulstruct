from __future__ import annotations

__all__ = ["MOVE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MOVE_PARAM_ST(ParamRow):
    StillAnimation: Animation = ParamField(
        int, "stayId", default=-1,
        tooltip="Animation ID.",
    )
    WalkForwardAnimatiom: Animation = ParamField(
        int, "walkF", default=-1,
        tooltip="Animation ID.",
    )
    WalkBackwardAnimation: Animation = ParamField(
        int, "walkB", default=-1,
        tooltip="Animation ID.",
    )
    StrafeLeftAnimation: Animation = ParamField(
        int, "walkL", default=-1,
        tooltip="Animation ID.",
    )
    StrafeRightAnimation: Animation = ParamField(
        int, "walkR", default=-1,
        tooltip="Animation ID.",
    )
    RunForwardAnimation: Animation = ParamField(
        int, "dashF", default=-1,
        tooltip="Animation ID.",
    )
    RunBackwardAnimation: Animation = ParamField(
        int, "dashB", default=-1,
        tooltip="Animation ID.",
    )
    StrafeRunLeftAnimation: Animation = ParamField(
        int, "dashL", default=-1,
        tooltip="Animation ID.",
    )
    StrafeRunRightAnimation: Animation = ParamField(
        int, "dashR", default=-1,
        tooltip="Animation ID.",
    )
    SprintForwardAnimation: Animation = ParamField(
        int, "superDash", default=-1,
        tooltip="Animation ID.",
    )
    RollForwardAnimation: Animation = ParamField(
        int, "escapeF", default=-1,
        tooltip="Animation ID.",
    )
    RollBackwardAnimation: Animation = ParamField(
        int, "escapeB", default=-1,
        tooltip="Animation ID.",
    )
    RollLeftAnimation: Animation = ParamField(
        int, "escapeL", default=-1,
        tooltip="Animation ID.",
    )
    RollRightAnimation: Animation = ParamField(
        int, "escapeR", default=-1,
        tooltip="Animation ID.",
    )
    TurnLeftAnimation: Animation = ParamField(
        int, "turnL", default=-1,
        tooltip="Animation ID.",
    )
    TurnRightAnimation: Animation = ParamField(
        int, "trunR", default=-1,
        tooltip="Animation ID.",
    )
    LargeTurnLeftAnimation: Animation = ParamField(
        int, "largeTurnL", default=-1,
        tooltip="Animation ID.",
    )
    LargeTurnRightAnimation: Animation = ParamField(
        int, "largeTurnR", default=-1,
        tooltip="Animation ID.",
    )
    BackstepAnimation: Animation = ParamField(
        int, "stepMove", default=-1,
        tooltip="Animation ID.",
    )
    HoverAnimation: Animation = ParamField(
        int, "flyStay", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardAnimation: Animation = ParamField(
        int, "flyWalkF", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeftAnimation: Animation = ParamField(
        int, "flyWalkFL", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRightAnimation: Animation = ParamField(
        int, "flyWalkFR", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeft2Animation: Animation = ParamField(
        int, "flyWalkFL2", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRight2Animation: Animation = ParamField(
        int, "flyWalkFR2", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardFastAnimation: Animation = ParamField(
        int, "flyDashF", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeftFastAnimation: Animation = ParamField(
        int, "flyDashFL", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRightFastAnimation: Animation = ParamField(
        int, "flyDashFR", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeftFast2Animation: Animation = ParamField(
        int, "flyDashFL2", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRightFast2Animation: Animation = ParamField(
        int, "flyDashFR2", default=-1,
        tooltip="Animation ID.",
    )
    RunningRollForwardAnimation: Animation = ParamField(
        int, "dashEscapeF", default=-1,
        tooltip="Animation ID.",
    )
    RunningRollBackwardAnimation: Animation = ParamField(
        int, "dashEscapeB", default=-1,
        tooltip="Animation ID. (Never used.)",
    )
    RunningRollLeftAnimation: Animation = ParamField(
        int, "dashEscapeL", default=-1,
        tooltip="Animation ID. (Never used.)",
    )
    RunningRollRightAnimation: Animation = ParamField(
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
