from __future__ import annotations

__all__ = ["MATERIAL_EX_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class MATERIAL_EX_PARAM_ST(ParamRow):
    ParamName: str = ParamField(
        str, "paramName[32]", encoding="utf-16", length=64, default='',
        tooltip="TOOLTIP-TODO",
    )
    MaterialId: int = ParamField(
        int32, "materialId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamValue0: float = ParamField(
        float32, "materialParamValue0", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamValue1: float = ParamField(
        float32, "materialParamValue1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamValue2: float = ParamField(
        float32, "materialParamValue2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamValue3: float = ParamField(
        float32, "materialParamValue3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaterialParamValue4: float = ParamField(
        float32, "materialParamValue4", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(8, "pad[8]")
