from __future__ import annotations

__all__ = ["ROLLING_OBJ_LOT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ROLLING_OBJ_LOT_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    AssetId0: int = ParamField(
        int, "AssetId_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId1: int = ParamField(
        int, "AssetId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId2: int = ParamField(
        int, "AssetId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId3: int = ParamField(
        int, "AssetId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId4: int = ParamField(
        int, "AssetId_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId5: int = ParamField(
        int, "AssetId_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId6: int = ParamField(
        int, "AssetId_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AssetId7: int = ParamField(
        int, "AssetId_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight0: int = ParamField(
        byte, "CreateWeight_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight1: int = ParamField(
        byte, "CreateWeight_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight2: int = ParamField(
        byte, "CreateWeight_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight3: int = ParamField(
        byte, "CreateWeight_3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight4: int = ParamField(
        byte, "CreateWeight_4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight5: int = ParamField(
        byte, "CreateWeight_5", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight6: int = ParamField(
        byte, "CreateWeight_6", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CreateWeight7: int = ParamField(
        byte, "CreateWeight_7", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(20, "Reserve_0[20]")
