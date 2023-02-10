__all__ = ["BEHAVIOR_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, DynamicParamFieldInfo, pad_field
from soulstruct.bloodborne.params.enums import *
from soulstruct.darksouls1ptde.game_types.param_types import AttackParam, BulletParam, SpecialEffectParam


class DynamicBehaviorRef(DynamicParamFieldInfo):

    POSSIBLE_TYPES = {AttackParam, BulletParam, SpecialEffectParam}

    def __call__(self, entry) -> ParamFieldInfo:
        if entry[self.type_field_name] == BEHAVIOR_REF_TYPE.Default:
            return ParamFieldInfo(
                self.name,
                "Attack",
                True,
                AttackParam,
                "Attack ID triggered by behavior.",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.Bullet:
            return ParamFieldInfo(
                self.name,
                "Bullet",
                True,
                BulletParam,
                "Bullet ID triggered by behavior.",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.SpecialEffect:
            return ParamFieldInfo(
                self.name,
                "SpecialEffect",
                True,
                SpecialEffectParam,
                "Special Effect ID triggered by behavior. (Never used; may not work.)",
            )
        else:
            return ParamFieldInfo(
                self.name,
                "UnknownRef",
                True,
                int,
                "Could not determine reference ID type (usually Attack or Bullet).",
            )


BEHAVIOR_PARAM_ST = {
    "param_type": "BEHAVIOR_PARAM_ST",
    "file_name": "BehaviorParam",  # also BehaviorParam_PC
    "nickname": None,
    "fields": [
        ParamFieldInfo("variationId", "VariationID", True, int, ""),  # TODO: connect to model/TAE somehow.
        ParamFieldInfo(
            "behaviorJudgeId",
            "BehaviorJudgeID",
            True,
            int,
            "This is the ID specified by TAE events that trigger behaviors.",
        ),
        ParamFieldInfo(
            "ezStateBehaviorType_old", "EzstateBehaviorType", False, int, "Unused remnant from Demon's Souls."
        ),
        ParamFieldInfo(
            "refType", "ReferenceType", True, BEHAVIOR_REF_TYPE, "Is the reference ID below an Attack or Bullet ID?"
        ),
        ParamFieldInfo("pad0[2]", "Pad1", False, pad_field(2), "Null padding."),
        DynamicBehaviorRef("refId", "refType"),
        ParamFieldInfo("sfxVariationId", "VFXVariationID", True, int, "Visual effect ID."),
        ParamFieldInfo("stamina", "StaminaCost", True, int, "Stamina cost of behavior."),
        ParamFieldInfo("mp", "DurabilityCost", True, int, "Weapon/shield durability cost of behavior."),
        ParamFieldInfo(
            "category",
            "Category",
            True,
            BEHAVIOR_CATEGORY,
            "Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' "
            "for thrown goods and 'No Category' otherwise.",
        ),
        ParamFieldInfo("heroPoint", "HumanityCost", False, int, "Humanity cost of behavior. Never used."),
        ParamFieldInfo("pad1[2]", "Pad2", False, pad_field(2), "Null padding."),
    ],
}
