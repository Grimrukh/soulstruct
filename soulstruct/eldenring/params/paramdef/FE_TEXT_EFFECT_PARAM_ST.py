from __future__ import annotations

__all__ = ["FE_TEXT_EFFECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class FE_TEXT_EFFECT_PARAM_ST(ParamRowData):
    ResId: int = ParamField(
        short, "resId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad1[2]")
    TextId: int = ParamField(
        int, "textId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SeId: int = ParamField(
        int, "seId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    CanMixMapName: int = ParamField(
        byte, "canMixMapName:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad3:7")
    _Pad2: bytes = ParamPad(19, "pad2[19]")
