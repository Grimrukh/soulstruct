from __future__ import annotations

__all__ = ["MAGIC_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MAGIC_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    ConfirmationMessage: int = ParamField(
        int, "yesNoDialogMessageId", default=0,
        tooltip="Message displayed in yes/no dialog box to confirm use of spell. Requires the Yes/No menu type.",
    )
    LimitRemoveSpecialEffect: int = ParamField(
        int, "limitCancelSpEffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="Unknown. Never used.",
    )
    SortIndex: int = ParamField(
        short, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    RequirementLuck: int = ParamField(
        byte, "requirementLuck", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiNotifyType: int = ParamField(
        byte, "aiNotifyType", MAGIC_AI_NOTIFY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    MPCost: int = ParamField(
        short, "mp", default=0,
        tooltip="MP cost of spell. Unused in Dark Souls 1 (always zero).",
    )
    StaminaCost: int = ParamField(
        short, "stamina", default=0,
        tooltip="Stamina cost of spell. Always zero.",
    )
    SpellIcon: int = ParamField(
        short, "iconId", game_type=Icon, default=0,
        tooltip="Spell icon texture for inventory and equipped slot.",
    )
    Behavior: int = ParamField(
        short, "behaviorId", game_type=BehaviorParam, default=0,
        tooltip="Behavior triggered by spell. Never used.",
    )
    RequiredGood: int = ParamField(
        short, "mtrlItemId", game_type=GoodParam, default=-1,
        tooltip="Good required for use. Never used (usability is handled in Shops parameters).",
    )
    ReplaceSpell: int = ParamField(
        short, "replaceMagicId", game_type=SpellParam, default=-1,
        tooltip="Spell to replace 'when the state change matches'. Never used.",
    )
    BaseCastCount: int = ParamField(
        short, "maxQuantity", default=0,
        tooltip="Number of spell casts. Note that some spells consume multiple casts per use (e.g. Firestorm).",
    )
    RefCategory1: int = ParamField(
        byte, "refCategory1", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverDexterity: int = ParamField(
        byte, "overDexterity", default=0,
        tooltip="Unknown effect. Always 99.",
    )
    RefCategory2: int = ParamField(
        byte, "refCategory2", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttunementSlotsUsed: int = ParamField(
        byte, "slotLength", default=0,
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
    AnalogDexterityMin: int = ParamField(
        byte, "analogDexterityMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnalogDexterityMax: int = ParamField(
        byte, "analogDexterityMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpellCategory: int = ParamField(
        byte, "ezStateBehaviorType", MAGIC_CATEGORY, default=0,
        tooltip="Type of spell.",
    )
    RefCategory3: int = ParamField(
        byte, "refCategory3", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectCategory: int = ParamField(
        byte, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="Determines what type of special effects affect the stats of this spell. (Vanilla game uses 3 for "
                "sorceries and pyromancies, and 4 for miracles.)",
    )
    AnimationType: int = ParamField(
        byte, "refType", MAGIC_MOTION_TYPE, default=0,
        tooltip="Basic animation type when casting spell. The Visual Effect Variation field further refines it.",
    )
    MenuActivated: int = ParamField(
        byte, "opmeMenuType", GOODS_OPEN_MENU, default=0,
        tooltip="Menu activated (if any) when spell is cast. Only used by Homeward (Yes/No Dialog).",
    )
    RefCategory4: int = ParamField(
        byte, "refCategory4", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    HasSpecialEffectType: int = ParamField(
        ushort, "hasSpEffectType", SP_EFFECT_TYPE, default=0,
        tooltip="Determines 'the state change that needs to replace the spell ID'. Never used.",
    )
    ReplaceCategory: int = ParamField(
        byte, "replaceCategory", REPLACE_CATEGORY, default=0,
        tooltip="Determines which existing effects this spell will replace. Only used for a few spells.",
    )
    LimitCategory: int = ParamField(
        byte, "useLimitCategory", SP_EFFECT_USELIMIT_CATEGORY, default=0,
        tooltip="Only one special effect with this category can be active at once. Additional attempts to cast spells "
                "(or use goods) in this category will be prevented.",
    )
    UseableByNoCovenant: bool = ParamField(
        byte, "vowType0:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters with no covenant.",
    )
    UseableByCovenant1: bool = ParamField(
        byte, "vowType1:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 1.",
    )
    UseableByCovenant2: bool = ParamField(
        byte, "vowType2:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 2.",
    )
    UseableByCovenant3: bool = ParamField(
        byte, "vowType3:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 3.",
    )
    UseableByCovenant4: bool = ParamField(
        byte, "vowType4:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 4.",
    )
    UseableByCovenant5: bool = ParamField(
        byte, "vowType5:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 5.",
    )
    UseableByCovenant6: bool = ParamField(
        byte, "vowType6:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 6.",
    )
    UseableByCovenant7: bool = ParamField(
        byte, "vowType7:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 7.",
    )
    UseableInMultiplayer: bool = ParamField(
        byte, "enable_multi:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast while multiple players are together. Only disabled for Homeward "
                "in vanilla game.",
    )
    DisabledOutsideMultiplayer: bool = ParamField(
        byte, "enable_multi_only:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can ONLY be cast while multiple players are together. Always False.",
    )
    IsWeaponBuff: bool = ParamField(
        byte, "isEnchant:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Indicates if this spell buffs your weapon.",
    )
    IsShieldBuff: bool = ParamField(
        byte, "isShieldEnchant:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Indicates if this spell buffs your shield.",
    )
    UseableByHumans: bool = ParamField(
        byte, "enable_live:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by players who have revived to human.",
    )
    UseableByHollows: bool = ParamField(
        byte, "enable_gray:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by players who have NOT revived to human.",
    )
    UseableByWhitePhantoms: bool = ParamField(
        byte, "enable_white:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by White Phantoms (summons). Only disabled for Homeward and the "
                "unused Escape Death miracle in vanilla game.",
    )
    UseableByBlackPhantoms: bool = ParamField(
        byte, "enable_black:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by Black Phantoms (invaders). Only disabled for Homeward and "
                "the unused Escape Death miracle in vanilla game.",
    )
    DisabledOffline: bool = ParamField(
        byte, "disableOffline:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="If True, this spell cannot be cast without a network connection. Always False.",
    )
    CreateResonanceRing: bool = ParamField(
        byte, "castResonanceMagic:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="If True, using this spell will create a resonance ring to help players in other worlds.",
    )
    IsValidToughProtSADmg: bool = ParamField(
        byte, "isValidTough_ProtSADmg:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWarpMagic: bool = ParamField(
        byte, "isWarpMagic:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableRiding: bool = ParamField(
        byte, "enableRiding:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableRiding: bool = ParamField(
        byte, "disableRiding:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseNoAttackRegion: bool = ParamField(
        byte, "isUseNoAttackRegion:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad_1:1", bit_count=1)
    UseableByCovenant8: bool = ParamField(
        byte, "vowType8:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 8.",
    )
    UseableByCovenant9: bool = ParamField(
        byte, "vowType9:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 9.",
    )
    UseableByCovenant10: bool = ParamField(
        byte, "vowType10:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 10.",
    )
    UseableByCovenant11: bool = ParamField(
        byte, "vowType11:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 11.",
    )
    UseableByCovenant12: bool = ParamField(
        byte, "vowType12:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 12.",
    )
    UseableByCovenant13: bool = ParamField(
        byte, "vowType13:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 13.",
    )
    UseableByCovenant14: bool = ParamField(
        byte, "vowType14:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 14.",
    )
    UseableByCovenant15: bool = ParamField(
        byte, "vowType15:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in unused covenant 15.",
    )
    CastSfxId: int = ParamField(
        int, "castSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FireSfxId: int = ParamField(
        int, "fireSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EffectSfxId: int = ParamField(
        int, "effectSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessCorrectRate: float = ParamField(
        float, "toughnessCorrectRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatusType: int = ParamField(
        byte, "ReplacementStatusType", MAGIC_STATUS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus1: int = ParamField(
        sbyte, "ReplacementStatus1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus2: int = ParamField(
        sbyte, "ReplacementStatus2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus3: int = ParamField(
        sbyte, "ReplacementStatus3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus4: int = ParamField(
        sbyte, "ReplacementStatus4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory5: int = ParamField(
        byte, "refCategory5", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeSA: int = ParamField(
        short, "consumeSA", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic1: int = ParamField(
        int, "ReplacementMagic1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic2: int = ParamField(
        int, "ReplacementMagic2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic3: int = ParamField(
        int, "ReplacementMagic3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic4: int = ParamField(
        int, "ReplacementMagic4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Mpcharge: int = ParamField(
        short, "mp_charge", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Staminacharge: int = ParamField(
        short, "stamina_charge", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateLimitGroupId: int = ParamField(
        byte, "createLimitGroupId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory6: int = ParamField(
        byte, "refCategory6", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory1: int = ParamField(
        byte, "subCategory1", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory2: int = ParamField(
        byte, "subCategory2", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory7: int = ParamField(
        byte, "refCategory7", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory8: int = ParamField(
        byte, "refCategory8", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory9: int = ParamField(
        byte, "refCategory9", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory10: int = ParamField(
        byte, "refCategory10", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefId1: int = ParamField(
        int, "refId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId2: int = ParamField(
        int, "refId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId3: int = ParamField(
        int, "refId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AiUseJudgeId: int = ParamField(
        int, "aiUseJudgeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId4: int = ParamField(
        int, "refId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId5: int = ParamField(
        int, "refId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId6: int = ParamField(
        int, "refId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId7: int = ParamField(
        int, "refId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId8: int = ParamField(
        int, "refId8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId9: int = ParamField(
        int, "refId9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId10: int = ParamField(
        int, "refId10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType1: int = ParamField(
        byte, "consumeType1", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType2: int = ParamField(
        byte, "consumeType2", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType3: int = ParamField(
        byte, "consumeType3", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType4: int = ParamField(
        byte, "consumeType4", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType5: int = ParamField(
        byte, "consumeType5", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType6: int = ParamField(
        byte, "consumeType6", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType7: int = ParamField(
        byte, "consumeType7", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType8: int = ParamField(
        byte, "consumeType8", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType9: int = ParamField(
        byte, "consumeType9", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType10: int = ParamField(
        byte, "consumeType10", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeLoopMPforMenu: int = ParamField(
        short, "consumeLoopMP_forMenu", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad[8]")
