from __future__ import annotations

__all__ = ["MOVE_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field
from soulstruct.darksouls1ptde.game_types import *

MOVE_PARAM_ST = {
    "param_type": "MOVE_PARAM_ST",
    "file_name": "MoveParam",
    "nickname": "Movement",
    "fields": [
        ParamFieldInfo("stayId", "StillAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("walkF", "WalkForwardAnimatiom", True, Animation, "Animation ID."),
        ParamFieldInfo("walkB", "WalkBackwardAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("walkL", "StrafeLeftAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("walkR", "StrafeRightAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("dashF", "RunForwardAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("dashB", "RunBackwardAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("dashL", "StrafeRunLeftAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("dashR", "StrafeRunRightAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("superDash", "SprintForwardAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("escapeF", "RollForwardAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("escapeB", "RollBackwardAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("escapeL", "RollLeftAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("escapeR", "RollRightAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("turnL", "TurnLeftAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("trunR", "TurnRightAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("largeTurnL", "LargeTurnLeftAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("largeTurnR", "LargeTurnRightAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("stepMove", "BackstepAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyStay", "HoverAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyWalkF", "FlyForwardAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyWalkFL", "FlyForwardLeftAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyWalkFR", "FlyForwardRightAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyWalkFL2", "FlyForwardLeft2Animation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyWalkFR2", "FlyForwardRight2Animation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyDashF", "FlyForwardFastAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyDashFL", "FlyForwardLeftFastAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyDashFR", "FlyForwardRightFastAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyDashFL2", "FlyForwardLeftFast2Animation", True, Animation, "Animation ID."),
        ParamFieldInfo("flyDashFR2", "FlyForwardRightFast2Animation", True, Animation, "Animation ID."),
        ParamFieldInfo("dashEscapeF", "RunningRollForwardAnimation", True, Animation, "Animation ID."),
        ParamFieldInfo("dashEscapeB", "RunningRollBackwardAnimation", True, Animation, "Animation ID. (Never used.)"),
        ParamFieldInfo("dashEscapeL", "RunningRollLeftAnimation", True, Animation, "Animation ID. (Never used.)"),
        ParamFieldInfo("dashEscapeR", "RunningRollRightAnimation", True, Animation, "Animation ID. (Never used.)"),
        ParamFieldInfo(
            "analogMoveParamId",
            "AnalogMovement",
            True,
            int,
            "Movement settings for analog stick version of movement. (Unknown enum.)",
        ),
        ParamFieldInfo("pad[4]", "Pad1", False, pad_field(4), "Null padding."),
    ],
}
