from __future__ import annotations

__all__ = ["EQUIP_PARAM_ACCESSORY_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field
from soulstruct.darksouls1ptde.game_types import *
from ..enums import *

EQUIP_PARAM_ACCESSORY_ST = {
    "param_type": "EQUIP_PARAM_ACCESSORY_ST",
    "file_name": "EquipParamAccessory",
    "nickname": "Rings",
    "fields": [
        ParamFieldInfo(
            "refId", "SpecialEffect", True, SpecialEffectParam, "Special effect applied when ring is equipped."
        ),
        ParamFieldInfo(
            "sfxVariationId",
            "SFXVariation",
            False,
            int,
            "SFX variation ID combined with the value specified in TAE animation data. Always -1; likely works "
            "with unused Behavior parameter below.",
        ),
        ParamFieldInfo(
            "weight",
            "Weight",
            False,
            float,
            "Weight of ring. Always set to zero in vanilla Dark Souls, but likely works just like other equipment.",
        ),
        ParamFieldInfo(
            "behaviorId",
            "Behavior",
            False,
            BehaviorParam,
            "Behavior of ring 'skill'. Always zero in the vanilla game.",
        ),
        ParamFieldInfo("basicPrice", "BasicCost", False, int, "Unknown purpose, and unused."),
        ParamFieldInfo(
            "sellValue",
            "FramptSellValue",
            True,
            int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
        ),
        ParamFieldInfo("sortId", "SortIndex", True, int, "Index for automatic inventory sorting."),
        ParamFieldInfo("qwcId", "QWCID", False, int, "Unused world tendency remnant."),
        ParamFieldInfo(
            "equipModelId", "EquipmentModel", False, int, "Always zero. (Rings have no model, presumably.)"
        ),
        ParamFieldInfo("iconId", "MenuIcon", True, Texture, "Icon ID of ring in menu."),
        ParamFieldInfo(
            "shopLv",
            "ShopLevel",
            False,
            int,
            "Internal description: 'Level that can be solved in the shop.' Unknown and unused (rings have no "
            "level).",
        ),
        ParamFieldInfo(
            "trophySGradeId",
            "AchievementContributionID",
            False,
            int,
            "Index of ring as it contributes to certain multi-item achievements (none for rings).",
        ),
        ParamFieldInfo(
            "trophySeqId",
            "AchievementUnlockID",
            False,
            int,
            "Achievement unlocked when ring is acquired (Covenant of Artorias).",
        ),
        ParamFieldInfo("equipModelCategory", "EquipmentModelCategory", False, EQUIP_MODEL_CATEGORY, "Always zero."),
        ParamFieldInfo("equipModelGender", "EquipmentModelGender", False, EQUIP_MODEL_GENDER, "Always zero."),
        ParamFieldInfo("accessoryCategory", "AccessoryCategory", False, ACCESSORY_CATEGORY, "Always zero."),
        ParamFieldInfo(
            "refCategory",
            "ReferenceType",
            False,
            BEHAVIOR_REF_TYPE,
            "Always set to Special Effects. No idea what happens if you set it to Attacks for a ring...",
        ),
        ParamFieldInfo(
            "spEffectCategory",
            "SpecialEffectCategory",
            False,
            SP_EFFECT_SPCATEGORY,
            "Determines what type of special effects affect the stats of this equipment. Unused for rings.",
        ),
        ParamFieldInfo("pad[1]", "Pad1", False, pad_field(1), "Null padding."),
        ParamFieldInfo("vagrantItemLotId", "VagrantItemLot", False, ItemLotParam, ""),
        ParamFieldInfo(
            "vagrantBonusEneDropItemLotId", "VagrantBonusEnemyDropItemLot", False, ItemLotParam, ""
        ),
        ParamFieldInfo("vagrantItemEneDropItemLotId", "VagrantItemEnemyDropItemLot", False, ItemLotParam, ""),
        ParamFieldInfo(
            "isDeposit:1",
            "CanBeStored",
            False,
            bool,
            "If True, this ring can be stored in the Bottomless Box. Always True for rings.",
        ),
        ParamFieldInfo(
            "isEquipOutBrake:1",
            "BreaksWhenUnequipped",
            True,
            bool,
            "If True, this ring will break when it is unequipped (e.g. Ring of Favor and Protection).",
        ),
        ParamFieldInfo(
            "disableMultiDropShare:1",
            "DisableMultiplayerShare",
            False,
            bool,
            "If True, this ring cannot be given to other players by dropping it. Always False in vanilla.",
        ),
        ParamFieldInfo("pad1[3]", "Pad2", False, pad_field(3), "Null padding."),
    ],
}
