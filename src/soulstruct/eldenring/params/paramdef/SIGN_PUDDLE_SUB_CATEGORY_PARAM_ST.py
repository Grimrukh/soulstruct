from __future__ import annotations

__all__ = ["SIGN_PUDDLE_SUB_CATEGORY_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class SIGN_PUDDLE_SUB_CATEGORY_PARAM_ST(ParamRow):
    _Pad0: bytes = ParamPad(4, "startPad[4]")
    SignPuddleCategoryText: int = ParamField(
        int32, "signPuddleCategoryText", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SignPuddleTabId: int = ParamField(
        uint16, "signPuddleTabId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xa: int = ParamField(
        uint16, "unknown_0xa", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(4, "endPad[4]")
