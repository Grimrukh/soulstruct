from __future__ import annotations

__all__ = ["MOVE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class MOVE_PARAM_ST(ParamRow):
    StillAnimation: int = ParamField(
        int32, "stayId", default=-1,
        tooltip="Animation ID.",
    )
    WalkForwardAnimatiom: int = ParamField(
        int32, "walkF", default=-1,
        tooltip="Animation ID.",
    )
    WalkBackwardAnimation: int = ParamField(
        int32, "walkB", default=-1,
        tooltip="Animation ID.",
    )
    StrafeLeftAnimation: int = ParamField(
        int32, "walkL", default=-1,
        tooltip="Animation ID.",
    )
    StrafeRightAnimation: int = ParamField(
        int32, "walkR", default=-1,
        tooltip="Animation ID.",
    )
    RunForwardAnimation: int = ParamField(
        int32, "dashF", default=-1,
        tooltip="Animation ID.",
    )
    RunBackwardAnimation: int = ParamField(
        int32, "dashB", default=-1,
        tooltip="Animation ID.",
    )
    StrafeRunLeftAnimation: int = ParamField(
        int32, "dashL", default=-1,
        tooltip="Animation ID.",
    )
    StrafeRunRightAnimation: int = ParamField(
        int32, "dashR", default=-1,
        tooltip="Animation ID.",
    )
    SprintForwardAnimation: int = ParamField(
        int32, "superDash", default=-1,
        tooltip="Animation ID.",
    )
    RollForwardAnimation: int = ParamField(
        int32, "escapeF", default=-1,
        tooltip="Animation ID.",
    )
    RollBackwardAnimation: int = ParamField(
        int32, "escapeB", default=-1,
        tooltip="Animation ID.",
    )
    RollLeftAnimation: int = ParamField(
        int32, "escapeL", default=-1,
        tooltip="Animation ID.",
    )
    RollRightAnimation: int = ParamField(
        int32, "escapeR", default=-1,
        tooltip="Animation ID.",
    )
    TurnLeftAnimation: int = ParamField(
        int32, "turnL", default=-1,
        tooltip="Animation ID.",
    )
    TurnRightAnimation: int = ParamField(
        int32, "trunR", default=-1,
        tooltip="Animation ID.",
    )
    LargeTurnLeftAnimation: int = ParamField(
        int32, "largeTurnL", default=-1,
        tooltip="Animation ID.",
    )
    LargeTurnRightAnimation: int = ParamField(
        int32, "largeTurnR", default=-1,
        tooltip="Animation ID.",
    )
    BackstepAnimation: int = ParamField(
        int32, "stepMove", default=-1,
        tooltip="Animation ID.",
    )
    HoverAnimation: int = ParamField(
        int32, "flyStay", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardAnimation: int = ParamField(
        int32, "flyWalkF", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeftAnimation: int = ParamField(
        int32, "flyWalkFL", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRightAnimation: int = ParamField(
        int32, "flyWalkFR", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeft2Animation: int = ParamField(
        int32, "flyWalkFL2", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRight2Animation: int = ParamField(
        int32, "flyWalkFR2", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardFastAnimation: int = ParamField(
        int32, "flyDashF", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeftFastAnimation: int = ParamField(
        int32, "flyDashFL", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRightFastAnimation: int = ParamField(
        int32, "flyDashFR", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardLeftFast2Animation: int = ParamField(
        int32, "flyDashFL2", default=-1,
        tooltip="Animation ID.",
    )
    FlyForwardRightFast2Animation: int = ParamField(
        int32, "flyDashFR2", default=-1,
        tooltip="Animation ID.",
    )
    RunningRollForwardAnimation: int = ParamField(
        int32, "dashEscapeF", default=-1,
        tooltip="Animation ID.",
    )
    RunningRollBackwardAnimation: int = ParamField(
        int32, "dashEscapeB", default=-1,
        tooltip="Animation ID. (Never used.)",
    )
    RunningRollLeftAnimation: int = ParamField(
        int32, "dashEscapeL", default=-1,
        tooltip="Animation ID. (Never used.)",
    )
    RunningRollRightAnimation: int = ParamField(
        int32, "dashEscapeR", default=-1,
        tooltip="Animation ID. (Never used.)",
    )
    AnalogMovement: int = ParamField(
        int32, "analogMoveParamId", default=-1,
        tooltip="Movement settings for analog stick version of movement. (Unknown enum.)",
    )
    _Pad0: bytes = ParamPad(4, "pad[4]")
