from __future__ import annotations

__all__ = ["EQUIP_PARAM_ACCESSORY_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class EQUIP_PARAM_ACCESSORY_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
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
        float32, "weight", default=1.0,
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
        int32, "qwcId", default=-1,
        tooltip="Unused world tendency remnant.",
    )
    EquipmentModel: int = ParamField(
        uint16, "equipModelId", game_type=EquipmentModel, default=0,
        tooltip="Always zero. (Talismans have no model, presumably.)",
    )
    MenuIcon: int = ParamField(
        uint16, "iconId", game_type=Icon, default=0,
        tooltip="Icon ID of talisman in menu.",
    )
    ShopLevel: int = ParamField(
        int16, "shopLv", default=0,
        tooltip="Internal description: 'Level that can be solved in the shop.' Unknown and unused (talismans have no "
                "level).",
    )
    AchievementContributionID: int = ParamField(
        int16, "trophySGradeId", default=-1,
        tooltip="Index of talisman as it contributes to certain multi-item achievements (none for talismans).",
    )
    AchievementUnlockID: int = ParamField(
        int16, "trophySeqId", default=-1,
        tooltip="Achievement unlocked when talisman is acquired (Covenant of Artorias).",
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
        uint8, "refCategory", BEHAVIOR_REF_TYPE, default=0,
        tooltip="Always set to Special Effects. No idea what happens if you set it to Attacks for a talisman...",
    )
    SpecialEffectCategory: int = ParamField(
        uint8, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="Determines what type of special effects affect the stats of this equipment. Unused for talismans.",
    )
    SortGroupId: int = ParamField(
        uint8, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
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
        uint8, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this talisman can be stored in storage. Always True for talismans.",
    )
    BreaksWhenUnequipped: bool = ParamField(
        uint8, "isEquipOutBrake:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this talisman will break when it is unequipped.",
    )
    DisableMultiplayerShare: bool = ParamField(
        uint8, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="If True, this talisman cannot be given to other players by dropping it. Always False in vanilla.",
    )
    IsDiscard: bool = ParamField(
        uint8, "isDiscard:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDrop: bool = ParamField(
        uint8, "isDrop:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: bool = ParamField(
        uint8, "showLogCondType:1", EQUIP_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        uint8, "showDialogCondType:2", GET_DIALOG_CONDITION_TYPE, bit_count=2, default=2,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        uint8, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad2[2]")
    SaleValue: int = ParamField(
        int32, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccessoryGroup: int = ParamField(
        int16, "accessoryGroup", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad3[1]")
    CompTrophySedId: int = ParamField(
        int8, "compTrophySedId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId1: int = ParamField(
        int32, "residentSpEffectId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId2: int = ParamField(
        int32, "residentSpEffectId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId3: int = ParamField(
        int32, "residentSpEffectId3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSpEffectId4: int = ParamField(
        int32, "residentSpEffectId4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "pad1[4]")
