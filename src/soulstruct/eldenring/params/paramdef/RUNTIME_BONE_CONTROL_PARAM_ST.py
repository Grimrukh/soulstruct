from __future__ import annotations

__all__ = ["RUNTIME_BONE_CONTROL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class RUNTIME_BONE_CONTROL_PARAM_ST(ParamRow):
    ChrId: int = ParamField(
        uint32, "chrId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CtrlType: int = ParamField(
        uint8, "ctrlType", RUNTIME_BONE_CONTROL_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(11, "pad[11]")
    ApplyBone: str = ParamField(
        str, "applyBone[32]", encoding="shift_jis_2004", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
    TargetBone1: str = ParamField(
        str, "targetBone1[32]", encoding="shift_jis_2004", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
    TargetBone2: str = ParamField(
        str, "targetBone2[32]", encoding="shift_jis_2004", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
