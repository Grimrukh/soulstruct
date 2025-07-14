from __future__ import annotations

__all__ = ["EQUIP_PARAM_ACCESSORY_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_ACCESSORY_ST(ParamRow):
    SpecialEffect: int = ParamField(
        int32, "refId", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied when accessory is equipped.",
    )
    SFXVariation: int = ParamField(
        int32, "sfxVariationId", default=-1,
        tooltip="SFX variation ID combined with the value specified in TAE animation data. Always -1; likely works "
                "with unused Behavior parameter below.",
    )
    Weight: float = ParamField(
        float32, "weight", default=0.0,
        tooltip="Weight of accessory. Always set to zero in vanilla Dark Souls, but likely works just like other "
                "equipment.",
    )
    Behavior: int = ParamField(
        int32, "behaviorId", game_type=BehaviorParam, default=0,
        tooltip="Behavior of accessory 'skill'. Always zero in the vanilla game.",
    )
    BasicCost: int = ParamField(
        int32, "basicPrice", default=0,
        tooltip="Unknown purpose, and unused.",
    )
    FramptSellValue: int = ParamField(
        int32, "sellValue", default=0,
        tooltip="Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
    )
    SortIndex: int = ParamField(
        int32, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    QWCID: int = ParamField(
        int32, "qwcId", default=0,
        tooltip="Unused world tendency remnant.",
    )
    EquipmentModel: int = ParamField(
        uint16, "equipModelId", game_type=EquipmentModel, default=0,
        tooltip="Always zero. (Rings have no model, presumably.)",
    )
    MenuIcon: int = ParamField(
        uint16, "iconId", game_type=Icon, default=0,
        tooltip="Icon ID of ring in menu.",
    )
    ShopLevel: int = ParamField(
        int16, "shopLv", default=-1,
        tooltip="Internal description: 'Level that can be solved in the shop.' Unknown and unused (rings have no "
                "level).",
    )
    AchievementContributionID: int = ParamField(
        int16, "trophySGradeId", default=-1,
        tooltip="Index of ring as it contributes to certain multi-item achievements (none for rings).",
    )
    AchievementUnlockID: int = ParamField(
        int16, "trophySeqId", default=-1,
        tooltip="Achievement unlocked when ring is acquired (Covenant of Artorias).",
    )
    EquipmentModelCategory: int = ParamField(
        uint8, "equipModelCategory", EQUIP_MODEL_CATEGORY, default=0,
        tooltip="Always zero.",
    )
    EquipmentModelGender: int = ParamField(
        uint8, "equipModelGender", EQUIP_MODEL_GENDER, default=0,
        tooltip="Always zero.",
    )
    AccessoryCategory: int = ParamField(
        uint8, "accessoryCategory", ACCESSORY_CATEGORY, default=0,
        tooltip="Always zero.",
    )
    ReferenceType: int = ParamField(
        uint8, "refCategory", BEHAVIOR_REF_TYPE, default=2,
        tooltip="Always set to Special Effects. No idea what happens if you set it to Attacks for a ring...",
    )
    SpecialEffectCategory: int = ParamField(
        uint8, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="Determines what type of special effects affect the stats of this equipment. Unused for rings.",
    )
    _Pad0: bytes = ParamPad(1, "pad[1]")
    VagrantItemLot: int = ParamField(
        int32, "vagrantItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
    )
    VagrantBonusEnemyDropItemLot: int = ParamField(
        int32, "vagrantBonusEneDropItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
    )
    VagrantItemEnemyDropItemLot: int = ParamField(
        int32, "vagrantItemEneDropItemLotId", game_type=ItemLotParam, default=0,
        tooltip="TODO",
    )
    CanBeStored: bool = ParamField(
        uint8, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="If True, this ring can be stored in the Bottomless Box. Always True for rings.",
    )
    BreaksWhenUnequipped: bool = ParamField(
        uint8, "isEquipOutBrake:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this ring will break when it is unequipped (e.g. Ring of Favor and Protection).",
    )
    DisableMultiplayerShare: bool = ParamField(
        uint8, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this ring cannot be given to other players by dropping it. Always False in vanilla.",
    )
    _Pad1: bytes = ParamPad(3, "pad1[3]")
