from __future__ import annotations

__all__ = ["CHR_MODEL_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CHR_MODEL_PARAM_ST(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    ModelMemoryType: int = ParamField(
        byte, "modelMemoryType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TexMemoryType: int = ParamField(
        byte, "texMemoryType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CameraDitherFadeId: int = ParamField(
        short, "cameraDitherFadeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ReportAnimMemSizeMb: float = ParamField(
        float, "reportAnimMemSizeMb", default=12,
        tooltip="TOOLTIP-TODO",
    )
