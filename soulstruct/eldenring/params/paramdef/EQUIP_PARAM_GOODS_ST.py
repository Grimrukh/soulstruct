from __future__ import annotations

__all__ = ["EQUIP_PARAM_GOODS_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_GOODS_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    RefIddefault: int = ParamField(
        int, "refId_default", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AnimationVariationID: int = ParamField(
        int, "sfxVariationId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Weight: float = ParamField(
        float, "weight", default=1,
        tooltip="TOOLTIP-TODO",
    )
    BasicPrice: int = ParamField(
        int, "basicPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FramptSellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Behavior: int = ParamField(
        int, "behaviorId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodToReplace: int = ParamField(
        int, "replaceItemId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SortIndex: int = ParamField(
        int, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AppearanceReplaceItemId: int = ParamField(
        int, "appearanceReplaceItemId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConfirmationMessage: int = ParamField(
        int, "yesNoDialogMessageId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UseEnableSpEffectType: int = ParamField(
        ushort, "useEnableSpEffectType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PotGroupId: int = ParamField(
        sbyte, "potGroupId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad[1]")
    GoodIcon: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelID: int = ParamField(
        ushort, "modelId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShopLevel: int = ParamField(
        short, "shopLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CollectionAchievementID: int = ParamField(
        short, "compTrophySedId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AchievementID: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaxHoldQuantity: int = ParamField(
        short, "maxNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HumanityCost: int = ParamField(
        byte, "consumeHeroPoint", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverDexterity: int = ParamField(
        byte, "overDexterity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GoodType: int = ParamField(
        byte, "goodsType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReferenceType: int = ParamField(
        byte, "refCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectCategory: int = ParamField(
        byte, "spEffectCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad3[1]")
    UseAnimation: int = ParamField(
        byte, "goodsUseAnim", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuActivated: int = ParamField(
        byte, "opmeMenuType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LimitCategory: int = ParamField(
        byte, "useLimitCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceCategory: int = ParamField(
        byte, "replaceCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(2, "reserve4[2]")
    UseableByHumans: int = ParamField(
        byte, "enable_live:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByHollows: int = ParamField(
        byte, "enable_gray:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByWhitePhantoms: int = ParamField(
        byte, "enable_white:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableByBlackPhantoms: int = ParamField(
        byte, "enable_black:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseableInMultiplayer: int = ParamField(
        byte, "enable_multi:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisabledOffline: int = ParamField(
        byte, "disable_offline:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanBeEquipped: int = ParamField(
        byte, "isEquip:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ConsumedOnUse: int = ParamField(
        byte, "isConsume:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutomaticallyEquipped: int = ParamField(
        byte, "isAutoEquip:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsStationary: int = ParamField(
        byte, "isEstablishment:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUnique: int = ParamField(
        byte, "isOnlyOne:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDiscard: int = ParamField(
        byte, "isDiscard:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanBeStored: int = ParamField(
        byte, "isDeposit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableHand: int = ParamField(
        byte, "isDisableHand:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsRemoveItemforGameClear: int = ParamField(
        byte, "isRemoveItem_forGameClear:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEmptyEstusFlask: int = ParamField(
        byte, "isSuppleItem:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsNonEmptyEstusFlask: int = ParamField(
        byte, "isFullSuppleItem:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUpgradeMaterial: int = ParamField(
        byte, "isEnhance:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsFixItem: int = ParamField(
        byte, "isFixItem:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiplayerShare: int = ParamField(
        byte, "disableMultiDropShare:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisabledInArena: int = ParamField(
        byte, "disableUseAtColiseum:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisabledOutsideArena: int = ParamField(
        byte, "disableUseAtOutOfColiseum:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableFastUseItem: int = ParamField(
        byte, "isEnableFastUseItem:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ApplySpecialEffect: int = ParamField(
        byte, "isApplySpecialEffect:1", default=0,
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
    VirtualWeaponID: int = ParamField(
        int, "refVirtualWepId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VagrantItemLot: int = ParamField(
        int, "vagrantItemLotId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VagrantBonusEnemyDropItemLot: int = ParamField(
        int, "vagrantBonusEneDropItemLotId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VagrantItemEnemyDropItemLot: int = ParamField(
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
    EnableActiveBigRune: int = ParamField(
        byte, "enable_ActiveBigRune:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBonfireWarpItem: int = ParamField(
        byte, "isBonfireWarpItem:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableLadder: int = ParamField(
        byte, "enable_Ladder:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUseMultiPlayPreparation: int = ParamField(
        byte, "isUseMultiPlayPreparation:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanMultiUse: int = ParamField(
        byte, "canMultiUse:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsShieldEnchant: int = ParamField(
        byte, "isShieldEnchant:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsWarpProhibited: int = ParamField(
        byte, "isWarpProhibited:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsUseMultiPenaltyOnly: int = ParamField(
        byte, "isUseMultiPenaltyOnly:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SuppleType: int = ParamField(
        byte, "suppleType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoReplenishType: int = ParamField(
        byte, "autoReplenishType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CanBeDropped: int = ParamField(
        byte, "isDrop:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: int = ParamField(
        byte, "showLogCondType:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsSummonHorse: int = ParamField(
        byte, "isSummonHorse:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        byte, "showDialogCondType:2", default=2,
        tooltip="TOOLTIP-TODO",
    )
    IsSleepCollectionItem: int = ParamField(
        byte, "isSleepCollectionItem:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnableRiding: int = ParamField(
        byte, "enableRiding:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableRiding: int = ParamField(
        byte, "disableRiding:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaxStorageCount: int = ParamField(
        short, "maxRepositoryNum", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortGroupId: int = ParamField(
        byte, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
    IsUseNoAttackRegion: int = ParamField(
        byte, "isUseNoAttackRegion:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad5: bytes = ParamPad(1, "pad1:7")
    SaleValue: int = ParamField(
        int, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        byte, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLimitSummonBuddy: int = ParamField(
        byte, "useLimitSummonBuddy", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UseLimitSpEffectType: int = ParamField(
        ushort, "useLimitSpEffectType", default=0,
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
    _Pad6: bytes = ParamPad(2, "reserve5[2]")
    ItemGetTutorialFlagId: int = ParamField(
        uint, "itemGetTutorialFlagId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad7: bytes = ParamPad(8, "reserve3[8]")
