from __future__ import annotations

__all__ = ["CUTSCENE_WEATHER_OVERRIDE_GPARAM_ID_CONVERT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class CUTSCENE_WEATHER_OVERRIDE_GPARAM_ID_CONVERT_PARAM_ST(ParamRowData):
    WeatherOverrideGparamId: int = ParamField(
        uint, "weatherOverrideGparamId", default=0,
        tooltip="TOOLTIP-TODO",
    )
