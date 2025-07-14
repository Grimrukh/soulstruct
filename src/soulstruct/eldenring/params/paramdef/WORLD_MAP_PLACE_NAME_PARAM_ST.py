from __future__ import annotations

__all__ = ["WORLD_MAP_PLACE_NAME_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WORLD_MAP_PLACE_NAME_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    WorldMapPieceId: int = ParamField(
        int32, "worldMapPieceId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TextId: int = ParamField(
        int32, "textId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "pad1[4]")
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
    _Pad2: bytes = ParamPad(1, "pad2[1]")
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
