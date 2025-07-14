from __future__ import annotations

__all__ = ["MAP_NAME_TEX_PARAM_ST_DLC02"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class MAP_NAME_TEX_PARAM_ST_DLC02(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SrcR: int = ParamField(
        byte, "srcR", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcG: int = ParamField(
        byte, "srcG", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcB: int = ParamField(
        byte, "srcB", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    MapNameId: int = ParamField(
        int, "mapNameId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xc: int = ParamField(
        int, "unknown_0xc", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x10: int = ParamField(
        byte, "unknown_0x10", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x11: int = ParamField(
        byte, "unknown_0x11", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x12: int = ParamField(
        byte, "unknown_0x12", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x13: int = ParamField(
        byte, "unknown_0x13", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x14: int = ParamField(
        int, "unknown_0x14", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnknownTextID1: int = ParamField(
        int, "unknownTextID_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnknownTextID2: int = ParamField(
        int, "unknownTextID_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x20: int = ParamField(
        int, "unknown_0x20", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x24: int = ParamField(
        int, "unknown_0x24", default=0,
        tooltip="TOOLTIP-TODO",
    )
