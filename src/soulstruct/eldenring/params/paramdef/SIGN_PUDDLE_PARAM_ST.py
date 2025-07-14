from __future__ import annotations

__all__ = ["SIGN_PUDDLE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SIGN_PUDDLE_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    MatchAreaId: int = ParamField(
        int32, "matchAreaId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(24, "pad1[24]")
    Unknown0x20: int = ParamField(
        int32, "unknown_0x20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x24: int = ParamField(
        int32, "unknown_0x24", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AreaNo: int = ParamField(
        uint8, "areaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridXNo: int = ParamField(
        uint8, "gridXNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GridZNo: int = ParamField(
        uint8, "gridZNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad3[1]")
    PosX: float = ParamField(
        float32, "posX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosY: float = ParamField(
        float32, "posY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PosZ: float = ParamField(
        float32, "posZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SignSubCategoryId: int = ParamField(
        int32, "signSubCategoryId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LocationTextId: int = ParamField(
        int32, "locationTextId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortId: int = ParamField(
        int32, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(4, "endPad[4]")
