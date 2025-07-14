from __future__ import annotations

__all__ = ["MAGIC_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MAGIC_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
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
    RequirementLuck: int = ParamField(
        uint8, "requirementLuck", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiNotifyType: int = ParamField(
        uint8, "aiNotifyType", MAGIC_AI_NOTIFY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
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
    RefCategory1: int = ParamField(
        uint8, "refCategory1", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverDexterity: int = ParamField(
        uint8, "overDexterity", default=0,
        tooltip="Unknown effect. Always 99.",
    )
    RefCategory2: int = ParamField(
        uint8, "refCategory2", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
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
    AnalogDexterityMin: int = ParamField(
        uint8, "analogDexterityMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnalogDexterityMax: int = ParamField(
        uint8, "analogDexterityMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpellCategory: int = ParamField(
        uint8, "ezStateBehaviorType", MAGIC_CATEGORY, default=0,
        tooltip="Type of spell.",
    )
    RefCategory3: int = ParamField(
        uint8, "refCategory3", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
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
    MenuActivated: int = ParamField(
        uint8, "opmeMenuType", GOODS_OPEN_MENU, default=0,
        tooltip="Menu activated (if any) when spell is cast. Only used by Homeward (Yes/No Dialog).",
    )
    RefCategory4: int = ParamField(
        uint8, "refCategory4", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
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
    UseableByCovenant1: bool = ParamField(
        uint8, "vowType1:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 1.",
    )
    UseableByCovenant2: bool = ParamField(
        uint8, "vowType2:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 2.",
    )
    UseableByCovenant3: bool = ParamField(
        uint8, "vowType3:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 3.",
    )
    UseableByCovenant4: bool = ParamField(
        uint8, "vowType4:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 4.",
    )
    UseableByCovenant5: bool = ParamField(
        uint8, "vowType5:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 5.",
    )
    UseableByCovenant6: bool = ParamField(
        uint8, "vowType6:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 6.",
    )
    UseableByCovenant7: bool = ParamField(
        uint8, "vowType7:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 7.",
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
    IsValidToughProtSADmg: bool = ParamField(
        uint8, "isValidTough_ProtSADmg:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWarpMagic: bool = ParamField(
        uint8, "isWarpMagic:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableRiding: bool = ParamField(
        uint8, "enableRiding:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableRiding: bool = ParamField(
        uint8, "disableRiding:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseNoAttackRegion: bool = ParamField(
        uint8, "isUseNoAttackRegion:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "pad_1:1", bit_count=1)
    UseableByCovenant8: bool = ParamField(
        uint8, "vowType8:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 8.",
    )
    UseableByCovenant9: bool = ParamField(
        uint8, "vowType9:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="Determines if this spell can be cast by characters in Covenant 9.",
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
    CastSfxId: int = ParamField(
        int32, "castSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FireSfxId: int = ParamField(
        int32, "fireSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EffectSfxId: int = ParamField(
        int32, "effectSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ToughnessCorrectRate: float = ParamField(
        float32, "toughnessCorrectRate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatusType: int = ParamField(
        uint8, "ReplacementStatusType", MAGIC_STATUS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus1: int = ParamField(
        int8, "ReplacementStatus1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus2: int = ParamField(
        int8, "ReplacementStatus2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus3: int = ParamField(
        int8, "ReplacementStatus3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementStatus4: int = ParamField(
        int8, "ReplacementStatus4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory5: int = ParamField(
        uint8, "refCategory5", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeSA: int = ParamField(
        int16, "consumeSA", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic1: int = ParamField(
        int32, "ReplacementMagic1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic2: int = ParamField(
        int32, "ReplacementMagic2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic3: int = ParamField(
        int32, "ReplacementMagic3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplacementMagic4: int = ParamField(
        int32, "ReplacementMagic4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Mpcharge: int = ParamField(
        int16, "mp_charge", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Staminacharge: int = ParamField(
        int16, "stamina_charge", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateLimitGroupId: int = ParamField(
        uint8, "createLimitGroupId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory6: int = ParamField(
        uint8, "refCategory6", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory1: int = ParamField(
        uint8, "subCategory1", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory2: int = ParamField(
        uint8, "subCategory2", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory7: int = ParamField(
        uint8, "refCategory7", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory8: int = ParamField(
        uint8, "refCategory8", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory9: int = ParamField(
        uint8, "refCategory9", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory10: int = ParamField(
        uint8, "refCategory10", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefId1: int = ParamField(
        int32, "refId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId2: int = ParamField(
        int32, "refId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId3: int = ParamField(
        int32, "refId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AiUseJudgeId: int = ParamField(
        int32, "aiUseJudgeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId4: int = ParamField(
        int32, "refId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId5: int = ParamField(
        int32, "refId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId6: int = ParamField(
        int32, "refId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId7: int = ParamField(
        int32, "refId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId8: int = ParamField(
        int32, "refId8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId9: int = ParamField(
        int32, "refId9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefId10: int = ParamField(
        int32, "refId10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType1: int = ParamField(
        uint8, "consumeType1", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType2: int = ParamField(
        uint8, "consumeType2", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType3: int = ParamField(
        uint8, "consumeType3", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType4: int = ParamField(
        uint8, "consumeType4", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType5: int = ParamField(
        uint8, "consumeType5", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType6: int = ParamField(
        uint8, "consumeType6", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType7: int = ParamField(
        uint8, "consumeType7", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType8: int = ParamField(
        uint8, "consumeType8", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType9: int = ParamField(
        uint8, "consumeType9", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeType10: int = ParamField(
        uint8, "consumeType10", MAGIC_CONSUME_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeLoopMPforMenu: int = ParamField(
        int16, "consumeLoopMP_forMenu", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad[8]")
