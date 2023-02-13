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
    MaterialId01: int = ParamField(
        int, "materialId01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialId02: int = ParamField(
        int, "materialId02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialId03: int = ParamField(
        int, "materialId03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialId04: int = ParamField(
        int, "materialId04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialId05: int = ParamField(
        int, "materialId05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialId06: int = ParamField(
        int, "materialId06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad_id[8]")
    ItemNum01: int = ParamField(
        sbyte, "itemNum01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum02: int = ParamField(
        sbyte, "itemNum02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum03: int = ParamField(
        sbyte, "itemNum03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum04: int = ParamField(
        sbyte, "itemNum04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum05: int = ParamField(
        sbyte, "itemNum05", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ItemNum06: int = ParamField(
        sbyte, "itemNum06", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad_num[2]")
    MaterialCate01: int = ParamField(
        byte, "materialCate01", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate02: int = ParamField(
        byte, "materialCate02", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate03: int = ParamField(
        byte, "materialCate03", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate04: int = ParamField(
        byte, "materialCate04", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate05: int = ParamField(
        byte, "materialCate05", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    MaterialCate06: int = ParamField(
        byte, "materialCate06", GAITEM_CATEGORY, default=4,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "pad_cate[2]")
    IsDisableDispNum01: bool = ParamField(
        byte, "isDisableDispNum01:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableDispNum02: bool = ParamField(
        byte, "isDisableDispNum02:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableDispNum03: bool = ParamField(
        byte, "isDisableDispNum03:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableDispNum04: bool = ParamField(
        byte, "isDisableDispNum04:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableDispNum05: bool = ParamField(
        byte, "isDisableDispNum05:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableDispNum06: bool = ParamField(
        byte, "isDisableDispNum06:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(3, "pad[3]")
