from __future__ import annotations

__all__ = ["CHR_MODEL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CHR_MODEL_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        uint8, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    ModelMemoryType: int = ParamField(
        uint8, "modelMemoryType", CHR_MEMORY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TexMemoryType: int = ParamField(
        uint8, "texMemoryType", CHR_MEMORY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CameraDitherFadeId: int = ParamField(
        int16, "cameraDitherFadeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReportAnimMemSizeMb: float = ParamField(
        float32, "reportAnimMemSizeMb", default=12.0,
        tooltip="TOOLTIP-TODO",
    )
    Unk: int = ParamField(
        uint32, "unk", default=0,
        tooltip="TOOLTIP-TODO",
    )
