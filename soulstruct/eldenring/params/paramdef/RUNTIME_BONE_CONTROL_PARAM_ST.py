from __future__ import annotations

__all__ = ["RUNTIME_BONE_CONTROL_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class RUNTIME_BONE_CONTROL_PARAM_ST(ParamRow):
    ChrId: int = ParamField(
        uint, "chrId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CtrlType: int = ParamField(
        byte, "ctrlType", RUNTIME_BONE_CONTROL_TYPE, default=0,
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
