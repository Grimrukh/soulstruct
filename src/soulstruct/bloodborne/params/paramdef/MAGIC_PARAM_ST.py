from __future__ import annotations

__all__ = ["MAGIC_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import MagicReference


class MAGIC_PARAM_ST(ParamRow):
    ConfirmationMessage: int = ParamField(
        int32, "yesNoDialogMessageId", default=0,
        tooltip="Message displayed in yes/no dialog box to confirm use of spell. Requires the Yes/No menu type.",
    )
    LimitRemoveSpecialEffect: int = ParamField(
        int32, "limitCancelSpEffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="Unknown. Never used.",
    )
    SortIndex: int = ParamField(
        int16, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    ReferenceID: int = ParamField(
        int16, "refId", default=-1, dynamic_callback=MagicReference(),
        tooltip="TODO",
    )
    MPCost: int = ParamField(
        int16, "mp", default=0,
        tooltip="MP cost of spell. Unused in Dark Souls 1 (always zero).",
    )
    StaminaCost: int = ParamField(
        int16, "stamina", default=0,
        tooltip="Stamina cost of spell. Always zero.",
    )
    SpellIcon: int = ParamField(
        int16, "iconId", game_type=Icon, default=0,
        tooltip="Spell icon texture for inventory and equipped slot.",
    )
    Behavior: int = ParamField(
        int16, "behaviorId", game_type=BehaviorParam, default=0,
        tooltip="Behavior triggered by spell. Never used.",
    )
    RequiredGood: int = ParamField(
        int16, "mtrlItemId", game_type=GoodParam, default=-1,
        tooltip="Good required for use. Never used (usability is handled in Shops parameters).",
    )
    ReplaceSpell: int = ParamField(
        int16, "replaceMagicId", game_type=SpellParam, default=-1,
        tooltip="Spell to replace 'when the state change matches'. Never used.",
    )
    BaseCastCount: int = ParamField(
        int16, "maxQuantity", default=0,
        tooltip="Number of spell casts. Note that some spells consume multiple casts per use (e.g. Firestorm).",
    )
    HumanityCost: int = ParamField(
        uint8, "heroPoint", default=0,
        tooltip="Soft humanity consumed when casting spell. Never used.",
    )
    OverDexterity: int = ParamField(
        uint8, "overDexterity", default=0,
        tooltip="Unknown effect. Always 99.",
    )
    VisualEffectVariation: int = ParamField(
        int8, "sfxVariationId", default=-1,
        tooltip="Visual effect variation. (I believe this alters the animation ID used for casting.)",
    )
    AttunementSlotsUsed: int = ParamField(
        uint8, "slotLength", default=0,
        tooltip="Number of attunement slots required to attune spell.",
    )
    RequiredIntelligence: int = ParamField(
        uint8, "requirementIntellect", default=0,
        tooltip="Minimum intelligence required to cast spell.",
    )
    RequiredFaith: int = ParamField(
        uint8, "requirementFaith", default=0,
        tooltip="Minimum faith required to cast spell.",
    )
    MinDexterityForBonus: int = ParamField(
        uint8, "analogDexiterityMin", default=0,
        tooltip="Dexterity value where casting speed starts to be affected (I think). This is always 20, but "
                "apparently speed isn't actually affected until dexterity is 35.",
    )
    MaxDexterityForBonus: int = ParamField(
        uint8, "analogDexiterityMax", default=0,
        tooltip="Dexterity value where casting speed stops being further affected (I think). Always 45, which is "
                "consistent with the observed dexterity cap.",
    )
    SpellCategory: int = ParamField(
        uint8, "ezStateBehaviorType", MAGIC_CATEGORY, default=0,
        tooltip="Type of spell.",
    )
    ReferenceType: int = ParamField(
        uint8, "refCategory", BEHAVIOR_REF_TYPE, default=0,
        tooltip="Determines if this spell triggers a Bullet or Special Effect. ('Default' is never used, but probably "
                "triggers an Attack, which is unlikely to be useful to you.)",
    )
    SpecialEffectCategory: int = ParamField(
        uint8, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="Determines what type of special effects affect the stats of this spell. (Vanilla game uses 3 for "
                "sorceries and pyromancies, and 4 for miracles.)",
    )
    AnimationType: int = ParamField(
        uint8, "refType", MAGIC_MOTION_TYPE, default=0,
        tooltip="Basic animation type when casting spell. The Visual Effect Variation field further refines it.",
    )
    _Pad0: bytes = ParamPad(1, "pad")
    MenuActivated: int = ParamField(
        uint8, "opmeMenuType", GOODS_OPEN_MENU, default=0,
        tooltip="Menu activated (if any) when spell is cast. Only used by Homeward (Yes/No Dialog).",
    )
    HasSpecialEffectType: int = ParamField(
        uint16, "hasSpEffectType", SP_EFFECT_TYPE, default=0,
        tooltip="Determines 'the state change that needs to replace the spell ID'. Never used.",
    )
    ReplaceCategory: int = ParamField(
        uint8, "replaceCategory", REPLACE_CATEGORY, default=0,
        tooltip="Determines which existing effects this spell will replace. Only used for a few spells.",
    )
    LimitCategory: int = ParamField(
        uint8, "useLimitCategory", SP_EFFECT_USELIMIT_CATEGORY, default=0,
        tooltip="Only one special effect with this category can be active at once. Additional attempts to cast spells "
                "(or use goods) in this category will be prevented.",
    )
    UseableByNoCovenant: bool = ParamField(
        uint8, "vowType0:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters with no covenant.",
    )
    UseableByWayOfWhite: bool = ParamField(
        uint8, "vowType1:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in the Way of White.",
    )
    UseableByPrincessGuard: bool = ParamField(
        uint8, "vowType2:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in the Princess's Guard.",
    )
    UseableByWarriorsOfSunlight: bool = ParamField(
        uint8, "vowType3:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in the Warriors of Sunlight.",
    )
    UseableByDarkwraith: bool = ParamField(
        uint8, "vowType4:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in the Darkwraith covenant.",
    )
    UseableByPathOfTheDragon: bool = ParamField(
        uint8, "vowType5:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in the Path of the Dragon.",
    )
    UseableByGravelordServant: bool = ParamField(
        uint8, "vowType6:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in the Gravelord Servants.",
    )
    UseableByForestHunter: bool = ParamField(
        uint8, "vowType7:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in the Forest Hunters.",
    )
    UseableInMultiplayer: bool = ParamField(
        uint8, "enable_multi:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast while multiple players are together. Only disabled for Homeward "
                "in vanilla game.",
    )
    DisabledOutsideMultiplayer: bool = ParamField(
        uint8, "enable_multi_only:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can ONLY be cast while multiple players are together. Always False.",
    )
    IsWeaponBuff: bool = ParamField(
        uint8, "isEnchant:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Indicates if this spell buffs your weapon.",
    )
    IsShieldBuff: bool = ParamField(
        uint8, "isShieldEnchant:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Indicates if this spell buffs your shield.",
    )
    UseableByHumans: bool = ParamField(
        uint8, "enable_live:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by players who have revived to human.",
    )
    UseableByHollows: bool = ParamField(
        uint8, "enable_gray:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by players who have NOT revived to human.",
    )
    UseableByWhitePhantoms: bool = ParamField(
        uint8, "enable_white:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by White Phantoms (summons). Only disabled for Homeward and the "
                "unused Escape Death miracle in vanilla game.",
    )
    UseableByBlackPhantoms: bool = ParamField(
        uint8, "enable_black:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by Black Phantoms (invaders). Only disabled for Homeward and "
                "the unused Escape Death miracle in vanilla game.",
    )
    DisabledOffline: bool = ParamField(
        uint8, "disableOffline:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="If True, this spell cannot be cast without a network connection. Always False.",
    )
    CreateResonanceRing: bool = ParamField(
        uint8, "castResonanceMagic:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="If True, using this spell will create a resonance ring to help players in other worlds.",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad_1:6", bit_count=6)
    UseableByDarkmoonBlade: bool = ParamField(
        uint8, "vowType8:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in the Blades of the Darkmoon.",
    )
    UseableByChaosServant: bool = ParamField(
        uint8, "vowType9:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in the Chaos Servant covenant.",
    )
    UseableByCovenant10: bool = ParamField(
        uint8, "vowType10:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 10.",
    )
    UseableByCovenant11: bool = ParamField(
        uint8, "vowType11:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 11.",
    )
    UseableByCovenant12: bool = ParamField(
        uint8, "vowType12:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 12.",
    )
    UseableByCovenant13: bool = ParamField(
        uint8, "vowType13:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 13.",
    )
    UseableByCovenant14: bool = ParamField(
        uint8, "vowType14:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 14.",
    )
    UseableByCovenant15: bool = ParamField(
        uint8, "vowType15:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 15.",
    )
