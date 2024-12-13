from __future__ import annotations

__all__ = ["CUTSCENE_MAP_ID_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CUTSCENE_MAP_ID_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableParamDebug: bool = ParamField(
        byte, "disableParam_Debug:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:6", bit_count=6)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    PlayMapId: int = ParamField(
        uint, "PlayMapId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequireMapId0: int = ParamField(
        uint, "RequireMapId0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequireMapId1: int = ParamField(
        uint, "RequireMapId1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RequireMapId2: int = ParamField(
        uint, "RequireMapId2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RefCamPosHitPartsID: int = ParamField(
        int, "RefCamPosHitPartsID", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(12, "reserved_2[12]")
    ClientDisableViewTimeForProgress: int = ParamField(
        ushort, "ClientDisableViewTimeForProgress", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(2, "reserved[2]")
    HitParts0: int = ParamField(
        int, "HitParts_0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitParts1: int = ParamField(
        int, "HitParts_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
