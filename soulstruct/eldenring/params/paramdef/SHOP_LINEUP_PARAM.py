from __future__ import annotations

__all__ = ["SHOP_LINEUP_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class SHOP_LINEUP_PARAM(ParamRow):
    EquipId: int = ParamField(
        int, "equipId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Value: int = ParamField(
        int, "value", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MtrlId: int = ParamField(
        int, "mtrlId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    EventFlagforStock: int = ParamField(
        uint, "eventFlag_forStock", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EventFlagforRelease: int = ParamField(
        uint, "eventFlag_forRelease", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SellQuantity: int = ParamField(
        short, "sellQuantity", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad3[1]")
    EquipType: int = ParamField(
        byte, "equipType", SHOP_LINEUP_EQUIPTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CostType: int = ParamField(
        byte, "costType", SHOP_LINEUP_COSTTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    SetNum: int = ParamField(
        ushort, "setNum", default=1,
        tooltip="TOOLTIP-TODO",
    )
    ValueAdd: int = ParamField(
        int, "value_Add", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ValueMagnification: float = ParamField(
        float, "value_Magnification", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    IconId: int = ParamField(
        int, "iconId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NameMsgId: int = ParamField(
        int, "nameMsgId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MenuTitleMsgId: int = ParamField(
        int, "menuTitleMsgId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MenuIconId: int = ParamField(
        short, "menuIconId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "pad2[2]")
