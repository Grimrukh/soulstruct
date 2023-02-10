from __future__ import annotations

__all__ = ["MAGIC_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, DynamicParamFieldInfo, pad_field, bit_pad_field
from soulstruct.darksouls1ptde.game_types import *
from ..enums import *


class DynamicSpellRef(DynamicParamFieldInfo):

    POSSIBLE_TYPES = {BulletParam, SpecialEffectParam}

    def __call__(self, entry) -> ParamFieldInfo:
        if entry[self.type_field_name] == BEHAVIOR_REF_TYPE.Default:
            return ParamFieldInfo(
                self.name,
                "NoReference",
                True,
                int,
                "This value should be -1 when 'Default' reference type is selected.",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.Bullet:
            return ParamFieldInfo(
                self.name,
                "Bullet",
                True,
                BulletParam,
                "Bullet triggered by casting spell (which may simply be targeted at self).",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.SpecialEffect:
            return ParamFieldInfo(
                self.name,
                "SpecialEffect",
                True,
                SpecialEffectParam,
                "Special effect triggered (on self) by casting spell.",
            )
        else:
            return ParamFieldInfo(
                self.name,
                "UnknownReferenceID",
                True,
                int,
                "Could not determine spell reference type (usually Bullet or SpecialEffect).",
            )


MAGIC_PARAM_ST = {
    "param_type": "MAGIC_PARAM_ST",
    "file_name": "Magic",
    "nickname": "Spells",
    "fields": [
        ParamFieldInfo(
            "yesNoDialogMessageId",
            "ConfirmationMessage",
            True,
            EventText,
            "Message displayed in yes/no dialog box to confirm use of spell. Requires the Yes/No menu type.",
        ),
        ParamFieldInfo(
            "limitCancelSpEffectId",
            "LimitRemoveSpecialEffect",
            False,
            SpecialEffectParam,
            "Unknown. Never used.",
        ),
        ParamFieldInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        DynamicSpellRef("refId", "refCategory"),
        ParamFieldInfo("mp", "MPCost", False, int, "MP cost of spell. Unused in Dark Souls 1 (always zero)."),
        ParamFieldInfo("stamina", "StaminaCost", False, int, "Stamina cost of spell. Always zero."),
        ParamFieldInfo("iconId", "SpellIcon", True, Texture, "Spell icon texture for inventory and equipped slot."),
        ParamFieldInfo("behaviorId", "Behavior", False, BehaviorParam, "Behavior triggered by spell. Never used."),
        ParamFieldInfo(
            "mtrlItemId",
            "RequiredGood",
            False,
            GoodParam,
            "Good required for use. Never used (usability is handled in Shops parameters).",
        ),
        ParamFieldInfo(
            "replaceMagicId",
            "ReplaceSpell",
            False,
            SpellParam,
            "Spell to replace 'when the state change matches'. Never used.",
        ),
        ParamFieldInfo(
            "maxQuantity",
            "BaseCastCount",
            True,
            int,
            "Number of spell casts. Note that some spells consume multiple casts per use (e.g. Firestorm).",
        ),
        ParamFieldInfo(
            "heroPoint", "HumanityCost", False, int, "Soft humanity consumed when casting spell. Never used."
        ),
        ParamFieldInfo("overDexterity", "OverDexterity", False, int, "Unknown effect. Always 99."),
        ParamFieldInfo(
            "sfxVariationId",
            "VisualEffectVariation",
            True,
            int,
            "Visual effect variation. (I believe this alters the animation ID used for casting.)",
        ),
        ParamFieldInfo(
            "slotLength", "AttunementSlotsUsed", True, int, "Number of attunement slots required to attune spell."
        ),
        ParamFieldInfo(
            "requirementIntellect",
            "RequiredIntelligence",
            True,
            int,
            "Minimum intelligence required to cast spell.",
        ),
        ParamFieldInfo("requirementFaith", "RequiredFaith", True, int, "Minimum faith required to cast spell."),
        ParamFieldInfo(
            "analogDexiterityMin",
            "MinDexterityForBonus",
            False,
            int,
            "Dexterity value where casting speed starts to be affected (I think). This is always 20, "
            "but apparently speed isn't actually affected until dexterity is 35.",
        ),
        ParamFieldInfo(
            "analogDexiterityMax",
            "MaxDexterityForBonus",
            False,
            int,
            "Dexterity value where casting speed stops being further affected (I think). Always 45, which is "
            "consistent with the observed dexterity cap.",
        ),
        ParamFieldInfo("ezStateBehaviorType", "SpellCategory", True, MAGIC_CATEGORY, "Type of spell."),
        ParamFieldInfo(
            "refCategory",
            "ReferenceType",
            True,
            BEHAVIOR_REF_TYPE,
            "Determines if this spell triggers a Bullet or Special Effect. ('Default' is never used, but probably "
            "triggers an Attack, which is unlikely to be useful to you.)",
        ),
        ParamFieldInfo(
            "spEffectCategory",
            "SpecialEffectCategory",
            True,
            SP_EFFECT_SPCATEGORY,
            "Determines what type of special effects affect the stats of this spell. (Vanilla game uses 3 for "
            "sorceries and pyromancies, and 4 for miracles.)",
        ),
        ParamFieldInfo(
            "refType",
            "AnimationType",
            True,
            MAGIC_MOTION_TYPE,
            "Basic animation type when casting spell. The Visual Effect Variation field further refines it.",
        ),
        ParamFieldInfo(
            "opmeMenuType",
            "MenuActivated",
            True,
            GOODS_OPEN_MENU,
            "Menu activated (if any) when spell is cast. Only used by Homeward (Yes/No Dialog).",
        ),
        ParamFieldInfo(
            "hasSpEffectType",
            "HasSpecialEffectType",
            False,
            int,
            "Determines 'the state change that needs to replace the spell ID'. Never used.",
        ),
        ParamFieldInfo(
            "replaceCategory",
            "ReplaceCategory",
            True,
            REPLACE_CATEGORY,
            "Determines which existing effects this spell will replace. Only used for a few spells.",
        ),
        ParamFieldInfo(
            "useLimitCategory",
            "LimitCategory",
            True,
            SP_EFFECT_USELIMIT_CATEGORY,
            "Only one special effect with this category can be active at once. Additional attempts to cast spells "
            "(or use goods) in this category will be prevented.",
        ),
        ParamFieldInfo(
            "vowType0:1",
            "UseableByNoCovenant",
            True,
            bool,
            "Determines if this spell can be cast by characters with no covenant.",
        ),
        ParamFieldInfo(
            "vowType1:1",
            "UseableByWayOfWhite",
            True,
            bool,
            "Determines if this spell can be cast by characters in the Way of White.",
        ),
        ParamFieldInfo(
            "vowType2:1",
            "UseableByPrincessGuard",
            True,
            bool,
            "Determines if this spell can be cast by characters in the Princess's Guard.",
        ),
        ParamFieldInfo(
            "vowType3:1",
            "UseableByWarriorsOfSunlight",
            True,
            bool,
            "Determines if this spell can be cast by characters in the Warriors of Sunlight.",
        ),
        ParamFieldInfo(
            "vowType4:1",
            "UseableByDarkwraith",
            True,
            bool,
            "Determines if this spell can be cast by characters in the Darkwraith covenant.",
        ),
        ParamFieldInfo(
            "vowType5:1",
            "UseableByPathOfTheDragon",
            True,
            bool,
            "Determines if this spell can be cast by characters in the Path of the Dragon.",
        ),
        ParamFieldInfo(
            "vowType6:1",
            "UseableByGravelordServant",
            True,
            bool,
            "Determines if this spell can be cast by characters in the Gravelord Servants.",
        ),
        ParamFieldInfo(
            "vowType7:1",
            "UseableByForestHunter",
            True,
            bool,
            "Determines if this spell can be cast by characters in the Forest Hunters.",
        ),
        ParamFieldInfo(
            "vowType8:1",
            "UseableByDarkmoonBlade",
            True,
            bool,
            "Determines if this spell can be cast by characters in the Blades of the Darkmoon.",
        ),
        ParamFieldInfo(
            "vowType9:1",
            "UseableByChaosServant",
            True,
            bool,
            "Determines if this spell can be cast by characters in the Chaos Servant covenant.",
        ),
        ParamFieldInfo(
            "vowType10:1",
            "UseableByCovenant10",
            False,
            bool,
            "Determines if this spell can be cast by characters in unused covenant 10.",
        ),
        ParamFieldInfo(
            "vowType11:1",
            "UseableByCovenant11",
            False,
            bool,
            "Determines if this spell can be cast by characters in unused covenant 11.",
        ),
        ParamFieldInfo(
            "vowType12:1",
            "UseableByCovenant12",
            False,
            bool,
            "Determines if this spell can be cast by characters in unused covenant 12.",
        ),
        ParamFieldInfo(
            "vowType13:1",
            "UseableByCovenant13",
            False,
            bool,
            "Determines if this spell can be cast by characters in unused covenant 13.",
        ),
        ParamFieldInfo(
            "vowType14:1",
            "UseableByCovenant14",
            False,
            bool,
            "Determines if this spell can be cast by characters in unused covenant 14.",
        ),
        ParamFieldInfo(
            "vowType15:1",
            "UseableByCovenant15",
            False,
            bool,
            "Determines if this spell can be cast by characters in unused covenant 15.",
        ),
        ParamFieldInfo(
            "enable_multi:1",
            "UseableInMultiplayer",
            True,
            bool,
            "Determines if this spell can be cast while multiple players are together. Only disabled for Homeward "
            "in vanilla game.",
        ),
        ParamFieldInfo(
            "enable_multi_only:1",
            "DisabledOutsideMultiplayer",
            False,
            bool,
            "Determines if this spell can ONLY be cast while multiple players are together. Always False.",
        ),
        ParamFieldInfo("isEnchant:1", "IsWeaponBuff", True, bool, "Indicates if this spell buffs your weapon."),
        ParamFieldInfo("isShieldEnchant:1", "IsShieldBuff", True, bool, "Indicates if this spell buffs your shield."),
        ParamFieldInfo(
            "enable_live:1",
            "UseableByHumans",
            True,
            bool,
            "Determines if this spell can be cast by players who have revived to human.",
        ),
        ParamFieldInfo(
            "enable_gray:1",
            "UseableByHollows",
            True,
            bool,
            "Determines if this spell can be cast by players who have NOT revived to human.",
        ),
        ParamFieldInfo(
            "enable_white:1",
            "UseableByWhitePhantoms",
            True,
            bool,
            "Determines if this spell can be cast by White Phantoms (summons). Only disabled for Homeward and the "
            "unused Escape Death miracle in vanilla game.",
        ),
        ParamFieldInfo(
            "enable_black:1",
            "UseableByBlackPhantoms",
            True,
            bool,
            "Determines if this spell can be cast by Black Phantoms (invaders). Only disabled for Homeward and "
            "the unused Escape Death miracle in vanilla game.",
        ),
        ParamFieldInfo(
            "disableOffline:1",
            "DisabledOffline",
            False,
            bool,
            "If True, this spell cannot be cast without a network connection. Always False.",
        ),
        ParamFieldInfo(
            "castResonanceMagic:1",
            "CreateResonanceRing",
            True,
            bool,
            "If True, using this spell will create a resonance ring to help players in other worlds.",
        ),
        ParamFieldInfo("pad_1:6", "Pad1", False, bit_pad_field(6), "Null padding."),
        ParamFieldInfo("pad[2]", "Pad2", False, pad_field(2), "Null padding."),
    ],
}
