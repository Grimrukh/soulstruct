from __future__ import annotations

__all__ = ["SPEEDTREE_MODEL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class SPEEDTREE_MODEL_PARAM_ST(ParamRow):
    MinFadeLeaf: float = ParamField(
        float32, "MinFadeLeaf", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MinFadeFrond: float = ParamField(
        float32, "MinFadeFrond", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MinFadeBranch: float = ParamField(
        float32, "MinFadeBranch", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MinTranslucencyLeaf: float = ParamField(
        float32, "MinTranslucencyLeaf", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxTranslucencyLeaf: float = ParamField(
        float32, "MaxTranslucencyLeaf", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    MinTranslucencyFrond: float = ParamField(
        float32, "MinTranslucencyFrond", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxTranslucencyFrond: float = ParamField(
        float32, "MaxTranslucencyFrond", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    MinTranslucencyBranch: float = ParamField(
        float32, "MinTranslucencyBranch", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MaxTranslucencyBranch: float = ParamField(
        float32, "MaxTranslucencyBranch", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    BillboardBackSpecularWeakenParam: float = ParamField(
        float32, "BillboardBackSpecularWeakenParam", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
