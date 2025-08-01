from __future__ import annotations

__all__ = ["CUTSCENE_WEATHER_OVERRIDE_GPARAM_ID_CONVERT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class CUTSCENE_WEATHER_OVERRIDE_GPARAM_ID_CONVERT_PARAM_ST(ParamRow):
    WeatherOverrideGparamId: int = ParamField(
        uint32, "weatherOverrideGparamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
