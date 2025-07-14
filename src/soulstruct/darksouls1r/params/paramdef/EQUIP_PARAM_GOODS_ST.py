from __future__ import annotations

__all__ = ["EQUIP_PARAM_GOODS_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1r.game_types import *
from soulstruct.darksouls1r.params.enums import *
from soulstruct.utilities.binary import *

from .dynamics import GoodReference


class EQUIP_PARAM_GOODS_ST(ParamRow):
    ReferenceID: int = ParamField(
        int32, "refId", default=-1, dynamic_callback=GoodReference(),
        tooltip="TODO",
    )
    AnimationVariationID: int = ParamField(
        int32, "sfxVariationId", default=-1,
        tooltip="Animation variation ID to combine with the base usage animation.",
    )
    Weight: float = ParamField(
        float32, "weight", default=0.0,
        tooltip="Weight of good. Never used in vanilla Dark Souls.",
    )
    BasicCost: int = ParamField(
        int32, "basicPrice", default=0,
        tooltip="Unsure. Does not appear to be used.",
    )
    FramptSellValue: int = ParamField(
        int32, "sellValue", default=0,
        tooltip="Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
    )
    Behavior: int = ParamField(
        int32, "behaviorId", game_type=BehaviorParam, default=0,
        tooltip="Behavior triggered by good use. Never used.",
    )
    GoodToReplace: int = ParamField(
        int32, "replaceItemId", default=-1,
        tooltip="Good to replace when this item is obtained. Used only for full/empty Estus Flask exchange.",
    )
    SortIndex: int = ParamField(
        int32, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    QWCID: int = ParamField(
        int32, "qwcId", default=-1,
        tooltip="Unused world tendency remnant.",
    )
    ConfirmationMessage: int = ParamField(
        int32, "yesNoDialogMessageId", default=-1,
        tooltip="Message displayed in yes/no dialog box to confirm use of good.",
    )
    Spell: int = ParamField(
        int32, "magicId", game_type=SpellParam, default=-1,
        tooltip="Spell unlocked in attunement menu by possession of this good. (Usually matches the good ID.)",
    )
    GoodIcon: int = ParamField(
        uint16, "iconId", game_type=Icon, default=0,
        tooltip="Good icon texture ID.",
    )
    ModelID: int = ParamField(
        uint16, "modelId", game_type=EquipmentModel, default=0,
        tooltip="Model of good. Never used.",
    )
    ShopLevel: int = ParamField(
        int16, "shopLv", default=-1,
        tooltip="Level of good that can be sold in 'the shop'. Always -1 or 0. Probably unused.",
    )
    CollectionAchievementID: int = ParamField(
        int16, "compTrophySedId", default=-1,
        tooltip="Collection achievement (e.g. all spells) to which obtaining this good contributes.",
    )
    AchievementID: int = ParamField(
        int16, "trophySeqId", default=-1,
        tooltip="Achievement unlocked when this good is first obtained (e.g. Estus Flask).",
    )
    MaxHoldQuantity: int = ParamField(
        int16, "maxNum", default=0,
        tooltip="Maximum number of good that can be held at once.",
    )
    HumanityCost: int = ParamField(
        uint8, "consumeHeroPoint", default=0,
        tooltip="Humanity cost of using good. Always zero.",
    )
    OverDexterity: int = ParamField(
        uint8, "overDexterity", default=0,
        tooltip="'Skill over start value'. Unknown effect; set to 0 for spells and 50 otherwise.",
    )
    GoodType: int = ParamField(
        uint8, "goodsType", GOODS_TYPE, default=0,
        tooltip="Determines if this is a basic good, upgrade material, key item, or spell.",
    )
    ReferenceType: int = ParamField(
        uint8, "refCategory", BEHAVIOR_REF_TYPE, default=0,
        tooltip="Indicates if this good triggers a Bullet or Special Effect. (Attacks are possible, but unused.)",
    )
    SpecialEffectCategory: int = ParamField(
        uint8, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' "
                "for thrown goods and 'No Category' otherwise.",
    )
    GoodCategory: int = ParamField(
        uint8, "goodsCategory", GOODS_CATEGORY, default=0,
        tooltip="Never used. Only one value (0) used.",
    )
    UseAnimation: int = ParamField(
        uint8, "goodsUseAnim", GOODS_USE_ANIM, default=0,
        tooltip="Points to basic animation used when good is used. Visual/sound effects are set by the variation ID.",
    )
    MenuActivated: int = ParamField(
        uint8, "opmeMenuType", GOODS_OPEN_MENU, default=0,
        tooltip="Menu activated (if any) when good is used. Generally only 'No Menu' or 'Yes or No Menu' will be "
                "useful.",
    )
    LimitCategory: int = ParamField(
        uint8, "useLimitCategory", SP_EFFECT_USELIMIT_CATEGORY, default=0,
        tooltip="Only one good-triggered special effect with this category can be active at once. Additional attempts "
                "to use goods in this category will be prevented. (Unclear how Dragon Stones work, though.)",
    )
    ReplaceCategory: int = ParamField(
        uint8, "replaceCategory", REPLACE_CATEGORY, default=0,
        tooltip="The special effect triggered by this good will replace any special effects in the same category as "
                "this one. Used only by Dragon Stones.",
    )
    UseableByNoCovenant: bool = ParamField(
        uint8, "vowType0:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters with no covenant.",
    )
    UseableByWayOfWhite: bool = ParamField(
        uint8, "vowType1:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in the Way of White.",
    )
    UseableByPrincessGuard: bool = ParamField(
        uint8, "vowType2:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in the Princess's Guard.",
    )
    UseableByWarriorsOfSunlight: bool = ParamField(
        uint8, "vowType3:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in the Warriors of Sunlight.",
    )
    UseableByDarkwraith: bool = ParamField(
        uint8, "vowType4:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in the Darkwraith covenant.",
    )
    UseableByPathOfTheDragon: bool = ParamField(
        uint8, "vowType5:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in the Path of the Dragon.",
    )
    UseableByGravelordServant: bool = ParamField(
        uint8, "vowType6:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in the Gravelord Servants.",
    )
    UseableByForestHunter: bool = ParamField(
        uint8, "vowType7:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in the Forest Hunters.",
    )
    UseableByDarkmoonBlade: bool = ParamField(
        uint8, "vowType8:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in the Blades of the Darkmoon.",
    )
    UseableByChaosServant: bool = ParamField(
        uint8, "vowType9:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in the Chaos Servant covenant.",
    )
    UseableByCovenant10: bool = ParamField(
        uint8, "vowType10:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in unused covenant 10.",
    )
    UseableByCovenant11: bool = ParamField(
        uint8, "vowType11:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in unused covenant 11.",
    )
    UseableByCovenant12: bool = ParamField(
        uint8, "vowType12:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in unused covenant 12.",
    )
    UseableByCovenant13: bool = ParamField(
        uint8, "vowType13:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in unused covenant 13.",
    )
    UseableByCovenant14: bool = ParamField(
        uint8, "vowType14:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in unused covenant 14.",
    )
    UseableByCovenant15: bool = ParamField(
        uint8, "vowType15:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters in unused covenant 15.",
    )
    UseableByHumans: bool = ParamField(
        uint8, "enable_live:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters who have revived to Human status.",
    )
    UseableByHollows: bool = ParamField(
        uint8, "enable_gray:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be used by characters who are Hollow.",
    )
    UseableByWhitePhantoms: bool = ParamField(
        uint8, "enable_white:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used by White Phantoms (summons).",
    )
    UseableByBlackPhantoms: bool = ParamField(
        uint8, "enable_black:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used by Black Phantoms (invaders).",
    )
    UseableInMultiplayer: bool = ParamField(
        uint8, "enable_multi:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used while multiple players are together.",
    )
    UseableInPVP: bool = ParamField(
        uint8, "enable_pvp:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used while in multiplayer PvP (invasion/arena).",
    )
    DisabledOffline: bool = ParamField(
        uint8, "disable_offline:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this good can be used while the game is disconnected from the network.",
    )
    CanBeEquipped: bool = ParamField(
        uint8, "isEquip:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good can be equipped in a quick item slot.",
    )
    ConsumedOnUse: bool = ParamField(
        uint8, "isConsume:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good is consumed (count decreases) when used.",
    )
    AutomaticallyEquipped: bool = ParamField(
        uint8, "isAutoEquip:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this good will be equipped in an available quick slot when obtained.",
    )
    IsStationary: bool = ParamField(
        uint8, "isEstablishment:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Unknown; need to look at usage.",
    )
    IsUnique: bool = ParamField(
        uint8, "isOnlyOne:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if only one of this good exists in the game.",
    )
    CanBeDropped: bool = ParamField(
        uint8, "isDrop:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if this item can be dropped.",
    )
    CanBeStored: bool = ParamField(
        uint8, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="Determines if good can be stored in Bottomless Box.",
    )
    IsDisableHand: bool = ParamField(
        uint8, "isDisableHand:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Not sure. Could disable model hand when good is used?",
    )
    IsTravelItem: bool = ParamField(
        uint8, "IsTravelItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Not sure. Could flag items that warp the player.",
    )
    IsEmptyEstusFlask: bool = ParamField(
        uint8, "isSuppleItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Not sure. Only enabled for empty Estus Flask.",
    )
    IsNonEmptyEstusFlask: bool = ParamField(
        uint8, "isFullSuppleItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Not sure. Only enabled for non-empty Estus Flask.",
    )
    IsUpgradeMaterial: bool = ParamField(
        uint8, "isEnhance:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Determines if this is an upgrade material.",
    )
    IsFixItem: bool = ParamField(
        uint8, "isFixItem:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="Probably True for Repair Powder, etc.",
    )
    DisableMultiplayerShare: bool = ParamField(
        uint8, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this good cannot be given to other players by dropping it.",
    )
    DisabledInArena: bool = ParamField(
        uint8, "disableUseAtColiseum:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this good cannot be used in the PvP Arena in Oolacile.",
    )
    DisabledOutsideArena: bool = ParamField(
        uint8, "disableUseAtOutOfColiseum:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this good cannot be used outside the PvP Arena in Oolacile.",
    )
    _Pad0: bytes = ParamPad(9, "pad[9]")
    VagrantItemLot: int = ParamField(
        int32, "vagrantItemLotId", game_type=ItemLotParam, default=-1,
        tooltip="TODO",
    )
    VagrantBonusEnemyDropItemLot: int = ParamField(
        int32, "vagrantBonusEneDropItemLotId", game_type=ItemLotParam, default=-1,
        tooltip="TODO",
    )
    VagrantItemEnemyDropItemLot: int = ParamField(
        int32, "vagrantItemEneDropItemLotId", game_type=ItemLotParam, default=-1,
        tooltip="TODO",
    )
