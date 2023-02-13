from __future__ import annotations

__all__ = ["EQUIP_PARAM_GOODS_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_GOODS_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    RefIddefault: int = ParamField(
        int, "refId_default", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxVariationId: int = ParamField(
        int, "sfxVariationId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Weight: float = ParamField(
        float, "weight", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BasicPrice: int = ParamField(
        int, "basicPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorId: int = ParamField(
        int, "behaviorId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceItemId: int = ParamField(
        int, "replaceItemId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SortId: int = ParamField(
        int, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AppearanceReplaceItemId: int = ParamField(
        int, "appearanceReplaceItemId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    YesNoDialogMessageId: int = ParamField(
        int, "yesNoDialogMessageId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UseEnableSpEffectType: int = ParamField(
        ushort, "useEnableSpEffectType", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PotGroupId: int = ParamField(
        sbyte, "potGroupId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad[1]")
    IconId: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelId: int = ParamField(
        ushort, "modelId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShopLv: int = ParamField(
        short, "shopLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CompTrophySedId: int = ParamField(
        short, "compTrophySedId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TrophySeqId: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxNum: int = ParamField(
        short, "maxNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeHeroPoint: int = ParamField(
        byte, "consumeHeroPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverDexterity: int = ParamField(
        byte, "overDexterity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodsType: int = ParamField(
        byte, "goodsType", GOODS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory: int = ParamField(
        byte, "refCategory", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectCategory: int = ParamField(
        byte, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad3[1]")
    GoodsUseAnim: int = ParamField(
        byte, "goodsUseAnim", GOODS_USE_ANIM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OpmeMenuType: int = ParamField(
        byte, "opmeMenuType", GOODS_OPEN_MENU, default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLimitCategory: int = ParamField(
        byte, "useLimitCategory", SP_EFFECT_USELIMIT_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceCategory: int = ParamField(
        byte, "replaceCategory", REPLACE_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(2, "reserve4[2]")
    Enablelive: bool = ParamField(
        byte, "enable_live:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Enablegray: bool = ParamField(
        byte, "enable_gray:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Enablewhite: bool = ParamField(
        byte, "enable_white:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Enableblack: bool = ParamField(
        byte, "enable_black:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Enablemulti: bool = ParamField(
        byte, "enable_multi:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Disableoffline: bool = ParamField(
        byte, "disable_offline:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEquip: bool = ParamField(
        byte, "isEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsConsume: bool = ParamField(
        byte, "isConsume:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAutoEquip: bool = ParamField(
        byte, "isAutoEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEstablishment: bool = ParamField(
        byte, "isEstablishment:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsOnlyOne: bool = ParamField(
        byte, "isOnlyOne:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDiscard: bool = ParamField(
        byte, "isDiscard:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDeposit: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableHand: bool = ParamField(
        byte, "isDisableHand:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsRemoveItemforGameClear: bool = ParamField(
        byte, "isRemoveItem_forGameClear:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSuppleItem: bool = ParamField(
        byte, "isSuppleItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFullSuppleItem: bool = ParamField(
        byte, "isFullSuppleItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnhance: bool = ParamField(
        byte, "isEnhance:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsFixItem: bool = ParamField(
        byte, "isFixItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiDropShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableUseAtColiseum: bool = ParamField(
        byte, "disableUseAtColiseum:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableUseAtOutOfColiseum: bool = ParamField(
        byte, "disableUseAtOutOfColiseum:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableFastUseItem: bool = ParamField(
        byte, "isEnableFastUseItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsApplySpecialEffect: bool = ParamField(
        byte, "isApplySpecialEffect:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    SyncNumVaryId: int = ParamField(
        byte, "syncNumVaryId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefId1: int = ParamField(
        int, "refId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefVirtualWepId: int = ParamField(
        int, "refVirtualWepId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VagrantItemLotId: int = ParamField(
        int, "vagrantItemLotId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VagrantBonusEneDropItemLotId: int = ParamField(
        int, "vagrantBonusEneDropItemLotId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VagrantItemEneDropItemLotId: int = ParamField(
        int, "vagrantItemEneDropItemLotId", default=0,
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
    EnableActiveBigRune: bool = ParamField(
        byte, "enable_ActiveBigRune:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBonfireWarpItem: bool = ParamField(
        byte, "isBonfireWarpItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableLadder: bool = ParamField(
        byte, "enable_Ladder:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseMultiPlayPreparation: bool = ParamField(
        byte, "isUseMultiPlayPreparation:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanMultiUse: bool = ParamField(
        byte, "canMultiUse:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsShieldEnchant: bool = ParamField(
        byte, "isShieldEnchant:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsWarpProhibited: bool = ParamField(
        byte, "isWarpProhibited:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsUseMultiPenaltyOnly: bool = ParamField(
        byte, "isUseMultiPenaltyOnly:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    SuppleType: int = ParamField(
        byte, "suppleType", GOODS_SUPPLE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoReplenishType: int = ParamField(
        byte, "autoReplenishType", AUTO_REPLENISH_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDrop: bool = ParamField(
        byte, "isDrop:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: bool = ParamField(
        byte, "showLogCondType:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsSummonHorse: bool = ParamField(
        byte, "isSummonHorse:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        byte, "showDialogCondType:2", GET_DIALOG_CONDITION_TYPE, bit_count=2, default=2,
        tooltip="TOOLTIP-TODO",
    )
    IsSleepCollectionItem: bool = ParamField(
        byte, "isSleepCollectionItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    EnableRiding: bool = ParamField(
        byte, "enableRiding:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableRiding: bool = ParamField(
        byte, "disableRiding:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    MaxRepositoryNum: int = ParamField(
        short, "maxRepositoryNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortGroupId: int = ParamField(
        byte, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
    IsUseNoAttackRegion: bool = ParamField(
        byte, "isUseNoAttackRegion:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad1:7", bit_count=7)
    SaleValue: int = ParamField(
        int, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        byte, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLimitSummonBuddy: int = ParamField(
        byte, "useLimitSummonBuddy", GOODS_USELIMIT_SUMMONBUDDY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLimitSpEffectType: int = ParamField(
        ushort, "useLimitSpEffectType", SP_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AiUseJudgeId: int = ParamField(
        int, "aiUseJudgeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeMP: int = ParamField(
        short, "consumeMP", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumeHP: int = ParamField(
        short, "consumeHP", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReinforceGoodsId: int = ParamField(
        int, "reinforceGoodsId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReinforceMaterialId: int = ParamField(
        int, "reinforceMaterialId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReinforcePrice: int = ParamField(
        int, "reinforcePrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType0: int = ParamField(
        sbyte, "useLevel_vowType0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType1: int = ParamField(
        sbyte, "useLevel_vowType1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType2: int = ParamField(
        sbyte, "useLevel_vowType2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType3: int = ParamField(
        sbyte, "useLevel_vowType3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType4: int = ParamField(
        sbyte, "useLevel_vowType4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType5: int = ParamField(
        sbyte, "useLevel_vowType5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType6: int = ParamField(
        sbyte, "useLevel_vowType6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType7: int = ParamField(
        sbyte, "useLevel_vowType7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType8: int = ParamField(
        sbyte, "useLevel_vowType8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType9: int = ParamField(
        sbyte, "useLevel_vowType9", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType10: int = ParamField(
        sbyte, "useLevel_vowType10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType11: int = ParamField(
        sbyte, "useLevel_vowType11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType12: int = ParamField(
        sbyte, "useLevel_vowType12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType13: int = ParamField(
        sbyte, "useLevel_vowType13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType14: int = ParamField(
        sbyte, "useLevel_vowType14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevelvowType15: int = ParamField(
        sbyte, "useLevel_vowType15", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLevel: int = ParamField(
        ushort, "useLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(2, "reserve5[2]")
    ItemGetTutorialFlagId: int = ParamField(
        uint, "itemGetTutorialFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(8, "reserve3[8]")
