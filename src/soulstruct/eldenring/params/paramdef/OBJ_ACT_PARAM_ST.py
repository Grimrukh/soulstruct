from __future__ import annotations

__all__ = ["OBJ_ACT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class OBJ_ACT_PARAM_ST(ParamRow):
    PromptMessage: int = ParamField(
        int, "actionEnableMsgId", default=-1,
        tooltip="Message displayed in dialog box that prompts action (e.g. 'Open').",
    )
    FailureMessage: int = ParamField(
        int, "actionFailedMsgId", default=-1,
        tooltip="Message displayed in dialog box upon failed action (e.g. 'It's locked').",
    )
    FlagForAutomaticSuccess: int = ParamField(
        uint, "spQualifiedPassEventFlag", default=0,
        tooltip="Action will always be successful if this flag is enabled.",
    )
    PlayerActionAnimation: int = ParamField(
        uint, "playerAnimId", game_type=Animation, default=0,
        tooltip="Animation played by a player character when they successfully activate the object.",
    )
    NonPlayerActionAnimation: int = ParamField(
        uint, "chrAnimId", game_type=Animation, default=0,
        tooltip="Animation played by a non-player character when they successfully activate the object.",
    )
    MaxActionDistance: int = ParamField(
        ushort, "validDist", default=150,
        tooltip="Maximum distance from action model point at which the object action will be prompted.",
    )
    SpQualifiedIdold: int = ParamField(
        ushort, "spQualifiedId_old", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpQualifiedId2old: int = ParamField(
        ushort, "spQualifiedId2_old", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ObjectActionModelPoint: int = ParamField(
        byte, "objDummyId", game_type=ModelDummy, default=0,
        tooltip="Model point that specifies where the action occurs on the object (for snapping the player and "
                "distance check).",
    )
    IsEventKickSync: int = ParamField(
        byte, "isEventKickSync", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ObjectActionAnimation: int = ParamField(
        uint, "objAnimId", game_type=Animation, default=0,
        tooltip="Animation played by the object when it is successfully activated.",
    )
    MaxPlayerAngle: int = ParamField(
        byte, "validPlayerAngle", default=30,
        tooltip="Maximum angle between the character's forward direction and the direction to the object action point "
                "for the action prompt to appear.",
    )
    SuccessCondition1Type: int = ParamField(
        byte, "spQualifiedType", OBJACT_SP_QUALIFIED_TYPE, default=0,
        tooltip="Type of first success condition.",
    )
    SuccessCondition2Type: int = ParamField(
        byte, "spQualifiedType2", OBJACT_SP_QUALIFIED_TYPE, default=0,
        tooltip="Type of second success condition.",
    )
    MaxObjectAngle: int = ParamField(
        byte, "validObjAngle", default=30,
        tooltip="Maximum angle between the object's forward direction and the direction to the player for the action "
                "prompt to appear.",
    )
    CharacterSnapType: int = ParamField(
        byte, "chrSorbType", OBJACT_CHR_SORB_TYPE, default=0,
        tooltip="Type of method used to snap the character to the object before animations are played.",
    )
    EventTriggerDelay: int = ParamField(
        byte, "eventKickTiming", OBJACT_EVENT_KICK_TIMING, default=0,
        tooltip="I believe this is the delay between successful object activation and the outgoing 'success' trigger "
                "used by game events.",
    )
    _Pad0: bytes = ParamPad(2, "pad1[2]")
    ActionButtonParamID: int = ParamField(
        int, "actionButtonParamId", game_type=ActionButtonParam, default=-1,
        tooltip="TODO",
    )
    EnableTreasureDelaySec: float = ParamField(
        float, "enableTreasureDelaySec", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PreActionSfxDmypolyId: int = ParamField(
        int, "preActionSfxDmypolyId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PreActionSfxId: int = ParamField(
        int, "preActionSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(40, "pad2_old[40]")
    SpQualifiedIdnew: int = ParamField(
        int, "spQualifiedId_new", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpQualifiedId2new: int = ParamField(
        int, "spQualifiedId2_new", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(32, "pad2[32]")
