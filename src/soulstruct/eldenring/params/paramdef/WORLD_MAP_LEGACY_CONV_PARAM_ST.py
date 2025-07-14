from __future__ import annotations

__all__ = ["WORLD_MAP_LEGACY_CONV_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class WORLD_MAP_LEGACY_CONV_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    SrcAreaNo: int = ParamField(
        uint8, "srcAreaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcGridXNo: int = ParamField(
        uint8, "srcGridXNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcGridZNo: int = ParamField(
        uint8, "srcGridZNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1[1]")
    SrcPosX: float = ParamField(
        float32, "srcPosX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SrcPosY: float = ParamField(
        float32, "srcPosY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SrcPosZ: float = ParamField(
        float32, "srcPosZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DstAreaNo: int = ParamField(
        uint8, "dstAreaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstGridXNo: int = ParamField(
        uint8, "dstGridXNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstGridZNo: int = ParamField(
        uint8, "dstGridZNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad2[1]")
    DstPosX: float = ParamField(
        float32, "dstPosX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DstPosY: float = ParamField(
        float32, "dstPosY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DstPosZ: float = ParamField(
        float32, "dstPosZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IsBasePoint: bool = ParamField(
        uint8, "isBasePoint:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(uint8, "pad3:7", bit_count=7)
    _Pad3: bytes = ParamPad(11, "pad4[11]")
