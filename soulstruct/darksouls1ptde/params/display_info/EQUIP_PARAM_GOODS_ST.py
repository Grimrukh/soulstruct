from __future__ import annotations

__all__ = ["EQUIP_PARAM_GOODS_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, DynamicParamFieldInfo, pad_field
from soulstruct.darksouls1ptde.game_types import *
from ..enums import *


class DynamicGoodRef(DynamicParamFieldInfo):

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
                "Bullet triggered by using good (which may simply be targeted at self).",
            )
        elif entry[self.type_field_name] == BEHAVIOR_REF_TYPE.SpecialEffect:
            return ParamFieldInfo(
                self.name,
                "SpecialEffect",
                True,
                SpecialEffectParam,
                "Special effect triggered (on self) by using good.",
            )
        else:
            return ParamFieldInfo(
                self.name,
                "UnknownReferenceID",
                True,
                int,
                "Could not determine reference ID type (usually Bullet or SpecialEffect).",
            )


EQUIP_PARAM_GOODS_ST = {
    "param_type": "EQUIP_PARAM_GOODS_ST",
    "file_name": "EquipParamGoods",
    "nickname": "Goods",
    "fields": [
        DynamicGoodRef("refId", "refCategory"),
        ParamFieldInfo(
            "sfxVariationId",
            "AnimationVariationID",
            True,
            int,
            "Animation variation ID to combine with the base usage animation.",
        ),
        ParamFieldInfo("weight", "Weight", False, float, "Weight of good. Never used in vanilla Dark Souls."),
        ParamFieldInfo("basicPrice", "BasicCost", False, int, "Unsure. Does not appear to be used."),
        ParamFieldInfo(
            "sellValue",
            "FramptSellValue",
            True,
            int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
        ),
        ParamFieldInfo("behaviorId", "Behavior", False, BehaviorParam, "Behavior triggered by good use. Never used."),
        ParamFieldInfo(
            "replaceItemId",
            "GoodToReplace",
            True,
            GoodParam,
            "Good to replace when this item is obtained. Used only for full/empty Estus Flask exchange.",
        ),
        ParamFieldInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        ParamFieldInfo("qwcId", "QWCID", False, int, "Unused world tendency remnant."),
        ParamFieldInfo(
            "yesNoDialogMessageId",
            "ConfirmationMessage",
            True,
            EventText,
            "Message displayed in yes/no dialog box to confirm use of good.",
        ),
        ParamFieldInfo(
            "magicId",
            "Spell",
            True,
            SpellParam,
            "Spell unlocked in attunement menu by possession of this good. (Usually matches the good ID.)",
        ),
        ParamFieldInfo("iconId", "GoodIcon", True, Texture, "Good icon texture ID."),
        ParamFieldInfo("modelId", "ModelID", False, int, "Model of good. Never used."),
        ParamFieldInfo(
            "shopLv",
            "ShopLevel",
            False,
            int,
            "Level of good that can be sold in 'the shop'. Always -1 or 0. Probably unused.",
        ),
        ParamFieldInfo(
            "compTrophySedId",
            "CollectionAchievementID",
            False,
            int,
            "Collection achievement (e.g. all spells) to which obtaining this good contributes.",
        ),
        ParamFieldInfo(
            "trophySeqId",
            "AchievementID",
            False,
            int,
            "Achievement unlocked when this good is first obtained (e.g. Estus Flask).",
        ),
        ParamFieldInfo("maxNum", "MaxHoldQuantity", True, int, "Maximum number of good that can be held at once."),
        ParamFieldInfo("consumeHeroPoint", "HumanityCost", False, int, "Humanity cost of using good. Always zero."),
        ParamFieldInfo(
            "overDexterity",
            "OverDexterity",
            False,
            int,
            "'Skill over start value'. Unknown effect; set to 0 for spells and 50 otherwise.",
        ),
        ParamFieldInfo(
            "goodsType",
            "GoodType",
            True,
            GOODS_TYPE,
            "Determines if this is a basic good, upgrade material, key item, or spell.",
        ),
        ParamFieldInfo(
            "refCategory",
            "ReferenceType",
            True,
            BEHAVIOR_REF_TYPE,
            "Indicates if this good triggers a Bullet or Special Effect. (Attacks are possible, but unused.)",
        ),
        ParamFieldInfo(
            "spEffectCategory",
            "SpecialEffectCategory",
            True,
            BEHAVIOR_CATEGORY,
            "Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' "
            "for thrown goods and 'No Category' otherwise.",
        ),
        ParamFieldInfo("goodsCategory", "GoodCategory", False, GOODS_CATEGORY, "Never used. Only one value (0) used."),
        ParamFieldInfo(
            "goodsUseAnim",
            "UseAnimation",
            True,
            GOODS_USE_ANIM,
            "Points to basic animation used when good is used. Visual/sound effects are set by the variation ID.",
        ),
        ParamFieldInfo(
            "opmeMenuType",
            "MenuActivated",
            True,
            GOODS_OPEN_MENU,
            "Menu activated (if any) when good is used. Generally only 'No Menu' or 'Yes or No Menu' will be "
            "useful.",
        ),
        ParamFieldInfo(
            "useLimitCategory",
            "LimitCategory",
            True,
            SP_EFFECT_USELIMIT_CATEGORY,
            "Only one good-triggered special effect with this category can be active at once. Additional attempts "
            "to use goods in this category will be prevented. (Unclear how Dragon Stones work, though.)",
        ),
        ParamFieldInfo(
            "replaceCategory",
            "ReplaceCategory",
            False,
            REPLACE_CATEGORY,
            "The special effect triggered by this good will replace any special effects in the same category as "
            "this one. Used only by Dragon Stones.",
        ),
        ParamFieldInfo(
            "vowType0:1",
            "UseableByNoCovenant",
            True,
            bool,
            "Determines if this good can be used by characters with no covenant.",
        ),
        ParamFieldInfo(
            "vowType1:1",
            "UseableByWayOfWhite",
            True,
            bool,
            "Determines if this good can be used by characters in the Way of White.",
        ),
        ParamFieldInfo(
            "vowType2:1",
            "UseableByPrincessGuard",
            True,
            bool,
            "Determines if this good can be used by characters in the Princess's Guard.",
        ),
        ParamFieldInfo(
            "vowType3:1",
            "UseableByWarriorsOfSunlight",
            True,
            bool,
            "Determines if this good can be used by characters in the Warriors of Sunlight.",
        ),
        ParamFieldInfo(
            "vowType4:1",
            "UseableByDarkwraith",
            True,
            bool,
            "Determines if this good can be used by characters in the Darkwraith covenant.",
        ),
        ParamFieldInfo(
            "vowType5:1",
            "UseableByPathOfTheDragon",
            True,
            bool,
            "Determines if this good can be used by characters in the Path of the Dragon.",
        ),
        ParamFieldInfo(
            "vowType6:1",
            "UseableByGravelordServant",
            True,
            bool,
            "Determines if this good can be used by characters in the Gravelord Servants.",
        ),
        ParamFieldInfo(
            "vowType7:1",
            "UseableByForestHunter",
            True,
            bool,
            "Determines if this good can be used by characters in the Forest Hunters.",
        ),
        ParamFieldInfo(
            "vowType8:1",
            "UseableByDarkmoonBlade",
            True,
            bool,
            "Determines if this good can be used by characters in the Blades of the Darkmoon.",
        ),
        ParamFieldInfo(
            "vowType9:1",
            "UseableByChaosServant",
            True,
            bool,
            "Determines if this good can be used by characters in the Chaos Servant covenant.",
        ),
        ParamFieldInfo(
            "vowType10:1",
            "UseableByCovenant10",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 10.",
        ),
        ParamFieldInfo(
            "vowType11:1",
            "UseableByCovenant11",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 11.",
        ),
        ParamFieldInfo(
            "vowType12:1",
            "UseableByCovenant12",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 12.",
        ),
        ParamFieldInfo(
            "vowType13:1",
            "UseableByCovenant13",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 13.",
        ),
        ParamFieldInfo(
            "vowType14:1",
            "UseableByCovenant14",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 14.",
        ),
        ParamFieldInfo(
            "vowType15:1",
            "UseableByCovenant15",
            False,
            bool,
            "Determines if this good can be used by characters in unused covenant 15.",
        ),
        ParamFieldInfo(
            "enable_live:1",
            "UseableByHumans",
            True,
            bool,
            "Determines if this good can be used by characters who have revived to Human status.",
        ),
        ParamFieldInfo(
            "enable_gray:1",
            "UseableByHollows",
            True,
            bool,
            "Determines if this good can be used by characters who are Hollow.",
        ),
        ParamFieldInfo(
            "enable_white:1",
            "UseableByWhitePhantoms",
            True,
            bool,
            "Determines if this good can be used by White Phantoms (summons).",
        ),
        ParamFieldInfo(
            "enable_black:1",
            "UseableByBlackPhantoms",
            True,
            bool,
            "Determines if this good can be used by Black Phantoms (invaders).",
        ),
        ParamFieldInfo(
            "enable_multi:1",
            "UseableInMultiplayer",
            True,
            bool,
            "Determines if this good can be used while multiple players are together.",
        ),
        ParamFieldInfo(
            "disable_offline:1",
            "DisabledOffline",
            True,
            bool,
            "Determines if this good can be used while the game is disconnected from the network.",
        ),
        ParamFieldInfo(
            "isEquip:1",
            "CanBeEquipped",
            True,
            bool,
            "Determines if this good can be equipped in a quick item slot.",
        ),
        ParamFieldInfo(
            "isConsume:1",
            "ConsumedOnUse",
            True,
            bool,
            "Determines if this good is consumed (count decreases) when used.",
        ),
        ParamFieldInfo(
            "isAutoEquip:1",
            "AutomaticallyEquipped",
            True,
            bool,
            "Determines if this good will be equipped in an available quick slot when obtained.",
        ),
        ParamFieldInfo("isEstablishment:1", "IsStationary", True, bool, "Unknown; need to look at usage."),
        ParamFieldInfo("isOnlyOne:1", "IsUnique", True, bool, "Determines if only one of this good exists in the game."),
        ParamFieldInfo("isDrop:1", "CanBeDropped", True, bool, "Determines if this item can be dropped."),
        ParamFieldInfo("isDeposit:1", "CanBeStored", True, bool, "Determines if good can be stored in Bottomless Box."),
        ParamFieldInfo(
            "isDisableHand:1", "IsDisableHand?", True, bool, "Not sure. Could disable model hand when good is used?"
        ),
        ParamFieldInfo(
            "IsTravelItem:1", "IsTravelItem?", True, bool, "Not sure. Could flag items that warp the player."
        ),
        ParamFieldInfo(
            "isSuppleItem:1", "IsEmptyEstusFlask?", True, bool, "Not sure. Only enabled for empty Estus Flask."
        ),
        ParamFieldInfo(
            "isFullSuppleItem:1",
            "IsNonEmptyEstusFlask?",
            True,
            bool,
            "Not sure. Only enabled for non-empty Estus Flask.",
        ),
        ParamFieldInfo("isEnhance:1", "IsUpgradeMaterial", True, bool, "Determines if this is an upgrade material."),
        ParamFieldInfo("isFixItem:1", "IsFixItem?", True, bool, "Probably True for Repair Powder, etc."),
        ParamFieldInfo(
            "disableMultiDropShare:1",
            "DisableMultiplayerShare",
            True,
            bool,
            "If True, this good cannot be given to other players by dropping it.",
        ),
        ParamFieldInfo(
            "disableUseAtColiseum:1",
            "DisabledInArena",
            False,
            bool,
            "If True, this good cannot be used in the PvP Arena in Oolacile.",
        ),
        ParamFieldInfo(
            "disableUseAtOutOfColiseum:1",
            "DisabledOutsideArena",
            False,
            bool,
            "If True, this good cannot be used outside the PvP Arena in Oolacile.",
        ),
        ParamFieldInfo("pad[9]", "Pad1", False, pad_field(9), "Null padding."),
        ParamFieldInfo("vagrantItemLotId", "VagrantItemLot", False, ItemLotParam, ""),
        ParamFieldInfo(
            "vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", False, ItemLotParam, ""
        ),
        ParamFieldInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", False, ItemLotParam, ""),
    ],
}
