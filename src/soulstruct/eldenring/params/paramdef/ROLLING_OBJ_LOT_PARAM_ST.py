from __future__ import annotations

__all__ = ["ROLLING_OBJ_LOT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class ROLLING_OBJ_LOT_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    AssetId0: int = ParamField(
        int32, "AssetId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId1: int = ParamField(
        int32, "AssetId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId2: int = ParamField(
        int32, "AssetId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId3: int = ParamField(
        int32, "AssetId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId4: int = ParamField(
        int32, "AssetId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId5: int = ParamField(
        int32, "AssetId_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId6: int = ParamField(
        int32, "AssetId_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId7: int = ParamField(
        int32, "AssetId_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight0: int = ParamField(
        uint8, "CreateWeight_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight1: int = ParamField(
        uint8, "CreateWeight_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight2: int = ParamField(
        uint8, "CreateWeight_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight3: int = ParamField(
        uint8, "CreateWeight_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight4: int = ParamField(
        uint8, "CreateWeight_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight5: int = ParamField(
        uint8, "CreateWeight_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight6: int = ParamField(
        uint8, "CreateWeight_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight7: int = ParamField(
        uint8, "CreateWeight_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(20, "Reserve_0[20]")
