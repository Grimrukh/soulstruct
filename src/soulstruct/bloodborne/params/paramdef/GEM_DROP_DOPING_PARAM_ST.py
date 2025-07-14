from __future__ import annotations

__all__ = ["GEM_DROP_DOPING_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class GEM_DROP_DOPING_PARAM_ST(ParamRow):
    MinimumRank: int = ParamField(
        int32, "rankMin", default=0,
        tooltip="TODO",
    )
    MaximumRank: int = ParamField(
        int32, "rankMax", default=0,
        tooltip="TODO",
    )
    NormalDistributionMean: int = ParamField(
        int32, "normalDistributionAve", default=0,
        tooltip="TODO",
    )
    NormalDistributionSigma: int = ParamField(
        int32, "normalDistributionSigma", default=1,
        tooltip="TODO",
    )
    SlotTypeRateA: float = ParamField(
        float32, "slotTypeRateA", default=1.0,
        tooltip="TODO",
    )
    SlotTypeRateB: float = ParamField(
        float32, "slotTypeRateB", default=1.0,
        tooltip="TODO",
    )
    SlotTypeRateC: float = ParamField(
        float32, "slotTypeRateC", default=1.0,
        tooltip="TODO",
    )
    SlotTypeRateD: float = ParamField(
        float32, "slotTypeRateD", default=1.0,
        tooltip="TODO",
    )
    SlotTypeRateE: float = ParamField(
        float32, "slotTypeRateE", default=1.0,
        tooltip="TODO",
    )
    SlotTypeRateF: float = ParamField(
        float32, "slotTypeRateF", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate0: float = ParamField(
        float32, "directionalIdRate_0", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate1: float = ParamField(
        float32, "directionalIdRate_1", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate2: float = ParamField(
        float32, "directionalIdRate_2", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate3: float = ParamField(
        float32, "directionalIdRate_3", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate4: float = ParamField(
        float32, "directionalIdRate_4", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate5: float = ParamField(
        float32, "directionalIdRate_5", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate6: float = ParamField(
        float32, "directionalIdRate_6", default=1.0,
        tooltip="TODO",
    )
    DirectionalIDRate7: float = ParamField(
        float32, "directionalIdRate_7", default=1.0,
        tooltip="TODO",
    )
