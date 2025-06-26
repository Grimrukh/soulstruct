from __future__ import annotations

__all__ = ["CS_SSAO_QUALITY_DETAIL"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class CS_SSAO_QUALITY_DETAIL(ParamRow):
    Enabled: int = ParamField(
        byte, "enabled", ON_OFF, default=1,
        tooltip="TOOLTIP-TODO",
    )
    CsreprojEnabledType: int = ParamField(
        byte, "cs_reprojEnabledType", CS_GCONFIG_ENABLED_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    CsupScaleEnabledType: int = ParamField(
        byte, "cs_upScaleEnabledType", CS_GCONFIG_ENABLED_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CsuseNormalEnabledType: int = ParamField(
        byte, "cs_useNormalEnabledType", CS_GCONFIG_ENABLED_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "dmy[1]")
