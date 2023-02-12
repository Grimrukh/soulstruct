from __future__ import annotations

__all__ = ["WORLD_MAP_LEGACY_CONV_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class WORLD_MAP_LEGACY_CONV_PARAM_ST(ParamRow):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    SrcAreaNo: int = ParamField(
        byte, "srcAreaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcGridXNo: int = ParamField(
        byte, "srcGridXNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SrcGridZNo: int = ParamField(
        byte, "srcGridZNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(1, "pad1[1]")
    SrcPosX: float = ParamField(
        float, "srcPosX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SrcPosY: float = ParamField(
        float, "srcPosY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SrcPosZ: float = ParamField(
        float, "srcPosZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DstAreaNo: int = ParamField(
        byte, "dstAreaNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstGridXNo: int = ParamField(
        byte, "dstGridXNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DstGridZNo: int = ParamField(
        byte, "dstGridZNo", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad2[1]")
    DstPosX: float = ParamField(
        float, "dstPosX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DstPosY: float = ParamField(
        float, "dstPosY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DstPosZ: float = ParamField(
        float, "dstPosZ", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    IsBasePoint: int = ParamField(
        byte, "isBasePoint:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(1, "pad3:7")
    _Pad5: bytes = ParamPad(11, "pad4[11]")
