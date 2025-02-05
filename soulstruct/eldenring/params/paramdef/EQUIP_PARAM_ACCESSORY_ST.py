from __future__ import annotations

__all__ = ["EQUIP_PARAM_ACCESSORY_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_ACCESSORY_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SpecialEffect: int = ParamField(
        int, "refId", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied when accessory is equipped.",
    )
    SFXVariation: int = ParamField(
        int, "sfxVariationId", default=-1,
        tooltip="SFX variation ID combined with the value specified in TAE animation data. Always -1; likely works "
                "with unused Behavior parameter below.",
    )
    Weight: float = ParamField(
        float, "weight", default=1.0,
        tooltip="Weight of accessory. Always set to zero in vanilla Dark Souls, but likely works just like other "
                "equipment.",
    )
    Behavior: int = ParamField(
        int, "behaviorId", game_type=BehaviorParam, default=0,
        tooltip="Behavior of accessory 'skill'. Always zero in the vanilla game.",
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
        tooltip="Always zero. (Talismans have no model, presumably.)",
    )
    MenuIcon: int = ParamField(
        ushort, "iconId", game_type=Icon, default=0,
        tooltip="Icon ID of talisman in menu.",
    )
    ShopLevel: int = ParamField(
        short, "shopLv", default=0,
        tooltip="Internal description: 'Level that can be solved in the shop.' Unknown and unused (talismans have no "
                "level).",
    )
    AchievementContributionID: int = ParamField(
        short, "trophySGradeId", default=-1,
        tooltip="Index of talisman as it contributes to certain multi-item achievements (none for talismans).",
    )
    AchievementUnlockID: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="Achievement unlocked when talisman is acquired (Covenant of Artorias).",
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
        tooltip="Always set to Special Effects. No idea what happens if you set it to Attacks for a talisman...",
    )
    SpecialEffectCategory: int = ParamField(
        byte, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="Determines what type of special effects affect the stats of this equipment. Unused for talismans.",
    )
    SortGroupId: int = ParamField(
        byte, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
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
    CanBeStored: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this talisman can be stored in storage. Always True for talismans.",
    )
    BreaksWhenUnequipped: bool = ParamField(
        byte, "isEquipOutBrake:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this talisman will break when it is unequipped.",
    )
    DisableMultiplayerShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this talisman cannot be given to other players by dropping it. Always False in vanilla.",
    )
    IsDiscard: bool = ParamField(
        byte, "isDiscard:1", EQUIP_BOOL, bit_count=1, default=False,
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
    ShowDialogCondType: int = ParamField(
        byte, "showDialogCondType:2", GET_DIALOG_CONDITION_TYPE, bit_count=2, default=2,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        byte, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad2[2]")
    SaleValue: int = ParamField(
        int, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccessoryGroup: int = ParamField(
        short, "accessoryGroup", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad3[1]")
    CompTrophySedId: int = ParamField(
        sbyte, "compTrophySedId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId1: int = ParamField(
        int, "residentSpEffectId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId2: int = ParamField(
        int, "residentSpEffectId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId3: int = ParamField(
        int, "residentSpEffectId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId4: int = ParamField(
        int, "residentSpEffectId4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "pad1[4]")
