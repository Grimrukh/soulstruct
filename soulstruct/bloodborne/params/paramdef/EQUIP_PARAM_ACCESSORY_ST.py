from __future__ import annotations

__all__ = ["EQUIP_PARAM_ACCESSORY_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_ACCESSORY_ST(ParamRow):
    SpecialEffect: int = ParamField(
        int, "refId", default=-1,
        tooltip="Special effect applied when ring is equipped.",
    )
    SFXVariation: int = ParamField(
        int, "sfxVariationId", default=-1,
        tooltip="SFX variation ID combined with the value specified in TAE animation data. Always -1; likely works "
                "with unused Behavior parameter below.",
    )
    Weight: float = ParamField(
        float, "weight", default=1.0,
        tooltip="Weight of ring. Always set to zero in vanilla Dark Souls, but likely works just like other "
                "equipment.",
    )
    Behavior: int = ParamField(
        int, "behaviorId", game_type=BehaviorParam, default=0,
        tooltip="Behavior of ring 'skill'. Always zero in the vanilla game.",
    )
    BasicCost: int = ParamField(
        int, "basicPrice", default=0,
        tooltip="Unknown purpose, and unused.",
    )
    FramptSellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold.",
    )
    SortIndex: int = ParamField(
        int, "sortId", default=0,
        tooltip="Index for automatic inventory sorting.",
    )
    QWCID: int = ParamField(
        int, "qwcId", default=-1,
        tooltip="Unused world tendency remnant.",
    )
    EquipmentModel: int = ParamField(
        ushort, "equipModelId", game_type=EquipmentModel, default=0,
        tooltip="Always zero. (Rings have no model, presumably.)",
    )
    MenuIcon: int = ParamField(
        ushort, "iconId", game_type=Icon, default=0,
        tooltip="Icon ID of ring in menu.",
    )
    ShopLevel: int = ParamField(
        short, "shopLv", default=0,
        tooltip="Internal description: 'Level that can be solved in the shop.' Unknown and unused (rings have no "
                "level).",
    )
    AchievementContributionID: int = ParamField(
        short, "trophySGradeId", default=-1,
        tooltip="Index of ring as it contributes to certain multi-item achievements (none for rings).",
    )
    AchievementUnlockID: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="Achievement unlocked when ring is acquired (Covenant of Artorias).",
    )
    EquipmentModelCategory: int = ParamField(
        byte, "equipModelCategory", EQUIP_MODEL_CATEGORY, default=0,
        tooltip="Always zero.",
    )
    EquipmentModelGender: int = ParamField(
        byte, "equipModelGender", EQUIP_MODEL_GENDER, default=0,
        tooltip="Always zero.",
    )
    AccessoryCategory: int = ParamField(
        byte, "accessoryCategory", ACCESSORY_CATEGORY, default=0,
        tooltip="Always zero.",
    )
    ReferenceType: int = ParamField(
        byte, "refCategory", BEHAVIOR_REF_TYPE, default=0,
        tooltip="Always set to Special Effects. No idea what happens if you set it to Attacks for a ring...",
    )
    SpecialEffectCategory: int = ParamField(
        byte, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="Determines what type of special effects affect the stats of this equipment. Unused for rings.",
    )
    _Pad0: bytes = ParamPad(1, "pad[1]")
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
    CanBeStored: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="If True, this ring can be stored in the Bottomless Box. Always True for rings.",
    )
    BreaksWhenUnequipped: bool = ParamField(
        byte, "isEquipOutBrake:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this ring will break when it is unequipped (e.g. Ring of Favor and Protection).",
    )
    DisableMultiplayerShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this ring cannot be given to other players by dropping it. Always False in vanilla.",
    )
    _Pad1: bytes = ParamPad(3, "pad1[3]")
