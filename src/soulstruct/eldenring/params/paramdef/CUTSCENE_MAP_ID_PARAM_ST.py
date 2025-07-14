from __future__ import annotations

__all__ = ["CUTSCENE_MAP_ID_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CUTSCENE_MAP_ID_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableParamDebug: bool = ParamField(
        uint8, "disableParam_Debug:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:6", bit_count=6)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    PlayMapId: int = ParamField(
        uint32, "PlayMapId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequireMapId0: int = ParamField(
        uint32, "RequireMapId0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequireMapId1: int = ParamField(
        uint32, "RequireMapId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequireMapId2: int = ParamField(
        uint32, "RequireMapId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCamPosHitPartsID: int = ParamField(
        int32, "RefCamPosHitPartsID", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(12, "reserved_2_old[12]")
    Unknown0x18: int = ParamField(
        int32, "unknown_0x18", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(8, "reserved_2[8]")
    ClientDisableViewTimeForProgress: int = ParamField(
        uint16, "ClientDisableViewTimeForProgress", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(2, "reserved[2]")
    HitParts0: int = ParamField(
        int32, "HitParts_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitParts1: int = ParamField(
        int32, "HitParts_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
