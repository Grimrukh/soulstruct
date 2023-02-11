from __future__ import annotations

__all__ = ["EQUIP_PARAM_ACCESSORY_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_ACCESSORY_ST(ParamRowData):
    SpecialEffect: SpecialEffectParam = ParamField(
        int, "refId", default=-1,
        tooltip="Special effect applied when ring is equipped.",
    )
    SFXVariation: int = ParamField(
        int, "sfxVariationId", default=-1, hide=True,
        tooltip="SFX variation ID combined with the value specified in TAE animation data. Always -1; likely works "
                "with unused Behavior parameter below.",
    )
    Weight: float = ParamField(
        float, "weight", default=1.0, hide=True,
        tooltip="Weight of ring. Always set to zero in vanilla Dark Souls, but likely works just like other "
                "equipment.",
    )
    Behavior: BehaviorParam = ParamField(
        int, "behaviorId", default=0, hide=True,
        tooltip="Behavior of ring 'skill'. Always zero in the vanilla game.",
    )
    BasicCost: int = ParamField(
        int, "basicPrice", default=0, hide=True,
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
        int, "qwcId", default=-1, hide=True,
        tooltip="Unused world tendency remnant.",
    )
    EquipmentModel: int = ParamField(
        ushort, "equipModelId", default=0, hide=True,
        tooltip="Always zero. (Rings have no model, presumably.)",
    )
    MenuIcon: Texture = ParamField(
        ushort, "iconId", default=0,
        tooltip="Icon ID of ring in menu.",
    )
    ShopLevel: int = ParamField(
        short, "shopLv", default=0, hide=True,
        tooltip="Internal description: 'Level that can be solved in the shop.' Unknown and unused (rings have no "
                "level).",
    )
    AchievementContributionID: int = ParamField(
        short, "trophySGradeId", default=-1, hide=True,
        tooltip="Index of ring as it contributes to certain multi-item achievements (none for rings).",
    )
    AchievementUnlockID: int = ParamField(
        short, "trophySeqId", default=-1, hide=True,
        tooltip="Achievement unlocked when ring is acquired (Covenant of Artorias).",
    )
    EquipmentModelCategory: EQUIP_MODEL_CATEGORY = ParamField(
        byte, "equipModelCategory", default=0, hide=True,
        tooltip="Always zero.",
    )
    EquipmentModelGender: EQUIP_MODEL_GENDER = ParamField(
        byte, "equipModelGender", default=0, hide=True,
        tooltip="Always zero.",
    )
    AccessoryCategory: ACCESSORY_CATEGORY = ParamField(
        byte, "accessoryCategory", default=0, hide=True,
        tooltip="Always zero.",
    )
    ReferenceType: BEHAVIOR_REF_TYPE = ParamField(
        byte, "refCategory", default=0, hide=True,
        tooltip="Always set to Special Effects. No idea what happens if you set it to Attacks for a ring...",
    )
    SpecialEffectCategory: SP_EFFECT_SPCATEGORY = ParamField(
        byte, "spEffectCategory", default=0, hide=True,
        tooltip="Determines what type of special effects affect the stats of this equipment. Unused for rings.",
    )
    _Pad0: bytes = ParamPad(1, "pad[1]")
    VagrantItemLot: ItemLotParam = ParamField(
        int, "vagrantItemLotId", default=0, hide=True,
        tooltip="TODO",
    )
    VagrantBonusEnemyDropItemLot: ItemLotParam = ParamField(
        int, "vagrantBonusEneDropItemLotId", default=0, hide=True,
        tooltip="TODO",
    )
    VagrantItemEnemyDropItemLot: ItemLotParam = ParamField(
        int, "vagrantItemEneDropItemLotId", default=0, hide=True,
        tooltip="TODO",
    )
    CanBeStored: bool = ParamField(
        byte, "isDeposit:1", bit_count=1, default=True, hide=True,
        tooltip="If True, this ring can be stored in the Bottomless Box. Always True for rings.",
    )
    BreaksWhenUnequipped: bool = ParamField(
        byte, "isEquipOutBrake:1", bit_count=1, default=False,
        tooltip="If True, this ring will break when it is unequipped (e.g. Ring of Favor and Protection).",
    )
    DisableMultiplayerShare: bool = ParamField(
        byte, "disableMultiDropShare:1", bit_count=1, default=False, hide=True,
        tooltip="If True, this ring cannot be given to other players by dropping it. Always False in vanilla.",
    )
    _Pad1: bytes = ParamPad(3, "pad1[3]")
