from __future__ import annotations

__all__ = ["BONFIRE_WARP_SUB_CATEGORY_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class BONFIRE_WARP_SUB_CATEGORY_PARAM_ST(ParamRow):
    DisableParamNT: int = ParamField(
        byte, "disableParam_NT:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "disableParamReserve1:7")
    _Pad1: bytes = ParamPad(3, "disableParamReserve2[3]")
    TextId: int = ParamField(
        int, "textId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TabId: int = ParamField(
        ushort, "tabId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SortId: int = ParamField(
        ushort, "sortId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(4, "pad[4]")
