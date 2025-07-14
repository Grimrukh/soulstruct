from __future__ import annotations

__all__ = ["MAP_PIECE_TEX_PARAM_ST_DLC02"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MAP_PIECE_TEX_PARAM_ST_DLC02(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SrcR: int = ParamField(
        uint8, "srcR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcG: int = ParamField(
        uint8, "srcG", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcB: int = ParamField(
        uint8, "srcB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    SaveMapNameId: int = ParamField(
        int32, "saveMapNameId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MultiPlayAreaId: int = ParamField(
        int32, "multiPlayAreaId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x10: int = ParamField(
        int32, "unknown_0x10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x14: int = ParamField(
        int32, "unknown_0x14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x18: int = ParamField(
        int32, "unknown_0x18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x1c: int = ParamField(
        int32, "unknown_0x1c", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnknownPlayRegion1: int = ParamField(
        int32, "unknownPlayRegion_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnknownPlayRegion2: int = ParamField(
        int32, "unknownPlayRegion_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
