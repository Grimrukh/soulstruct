from __future__ import annotations

__all__ = ["CHR_MODEL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CHR_MODEL_PARAM_ST(ParamRow):
    DisableParamNT: bool = ParamField(
        byte, "disableParam_NT:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "disableParamReserve1:7", bit_count=7)
    _Pad0: bytes = ParamPad(3, "disableParamReserve2[3]")
    ModelMemoryType: int = ParamField(
        byte, "modelMemoryType", CHR_MEMORY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    TexMemoryType: int = ParamField(
        byte, "texMemoryType", CHR_MEMORY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CameraDitherFadeId: int = ParamField(
        short, "cameraDitherFadeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReportAnimMemSizeMb: float = ParamField(
        float, "reportAnimMemSizeMb", default=12.0,
        tooltip="TOOLTIP-TODO",
    )
    Unk: int = ParamField(
        uint, "unk", default=0,
        tooltip="TOOLTIP-TODO",
    )
