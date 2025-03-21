from __future__ import annotations

__all__ = ["OBJ_ACT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import ObjActSuccessCondition, ObjActSuccessCondition


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
        int, "spQualifiedPassEventFlag", default=-1,
        tooltip="Action will always be successful if this flag is enabled.",
    )
    MaxActionDistance: int = ParamField(
        ushort, "validDist", default=150,
        tooltip="Maximum distance from action model point at which the object action will be prompted.",
    )
    PlayerActionAnimation: int = ParamField(
        ushort, "playerAnimId", game_type=Animation, default=0,
        tooltip="Animation played by a player character when they successfully activate the object.",
    )
    NonPlayerActionAnimation: int = ParamField(
        ushort, "chrAnimId", game_type=Animation, default=0,
        tooltip="Animation played by a non-player character when they successfully activate the object.",
    )
    SuccessConditionID1: int = ParamField(
        ushort, "spQualifiedId", default=0, dynamic_callback=ObjActSuccessCondition(1),
        tooltip="TODO",
    )
    SuccessConditionID2: int = ParamField(
        ushort, "spQualifiedId2", default=0, dynamic_callback=ObjActSuccessCondition(2),
        tooltip="TODO",
    )
    ObjectActionModelPoint: int = ParamField(
        byte, "objDummyId", game_type=ModelDummy, default=0,
        tooltip="Model point that specifies where the action occurs on the object (for snapping the player and "
                "distance check).",
    )
    ObjectActionAnimation: int = ParamField(
        byte, "objAnimId", game_type=Animation, default=0,
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
