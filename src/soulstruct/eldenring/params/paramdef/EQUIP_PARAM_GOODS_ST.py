from __future__ import annotations

__all__ = ["EQUIP_PARAM_GOODS_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


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
    AnimationVariationID: int = ParamField(
        int, "sfxVariationId", default=-1,
        tooltip="Animation variation ID to combine with the base usage animation.",
    )
    Weight: float = ParamField(
        float, "weight", default=1.0,
        tooltip="Weight of good. Never used in vanilla Dark Souls.",
    )
    BasicPrice: int = ParamField(
        int, "basicPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FramptSellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
    )
    Behavior: int = ParamField(
        int, "behaviorId", game_type=BehaviorParam, default=0,
        tooltip="Behavior triggered by good use. Never used.",
    )
    GoodToReplace: int = ParamField(
        int, "replaceItemId", default=-1,
        tooltip="Good to replace when this item is obtained. Used only for full/empty Estus Flask exchange.",
    )
    SortIndex: int = ParamField(
        int, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    AppearanceReplaceItemId: int = ParamField(
        int, "appearanceReplaceItemId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ConfirmationMessage: int = ParamField(
        int, "yesNoDialogMessageId", default=-1,
        tooltip="Message displayed in yes/no dialog box to confirm use of good.",
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
    GoodIcon: int = ParamField(
        ushort, "iconId", game_type=Icon, default=0,
        tooltip="Good icon texture ID.",
    )
    ModelID: int = ParamField(
        ushort, "modelId", game_type=EquipmentModel, default=0,
        tooltip="Model of good. Never used.",
    )
    ShopLevel: int = ParamField(
        short, "shopLv", default=0,
        tooltip="Level of good that can be sold in 'the shop'. Always -1 or 0. Probably unused.",
    )
    CollectionAchievementID: int = ParamField(
        short, "compTrophySedId", default=-1,
        tooltip="Collection achievement (e.g. all spells) to which obtaining this good contributes.",
    )
    AchievementID: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="Achievement unlocked when this good is first obtained (e.g. Estus Flask).",
    )
    MaxHoldQuantity: int = ParamField(
        short, "maxNum", default=0,
        tooltip="Maximum number of good that can be held at once.",
    )
    HumanityCost: int = ParamField(
        byte, "consumeHeroPoint", default=0,
        tooltip="Humanity cost of using good. Always zero.",
    )
    OverDexterity: int = ParamField(
        byte, "overDexterity", default=0,
        tooltip="'Skill over start value'. Unknown effect; set to 0 for spells and 50 otherwise.",
    )
    GoodType: int = ParamField(
        byte, "goodsType", GOODS_TYPE, default=0,
        tooltip="Determines if this is a basic good, upgrade material, key item, or spell.",
    )
    ReferenceType: int = ParamField(
        byte, "refCategory", BEHAVIOR_REF_TYPE, default=0,
        tooltip="Indicates if this good triggers a Bullet or Special Effect. (Attacks are possible, but unused.)",
    )
    SpecialEffectCategory: int = ParamField(
        byte, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' "
                "for thrown goods and 'No Category' otherwise.",
    )
    _Pad2: bytes = ParamPad(1, "pad3[1]")
    UseAnimation: int = ParamField(
        byte, "goodsUseAnim", GOODS_USE_ANIM, default=0,
        tooltip="Points to basic animation used when good is used. Visual/sound effects are set by the variation ID.",
    )
    MenuActivated: int = ParamField(
        byte, "opmeMenuType", GOODS_OPEN_MENU, default=0,
        tooltip="Menu activated (if any) when good is used. Generally only 'No Menu' or 'Yes or No Menu' will be "
                "useful.",
    )
    LimitCategory: int = ParamField(
        byte, "useLimitCategory", SP_EFFECT_USELIMIT_CATEGORY, default=0,
        tooltip="Only one good-triggered special effect with this category can be active at once. Additional attempts "
                "to use goods in this category will be prevented. (Unclear how Dragon Stones work, though.)",
    )
    ReplaceCategory: int = ParamField(
        byte, "replaceCategory", REPLACE_CATEGORY, default=0,
        tooltip="The special effect triggered by this good will replace any special effects in the same category as "
                "this one. Used only by Dragon Stones.",
    )
    _Pad3: bytes = ParamPad(2, "reserve4[2]")
    UseableByHumans: bool = ParamField(
        byte, "enable_live:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used by characters who have revived to Human status.",
    )
    UseableByHollows: bool = ParamField(
        byte, "enable_gray:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used by characters who are Hollow.",
    )
    UseableByWhitePhantoms: bool = ParamField(
        byte, "enable_white:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used by White Phantoms (summons).",
    )
    UseableByBlackPhantoms: bool = ParamField(
        byte, "enable_black:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used by Black Phantoms (invaders).",
    )
    UseableInMultiplayer: bool = ParamField(
        byte, "enable_multi:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used while multiple players are together.",
    )
    DisabledOffline: bool = ParamField(
        byte, "disable_offline:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used while the game is disconnected from the network.",
    )
    CanBeEquipped: bool = ParamField(
        byte, "isEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be equipped in a quick item slot.",
    )
    ConsumedOnUse: bool = ParamField(
        byte, "isConsume:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good is consumed (count decreases) when used.",
    )
    AutomaticallyEquipped: bool = ParamField(
        byte, "isAutoEquip:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good will be equipped in an available quick slot when obtained.",
    )
    IsStationary: bool = ParamField(
        byte, "isEstablishment:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Unknown; need to look at usage.",
    )
    IsUnique: bool = ParamField(
        byte, "isOnlyOne:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if only one of this good exists in the game.",
    )
    IsDiscard: bool = ParamField(
        byte, "isDiscard:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    CanBeStored: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if good can be stored in Bottomless Box.",
    )
    IsDisableHand: bool = ParamField(
        byte, "isDisableHand:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Not sure. Could disable model hand when good is used?",
    )
    IsRemoveItemforGameClear: bool = ParamField(
        byte, "isRemoveItem_forGameClear:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEmptyEstusFlask: bool = ParamField(
        byte, "isSuppleItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Not sure. Only enabled for empty Estus Flask.",
    )
    IsNonEmptyEstusFlask: bool = ParamField(
        byte, "isFullSuppleItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Not sure. Only enabled for non-empty Estus Flask.",
    )
    IsUpgradeMaterial: bool = ParamField(
        byte, "isEnhance:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this is an upgrade material.",
    )
    IsFixItem: bool = ParamField(
        byte, "isFixItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Probably True for Repair Powder, etc.",
    )
    DisableMultiplayerShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this good cannot be given to other players by dropping it.",
    )
    DisabledInArena: bool = ParamField(
        byte, "disableUseAtColiseum:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this good cannot be used in the PvP Arena in Oolacile.",
    )
    DisabledOutsideArena: bool = ParamField(
        byte, "disableUseAtOutOfColiseum:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this good cannot be used outside the PvP Arena in Oolacile.",
    )
    IsEnableFastUseItem: bool = ParamField(
        byte, "isEnableFastUseItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ApplySpecialEffect: bool = ParamField(
        byte, "isApplySpecialEffect:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TODO",
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
        tooltip="TODO",
    )
    VagrantItemLot: int = ParamField(
        int, "vagrantItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
    )
    VagrantBonusEnemyDropItemLot: int = ParamField(
        int, "vagrantBonusEneDropItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
    )
    VagrantItemEnemyDropItemLot: int = ParamField(
        int, "vagrantItemEneDropItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
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
        tooltip="TODO",
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
    CanBeDropped: bool = ParamField(
        byte, "isDrop:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this item can be dropped.",
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
    MaxStorageCount: int = ParamField(
        short, "maxRepositoryNum", default=0,
        tooltip="TODO",
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
