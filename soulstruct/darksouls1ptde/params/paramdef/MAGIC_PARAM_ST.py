from __future__ import annotations

__all__ = ["MAGIC_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import MagicReference


# noinspection PyDataclass
@dataclass(slots=True)
class MAGIC_PARAM_ST(ParamRow):
    ConfirmationMessage: EventText = ParamField(
        int, "yesNoDialogMessageId", default=0,
        tooltip="Message displayed in yes/no dialog box to confirm use of spell. Requires the Yes/No menu type.",
    )
    LimitRemoveSpecialEffect: SpecialEffectParam = ParamField(
        int, "limitCancelSpEffectId", default=-1, hide=True,
        tooltip="Unknown. Never used.",
    )
    SortIndex: int = ParamField(
        short, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    refId: short = ParamField(
        short, "refId", default=-1, dynamic_callback=MagicReference(),
        tooltip="TODO",
    )
    MPCost: int = ParamField(
        short, "mp", default=0, hide=True,
        tooltip="MP cost of spell. Unused in Dark Souls 1 (always zero).",
    )
    StaminaCost: int = ParamField(
        short, "stamina", default=25, hide=True,
        tooltip="Stamina cost of spell. Always zero.",
    )
    SpellIcon: Texture = ParamField(
        short, "iconId", default=0,
        tooltip="Spell icon texture for inventory and equipped slot.",
    )
    Behavior: BehaviorParam = ParamField(
        short, "behaviorId", default=0, hide=True,
        tooltip="Behavior triggered by spell. Never used.",
    )
    RequiredGood: GoodParam = ParamField(
        short, "mtrlItemId", default=-1, hide=True,
        tooltip="Good required for use. Never used (usability is handled in Shops parameters).",
    )
    ReplaceSpell: SpellParam = ParamField(
        short, "replaceMagicId", default=-1, hide=True,
        tooltip="Spell to replace 'when the state change matches'. Never used.",
    )
    BaseCastCount: int = ParamField(
        short, "maxQuantity", default=0,
        tooltip="Number of spell casts. Note that some spells consume multiple casts per use (e.g. Firestorm).",
    )
    HumanityCost: int = ParamField(
        byte, "heroPoint", default=0, hide=True,
        tooltip="Soft humanity consumed when casting spell. Never used.",
    )
    OverDexterity: int = ParamField(
        byte, "overDexterity", default=0, hide=True,
        tooltip="Unknown effect. Always 99.",
    )
    VisualEffectVariation: int = ParamField(
        sbyte, "sfxVariationId", default=-1,
        tooltip="Visual effect variation. (I believe this alters the animation ID used for casting.)",
    )
    AttunementSlotsUsed: int = ParamField(
        byte, "slotLength", default=1,
        tooltip="Number of attunement slots required to attune spell.",
    )
    RequiredIntelligence: int = ParamField(
        byte, "requirementIntellect", default=0,
        tooltip="Minimum intelligence required to cast spell.",
    )
    RequiredFaith: int = ParamField(
        byte, "requirementFaith", default=0,
        tooltip="Minimum faith required to cast spell.",
    )
    MinDexterityForBonus: int = ParamField(
        byte, "analogDexiterityMin", default=0, hide=True,
        tooltip="Dexterity value where casting speed starts to be affected (I think). This is always 20, but "
                "apparently speed isn't actually affected until dexterity is 35.",
    )
    MaxDexterityForBonus: int = ParamField(
        byte, "analogDexiterityMax", default=0, hide=True,
        tooltip="Dexterity value where casting speed stops being further affected (I think). Always 45, which is "
                "consistent with the observed dexterity cap.",
    )
    SpellCategory: MAGIC_CATEGORY = ParamField(
        byte, "ezStateBehaviorType", default=0,
        tooltip="Type of spell.",
    )
    ReferenceType: BEHAVIOR_REF_TYPE = ParamField(
        byte, "refCategory", default=0,
        tooltip="Determines if this spell triggers a Bullet or Special Effect. ('Default' is never used, but probably "
                "triggers an Attack, which is unlikely to be useful to you.)",
    )
    SpecialEffectCategory: SP_EFFECT_SPCATEGORY = ParamField(
        byte, "spEffectCategory", default=0,
        tooltip="Determines what type of special effects affect the stats of this spell. (Vanilla game uses 3 for "
                "sorceries and pyromancies, and 4 for miracles.)",
    )
    AnimationType: MAGIC_MOTION_TYPE = ParamField(
        byte, "refType", default=0,
        tooltip="Basic animation type when casting spell. The Visual Effect Variation field further refines it.",
    )
    MenuActivated: GOODS_OPEN_MENU = ParamField(
        byte, "opmeMenuType", default=0,
        tooltip="Menu activated (if any) when spell is cast. Only used by Homeward (Yes/No Dialog).",
    )
    HasSpecialEffectType: int = ParamField(
        byte, "hasSpEffectType", default=0, hide=True,
        tooltip="Determines 'the state change that needs to replace the spell ID'. Never used.",
    )
    ReplaceCategory: REPLACE_CATEGORY = ParamField(
        byte, "replaceCategory", default=0,
        tooltip="Determines which existing effects this spell will replace. Only used for a few spells.",
    )
    LimitCategory: SP_EFFECT_USELIMIT_CATEGORY = ParamField(
        byte, "useLimitCategory", default=0,
        tooltip="Only one special effect with this category can be active at once. Additional attempts to cast spells "
                "(or use goods) in this category will be prevented.",
    )
    UseableByNoCovenant: bool = ParamField(
        byte, "vowType0:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by characters with no covenant.",
    )
    UseableByWayOfWhite: bool = ParamField(
        byte, "vowType1:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by characters in the Way of White.",
    )
    UseableByPrincessGuard: bool = ParamField(
        byte, "vowType2:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by characters in the Princess's Guard.",
    )
    UseableByWarriorsOfSunlight: bool = ParamField(
        byte, "vowType3:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by characters in the Warriors of Sunlight.",
    )
    UseableByDarkwraith: bool = ParamField(
        byte, "vowType4:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by characters in the Darkwraith covenant.",
    )
    UseableByPathOfTheDragon: bool = ParamField(
        byte, "vowType5:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by characters in the Path of the Dragon.",
    )
    UseableByGravelordServant: bool = ParamField(
        byte, "vowType6:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by characters in the Gravelord Servants.",
    )
    UseableByForestHunter: bool = ParamField(
        byte, "vowType7:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by characters in the Forest Hunters.",
    )
    UseableInMultiplayer: bool = ParamField(
        byte, "enable_multi:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast while multiple players are together. Only disabled for Homeward "
                "in vanilla game.",
    )
    DisabledOutsideMultiplayer: bool = ParamField(
        byte, "enable_multi_only:1", bit_count=1, default=False, hide=True,
        tooltip="Determines if this spell can ONLY be cast while multiple players are together. Always False.",
    )
    IsWeaponBuff: bool = ParamField(
        byte, "isEnchant:1", bit_count=1, default=False,
        tooltip="Indicates if this spell buffs your weapon.",
    )
    IsShieldBuff: bool = ParamField(
        byte, "isShieldEnchant:1", bit_count=1, default=False,
        tooltip="Indicates if this spell buffs your shield.",
    )
    UseableByHumans: bool = ParamField(
        byte, "enable_live:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by players who have revived to human.",
    )
    UseableByHollows: bool = ParamField(
        byte, "enable_gray:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by players who have NOT revived to human.",
    )
    UseableByWhitePhantoms: bool = ParamField(
        byte, "enable_white:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by White Phantoms (summons). Only disabled for Homeward and the "
                "unused Escape Death miracle in vanilla game.",
    )
    UseableByBlackPhantoms: bool = ParamField(
        byte, "enable_black:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by Black Phantoms (invaders). Only disabled for Homeward and "
                "the unused Escape Death miracle in vanilla game.",
    )
    DisabledOffline: bool = ParamField(
        byte, "disableOffline:1", bit_count=1, default=False, hide=True,
        tooltip="If True, this spell cannot be cast without a network connection. Always False.",
    )
    CreateResonanceRing: bool = ParamField(
        byte, "castResonanceMagic:1", bit_count=1, default=False,
        tooltip="If True, using this spell will create a resonance ring to help players in other worlds.",
    )
    _BitPad0: int = ParamBitPad(byte, "pad_1:6", bit_count=6)
    UseableByDarkmoonBlade: bool = ParamField(
        byte, "vowType8:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by characters in the Blades of the Darkmoon.",
    )
    UseableByChaosServant: bool = ParamField(
        byte, "vowType9:1", bit_count=1, default=True,
        tooltip="Determines if this spell can be cast by characters in the Chaos Servant covenant.",
    )
    UseableByCovenant10: bool = ParamField(
        byte, "vowType10:1", bit_count=1, default=True, hide=True,
        tooltip="Determines if this spell can be cast by characters in unused covenant 10.",
    )
    UseableByCovenant11: bool = ParamField(
        byte, "vowType11:1", bit_count=1, default=True, hide=True,
        tooltip="Determines if this spell can be cast by characters in unused covenant 11.",
    )
    UseableByCovenant12: bool = ParamField(
        byte, "vowType12:1", bit_count=1, default=True, hide=True,
        tooltip="Determines if this spell can be cast by characters in unused covenant 12.",
    )
    UseableByCovenant13: bool = ParamField(
        byte, "vowType13:1", bit_count=1, default=True, hide=True,
        tooltip="Determines if this spell can be cast by characters in unused covenant 13.",
    )
    UseableByCovenant14: bool = ParamField(
        byte, "vowType14:1", bit_count=1, default=True, hide=True,
        tooltip="Determines if this spell can be cast by characters in unused covenant 14.",
    )
    UseableByCovenant15: bool = ParamField(
        byte, "vowType15:1", bit_count=1, default=True, hide=True,
        tooltip="Determines if this spell can be cast by characters in unused covenant 15.",
    )
    _Pad0: bytes = ParamPad(2, "pad[2]")
