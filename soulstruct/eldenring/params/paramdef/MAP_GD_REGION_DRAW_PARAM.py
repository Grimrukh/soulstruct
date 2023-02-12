from __future__ import annotations

__all__ = ["MAP_GD_REGION_DRAW_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MAP_GD_REGION_DRAW_PARAM(ParamRowData):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    OverrideIVLocalLightScale: float = ParamField(
        float, "overrideIVLocalLightScale", default=-1,
        tooltip="TOOLTIP-TODO",
    )
