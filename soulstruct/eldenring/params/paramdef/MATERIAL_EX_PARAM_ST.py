from __future__ import annotations

__all__ = ["MATERIAL_EX_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class MATERIAL_EX_PARAM_ST(ParamRow):
    ParamName: bytes = ParamField(
        bytes, "paramName[32]", length=64, default='',
        tooltip="TOOLTIP-TODO",
    )
    MaterialId: int = ParamField(
        int, "materialId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamValue0: float = ParamField(
        float, "materialParamValue0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamValue1: float = ParamField(
        float, "materialParamValue1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamValue2: float = ParamField(
        float, "materialParamValue2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamValue3: float = ParamField(
        float, "materialParamValue3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamValue4: float = ParamField(
        float, "materialParamValue4", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad[8]")
