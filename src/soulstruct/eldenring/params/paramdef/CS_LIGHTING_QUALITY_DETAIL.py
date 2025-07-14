from __future__ import annotations

__all__ = ["CS_LIGHTING_QUALITY_DETAIL"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_LIGHTING_QUALITY_DETAIL(ParamRow):
    LocalLightDistFactor: float = ParamField(
        float32, "localLightDistFactor", default=0.75,
        tooltip="TOOLTIP-TODO",
    )
    LocalLightShadowEnabled: int = ParamField(
        uint8, "localLightShadowEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    ForwardPassLightingEnabled: int = ParamField(
        uint8, "forwardPassLightingEnabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    LocalLightShadowSpecLevelMax: int = ParamField(
        uint8, "localLightShadowSpecLevelMax", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "dmy[1]")
