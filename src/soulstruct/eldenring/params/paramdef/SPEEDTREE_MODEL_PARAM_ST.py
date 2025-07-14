from __future__ import annotations

__all__ = ["SPEEDTREE_MODEL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class SPEEDTREE_MODEL_PARAM_ST(ParamRow):
    MinFadeLeaf: float = ParamField(
        float, "MinFadeLeaf", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MinFadeFrond: float = ParamField(
        float, "MinFadeFrond", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MinFadeBranch: float = ParamField(
        float, "MinFadeBranch", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MinTranslucencyLeaf: float = ParamField(
        float, "MinTranslucencyLeaf", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxTranslucencyLeaf: float = ParamField(
        float, "MaxTranslucencyLeaf", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    MinTranslucencyFrond: float = ParamField(
        float, "MinTranslucencyFrond", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxTranslucencyFrond: float = ParamField(
        float, "MaxTranslucencyFrond", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    MinTranslucencyBranch: float = ParamField(
        float, "MinTranslucencyBranch", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxTranslucencyBranch: float = ParamField(
        float, "MaxTranslucencyBranch", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    BillboardBackSpecularWeakenParam: float = ParamField(
        float, "BillboardBackSpecularWeakenParam", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
