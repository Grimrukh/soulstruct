from __future__ import annotations

__all__ = ["MAGIC_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MAGIC_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    YesNoDialogMessageId: int = ParamField(
        int, "yesNoDialogMessageId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LimitCancelSpEffectId: int = ParamField(
        int, "limitCancelSpEffectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SortId: int = ParamField(
        short, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequirementLuck: int = ParamField(
        byte, "requirementLuck", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiNotifyType: int = ParamField(
        byte, "aiNotifyType", MAGIC_AI_NOTIFY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Mp: int = ParamField(
        short, "mp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Stamina: int = ParamField(
        short, "stamina", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        short, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorId: int = ParamField(
        short, "behaviorId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MtrlItemId: int = ParamField(
        short, "mtrlItemId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceMagicId: int = ParamField(
        short, "replaceMagicId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxQuantity: int = ParamField(
        short, "maxQuantity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory1: int = ParamField(
        byte, "refCategory1", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverDexterity: int = ParamField(
        byte, "overDexterity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory2: int = ParamField(
        byte, "refCategory2", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SlotLength: int = ParamField(
        byte, "slotLength", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequirementIntellect: int = ParamField(
        byte, "requirementIntellect", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequirementFaith: int = ParamField(
        byte, "requirementFaith", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnalogDexterityMin: int = ParamField(
        byte, "analogDexterityMin", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnalogDexterityMax: int = ParamField(
        byte, "analogDexterityMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EzStateBehaviorType: int = ParamField(
        byte, "ezStateBehaviorType", MAGIC_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory3: int = ParamField(
        byte, "refCategory3", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectCategory: int = ParamField(
        byte, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefType: int = ParamField(
        byte, "refType", MAGIC_MOTION_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OpmeMenuType: int = ParamField(
        byte, "opmeMenuType", GOODS_OPEN_MENU, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory4: int = ParamField(
        byte, "refCategory4", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    HasSpEffectType: int = ParamField(
        ushort, "hasSpEffectType", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceCategory: int = ParamField(
        byte, "replaceCategory", REPLACE_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLimitCategory: int = ParamField(
        byte, "useLimitCategory", SP_EFFECT_USELIMIT_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    VowType0: bool = ParamField(
        byte, "vowType0:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType1: bool = ParamField(
        byte, "vowType1:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType2: bool = ParamField(
        byte, "vowType2:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType3: bool = ParamField(
        byte, "vowType3:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType4: bool = ParamField(
        byte, "vowType4:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType5: bool = ParamField(
        byte, "vowType5:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType6: bool = ParamField(
        byte, "vowType6:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType7: bool = ParamField(
        byte, "vowType7:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Enablemulti: bool = ParamField(
        byte, "enable_multi:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Enablemultionly: bool = ParamField(
        byte, "enable_multi_only:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnchant: bool = ParamField(
        byte, "isEnchant:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsShieldEnchant: bool = ParamField(
        byte, "isShieldEnchant:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Enablelive: bool = ParamField(
        byte, "enable_live:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Enablegray: bool = ParamField(
        byte, "enable_gray:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Enablewhite: bool = ParamField(
        byte, "enable_white:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Enableblack: bool = ParamField(
        byte, "enable_black:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableOffline: bool = ParamField(
        byte, "disableOffline:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CastResonanceMagic: bool = ParamField(
        byte, "castResonanceMagic:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
    VowType8: bool = ParamField(
        byte, "vowType8:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType9: bool = ParamField(
        byte, "vowType9:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType10: bool = ParamField(
        byte, "vowType10:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType11: bool = ParamField(
        byte, "vowType11:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType12: bool = ParamField(
        byte, "vowType12:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType13: bool = ParamField(
        byte, "vowType13:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType14: bool = ParamField(
        byte, "vowType14:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    VowType15: bool = ParamField(
        byte, "vowType15:1", MAGIC_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
