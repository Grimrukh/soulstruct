from __future__ import annotations

__all__ = ["MENU_PARAM_COLOR_TABLE_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MENU_PARAM_COLOR_TABLE_ST(ParamRowData):
    LerpMode: int = ParamField(
        byte, "lerpMode", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad1[3]")
    H: int = ParamField(
        ushort, "h", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad2[2]")
    S1: float = ParamField(
        float, "s1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    V1: float = ParamField(
        float, "v1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    S2: float = ParamField(
        float, "s2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    V2: float = ParamField(
        float, "v2", default=1,
        tooltip="TOOLTIP-TODO",
    )
    S3: float = ParamField(
        float, "s3", default=1,
        tooltip="TOOLTIP-TODO",
    )
    V3: float = ParamField(
        float, "v3", default=1,
        tooltip="TOOLTIP-TODO",
    )
