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
        byte, "ctrlType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(11, "pad[11]")
    ApplyBone: bytes = ParamField(
        bytes, "applyBone[32]", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
    TargetBone1: bytes = ParamField(
        bytes, "targetBone1[32]", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
    TargetBone2: bytes = ParamField(
        bytes, "targetBone2[32]", length=32, default='',
        tooltip="TOOLTIP-TODO",
    )
