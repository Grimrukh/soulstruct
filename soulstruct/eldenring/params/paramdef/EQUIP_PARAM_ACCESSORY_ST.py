from __future__ import annotations

__all__ = ["EQUIP_PARAM_ACCESSORY_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_PARAM_ACCESSORY_ST(ParamRow):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    SpecialEffect: int = ParamField(
        int, "refId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SFXVariation: int = ParamField(
        int, "sfxVariationId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Weight: float = ParamField(
        float, "weight", default=1,
        tooltip="TOOLTIP-TODO",
    )
    Behavior: int = ParamField(
        int, "behaviorId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BasicCost: int = ParamField(
        int, "basicPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FramptSellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortIndex: int = ParamField(
        int, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    QWCID: int = ParamField(
        int, "qwcId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipmentModel: int = ParamField(
        ushort, "equipModelId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MenuIcon: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShopLevel: int = ParamField(
        short, "shopLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AchievementContributionID: int = ParamField(
        short, "trophySGradeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AchievementUnlockID: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipmentModelCategory: int = ParamField(
        byte, "equipModelCategory", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquipmentModelGender: int = ParamField(
        byte, "equipModelGender", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AccessoryCategory: int = ParamField(
        byte, "accessoryCategory", default=0,
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
    SortGroupId: int = ParamField(
        byte, "sortGroupId", default=255,
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
    CanBeStored: int = ParamField(
        byte, "isDeposit:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreaksWhenUnequipped: int = ParamField(
        byte, "isEquipOutBrake:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiplayerShare: int = ParamField(
        byte, "disableMultiDropShare:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDiscard: int = ParamField(
        byte, "isDiscard:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDrop: int = ParamField(
        byte, "isDrop:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShowLogCondType: int = ParamField(
        byte, "showLogCondType:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ShowDialogCondType: int = ParamField(
        byte, "showDialogCondType:2", default=2,
        tooltip="TOOLTIP-TODO",
    )
    Rarity: int = ParamField(
        byte, "rarity", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "pad2[2]")
    SaleValue: int = ParamField(
        int, "saleValue", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AccessoryGroup: int = ParamField(
        short, "accessoryGroup", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad3[1]")
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
    _Pad4: bytes = ParamPad(4, "pad1[4]")
