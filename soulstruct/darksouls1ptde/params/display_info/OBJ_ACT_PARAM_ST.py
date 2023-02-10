from __future__ import annotations

__all__ = ["OBJ_ACT_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, DynamicParamFieldInfo, pad_field
from soulstruct.darksouls1ptde.game_types import *
from ..enums import *


class DynamicObjActRef(DynamicParamFieldInfo):

    POSSIBLE_TYPES = {GoodParam, SpecialEffectParam}

    def __call__(self, entry) -> ParamFieldInfo:
        n = "2" if self.type_field_name.endswith("2") else "1"
        if entry[self.type_field_name] == OBJACT_SP_QUALIFIED_TYPE.NoCondition:
            return ParamFieldInfo(
                self.name,
                f"NoCondition{n}",
                True,
                int,
                f"No condition type selected.",
            )
        elif entry[self.type_field_name] == OBJACT_SP_QUALIFIED_TYPE.HasGood:
            return ParamFieldInfo(
                self.name,
                f"RequiredGood{n}",
                True,
                GoodParam,
                f"Condition: object action will succeed if user has this good in their inventory (does not "
                "include Bottomless Box).",
            )
        elif entry[self.type_field_name] == OBJACT_SP_QUALIFIED_TYPE.HasSpecialEffect:
            return ParamFieldInfo(
                self.name,
                f"RequiredSpecialEffect{n}",
                True,
                SpecialEffectParam,
                "Condition: object action will succeed if user has this special effect.",
            )
        else:
            return ParamFieldInfo(
                self.name,
                f"UnknownCondition{n}",
                True,
                int,
                "Could not determine success condition ID type (usually HasGood or HasSpecialEffect).",
            )


OBJ_ACT_PARAM_ST = {
    "param_type": "OBJ_ACT_PARAM_ST",
    "file_name": "ObjActParam",
    "nickname": "ObjectActivations",
    "fields": [
        ParamFieldInfo(
            "actionEnableMsgId",
            "PromptMessage",
            True,
            EventText,
            "Message displayed in dialog box that prompts action (e.g. 'Open').",
        ),
        ParamFieldInfo(
            "actionFailedMsgId",
            "FailureMessage",
            True,
            EventText,
            "Message displayed in dialog box upon failed action (e.g. 'It's locked').",
        ),
        ParamFieldInfo(
            "spQualifiedPassEventFlag",
            "FlagForAutomaticSuccess",
            True,
            Flag,
            "Action will always be successful if this flag is enabled.",
        ),
        ParamFieldInfo(
            "validDist",
            "MaxActionDistance",
            True,
            int,
            "Maximum distance from action model point at which the object action will be prompted.",
        ),
        ParamFieldInfo(
            "playerAnimId",
            "PlayerActionAnimation",
            True,
            int,  # TODO: Animation
            "Animation played by a player character when they successfully activate the object.",
        ),
        ParamFieldInfo(
            "chrAnimId",
            "NonPlayerActionAnimation",
            True,
            int,  # TODO: Animation
            "Animation played by a non-player character when they successfully activate the object.",
        ),
        ParamFieldInfo(
            "spQualifiedType",
            "SuccessCondition1Type",
            True,
            OBJACT_SP_QUALIFIED_TYPE,
            "Type of first success condition.",
        ),
        DynamicObjActRef("spQualifiedId", "spQualifiedType"),
        ParamFieldInfo(
            "spQualifiedType2",
            "SuccessCondition2Type",
            True,
            OBJACT_SP_QUALIFIED_TYPE,
            "Type of second success condition.",
        ),
        DynamicObjActRef("spQualifiedId2", "spQualifiedType2"),
        ParamFieldInfo(
            "objDummyId",
            "ObjectActionModelPoint",
            True,
            int,
            "Model point that specifies where the action occurs on the object (for snapping the player and "
            "distance check).",
        ),
        ParamFieldInfo(
            "objAnimId",
            "ObjectActionAnimation",
            True,
            int,  # TODO: Animation
            "Animation played by the object when it is successfully activated.",
        ),
        ParamFieldInfo(
            "validPlayerAngle",
            "MaxPlayerAngle",
            True,
            int,
            "Maximum angle between the character's forward direction and the direction to the object action point "
            "for the action prompt to appear.",
        ),
        ParamFieldInfo(
            "validObjAngle",
            "MaxObjectAngle",
            True,
            int,
            "Maximum angle between the object's forward direction and the direction to the player for the action "
            "prompt to appear.",
        ),
        ParamFieldInfo(
            "chrSorbType",
            "CharacterSnapType",
            True,
            OBJACT_CHR_SORB_TYPE,
            "Type of method used to snap the character to the object before animations are played.",
        ),
        ParamFieldInfo(
            "eventKickTiming",
            "EventTriggerDelay",
            True,
            int,
            "I believe this is the delay between successful object activation and the outgoing 'success' trigger "
            "used by game events.",
        ),
        ParamFieldInfo("pad1[2]", "Pad1", False, pad_field(2), "Null padding."),
    ],
}
