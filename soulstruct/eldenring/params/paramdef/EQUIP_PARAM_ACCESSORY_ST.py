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
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    RefId: int = ParamField(
        int, "refId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SfxVariationId: int = ParamField(
        int, "sfxVariationId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Weight: float = ParamField(
        float, "weight", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorId: int = ParamField(
        int, "behaviorId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BasicPrice: int = ParamField(
        int, "basicPrice", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SellValue: int = ParamField(
        int, "sellValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortId: int = ParamField(
        int, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    QwcId: int = ParamField(
        int, "qwcId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipModelId: int = ParamField(
        ushort, "equipModelId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        ushort, "iconId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShopLv: int = ParamField(
        short, "shopLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TrophySGradeId: int = ParamField(
        short, "trophySGradeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TrophySeqId: int = ParamField(
        short, "trophySeqId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EquipModelCategory: int = ParamField(
        byte, "equipModelCategory", EQUIP_MODEL_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    EquipModelGender: int = ParamField(
        byte, "equipModelGender", EQUIP_MODEL_GENDER, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AccessoryCategory: int = ParamField(
        byte, "accessoryCategory", ACCESSORY_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCategory: int = ParamField(
        byte, "refCategory", BEHAVIOR_REF_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectCategory: int = ParamField(
        byte, "spEffectCategory", BEHAVIOR_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortGroupId: int = ParamField(
        byte, "sortGroupId", default=255,
        tooltip="TOOLTIP-TODO",
    )
    VagrantItemLotId: int = ParamField(
        int, "vagrantItemLotId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VagrantBonusEneDropItemLotId: int = ParamField(
        int, "vagrantBonusEneDropItemLotId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VagrantItemEneDropItemLotId: int = ParamField(
        int, "vagrantItemEneDropItemLotId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDeposit: bool = ParamField(
        byte, "isDeposit:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEquipOutBrake: bool = ParamField(
        byte, "isEquipOutBrake:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableMultiDropShare: bool = ParamField(
        byte, "disableMultiDropShare:1", EQUIP_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
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
