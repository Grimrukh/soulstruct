__all__ = ["BEHAVIOR_PARAM_ST"]

from soulstruct.game_types.param_types import AttackParam, BulletParam, SpecialEffectParam
from soulstruct.params.core import FieldDisplayInfo, DynamicFieldDisplayInfo, pad_field
from soulstruct.params.darksouls1r.enums import BEHAVIOR_CATEGORY, BEHAVIOR_REF_TYPE


class DynamicBehaviorRef(DynamicFieldDisplayInfo):

    POSSIBLE_TYPES = {AttackParam, BulletParam, SpecialEffectParam}

    def __call__(self, entry) -> FieldDisplayInfo:
        if entry[self.type_field_name] == BEHAVIOR_REF_TYPE.Default:
            return FieldDisplayInfo(
                self.name,
                "Attack",
                True,
                AttackParam,
                "Attack ID triggered by behavior.",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.Bullet:
            return FieldDisplayInfo(
                self.name,
                "Bullet",
                True,
                BulletParam,
                "Bullet ID triggered by behavior.",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.SpecialEffect:
            return FieldDisplayInfo(
                self.name,
                "SpecialEffect",
                True,
                SpecialEffectParam,
                "Special Effect ID triggered by behavior. (Never used; may not work.)",
            )
        else:
            return FieldDisplayInfo(
                self.name,
                "UnknownRef",
                True,
                int,
                "Could not determine reference ID type (usually Attack or Bullet).",
            )


BEHAVIOR_PARAM_ST = {
    "internal_name": "BEHAVIOR_PARAM_ST",
    "file_name": "BehaviorParam",  # also BehaviorParam_PC
    "nickname": None,
    "fields": [
        FieldDisplayInfo("variationId", "VariationID", True, int, ""),  # TODO: connect to model/TAE somehow.
        FieldDisplayInfo(
            "behaviorJudgeId",
            "BehaviorJudgeID",
            True,
            int,
            "This is the ID specified by TAE events that trigger behaviors.",
        ),
        FieldDisplayInfo(
            "ezStateBehaviorType_old", "EzstateBehaviorType", False, int, "Unused remnant from Demon's Souls."
        ),
        FieldDisplayInfo(
            "refType", "ReferenceType", True, BEHAVIOR_REF_TYPE, "Is the reference ID below an Attack or Bullet ID?"
        ),
        FieldDisplayInfo("pad0[2]", "Pad1", False, pad_field(2), "Null padding."),
        DynamicBehaviorRef("refId", "refType"),
        FieldDisplayInfo("sfxVariationId", "FXVariationID", True, int, "Visual effect ID."),
        FieldDisplayInfo("stamina", "StaminaCost", True, int, "Stamina cost of behavior."),
        FieldDisplayInfo("mp", "DurabilityCost", True, int, "Weapon/shield durability cost of behavior."),
        FieldDisplayInfo(
            "category",
            "Category",
            True,
            BEHAVIOR_CATEGORY,
            "Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' "
            "for thrown goods and 'No Category' otherwise.",
        ),
        FieldDisplayInfo("heroPoint", "HumanityCost", False, int, "Humanity cost of behavior. Never used."),
        FieldDisplayInfo("pad1[2]", "Pad2", False, pad_field(2), "Null padding."),
    ],
}
