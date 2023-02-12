from __future__ import annotations

__all__ = ["EQUIP_MTRL_SET_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class EQUIP_MTRL_SET_PARAM_ST(ParamRow):
    UpgradeGood: int = ParamField(
        int, "materialId01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeGood2: int = ParamField(
        int, "materialId02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeGood3: int = ParamField(
        int, "materialId03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeGood4: int = ParamField(
        int, "materialId04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeGood5: int = ParamField(
        int, "materialId05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialId06: int = ParamField(
        int, "materialId06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad_id[8]")
    UpgradeQuantity: int = ParamField(
        sbyte, "itemNum01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeQuantity2: int = ParamField(
        sbyte, "itemNum02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeQuantity3: int = ParamField(
        sbyte, "itemNum03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeQuantity4: int = ParamField(
        sbyte, "itemNum04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UpgradeQuantity5: int = ParamField(
        sbyte, "itemNum05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum06: int = ParamField(
        sbyte, "itemNum06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad_num[2]")
    MaterialCate01: int = ParamField(
        byte, "materialCate01", default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate02: int = ParamField(
        byte, "materialCate02", default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate03: int = ParamField(
        byte, "materialCate03", default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate04: int = ParamField(
        byte, "materialCate04", default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate05: int = ParamField(
        byte, "materialCate05", default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate06: int = ParamField(
        byte, "materialCate06", default=4,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "pad_cate[2]")
    DisableQuantityIndicator: int = ParamField(
        byte, "isDisableDispNum01:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableQuantityIndicator2: int = ParamField(
        byte, "isDisableDispNum02:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableQuantityIndicator3: int = ParamField(
        byte, "isDisableDispNum03:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableQuantityIndicator4: int = ParamField(
        byte, "isDisableDispNum04:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableQuantityIndicator5: int = ParamField(
        byte, "isDisableDispNum05:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableDispNum06: int = ParamField(
        byte, "isDisableDispNum06:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(3, "pad[3]")
